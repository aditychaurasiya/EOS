import pandas as pd
from datetime import datetime
import os


class OutputBuilder:

    def __init__(self, solver, input_data):
        self.solver = solver
        self.input_data = input_data
        self.output_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Output'))
        # Create output directory if it doesn't exist
        os.makedirs(self.output_path, exist_ok=True)

    def generate_all_outputs(self):
        """Generate all output files and console display"""
        print("=" * 80)
        print("EARTH OBSERVATION SCHEDULING - OPTIMIZATION RESULTS")
        print("=" * 80)

        # Display optimization summary
        self.display_optimization_summary()

        # Generate detailed outputs
        self.generate_observation_schedule()
        self.generate_downlink_schedule()
        self.generate_satellite_utilization()
        self.generate_target_analysis()
        self.generate_memory_tracking()
        self.generate_power_tracking()
        self.generate_resource_timeline()
        self.generate_summary_report()

        print("\n" + "=" * 80)
        print("All output files generated successfully in 'Output/' directory")
        print("=" * 80)

    def display_optimization_summary(self):
        """Display high-level optimization results"""
        print(f"\n{'OPTIMIZATION SUMMARY':<30}")
        print("-" * 50)

        if hasattr(self.solver.eos_model, 'objVal'):
            print(f"{'Objective Value:':<25} {self.solver.eos_model.objVal:.2f}")
            print(f"{'Status:':<25} {'Optimal' if self.solver.eos_model.status == 2 else 'Not Optimal'}")
        else:
            print("Model not solved or no solution available")
            return

        # Count scheduled observations
        total_observations = sum(1 for (s, t, k), var in self.solver.x.items()
                                 if var.x > 0.5)

        # Count scheduled downlinks
        total_downlinks = sum(1 for (s, g, k), var in self.solver.y.items()
                              if var.x > 0.5)

        # Calculate total data downlinked
        total_data_downlinked = sum(self.solver.d[s, g, k].x
                                    for (s, g, k), var in self.solver.y.items()
                                    if var.x > 0.5 and (s, g, k) in self.solver.d)

        # Count unique targets observed
        observed_targets = set()
        for (s, t, k), var in self.solver.x.items():
            if var.x > 0.5:
                observed_targets.add(t)

        print(f"{'Total Observations:':<25} {total_observations}")
        print(f"{'Unique Targets Observed:':<25} {len(observed_targets)}")
        print(f"{'Total Downlinks:':<25} {total_downlinks}")
        print(f"{'Total Data Downlinked:':<25} {total_data_downlinked:.2f} GB")
        print(
            f"{'Target Coverage:':<25} {len(observed_targets)}/{len(self.input_data.target)} ({100 * len(observed_targets) / len(self.input_data.target):.1f}%)")

    def generate_observation_schedule(self):
        """Generate detailed observation schedule"""
        observations = []

        for (s, t, k), var in self.solver.x.items():
            if var.x > 0.5:  # Variable is selected
                target_obj = self.input_data.target[t]
                satellite_obj = self.input_data.statellite[s]

                # Get power level at observation time
                power_level = self.solver.p[s, k].x if (s, k) in self.solver.p else 0

                observations.append({
                    'Satellite ID': s,
                    'Target ID': t,
                    'Time Slot': k,
                    'Target Urgency': target_obj.urgency,
                    'Target Importance': target_obj.importance,
                    'Weighted Value': target_obj.urgency * target_obj.importance,
                    'Target Latitude': target_obj.lat,
                    'Target Longitude': target_obj.lon,
                    'Satellite Orbit': satellite_obj.orbit,
                    'Power Level (Wh)': round(power_level, 2),
                    'Power Consumed (Wh)': self.solver.power_per_obs
                })

        # Sort by time slot then by satellite
        observations.sort(key=lambda x: (x['Time Slot'], x['Satellite ID']))

        # Create DataFrame and save
        obs_df = pd.DataFrame(observations)
        obs_df.to_csv(os.path.join(self.output_path, 'observation_schedule.csv'), index=False)

        # Display summary
        print(f"\n{'OBSERVATION SCHEDULE':<30}")
        print("-" * 50)
        print(f"Total scheduled observations: {len(observations)}")

        if observations:
            print(
                f"Time range: {min(obs['Time Slot'] for obs in observations)} to {max(obs['Time Slot'] for obs in observations)}")
            print(f"Satellites involved: {len(set(obs['Satellite ID'] for obs in observations))}")
            print(f"Total power consumed: {sum(obs['Power Consumed (Wh)'] for obs in observations)} Wh")
            print("Saved to: observation_schedule.csv")

    def generate_downlink_schedule(self):
        """Generate detailed downlink schedule"""
        downlinks = []

        for (s, g, k), var in self.solver.y.items():
            if var.x > 0.5:  # Variable is selected
                satellite_obj = self.input_data.statellite[s]
                gs_obj = self.input_data.groudstation[g]

                # Get actual data transferred
                data_transferred = self.solver.d[s, g, k].x if (s, g, k) in self.solver.d else 0

                # Get power level and memory at downlink time
                power_level = self.solver.p[s, k].x if (s, k) in self.solver.p else 0
                memory_before = self.solver.m[s, k].x if (s, k) in self.solver.m else 0

                # Calculate power consumed
                power_consumed = data_transferred * self.solver.power_per_downlink

                downlinks.append({
                    'Satellite ID': s,
                    'Ground Station ID': g,
                    'Time Slot': k,
                    'Data Transferred (GB)': round(data_transferred, 2),
                    'Max Data Rate (GB/slot)': gs_obj.max_data_rate,
                    'Ground Station Location': gs_obj.location,
                    'Memory Before (GB)': round(memory_before, 2),
                    'Memory After (GB)': round(memory_before - data_transferred, 2),
                    'Power Level (Wh)': round(power_level, 2),
                    'Power Consumed (Wh)': round(power_consumed, 2)
                })

        # Sort by time slot then by satellite
        downlinks.sort(key=lambda x: (x['Time Slot'], x['Satellite ID']))

        # Create DataFrame and save
        downlink_df = pd.DataFrame(downlinks)
        downlink_df.to_csv(os.path.join(self.output_path, 'downlink_schedule.csv'), index=False)

        # Display summary
        print(f"\n{'DOWNLINK SCHEDULE':<30}")
        print("-" * 50)
        print(f"Total scheduled downlinks: {len(downlinks)}")

        if downlinks:
            print(f"Ground stations used: {len(set(dl['Ground Station ID'] for dl in downlinks))}")
            total_data = sum(dl['Data Transferred (GB)'] for dl in downlinks)
            total_power = sum(dl['Power Consumed (Wh)'] for dl in downlinks)
            print(f"Total data transferred: {total_data:.2f} GB")
            print(f"Total power consumed: {total_power:.2f} Wh")
            print("Saved to: downlink_schedule.csv")

    def generate_satellite_utilization(self):
        """Generate satellite utilization analysis"""
        satellite_stats = []

        for s in self.input_data.statellite:
            satellite_obj = self.input_data.statellite[s]

            # Count observations for this satellite
            obs_count = sum(1 for (sat, t, k), var in self.solver.x.items()
                            if sat == s and var.x > 0.5)

            # Count downlinks for this satellite
            downlink_count = sum(1 for (sat, g, k), var in self.solver.y.items()
                                 if sat == s and var.x > 0.5)

            # Calculate total data downlinked
            total_data_down = sum(self.solver.d[sat, g, k].x
                                  for (sat, g, k), var in self.solver.y.items()
                                  if sat == s and var.x > 0.5 and (sat, g, k) in self.solver.d)

            # Calculate utilization percentage
            max_possible_obs = satellite_obj.max_obs_per_day * 7
            utilization_percent = (obs_count / max_possible_obs) * 100 if max_possible_obs > 0 else 0

            # Get unique targets observed
            targets_observed = set()
            for (sat, t, k), var in self.solver.x.items():
                if sat == s and var.x > 0.5:
                    targets_observed.add(t)

            # Get final power and memory levels
            final_slot = self.solver.combined_slots[-1]
            final_power = self.solver.p[s, final_slot].x if (s, final_slot) in self.solver.p else 0
            final_memory = self.solver.m[s, final_slot].x if (s, final_slot) in self.solver.m else 0

            satellite_stats.append({
                'Satellite ID': s,
                'Orbit': satellite_obj.orbit,
                'Memory Capacity (GB)': satellite_obj.memory_capacity,
                'Max Obs/Day': satellite_obj.max_obs_per_day,
                'Total Observations': obs_count,
                'Unique Targets': len(targets_observed),
                'Total Downlinks': downlink_count,
                'Data Downlinked (GB)': round(total_data_down, 2),
                'Final Memory (GB)': round(final_memory, 2),
                'Final Power (Wh)': round(final_power, 2),
                'Utilization (%)': round(utilization_percent, 1),
                'Status': 'Active' if obs_count > 0 else 'Idle'
            })

        # Sort by utilization percentage (descending)
        satellite_stats.sort(key=lambda x: x['Utilization (%)'], reverse=True)

        # Create DataFrame and save
        sat_df = pd.DataFrame(satellite_stats)
        sat_df.to_csv(os.path.join(self.output_path, 'satellite_utilization.csv'), index=False)

        # Display summary
        print(f"\n{'SATELLITE UTILIZATION':<30}")
        print("-" * 50)
        active_satellites = sum(1 for stat in satellite_stats if stat['Status'] == 'Active')
        avg_utilization = sum(stat['Utilization (%)'] for stat in satellite_stats) / len(satellite_stats)

        print(f"Active satellites: {active_satellites}/{len(satellite_stats)}")
        print(f"Average utilization: {avg_utilization:.1f}%")

        if satellite_stats:
            best_sat = satellite_stats[0]
            print(f"Best utilized: {best_sat['Satellite ID']} ({best_sat['Utilization (%)']}%)")
            print("Saved to: satellite_utilization.csv")

    def generate_target_analysis(self):
        """Generate target observation analysis"""
        target_stats = []

        for t in self.input_data.target:
            target_obj = self.input_data.target[t]

            # Check if target was observed
            observed = False
            observing_satellite = None
            observation_time = None

            for (s, tar, k), var in self.solver.x.items():
                if tar == t and var.x > 0.5:
                    observed = True
                    observing_satellite = s
                    observation_time = k
                    break

            target_stats.append({
                'Target ID': t,
                'Latitude': target_obj.lat,
                'Longitude': target_obj.lon,
                'Urgency': target_obj.urgency,
                'Importance': target_obj.importance,
                'Weighted Value': target_obj.urgency * target_obj.importance,
                'Observed': 'Yes' if observed else 'No',
                'Observing Satellite': observing_satellite if observed else 'None',
                'Observation Time': observation_time if observed else 'None',
                'Priority Level': self._get_priority_level(target_obj.urgency, target_obj.importance)
            })

        # Sort by weighted value (descending)
        target_stats.sort(key=lambda x: x['Weighted Value'], reverse=True)

        # Create DataFrame and save
        target_df = pd.DataFrame(target_stats)
        target_df.to_csv(os.path.join(self.output_path, 'target_analysis.csv'), index=False)

        # Display summary
        print(f"\n{'TARGET ANALYSIS':<30}")
        print("-" * 50)
        observed_count = sum(1 for stat in target_stats if stat['Observed'] == 'Yes')
        coverage = (observed_count / len(target_stats)) * 100

        print(f"Targets observed: {observed_count}/{len(target_stats)} ({coverage:.1f}%)")

        # Priority analysis
        high_priority = sum(
            1 for stat in target_stats if stat['Priority Level'] == 'High' and stat['Observed'] == 'Yes')
        total_high_priority = sum(1 for stat in target_stats if stat['Priority Level'] == 'High')

        if total_high_priority > 0:
            high_priority_coverage = (high_priority / total_high_priority) * 100
            print(f"High priority coverage: {high_priority}/{total_high_priority} ({high_priority_coverage:.1f}%)")

        print("Saved to: target_analysis.csv")

    def generate_memory_tracking(self):
        """Generate satellite memory usage tracking"""
        memory_data = []

        for s in self.input_data.statellite:
            satellite_obj = self.input_data.statellite[s]

            for k in self.solver.combined_slots:
                if (s, k) in self.solver.m:
                    memory_level = self.solver.m[s, k].x

                    # Check for observations in this time slot
                    observations_this_slot = sum(1 for (sat, t, slot), var in self.solver.x.items()
                                                 if sat == s and slot == k and var.x > 0.5)

                    # Check for downlinks and get actual data transferred
                    data_downlinked = sum(self.solver.d[sat, g, slot].x
                                          for (sat, g, slot), var in self.solver.y.items()
                                          if sat == s and slot == k and var.x > 0.5 and (sat, g, slot) in self.solver.d)

                    memory_data.append({
                        'Satellite ID': s,
                        'Time Slot': k,
                        'Memory Level (GB)': round(memory_level, 2),
                        'Memory Capacity (GB)': satellite_obj.memory_capacity,
                        'Memory Usage (%)': round((memory_level / satellite_obj.memory_capacity) * 100, 1),
                        'Observations This Slot': observations_this_slot,
                        'Data Added (GB)': observations_this_slot * self.solver.data_per_obs,
                        'Data Downlinked (GB)': round(data_downlinked, 2),
                        'Status': 'Near Full' if memory_level > 0.8 * satellite_obj.memory_capacity else 'Normal'
                    })

        # Sort by satellite and time slot
        memory_data.sort(key=lambda x: (x['Satellite ID'], x['Time Slot']))

        # Create DataFrame and save
        memory_df = pd.DataFrame(memory_data)
        memory_df.to_csv(os.path.join(self.output_path, 'memory_tracking.csv'), index=False)

        # Display summary
        print(f"\n{'MEMORY TRACKING':<30}")
        print("-" * 50)
        if memory_data:
            max_usage = max(entry['Memory Usage (%)'] for entry in memory_data)
            near_full_instances = sum(1 for entry in memory_data if entry['Status'] == 'Near Full')

            print(f"Maximum memory usage: {max_usage:.1f}%")
            print(f"Near-full instances: {near_full_instances}")
            print("Saved to: memory_tracking.csv")

    def generate_power_tracking(self):
        """Generate satellite power usage tracking"""
        power_data = []

        for s in self.input_data.statellite:
            for k in self.solver.combined_slots:
                if (s, k) in self.solver.p:
                    power_level = self.solver.p[s, k].x

                    # Check for observations
                    observations_this_slot = sum(1 for (sat, t, slot), var in self.solver.x.items()
                                                 if sat == s and slot == k and var.x > 0.5)

                    # Check for downlinks and calculate power consumed
                    data_downlinked = sum(self.solver.d[sat, g, slot].x
                                          for (sat, g, slot), var in self.solver.y.items()
                                          if sat == s and slot == k and var.x > 0.5 and (sat, g, slot) in self.solver.d)

                    # Check if recharging
                    is_recharging = self.solver.recharge_window.get((s, k), 0) == 1

                    power_consumed_obs = observations_this_slot * self.solver.power_per_obs
                    power_consumed_dl = data_downlinked * self.solver.power_per_downlink
                    power_recharged = self.solver.charge_rate_per_slot if is_recharging else 0

                    power_data.append({
                        'Satellite ID': s,
                        'Time Slot': k,
                        'Power Level (Wh)': round(power_level, 2),
                        'Power Capacity (Wh)': self.solver.power_capacity,
                        'Power Usage (%)': round((power_level / self.solver.power_capacity) * 100, 1),
                        'Observations': observations_this_slot,
                        'Power Consumed Obs (Wh)': round(power_consumed_obs, 2),
                        'Power Consumed DL (Wh)': round(power_consumed_dl, 2),
                        'Power Recharged (Wh)': round(power_recharged, 2),
                        'Recharging': 'Yes' if is_recharging else 'No',
                        'Status': 'Low' if power_level < 0.2 * self.solver.power_capacity else 'Normal'
                    })

        # Sort by satellite and time slot
        power_data.sort(key=lambda x: (x['Satellite ID'], x['Time Slot']))

        # Create DataFrame and save
        power_df = pd.DataFrame(power_data)
        power_df.to_csv(os.path.join(self.output_path, 'power_tracking.csv'), index=False)

        # Display summary
        print(f"\n{'POWER TRACKING':<30}")
        print("-" * 50)
        if power_data:
            min_power = min(entry['Power Usage (%)'] for entry in power_data)
            low_power_instances = sum(1 for entry in power_data if entry['Status'] == 'Low')
            recharge_events = sum(1 for entry in power_data if entry['Recharging'] == 'Yes')

            print(f"Minimum power level: {min_power:.1f}%")
            print(f"Low power instances: {low_power_instances}")
            print(f"Recharge events: {recharge_events}")
            print("Saved to: power_tracking.csv")

    def generate_resource_timeline(self):
        """Generate combined resource timeline for visualization"""
        timeline_data = []

        for s in self.input_data.statellite:
            for k in self.solver.combined_slots:
                memory_level = self.solver.m[s, k].x if (s, k) in self.solver.m else 0
                power_level = self.solver.p[s, k].x if (s, k) in self.solver.p else 0

                # Check activities
                observing = sum(1 for (sat, t, slot), var in self.solver.x.items()
                                if sat == s and slot == k and var.x > 0.5) > 0
                downlinking = sum(1 for (sat, g, slot), var in self.solver.y.items()
                                  if sat == s and slot == k and var.x > 0.5) > 0
                recharging = self.solver.recharge_window.get((s, k), 0) == 1

                activity = 'Idle'
                if observing:
                    activity = 'Observing'
                elif downlinking:
                    activity = 'Downlinking'
                elif recharging:
                    activity = 'Recharging'

                timeline_data.append({
                    'Satellite ID': s,
                    'Time Slot': k,
                    'Activity': activity,
                    'Memory (GB)': round(memory_level, 2),
                    'Memory (%)': round((memory_level / self.input_data.statellite[s].memory_capacity) * 100, 1),
                    'Power (Wh)': round(power_level, 2),
                    'Power (%)': round((power_level / self.solver.power_capacity) * 100, 1)
                })

        timeline_data.sort(key=lambda x: (x['Satellite ID'], x['Time Slot']))

        timeline_df = pd.DataFrame(timeline_data)
        timeline_df.to_csv(os.path.join(self.output_path, 'resource_timeline.csv'), index=False)

        print(f"\n{'RESOURCE TIMELINE':<30}")
        print("-" * 50)
        print("Combined memory and power timeline generated")
        print("Saved to: resource_timeline.csv")

    def generate_summary_report(self):
        """Generate executive summary report"""
        summary_lines = []
        summary_lines.append("EARTH OBSERVATION SCHEDULING - EXECUTIVE SUMMARY")
        summary_lines.append("=" * 60)
        summary_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        summary_lines.append("")

        # Optimization Results
        if hasattr(self.solver.eos_model, 'objVal'):
            summary_lines.append("OPTIMIZATION RESULTS:")
            summary_lines.append(f"  Objective Value: {self.solver.eos_model.objVal:.2f}")
            summary_lines.append(
                f"  Solution Status: {'Optimal' if self.solver.eos_model.status == 2 else 'Not Optimal'}")
            summary_lines.append("")

        # Mission Statistics
        total_observations = sum(1 for (s, t, k), var in self.solver.x.items() if var.x > 0.5)
        observed_targets = set(t for (s, t, k), var in self.solver.x.items() if var.x > 0.5)
        total_downlinks = sum(1 for (s, g, k), var in self.solver.y.items() if var.x > 0.5)
        total_data = sum(self.solver.d[s, g, k].x for (s, g, k), var in self.solver.y.items()
                         if var.x > 0.5 and (s, g, k) in self.solver.d)

        summary_lines.append("MISSION STATISTICS:")
        summary_lines.append(f"  Total Observations Scheduled: {total_observations}")
        summary_lines.append(f"  Unique Targets Observed: {len(observed_targets)}")
        summary_lines.append(f"  Target Coverage: {100 * len(observed_targets) / len(self.input_data.target):.1f}%")
        summary_lines.append(f"  Total Downlinks Scheduled: {total_downlinks}")
        summary_lines.append(f"  Total Data Downlinked: {total_data:.2f} GB")
        summary_lines.append("")

        # Resource Utilization
        active_satellites = sum(1 for s in self.input_data.statellite
                                if any(var.x > 0.5 for (sat, t, k), var in self.solver.x.items() if sat == s))

        summary_lines.append("RESOURCE UTILIZATION:")
        summary_lines.append(f"  Active Satellites: {active_satellites}/{len(self.input_data.statellite)}")
        summary_lines.append(
            f"  Ground Stations Used: {len(set(g for (s, g, k), var in self.solver.y.items() if var.x > 0.5))}/{len(self.input_data.groudstation)}")
        summary_lines.append("")

        # Value Analysis
        total_weighted_value = sum(
            self.input_data.target[t].urgency * self.input_data.target[t].importance
            for (s, t, k), var in self.solver.x.items() if var.x > 0.5
        )

        summary_lines.append("VALUE ANALYSIS:")
        summary_lines.append(f"  Total Weighted Value Captured: {total_weighted_value}")

        if observed_targets:
            avg_urgency = sum(self.input_data.target[t].urgency for t in observed_targets) / len(observed_targets)
            avg_importance = sum(self.input_data.target[t].importance for t in observed_targets) / len(observed_targets)
            summary_lines.append(f"  Average Target Urgency: {avg_urgency:.2f}")
            summary_lines.append(f"  Average Target Importance: {avg_importance:.2f}")

        summary_lines.append("")
        summary_lines.append("OUTPUT FILES GENERATED:")
        summary_lines.append("  - observation_schedule.csv")
        summary_lines.append("  - downlink_schedule.csv")
        summary_lines.append("  - satellite_utilization.csv")
        summary_lines.append("  - target_analysis.csv")
        summary_lines.append("  - memory_tracking.csv")
        summary_lines.append("  - power_tracking.csv")
        summary_lines.append("  - resource_timeline.csv")
        summary_lines.append("  - summary_report.txt")

        # Save summary report
        with open(os.path.join(self.output_path, 'summary_report.txt'), 'w') as f:
            f.write('\n'.join(summary_lines))

        # Display key points
        print(f"\n{'SUMMARY REPORT':<30}")
        print("-" * 50)
        print(f"Total weighted value: {total_weighted_value}")
        print(f"Total data downlinked: {total_data:.2f} GB")
        print(f"Mission efficiency: {100 * len(observed_targets) / len(self.input_data.target):.1f}% target coverage")
        print("Saved to: summary_report.txt")

    def _get_priority_level(self, urgency, importance):
        """Determine priority level based on urgency and importance"""
        weighted_value = urgency * importance
        if weighted_value >= 30:
            return 'High'
        elif weighted_value >= 15:
            return 'Medium'
        else:
            return 'Low'
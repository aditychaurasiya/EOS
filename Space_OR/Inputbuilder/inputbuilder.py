import pandas as pd

from Entities.Downlink import Downlink
from Entities.GroundStation import GroundStation
from Entities.Statellite import Statellite
from Entities.Target import Target
from Entities.Visual_Time_Window import Visual_Time_Window

class Inputbuilder:

    def __init__(self):
        self.downlink = {}
        self.groudstation = {}
        self.statellite = {}
        self.target = {}
        self.vtw = {}
        self.path = 'Data\\'

    def build(self):
        self.read_downlink_data(self.path + "Downlink.csv")
        self.read_groundstation_data(self.path + "GroundStation.csv")
        self.read_statellite_data(self.path + "Satellite.csv")
        self.read_target_data(self.path + "Target.csv")
        self.read_vtw_data(self.path + "VTW.csv")

    def read_downlink_data(self, file_name):
        downlink_df = pd.read_csv(file_name)

        for index, row in downlink_df.iterrows():
            time_slot_start = row['Time Slot'].split('–')[0].strip()
            time_slot_end = row['Time Slot'].split('–')[1].strip()
            satellite_id = row['Satellite ID']
            groundstation_id = row['Ground Station ID']
            duration = row['Duration (min)']
            max_data = row['Max Data (GB)']

            # Downlink constructor: (timeSlotStart, timeSlotEnd, satelliteid, groundstationid, duration, max_data)
            downlink_obj = Downlink(time_slot_start, time_slot_end, satellite_id, groundstation_id, duration, max_data)
            self.downlink[len(self.downlink)] = downlink_obj

    def read_groundstation_data(self, file_name):
        groundstation_df = pd.read_csv(file_name)

        for index, row in groundstation_df.iterrows():
            station_id = row['Station ID']
            location = row['Location (Lat, Lon)']
            max_data_rate = row['Max Data Rate (GB/slot)']

            # GroundStation constructor: (stationid, location, max_data_rate)
            groundstation_obj = GroundStation(station_id, location, max_data_rate)
            self.groudstation[station_id] = groundstation_obj

    def read_statellite_data(self, file_name):
        statellite_df = pd.read_csv(file_name)

        for index, row in statellite_df.iterrows():
            satellite_id = row['Satellite ID']
            orbit = row['Orbit']
            memory_capacity = row['Memory Capacity (GB)']
            max_obs_per_day = row['Max Observations/Day']

            # Statellite constructor: (satelliteid, orbit, memory_capacity, max_obs_per_day)
            statellite_obj = Statellite(satellite_id, orbit, memory_capacity, max_obs_per_day)
            self.statellite[satellite_id] = statellite_obj

    def read_target_data(self, file_name):
        target_df = pd.read_csv(file_name)

        for index, row in target_df.iterrows():
            target_id = row['Target ID']
            lat = row['Latitude (°N)']
            lon = row['Longitude (°E)']
            urgency = row['Urgency']
            importance = row['Importance']

            # Target constructor: (target_id, lat, lon, urgency, importance)
            target_obj = Target(target_id, lat, lon, urgency, importance)
            self.target[target_id] = target_obj

    def read_vtw_data(self, file_name):
        vtw_df = pd.read_csv(file_name)

        for index, row in vtw_df.iterrows():
            time_slot_start = row['Time Slot '].split('–')[0].strip()
            time_slot_end = row['Time Slot '].split('–')[1].strip()
            satellite_id = row['Satellite ID']
            target_id = row['Target ID']
            duration = row['Duration (min)']

            # Visual_Time_Window constructor: (timeSlotStart, timeSlotEnd, satelliteid, target_id, duration)
            vtw_obj = Visual_Time_Window(time_slot_start, time_slot_end, satellite_id, target_id, duration)
            self.vtw[len(self.vtw)] = vtw_obj

    def _create_time_slot_mapping(self):
        # Create time slot mappings for both VTW and downlink slots
        time_slots = set()  # For VTW time slots
        dl_time_slots = set()  # For downlink time slots

        # Add VTW time slots
        for vtw in self.vtw.values():
            time_slot = vtw.timeSlotStart.strip()
            time_slots.add(time_slot)

        # Add downlink time slots
        for dl in self.downlink.values():
            time_slot = dl.timeSlotStart.strip()
            dl_time_slots.add(time_slot)

        # Convert to sorted lists for consistent ordering
        return sorted(list(time_slots)), sorted(list(dl_time_slots))



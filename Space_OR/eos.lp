\ Model Earth_Observation_Scheduling
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  21 x_S1_T1_0000 + 21 x_S1_T1_0005 + 21 x_S1_T1_0130 + 45 x_S1_T2_0000
   + 45 x_S1_T2_0005 + 45 x_S1_T2_0130 + 8 x_S1_T3_0000 + 8 x_S1_T3_0005
   + 8 x_S1_T3_0130 + 32 x_S1_T4_0000 + 32 x_S1_T4_0005 + 32 x_S1_T4_0130
   + 3 x_S1_T5_0000 + 3 x_S1_T5_0005 + 3 x_S1_T5_0130 + 21 x_S2_T1_0000
   + 21 x_S2_T1_0005 + 21 x_S2_T1_0130 + 45 x_S2_T2_0000 + 45 x_S2_T2_0005
   + 45 x_S2_T2_0130 + 8 x_S2_T3_0000 + 8 x_S2_T3_0005 + 8 x_S2_T3_0130
   + 32 x_S2_T4_0000 + 32 x_S2_T4_0005 + 32 x_S2_T4_0130 + 3 x_S2_T5_0000
   + 3 x_S2_T5_0005 + 3 x_S2_T5_0130 + 21 x_S3_T1_0000 + 21 x_S3_T1_0005
   + 21 x_S3_T1_0130 + 45 x_S3_T2_0000 + 45 x_S3_T2_0005 + 45 x_S3_T2_0130
   + 8 x_S3_T3_0000 + 8 x_S3_T3_0005 + 8 x_S3_T3_0130 + 32 x_S3_T4_0000
   + 32 x_S3_T4_0005 + 32 x_S3_T4_0130 + 3 x_S3_T5_0000 + 3 x_S3_T5_0005
   + 3 x_S3_T5_0130 + 21 x_S4_T1_0000 + 21 x_S4_T1_0005 + 21 x_S4_T1_0130
   + 45 x_S4_T2_0000 + 45 x_S4_T2_0005 + 45 x_S4_T2_0130 + 8 x_S4_T3_0000
   + 8 x_S4_T3_0005 + 8 x_S4_T3_0130 + 32 x_S4_T4_0000 + 32 x_S4_T4_0005
   + 32 x_S4_T4_0130 + 3 x_S4_T5_0000 + 3 x_S4_T5_0005 + 3 x_S4_T5_0130
   + 21 x_S5_T1_0000 + 21 x_S5_T1_0005 + 21 x_S5_T1_0130 + 45 x_S5_T2_0000
   + 45 x_S5_T2_0005 + 45 x_S5_T2_0130 + 8 x_S5_T3_0000 + 8 x_S5_T3_0005
   + 8 x_S5_T3_0130 + 32 x_S5_T4_0000 + 32 x_S5_T4_0005 + 32 x_S5_T4_0130
   + 3 x_S5_T5_0000 + 3 x_S5_T5_0005 + 3 x_S5_T5_0130 + 0.1 d_S1_GS1_0015
   + 0.1 d_S1_GS1_0200 + 0.1 d_S1_GS2_0015 + 0.1 d_S1_GS2_0200
   + 0.1 d_S1_GS3_0015 + 0.1 d_S1_GS3_0200 + 0.1 d_S1_GS4_0015
   + 0.1 d_S1_GS4_0200 + 0.1 d_S1_GS5_0015 + 0.1 d_S1_GS5_0200
   + 0.1 d_S2_GS1_0015 + 0.1 d_S2_GS1_0200 + 0.1 d_S2_GS2_0015
   + 0.1 d_S2_GS2_0200 + 0.1 d_S2_GS3_0015 + 0.1 d_S2_GS3_0200
   + 0.1 d_S2_GS4_0015 + 0.1 d_S2_GS4_0200 + 0.1 d_S2_GS5_0015
   + 0.1 d_S2_GS5_0200 + 0.1 d_S3_GS1_0015 + 0.1 d_S3_GS1_0200
   + 0.1 d_S3_GS2_0015 + 0.1 d_S3_GS2_0200 + 0.1 d_S3_GS3_0015
   + 0.1 d_S3_GS3_0200 + 0.1 d_S3_GS4_0015 + 0.1 d_S3_GS4_0200
   + 0.1 d_S3_GS5_0015 + 0.1 d_S3_GS5_0200 + 0.1 d_S4_GS1_0015
   + 0.1 d_S4_GS1_0200 + 0.1 d_S4_GS2_0015 + 0.1 d_S4_GS2_0200
   + 0.1 d_S4_GS3_0015 + 0.1 d_S4_GS3_0200 + 0.1 d_S4_GS4_0015
   + 0.1 d_S4_GS4_0200 + 0.1 d_S4_GS5_0015 + 0.1 d_S4_GS5_0200
   + 0.1 d_S5_GS1_0015 + 0.1 d_S5_GS1_0200 + 0.1 d_S5_GS2_0015
   + 0.1 d_S5_GS2_0200 + 0.1 d_S5_GS3_0015 + 0.1 d_S5_GS3_0200
   + 0.1 d_S5_GS4_0015 + 0.1 d_S5_GS4_0200 + 0.1 d_S5_GS5_0015
   + 0.1 d_S5_GS5_0200
Subject To
 vtw_constraint[S1,T1,00_00]: x_S1_T1_0000 <= 1
 vtw_constraint[S1,T1,00_05]: x_S1_T1_0005 <= 0
 vtw_constraint[S1,T1,01_30]: x_S1_T1_0130 <= 0
 vtw_constraint[S1,T2,00_00]: x_S1_T2_0000 <= 0
 vtw_constraint[S1,T2,00_05]: x_S1_T2_0005 <= 0
 vtw_constraint[S1,T2,01_30]: x_S1_T2_0130 <= 0
 vtw_constraint[S1,T3,00_00]: x_S1_T3_0000 <= 0
 vtw_constraint[S1,T3,00_05]: x_S1_T3_0005 <= 0
 vtw_constraint[S1,T3,01_30]: x_S1_T3_0130 <= 0
 vtw_constraint[S1,T4,00_00]: x_S1_T4_0000 <= 0
 vtw_constraint[S1,T4,00_05]: x_S1_T4_0005 <= 0
 vtw_constraint[S1,T4,01_30]: x_S1_T4_0130 <= 1
 vtw_constraint[S1,T5,00_00]: x_S1_T5_0000 <= 0
 vtw_constraint[S1,T5,00_05]: x_S1_T5_0005 <= 0
 vtw_constraint[S1,T5,01_30]: x_S1_T5_0130 <= 0
 vtw_constraint[S2,T1,00_00]: x_S2_T1_0000 <= 0
 vtw_constraint[S2,T1,00_05]: x_S2_T1_0005 <= 0
 vtw_constraint[S2,T1,01_30]: x_S2_T1_0130 <= 0
 vtw_constraint[S2,T2,00_00]: x_S2_T2_0000 <= 0
 vtw_constraint[S2,T2,00_05]: x_S2_T2_0005 <= 0
 vtw_constraint[S2,T2,01_30]: x_S2_T2_0130 <= 0
 vtw_constraint[S2,T3,00_00]: x_S2_T3_0000 <= 1
 vtw_constraint[S2,T3,00_05]: x_S2_T3_0005 <= 0
 vtw_constraint[S2,T3,01_30]: x_S2_T3_0130 <= 0
 vtw_constraint[S2,T4,00_00]: x_S2_T4_0000 <= 0
 vtw_constraint[S2,T4,00_05]: x_S2_T4_0005 <= 0
 vtw_constraint[S2,T4,01_30]: x_S2_T4_0130 <= 0
 vtw_constraint[S2,T5,00_00]: x_S2_T5_0000 <= 0
 vtw_constraint[S2,T5,00_05]: x_S2_T5_0005 <= 0
 vtw_constraint[S2,T5,01_30]: x_S2_T5_0130 <= 0
 vtw_constraint[S3,T1,00_00]: x_S3_T1_0000 <= 0
 vtw_constraint[S3,T1,00_05]: x_S3_T1_0005 <= 0
 vtw_constraint[S3,T1,01_30]: x_S3_T1_0130 <= 0
 vtw_constraint[S3,T2,00_00]: x_S3_T2_0000 <= 0
 vtw_constraint[S3,T2,00_05]: x_S3_T2_0005 <= 1
 vtw_constraint[S3,T2,01_30]: x_S3_T2_0130 <= 0
 vtw_constraint[S3,T3,00_00]: x_S3_T3_0000 <= 0
 vtw_constraint[S3,T3,00_05]: x_S3_T3_0005 <= 0
 vtw_constraint[S3,T3,01_30]: x_S3_T3_0130 <= 0
 vtw_constraint[S3,T4,00_00]: x_S3_T4_0000 <= 0
 vtw_constraint[S3,T4,00_05]: x_S3_T4_0005 <= 0
 vtw_constraint[S3,T4,01_30]: x_S3_T4_0130 <= 0
 vtw_constraint[S3,T5,00_00]: x_S3_T5_0000 <= 0
 vtw_constraint[S3,T5,00_05]: x_S3_T5_0005 <= 0
 vtw_constraint[S3,T5,01_30]: x_S3_T5_0130 <= 0
 vtw_constraint[S4,T1,00_00]: x_S4_T1_0000 <= 0
 vtw_constraint[S4,T1,00_05]: x_S4_T1_0005 <= 0
 vtw_constraint[S4,T1,01_30]: x_S4_T1_0130 <= 0
 vtw_constraint[S4,T2,00_00]: x_S4_T2_0000 <= 0
 vtw_constraint[S4,T2,00_05]: x_S4_T2_0005 <= 0
 vtw_constraint[S4,T2,01_30]: x_S4_T2_0130 <= 0
 vtw_constraint[S4,T3,00_00]: x_S4_T3_0000 <= 0
 vtw_constraint[S4,T3,00_05]: x_S4_T3_0005 <= 0
 vtw_constraint[S4,T3,01_30]: x_S4_T3_0130 <= 0
 vtw_constraint[S4,T4,00_00]: x_S4_T4_0000 <= 0
 vtw_constraint[S4,T4,00_05]: x_S4_T4_0005 <= 0
 vtw_constraint[S4,T4,01_30]: x_S4_T4_0130 <= 0
 vtw_constraint[S4,T5,00_00]: x_S4_T5_0000 <= 0
 vtw_constraint[S4,T5,00_05]: x_S4_T5_0005 <= 0
 vtw_constraint[S4,T5,01_30]: x_S4_T5_0130 <= 1
 vtw_constraint[S5,T1,00_00]: x_S5_T1_0000 <= 0
 vtw_constraint[S5,T1,00_05]: x_S5_T1_0005 <= 0
 vtw_constraint[S5,T1,01_30]: x_S5_T1_0130 <= 0
 vtw_constraint[S5,T2,00_00]: x_S5_T2_0000 <= 0
 vtw_constraint[S5,T2,00_05]: x_S5_T2_0005 <= 0
 vtw_constraint[S5,T2,01_30]: x_S5_T2_0130 <= 0
 vtw_constraint[S5,T3,00_00]: x_S5_T3_0000 <= 0
 vtw_constraint[S5,T3,00_05]: x_S5_T3_0005 <= 0
 vtw_constraint[S5,T3,01_30]: x_S5_T3_0130 <= 0
 vtw_constraint[S5,T4,00_00]: x_S5_T4_0000 <= 0
 vtw_constraint[S5,T4,00_05]: x_S5_T4_0005 <= 0
 vtw_constraint[S5,T4,01_30]: x_S5_T4_0130 <= 0
 vtw_constraint[S5,T5,00_00]: x_S5_T5_0000 <= 0
 vtw_constraint[S5,T5,00_05]: x_S5_T5_0005 <= 0
 vtw_constraint[S5,T5,01_30]: x_S5_T5_0130 <= 0
 max_obs_per_day_S1: x_S1_T1_0000 + x_S1_T1_0005 + x_S1_T1_0130
   + x_S1_T2_0000 + x_S1_T2_0005 + x_S1_T2_0130 + x_S1_T3_0000
   + x_S1_T3_0005 + x_S1_T3_0130 + x_S1_T4_0000 + x_S1_T4_0005
   + x_S1_T4_0130 + x_S1_T5_0000 + x_S1_T5_0005 + x_S1_T5_0130 <= 5
 max_obs_per_day_S2: x_S2_T1_0000 + x_S2_T1_0005 + x_S2_T1_0130
   + x_S2_T2_0000 + x_S2_T2_0005 + x_S2_T2_0130 + x_S2_T3_0000
   + x_S2_T3_0005 + x_S2_T3_0130 + x_S2_T4_0000 + x_S2_T4_0005
   + x_S2_T4_0130 + x_S2_T5_0000 + x_S2_T5_0005 + x_S2_T5_0130 <= 5
 max_obs_per_day_S3: x_S3_T1_0000 + x_S3_T1_0005 + x_S3_T1_0130
   + x_S3_T2_0000 + x_S3_T2_0005 + x_S3_T2_0130 + x_S3_T3_0000
   + x_S3_T3_0005 + x_S3_T3_0130 + x_S3_T4_0000 + x_S3_T4_0005
   + x_S3_T4_0130 + x_S3_T5_0000 + x_S3_T5_0005 + x_S3_T5_0130 <= 5
 max_obs_per_day_S4: x_S4_T1_0000 + x_S4_T1_0005 + x_S4_T1_0130
   + x_S4_T2_0000 + x_S4_T2_0005 + x_S4_T2_0130 + x_S4_T3_0000
   + x_S4_T3_0005 + x_S4_T3_0130 + x_S4_T4_0000 + x_S4_T4_0005
   + x_S4_T4_0130 + x_S4_T5_0000 + x_S4_T5_0005 + x_S4_T5_0130 <= 5
 max_obs_per_day_S5: x_S5_T1_0000 + x_S5_T1_0005 + x_S5_T1_0130
   + x_S5_T2_0000 + x_S5_T2_0005 + x_S5_T2_0130 + x_S5_T3_0000
   + x_S5_T3_0005 + x_S5_T3_0130 + x_S5_T4_0000 + x_S5_T4_0005
   + x_S5_T4_0130 + x_S5_T5_0000 + x_S5_T5_0005 + x_S5_T5_0130 <= 5
 single_obs_T1: x_S1_T1_0000 + x_S1_T1_0005 + x_S1_T1_0130 + x_S2_T1_0000
   + x_S2_T1_0005 + x_S2_T1_0130 + x_S3_T1_0000 + x_S3_T1_0005
   + x_S3_T1_0130 + x_S4_T1_0000 + x_S4_T1_0005 + x_S4_T1_0130
   + x_S5_T1_0000 + x_S5_T1_0005 + x_S5_T1_0130 <= 1
 single_obs_T2: x_S1_T2_0000 + x_S1_T2_0005 + x_S1_T2_0130 + x_S2_T2_0000
   + x_S2_T2_0005 + x_S2_T2_0130 + x_S3_T2_0000 + x_S3_T2_0005
   + x_S3_T2_0130 + x_S4_T2_0000 + x_S4_T2_0005 + x_S4_T2_0130
   + x_S5_T2_0000 + x_S5_T2_0005 + x_S5_T2_0130 <= 1
 single_obs_T3: x_S1_T3_0000 + x_S1_T3_0005 + x_S1_T3_0130 + x_S2_T3_0000
   + x_S2_T3_0005 + x_S2_T3_0130 + x_S3_T3_0000 + x_S3_T3_0005
   + x_S3_T3_0130 + x_S4_T3_0000 + x_S4_T3_0005 + x_S4_T3_0130
   + x_S5_T3_0000 + x_S5_T3_0005 + x_S5_T3_0130 <= 1
 single_obs_T4: x_S1_T4_0000 + x_S1_T4_0005 + x_S1_T4_0130 + x_S2_T4_0000
   + x_S2_T4_0005 + x_S2_T4_0130 + x_S3_T4_0000 + x_S3_T4_0005
   + x_S3_T4_0130 + x_S4_T4_0000 + x_S4_T4_0005 + x_S4_T4_0130
   + x_S5_T4_0000 + x_S5_T4_0005 + x_S5_T4_0130 <= 1
 single_obs_T5: x_S1_T5_0000 + x_S1_T5_0005 + x_S1_T5_0130 + x_S2_T5_0000
   + x_S2_T5_0005 + x_S2_T5_0130 + x_S3_T5_0000 + x_S3_T5_0005
   + x_S3_T5_0130 + x_S4_T5_0000 + x_S4_T5_0005 + x_S4_T5_0130
   + x_S5_T5_0000 + x_S5_T5_0005 + x_S5_T5_0130 <= 1
 mem_initial_S1: - 5 x_S1_T1_0000 - 5 x_S1_T2_0000 - 5 x_S1_T3_0000
   - 5 x_S1_T4_0000 - 5 x_S1_T5_0000 + m_S1_0000 = 0
 memory_balance_S1_0005: - 5 x_S1_T1_0005 - 5 x_S1_T2_0005 - 5 x_S1_T3_0005
   - 5 x_S1_T4_0005 - 5 x_S1_T5_0005 - m_S1_0000 + m_S1_0005 = 0
 memory_balance_S1_0015: d_S1_GS1_0015 + d_S1_GS2_0015 + d_S1_GS3_0015
   + d_S1_GS4_0015 + d_S1_GS5_0015 - m_S1_0005 + m_S1_0015 = 0
 memory_balance_S1_0130: - 5 x_S1_T1_0130 - 5 x_S1_T2_0130 - 5 x_S1_T3_0130
   - 5 x_S1_T4_0130 - 5 x_S1_T5_0130 - m_S1_0015 + m_S1_0130 = 0
 memory_balance_S1_0200: d_S1_GS1_0200 + d_S1_GS2_0200 + d_S1_GS3_0200
   + d_S1_GS4_0200 + d_S1_GS5_0200 - m_S1_0130 + m_S1_0200 = 0
 mem_initial_S2: - 5 x_S2_T1_0000 - 5 x_S2_T2_0000 - 5 x_S2_T3_0000
   - 5 x_S2_T4_0000 - 5 x_S2_T5_0000 + m_S2_0000 = 0
 memory_balance_S2_0005: - 5 x_S2_T1_0005 - 5 x_S2_T2_0005 - 5 x_S2_T3_0005
   - 5 x_S2_T4_0005 - 5 x_S2_T5_0005 - m_S2_0000 + m_S2_0005 = 0
 memory_balance_S2_0015: d_S2_GS1_0015 + d_S2_GS2_0015 + d_S2_GS3_0015
   + d_S2_GS4_0015 + d_S2_GS5_0015 - m_S2_0005 + m_S2_0015 = 0
 memory_balance_S2_0130: - 5 x_S2_T1_0130 - 5 x_S2_T2_0130 - 5 x_S2_T3_0130
   - 5 x_S2_T4_0130 - 5 x_S2_T5_0130 - m_S2_0015 + m_S2_0130 = 0
 memory_balance_S2_0200: d_S2_GS1_0200 + d_S2_GS2_0200 + d_S2_GS3_0200
   + d_S2_GS4_0200 + d_S2_GS5_0200 - m_S2_0130 + m_S2_0200 = 0
 mem_initial_S3: - 5 x_S3_T1_0000 - 5 x_S3_T2_0000 - 5 x_S3_T3_0000
   - 5 x_S3_T4_0000 - 5 x_S3_T5_0000 + m_S3_0000 = 0
 memory_balance_S3_0005: - 5 x_S3_T1_0005 - 5 x_S3_T2_0005 - 5 x_S3_T3_0005
   - 5 x_S3_T4_0005 - 5 x_S3_T5_0005 - m_S3_0000 + m_S3_0005 = 0
 memory_balance_S3_0015: d_S3_GS1_0015 + d_S3_GS2_0015 + d_S3_GS3_0015
   + d_S3_GS4_0015 + d_S3_GS5_0015 - m_S3_0005 + m_S3_0015 = 0
 memory_balance_S3_0130: - 5 x_S3_T1_0130 - 5 x_S3_T2_0130 - 5 x_S3_T3_0130
   - 5 x_S3_T4_0130 - 5 x_S3_T5_0130 - m_S3_0015 + m_S3_0130 = 0
 memory_balance_S3_0200: d_S3_GS1_0200 + d_S3_GS2_0200 + d_S3_GS3_0200
   + d_S3_GS4_0200 + d_S3_GS5_0200 - m_S3_0130 + m_S3_0200 = 0
 mem_initial_S4: - 5 x_S4_T1_0000 - 5 x_S4_T2_0000 - 5 x_S4_T3_0000
   - 5 x_S4_T4_0000 - 5 x_S4_T5_0000 + m_S4_0000 = 0
 memory_balance_S4_0005: - 5 x_S4_T1_0005 - 5 x_S4_T2_0005 - 5 x_S4_T3_0005
   - 5 x_S4_T4_0005 - 5 x_S4_T5_0005 - m_S4_0000 + m_S4_0005 = 0
 memory_balance_S4_0015: d_S4_GS1_0015 + d_S4_GS2_0015 + d_S4_GS3_0015
   + d_S4_GS4_0015 + d_S4_GS5_0015 - m_S4_0005 + m_S4_0015 = 0
 memory_balance_S4_0130: - 5 x_S4_T1_0130 - 5 x_S4_T2_0130 - 5 x_S4_T3_0130
   - 5 x_S4_T4_0130 - 5 x_S4_T5_0130 - m_S4_0015 + m_S4_0130 = 0
 memory_balance_S4_0200: d_S4_GS1_0200 + d_S4_GS2_0200 + d_S4_GS3_0200
   + d_S4_GS4_0200 + d_S4_GS5_0200 - m_S4_0130 + m_S4_0200 = 0
 mem_initial_S5: - 5 x_S5_T1_0000 - 5 x_S5_T2_0000 - 5 x_S5_T3_0000
   - 5 x_S5_T4_0000 - 5 x_S5_T5_0000 + m_S5_0000 = 0
 memory_balance_S5_0005: - 5 x_S5_T1_0005 - 5 x_S5_T2_0005 - 5 x_S5_T3_0005
   - 5 x_S5_T4_0005 - 5 x_S5_T5_0005 - m_S5_0000 + m_S5_0005 = 0
 memory_balance_S5_0015: d_S5_GS1_0015 + d_S5_GS2_0015 + d_S5_GS3_0015
   + d_S5_GS4_0015 + d_S5_GS5_0015 - m_S5_0005 + m_S5_0015 = 0
 memory_balance_S5_0130: - 5 x_S5_T1_0130 - 5 x_S5_T2_0130 - 5 x_S5_T3_0130
   - 5 x_S5_T4_0130 - 5 x_S5_T5_0130 - m_S5_0015 + m_S5_0130 = 0
 memory_balance_S5_0200: d_S5_GS1_0200 + d_S5_GS2_0200 + d_S5_GS3_0200
   + d_S5_GS4_0200 + d_S5_GS5_0200 - m_S5_0130 + m_S5_0200 = 0
 memory_capacity_S1_0000: m_S1_0000 <= 100
 memory_capacity_S1_0005: m_S1_0005 <= 100
 memory_capacity_S1_0015: m_S1_0015 <= 100
 memory_capacity_S1_0130: m_S1_0130 <= 100
 memory_capacity_S1_0200: m_S1_0200 <= 100
 memory_capacity_S2_0000: m_S2_0000 <= 100
 memory_capacity_S2_0005: m_S2_0005 <= 100
 memory_capacity_S2_0015: m_S2_0015 <= 100
 memory_capacity_S2_0130: m_S2_0130 <= 100
 memory_capacity_S2_0200: m_S2_0200 <= 100
 memory_capacity_S3_0000: m_S3_0000 <= 100
 memory_capacity_S3_0005: m_S3_0005 <= 100
 memory_capacity_S3_0015: m_S3_0015 <= 100
 memory_capacity_S3_0130: m_S3_0130 <= 100
 memory_capacity_S3_0200: m_S3_0200 <= 100
 memory_capacity_S4_0000: m_S4_0000 <= 100
 memory_capacity_S4_0005: m_S4_0005 <= 100
 memory_capacity_S4_0015: m_S4_0015 <= 100
 memory_capacity_S4_0130: m_S4_0130 <= 100
 memory_capacity_S4_0200: m_S4_0200 <= 100
 memory_capacity_S5_0000: m_S5_0000 <= 100
 memory_capacity_S5_0005: m_S5_0005 <= 100
 memory_capacity_S5_0015: m_S5_0015 <= 100
 memory_capacity_S5_0130: m_S5_0130 <= 100
 memory_capacity_S5_0200: m_S5_0200 <= 100
 power_initial_S1: 10 x_S1_T1_0000 + 10 x_S1_T2_0000 + 10 x_S1_T3_0000
   + 10 x_S1_T4_0000 + 10 x_S1_T5_0000 + p_S1_0000 = 100
 power_balance_S1_0005: 10 x_S1_T1_0005 + 10 x_S1_T2_0005 + 10 x_S1_T3_0005
   + 10 x_S1_T4_0005 + 10 x_S1_T5_0005 - p_S1_0000 + p_S1_0005 = 0
 power_balance_S1_0015: 5 d_S1_GS1_0015 + 5 d_S1_GS2_0015 + 5 d_S1_GS3_0015
   + 5 d_S1_GS4_0015 + 5 d_S1_GS5_0015 - p_S1_0005 + p_S1_0015 = 0
 power_balance_S1_0130: 10 x_S1_T1_0130 + 10 x_S1_T2_0130 + 10 x_S1_T3_0130
   + 10 x_S1_T4_0130 + 10 x_S1_T5_0130 - p_S1_0015 + p_S1_0130 = 0
 power_balance_S1_0200: 5 d_S1_GS1_0200 + 5 d_S1_GS2_0200 + 5 d_S1_GS3_0200
   + 5 d_S1_GS4_0200 + 5 d_S1_GS5_0200 - p_S1_0130 + p_S1_0200 = 0
 power_initial_S2: 10 x_S2_T1_0000 + 10 x_S2_T2_0000 + 10 x_S2_T3_0000
   + 10 x_S2_T4_0000 + 10 x_S2_T5_0000 + p_S2_0000 = 100
 power_balance_S2_0005: 10 x_S2_T1_0005 + 10 x_S2_T2_0005 + 10 x_S2_T3_0005
   + 10 x_S2_T4_0005 + 10 x_S2_T5_0005 - p_S2_0000 + p_S2_0005 = 0
 power_balance_S2_0015: 5 d_S2_GS1_0015 + 5 d_S2_GS2_0015 + 5 d_S2_GS3_0015
   + 5 d_S2_GS4_0015 + 5 d_S2_GS5_0015 - p_S2_0005 + p_S2_0015 = 0
 power_balance_S2_0130: 10 x_S2_T1_0130 + 10 x_S2_T2_0130 + 10 x_S2_T3_0130
   + 10 x_S2_T4_0130 + 10 x_S2_T5_0130 - p_S2_0015 + p_S2_0130 = 0
 power_balance_S2_0200: 5 d_S2_GS1_0200 + 5 d_S2_GS2_0200 + 5 d_S2_GS3_0200
   + 5 d_S2_GS4_0200 + 5 d_S2_GS5_0200 - p_S2_0130 + p_S2_0200 = 0
 power_initial_S3: 10 x_S3_T1_0000 + 10 x_S3_T2_0000 + 10 x_S3_T3_0000
   + 10 x_S3_T4_0000 + 10 x_S3_T5_0000 + p_S3_0000 = 100
 power_balance_S3_0005: 10 x_S3_T1_0005 + 10 x_S3_T2_0005 + 10 x_S3_T3_0005
   + 10 x_S3_T4_0005 + 10 x_S3_T5_0005 - p_S3_0000 + p_S3_0005 = 0
 power_balance_S3_0015: 5 d_S3_GS1_0015 + 5 d_S3_GS2_0015 + 5 d_S3_GS3_0015
   + 5 d_S3_GS4_0015 + 5 d_S3_GS5_0015 - p_S3_0005 + p_S3_0015 = 0
 power_balance_S3_0130: 10 x_S3_T1_0130 + 10 x_S3_T2_0130 + 10 x_S3_T3_0130
   + 10 x_S3_T4_0130 + 10 x_S3_T5_0130 - p_S3_0015 + p_S3_0130 = 0
 power_balance_S3_0200: 5 d_S3_GS1_0200 + 5 d_S3_GS2_0200 + 5 d_S3_GS3_0200
   + 5 d_S3_GS4_0200 + 5 d_S3_GS5_0200 - p_S3_0130 + p_S3_0200 = 0
 power_initial_S4: 10 x_S4_T1_0000 + 10 x_S4_T2_0000 + 10 x_S4_T3_0000
   + 10 x_S4_T4_0000 + 10 x_S4_T5_0000 + p_S4_0000 = 100
 power_balance_S4_0005: 10 x_S4_T1_0005 + 10 x_S4_T2_0005 + 10 x_S4_T3_0005
   + 10 x_S4_T4_0005 + 10 x_S4_T5_0005 - p_S4_0000 + p_S4_0005 = 0
 power_balance_S4_0015: 5 d_S4_GS1_0015 + 5 d_S4_GS2_0015 + 5 d_S4_GS3_0015
   + 5 d_S4_GS4_0015 + 5 d_S4_GS5_0015 - p_S4_0005 + p_S4_0015 = 0
 power_balance_S4_0130: 10 x_S4_T1_0130 + 10 x_S4_T2_0130 + 10 x_S4_T3_0130
   + 10 x_S4_T4_0130 + 10 x_S4_T5_0130 - p_S4_0015 + p_S4_0130 = 0
 power_balance_S4_0200: 5 d_S4_GS1_0200 + 5 d_S4_GS2_0200 + 5 d_S4_GS3_0200
   + 5 d_S4_GS4_0200 + 5 d_S4_GS5_0200 - p_S4_0130 + p_S4_0200 = 0
 power_initial_S5: 10 x_S5_T1_0000 + 10 x_S5_T2_0000 + 10 x_S5_T3_0000
   + 10 x_S5_T4_0000 + 10 x_S5_T5_0000 + p_S5_0000 = 100
 power_balance_S5_0005: 10 x_S5_T1_0005 + 10 x_S5_T2_0005 + 10 x_S5_T3_0005
   + 10 x_S5_T4_0005 + 10 x_S5_T5_0005 - p_S5_0000 + p_S5_0005 = 0
 power_balance_S5_0015: 5 d_S5_GS1_0015 + 5 d_S5_GS2_0015 + 5 d_S5_GS3_0015
   + 5 d_S5_GS4_0015 + 5 d_S5_GS5_0015 - p_S5_0005 + p_S5_0015 = 0
 power_balance_S5_0130: 10 x_S5_T1_0130 + 10 x_S5_T2_0130 + 10 x_S5_T3_0130
   + 10 x_S5_T4_0130 + 10 x_S5_T5_0130 - p_S5_0015 + p_S5_0130 = 0
 power_balance_S5_0200: 5 d_S5_GS1_0200 + 5 d_S5_GS2_0200 + 5 d_S5_GS3_0200
   + 5 d_S5_GS4_0200 + 5 d_S5_GS5_0200 - p_S5_0130 + p_S5_0200 = 0
 power_capacity_upper_S1_0000: p_S1_0000 <= 100
 power_capacity_lower_S1_0000: p_S1_0000 >= 0
 power_capacity_upper_S1_0005: p_S1_0005 <= 100
 power_capacity_lower_S1_0005: p_S1_0005 >= 0
 power_capacity_upper_S1_0015: p_S1_0015 <= 100
 power_capacity_lower_S1_0015: p_S1_0015 >= 0
 power_capacity_upper_S1_0130: p_S1_0130 <= 100
 power_capacity_lower_S1_0130: p_S1_0130 >= 0
 power_capacity_upper_S1_0200: p_S1_0200 <= 100
 power_capacity_lower_S1_0200: p_S1_0200 >= 0
 power_capacity_upper_S2_0000: p_S2_0000 <= 100
 power_capacity_lower_S2_0000: p_S2_0000 >= 0
 power_capacity_upper_S2_0005: p_S2_0005 <= 100
 power_capacity_lower_S2_0005: p_S2_0005 >= 0
 power_capacity_upper_S2_0015: p_S2_0015 <= 100
 power_capacity_lower_S2_0015: p_S2_0015 >= 0
 power_capacity_upper_S2_0130: p_S2_0130 <= 100
 power_capacity_lower_S2_0130: p_S2_0130 >= 0
 power_capacity_upper_S2_0200: p_S2_0200 <= 100
 power_capacity_lower_S2_0200: p_S2_0200 >= 0
 power_capacity_upper_S3_0000: p_S3_0000 <= 100
 power_capacity_lower_S3_0000: p_S3_0000 >= 0
 power_capacity_upper_S3_0005: p_S3_0005 <= 100
 power_capacity_lower_S3_0005: p_S3_0005 >= 0
 power_capacity_upper_S3_0015: p_S3_0015 <= 100
 power_capacity_lower_S3_0015: p_S3_0015 >= 0
 power_capacity_upper_S3_0130: p_S3_0130 <= 100
 power_capacity_lower_S3_0130: p_S3_0130 >= 0
 power_capacity_upper_S3_0200: p_S3_0200 <= 100
 power_capacity_lower_S3_0200: p_S3_0200 >= 0
 power_capacity_upper_S4_0000: p_S4_0000 <= 100
 power_capacity_lower_S4_0000: p_S4_0000 >= 0
 power_capacity_upper_S4_0005: p_S4_0005 <= 100
 power_capacity_lower_S4_0005: p_S4_0005 >= 0
 power_capacity_upper_S4_0015: p_S4_0015 <= 100
 power_capacity_lower_S4_0015: p_S4_0015 >= 0
 power_capacity_upper_S4_0130: p_S4_0130 <= 100
 power_capacity_lower_S4_0130: p_S4_0130 >= 0
 power_capacity_upper_S4_0200: p_S4_0200 <= 100
 power_capacity_lower_S4_0200: p_S4_0200 >= 0
 power_capacity_upper_S5_0000: p_S5_0000 <= 100
 power_capacity_lower_S5_0000: p_S5_0000 >= 0
 power_capacity_upper_S5_0005: p_S5_0005 <= 100
 power_capacity_lower_S5_0005: p_S5_0005 >= 0
 power_capacity_upper_S5_0015: p_S5_0015 <= 100
 power_capacity_lower_S5_0015: p_S5_0015 >= 0
 power_capacity_upper_S5_0130: p_S5_0130 <= 100
 power_capacity_lower_S5_0130: p_S5_0130 >= 0
 power_capacity_upper_S5_0200: p_S5_0200 <= 100
 power_capacity_lower_S5_0200: p_S5_0200 >= 0
 downlink_window_S1_GS1_0015: y_S1_GS1_0015 <= 1
 downlink_window_S1_GS1_0200: y_S1_GS1_0200 <= 0
 downlink_window_S1_GS2_0015: y_S1_GS2_0015 <= 0
 downlink_window_S1_GS2_0200: y_S1_GS2_0200 <= 0
 downlink_window_S1_GS3_0015: y_S1_GS3_0015 <= 0
 downlink_window_S1_GS3_0200: y_S1_GS3_0200 <= 0
 downlink_window_S1_GS4_0015: y_S1_GS4_0015 <= 0
 downlink_window_S1_GS4_0200: y_S1_GS4_0200 <= 0
 downlink_window_S1_GS5_0015: y_S1_GS5_0015 <= 0
 downlink_window_S1_GS5_0200: y_S1_GS5_0200 <= 0
 downlink_window_S2_GS1_0015: y_S2_GS1_0015 <= 0
 downlink_window_S2_GS1_0200: y_S2_GS1_0200 <= 0
 downlink_window_S2_GS2_0015: y_S2_GS2_0015 <= 1
 downlink_window_S2_GS2_0200: y_S2_GS2_0200 <= 0
 downlink_window_S2_GS3_0015: y_S2_GS3_0015 <= 0
 downlink_window_S2_GS3_0200: y_S2_GS3_0200 <= 0
 downlink_window_S2_GS4_0015: y_S2_GS4_0015 <= 0
 downlink_window_S2_GS4_0200: y_S2_GS4_0200 <= 0
 downlink_window_S2_GS5_0015: y_S2_GS5_0015 <= 0
 downlink_window_S2_GS5_0200: y_S2_GS5_0200 <= 0
 downlink_window_S3_GS1_0015: y_S3_GS1_0015 <= 0
 downlink_window_S3_GS1_0200: y_S3_GS1_0200 <= 0
 downlink_window_S3_GS2_0015: y_S3_GS2_0015 <= 0
 downlink_window_S3_GS2_0200: y_S3_GS2_0200 <= 0
 downlink_window_S3_GS3_0015: y_S3_GS3_0015 <= 0
 downlink_window_S3_GS3_0200: y_S3_GS3_0200 <= 1
 downlink_window_S3_GS4_0015: y_S3_GS4_0015 <= 0
 downlink_window_S3_GS4_0200: y_S3_GS4_0200 <= 0
 downlink_window_S3_GS5_0015: y_S3_GS5_0015 <= 0
 downlink_window_S3_GS5_0200: y_S3_GS5_0200 <= 0
 downlink_window_S4_GS1_0015: y_S4_GS1_0015 <= 0
 downlink_window_S4_GS1_0200: y_S4_GS1_0200 <= 0
 downlink_window_S4_GS2_0015: y_S4_GS2_0015 <= 0
 downlink_window_S4_GS2_0200: y_S4_GS2_0200 <= 0
 downlink_window_S4_GS3_0015: y_S4_GS3_0015 <= 0
 downlink_window_S4_GS3_0200: y_S4_GS3_0200 <= 0
 downlink_window_S4_GS4_0015: y_S4_GS4_0015 <= 0
 downlink_window_S4_GS4_0200: y_S4_GS4_0200 <= 1
 downlink_window_S4_GS5_0015: y_S4_GS5_0015 <= 0
 downlink_window_S4_GS5_0200: y_S4_GS5_0200 <= 0
 downlink_window_S5_GS1_0015: y_S5_GS1_0015 <= 0
 downlink_window_S5_GS1_0200: y_S5_GS1_0200 <= 0
 downlink_window_S5_GS2_0015: y_S5_GS2_0015 <= 0
 downlink_window_S5_GS2_0200: y_S5_GS2_0200 <= 0
 downlink_window_S5_GS3_0015: y_S5_GS3_0015 <= 0
 downlink_window_S5_GS3_0200: y_S5_GS3_0200 <= 0
 downlink_window_S5_GS4_0015: y_S5_GS4_0015 <= 0
 downlink_window_S5_GS4_0200: y_S5_GS4_0200 <= 0
 downlink_window_S5_GS5_0015: y_S5_GS5_0015 <= 0
 downlink_window_S5_GS5_0200: y_S5_GS5_0200 <= 0
 link_downlink_amount_S1_GS1_0015: - 10 y_S1_GS1_0015 + d_S1_GS1_0015 <= 0
 link_downlink_amount_S1_GS1_0200: - 10 y_S1_GS1_0200 + d_S1_GS1_0200 <= 0
 link_downlink_amount_S1_GS2_0015: - 10 y_S1_GS2_0015 + d_S1_GS2_0015 <= 0
 link_downlink_amount_S1_GS2_0200: - 10 y_S1_GS2_0200 + d_S1_GS2_0200 <= 0
 link_downlink_amount_S1_GS3_0015: - 10 y_S1_GS3_0015 + d_S1_GS3_0015 <= 0
 link_downlink_amount_S1_GS3_0200: - 10 y_S1_GS3_0200 + d_S1_GS3_0200 <= 0
 link_downlink_amount_S1_GS4_0015: - 10 y_S1_GS4_0015 + d_S1_GS4_0015 <= 0
 link_downlink_amount_S1_GS4_0200: - 10 y_S1_GS4_0200 + d_S1_GS4_0200 <= 0
 link_downlink_amount_S1_GS5_0015: - 10 y_S1_GS5_0015 + d_S1_GS5_0015 <= 0
 link_downlink_amount_S1_GS5_0200: - 10 y_S1_GS5_0200 + d_S1_GS5_0200 <= 0
 link_downlink_amount_S2_GS1_0015: - 10 y_S2_GS1_0015 + d_S2_GS1_0015 <= 0
 link_downlink_amount_S2_GS1_0200: - 10 y_S2_GS1_0200 + d_S2_GS1_0200 <= 0
 link_downlink_amount_S2_GS2_0015: - 10 y_S2_GS2_0015 + d_S2_GS2_0015 <= 0
 link_downlink_amount_S2_GS2_0200: - 10 y_S2_GS2_0200 + d_S2_GS2_0200 <= 0
 link_downlink_amount_S2_GS3_0015: - 10 y_S2_GS3_0015 + d_S2_GS3_0015 <= 0
 link_downlink_amount_S2_GS3_0200: - 10 y_S2_GS3_0200 + d_S2_GS3_0200 <= 0
 link_downlink_amount_S2_GS4_0015: - 10 y_S2_GS4_0015 + d_S2_GS4_0015 <= 0
 link_downlink_amount_S2_GS4_0200: - 10 y_S2_GS4_0200 + d_S2_GS4_0200 <= 0
 link_downlink_amount_S2_GS5_0015: - 10 y_S2_GS5_0015 + d_S2_GS5_0015 <= 0
 link_downlink_amount_S2_GS5_0200: - 10 y_S2_GS5_0200 + d_S2_GS5_0200 <= 0
 link_downlink_amount_S3_GS1_0015: - 10 y_S3_GS1_0015 + d_S3_GS1_0015 <= 0
 link_downlink_amount_S3_GS1_0200: - 10 y_S3_GS1_0200 + d_S3_GS1_0200 <= 0
 link_downlink_amount_S3_GS2_0015: - 10 y_S3_GS2_0015 + d_S3_GS2_0015 <= 0
 link_downlink_amount_S3_GS2_0200: - 10 y_S3_GS2_0200 + d_S3_GS2_0200 <= 0
 link_downlink_amount_S3_GS3_0015: - 10 y_S3_GS3_0015 + d_S3_GS3_0015 <= 0
 link_downlink_amount_S3_GS3_0200: - 10 y_S3_GS3_0200 + d_S3_GS3_0200 <= 0
 link_downlink_amount_S3_GS4_0015: - 10 y_S3_GS4_0015 + d_S3_GS4_0015 <= 0
 link_downlink_amount_S3_GS4_0200: - 10 y_S3_GS4_0200 + d_S3_GS4_0200 <= 0
 link_downlink_amount_S3_GS5_0015: - 10 y_S3_GS5_0015 + d_S3_GS5_0015 <= 0
 link_downlink_amount_S3_GS5_0200: - 10 y_S3_GS5_0200 + d_S3_GS5_0200 <= 0
 link_downlink_amount_S4_GS1_0015: - 10 y_S4_GS1_0015 + d_S4_GS1_0015 <= 0
 link_downlink_amount_S4_GS1_0200: - 10 y_S4_GS1_0200 + d_S4_GS1_0200 <= 0
 link_downlink_amount_S4_GS2_0015: - 10 y_S4_GS2_0015 + d_S4_GS2_0015 <= 0
 link_downlink_amount_S4_GS2_0200: - 10 y_S4_GS2_0200 + d_S4_GS2_0200 <= 0
 link_downlink_amount_S4_GS3_0015: - 10 y_S4_GS3_0015 + d_S4_GS3_0015 <= 0
 link_downlink_amount_S4_GS3_0200: - 10 y_S4_GS3_0200 + d_S4_GS3_0200 <= 0
 link_downlink_amount_S4_GS4_0015: - 10 y_S4_GS4_0015 + d_S4_GS4_0015 <= 0
 link_downlink_amount_S4_GS4_0200: - 10 y_S4_GS4_0200 + d_S4_GS4_0200 <= 0
 link_downlink_amount_S4_GS5_0015: - 10 y_S4_GS5_0015 + d_S4_GS5_0015 <= 0
 link_downlink_amount_S4_GS5_0200: - 10 y_S4_GS5_0200 + d_S4_GS5_0200 <= 0
 link_downlink_amount_S5_GS1_0015: - 10 y_S5_GS1_0015 + d_S5_GS1_0015 <= 0
 link_downlink_amount_S5_GS1_0200: - 10 y_S5_GS1_0200 + d_S5_GS1_0200 <= 0
 link_downlink_amount_S5_GS2_0015: - 10 y_S5_GS2_0015 + d_S5_GS2_0015 <= 0
 link_downlink_amount_S5_GS2_0200: - 10 y_S5_GS2_0200 + d_S5_GS2_0200 <= 0
 link_downlink_amount_S5_GS3_0015: - 10 y_S5_GS3_0015 + d_S5_GS3_0015 <= 0
 link_downlink_amount_S5_GS3_0200: - 10 y_S5_GS3_0200 + d_S5_GS3_0200 <= 0
 link_downlink_amount_S5_GS4_0015: - 10 y_S5_GS4_0015 + d_S5_GS4_0015 <= 0
 link_downlink_amount_S5_GS4_0200: - 10 y_S5_GS4_0200 + d_S5_GS4_0200 <= 0
 link_downlink_amount_S5_GS5_0015: - 10 y_S5_GS5_0015 + d_S5_GS5_0015 <= 0
 link_downlink_amount_S5_GS5_0200: - 10 y_S5_GS5_0200 + d_S5_GS5_0200 <= 0
 groundstation_conflict_GS1_0015: y_S1_GS1_0015 + y_S2_GS1_0015
   + y_S3_GS1_0015 + y_S4_GS1_0015 + y_S5_GS1_0015 <= 1
 groundstation_conflict_GS1_0200: y_S1_GS1_0200 + y_S2_GS1_0200
   + y_S3_GS1_0200 + y_S4_GS1_0200 + y_S5_GS1_0200 <= 1
 groundstation_conflict_GS2_0015: y_S1_GS2_0015 + y_S2_GS2_0015
   + y_S3_GS2_0015 + y_S4_GS2_0015 + y_S5_GS2_0015 <= 1
 groundstation_conflict_GS2_0200: y_S1_GS2_0200 + y_S2_GS2_0200
   + y_S3_GS2_0200 + y_S4_GS2_0200 + y_S5_GS2_0200 <= 1
 groundstation_conflict_GS3_0015: y_S1_GS3_0015 + y_S2_GS3_0015
   + y_S3_GS3_0015 + y_S4_GS3_0015 + y_S5_GS3_0015 <= 1
 groundstation_conflict_GS3_0200: y_S1_GS3_0200 + y_S2_GS3_0200
   + y_S3_GS3_0200 + y_S4_GS3_0200 + y_S5_GS3_0200 <= 1
 groundstation_conflict_GS4_0015: y_S1_GS4_0015 + y_S2_GS4_0015
   + y_S3_GS4_0015 + y_S4_GS4_0015 + y_S5_GS4_0015 <= 1
 groundstation_conflict_GS4_0200: y_S1_GS4_0200 + y_S2_GS4_0200
   + y_S3_GS4_0200 + y_S4_GS4_0200 + y_S5_GS4_0200 <= 1
 groundstation_conflict_GS5_0015: y_S1_GS5_0015 + y_S2_GS5_0015
   + y_S3_GS5_0015 + y_S4_GS5_0015 + y_S5_GS5_0015 <= 1
 groundstation_conflict_GS5_0200: y_S1_GS5_0200 + y_S2_GS5_0200
   + y_S3_GS5_0200 + y_S4_GS5_0200 + y_S5_GS5_0200 <= 1
 satellite_downlink_exclusivity_S1_0015: y_S1_GS1_0015 + y_S1_GS2_0015
   + y_S1_GS3_0015 + y_S1_GS4_0015 + y_S1_GS5_0015 <= 1
 satellite_downlink_exclusivity_S1_0200: y_S1_GS1_0200 + y_S1_GS2_0200
   + y_S1_GS3_0200 + y_S1_GS4_0200 + y_S1_GS5_0200 <= 1
 satellite_downlink_exclusivity_S2_0015: y_S2_GS1_0015 + y_S2_GS2_0015
   + y_S2_GS3_0015 + y_S2_GS4_0015 + y_S2_GS5_0015 <= 1
 satellite_downlink_exclusivity_S2_0200: y_S2_GS1_0200 + y_S2_GS2_0200
   + y_S2_GS3_0200 + y_S2_GS4_0200 + y_S2_GS5_0200 <= 1
 satellite_downlink_exclusivity_S3_0015: y_S3_GS1_0015 + y_S3_GS2_0015
   + y_S3_GS3_0015 + y_S3_GS4_0015 + y_S3_GS5_0015 <= 1
 satellite_downlink_exclusivity_S3_0200: y_S3_GS1_0200 + y_S3_GS2_0200
   + y_S3_GS3_0200 + y_S3_GS4_0200 + y_S3_GS5_0200 <= 1
 satellite_downlink_exclusivity_S4_0015: y_S4_GS1_0015 + y_S4_GS2_0015
   + y_S4_GS3_0015 + y_S4_GS4_0015 + y_S4_GS5_0015 <= 1
 satellite_downlink_exclusivity_S4_0200: y_S4_GS1_0200 + y_S4_GS2_0200
   + y_S4_GS3_0200 + y_S4_GS4_0200 + y_S4_GS5_0200 <= 1
 satellite_downlink_exclusivity_S5_0015: y_S5_GS1_0015 + y_S5_GS2_0015
   + y_S5_GS3_0015 + y_S5_GS4_0015 + y_S5_GS5_0015 <= 1
 satellite_downlink_exclusivity_S5_0200: y_S5_GS1_0200 + y_S5_GS2_0200
   + y_S5_GS3_0200 + y_S5_GS4_0200 + y_S5_GS5_0200 <= 1
Bounds
 d_S1_GS1_0015 <= 10
 d_S1_GS1_0200 <= 10
 d_S1_GS2_0015 <= 10
 d_S1_GS2_0200 <= 10
 d_S1_GS3_0015 <= 10
 d_S1_GS3_0200 <= 10
 d_S1_GS4_0015 <= 10
 d_S1_GS4_0200 <= 10
 d_S1_GS5_0015 <= 10
 d_S1_GS5_0200 <= 10
 d_S2_GS1_0015 <= 10
 d_S2_GS1_0200 <= 10
 d_S2_GS2_0015 <= 10
 d_S2_GS2_0200 <= 10
 d_S2_GS3_0015 <= 10
 d_S2_GS3_0200 <= 10
 d_S2_GS4_0015 <= 10
 d_S2_GS4_0200 <= 10
 d_S2_GS5_0015 <= 10
 d_S2_GS5_0200 <= 10
 d_S3_GS1_0015 <= 10
 d_S3_GS1_0200 <= 10
 d_S3_GS2_0015 <= 10
 d_S3_GS2_0200 <= 10
 d_S3_GS3_0015 <= 10
 d_S3_GS3_0200 <= 10
 d_S3_GS4_0015 <= 10
 d_S3_GS4_0200 <= 10
 d_S3_GS5_0015 <= 10
 d_S3_GS5_0200 <= 10
 d_S4_GS1_0015 <= 10
 d_S4_GS1_0200 <= 10
 d_S4_GS2_0015 <= 10
 d_S4_GS2_0200 <= 10
 d_S4_GS3_0015 <= 10
 d_S4_GS3_0200 <= 10
 d_S4_GS4_0015 <= 10
 d_S4_GS4_0200 <= 10
 d_S4_GS5_0015 <= 10
 d_S4_GS5_0200 <= 10
 d_S5_GS1_0015 <= 10
 d_S5_GS1_0200 <= 10
 d_S5_GS2_0015 <= 10
 d_S5_GS2_0200 <= 10
 d_S5_GS3_0015 <= 10
 d_S5_GS3_0200 <= 10
 d_S5_GS4_0015 <= 10
 d_S5_GS4_0200 <= 10
 d_S5_GS5_0015 <= 10
 d_S5_GS5_0200 <= 10
 p_S1_0000 <= 100
 p_S1_0005 <= 100
 p_S1_0015 <= 100
 p_S1_0130 <= 100
 p_S1_0200 <= 100
 p_S2_0000 <= 100
 p_S2_0005 <= 100
 p_S2_0015 <= 100
 p_S2_0130 <= 100
 p_S2_0200 <= 100
 p_S3_0000 <= 100
 p_S3_0005 <= 100
 p_S3_0015 <= 100
 p_S3_0130 <= 100
 p_S3_0200 <= 100
 p_S4_0000 <= 100
 p_S4_0005 <= 100
 p_S4_0015 <= 100
 p_S4_0130 <= 100
 p_S4_0200 <= 100
 p_S5_0000 <= 100
 p_S5_0005 <= 100
 p_S5_0015 <= 100
 p_S5_0130 <= 100
 p_S5_0200 <= 100
Binaries
 x_S1_T1_0000 x_S1_T1_0005 x_S1_T1_0130 x_S1_T2_0000 x_S1_T2_0005
 x_S1_T2_0130 x_S1_T3_0000 x_S1_T3_0005 x_S1_T3_0130 x_S1_T4_0000
 x_S1_T4_0005 x_S1_T4_0130 x_S1_T5_0000 x_S1_T5_0005 x_S1_T5_0130
 x_S2_T1_0000 x_S2_T1_0005 x_S2_T1_0130 x_S2_T2_0000 x_S2_T2_0005
 x_S2_T2_0130 x_S2_T3_0000 x_S2_T3_0005 x_S2_T3_0130 x_S2_T4_0000
 x_S2_T4_0005 x_S2_T4_0130 x_S2_T5_0000 x_S2_T5_0005 x_S2_T5_0130
 x_S3_T1_0000 x_S3_T1_0005 x_S3_T1_0130 x_S3_T2_0000 x_S3_T2_0005
 x_S3_T2_0130 x_S3_T3_0000 x_S3_T3_0005 x_S3_T3_0130 x_S3_T4_0000
 x_S3_T4_0005 x_S3_T4_0130 x_S3_T5_0000 x_S3_T5_0005 x_S3_T5_0130
 x_S4_T1_0000 x_S4_T1_0005 x_S4_T1_0130 x_S4_T2_0000 x_S4_T2_0005
 x_S4_T2_0130 x_S4_T3_0000 x_S4_T3_0005 x_S4_T3_0130 x_S4_T4_0000
 x_S4_T4_0005 x_S4_T4_0130 x_S4_T5_0000 x_S4_T5_0005 x_S4_T5_0130
 x_S5_T1_0000 x_S5_T1_0005 x_S5_T1_0130 x_S5_T2_0000 x_S5_T2_0005
 x_S5_T2_0130 x_S5_T3_0000 x_S5_T3_0005 x_S5_T3_0130 x_S5_T4_0000
 x_S5_T4_0005 x_S5_T4_0130 x_S5_T5_0000 x_S5_T5_0005 x_S5_T5_0130
 y_S1_GS1_0015 y_S1_GS1_0200 y_S1_GS2_0015 y_S1_GS2_0200 y_S1_GS3_0015
 y_S1_GS3_0200 y_S1_GS4_0015 y_S1_GS4_0200 y_S1_GS5_0015 y_S1_GS5_0200
 y_S2_GS1_0015 y_S2_GS1_0200 y_S2_GS2_0015 y_S2_GS2_0200 y_S2_GS3_0015
 y_S2_GS3_0200 y_S2_GS4_0015 y_S2_GS4_0200 y_S2_GS5_0015 y_S2_GS5_0200
 y_S3_GS1_0015 y_S3_GS1_0200 y_S3_GS2_0015 y_S3_GS2_0200 y_S3_GS3_0015
 y_S3_GS3_0200 y_S3_GS4_0015 y_S3_GS4_0200 y_S3_GS5_0015 y_S3_GS5_0200
 y_S4_GS1_0015 y_S4_GS1_0200 y_S4_GS2_0015 y_S4_GS2_0200 y_S4_GS3_0015
 y_S4_GS3_0200 y_S4_GS4_0015 y_S4_GS4_0200 y_S4_GS5_0015 y_S4_GS5_0200
 y_S5_GS1_0015 y_S5_GS1_0200 y_S5_GS2_0015 y_S5_GS2_0200 y_S5_GS3_0015
 y_S5_GS3_0200 y_S5_GS4_0015 y_S5_GS4_0200 y_S5_GS5_0015 y_S5_GS5_0200
End

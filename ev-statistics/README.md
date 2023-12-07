# EV statistics calculations

Simple script to calculate EV trip statistics for a single trip data file recorder using [Car Scanner ELM OBD2](https://play.google.com/store/apps/details?id=com.ovz.carscanner&hl=en&gl=US) 
app connected to EV via [ELM327](https://www.alza.sk/mobilly-obd-ii-bt-d4624328.htm) OBD bluetooth adapter. One CSV file is one trip.

To calculate statistics from data file:
```
./ev-stats.py <data-file.csv>
```

## Actual Stats Calculations
| Variable        | Description                                                        |
|-----------------|--------------------------------------------------------------------|
| trip total time | total trip time                                                    |
| power consumed  | total power consumtion for a trip in kWh                           |
| trip distance   | trip distance in km                                                |
| avg. speed      | average trip speed in km/h                                         |
| avg. consumtion | average power consumption in kWh per 100km for the trip conditions |
| avg. amb. temp. | average ambient temperature in ℃                                   |
| avg. bat. temp. | average battery temperature in ℃                                   |
| battery SoH     | battery State of Health for the trip in %                          |
| max battery cap.| estimated max. battery capacity for the trip in kWh                |
| max range estim.| estimated max. range for trip conditions in km                     |

### Trip: 2023-12-07 12:41:33.csv
| Variable        | Value                                      |
|-----------------|--------------------------------------------|
| trip time       |  0:30:20.867000 |
| power consumed  |  2.87 kWh   |
| distance        |  16.18 km   |
| avg. speed      |  32.31 km/h   |
| avg. consumtion |  17.76 kWh/100km   |
| avg. amb. temp. |  -0.16 ℃   |
| avg. bat. temp. |  4.45 ℃   |
| battery SoH     |  99.12 %   |
| max battery cap.|  43.68 kWh   |
| max range estim.|  245.98 km   |

### Trip: 2023-12-04 07:13:19
| Variable        | Value                                      |
|-----------------|--------------------------------------------|
| trip total time |  0:31:00.886000 |
| power consumed  |  2.7 kWh   |
| trip distance   |  13.64 km   |
| avg. speed      |  26.5 km/h   |
| avg. consumtion |  19.83 kWh/100km   |
| avg. amb. temp. |  -2.48 ℃   |
| avg. bat. temp. |  5.0 ℃   |
| battery SoH     |  98.44 %   |
| max battery cap.|  43.9 kWh   |
| max range estim.|  221.37 km   |

### Trip: 2023-12-02 09:33:16 ZA Reference 01
| Variable        | Value                                      |
|-----------------|--------------------------------------------|
| trip total time |  0:25:28.143000 |
| power consumed  |  3.41 kWh   |
| trip distance   |  19.43 km   |
| avg. speed      |  45.93 km/h   |
| avg. consumtion |  17.56 kWh/100km   |
| avg. amb. temp. |  -0.07 ℃   |
| avg. bat. temp. |  7.0 ℃   |
| battery SoH     |  98.44 %   |
| max battery cap.|  44.19 kWh   |
| max range estim.|  251.68 km   |

### Trip: 2023-11-19 12:40:45
| Variable        | Value                                      |
|-----------------|--------------------------------------------|
| trip total time |  0:48:52.798000 |
| power consumed  |  4.31 kWh   |
| trip distance   |  20.6 km   |
| avg. speed      |  30.92 km/h   |
| avg. consumtion |  20.92 kWh/100km   |
| avg. amb. temp. |  1.32 ℃   |
| avg. bat. temp. |  9.18 ℃   |
| battery SoH     |  99.25 %   |
| max battery cap.|  44.19 kWh   |
| max range estim.|  211.21 km   |






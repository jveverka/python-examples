# EV statistics calculation

Simple script to calculate EV statrictics for a single trip data recorder using [Car Scanner ELM OBD2](https://play.google.com/store/apps/details?id=com.ovz.carscanner&hl=en&gl=US) app connected to EV via [ELM327](https://www.alza.sk/mobilly-obd-ii-bt-d4624328.htm) OBD adapter.
One CSV file is one trip.

```
./ev-stats.py <data-file.csv>
```

## Stats calculations
### 2023-12-02 09:33:16 ZA Reference 01
trip time       :  0:25:28.143000
power consumed  :  3.41 kWh
distance        :  19.43 km
avg. speed      :  45.93 km/h
avg. consumtion :  17.56 kWh/100km
avg. amb. temp. :  -0.07 ℃
avg. bat. temp. :  7.0 ℃


### 2023-12-04 07:13:19
trip time       :  0:31:00.886000
power consumed  :  2.7 kWh
distance        :  13.64 km
avg. speed      :  26.5 km/h
avg. consumtion :  19.83 kWh/100km
avg. amb. temp. :  -2.48 ℃
avg. bat. temp. :  5.0 ℃


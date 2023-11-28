#!/usr/bin/env python3

import csv
from datetime import datetime

with open('2023-11-28_22-42-22.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    power_timestamp_old = None
    power_old = None
    counter = 0
    power_summary = 0
    time_summary = 0
    start_time = None
    end_time = None

    speed_timestamp_old = None
    speed_old = None
    distance_total = 0
    
    for row in reader:
        
        counter = counter + 1
        timestring = row['time']
        powerstring = row['HV EV Battery Power (kW)'] 
        speedstring = row['Vehicle speed (km/h)']
        df = datetime.strptime(timestring,'%H:%M:%S.%f')
        seconds = float(df.hour*3600) + float(df.minute*60) + float(df.second) + float(df.microsecond)/1000000
        if not start_time:
           start_time = df 
        end_time = df
        
        if powerstring:
        
            power = float(powerstring)
            
            if power_timestamp_old:
               time_delta = seconds - power_timestamp_old
               power_kwh = power_old * (time_delta/3600) 
               power_summary = power_summary + power_kwh
               time_summary = time_summary + time_delta
               print("calculating power: ", timestring, time_delta, power_old, power_kwh)

            power_timestamp_old = seconds
            power_old = power
        
        if speedstring:
        
           speed = float(speedstring)
           
           if speed_timestamp_old:
              time_delta = seconds - speed_timestamp_old
              distance = speed_old * (time_delta/3600)
              distance_total = distance_total + distance
           
           speed_timestamp_old = seconds
           speed_old = speed


time_interval = end_time - start_time
print("power   : ", time_interval, power_summary, "kWh")
print("distance: ", time_interval, distance_total, "km")
 


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import cartopy.io.shapereader as shpreader

np.set_printoptions(threshold=sys.maxsize)

pd.set_option('display.max_columns', None)
input = pd.read_csv('tlc_yellow_trips_2018_11_22.csv')
print(input.shape[0])
input = input.drop('vendor_id',1)# removed these as they seem irrelevant
input = input.drop('store_and_fwd_flag',1)

# remove all voided trips
input = input[input['payment_type']!=6]

# remove trips with no total_amount
input = input[input['fare_amount']>0.]

# remove trips with no passenger
input = input[input['passenger_count']!=0]

# remove trips with no distance
input = input[input['trip_distance']!=0.]

input['pickup_datetime']=pd.to_datetime(input['pickup_datetime'])
input['dropoff_datetime']=pd.to_datetime(input['dropoff_datetime'])

input['duration_min'] = (np.array(input['dropoff_datetime']) - np.array(input['pickup_datetime'])).astype(float)/(60*1000000000)

# remove trips which seem to have start and end time switched
input = input[input['duration_min']<1380.]

# remove trips with zero time
input = input[input['duration_min']>0.]

# creation of 'speed' column
input['speed_mph'] = (np.array(input['trip_distance'])*60)/np.array(input['duration_min'])

# removing outliers
def remove_outliers(df, key):
    q1 = df[key].quantile(q=0.25)
    q3 = df[key].quantile(q=0.75)

    df = df[df[key] > (q1 - 3. * (q3 - q1))]
    df = df[df[key] < (q3 + 3. * (q3 - q1))]

    return df

input = remove_outliers(input, 'speed_mph')
input = remove_outliers(input, 'trip_distance')
input = remove_outliers(input, 'duration_min')
input = remove_outliers(input, 'total_amount')

# filter out those not in NYC (or at least not in the shapefiles)
shpfilename = '/home/Earth/mfalls/Downloads/junior-data-scientist-test-data-team-master/tlc_yellow_geom.shp'
reader = shpreader.Reader(shpfilename)
zones = reader.records()
zone_ids = []
for zone in zones:
    zone_ids.append(int(zone.attributes['zone_id']))

input = input[input['pickup_location_id'].isin(zone_ids)]
input = input[input['dropoff_location_id'].isin(zone_ids)]

#print(input.head())

input.to_csv('tlc_yellow_trips_2018_11_22_CLEAN.csv')

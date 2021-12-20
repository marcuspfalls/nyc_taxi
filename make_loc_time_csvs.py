import pandas as pd
import numpy as np
import cartopy.io.shapereader as shpreader

input = pd.read_csv('tlc_yellow_trips_2018_11_22_CLEAN.csv')
print(input.head())

input['pickup_datetime']=pd.to_datetime(input['pickup_datetime'])
input['dropoff_datetime']=pd.to_datetime(input['dropoff_datetime'])

shpfilename = '/home/Earth/mfalls/Downloads/junior-data-scientist-test-data-team-master/tlc_yellow_geom.shp'
reader = shpreader.Reader(shpfilename)
zones = reader.records()
zone_ids = []
for zone in zones:
    zone_ids.append(int(zone.attributes['zone_id']))
zone_ids = sorted(zone_ids)
n = len(zone_ids)

pickup = pd.DataFrame({'zone_id':zone_ids, 'all':np.zeros((n))})
dropoff = pd.DataFrame({'zone_id':zone_ids, 'all':np.zeros((n))})
pickup = pickup.set_index('zone_id')
dropoff = dropoff.set_index('zone_id')

for h in range(24):
    pickup[str(h)] = np.zeros((n))
    dropoff[str(h)] = np.zeros((n))
for r in range(input.shape[0]):
    #print(r)
    puID = input['pickup_location_id'][r]
    doID = input['dropoff_location_id'][r]
    puH = input['pickup_datetime'][r].hour
    doH = input['dropoff_datetime'][r].hour
    pickup['all'][puID] = pickup['all'][puID] + 1
    pickup[str(puH)][puID] = pickup[str(puH)][puID] + 1
    dropoff['all'][doID] = dropoff['all'][doID] + 1
    dropoff[str(doH)][doID] = dropoff[str(doH)][doID] + 1

pickup.to_csv('pickup_timeplace.csv')
dropoff.to_csv('dropoff_timeplace.csv')


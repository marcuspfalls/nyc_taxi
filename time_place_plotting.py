import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import pandas as pd
import numpy as np
from shapely.geometry import MultiPolygon
import math as m

pickup = pd.read_csv('pickup_timeplace.csv')
dropoff = pd.read_csv('dropoff_timeplace.csv')
zone_ids = np.array(pickup['zone_id'])
pickup = pickup.set_index('zone_id')
dropoff = dropoff.set_index('zone_id')
pickmax = np.max(pickup.to_numpy()[:,1:])
dropmax = np.max(dropoff.to_numpy()[:,1:])
hourlymax = max([pickmax,dropmax])

datas = [pickup,dropoff]
names = ['pickup','dropoff']

for i in range(2):
    data = datas[i]
    name = names[i]
    fig, ax = plt.subplots(4,6,figsize=[12.8,9.6])
    fig.tight_layout()
    for h in range(24):
        j=m.floor(h/6)
        i=h%6
        ax = plt.subplot(4, 6, h+1, projection=ccrs.PlateCarree())
        ax.set_extent([-74.27, -73.68, 40.48, 40.92], ccrs.PlateCarree())
        shpfilename = '/home/Earth/mfalls/Downloads/junior-data-scientist-test-data-team-master/tlc_yellow_geom.shp'
        reader = shpreader.Reader(shpfilename)
        zones = reader.records()
        for zone in zones:
            zid = zone.attributes['zone_id']
            if zid not in ['56', '103']:
                r = data[str(h)][int(zid)]
                try:
                    if r == 0:
                        ax.add_geometries(zone.geometry, ccrs.PlateCarree(), facecolor='#FFFFFF', linewidth=0.1,
                                          edgecolor="black")
                    elif 0 < r and r <= 100:
                        ax.add_geometries(zone.geometry, ccrs.PlateCarree(), facecolor='#FFECEC', linewidth=0.1,
                                          edgecolor="black")
                    elif 100 < r and r <= 200:
                        ax.add_geometries(zone.geometry, ccrs.PlateCarree(), facecolor='#FFB5B5', linewidth=0.1,
                                          edgecolor="black")
                    elif 200 < r and r <= 300:
                        ax.add_geometries(zone.geometry, ccrs.PlateCarree(), facecolor='#ff7575', linewidth=0.1,
                                          edgecolor="black")
                    elif 300 < r and r <= 400:
                        ax.add_geometries(zone.geometry, ccrs.PlateCarree(), facecolor='#FF2D2D', linewidth=0.1,
                                          edgecolor="black")
                    elif 400 < r and r <= 500:
                        ax.add_geometries(zone.geometry, ccrs.PlateCarree(), facecolor='#EA0000', linewidth=0.1,
                                          edgecolor="black")
                    elif  r > 500:
                        ax.add_geometries(zone.geometry, ccrs.PlateCarree(), facecolor='#AE0000', linewidth=0.1,
                                          edgecolor="black")
                except Exception as e:
                    list_str_polygons = [str(zone.geometry)]
                    c = MultiPolygon(map(wkt.loads, list_str_polygons))
                    if r == 0:
                        ax.add_geometries(c, ccrs.PlateCarree(), facecolor='#FFFFFF', linewidth=0.1, edgecolor="black")
                    elif 0 < r and r <= 100:
                        ax.add_geometries(c, ccrs.PlateCarree(), facecolor='#FFECEC', linewidth=0.1, edgecolor="black")
                    elif 100 < r and r <= 200:
                        ax.add_geometries(c, ccrs.PlateCarree(), facecolor='#FFB5B5', linewidth=0.1, edgecolor="black")
                    elif 200 < r and r <= 300:
                        ax.add_geometries(c, ccrs.PlateCarree(), facecolor='#ff7575', linewidth=0.1, edgecolor="black")
                    elif 300 < r and r <= 400:
                        ax.add_geometries(c, ccrs.PlateCarree(), facecolor='#FF2D2D', linewidth=0.1, edgecolor="black")
                    elif 400 < r and r <= 500:
                        ax.add_geometries(c, ccrs.PlateCarree(), facecolor='#EA0000', linewidth=0.1, edgecolor="black")
                    elif r > 500:
                        ax.add_geometries(c, ccrs.PlateCarree(), facecolor='#AE0000', linewidth=0.1, edgecolor="black")

        ax.set_title(str(h)+ '.00-' + str(h+1) + '.00')

    print(name + '_locs_hourly.png')
    plt.show()
    plt.savefig(name + '_locs_hourly.png')

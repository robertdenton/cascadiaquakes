### Alert

import requests
import time, datetime

r = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson')
json = r.json()

quakes = json['features']

for quake in quakes:
    #print(quake['id'])
    #print(quake['properties']['place'])
    quakeid         = quake['id']
    mag             = quake['properties']['mag']
    loc             = quake['properties']['place']
    url             = quake['properties']['url']
    tsu             = quake['properties']['tsunami']
    


# Disregarding for now, pytz looks to be best way to handle if I want easy way in future
# epoch time conversion: https://docs.python.org/3/library/time.html?highlight=time#time.localtime
# datetime formatting: https://docs.python.org/3/library/time.html?highlight=time#time.strftime
# time is in milliseconds so need to /1000: https://earthquake.usgs.gov/data/comcat/data-eventterms.php#time
# deltasecs       = (quake['properties']['time'] / 1000)
# print(deltasecs)
# gmt             = time.gmtime(deltasecs)
# print(gmt)
# pacific         = time.localtime(gmt)
# print(pacific)

# mdy             = time.strftime('%m-%d-%Y', pacific)
# time            = time.strftime('%H:%M', pacific)
# update_time     = time.strftime('%H:%M', pacific)
# print(quake_mdy)

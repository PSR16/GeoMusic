import json
from pandas.io.json import json_normalize
import pandas as pd
import datetime


file = "Location History.json"

with open(file) as f:
    jsonF = json.load(f)

locations = json_normalize(jsonF['locations'])
locations.drop(['activity', 'altitude', 'heading', 'velocity', 'verticalAccuracy'], axis=1,inplace=True)

locations['Latitude'] = locations['latitudeE7']/10000000
locations['Longitude'] = locations['longitudeE7']/10000000
locations['timestamp'] = pd.to_datetime((locations['timestampMs']).astype(int), unit='ms')
print(locations.head(10))

locations.to_csv('location_info.csv')

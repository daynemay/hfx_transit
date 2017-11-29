import requests
import pygtfs

GTFS_URL = "http://gtfs.halifax.ca/realtime/Vehicle/VehiclePositions.pb"


from google.transit import gtfs_realtime_pb2

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get(GTFS_URL)
feed.ParseFromString(response.content)
for entity in feed.entity:
  print (entity)
  if entity.HasField('trip_update'):
    print ( entity.trip_update)




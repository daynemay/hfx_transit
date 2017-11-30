import requests
from google.transit import gtfs_realtime_pb2

URLS = {
  'vehicle_positions': 'http://gtfs.halifax.ca/realtime/Vehicle/VehiclePositions.pb',
  'alerts': 'http://gtfs.halifax.ca/realtime/Alert/Alerts.pb',
  'trip_updates': 'http://gtfs.halifax.ca/realtime/TripUpdate/TripUpdates.pb'
}


response = requests.get(URLS['vehicle_positions'])

feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(response.content)

for entity in feed.entity:
  print (entity)




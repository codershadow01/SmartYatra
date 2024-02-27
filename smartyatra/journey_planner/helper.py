import pandas as pd  # You might use a proper SQL database instead
from geohash import neighbors 
import geohash
import math
from .models import Nodes
from .models import Edges
import requests
from queue import Queue


def get_geohash(node):
    return node.geohash


# df = pd.DataFrame(list(Nodes.objects.all().values()))
df = pd.DataFrame(Nodes.objects.all(),columns=["Nodes"])
df['geohash'] = df['Nodes'].apply(get_geohash)

# //to find nearby public transport services within 2 km radius
def find_nearest_points(latitude, longitude, precision=7, max_distance=None):
    center_geohash = geohash.encode(latitude, longitude, precision=precision)
    # cur_node = Nodes.objects.create(name='source', lat=latitude, lon=longitude, geohash=center_geohash)
    # print(center_geohash)
    neighbor_geohashes = neighbors(center_geohash) + [center_geohash]

    # Query your database using the geohashes
    # print("Df")
    # print(df)
    nearby_points = df[df['geohash'].isin(neighbor_geohashes)]
    # nearby_nodes = Nodes.objects.filter(geohash=neighbor_geohashes)
    # print("Hello",nearby_points)
    # print(neighbor_geohashes)
    # Calculate exact distances and filter by max_distance
    if max_distance:
        nearby_points['distance'] = nearby_points.apply(
            lambda row: haversine_distance(latitude, longitude, row['latitude'], row['longitude']),
            axis=1
        )
        nearby_points = nearby_points[nearby_points['distance'] <= max_distance]
    # add_edge(nearby_points, cur_node)
    # return nearby_points.to_dict('records')
    return nearby_points 


#to calculate distance between two points
def haversine_distance(lat1, lon1, lat2, lon2):
  # Convert degrees to radians
  lat1 = math.radians(lat1)
  lon1 = math.radians(lon1)
  lat2 = math.radians(lat2)
  lon2 = math.radians(lon2)

  # Define the Earth's radius in kilometers
  earth_radius = 6371

  # Calculate the difference in latitude and longitude
  dlat = lat2 - lat1
  dlon = lon2 - lon1

  # Calculate the square of half the chord length between the points
  a = math.sin(dlat / 2) * math.sin(dlat / 2) + \
      math.cos(lat1) * math.cos(lat2) * \
      math.sin(dlon / 2) * math.sin(dlon / 2) 

  # Calculate the angular distance (central angle) in radians
  c = 2 * math.asin(math.sqrt(a))

  # Calculate the distance in kilometers
  distance = earth_radius * c

  return distance


#to find estimated time between two points
def duration(lat1, lon1, lat2, lon2):
    body = {
        "locations" : [[lat1,lon1],[lat2,lon2]]
        }
    
    print(body)
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        'Authorization': '5b3ce3597851110001cf6248b2b3c6a342184474a0053180d389d68b',
        'Content-Type': 'application/json; charset=utf-8'
    }
    response = requests.post('https://api.openrouteservice.org/v2/matrix/foot-walking', json=body, headers=headers)

    if response.status_code == 200:
        data = response.json()
        durations_matrix = data['durations']

        # Example: Get walking duration from point 1 to point 2 (in seconds)
        walking_duration_1_to_2 = durations_matrix[0][1]  

        return(walking_duration_1_to_2) 
    else:
        print("Error:", response.status_code)


#a*search algorithm to find path between source and destination
        
def search_algo(src1,src2,dest1,dest2,arr1,arr2):
    q = []
    res = []

    center_geohash = geohash.encode(src1, src2, precision=7)
    center_geohash1 = geohash.encode(dest1,dest2,precision=7)
    src = Nodes.objects.create(name='source', lat=src1, lon=src2, geohash=center_geohash)
    dest = Nodes.objects.create(name='destination', lat=dest1, lon=dest2, geohash=center_geohash1)
    


    print("In Search Algo Section")
    # print(arr1)
    for i in range(len(arr1)):
        # print(arr1.iloc[i]['Nodes'])
        q.append((src,arr1.iloc[i]['Nodes']))

    # print(q)
    
    while q:
        cur = q[0]
        q.pop(0)

        # obj = cur[2]
        if cur[1].lat==dest1 and cur[1].lon==dest2:
            res.append((1,cur[0],cur[1]))
            continue

        for i in range(len(arr2)):
            obj = arr2.iloc[i]['Nodes']
            if(obj.lat == cur[1].lat and obj.lon == cur[1].lon):
                res.append((1,cur[0],cur[1]))
                res.append((0,cur[1],dest))
                break


        neighbors = cur[1].outgoing_edges.all() 
        
        for i in neighbors:
            q.append((cur[1],i.node2))


    return res













    
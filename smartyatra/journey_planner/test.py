from .helper import find_nearest_points, search_algo, haversine_distance



# print(haversine_distance(25.26112,82.98376,25.45073,82.85599))
arr1 = find_nearest_points(25.26112,82.98376,7)
arr2 = find_nearest_points(25.45068,82.85594,7)
print(arr1)
print(arr2)
print(search_algo(25.26112,82.98376,25.45068,82.85594, arr1, arr2));


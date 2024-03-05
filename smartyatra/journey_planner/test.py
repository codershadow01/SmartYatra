from .helper import find_nearest_points, search_algo


arr1 = find_nearest_points(25.26121,82.9837,7)
arr2 = find_nearest_points(25.45073,82.85599,7)
print(arr1)
print(arr2)
print(search_algo(25.26121,82.9837,25.45073,82.85599, arr1, arr2));


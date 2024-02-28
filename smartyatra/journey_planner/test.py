from .helper import find_nearest_points, search_algo

arr1 = find_nearest_points(25.31821, 82.97397,7)
arr2 = find_nearest_points(25.31723, 82.96815, 7)

print(search_algo(25.31820, 82.97397, 25.31723, 82.96815, arr1, arr2));
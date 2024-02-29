from .helper import find_nearest_points, search_algo, address_to_latlng


x = address_to_latlng("Varanasi Cantt Bus Stand, Varanasi, India")
y = address_to_latlng("Lehertara, Varanasi, India")
print(x[0])
print(x[1])
print(y[0])
print(y[1])
arr1 = find_nearest_points(x[0],x[1],7)
arr2 = find_nearest_points(y[0],y[1],7)
print("arr1")
print(arr1)
print("arr2")
print(arr2)
print(search_algo(x[0],x[1],y[0],y[1], arr1, arr2));


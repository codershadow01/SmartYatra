from .helper import find_nearest_points, search_algo, address_to_latlng

x = address_to_latlng("Cantt,Varanasi")
y = address_to_latlng("Lehertara,Varanasi")
print(x[0])
print(x[1])
arr1 = find_nearest_points(x[0],x[1], 7)
arr2 = find_nearest_points(y[0],y[1], 7)

print(search_algo(x[0],x[1],y[0],y[1], arr1, arr2));

# res = [
#         [(1, <Nodes: source>, <Nodes: RTO>), (1, <Nodes: source>, <Nodes: source>), (1, <Nodes: source>, <Nodes: source>), (1, <Nodes: source>, <Nodes: source>), (1, <Nodes: RTO>, <Nodes: Babatpur>), (1, <Nodes: Babatpur>, <Nodes: Pindara>), (1, <Nodes: Pindara>, <Nodes: Trilochan Mahadev>), (0, <Nodes: Trilochan Mahadev>, <Nodes: destination>), (1, <Nodes: Pindara>, <Nodes: Trilochan Mahadev>)]
#     ]

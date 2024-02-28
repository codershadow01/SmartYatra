from .helper import find_nearest_points, search_algo

arr1 = find_nearest_points(25.35480, 82.99560,7)
arr2 = find_nearest_points(25.57320, 82.78570, 7)

print(search_algo(25.35480, 82.99560, 25.57320, 82.78570, arr1, arr2));

# res = [
#         [(1, <Nodes: source>, <Nodes: RTO>), (1, <Nodes: source>, <Nodes: source>), (1, <Nodes: source>, <Nodes: source>), (1, <Nodes: source>, <Nodes: source>), (1, <Nodes: RTO>, <Nodes: Babatpur>), (1, <Nodes: Babatpur>, <Nodes: Pindara>), (1, <Nodes: Pindara>, <Nodes: Trilochan Mahadev>), (0, <Nodes: Trilochan Mahadev>, <Nodes: destination>), (1, <Nodes: Pindara>, <Nodes: Trilochan Mahadev>)]
#     ]
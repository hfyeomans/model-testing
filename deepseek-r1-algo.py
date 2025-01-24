import heapq

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 3, 'E': 1},
    'C': {'B': 1, 'D': 5},
    'D': {'E': 2},
    'E': {}
}


def shortest_path(graph, start, end):
    if not graph:
        return None, 0
    
    nodes = list(graph.keys())
    
    distances = {node: float('infinity') for node in nodes}
    distances[start] = 0
    parents = {node: None for node in nodes}
    
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        
        if current_dist > distances[u]:
            continue
        
        if u == end:
            break
        
        for v, weight in graph[u].items():
            if current_dist + weight < distances[v]:
                distances[v] = current_dist + weight
                parents[v] = u
                heapq.heappush(heap, (distances[v], v))
    
    if distances[end] == float('infinity'):
        return None, 0
    
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parents[node]
    
    path.reverse()
    
    total_distance = distances[end]
    
    return (path, total_distance)

assert shortest_path(graph, 'A', 'E') == (['A', 'C', 'B', 'E'], 4)
assert shortest_path(graph, 'A', 'D') == (['A', 'C', 'B', 'D'], 6)


print(shortest_path(graph, 'B', 'E'))

import heapq # a python util for priority queue

def Dijkstra(graph, start):
    """
    Dijkstra's algorithm to find the shortest path from a start node to all other nodes.
    
    :param graph: A dictionary where each key is a node and the value is a list of (neighbor, weight) tuples.
    :param start: The starting node for the algorithm.
    :return: A tuple (shortest_distances, previous_nodes) where:
             - shortest_distances: Dictionary of the shortest distances from the start node to each node.
             - previous_nodes: Dictionary storing the previous node in the shortest path for each node.
    """
    
    # Priority queue for selecting the node with the smallest distance
    pq = [(0, start)]
    
    # Dictionary to store the previous node for each node (for path reconstruction)
    previous_nodes = {node: None for node in graph.keys()}
    
    # Dictionary to store the shortest distance from start node to each node, initially set to infinity
    shortest_distances = {node: float('inf') for node in graph.keys()}
    shortest_distances[start] = 0  # The distance to the start node is 0
    
    # Set to track visited nodes
    visited = set()

    while pq:
        # Pop the node with the smallest tentative distance
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if the node has already been visited
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # Update distances for all neighbors of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < shortest_distances[neighbor]:
                # Update the shortest distance and previous node if a shorter path is found
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                # Push the neighbor to the priority queue with the updated distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_distances, previous_nodes

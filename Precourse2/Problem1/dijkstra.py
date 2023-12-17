import heap


def dijkstra(graph, start):
    """
    calculate the shortest distances from start using dijkstra algorithm, give the graph
    =================================================================================================
    Arguments:
        + graph: info of the graph (nodes, edges)
        + start: the start node
    Outputs:
        + distances: the shortest distances to all nodes from start
    """
    min_heap = heap.MinHeap()
    distances = {node: float("inf") for node in graph}

    distances[start] = 0
    min_heap.push((start, 0))

    while not min_heap.is_empty():
        top_heap = min_heap.pop()
        u, distance_u = top_heap
        if distances[u] != distance_u:
            continue
        for v in graph[u]:
            value_v = distance_u + graph[u][v]
            if distances[v] > value_v:
                distances[v] = value_v
                min_heap.push((v, value_v))

    return distances


if __name__ == "__main__":
    graph = {}
    with open("input_graph.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split()
            node1, node2, weight = line[0], line[1], int(line[2])
            if node1 not in graph:
                graph[node1] = {}
            graph[node1][node2] = weight

    start_node = "A"
    result = dijkstra(graph, start_node)
    print(f"Start Node: {start_node}")
    print(f"Shortest distances: {result}")

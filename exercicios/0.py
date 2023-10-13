# https://www.beecrowd.com.br/judge/pt/problems/view/2550

import heapq

def prim(graph):
    num_vertices = len(graph)
    key = [float('inf')] * num_vertices
    in_mst = [False] * num_vertices
    key[0] = 0
    total_cost = 0

    pq = [(0, 0)]

    while pq:
        cost, u = heapq.heappop(pq)

        if in_mst[u]:
            continue

        in_mst[u] = True
        total_cost += cost

        for v, weight in graph[u]:
            if not in_mst[v] and weight < key[v]:
                key[v] = weight
                heapq.heappush(pq, (key[v], v))

    return total_cost

def minimum_cost_to_connect(N, M, edges):
    graph = [[] for _ in range(N)]

    for a, b, c in edges:
        graph[a-1].append((b-1, c))
        graph[b-1].append((a-1, c))

    total_cost = prim(graph)

    return total_cost

def find_connected_components(N, edges):
    parent = list(range(N))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    for a, b, _ in edges:
        union(a - 1, b - 1)

    components = set()
    for i in range(N):
        components.add(find(i))

    return components

while True:
    try:
        N, M = map(int, input().split())
        edges = [list(map(int, input().split())) for _ in range(M)]

        components = find_connected_components(N, edges)
        if len(components) > 1:
            print("impossivel")
        else:
            result = minimum_cost_to_connect(N, M, edges)
            print(result)

    except EOFError:
        break

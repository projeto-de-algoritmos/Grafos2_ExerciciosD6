# https://www.hackerrank.com/challenges/primsmstsub/problem

import heapq

INFINITY = float('inf')

def prim(n, edges, start):
    graph = {i: [] for i in range(1, n + 1)}
    
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    visitado = set()
    distancia = {i: INFINITY for i in range(1, n + 1)}
    distancia[start] = 0
    total_custo = 0
    pq = [(0, start)]  
    
    while pq and len(visitado) < n:
        dist, u = heapq.heappop(pq)
        if u not in visitado:
            visitado.add(u)
            total_custo += dist
            for vizinho, peso in graph[u]:
                if vizinho not in visitado and peso < distancia[vizinho]:
                    distancia[vizinho] = peso
                    heapq.heappush(pq, (peso, vizinho))
    
    return total_custo

# Entrada
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])
start = int(input())

# executa o prim
result = prim(n, edges, start)

print(result)

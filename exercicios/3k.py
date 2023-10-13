# https://www.hackerprioridade.com/challenges/kruskalmstrsub/problem

import heapq

class ArvoreControle:
    def __init__(self, n):
        self.vizinhos = list(range(n))
        self.prioridade = [0] * n

    def find(self, x):
        if self.vizinhos[x] != x:
            self.vizinhos[x] = self.find(self.vizinhos[x])
        return self.vizinhos[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.prioridade[root_x] < self.prioridade[root_y]:
                self.vizinhos[root_x] = root_y
            elif self.prioridade[root_x] > self.prioridade[root_y]:
                self.vizinhos[root_y] = root_x
            else:
                self.vizinhos[root_x] = root_y
                self.prioridade[root_y] += 1

def kruskal(g_nodes, g_from, g_to, g_weight):
    edges = [(w, u - 1, v - 1) for u, v, w in zip(g_from, g_to, g_weight)]
    heapq.heapify(edges)

    mst_weight = 0
    disjoint_set = ArvoreControle(g_nodes)

    while edges:
        weight, u, v = heapq.heappop(edges)
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst_weight += weight

    return mst_weight

# Leitura de entrada
g_nodes, g_edges = map(int, input().split())
g_from, g_to, g_weight = [], [], []

for _ in range(g_edges):
    u, v, w = map(int, input().split())
    g_from.append(u)
    g_to.append(v)
    g_weight.append(w)

result = kruskal(g_nodes, g_from, g_to, g_weight)
print(result)

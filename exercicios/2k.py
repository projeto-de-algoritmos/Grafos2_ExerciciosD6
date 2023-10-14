# https://www.beecrowd.com.br/judge/pt/problems/view/1152

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

def kruskal(graph, n):
    graph.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    total_cost = 0

    for edge in graph:
        x, y, cost = edge
        if uf.find(x) != uf.find(y):
            uf.union(x, y)
            total_cost += cost

    return total_cost

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    graph = []
    total_length = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        graph.append((x, y, z))
        total_length += z

    cost_saved = total_length - kruskal(graph, m)
    print(cost_saved)

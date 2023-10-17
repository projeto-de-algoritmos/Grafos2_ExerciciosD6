# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/description/
class Solution:
    def minimumWeight(self, n, edges, s1, s2, dest):
        G1 = defaultdict(list)
        G2 = defaultdict(list)

        for a, b, w in edges:
            G1[a].append((b, w))
            G2[b].append((a, w))

        def Dijkstra(graph, K):
            q, t = [(0, K)], {}

            while q:
                time, node = heappop(q)
                if node not in t:
                    t[node] = time
                    for v, p in graph[node]:
                        heappush(q, (time + p, v))
            return [t.get(i, float("inf")) for i in range(n)]

        S1 = Dijkstra(G1, s1)
        S2 = Dijkstra(G1, s2)
        Dest = Dijkstra(G2, dest)

        result = float("inf")

        for i in range(n):
            path_sum = S1[i] + S2[i] + Dest[i]
            result = min(result, path_sum)

        if result == float("inf"):
            return -1
        else:
            return result

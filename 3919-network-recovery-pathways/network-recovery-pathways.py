class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        # Build DAG
        graph = [[] for _ in range(n)]
        indeg = [0] * n

        for u, v, w in edges:
            graph[u].append((v, w))
            indeg[v] += 1

        # Topological ordering
        from collections import deque

        q = deque(i for i in range(n) if indeg[i] == 0)
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # Check if a minimum edge value is feasible
        def feasible(limit: int) -> bool:
            INF = float("inf")
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u not in (0, n - 1) and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    dist[v] = min(dist[v], dist[u] + w)

            return dist[-1] <= k

        # Binary search for maximum minimum edge weight
        lo, hi = 0, 10**9
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if feasible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
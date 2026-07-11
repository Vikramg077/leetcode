from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        # Build adjacency list
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        complete_count = 0

        for node in range(n):
            if visited[node]:
                continue

            stack = [node]
            visited[node] = True
            vertices = 0
            degree_sum = 0

            # Iterative DFS
            while stack:
                current = stack.pop()
                vertices += 1
                degree_sum += len(graph[current])

                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

            # A complete graph with k vertices has k*(k-1) total degree
            if degree_sum == vertices * (vertices - 1):
                complete_count += 1

        return complete_count
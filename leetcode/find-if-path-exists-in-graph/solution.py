from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if n == 1:
            return True
        nodes_edges = {}
        for u,v  in edges:
            if u not in nodes_edges:
                nodes_edges[u] = set()
            nodes_edges[u].add(v)

            if v not in nodes_edges:
                nodes_edges[v] = set()
            nodes_edges[v].add(u)

        visited = {start}
        available = nodes_edges[start]
        to_visit = nodes_edges[start]
        print(nodes_edges)
        while end not in available and to_visit:
            next_node = to_visit.pop()
            print(f"visiting {next_node}")
            visited.add(next_node)
            available = [n for n in nodes_edges[next_node] if n not in visited]
            to_visit = set(list(to_visit) + list(available))
        return end in available

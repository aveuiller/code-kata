from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_count = dict()
        for edge in edges:
            for node in edge:
                if node not in edge_count:
                    edge_count[node] = 1
                else:
                    edge_count[node] += 1
        return max(edge_count, key=edge_count.get)

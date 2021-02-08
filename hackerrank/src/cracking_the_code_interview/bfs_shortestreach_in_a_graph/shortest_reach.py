# Challenge:
# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
from dataclasses import dataclass, field
from queue import Queue

from typing import Dict, List, Set


@dataclass
class Graph:
    size: int
    weight: int = 6
    _edges: Dict[int, List[int]] = field(default_factory=dict)

    def connect(self, x, y):
        connected_to_x = self._edges.setdefault(x, [])
        connected_to_x.append(y)
        connected_to_y = self._edges.setdefault(y, [])
        connected_to_y.append(x)

    def find_all_distances(self, start) -> None:
        distances = {}
        self._find_all_distances_iter(start, distances)
        print(" ".join(list(self._format_result(distances, start))))

    def _find_all_distances(self, start,
                            distances,
                            current_distance=0):
        """
        # Todo: Timeout on 1 test case, use iterative to avoid this.

        :param start:
        :param distances:
        :param current_distance:
        :return:
        """
        # Avoid any call to deeper computation
        if distances.get(start, current_distance) < current_distance:
            return

        for connected in self._edges.get(start, []):
            previous_dist = distances.get(connected, None)
            new_dist = current_distance + self.weight

            if not previous_dist or new_dist < previous_dist:
                distances[connected] = new_dist

                self._find_all_distances(connected, distances,
                                         current_distance + self.weight)

    def _find_all_distances_iter(self, start, distances):
        queue = Queue()
        queue.put(start)

        while not queue.empty():
            node = queue.get()
            node_distance = distances.get(node, 0)
            for connected in self._edges.get(node, []):
                previous_dist = distances.get(connected, None)
                new_dist = node_distance + self.weight

                if not previous_dist or new_dist < previous_dist:
                    distances[connected] = new_dist
                    queue.put(connected)

    def _format_result(self, distances, start):
        for i in range(self.size):
            if i != start:
                yield str(distances.get(i, -1))


def main():
    t = int(input())
    for i in range(t):
        n, m = [int(value) for value in input().split()]
        graph = Graph(n)
        for i in range(m):
            x, y = [int(x) for x in input().split()]
            graph.connect(x - 1, y - 1)
        s = int(input())
        graph.find_all_distances(s - 1)


if __name__ == '__main__':
    main()

"""
Actual:   6 6 6 6 18 6 12 6 12 12 6 6 6 6 6 12 60 6 6 6 6 12 6 18 6 12 6 18 
12 12 12 6 12 12 6 12 12 6 12 6 18 6 12 12 6 6 12 6 6 6 6 12 12 12 12 6 6 6 
12 6 6 12 12 24 18 12 12 6 6
Expected: 6 6 6 6 12 6 12 6 12 12 6 6 6 6 6 12 12 6 6 6 6 12 6 12 6 12 6 12 
12 12 12 6 12 12 6 12 12 6 12 6 12 6 12 12 6 6 12 6 6 6 6 12 12 12 12 6 6 6 
12 6 6 12 12 12 12 12 12 6 6
"""

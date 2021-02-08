#!/bin/python3

import math
import os
import random
import re
import sys
from queue import Queue


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    """
    Challenge: https://www.hackerrank.com/challenges/find-the-nearest-clone

    # For the weighted graph, <name>:
    #
    # 1. The number of nodes is <name>_nodes.
    # 2. The number of edges is <name>_edges.
    # 3. An edge exists between <name>_from[i] to <name>_to[i].
    :param graph_nodes:
    :param graph_from:
    :param graph_to:
    :param ids:
    :param val:
    :return:
    """
    color_nodes, edges = build_data(graph_from, graph_to, ids, val)
    potential = []
    for start in color_nodes:
        result = min_cost(edges, start, color_nodes - {start}, graph_nodes)
        if result > -1:
            potential.append(result)

    return min(potential) if potential else -1


def min_cost(edges, start, ends, graph_nodes):
    to_visit = Queue()
    to_visit.put(start)
    costs = [None] * graph_nodes
    costs[start] = 0

    while not to_visit.empty():
        node = to_visit.get()
        new_cost = costs[node] + 1
        for reachable in edges[node]:
            if not costs[reachable] or costs[reachable] > new_cost:
                costs[reachable] = new_cost
                to_visit.put(reachable)

    potential_costs = [costs[end] for end in ends]
    if not potential_costs:
        return -1
    return min(potential_costs)


def build_data(graph_from, graph_to, ids, val):
    available_nodes = set(i for i, color in enumerate(ids) if color == val)
    edges = {}
    for i, node in enumerate(graph_from):
        other_side = graph_to[i] - 1
        connected = edges.setdefault(node - 1, [])
        connected.append(other_side)
        connected = edges.setdefault(other_side, [])
        connected.append(node - 1)
    return available_nodes, edges


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    graph_nodes, graph_edges = map(int, input().split())
    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges
    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))
    val = int(input())
    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    print(str(ans) + '\n')
    # fptr.write(str(ans) + '\n')
    # fptr.close()


if __name__ == '__main__':
    main()

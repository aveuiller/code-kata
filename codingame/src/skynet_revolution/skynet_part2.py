import sys
import math

DEBUG = True
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
nodes = {}
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    if not nodes.get(n1):
        nodes[n1] = []
    nodes[n1].append(n2)

    if not nodes.get(n2):
        nodes[n2] = []
    nodes[n2].append(n1)

gateways = []
for i in range(e):
    gateways.append(int(input()))  # the index of a gateway node

def _remove_link(n1, n2):
    l1 = nodes[n1]
    l1.remove(n2)
    nodes[n1] = l1

    l2 = nodes[n2]
    l2.remove(n1)
    nodes[n2] = l2


def _get_weight(distance, node, gateway):
    node_urgency = len(set(nodes.get(node, [])).intersection(gateways))
    gateway_urgency = len(nodes.get(gateway, []))
    return distance - (node_urgency + gateway_urgency)


def closest_path(si, available_nodes, distance, visited):
    # Find closest gateways to close
    if DEBUG:
        print(f"Checking from {si} (distance {distance}) nodes {available_nodes}", file=sys.stderr, flush=True)
        print(f"Visited nodes {visited}", file=sys.stderr, flush=True)
    # Limit the amount of checks, there must be a better solution
    if distance > 6:
        return (None, None, distance)

    # Find farther nodes to close
    found = (None, None, 9999)
    concurrent = (None, None, 9999)

    for node in available_nodes:
        if node in gateways:
            return si, node, _get_weight(distance, si, node)

        if DEBUG:
            print(f"Calling for node {node} ({distance}), tmp result: {found}", file=sys.stderr, flush=True)
        # Do not even try if you already have a better solution
        if node not in visited:
            next_nodes = nodes.get(node, [])
            next_weight = _get_weight(distance + 1, node, None)
            concurrent = closest_path(node, next_nodes, next_weight, [si] + available_nodes)
        if concurrent[2] < found[2]:
            found = concurrent

    if DEBUG:
        print(f"Found on check from {si}, distance {distance}: {found}", file=sys.stderr, flush=True)
    return found

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    # Write an action using print
    if DEBUG:
        print(f"Links: {nodes}", file=sys.stderr, flush=True)
        print(f"Gateways: {gateways}", file=sys.stderr, flush=True)
        print(f"Agent: {si}", file=sys.stderr, flush=True)

    # Find closest gateway:
    available = nodes.get(si, [])
    n1, n2, _ = closest_path(si, available, 0, [si])
    _remove_link(n1, n2)

    # print(input(), file=sys.stderr, flush=True)
    print(f"{n1} {n2}")

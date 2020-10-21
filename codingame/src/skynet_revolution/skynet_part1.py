import sys
import math

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

exits = []
for i in range(e):
    exits.append(int(input()))  # the index of a gateway node


def closest_path(si, available_nodes):
    # Find closest exits to close
    for exit in exits:
        if exit in available_nodes:
            return si, exit
    # Find farther nodes to close
    for node in available_nodes:
        return closest_path(node, nodes.get(node, []))

    # Should not happen, but checking anyway
    return None, None

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    # Write an action using print
    print(f"Links: {nodes}", file=sys.stderr, flush=True)
    print(f"Exits: {exits}", file=sys.stderr, flush=True)
    print(f"Agent: {si}", file=sys.stderr, flush=True)

    # Find closest exit:
    available = nodes.get(si, [])
    n1, n2 = closest_path(si, available)

    print(f"{n1} {n2}")
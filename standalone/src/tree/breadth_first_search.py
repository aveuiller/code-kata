from functools import reduce

from src.tree import Node


def bfs(nodes):
    for node in nodes:
        print(node.value)

    next_entry = reduce(lambda coll, x: coll + x.children, nodes, [])
    if next_entry:
        bfs(next_entry)


def main():
    print(f"BFS")
    nodes = [Node(i) for i in range(0, 9)]
    # Layer 1
    nodes[0].children = [nodes[1], nodes[2], nodes[3]]
    # Layer 2
    nodes[1].children = [nodes[4]]
    nodes[2].children = [nodes[5], nodes[6]]
    nodes[3].children = [nodes[7]]
    # Layer 3
    nodes[5].children = [nodes[8]]
    bfs([nodes[0]])

main()

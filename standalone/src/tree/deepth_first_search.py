from src.tree import Node


def dfs(node):
    print(node.value)
    for child in node.children:
        dfs(child)


def main():
    print(f"DFS")
    nodes = [Node(i) for i in range(0, 9)]
    # Layer 1
    nodes[0].children = [nodes[1], nodes[3], nodes[7]]
    # Layer 2
    nodes[1].children = [nodes[2]]
    nodes[3].children = [nodes[4], nodes[6]]
    nodes[7].children = [nodes[8]]
    # Layer 3
    nodes[4].children = [nodes[5]]
    dfs(nodes[0])


main()

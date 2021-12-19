from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Node:
    val: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None


def minimum_depth(root: Node):
    """Returns the min depth from any given node.

    :param root: Node instance
    """
    return _minimum_depth([root])


def _minimum_depth(nodes: List[Node]):
    next_depth = []
    # https://interviewing.io/recordings/Ruby-Amazon-11/O(n)
    for node in nodes:
        # is_null_node
        if not node:
            continue
        # is_leaf
        if not (node.left or node.right):
            return 1
        next_depth += [node.right, node.left]

    return 1 + _minimum_depth(next_depth)


def main():
    root = Node(50,
                Node(30,
                     Node(20),
                     Node(40)),
                Node(70,
                     Node(60),
                     Node(80,
                          Node(75)))
                )

    print(minimum_depth(root))


if __name__ == '__main__':
    main()

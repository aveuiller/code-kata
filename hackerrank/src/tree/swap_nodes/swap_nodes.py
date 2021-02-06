#!/bin/python3
from collections import deque
from dataclasses import dataclass

from typing import Optional


# TODO: Not my solution, get a clear view on this.

@dataclass
class Node:
    info: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None


class Tree:
    root: Node

    def __init__(self, nodes):
        self.root = Node(1)
        f = lambda x: None if x == -1 else Node(x)
        children = [list(map(f, x)) for x in nodes]
        nodes = {n.info: n for n in filter(None, sum(children, []))}
        nodes[1] = self.root
        for idx, child_pair in enumerate(children):
            nodes[idx + 1].left = child_pair[0]
            nodes[idx + 1].right = child_pair[1]

    def in_order_traversal(self):
        stack = []
        curr = self.root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                yield curr.info
                curr = curr.right

    def swap(self, level):
        h = 1
        q = deque([self.root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if h % level == 0:
                    node.left, node.right = node.right, node.left
                q += filter(None, (node.left, node.right))
            h += 1


def swap(tree, index):
    child_level = tree[index - 1]
    tmp = child_level[0]
    child_level[0] = child_level[1]
    child_level[1] = tmp


def swapNodes(nodes, swap_queries):
    """Request to swap k indexes (len(queries) == k)
    where indexes are the tree represented as an array.

    e.g.:
    [1, 2, 3, -1, -1, 2, 1, 1]

    :param nodes:
    :param swap_queries:
    :return:
    """
    printed = []
    tree = Tree(nodes)
    for query in swap_queries:
        tree.swap(query)
        printed.append(list(tree.in_order_traversal()))
    return printed


# Expected
# 3 1 2
# 2 1 3
#     1   [s]       1    [s]       1
#    / \      ->   / \        ->  / \
#   2   3 [s]     3   2  [s]     2   3
TEST_CASE_1_INDEXES = [
    [2, 3],
    [-1, -1],
    [-1, -1]
]
TEST_CASE_1_QUERIES = [1, 1]

# Expected
# 2 9 6 4 1 3 7 5 11 8 10
# 2 6 9 4 1 3 7 5 10 8 11
#         1                     1                          1
#         / \                   / \                        / \
#        /   \                 /   \                      /   \
#       2     3    [s]        2     3                    2     3
#      /      /                \     \                    \     \
#     /      /                  \     \                    \     \
#    4      5          ->        4     5          ->        4     5
#   /      / \                  /     / \                  /     / \
#  /      /   \                /     /   \                /     /   \
# 6      7     8   [s]        6     7     8   [s]        6     7     8
#  \          / \            /           / \              \         / \
#   \        /   \          /           /   \              \       /   \
#    9      10   11        9           11   10              9     10   11
TEST_CASE_2_INDEXES = [
    # Only fills the defined branches
    [2, 3],  # level 2
    [4, -1],  # level 3 (l)
    [5, -1],  # level 3 (r)
    [6, -1],  # level 4 (ll)
    [7, 8],  # level 4 (rl)
    [-1, 9],  # level 5 (lll)
    [-1, -1],  # level 5 (rll)
    [10, 11],  # level 5 (rlr)
    [-1, -1],  # level 6 (lllr)
    [-1, -1],  # level 6 (rlrl)
    [-1, -1]  # level 6 (rlrr)

]
TEST_CASE_2_QUERIES = [2, 4]

if __name__ == '__main__':
    print(swapNodes(TEST_CASE_1_INDEXES, TEST_CASE_1_QUERIES))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     indexes = []
#
#     for _ in range(n):
#         indexes.append(list(map(int, input().rstrip().split())))
#
#     queries_count = int(input())
#
#     queries = []
#
#     for _ in range(queries_count):
#         queries_item = int(input())
#         queries.append(queries_item)
#
#     result = swapNodes(indexes, queries)
#
#     fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
#     fptr.write('\n')
#
#     fptr.close()

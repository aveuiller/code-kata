import math


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    """Print visible nodes of a tree if looked from above
    Challenge: https://www.hackerrank.com/challenges/tree-top-view/problem
   E.g.:
   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4

    Top View: 1 - 2 - 5 - 6

    E.g. 2:
           1
        /     \
       2       3
      /  \    / \
     4    5  6   7

     Top View: 4 - 2 - 1 - 3 - 7
    :param root:
    :return:
    """
    view = {}
    find_top_view(root, 0, 0, view)
    output = [str(view[key]) for key in sorted(view.keys())]
    print(" ".join(output))


def find_top_view(root, h_level, depth, view):
    root.level = depth
    if root.left:
        find_top_view(root.left, h_level - 1, depth + 1, view)

    visible_node = view.get(h_level)
    if not visible_node or visible_node.level > depth:
        view[h_level] = root

    if root.right:
        find_top_view(root.right, h_level + 1, depth + 1, view)

    visible_node = view.get(h_level)
    if not visible_node or visible_node.level > depth:
        view[h_level] = root

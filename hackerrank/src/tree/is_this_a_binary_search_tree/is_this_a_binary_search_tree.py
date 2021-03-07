""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import sys


def checkBST(root):
    """
    # Challenge:
    # https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
    :param root:
    :return:
    """
    return check(root, -sys.maxsize, sys.maxsize)


def check(node, min_v, max_v):
    if node is None:
        return True
    if not(min_v < node.data < max_v):
        return False

    check_left = check(node.left, min_v, node.data)
    check_right = check(node.right, node.data, max_v)
    return check_left and check_right

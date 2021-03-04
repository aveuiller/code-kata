from functools import reduce


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

TEST_CASE_1 = [1, 2, 5, 3, 6, 4]
TEST_CASE_2 = [
    37, 23, 108, 59, 86, 64, 94, 14, 105, 17, 111, 65, 55, 31, 79, 97, 78, 25,
    50, 22, 66, 46, 104, 98, 81, 90, 68, 40, 103, 77, 74, 18, 69, 82, 41, 4,
    48, 83, 67, 6, 2, 95, 54, 100, 99, 84, 34, 88, 27, 72, 32, 62, 9, 56, 109,
    115, 33, 15, 91, 29, 85, 114, 112, 20, 26, 30, 93, 96, 87, 42, 38, 60, 7,
    73, 35, 12, 10, 57, 80, 13, 52, 44, 16, 70, 8, 39, 107, 106, 63, 24, 92,
    45, 75, 116, 5, 61, 49, 101, 71, 11, 53, 43, 102, 110, 1, 58, 36, 28, 76,
    47, 113, 21, 89, 51, 19, 3
]


def levelOrder(root):
    result = []
    levelOrderNodes([root], result)
    print(" ".join(result))


def levelOrderNodes(nodes, result):
    nodes = [n for n in nodes if n]
    for node in nodes:
        result += [str(node.info)]
    children = reduce(lambda coll, x: coll + [x.left, x.right], nodes, [])
    if any(children):
        levelOrderNodes(children, result)


def iterative_level_order(root):
    """Iterative edition"""
    stack_tovisit = [root]
    traversal = []
    while stack_tovisit:
        node = stack_tovisit.pop(0)
        traversal.append(str(node.info))
        if node.left:
            stack_tovisit.append(node.left)
        if node.right:
            stack_tovisit.append(node.right)

    print(" ".join(traversal))

if __name__ == '__main__':
    tree = BinarySearchTree()
    for i in TEST_CASE_2:
        tree.create(i)
    levelOrder(tree.root)

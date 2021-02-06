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


def in_order_traversal(root):
    """Iterative solution"""
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            yield curr.info
            curr = curr.right


def in_ot(root, values):
    """Recursive solution"""
    current = root
    if current.left:
        in_ot(current.left, values)
    values.append(str(current.info))
    if current.right:
        in_ot(current.right, values)


def inOrder(root):
    """
    Node is defined as
    self.left (the left child of the node)
    self.right (the right child of the node)
    self.info (the value of the node)
    """
    # print(" ".join([str(val) for val in in_order_traversal(root)]))
    values = []
    in_ot(root, values)
    print(" ".join(values))


TREE_TEST_1 = [1, 2, 5, 3, 6, 4]
TREE_TEST_2 = [1, 14, 3, 7, 4, 5, 15, 6, 13, 10, 11, 2, 12, 8, 9]


def main():
    tree = BinarySearchTree()
    for val in TREE_TEST_1:
        tree.create(val)
    inOrder(tree.root)


if __name__ == '__main__':
    main()

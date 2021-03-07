class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        node = self.root
        if not node:
            self.root = Node(val)
            self.root.level = 0
        else:
            next_child = self._next_child(node, val)
            while next_child:
                node = next_child
                next_child = self._next_child(node, val)

            if val < node.info:
                node.left = Node(val)
                node.left.level = node.level + 1
            elif val > node.info:
                node.right = Node(val)
                node.right.level = node.level + 1

    @staticmethod
    def _next_child(node, val):
        return node.left if val <= node.info else node.right


TEST_ARRAY_1 = [4, 2, 3, 1, 7, 6]


def main():
    tree = BinarySearchTree()
    # t = int(input())
    # arr = list(map(int, input().split()))

    t = len(TEST_ARRAY_1)
    arr = TEST_ARRAY_1
    for i in range(t):
        tree.insert(arr[i])

    preOrder(tree.root)


if __name__ == '__main__':
    main()

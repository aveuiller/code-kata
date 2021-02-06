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


def post_ot(root, values):
    current = root
    if current.left:
        post_ot(current.left, values)
    if current.right:
        post_ot(current.right, values)
    values.append(str(current.info))


def postOrder(root):
    values = []
    post_ot(root, values)
    print(" ".join(values))


TEST_CASE_1 = [1, 2, 5, 3, 6, 4]


def main():
    tree = BinarySearchTree()
    for val in TEST_CASE_1:
        tree.create(val)
    postOrder(tree.root)


if __name__ == '__main__':
    main()

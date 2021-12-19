from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None


# https://www.youtube.com/watch?v=RblP72t11LQ
def next_inorder(root, node):
    if not root.left and not root.right:
        return root if root.val != node.val else None

    if root.left and root.left.val == node.val:
        return root if not root.left.right else root.left.right
    elif root.left and root.left.val > node.val:
        return next_inorder(root.left, node)
    else:
        return next_inorder(root.right, node)


def prev_inorder(root, node):
    if not (root.left or root.right):
        return root if root.val != node.val else None
    elif root.left and root.left.val == node.val:
        return root.left.left
    elif root.right and root.right.val == node.val:
        return root if not root.right.left else root.right.left
    elif root.right and root.right.val < node.val:
        return prev_inorder(root.right, node)
    else:
        return prev_inorder(root.left, node)


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

    print("From 20:")
    print(f"next: 30? {next_inorder(root, Node(20)).val}")
    print(f"prev: None? {prev_inorder(root, Node(20))}")

    print("From 30:")
    print(f"next: 40? {next_inorder(root, Node(30)).val}")
    print(f"prev: 20? {prev_inorder(root, Node(30)).val}")

    print("From 40:")
    print(f"next: 50? {next_inorder(root, Node(40)).val}")  # FIXME: 60
    print(f"prev: 30? {prev_inorder(root, Node(40)).val}")

    print("From 50:")
    print(f"next: 60? {next_inorder(root, Node(50)).val}")
    print(f"prev: 40? {prev_inorder(root, Node(50)).val}")

    print("From 60:")
    print(f"next: 70? {next_inorder(root, Node(60)).val}")
    print(f"prev: 50? {prev_inorder(root, Node(60)).val}")  # FIXME: 40

    print("From 70:")
    print(f"next: 75? {next_inorder(root, Node(70)).val}")  # FIXME: 80
    print(f"prev: 60? {prev_inorder(root, Node(70)).val}")

    print("From 75:")
    print(f"next: 80? {next_inorder(root, Node(75)).val}")
    print(f"prev: 70? {prev_inorder(root, Node(75)).val}")  # FIXME: 60

    print("From 80:")
    print(f"next: None? {next_inorder(root, Node(80))}")
    print(f"prev: 75? {prev_inorder(root, Node(80)).val}")


if __name__ == '__main__':
    main()

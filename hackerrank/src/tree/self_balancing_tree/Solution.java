package tree.self_balancing_tree;

import Math;

class Node {
    int val;
    int ht;
    Node left;
    Node right;

    public Node() {
    }
}

public class Solution {
    /**
     * Class node is defined as :
     * class Node
     * int val;	//Value
     * int ht;		//Height
     * Node left;	//Left child
     * Node right;	//Right child
     * <p>
     * Example, add 6 to :
     * 3
     * /  \
     * 2    4
     * \
     * 5
     * <p>
     * Result:
     * 3
     * /  \
     * 2    5
     * / \
     * 4   6
     */
    static Node insert(Node root, int val) {
        if (root == null) {
            root = new Node();
            root.val = val;
            root.ht = computeHeight(root);
            return root;
        }

        if (val <= root.val) {
            root.left = insert(root.left, val);
        } else {
            root.right = insert(root.right, val);
        }

        return balance(root);
    }

    private static int computeHeight(Node root) {
        if (root == null) {
            return -1;
        }
        return 1 + Math.max(height(root.left), height(root.right));
    }

    private static Node balance(Node root) {
        int factor = balanceFactor(root);
        if (factor > 1) {
            if (height(root.left.left) < height(root.left.right)) {
                root.left = rotateLeft(root.left);
            }
            root = rotateRight(root);
        } else if (factor < -1) {
            if (height(root.right.right) < height(root.right.left)) {
                root.right = rotateRight(root.right);
            }
            root = rotateLeft(root);
        } else {
            root.ht = computeHeight(root);
        }
        return root;
    }

    private static int balanceFactor(Node root) {
        return height(root.left) - height(root.right);
    }

    private static int height(Node node) {
        if (node == null) {
            return -1;
        }
        return node.ht;
    }

    private static Node rotateRight(Node root) {
        Node newRoot = root.left;
        root.left = newRoot.right;
        newRoot.right = root;

        root.ht = computeHeight(root);
        newRoot.ht = computeHeight(newRoot);
        return newRoot;
    }

    private static Node rotateLeft(Node root) {
        Node newRoot = root.right;
        root.right = newRoot.left;
        newRoot.left = root;

        root.ht = computeHeight(root);
        newRoot.ht = computeHeight(newRoot);
        return newRoot;
    }
}

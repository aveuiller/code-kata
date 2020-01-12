package tree.height_binary_tree;

/**
 * Challenge: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree
 */
public class Solution {
    /*
    class Node
        int data;
        Node left;
        Node right;
    */
    public static int height(Node root) {
        if (root.left == null && root.right == null) {
            return 0;
        }
        int leftHeight = root.left == null ? 0 : height(root.left);
        int rightHeight = root.right == null ? 0 : height(root.right);
        return 1 + Math.max(leftHeight, rightHeight);
    }
}

class Node {
    Node left;
    Node right;
}
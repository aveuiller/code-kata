package linked_list.detect_a_cycle;

import java.util.Collection;
import java.util.HashSet;

/**
 * Challenge: https://www.hackerrank.com/challenges/ctci-linked-list-cycle
 */
public class Solution {

    static class Node {
        int data;
        Node next;
    }

    /*
        Detect a cycle in a linked list. Note that the head pointer may be 'null' if the list is empty.

        A Node is defined as:
            class Node {
                int data;
                Node next;
            }
    */
    boolean hasCycle(Node head) {
        Collection<Node> visitedNodes = new HashSet<>();
        Node current = head;
        while (current != null) {
            if (visitedNodes.contains(current)) {
                return true;
            }
            visitedNodes.add(current);
            current = current.next;
        }
        return false;
    }
}

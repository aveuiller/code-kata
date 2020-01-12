package linked_list.insert_node_simply_linked;

/**
 * Challenge: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list
 */
public class Solution {
    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static SinglyLinkedListNode insertNodeAtPosition(SinglyLinkedListNode head, int data, int position) {
        SinglyLinkedListNode newNode = new SinglyLinkedListNode(data);
        if (head == null) {
            return newNode;
        }

        SinglyLinkedListNode node = head;
        for (int i = 0; i < position - 1; i++) {
            node = node.next;
        }

        newNode.next = node.next;
        node.next = newNode;
        return head;
    }

}

class SinglyLinkedListNode {
    public int data;
    public SinglyLinkedListNode next;

    public SinglyLinkedListNode(int data) {
        this.data = data;
    }
}
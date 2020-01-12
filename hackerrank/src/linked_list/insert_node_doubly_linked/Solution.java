package linked_list.insert_node_doubly_linked;

/**
 * Challenge: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list
 */
public class Solution {
    /*
     * For your reference:
     *
     * DoublyLinkedListNode {
     *     int data;
     *     DoublyLinkedListNode next;
     *     DoublyLinkedListNode prev;
     * }
     *
     */
    static DoublyLinkedListNode sortedInsert(DoublyLinkedListNode head, int data) {
        DoublyLinkedListNode newNode = new DoublyLinkedListNode(data);

        DoublyLinkedListNode prevNode = null;
        DoublyLinkedListNode nextNode = head;
        while (nextNode != null && nextNode.data < data) {
            prevNode = nextNode;
            nextNode = nextNode.next;
        }

        if (nextNode != null) {
            newNode.next = nextNode;
            nextNode.prev = newNode;
        }
        if (prevNode != null) {
            prevNode.next = newNode;
            newNode.prev = prevNode;
        } else {
            return newNode;
        }

        return head;
    }

}

class DoublyLinkedListNode {
    public int data;
    public DoublyLinkedListNode next;
    public DoublyLinkedListNode prev;

    public DoublyLinkedListNode(int data) {
        this.data = data;
    }
}
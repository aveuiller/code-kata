# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        node = result
        l1_current = l1
        l2_current = l2
        remainder = 0

        while l1_current is not None:
            l2_val = l2_current.val if l2_current is not None else 0
            summed = (l1_current.val + l2_val + remainder)
            remainder = summed // 10
            node.val = summed % 10

            node.next = ListNode()
            node = node.next
            l2_current = l2_current.next if l2_current is not None else None
            l1_current = l1_current.next

        while l2_current is not None:
            node.val = l2_current
            node.next = ListNode()
            node = node.next
            l2_current = l2.next

        return result


def testcase():
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]
    l1 = ListNode(2, next=ListNode(4, next=ListNode(3)))
    l2 = ListNode(5, next=ListNode(6, next=ListNode(4)))

    expected = [7, 0, 8]
    result = Solution().addTwoNumbers(l1, l2)

    print(expected)
    print(result)


testcase()

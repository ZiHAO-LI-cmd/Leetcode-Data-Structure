# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newHead = ListNode(-1)
        newHead.next = head
        tmp1 = newHead

        while tmp1 and tmp1.next:
            if tmp1.next.val == val:
                tmp1.next = tmp1.next.next
            else:
                tmp1 = tmp1.next

        return newHead.next

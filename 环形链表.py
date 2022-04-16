# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 哈希
        # if head == None or head.next == None:
        #     return False
        # s = set()
        # while head:
        #     s.add(head)
        #     if head.next in s:
        #         return True
        #     head = head.next
        # return False

        # 快慢指针
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
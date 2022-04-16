# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # newHead = ListNode(-1)
        # tmpHead = newHead
        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         tmpHead.next = list1
        #         list1 = list1.next
        #     else:
        #         tmpHead.next = list2
        #         list2 = list2.next
        #     tmpHead = tmpHead.next
        
        # if list1:
        #     tmpHead.next = list1
        # else:
        #     tmpHead.next = list2
        
        # return newHead.next

        # 递归
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        res = ListNode(0)
        dummy = res
        while l1 and l2:
            curr_val = l1.val + l2.val + rem
            rem = 0
            if curr_val > 9:
                rem = curr_val//10
                val = curr_val%10
            else:
                val = curr_val
            l1 = l1.next
            l2 = l2.next
            res.next = ListNode(val)
            res = res.next
            
        while l1:
            curr_val = l1.val + rem
            rem = 0
            if curr_val > 9:
                rem = curr_val//10
                val = curr_val%10
            else:
                val = curr_val
            l1 = l1.next
            res.next = ListNode(val)
            res = res.next
            
        while l2:
            curr_val = l2.val + rem
            rem = 0
            if curr_val > 9:
                rem = curr_val//10
                val = curr_val%10
            else:
                val = curr_val
            l2 = l2.next
            res.next = ListNode(val)
            res = res.next
        if rem != 0:
            res.next = ListNode(rem)
        return dummy.next
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None 
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        temp.sort()
        res = ListNode()
        dummy = res
        
        for i in temp:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return res.next
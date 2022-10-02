# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        
        while head:
            arr.append(head.val)
            head=head.next
            
        arr.sort()
        
        
        dummy=ListNode(0)
        head=dummy
        
        for i in arr:
            dummy.next=ListNode(i)
            dummy=dummy.next
            
        return head.next   
            
        
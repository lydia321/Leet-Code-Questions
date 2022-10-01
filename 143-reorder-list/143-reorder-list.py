# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #find middle of the linked list
        slow,fast = head,head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #Reversing the list stating from slow
        
        second=slow.next
        
        prev,slow.next=None,None
        
        while second:
            next = second.next
            second.next = prev
            prev = second 
            second = next
            
        #Merging the two lists
        first,second = head , prev
        while second:
            FN = first.next
            SN = second.next       
            first.next = second
            second.next = FN
            first = FN
            second = SN

      
            
            
            
            
        
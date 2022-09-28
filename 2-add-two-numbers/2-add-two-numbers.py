# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output=ListNode()
        curr=output
        reminder=0
        
        while l1 or l2 or reminder:
            if l1:
                v1=l1.val
            else:
                v1=0
            if l2:
                v2=l2.val
            else:
                v2=0
            
            # adding the numbers
            s=v1+v2+reminder
            
            reminder=s //10
            
            s=s%10
            
            curr.next=ListNode(s)             
            curr=curr.next
            
            if l1:
                l1=l1.next
            else:
                l1=None
            if l2:
                l2=l2.next
            else:
                l2=None
            
        return output.next      
            

        
            
            
        
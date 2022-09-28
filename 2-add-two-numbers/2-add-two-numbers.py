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
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            
            # adding the numbers
            s=v1+v2+reminder
            reminder=s //10
            s=s%10
            curr.next=ListNode(s)
            
            #Updating pointers                
            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            
        return output.next      
            

        
            
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output=[]
        dummy=head
        while dummy:
            output.append(dummy.val)
            dummy=dummy.next
            
        m=len(output)//2    
        for i in range(m):
            head=head.next
        return head    
        
        
        
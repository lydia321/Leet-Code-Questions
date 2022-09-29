# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i,j=head,head
        while j:
            if j.val==i.val:
                j=j.next
            else:
                i.next=j
                i=j
                j=j.next
        #if duplicate value is at the end
        
        if i:
            i.next=None
                
        return head    
        
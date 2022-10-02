# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast = head,head.next
        head1=head
        count=0
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        #reverse the second half of the node
        head2=slow.next
        slow.next = None
        prev=None
        
        while head2:
            nextt =head2.next
            head2.next = prev
            prev = head2
            head2 = nextt
        
        H2=prev
        while head1 and H2:
            if head1.val + H2.val > count:
                count = head1.val + H2.val
            
            head1=head1.next
            H2=H2.next
        
        return count
        
        
        
        
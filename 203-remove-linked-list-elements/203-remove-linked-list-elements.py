# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        prev=dummy # Because the element we have to remove might be the first element
        curr=prev.next
        while curr:
            if curr.val==val:
                prev.next=curr.next
                curr=curr.next
            else:
                prev=curr
                curr=curr.next
        return dummy.next       
        
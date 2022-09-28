# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a,b='',''
        while l1:
            a= str(l1.val) +a #to reversee the order
            l1=l1.next
        while l2:
            b=str(l2.val) +b  #to reverse the order
            l2=l2.next
        sum=int(a)+int(b)
        output=ListNode()
        curr=output
        for i in reversed(str(sum)):
            curr.next=ListNode(i)
            curr=curr.next
        return output.next    
            
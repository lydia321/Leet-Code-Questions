# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        
        slow, fast = head, head
        dummy = head
       
          
        for _ in range(n):
             fast=fast.next
                
        # print(fast)
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
           
        # print(fast)
        if fast:
            if slow.next and slow.next.next:
                slow.next=slow.next.next
            else:
                slow.next=None
        else:
            return head.next
                        
        return head    
            
        
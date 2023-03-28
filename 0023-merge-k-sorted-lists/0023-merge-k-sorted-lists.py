# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeList(l1,l2):
            res = ListNode(None)
            dummy = res
            
            while l1 and l2:
                if l1.val > l2.val:
                    dummy.next = l2
                    l2 = l2.next
                else:
                    dummy.next = l1
                    l1 = l1.next
                dummy = dummy.next
            while l1:
                dummy.next = l1
                l1 = l1.next
                dummy = dummy.next
            while l2:
                dummy.next = l2
                l2 = l2.next
                dummy = dummy.next
            return res.next
        
        if len(lists) == 0 or not lists:
            return None
        
        queue = lists
        
        while len(queue) > 1:
            l1 = queue.pop(0)
            l2 = queue.pop(0)
            
            potential_res = mergeList(l1,l2)
            queue.append(potential_res)
        return queue[0]
    
                
                
        
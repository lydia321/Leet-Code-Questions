# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or not list:
            return None
        
        def mergeList(l1,l2):
            res = ListNode(None)
            dummy = res
            
            # when both l1 and l2 exits
            while l1 and l2:
                if l1.val > l2.val:
                    dummy.next = l2
                    l2 = l2.next
                else:
                    dummy.next = l1
                    l1 = l1.next
                dummy = dummy.next
                        
            #leftover l1
            while l1:
                dummy.next = l1
                l1 = l1.next
                dummy = dummy.next
                
            #leftover l2
            while l2:
                dummy.next = l2
                l2 = l2.next
                dummy = dummy.next
            
            return res.next
        
        queue = lists
        while len(queue) > 1:
            list1 = queue.pop()
            list2 = queue.pop()
            
            queue.append(mergeList(list1,list2))
        return queue[0]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        res = dummy
        
        while list1 and list2:
            if list1.val > list2.val:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            dummy = dummy.next
        # if remaining values in list1
        while list1:
            dummy.next = list1
            list1 = list1.next
            dummy = dummy.next
         # if remaining values in list2
        while list2:
            dummy.next = list2
            list2 = list2.next
            dummy = dummy.next
        return res.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = ListNode(0)
#         dummy = res
#         while list1 and list2:
#             if list1.val < list2.val:
#                 res.next = list1
#                 list1 = list1.next
#             else:
#                 res.next = list2
#                 list2 = list2.next
#             res = res.next
        
#         while list1:
#             res.next = list1
#             list1 = list1.next
#             res = res.next
        
#         while list2:
#             res.next = list2
#             list2 = list2.next
#             res = res.next
#         return dummy.next
            
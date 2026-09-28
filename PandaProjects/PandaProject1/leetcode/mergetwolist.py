from itertools import chain
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2 == []:
            return []
        c = list(chain(list1,list2))
        c.sort()
        return c
print(Solution.mergeTwoLists(Solution,[1,2,4],[1,3,4]))
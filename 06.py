"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        small_list = len(list1) >= len(list2)
        combined_list = []
        for char in list1:
            if len(list1)>0:
                len(list2)>0:
                    if list1[0] <=  list2[0]:

                        #min_elem = min(list1[0]), list2[0]))
                        list1.pop(0).append(combined_list)

                    else:
                        list2.pop(0).append(combined_list)


            #first element

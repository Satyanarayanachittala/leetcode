# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        x = headA
        y = headB

        while x != y:
            x = x.next if x else headB
            y = y.next if y else headA
        
        return x
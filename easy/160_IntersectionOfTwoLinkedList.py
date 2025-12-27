# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return
        
        cur_A = headA
        cur_B = headB

        while cur_A is not cur_B:
            if cur_A:
                cur_A = cur_A.next
            else:
                cur_A = headB
            
            if cur_B:
                cur_B = cur_B.next
            else:
                cur_B = headA
            
        return cur_A
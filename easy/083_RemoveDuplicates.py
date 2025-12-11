# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        dummy = ListNode()
        cur = dummy
        cur.next = head
        head = head.next
        cur = cur.next
        while head:
            if cur.val == head.val:
                head=head.next
            else:
                cur.next = head
                head = head.next
                cur = cur.next
        cur.next = None
        return dummy.next
        
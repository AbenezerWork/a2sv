# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        even = head
        odd = head.next
        trav = head
        prev = head.next
        while (prev and prev.next):
            trav.next = trav.next.next
            trav = trav.next
            prev.next = prev.next.next
            prev = prev.next
        if trav:
            trav.next = None
        prev = even
        while prev.next:
            prev = prev.next
        prev.next = odd
        return even
            
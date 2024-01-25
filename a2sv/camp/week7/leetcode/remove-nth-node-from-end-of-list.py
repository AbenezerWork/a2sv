# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        trav = head
        rem = head
        i =0
        while i<n+1 and trav:
            trav = trav.next
            i+=1
        if i<n+1:
            return head.next
        while trav:
            trav = trav.next
            rem = rem.next
        rem.next = rem.next.next
        return head
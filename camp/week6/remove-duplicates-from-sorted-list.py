# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, next = head, head
        while next:
            while next and prev.val == next.val:
                next = next.next
            prev.next = next
            prev = next
        return head
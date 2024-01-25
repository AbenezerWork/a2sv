# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        trav = head
        while trav.next:
            curr = head
            while curr.next:
                if curr.val>=x and x>curr.next.val:
                    curr.val,curr.next.val = curr.next.val, curr.val
                
                curr = curr.next
            trav = trav.next
        return head
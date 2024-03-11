# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        trav = dummy

        for i in range(left-1):
            trav = trav.next
        prev = None
        curr = trav.next
        for i in range(left,right+1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        trav.next.next = curr
        trav.next = prev
        return dummy.next
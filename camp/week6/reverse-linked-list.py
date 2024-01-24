# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        prev,next,last = None,head,head.next
        while next.next!=None:
            next.next = prev
            prev = next
            next = last
            last = last.next
        next.next = prev
        return next
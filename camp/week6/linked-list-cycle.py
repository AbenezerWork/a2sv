# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast  = head
        curr =0
        while fast!=None:
            if curr%2:
                slow = slow.next
            fast = fast.next
            if slow == fast:
                return True
            curr+=1
        return False

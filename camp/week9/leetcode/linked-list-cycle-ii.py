# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                ans = 0
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                    ans +=1
                break
        if fast and fast.next:
            return fast
        return
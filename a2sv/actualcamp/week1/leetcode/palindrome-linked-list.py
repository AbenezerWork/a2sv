# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        curr = slow
        prev = None

        while curr.next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        curr.next = prev

        while head.next:
            if head.val!= curr.val:
                return False
            curr = curr.next
            head = head.next
        return True

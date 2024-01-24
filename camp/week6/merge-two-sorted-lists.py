# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        one, two = list1, list2
        ans = None
        if list1.val>list2.val:
            ans = two
            two = two.next
        else:
            ans = one
            one = one.next
        curr = ans
        while one and two:
            if one.val<two.val:
                curr.next = one
                one = one.next
            else:
                curr.next = two
                two = two.next
            curr = curr.next

        if one:
            curr.next = one
        else:
            curr.next = two
            
        return ans
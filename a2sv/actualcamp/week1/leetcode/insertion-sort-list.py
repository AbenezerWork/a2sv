# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-float('inf'))
        dummy.next = head
        trav = dummy

        while trav and trav.next:
            if trav.val> trav.next.val:
                curr = trav.next
                sor = dummy
                nxt = trav.next.next

                while sor and sor.next:
                    if sor.next.val > curr.val:
                        tmp = sor.next
                        sor.next = curr
                        curr.next = tmp
                        break
                    sor = sor.next
                
                trav.next = nxt
            else:
                trav = trav.next
        return dummy.next

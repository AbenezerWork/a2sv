# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n= 0
        trav = head
        while trav:
            n+=1
            trav =trav.next
        length = n//k
        x = n%k
        ans = []
        trav = ListNode(0,head)
        print(length)

        for i in range(k):
            if trav:
                tmp = trav.next
                trav.next = None
                trav = tmp
            ans.append(trav)
            if not x:
                length-=1
            x-=1
            for j in range(length):
                if trav:
                    trav = trav.next
                else:break

        return ans
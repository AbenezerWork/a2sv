# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stk = [root]
        ans = 0
        
        while stk:
            curr = stk.pop()
            if curr:
                if curr.val<=high and curr.val>=low:
                    ans+=curr.val
                stk.extend([curr.left, curr.right])
        return ans
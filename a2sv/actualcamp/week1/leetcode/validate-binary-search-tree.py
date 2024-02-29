# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mx = -float("inf")
        def recc(r):
            nonlocal mx
            if not r:
                return True
            left =  recc(r.left)
            if r.val<=mx:
                return False
            mx = r.val
            right = recc(r.right)
            return left and right
        return recc(root)

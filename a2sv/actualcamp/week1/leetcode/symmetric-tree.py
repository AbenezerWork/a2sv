# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        ans = True
        def rec(r, rr):
            nonlocal ans
            if not r and not rr:
                return True
            elif not r or not rr:
                ans = False
                return False
            rec(r.left,rr.right)
            print(r.val, rr.val)
            if r.val!=rr.val:
                ans =False
                return False
            rec(r.right, rr.left)
        rec(root, root)
        return ans
            
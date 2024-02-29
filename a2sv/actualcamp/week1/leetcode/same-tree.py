# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recc(p,q):
            if not p or not q:
                if not p and not q:
                    return True
                else:
                    return False
            ans = recc(p.left,q.left)
            ans1 = recc(p.right,q.right)
            return ans and ans1 and (p.val == q.val)
        return recc(p,q)
        
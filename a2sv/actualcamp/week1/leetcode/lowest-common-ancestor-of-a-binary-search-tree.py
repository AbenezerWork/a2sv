# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recc(r, p,q):
            if r.val >=p.val and r.val<=q.val:
                return r
            elif r.val>p.val:
                return recc(r.left, p,q)
            else:
                return recc(r.right,p,q)
        if p.val<q.val:
            return recc(root, p,q)
        else:
            return recc(root, q,p)
            
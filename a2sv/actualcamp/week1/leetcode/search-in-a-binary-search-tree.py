# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def recc(r,v):
            if not r:
                return 
            print(r.val)
            if r.val>v:
                return recc(r.left,v)
            elif r.val<v:
                return recc(r.right, v)
            else:
                return r
        return recc(root,val)

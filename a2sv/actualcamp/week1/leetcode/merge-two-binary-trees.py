# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            if root1:
                root2 = TreeNode(0)
            elif root2:
                root1 = TreeNode(0)
            
        def recc(r1, r2):
            if not r1 and not r2:
                return

            r1.val+=r2.val
            if r2.left and not r1.left:
                r1.left = TreeNode(0)
            elif r1.left and not r2.left:
                r2.left = TreeNode(0)
            
            recc(r1.left, r2.left)

            if r2.right and not r1.right:
                r1.right = TreeNode(0)
            elif r1.right and not r2.right:
                r2.right = TreeNode(0)

            recc(r1.right, r2.right)
        recc(root1, root2)

        return root1

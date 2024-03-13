# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recc(left, right, dist):

            if left and right:
                one = recc(left.left,right.right,dist*2)
                two = recc(left.right, right.right, dist*2-1)
                three = recc(left.right, right.left, dist*2-2)
                four = recc(left.left, right.left, dist*2-1)
                return max(one, two, three, four)
            else:
                return dist
        return recc(root, root, 1)//2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        def recc(l, r):
            if r-l==1:
                return None
            
            mid = l + (r - l) // 2
            node = TreeNode(nums[mid])
            node.left = recc(l, mid)
            node.right = recc(mid, r)
            return node
        
        return recc(-1, len(nums))
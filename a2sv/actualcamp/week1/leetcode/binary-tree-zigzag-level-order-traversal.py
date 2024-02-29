# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        m = defaultdict(list)

        def recc(r, d):
            nonlocal m
            if not r:
                return
            recc(r.left, d+1)
            m[d].append(r.val)
            recc(r.right, d+1)
        recc(root,0)
        i = 0
        ans = []
        while m[i]:

            if i%2:
                ans.append(reversed(m[i]))
            else:
                ans.append(m[i])
            i+=1
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        m = defaultdict(int)
        mx = [0]
        def solve(root, mx, m):
            if not root:
                return 
            solve(root.left, mx, m)
            m[root.val]+=1
            mx[0] = max(m[root.val], mx[0])
            solve(root.right, mx, m)
        solve(root,mx,m)
        print(mx, m)

        ans = []
        for key in m.keys():
            if m[key]==mx[0]:
                ans.append(key)
        return ans



        
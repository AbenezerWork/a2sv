class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        ans =0
        for c in s:
            if c == '(':
                stk.append(c)
            else:
                if len(stk):
                    stk.pop()
                else:
                    ans+=1
        return ans+len(stk)
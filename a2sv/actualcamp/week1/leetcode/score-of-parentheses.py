class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        stk = []
        for ch in s:
            if ch == '(':
                stk.append(ch)
            else:
                if stk[-1] !='(':
                    cumm = 0
                    while stk and stk[-1]!='(':
                        cumm+=stk.pop()
                    stk.pop()
                    stk.append(cumm*2)
                else:
                    stk[-1] = 1
        return sum(stk)
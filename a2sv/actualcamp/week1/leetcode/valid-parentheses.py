class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == "(" or c == '{' or c == "[":
                stk.append(c)
            else:
                if len(stk) and ((stk[-1] == "{" and c == '}') or (stk[-1] == "(" and c == ')') or (stk[-1] == "[" and c == ']')):
                    stk.pop()
                else:
                    return False
        return len(stk) == 0
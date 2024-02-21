class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for ch in tokens:
            #print(stk)
            if ch not in "+-*/":
                stk.append(int(ch))
            else:
                ans = 0
                if ch == '+':
                    ans = int(stk[-1])+int(stk[-2])
                if ch == '-':
                    ans = int(stk[-2])-int(stk[-1])
                if ch == '*':
                    ans = int(stk[-1])*int(stk[-2])
                if ch == '/':
                    ans = int(stk[-2])/int(stk[-1])
                stk[-2] = ans
                stk.pop()
        return int(stk[0])
                
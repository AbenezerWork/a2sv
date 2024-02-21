class Solution:
    def simplifyPath(self, path: str) -> str:
        path = (path.split('/'))
        stk = []
        for dr in path:
            if dr == "..":
                if len(stk):
                    stk.pop()
            elif len(dr) and dr!='.':
                stk.append(dr)

        res = ['/', "/".join(stk)]
        return "".join(res)
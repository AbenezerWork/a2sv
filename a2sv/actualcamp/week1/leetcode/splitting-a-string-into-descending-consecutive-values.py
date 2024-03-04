class Solution:
    def splitString(self, s: str) -> bool:
        def rec(curr, idx):
            if idx== len(s):
                for i in range(1, len(curr)):
                    if curr[i-1]-curr[i] != 1:
                        return False
                return len(curr)>=2
            
            for i in range(idx, len(s)):
                val = int(s[idx:i+1])
                if not curr or curr[-1]-val==1:
                    curr.append(val)
                else:
                    continue
                val = rec(curr, i+1)
                if val:
                    return True
                curr.pop()
            return False
        return rec([],0)


class Solution:
    def minimumRecolors(self, b: str, k: int) -> int:
        j = 0
        curr = 0
        mx = float("inf")
        for i in range(len(b)):
            if b[i] == 'W':
                curr+=1
            if i>=k:
                if b[i-k] == "W":
                    curr-=1
            if i+1>=k:
                mx = min(mx,curr)
        
        return mx
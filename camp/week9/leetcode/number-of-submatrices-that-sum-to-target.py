class Solution:
    def numSubmatrixSumTarget(self, pref: List[List[int]], target: int) -> int:
        row , col = len(pref), len(pref[0])
        for r in range(row):
            for c in range(col):
                top = pref[r-1][c] if r !=0 else 0
                left = pref[r][c-1] if c !=0 else 0
                intersection = pref[r-1][c-1] if r!=0 and c!=0 else 0
                pref[r][c] +=(-intersection+left+top)
        res=0
        for r1 in range(row):
            for r2 in range(r1,row):
                seen = defaultdict(int)
                seen[0]=1
                for c in range(col):
                    top = pref[r1-1][c] if r1!=0 else 0
                    cur = pref[r2][c]
                    res+=seen[(cur-top)-target]
                    seen[cur-top]+=1
        return res
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = defaultdict(int)
        check = defaultdict(int)
        for c in s1:
            check[c]+=1
        for i in range(len(s2)):
            d[s2[i]]+=1
            if i >= len(s1):
                d[s2[i-len(s1)]]-=1
                if d[s2[i-len(s1)]]==0:
                    del(d[s2[i-len(s1)]])
            if check == d:
                return True
        return False
            
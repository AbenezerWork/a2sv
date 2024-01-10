class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        k,n =len(p),len(s)

        if k>n:
            return []

        dic = defaultdict(int)
        win = defaultdict(int)
        for i in range(k):
            dic[p[i]]+=1
            win[s[i]]+=1
        if dic == win:
            ans.append(0)
        for i in range(k,n):
            win[s[i-k]]-=1
            if win[s[i-k]]==0:
                del(win[s[i-k]])
            win[s[i]] +=1
            if dic == win:
                ans.append(i-k+1)
        return ans
            

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        j = ans = 0
        for i in range(len(fruits)):
            d[fruits[i]]+=1
            while len(d)>2:
                d[fruits[j]]-=1
                if d[fruits[j]]==0:
                    del(d[fruits[j]])
                j+=1
            ans = max(ans,i-j+1)
        return ans
            
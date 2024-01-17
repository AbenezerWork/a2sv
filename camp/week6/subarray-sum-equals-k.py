class Solution:
    def subarraySum(self, n: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0]+=1
        curr = 0
        count = 0
        for i in range(0,len(n)):
            curr+=n[i]
            count+=dic[curr-k]
            dic[curr]+=1
        return count
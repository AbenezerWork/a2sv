class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pref = [0]*(len(nums)+1)
        for req in requests:
            pref[req[0]]+=1
            pref[req[1]+1]-=1
        for i in range(1,len(pref)):
            pref[i]+=pref[i-1]
        nums.sort()
        pref = pref[:-1]
        pref.sort()
        ans = 0
        mod = 1e9+7
        for i in range(len(nums)):
            ans = (ans+(pref[i]*nums[i]))%mod
        print(ans%mod)
        return int(ans)
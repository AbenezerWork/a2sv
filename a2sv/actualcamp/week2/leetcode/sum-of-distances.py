class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        count = defaultdict(int)
        pref =  defaultdict(int)
        lastSeen = {}
        for i in range(len(nums)):

            if nums[i] in lastSeen:
                pref[nums[i]] += (i-lastSeen[nums[i]])*count[nums[i]]
                ans[i] +=pref[nums[i]]
            count[nums[i]] += 1
            lastSeen[nums[i]]=i

        count = defaultdict(int)
        pref =  defaultdict(int)
        lastSeen = {}
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in lastSeen:
                pref[nums[i]] += (lastSeen[nums[i]]-i)*count[nums[i]]
                ans[i] +=pref[nums[i]]
            count[nums[i]] += 1
            lastSeen[nums[i]]=i
        return ans
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        sett = set(nums)
        mx = 0
        while sett:
            piv = sett.pop()
            curr = piv
            count = 0
            while curr+1 in sett:
                curr+=1
                count+=1
                sett.remove(curr)
            curr = piv
            while curr-1 in sett:
                curr-=1
                sett.remove(curr)
                count+=1
            count+=1
            mx = max(count, mx)
        return mx
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = True
        ans = []
        lastneg = -1
        lastpos = -1
        while len(ans)<len(nums):
            if pos:
                for i in range(lastpos+1,len(nums)):
                    if nums[i]>0:
                        ans.append(nums[i])
                        pos = False
                        lastpos = i
                        break
                        
            if not pos:
                for i in range(lastneg+1,len(nums)):
                    if nums[i]<0:
                        pos = True
                        lastneg = i
                        ans.append(nums[i])
                        break
        return ans
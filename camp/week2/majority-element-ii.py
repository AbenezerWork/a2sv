class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        check = len(nums)//3
        dic = {}
        ans = []
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic:
            if dic[i] > check:
                ans.append(i)
    
        return ans
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        check = len(nums)//3
        dic = {}
        ans = set()
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
            if dic[i]>check:
                ans.add(i)
        
    
        return list(ans)
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        print(-2%6)
        for i in range(len(nums)):
            s = set()
            curr = i
            par = nums[i]/abs(nums[i])
            #print(par)
            step = 1
            while True:
                if nums[curr]/abs(nums[curr]) != par or (curr in s and step == 1) or curr == (curr+nums[curr])%len(nums):
                    break
                if curr in s and step != 1:
                    return True
                s.add(curr)
                curr = (curr+nums[curr])%len(nums)
                step+=1
                #print(curr,nums[i])
        return False
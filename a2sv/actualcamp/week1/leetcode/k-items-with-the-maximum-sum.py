class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        while k:
            if numOnes:
                numOnes-=1
                ans+=1
                k-=1
                continue
            if numZeros:
                numZeros-=1
                k-=1
                continue
            if numNegOnes:
                ans-=1
                k-=1
                numNegOnes-=1
        return ans
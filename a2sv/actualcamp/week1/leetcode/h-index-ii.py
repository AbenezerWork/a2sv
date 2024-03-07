class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        left, right = -1, len(citations)

        while left + 1 <  right:
            mid = left+(right-left)//2
            print(mid)
            if mid < len(citations) and len(citations)-mid > citations[mid]:
                left = mid
            else:
                right = mid

        return len(citations)-left-1
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r = -1,len(letters)
        while l+1<r:
            mid = l+(r-l)//2
            if letters[mid]<=target:
                l = mid
            else:
                r = mid
        if l+1 == len(letters):
            return letters[0]
        return letters[l+1]
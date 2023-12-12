class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        check = len(arr)/4
        i = 0
        if len(arr)==1:
            return arr[0]
        while i < (len(arr)-1):
            curr = 0
            while i<len(arr)-1 and arr[i]==arr[i+1] :
                curr+=1
                i+=1
            curr+=1
            if curr>check:
                return arr[i]
            i+=1
        return 0
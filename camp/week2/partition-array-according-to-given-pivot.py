class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivcount = 0
        arr1 = []
        arr2 = []
        for i in nums:
            if i<pivot:
                arr1.append(i)
            elif i>pivot:
                arr2.append(i)
            else:
                pivcount+=1
        arr1 += pivcount*[pivot]
        return arr1+arr2
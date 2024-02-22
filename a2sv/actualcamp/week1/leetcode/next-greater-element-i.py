class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        d = {}
        for i in range(len(nums2)):
            while stk and stk[-1]<nums2[i]:
                d[stk.pop()] = nums2[i]
            stk.append(nums2[i])
        
        for i in range(len(nums1)):
            if nums1[i] in d:
                nums1[i] = d[nums1[i]]
            else:
                nums1[i] = -1
        return nums1



                
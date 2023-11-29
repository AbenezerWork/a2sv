class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num%3:
            return []
        else:
            return [-1+num/3,num/3,1+num/3]
        
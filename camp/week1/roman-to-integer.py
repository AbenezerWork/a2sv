class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        return s.count('I') +s.count('V')*5 + s.count('X')*10 + s.count("L")*50 + s.count("C")*100 + s.count("D")*500 + s.count("M")*1000 - s.count("IV")*2 - 2*s.count("IX") - s.count("XL")*20 - s.count("XC")*20 - s.count("CD")*200 - s.count("CM")*200
        # prev = s[-1]
        # for c in s[-2::-1]:
        #     if c == "I" and prev = "V" or c ==
        # return 0

        
        
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        mx = 0
        mxstr = ''
        for i in range(len(num[0:len(num)-2])):
            if num[i]==num[i+1] and num[i] == num[i+2]:
                if mx<=int(num[i:i+3]):
                    mxstr = num[i:i+3]
                    mx = int(num[i:i+3])
        return mxstr
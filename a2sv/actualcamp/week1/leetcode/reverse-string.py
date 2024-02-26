class Solution:
    def reverseString(self, s: List[str]) :
        self.reverse(s, 0, len(s)-1)
        
    def reverse(self, s, start, end):
        if start >= end:
            return s
        s[start], s[end] = s[end], s[start]
        start+=1
        end-=1
        return self.reverse(s, start,end)
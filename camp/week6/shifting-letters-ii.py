class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans =[0]*(len(s)+1)
        for q in shifts:
            ans[q[0]]+=q[2]*2+-1
            ans[q[1]+1]-=q[2]*2+-1
        
        val = [0]*len(s)
        for i in range(1,len(ans)):
            ans[i] = ans[i-1]+ans[i]
            val[i-1] = ord(s[i-1])
        
        for i in range(len(val)):
            val[i] += ans[i]
            val[i] = chr(ord('a')+((val[i]-ord('a'))%26))
        return "".join(val)
        
        


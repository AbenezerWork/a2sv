class Solution:
    def printVertically(self, s: str) -> List[str]:
        mx = 0
        s = s.split(" ")
        for c in s:
            mx = max(len(c), mx)
        ans = []
        print(s)
        for i in range(mx):
            string = ""
            j = 0
            cutt = 0
            for j in range(len(s)):
                if len(s[j])>i:
                    string+=s[j][i]
                    cutt = j
                else:
                    string+=" "
            if cutt+1 == len(s):
                ans.append(string)
            else:
                ans.append(string[:cutt+1])
        return ans 


            
        
            
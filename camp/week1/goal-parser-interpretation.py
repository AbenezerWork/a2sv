class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans =""
        prev = ""
        for ch in command:
            if prev == "":
                prev = ch
                continue
            if prev == '(' and ch == ")":
                ans+='o'
            elif prev == 'l':
                ans+="al"
            elif prev == "G":
                ans+= "G"
            prev = ch
        if prev == "G":
            ans+= "G"
        return ans

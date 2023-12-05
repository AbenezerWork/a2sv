class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        base = ord('0')
        nm1 = 0
        digits1 = len(num1)
        for ch in num1:
            dig = ord(ch)-base
            nm1+=dig*10**(digits1-1)
            digits1-=1
        nm2 = 0
        digits2 = len(num2)
        for ch in num2:
            dig = ord(ch)-base
            nm2+=dig*10**(digits2-1)
            digits2-=1

        return str(nm1*nm2)
        
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        j,i = 0,0
        curr = ""
        if len(name)>len(typed):
            return False
        while j<len(typed) and i< len(name):
            if name[i] != typed[j]:
                return False
            curr = name[i]
            while i<len(name) and j<len(typed) and name[i] == curr and name[i] == typed[j]:
                i+=1
                j+=1
            
            if len(name) == i or len(typed) == j:
                break

            if typed[j] != curr and name[i] == curr:
                return False
            while j<len(typed) and  curr == typed[j]:
                j+=1
        while j<len(typed) and typed[j] == curr:
            j+=1
        return len(typed[j:]) == 0 and len(name[i:]) == 0
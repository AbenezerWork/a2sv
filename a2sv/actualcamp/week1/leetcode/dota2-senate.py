class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s = deque()
        r = deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else :
                s.append(i)
        while len(s) and len(r):
            if s[0]>r[0]:
                r.append(r.popleft()+len(senate))
                s.popleft()
            else:
                s.append(s.popleft()+len(senate))
                r.popleft()
            

        if len(s):
            return "Dire"
        return "Radiant"
            

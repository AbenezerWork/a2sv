class Solution:
    def bestClosingTime(self, customers: str) -> int:
        count = customers.count('Y')
        pen = 0
        n = len(customers)
        mn = count
        sc = 0
        for i,c in enumerate(customers):
            if c == 'Y':
                count-=1
            else:
                pen+=1

            if (pen+count)<mn:
                mn = pen+count
                sc = i+1
        return sc

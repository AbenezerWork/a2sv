class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for i in bills:
            if i == 5:
                fives+=1
            if i == 10:
                tens+=1
                if not fives:
                    return False
                fives-=1
            if i == 20:
                if tens and fives:
                    tens-=1
                    fives-=1
                elif fives>=3:
                    fives-=3
                else:
                    return False
        return True


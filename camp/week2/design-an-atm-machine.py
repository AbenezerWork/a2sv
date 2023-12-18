class ATM:

    def __init__(self):
        self.money = [0]*5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.money[i]+=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        denom = [20,50,100,200,500]
        uses = [0]*5
        money= self.money.copy()
        for i in range(4,-1,-1):
            if denom[i]<=amount and money[i]>0:
                tmp = amount//denom[i]
                leftOver = tmp-money[i]
                if tmp>money[i]:
                    amount -= money[i]*denom[i]
                    uses[i]+=money[i]
                    money[i]=0
                else:
                    money[i]-=tmp
                    amount-=tmp*denom[i]
                    uses[i]+=tmp
            if amount==0:
                self.money= money
                break

        return [-1] if amount != 0 else uses


        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
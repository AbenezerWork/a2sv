class MinStack:

    def __init__(self):
        self.stk = []
        self.basic = []
        self.it = 0
        

    def push(self, val: int) -> None:
        self.basic.append(val)
        if not self.stk or  val<self.stk[-1][0]:
            self.stk.append([val,self.it])
        self.it+=1
        

    def pop(self) -> None:
        if self.stk[-1][1] == self.it-1:
            self.stk.pop()
        self.it-=1
        self.basic.pop()

    def top(self) -> int:
        return self.basic[-1]
        

    def getMin(self) -> int:
        return self.stk[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
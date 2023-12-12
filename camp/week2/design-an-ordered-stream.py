class OrderedStream:

    def __init__(self, n: int):
        self.arr = [0]*n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1]=value
        ret = []
        while self.pointer< len(self.arr) and self.arr[self.pointer] != 0:
            ret.append(self.arr[self.pointer])
            self.pointer+=1
        return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
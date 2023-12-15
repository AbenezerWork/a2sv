class Bitset:

    def __init__(self, size: int):
        self.ones = set()
        self.zeros = set()
        for i in range(size):
            self.zeros.add(i)

    def fix(self, idx: int) -> None:
        self.zeros.discard(idx)
        self.ones.add(idx)

    def unfix(self, idx: int) -> None:
        self.zeros.add(idx)
        self.ones.discard(idx)

    def flip(self) -> None:
        tmp = self.ones
        self.ones = self.zeros
        self.zeros = tmp

    def all(self) -> bool:
        return len(self.zeros)==0

    def one(self) -> bool:
        return len(self.ones)

    def count(self) -> int:
        return len(self.ones)

    def toString(self) -> str:
        n = len(self.ones)+len(self.zeros)
        ans = []
        for i in range(n):
            if i in self.ones:
                ans.append('1')
            else:
                ans.append('0')
        return ''.join(ans)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
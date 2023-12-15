class FrequencyTracker:
    def __init__(self):
        self.count = defaultdict(int)
        self.freq = defaultdict(int)
        

    def add(self, number: int) -> None:

        self.freq[self.count[number]] -= 1 
        self.count[number] += 1
        self.freq[self.count[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.count:
            self.freq[self.count[number]] -= 1
            self.count[number] += -1
            self.freq[self.count[number]] += 1

            if self.count[number]==0:
                del (self.count[number])
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency]

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
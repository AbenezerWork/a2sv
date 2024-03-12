class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = deque()
        deck.sort(reverse = True)
        d.append(deck[0])
        for i in range(1,len(deck)):
            d.appendleft(d.pop())
            d.appendleft(deck[i])
        return d

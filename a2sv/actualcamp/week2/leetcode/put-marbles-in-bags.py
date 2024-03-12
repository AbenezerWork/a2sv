class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        parts = []
        for i in range(1,len(weights)):
            parts.append(weights[i]+weights[i-1])
        parts.sort()
        print(parts)
        return sum(parts[len(parts)-k+1:])-sum(parts[:k-1])
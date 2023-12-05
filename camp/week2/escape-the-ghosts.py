class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        minDist = float("inf")
        for ghost in ghosts:
            minDist = min(minDist, (abs(ghost[0]-target[0])+abs(ghost[1]-target[1])))
        print(minDist)
        return (abs(target[0])+abs(target[1]))<minDist
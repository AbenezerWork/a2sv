class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        curr = capacity
        steps = 0
        for i in range(len(plants)):
            if curr >= plants[i]:
                curr-=plants[i]
            else:
                print(steps, i)
                steps += 2*(i)
                curr = capacity
                curr-=plants[i]
            steps+=1
        return steps

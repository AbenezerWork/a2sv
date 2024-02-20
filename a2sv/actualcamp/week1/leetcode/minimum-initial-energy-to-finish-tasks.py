class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        ans = 0
        energy = 0
        tasks.sort(key=lambda x: x[0]-x[1])
        print(tasks)
        for i in range(len(tasks)):
            if energy >= tasks[i][1]:
                energy -= tasks[i][0]
            else:
                ans += tasks[i][1] - energy 
                energy = tasks[i][1] - tasks[i][0]
        return ans
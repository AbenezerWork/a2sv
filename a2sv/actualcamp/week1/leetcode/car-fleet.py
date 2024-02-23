class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        iota = [i for i in range(len(position))]
        iota.sort(key = lambda x: position[x])
        times = []

        for i in range(len(position)):
            times.append((target-position[i])/speed[i])
        mx = 0
        ans = 0
        stk = []
        for i in iota:
            while stk and stk[-1]<=times[i]:
                stk.pop()
            stk.append(times[i])


        return len(stk)


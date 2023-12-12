class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        dic = defaultdict(int)
        ans = set([2001])
        for i in range(len(backs)):
            if backs[i]==fronts[i]:
                dic[fronts[i]]=1

        for i in range(len(backs)):
            if fronts[i] not in dic:
                ans.add(fronts[i])
            if backs[i] not in dic:
                ans.add(backs[i])

        return 0 if min(ans)==2001 else min(ans)
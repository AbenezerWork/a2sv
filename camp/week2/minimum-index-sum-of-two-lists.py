class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}

        for i in range(len(list1)):
            dic[list1[i]] = i
        mn = float('inf')
        ans = []
        for i in range(len(list2)):
            if list2[i] in dic:
                if mn > dic[list2[i]]+i:
                    mn = dic[list2[i]]+i
                    ans = [list2[i]]
                elif mn == dic[list2[i]]+i:
                    ans.append(list2[i])
        return ans

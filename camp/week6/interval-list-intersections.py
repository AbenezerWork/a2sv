class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        ans = []

        while i<len(firstList) and j<len(secondList):
            fl,sl = firstList[i],secondList[j]
            if fl[0]<=sl[1] and sl[0]<=fl[1]:
                ans.append([max(fl[0],sl[0]),min(fl[1],sl[1])])

            if fl[1]>sl[1]:
                j+=1
            else:
                i+=1
        return ans

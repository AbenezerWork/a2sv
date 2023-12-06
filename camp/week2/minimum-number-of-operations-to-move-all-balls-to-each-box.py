class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        arr = []
        for i in range(len(boxes)):
            if boxes[i]=='1':
                arr.append(i)
        ans = []
        for i in range(len(boxes)):
            tmp = 0
            for j in arr:
                tmp += abs(j-i)
            ans.append(tmp)
        return ans
        
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        curr  = -1
        count = 0
        ans = 0
        for i in range(len(answers)):
            if answers[i] == curr and count<curr+1:
                count+=1
            else:
                ans +=answers[i]+1
                curr  = answers[i]
                count = 1
        return ans
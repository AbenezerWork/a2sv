class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        length = min(len(word1), len(word2))
        ans= ""
        for i in range(length):
            ans+=word1[i] +word2[i]
        ans += word1[length:]+word2[length:]
        return ans
        
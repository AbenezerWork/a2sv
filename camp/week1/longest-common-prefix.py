class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        check = strs[0]
        for string in strs:
            tmp = ""
            for i in range(len(string)):
                if i<len(check) and string[i]==check[i]:
                    tmp+=string[i]
                else:
                    break
            check = tmp
        return check
        
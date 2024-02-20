class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        check = Counter(s)
        win = Counter(s)
        ans = [0]
        last  =-1
        for i in range(len(s)):
            win[s[i]]-=1
            br = True
            for key in check.keys():
                if win[key] and check[key]!=win[key]:
                    br = False
            if br:
                ans.append(i-last)
                last=i
        return ans[1:]
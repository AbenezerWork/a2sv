class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        count = Counter(s)
        st = set()
        for i in range(len(s)):
            while stk and count[stk[-1]]>=1 and s[i]<stk[-1] and s[i] not in st:
                st.remove(stk[-1])
                stk.pop()

            count[s[i]]-=1
            if s[i] not in st:
                stk.append(s[i])
                st.add(s[i])
        print(stk)
        return ''.join(stk)
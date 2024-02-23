class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stk = []
        ans = 0
        for i in range(len(arr)):
            while stk and arr[stk[-1]]>arr[i]:
                curr = stk.pop()
                prev = -1
                if stk:
                    prev = stk[-1]
                mul=i-curr
                left=(curr-prev)
                right=mul
                ans+=left*right*arr[curr]
            stk.append(i)
            

        while stk:
            curr = stk.pop()
            prev = -1
            if stk:
                prev = stk[-1]
            mul=len(arr)-curr
            left=(curr-prev)
            right=mul
            ans += left*right*arr[curr]
        
        return int(ans%(1e9+7))
            
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+1)
        for p in bookings:
            ans[p[0]-1]+=p[2]
            ans[p[1]]-=p[2]
        for i in range(1,n+1):
            ans[i] += ans[i-1]
        return ans[:-1]
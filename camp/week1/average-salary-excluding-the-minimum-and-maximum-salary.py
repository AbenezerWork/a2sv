class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        sm = 0
        mx = -float("inf")
        mn = float("inf")
        for curr in salary:
            mn = min(mn, curr)
            mx = max(mx, curr)
            sm+=curr
        print len(salary), mx, mn, sm
        
        return (sm-mx-mn)/float(len(salary)-2)

        
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def checker(t):
    low = a[0]-b[0]*t
    high = a[0]+b[0]*t
    for i in range(n):
        low = max(a[i]-b[i]*t, low)
        high = min(a[i]+b[i]*t, high)
        if high < low:
            return False
    return True


l, r = 0, 1e10

while r-l > 1e-6:
    mid = l+(r-l)/2
    # print(mid)
    if checker(mid):
        # print(mid)
        r = mid
    else:
        l = mid
print(r)

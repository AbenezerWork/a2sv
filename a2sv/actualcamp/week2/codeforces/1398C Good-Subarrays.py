t =int(input())
from collections import defaultdict
for _ in range(t):
    n = int(input())
    a = input()
    d = defaultdict(int)
    tot =0
    ans = 0
    d[1]=1
    for i in range(n):
        tot+=int(a[i])
        ans += d[tot-i]
        d[tot-i]+=1

    print(ans)
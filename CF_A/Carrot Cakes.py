import math
n, t ,k ,d= list(map(int,input().split()))

one =math.ceil(n/k) 
second = math.floor(d/t)
if second >= one:
    print("No")
else:
    print("YES")


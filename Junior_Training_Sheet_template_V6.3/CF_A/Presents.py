n = int(input())
array = list(map(int,input().split()))

for i in range(1,n+1):
    print(array.index(i) + 1, end = " ")
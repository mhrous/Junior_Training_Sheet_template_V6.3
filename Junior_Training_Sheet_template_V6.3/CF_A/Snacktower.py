n=int(input())
s=set()
a=map(int,input().split())
for i in a:
    s.add(i)
    while n in s:
        print(n,end=' ')
        n-=1
    print()
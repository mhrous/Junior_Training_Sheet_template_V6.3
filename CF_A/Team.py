n = int(input())

count = 0

while n > 0:
    n -= 1
    _sum = sum(map(int,input().split()))
    if(_sum >= 2):
        count += 1

print(count) 
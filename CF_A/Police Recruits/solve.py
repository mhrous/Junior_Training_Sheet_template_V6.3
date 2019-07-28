n = int(input())
array = list(map(int,input().split()))

police = 0
count = 0

for num in array:
    if num != -1:
        police += num
    elif police > 0:
        police -= 1
    else:
        count += 1

print(count)
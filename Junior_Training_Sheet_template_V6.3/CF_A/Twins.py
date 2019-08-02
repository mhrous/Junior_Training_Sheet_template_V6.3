n = int(input())

array =sorted(list(map(int, input().split())))

count = 0
half = sum(array) // 2
_sum = 0



for index in range(n-1, -1, -1):
    _sum += array[index]

    count += 1
    if _sum > half:
        break

print(count)


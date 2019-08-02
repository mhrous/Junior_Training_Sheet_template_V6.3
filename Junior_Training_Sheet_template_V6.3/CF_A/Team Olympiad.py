n = int(input())
array = list(map(int,input().split()))

array_1 = []
array_2 = []
array_3 = []

for index in range(n):
    num = array[index]
    index += 1
    if num == 1:
        array_1.append(index)
    elif num == 2:
        array_2.append(index)
    else:
        array_3.append(index)

_min = min(len(array_1), len(array_2), len(array_3))

print(_min)

for i in range(_min):
    print("{} {} {}".format(array_1[i], array_2[i], array_3[i]))
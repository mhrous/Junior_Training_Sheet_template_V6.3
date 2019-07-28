n = int(input())
array =[]
count = 0

for i in range(n):
    new_array = list(map(int,input().split()))
    array.append(new_array)


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if array[i][0] == array[j][1]:
            count += 1

print(count)

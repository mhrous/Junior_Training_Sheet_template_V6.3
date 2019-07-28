n = int(input())
box = list(map(int,input().split()))
m = int(input())

for i in range(m):
    index, number = map(int,input().split())
    index -= 1
    if index != 0:
        box[index - 1] += (number - 1)
    if index != n-1:
        box[index + 1] += (box[index] - number)
    box[index] = 0

print("\n".join([str(x) for x in box]))
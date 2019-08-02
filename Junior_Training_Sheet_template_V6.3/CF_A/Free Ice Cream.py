n, x = map(int, input().split())
count = 0

for i in range(n):
    char, num = input().split()
    if char == "+":
        x += int(num)
    elif int(num) > x:
        count +=1
    else:
        x -= int(num)

print("{} {}".format(x, count))
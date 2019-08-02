n = int(input())

count = 0

for i in range(n):
    _str = input()
    if "+" in _str:
        count += 1
    else:
        count -= 1

print(count)
n = int(input())
last = ""
count = 0

for i in range(n):
    now = input()
    if now != last:
        last = now
        count += 1

print(count)
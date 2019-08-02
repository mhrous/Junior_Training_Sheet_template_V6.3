array = list(map(int,input().split()))
_str = input()

count = 0

for char in _str:
    if char == '1':
        count += array[0]

    elif char == '2':
        count += array[1]

    elif char == '3':
        count += array[2]

    else:
        count += array[3]

print(count)

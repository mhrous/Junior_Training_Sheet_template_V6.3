_str = input()

now = 'a'
count = 0

for char in _str:
    x = max(ord(char), ord(now)) - min(ord(char), ord(now))
    y = 26 - x
    count += min(x, y)
    now = char

print(count)
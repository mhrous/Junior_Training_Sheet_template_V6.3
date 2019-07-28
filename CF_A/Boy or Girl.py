name = input()
_dict = {}
count = 0

for char in name:
    if char not in _dict:
        count += 1
        _dict[char]=True

if count%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

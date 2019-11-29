n = input()
array = list(map(int,input().split()))
_min = min(array)
_max = max(array)
count = 0

for num in array:
    if(num != _min and num != _max):
        count += 1

print(count)

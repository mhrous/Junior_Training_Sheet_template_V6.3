n, k = map(int,input().split())

array = range(97,97+k)

_str=""

for i in range(n):
    _str += chr(array[i % k])

print(_str)
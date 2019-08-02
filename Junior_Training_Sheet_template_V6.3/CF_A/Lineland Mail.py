n = int(input())
array = list(map(int,input().split()))

for i in range(n):
    _min = abs(array[i-1] - array[i])
    if i+1 < n :
        _min = min(_min, abs(array[i+1] - array[i]))
    _max = max(abs(array[0] - array[i]), abs(array[-1] - array[i]))

    print("{} {}".format(_min, _max))

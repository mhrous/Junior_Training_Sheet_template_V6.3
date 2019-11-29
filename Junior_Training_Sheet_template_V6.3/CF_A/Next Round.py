n, k = map(int, input().split())
array = list(map(int, input().split()))

_min = array[k - 1]

last = array[::-1].index(_min)
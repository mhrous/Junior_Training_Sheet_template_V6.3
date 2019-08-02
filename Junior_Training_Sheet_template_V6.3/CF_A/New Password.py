n, k = map(int,input().split())

array = range(97,97+k)



for i in range(n):
    print(chr(array[i % k]),end = "")


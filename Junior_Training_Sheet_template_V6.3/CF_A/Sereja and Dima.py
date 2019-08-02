n = int(input())
array = list(map(int,input().split()))
a = 0
b = 0

frist = 0
last = n - 1
is_a = True

for i in range(n):
    if is_a:
        if array[frist] > array[last]:
            a += array[frist]
            frist += 1
        else:
            a += array[last]
            last -= 1
        

    else:
        if array[frist] > array[last]:
            b += array[frist]
            frist += 1
        else:
            b += array[last]
            last -= 1 

    is_a = not is_a


print("{} {}".format(a,b))

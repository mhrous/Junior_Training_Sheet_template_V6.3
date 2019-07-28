n = input()

array = list(map(int , input().split()))
array.sort()

for num in array:
    print(num,end=" ")
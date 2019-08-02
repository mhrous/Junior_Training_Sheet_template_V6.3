array = list(map(int,input().replace("+"," ").split()))
array.sort()

print("+".join([str(x) for x in array]))
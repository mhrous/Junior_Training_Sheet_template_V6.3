
result = 0
for i in range(5):
    array = list(map(int,input().split()))
    if(1 in array):
        row = i
        col = array.index(1)
        result = abs(2 - col) + abs(2 - row) 
    
print(result)


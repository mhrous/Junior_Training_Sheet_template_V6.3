_len = int(input())
stones = input()
last = stones[0]
count = 0

for index in range(1,_len):

    if stones[index] == last:
        count += 1
    
    last = stones[index]

print(count)
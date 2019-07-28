str_a = input()
str_b = input()

index = 0

for char in str_b:
    if char == str_a[index]:
        index += 1
    
print(index + 1)
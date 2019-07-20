n = input()
s = input()

result = 0

for c in s:
    if(c == 'A'):
        result += 1
    elif(c == 'D'):
        result -= 1

if(result == 0):
    print("Friendship")
elif(result > 0):
    print("Anton")
else:
    print("Danik")

    


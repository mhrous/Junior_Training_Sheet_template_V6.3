direction = input()
message = input()

Keyboard="qwertyuiopasdfghjkl;zxcvbnm,./"

for char in message:
    index = Keyboard.index(char) 
    if direction == "L":
        index += 1
    else:
        index -= 1
    
    print(Keyboard[index], end = "")
    
    
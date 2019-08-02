n = int(input())

x = 0
y = 0
z = 0

for i in range(n):
    _x, _y, _z = map(int, input().split())

    x += _x
    y += _y
    z += _z

if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")


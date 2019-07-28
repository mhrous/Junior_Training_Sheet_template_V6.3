n = int(input())

for i in range(n):
    _str = input()

    if len(_str) <= 10:
        print(_str)
    else :
        print("{}{}{}".format(_str[0],len(_str[1:-1]),_str[-1]))
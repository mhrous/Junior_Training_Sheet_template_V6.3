k,r = map(int,input().split())
spend = k

count = 1

while spend%10 != r and spend % 10 != 0:
    count += 1
    spend = count * k

print(count)
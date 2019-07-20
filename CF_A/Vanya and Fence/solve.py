n,m =map(int,input().split());
array=list(map(int,input().split()))
 
count=0
 
for num in array:
    if(num>m):
        count +=2
    else:
        count +=1
 
print(count)
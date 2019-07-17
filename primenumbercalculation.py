a=input()
c=len(a)
b=a.split()
headcount=0
for i in range(int(b[0]),int(b[1])+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        headcount=headcount+1
print(headcount)

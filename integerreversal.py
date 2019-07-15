a=str(input())
b=int(len(a))
c=[]
for i in range (b-1,-1,-1):
    c.append(a[i])
str1=""
print(str1.join(c))

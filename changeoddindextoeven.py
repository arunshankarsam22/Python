'''Given a number N followed by N numbers. Print the even numbers which are present in odd positions and odd numbers which are present in even positions(0 indexing).
Input Size : 1 <= N <= 100000
Sample Testcases :
INPUT
7
1 2 3 4 5 6 7
OUTPUT
1 2 3 4 5 6 7'''





m1=int(input())
m2=input()
n2=m2.split()
n3=[]
n4=[]
for i in n2:
    n3.append(int(i))
for i in range(0,len(n3)) :
    if(i%2==0):
        if(n3[i]%2!=0):
            n4.append(n3[i])
    else:
        if(n3[i]%2==0):
            n4.append(n3[i])
print(' '.join([str(n4[i]) for i in range (0,len(n4))]))

'''Given a number N followed by N numbers. Out of these N numbers some of them are repeated. Write a program to find the first number which is repeated. If no numbers are repeated print 'unique'.
Input Size : 1 <= N <= 100000
Sample Testcases :
INPUT
7
1 2 3 2 3 4 3
OUTPUT
2'''


m1=input()
m2=input()
n1=m1.split()
n2=m2.split()
m3=''.join(sorted(n2))
m4=len(m3)
i=0
for i in range (0,m4-1):
    if (m3[i]==m3[i+1]):
        print(m3[i])
        i=i+1
        break
if(i==0):
    print("unique")

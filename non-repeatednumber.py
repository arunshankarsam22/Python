'''Given a number N followed by N numbers. All the numbers in the given input appear twice except for one number(ie one number appears only once in the given input). Find the number which appears only once.
Input Size : 1 <= N <= 100000
Sample Testcases :
INPUT
5
1 2 1 3 2
OUTPUT
3'''




a=int(input())
b=input()
c=b.split()
for i in range (0,a):
    count=0
    for j in range(0,a):
        if(c[i]==c[j]):
            count=count+1
            if(count==2):
                break
    if (count==1):
        print(int(c[i]))

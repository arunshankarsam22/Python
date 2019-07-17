'''Given a number N followed by N numbers. Out of these N numbers some of them are repeated. Write a program to find the number which is repeated and print the repeated numbers in sorted order. If no numbers are repeated print "unique".
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
7
1 2 3 2 3 4 3
OUTPUT
2 3 '''



m1=input()
m2=input()
n1=m1.split()
n2=m2.split()
n3=[]
for i in range(0,int(n1[0])):
    for j in range(i+1,int(n1[0])):
        if(str(n2[i])==str(n2[j])):
            if(str(n2[i]) in n3):
                print (n3)
                break
            else:
                n3.extend((n2[i]))
if (len(n3)==0):
    print("unique")
else:
    print(' '.join(sorted(n3)))

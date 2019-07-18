'''Given a number n followed by n numbers. Find the numbers which are equal to their index value and print them in sorted order. If no such numbers are present print '-1' without quotes.
Input Size : 1 <= n <= 100000
Sample Testcases :
INPUT
6
6 7 3 3 4 5
OUTPUT
3 4 5'''



a=int(input())
b=input()
c=b.split()
d=[]
for i in range(0,a):
    if(str(i)==c[i]):
        d.append(c[i])
if(len(d)!=0):
    print(' '.join(sorted(d)))
else:
    print (-1)

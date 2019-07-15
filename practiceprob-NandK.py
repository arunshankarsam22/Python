''' Given 2 numbers N,K and an array of N integers, find the sum of the first 'K' integers.
Sample Testcase :
INPUT
5 2
1 2 3 4 5
OUTPUT
3'''

a=str(input())
b=str(input())
c=a.split()
d=b.split()
add=0
for i in range(0,int(c[1])):
	add=add + int(d[i])
print (add)

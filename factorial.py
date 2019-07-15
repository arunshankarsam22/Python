'''Given a number N, find its factorial.
Input Size  : N <= 20
Sample Testcase :
INPUT
5
OUTPUT
120'''

a=int(input())
factorial=1
for i in range (a,0,-1):
    factorial=factorial*i
print(factorial)

''' Given a string S, print its reverse.
Input Size : |s| <= 100000 (ie do it in O(n) or O(log n) time complexity)
Sample Testcase :
INPUT
aabbcc
OUTPUT
ccbbaa'''

a=str(input())
b=int(len(a))
c=[]
for i in range (b-1,-1,-1):
    c.append(a[i])
str1=""
print(str1.join(c))

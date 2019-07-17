'''Given a string s swap the even and odd characters.
Input Size : |s| <= 10000000(complexity O(n))
Sample Testcase :
INPUT
abcd
OUTPUT
badc'''



a=input()
b=len(a)
c="".join([a[i:i+2][::-1] for i in range(0,b,2)])
print (c)

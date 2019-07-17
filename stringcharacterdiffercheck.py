'''Given 2 strings check whether they differ by only one character.
Input Size : |s| <= 100000(complexity O(nlogn) or O(n))
Sample Testcase :
INPUT
aab aay
OUTPUT
yes '''


a=input()
b=a.split()
count=0
for i in range(0,len(b[0])):
    if b[0][i]!=b[1][i]:
        count=count+1
if (count==1):
    print("yes")
else:
    print("no")

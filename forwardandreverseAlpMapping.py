'''Each character of the alphabet is matched to a number. For example A is mapped to 1 , b to 2 so on z to 26. The reverse mapping is also true. 1 is mapped to a , 2 to b 3 to c and so on z to 26. So a number 12258 can be translated to abbeh , aveh , abyh , lbeh , and lyh , so there are 5 ways to translate 12258. Given a number N , write a program to print the number of ways to do this.
Input Size : 1 <= N <= 100000
Sample Testcases :
INPUT
12258
OUTPUT
5'''



a=str(input())
b=len(a)
i=0
count=1
for i in range(0,b):
    if(i<(b-1)):
        if((str(a[i]) + str(a[i+1]))<="26"):
            if(str(a[i])=="0"):
                continue
            else:
                count=count+1
for j in range(0,b):
    if(j<(b-3)):
        if((str(a[j+2]) + str(a[j+3]))<="26"):
            if(str(a[j+2])=="0"):
                continue
            else:
                count=count+1
print (count)   

'''Given 2 strings, check whether it is isomorphic.
Input Size : |s| <= 100000(complexity O(nlogn))
Sample Testcase :
INPUT
aab xxy
OUTPUT
yes'''   


maximum=256
a=input()
a1=a.split()
string1=a1[0]
string2=a1[1]
lengthstr1=len(a1[0])
lengthstr2=len(a1[1])
visitme= ["no"]*maximum
mapp = [0] * maximum
if lengthstr1!=lengthstr2:
	print("no")
for i in range(lengthstr1):
	if mapp[ord(string1[i])]==0:
	    if visitme[ord(string2[i])]=="yes":
	        print("no")
	    visitme[ord(string2[i])]="yes"
	    mapp[ord(string1[i])]=string2[i]
	elif(mapp[ord(string1[i])]!=string2[i]):
	        print("no")
	else:
            print("yes")


1	maximum=256
2	a=input()
3	a1=a.split()
4	string1=a1[0]
5	string2=a1[1]
6	lengthstr1=len(a1[0])
7	lengthstr2=len(a1[1])
8	visitme= ["no"]*maximum
9	mapp = [0] * maximum
10	if lengthstr1!=lengthstr2:
11	    print("no")
12	for i in range(lengthstr1):
13	    if mapp[ord(string1[i])]==0:
14	        if visitme[ord(string2[i])]=="yes":
15	            print("no")
16	        visitme[ord(string2[i])]="yes"
17	        mapp[ord(string1[i])]=string2[i]
18	    elif(mapp[ord(string1[i])]!=string2[i]):
19	        print("no")
20	    else:           
21	        print("yes")

'''Given a roman number N, convert it to integer.
Input Size : N <= 20
Sample Testcase :
INPUT
VI
OUTPUT
6'''



ROM={"I":"1","V":"5","X":"10"}
str=input() 
val = 0
i = 0
while (i < len(str)):
    s1 = int(ROM[str[i]])
    if (i+1 < len(str)): 
       s2 = int(ROM[str[i+1]])
       if (s1 >= s2): 
            val = val + s1 
            i = i + 1
       else: 
            val = val + s2 - s1 
            i = i + 2
    else: 
        val = val + s1 
        i = i + 1
print (val)

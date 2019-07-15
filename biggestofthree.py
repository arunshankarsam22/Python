a = str(input())
b=a.split()
if (int(b[0]) >= int(b[1])) and (int(b[0]) >= int(b[2])):
   largest = b[0]
elif (int(b[1]) >= int(b[0])) and (int(b[1]) >= int(b[2])):
   largest = b[1]
else:
   largest = b[2]
print(largest)

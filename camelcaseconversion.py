a=input()
a.split()
k=' '.join([str(i[0].upper()) + str(i[1:]) for i in a.split()])
print (k)

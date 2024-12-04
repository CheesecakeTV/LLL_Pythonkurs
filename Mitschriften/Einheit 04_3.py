
x = [1,7,2,3,6,2,3,5,1]

#for i in x: # i wäre quasi x[i]
#    print(i)

#for i in range(5,10,2):
#    print(i)

#x = list(range(1000))
#print(x)

n = 0
for i in x:
    #print(n,i)
    n += 1

for n,i in enumerate(x):
    ...
    #print(n,i)

x = [1,7,2,3,6,2,3,5,1]
y = [2,5,3,7,3,3,6,3,4]

#for n,i in enumerate(x):
#    print(i,y[n])

for X,Y in zip(x,y):
    print(X,Y)

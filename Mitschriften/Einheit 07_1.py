

def halloWelt(parameter,weitererParameter="Hallo Welt",hallo=None):
    print("Hallo Welt")
    print(parameter)
    print(weitererParameter)
    print(hallo)
    print()

#halloWelt("Hallo Discord","Hallo John")
#halloWelt("Hallo Discord",hallo="Hallo")

def printCopy(hallo,*parameter,sep,**benannt):
    print(hallo)
    print(parameter)
    print(benannt)

#printCopy("Hallo Welt",15,100,None,sep=None,discord="Welt")

dasDict = {"sep":" - ","end":"Hallo\n"}

x = [1,2,3,4,5]
print(*x, **dasDict)

y = [*x,6,7,8,9]
print(y)






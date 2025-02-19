
x = [1,-6,3,6,-8,8,2,-3,5,7,2]

def dieFkt(element:float) -> float:
    return abs(element)

print(list(map(dieFkt,x)))

x.sort(key=dieFkt)
#x.sort(key=lambda a:abs(a))
#x.sort(key=abs)
print(x)






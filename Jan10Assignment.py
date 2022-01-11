import math

def interest(p, r, l):
    r = (r/100)/12
    return math.ceil(p/((((1+r)**l)-1)/(r*(1+r)**l)))

print(interest(800000,6,103))
print(interest(30000,6,5*12))
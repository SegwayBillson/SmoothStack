import math

import math

print(50+50)

print(100-10)

#Throws an error
#print(30+*6)

print(6^6)

print(6**6)

print(6+6+6+6+6+6)

print("Hello World")

print("Hello World : 10")

def interest(p, r, l):
    r = (r/100)/12
    return math.ceil(p/((((1+r)**l)-1)/(r*(1+r)**l)))

print(interest(800000,6,103))
print(interest(30000,6,5*12))

def interest(p, r, l):
    r = (r/100)/12
    return math.ceil(p/((((1+r)**l)-1)/(r*(1+r)**l)))

print(interest(800000,6,103))
print(interest(30000,6,5*12))

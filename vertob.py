from math import sqrt,cos

def vertor_perpendicular(a,b):
    r = (a**2 + b**2) + (2 * a * b)
    result = sqrt(r)
    print(result)

vertor_perpendicular(float(input(':')),float(input(':')))
print(cos(45))

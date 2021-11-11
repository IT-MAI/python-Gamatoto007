a=int(input("Введите первый коэффициент "))
b=int(input("Введите второй коэффициент "))
c=int(input("Введите третий коэффициент "))
from math import sqrt
def sum (a,b,c):
    return ((b**2)-(4*a*c))
D = sum (a,b,c)
def biba (a,b,D):
    return ((-b+sqrt(D))/(2*a))
Biba=biba(a,b,D)
def boba (a,b,D):
    return ((-b-sqrt(D))/(2*a))
Boba=boba(a,b,D)
print(Biba,Boba)
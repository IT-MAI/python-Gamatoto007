a=int (input ("Ыведите значение a: "))
b=int (input ("Введите значение для b: "))
c=0
if a<b:
    a,b=b,a
while a%b!=0:
    c=a%b
    a,b=b,c
print ("Наибольший общий делитель: " + str (b))
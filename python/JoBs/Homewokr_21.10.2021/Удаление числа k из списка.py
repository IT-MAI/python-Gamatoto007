from random import shuffle
a=[]
n=int(input("Введите число: "))
while n!=0:
    a.append(n)
    n = int(input("Введите число: " ))
k=int(input("Введите число, которое нужно удалить: "))
while k in a: a.remove(k)
print(a)
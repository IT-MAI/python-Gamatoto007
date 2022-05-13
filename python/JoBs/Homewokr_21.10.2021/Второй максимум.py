Max=int(input("Введите число: "))
max=int(input("Введите число: "))
el=int(input("Введите число: "))
while el!=0:
    if el>Max:
        max, Max=Max, el
    elif el>max:
        max=el
    el=int(input("Введите число: "))
print(max)
max=0
n_of_max=0
el=1
while el!=0:
    el=int(input("Введите число: "))
    if el>max:
        max, n_of_max=el, 1
    elif el == max:
        n_of_max += 1
print(n_of_max)
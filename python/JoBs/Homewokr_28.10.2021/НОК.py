a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
n=1
while True:
    if n%a==0 and n%b==0:
        print("Наименьшее общее кратное abc это: " + str(n))
        break
    else:
        n+=1
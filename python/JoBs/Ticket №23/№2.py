n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))
a=2
while True:
    if a%n==0 and a%m==0:
        print("Наименьшее общее кратное n и m это: " + str(a))
        break
    else:
        a+=1

n=int(input("Введите число: "))
sum = 0
while n!=0:
    sum=sum+n%10
    n=n//10
print("Сумма цифр числа равна: ", sum)
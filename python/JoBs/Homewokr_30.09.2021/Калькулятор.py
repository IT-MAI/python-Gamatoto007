a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
c=input("Введите действие: ")
if c in ('+', '-', '*', '/'):
    if c=="/":
        print(a / b)
    elif c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
n=int(input("Введите число: "))
for i in range(2,n+1):
    if  n%i==0:
        print("diff")
    else:
        print("simple")
    break
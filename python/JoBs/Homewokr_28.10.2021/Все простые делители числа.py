n=int(input("Введите число: "))
for i in range(1,n+1):
    s=0
    if (n%i==0):
        for j in range(2, i-1):
            if (i % j == 0):
                s=s+1
        if (s==0):
            print(i, end=" ")
All=[int(i) for i in input("Введите рост мальчиков в классе: ").split()]
Petya=int(input("Введите рост Пети: "))
N=0
while N < len(All) and All[N] >= Petya:
    N=N+1
print(N+1)
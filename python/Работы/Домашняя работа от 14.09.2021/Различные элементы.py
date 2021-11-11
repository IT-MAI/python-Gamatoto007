a=[int(i) for i in input("Введите числовую последовательность: ").split()]
dif=1
for i in range(0, len(a)-1):
    if a[i] != a[i+1]:
        dif=dif+1
print(dif)
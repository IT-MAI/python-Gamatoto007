q=0
a=[int(i) for i in input("Введите числовую последовательность: ").split()]
for i in range(1, len(a)):
    if a[i] > a[q]:
        q = i
print("Наибольшее число: " + str(a[q]), "Его индекс: " + str(q))
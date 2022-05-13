Ok = [int(i) for i in input("Введите числовую последовательность: ").split()]
q=0
for i in range(1, len(Ok)):
    if Ok[i] > Ok[i - 1]:
        q=q+1
print(q)

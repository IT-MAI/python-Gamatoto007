Ok = [int(i) for i in input("Введите числовую последовательность: ").split()]
for i in range(1, len(Ok)):
    if Ok[i - 1] * Ok[i] > 0:
        print(Ok[i - 1], Ok[i])
        break
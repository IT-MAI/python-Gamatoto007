q=input("Введите числовую последовательность: ")
a=[int(q) for q in q.split()]
for i in a:
    if int(i) % 2 == 0:
        print(i)
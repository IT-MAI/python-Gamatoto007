a=[int(i) for i in input("Введите числовую последовательность: ").split()]
b=[int(i) for i in input("Введите числовую последовательность: ").split()]
print(a)
print(b)
c=[]
for i in a:
    c.append([])
for j in b:
    c[-1].append([j*i])
print(c[2])
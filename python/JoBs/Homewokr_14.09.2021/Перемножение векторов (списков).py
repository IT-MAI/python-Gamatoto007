a=[int(i) for i in input("Введите числовую последовательность: ").split()]
b=[int(i) for i in input("Введите числовую последовательность: ").split()]
print(a)
print(b)
c=[]
for i in a:
    c[-1].append([i])
for j in b:
    c[-1].append([j*i])
for i in c:
print(c)
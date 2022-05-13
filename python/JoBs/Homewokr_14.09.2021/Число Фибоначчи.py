N = int(input("Введите число: "))
if N == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, N + 1):
        a, b = b, a + b
    print(b)
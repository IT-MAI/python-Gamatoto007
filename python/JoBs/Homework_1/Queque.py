class Queque:
#Создаём список и задаём максимальную длину очереди
    def __init__(self, L):
        self.aboba=[]
        self.L=L
#Функцию, измеряющуя длину очереди
    def length(self):
        return len(self.aboba)
#Функция, добовляющая новый элемент и удаляющая первый элемент, если элементов станет больше, чем L
    def add(self, a):
        self.aboba.append(a)
        if len(self.aboba)>self.L:
            self.aboba.pop(0)
#Функция, убирающая первый элемент
    def gl(self):
        self.aboba.pop(0)
#Функция, убирающая нужный элемент
    def bye(self, k):
        self.aboba.pop(k)
#Функция, очищающая очередь с помощью задания пустого списка
    def clean(self):
        self.aboba=[]
#Функция, выводящая значение первого элемента
    def look(self):
        print("Первый элемент в списке:", self.aboba[0])
#Функция, которая позволяет выводить осмысленный результат с помощью метода print
    def __repr__(self):
        return repr(self.aboba)
stac = Queque(3)
stac.add(7)
stac.add(2)
stac.add(8)
stac.add(5)
stac.gl()
stac.add(9)
print("Ваш список:", stac)
print("Длина списка:", stac.length())
stac.look()
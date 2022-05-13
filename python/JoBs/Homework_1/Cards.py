import random
class Cards:
# Создаём конструктор и задаём два списка
    def __init__(self, aboba):
# Список для хранения карт
        self.aboba=sorted(aboba, key=lambda A: random.random())
#Список сброса
        self.out=[]
#Функция, убирающая карту из основной стопки и добовляющую в стопку сброса
    def draw(self):
        N=len(self.aboba) - 1
        print("\nВаша карта -", self.aboba[N], "\n" )
        self.out.append(self.aboba[N])
        self.aboba.pop(N)
#Функция, перемешивающая содержимое оставшейся колоды
    def shuffle(self):
        self.aboba=sorted(self.aboba, key=lambda A: random.random())
#Функция, соединяющая и перемешивающая сброс и основную колоду
    def reshuffle(self):
        self.aboba=self.aboba + self.out
        self.aboba=sorted(self.aboba, key=lambda A: random.random())
#Функция, выводящая остальные карты в основной колоде
    def print(self):
        for i in range(len(self.aboba)-1,-1,-1):
            print(self.aboba[i])
aboba = ["Пики 6", "Пики 7", "Пики 8", "Пики 9", "Пики 10", "Пики Валет", "Пики Дама", "Пики Король", "Пики Туз",
"Черви 6", "Черви 7", "Черви 8", "Черви 9", "Черви 10", "Черви Валет", "Черви Дама", "Черви Король", "Черви Туз",
"Крести 6", "Крести 7", "Крести 8", "Крести 9", "Крести 10", "Крести Валет", "Крести Дама", "Крести Король", "Крести Туз",
"Бубны 6", "Бубны 7", "Бубны 8", "Бубны 9", "Бубны 10", "Бубны Валет", "Бубны Дама", "Бубны Король", "Бубны Туз"]
Game=Cards(aboba)
Game.draw()
Game.print()
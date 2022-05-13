class Student():
    def __init__(self, name, Fname, age, gender, ticket):
        self.name=name
        self.Fname=Fname
        self.age=age
        self.gender= gender
        self.ind=ticket
Student1 = Student("Аня", "Иванова", 23, "женский", 8800 - 35)
Student2 = Student("Вито", "Скалетта", 19, "мужской", 8710 - 29)
Student3 = Student("Надя", "Карпова", 22, "женский", 3815 - 45)
Student4 = Student("Алексаднр", "Романов", 20, "мужской", 4255 - 30)
Student5 = Student("Раян", "Гостлинг", 18, "мужской", 1246 - 86)
students= [Student1, Student2, Student3, Student4, Student5]
#Выводим данные с помощью цикла
def info_students(students):
    for l in range(len(students)):
        print(students[l].name, students[l].Fname, students[l].age, students[l].gender, students[l].ind)
#Сортируем пузырьком элементы списка по возрасту
for i in range(len(students)-1):
    for j in range(len(students)-i-1):
        if students[j].age>students[j+1].age:
             students[j], students[j+1] = students[j+1], students[j]
info_students(students)
def binarity(b, N):
#Создаем вспомогательный список
    list=[]
    for i in range(len(b)):
        list.append(b[i].age)
    left=0
    right=len(list)-1
    while left<=right:
        middle=(left+right)//2
        if N>list[middle]:
            left=middle+1
        else:
            right=middle-1
    if list[left]==N:
        return left
    return -1
N=int(input("Введите возраст: "))
result=binarity(students, N)
if result==-1:
    print('Такого возраста нет')
else:
    print(students[result].name, students[result].Fname)
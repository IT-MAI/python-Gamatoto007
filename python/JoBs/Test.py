
    for k in range(len(b)):
        a.append(b[k].age)
    #Далее идет сам бинарный поиск
    left=0
    right=len(a)-1
    while left<=right:
        middle= (left+right)//2
        if x>a[middle]:
            left=middle+1
        else:
            right=middle-1
    if a[left]==x:
        return left
    return -1

x=int(input())
result= bin(students, x)
if result==-1:
    print('Такого возраста нет')
else:
    print(students[result].name, students[result].lname)
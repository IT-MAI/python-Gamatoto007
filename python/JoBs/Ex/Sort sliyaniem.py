from random import randint
from datetime import datetime
start = datetime.now()
def split(list):
    N=len(list)//2
    list1=list[:N]
    list2=list[N:]
    if len(list1) > 1:
        list1 = split(list1)
    if len(list2) > 1:
        list2 = split(list2)
    return merge_list(list1, list2)
def merge_list(list1, list2):
    spisok = []
    one = len(list1)
    two = len(list2)
    i = 0
    j = 0
    while i < one and j < two:
        if list1[i] <= list2[j]:
            spisok.append(list1[i])
            i += 1
        else:
            spisok.append(list2[j])
            j += 1
    spisok += list1[i:] + list2[j:]
    return spisok
list = [randint(0, 100) for i in range(1000)]
print(split(list))
print(datetime.now() - start)
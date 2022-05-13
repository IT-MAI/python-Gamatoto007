from random import randint
from datetime import datetime
start=datetime.now()
def insert_sort(numbers):
    for i in range(1, len(numbers)):
        number = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > number:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = number
list=[randint(0, 100) for i in range(1000)]
insert_sort(list)
print(list)
print(datetime.now()-start)
#O(n^2)
from random import randint
from datetime import datetime
start=datetime.now()
def choose_sort(numbers):
    for i in range(len(numbers)):
        min = i
        for j in range(i+1, len(numbers)):
            if numbers[j]<numbers[min]:
                min=j
        numbers[i], numbers[min] = numbers[min], numbers[i]
list=[randint(0, 100) for i in range(1000)]
choose_sort(list)
print(list)
print(datetime.now()-start)
#O(n^2)
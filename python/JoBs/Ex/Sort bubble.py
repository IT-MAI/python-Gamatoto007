from random import randint
from datetime import datetime
start=datetime.now()
list=[randint(0, 100) for i in range(1000)]
N=len(list)
for i in range(0, N-1):
    for j in range(0, N-1-i):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)
print(datetime.now()-start)
#O(n^2)
from random import randint
from datetime import datetime
def b_search(array, number):
    min=0
    max=len(array)
    while min<=max:
        center=(min+max)//2
        if array[center]==number:
            return center
        elif array[center]>number:
            max=center-1
        elif array[center]<number:
            min=center+1
    return -1
start=datetime.now()
N=[randint(0, 10) for i in range(1000)]
N=sorted(N)
print(b_search(N, 4))
print(datetime.now()-start)
#O(logN)
from random import randint
from datetime import datetime
def l_search(list, element):
    for i in range (len(list)):
        if list[i] == element:
            return i
    return -1
start=datetime.now()
N=[randint(0, 100) for i in range(50)]
N=sorted(N)
print(N)
print(l_search(N, 4))
print(datetime.now()-start)
#O(n)
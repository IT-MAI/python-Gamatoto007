import random
from random import randint
from datetime import datetime
start = datetime.now()
def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        N = random.choice(numbers)
        a_nums = []
        b_nums = []
        c_nums = []
        for i in numbers:
            if i < N:
                a_nums.append(i)
            elif i > N:
                b_nums.append(i)
            else:
                c_nums.append(i)
        return quicksort(a_nums) + c_nums + quicksort(b_nums)
list = [randint(0, 100) for i in range(1000)]
quicksort(list)
print(quicksort(list))
print(datetime.now() - start)
# Nlog2N
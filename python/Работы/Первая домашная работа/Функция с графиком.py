def aboba (x):
    return (x**3)
S = aboba (x)
array=[aboba(x) for x in range (-1001,1001)]
import matplotlib.pyplot as plt
plt.plot(array)
def aboba (x):
    return (x**3)
S = aboba (x)
array=[aboba(x) for x in range (-1000,1000)]
import matplotlib.pyplot as plt
plt.plot(array)
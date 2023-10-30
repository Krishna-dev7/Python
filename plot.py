import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
style.use('dark_background')

x = np.random.random(50) * 50
y = np.random.random(50) * 50
z = np.random.random(50) * 50

plt.pie(x)
plt.plot(x,y)
plt.title('Salary comparison')

plt.show()
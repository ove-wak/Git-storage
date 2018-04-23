import numpy as np
import matplotlib.pyplot as plt

N = 3
Original = (7.8, 7.4, 6.9)

ind = np.arange(N)  # the x locations for the groups
width = 0.4       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, Original, width, color='#FFE153')

Predicted = (3.2, 2.8, 4)
rects2 = ax.bar(ind + width, Predicted, width, color='#FF9224')

ax.set_ylabel("Loction error[m]",fontsize=16)
ax.set_xticks(ind + width/2)
ax.set_xticklabels(('9 AM', '2 PM', '7 PM'))
ax.set_xlabel("Time",fontsize=16)
ax.legend((rects1[0], rects2[0]), ('Original', 'Predicted'))

plt.show()
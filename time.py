import numpy as np
import matplotlib.pyplot as plt
freq = []
time = np.arange(0, 60, 2)
for i in range(0,len(time), 1):
  freq.append(np.sin(i) * 5)
line = plt.plot(time, freq)
plt.axis([0, 60, -7, 7])
plt.setp(line, linewidth=2, color='black') 
plt.title('Time Domain Plot')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.gcf().canvas.set_window_title('Time Domain Plot')
plt.show()
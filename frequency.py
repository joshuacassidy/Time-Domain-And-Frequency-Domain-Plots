import numpy as np
import matplotlib.pyplot as plt

amp = [5]
freq = [4]

line = plt.plot(freq, amp, 'ro')
plt.axis([0, 5, 0, 10])
plt.setp(line, linewidth=7, color='r') 
plt.title('Frequency Domain Plot')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.gcf().canvas.set_window_title('Frequency Domain Plot')

plt.show()
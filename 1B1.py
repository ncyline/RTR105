'''
from numpy import *
x = linspace(0,7,70)
y = cos(x)


import matplotlib.pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija$cos(x)$')
plt.plot(x, y)
plt.show()
'''

'''
from numpy import *
x = linspace(0,7,70)
y = cos(x)


import matplotlib.pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija$cos(x)$')
plt.plot(x, y, color = "#DF013A")
plt.show()
'''
'''
from numpy import *
x = linspace(0,7,70)
y2 = sin(x)


import matplotlib.pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija$cos(x)$')
plt.plot(x, y2, color = "#04B45F")
plt.show()
'''
'''
#
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
x = linspace(0, 4, 70)
y2 = sin(x)

import matplotlib.pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$')
plt.plot(x, y2, color='#FF0000')

y1=x
plt.plot(x, y1, color='#04B45F')

y2=x - x*x*x/(1*2*3)
plt.plot(x, y1, color='#610B4B')
plt.show()
'''



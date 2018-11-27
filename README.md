# RTR105
Datormācības kursa elektroniskā karte


firefox& - nets

f - burts _ 2x tab

echo &0 - dialekts

ls - parāda mapes

uname - linux

history - paraada vēsturi

who - kas ir pieslēdzies

whoami - kas es esmu

man help

man ffplay

sh - cita valoda

pwd - kur atrodās dators

man pwd - kur atrodās mans dators

ls - mapes satura aplūkošanai

ls -l info

ls -a info par failiem

ls -la info

ctr + l - ekrāna notīrīšana
cd /home/user - parvietoties

pwd - atrašanās vieta

mkdir ManaMape - izveidot mapi

rmdir ManaMape/ - izdzēst mapi

rm ManaMape/ - dzēst (remove)

echo "Teksts"

echo -e "Teksts\n jes\n lol"

echo "Teksts" > fails1.txt - teksts failā

echo "Teksts" > ../fails1.txt - teksta rediģēšana failā

cat fails1.txt - faila apskate

echo "Cits Teksts" > fails1.txt - Teksta satura maiņa

man chmod - info par chmod

chmod 700 fails1.txt

nano fails1.txt izveidot kopiju

cp fails1.txt fails3.txt - kopēt failu

mv *.txt Music/ - pārvietot

echo $PATH - 

   26  create_in.sh 
   
   29  PATH=$PATH:~/Mape
   
   31  /home/user/create_in.sh
   
   32  ./create_in.sh
   
   33  nano create_in.sh
   
   37  git clone https://github.com/ncyline/RTR105
   
   39  ~/rtr105$  ls -l
   
   40  ~/RTR105$ pwd
   
   41  cd /home/use/RTR105/
   
   44  cd /home/user/RTR105/
   
   46  nano README.md 
   
   47  nano git-upload
 
   51  ~/RTR105$ history > history_20180918.txt
   
   54  chmod 764 git-upload
   
   73  history > history_20180918.txt
   
   74  ./git-upload 20180918_15_30
import sys

sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

def f(x):

    return sin(x)

from numpy import sin, linspace

x = linspace(0, 7, 71)

y = f(x)

delta_x = x[1] - x[0]

from matplotlib import pyplot as plt

plt.grid()

plt.xlabel('x')

plt.ylabel('f(x)')

plt.title('Funkcija $sin(x)$')

plt.plot(x, y, color = "#FF0000")

#plt.legend(['$sin(x)$'])

#plt.show()


y_first_derivative = (f(x+delta_x) - f(x))/delta_x

plt.plot(x, y_first_derivative, color = "#00FF00")

#plt.legend(['$sin(x)$','$sin\'(x)$'])

#plt.show()


N = len(x)

y_first_derivative_build_from_array = []

for i in range(N-1):

    temp = ( y[i+1] - y[i] ) / (delta_x)
    
    #temp = ( y[i+1] - y[i] ) / (x[i+1] - x[1])
    
    y_first_derivative_build_from_array.append(temp)
    
    #print(i, x[i],x[i+1], y[i], y[i+1],temp, y_first_derivative_build_from_array)

plt.plot(x[0:N-1], y_first_derivative_build_from_array, color = "#0000FF")

plt.legend(['$sin(x)$','$sin\'(x)$', '$sin\'(x) - build_from array$'])

plt.show()


# coding utf -8
#1. N vienmērīgi sadalīti skaitļi
#N uniformly distributed random numbers

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import random
#pseido gadījumu skaitļu ģenerātora grauds
# random.seed(1)

N = 10000

x = random.uniform(0,5,N)
'''
k = [0,0,0,0,0]
for i in range(N):
    if x[i] < 1:
        k[0] = k[0] + 1
    elif x[i] < 2:
        k[1] = k[1] + 1
    elif x[i] < 3:
        k[2] = k[2] + 1
    elif x[i] < 4:
        k[3] = k[3] + 1
    else:
        k[4] = k[4] + 1
print(k)
print(sum(k))
'''

y = random.uniform(0,5,N)
N1 = 0
from matplotlib import pyplot as plt
plt.grid()
for i in range(N):
    #plt.plot(x[i],y[i],'ko')
    if x[i] > 0 and x[i] < 5:
        if y[i] > 0 and y[i] < x[i]:
            plt.plot(x[i],y[i], 'go')
            N1 = N1 + 1
        else:
            plt.plot(x[i],y[i], 'ro')
plt.show()

S_zinaamais = 5 * 5
S_nezinaamais = 1. * S_zinaamais * N1/N
print(S_nezinaamais)

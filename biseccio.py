import numpy as np
import matplotlib.pyplot as plt

#METÓDO DE LA BISECCIÓN

def f(x):
    return x - np.exp(-x)
#crear una lista de valores de f
x=np.linspace(0,1,100)

plt.plot(x,f(x))
plt.hlines(0.0,0,5, color="red")
#plt.show()

#metodo de la bisección

a = 0
b = 1

for i in range(10):
    c=0.5*(a+b)

    condicion = f(a) * f(c)

    if condicion < 0:
        b=c
    
    else:
        a=c

#asumimos que el ultimo valor de c es solucion de fc)=0

plt.plot(c,f(c),"o")
plt.show()

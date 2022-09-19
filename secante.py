import numpy as np
import matplotlib.pyplot as plt

#METÓDO DE secante

def f(x):
    return x - np.exp(-x)


def df(x):
      return 1 + np.exp(-x)


#crear una lista de valores de f
x=np.linspace(0,1,100)

plt.plot(x,f(x))
plt.hlines(0.0,0,5, color="red")
#plt.show()

#metodo de secante

x0 = 10 #semilla
x1=1

tolerancia=1e-5
error= 1.0

while not  np.abs(error)>tolerancia:
    error = f(x0)*(x1-x0)/f(x1)-f(xo)
    x0, x1 =x1, x0 - error
    
    print(x1)

plt.plot(x1,f(np.array(x1)), "o")
plt.show()

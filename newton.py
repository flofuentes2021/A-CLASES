import numpy as np
import matplotlib.pyplot as plt

#METÓDO DE NEWTON

def f(x):
    return x - np.exp(-x)


def df(x):
      return 1 + np.exp(-x)


#crear una lista de valores de f
x=np.linspace(0,1,100)

plt.plot(x,f(x))
plt.hlines(0.0,0,5, color="red")
#plt.show()

#metodo de Newton

x0 = 1.0 #semilla

tolerancia=1e-5
error= 1.0

while np.abs(error)>tolerancia:
    error = f(x0)/df(x0)
    x0 = x0 - error
    
    print(x0)

plt.plot(x0,f(x0), "o")
plt.show()

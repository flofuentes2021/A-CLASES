#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
import matplotlib.pyplot as plt


# In[36]:


ts= np.genfromtxt("Descargas/tiempos-sin-ver.txt")
tv=np.genfromtxt("Descargas/tiempos-viendo.txt")


# In[48]:


plt.errorbar(range(1,len(ts)+1),ts, yerr=0.005,fmt=".", linestyle="" , label="sin ver", color="pink")
plt.errorbar(range(1,len(tv)+1),tv, yerr=0.005,fmt=".", linestyle="", label="viendo", color= "purple")
plt.grid(True)
plt.xlabel("$\# Medición$")
plt.ylabel("$tiempo (s)$")
plt.hlines(np.mean(ts),0,52, label="sin ver", color="pink")
plt.hlines(np.mean(tv),0,52, label="viendo", color= "purple")
plt.legend(loc=4)
plt.ylim(0,2.5)
plt.title("Tiempo en caer una bolita en un plano inclinado vs número de medición")
plt.savefig("grafiquito.png")


# In[63]:


np.histogram(tv,bins=b)[0] #Veces que se repite cada dato


# In[64]:


np.histogram(tv, bins=b)[1]


# In[65]:


np.max(tv)


# In[67]:


b=np.arange(0.5,2.1,0.1)
b


# In[72]:


plt.hist(ts ,bins=b, alpha=0.5 ,color= "pink")
plt.hist(tv ,bins=b, alpha=0.5, color= "purple")
plt.grid(True)


# In[ ]:





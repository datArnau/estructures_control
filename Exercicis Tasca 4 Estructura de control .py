#!/usr/bin/env python
# coding: utf-8

# # Estructura de control

# ## Exercici 1

# In[25]:


print("escriu una nota entre 0 i 10")
inp = int(input())
if inp >= 0 and inp < 5:
    print ("Suspès")
elif inp >= 5 and inp < 7:
    print ("Aprovat")
elif inp >= 7 and inp < 9:
    print ("Notable")
elif inp >= 9 and inp <= 10:
    print ("Excel·lent")
else:
    print ("valor erroni")
    
    


# ## Exercici 2

# In[30]:


print("escriu el primer valor")
primer = int(input())
print("el primer valor es el " + str(primer))
print("escriu el segon valor")
segon = int(input())
print("el segon valor es el " + str(segon))

if primer > segon:
    print ("el primer és més gran")
elif primer < segon:
    print ("el segon és més gran")
else:
    print ("els dos son iguals")
    


# ## Exercici 3

# In[32]:


print("escriu el teu nom")
nom = str(input())
nom = nom + " "
print("quants cops el repetim?")
primer = int(input())
if primer <= 0:
    print ("no pot ser menor que zero")
else:
    print(primer*nom)


# ## Exercici 4

# In[37]:


import numpy


# In[54]:


print("escriu una llista")
llista = list(input())
llista_inv = llista[::-1]
if llista == llista_inv:
    print("la llista és simètrica")
    print("la llista conté " + str(len(llista)) + " elements")


# ## Exercici 5

# In[89]:


print("escriu una llista")
llista = list(input())
refer = list(range(len(llista)))
n=0
while n < len(llista):
    llista[n] = int(llista[n])
    n += 1

print(llista)
print(refer)

print ( "els valors que coincideixen amb la seva posició son "+ str([i for i, j in zip(llista, refer) if i == j]))


# In[ ]:





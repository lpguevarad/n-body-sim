#Este codigo calcula las posiciones para dos objetos que interactuan gravitacionalmente teniendo en cuenta la solución a las ecuaciones de newton en el sistema de laboratorio.
import numpy as np
import sys
import matplotlib.pyplot as plt

#CONSTANTES DEL PROBLEMA
m1=1e7 #masa cuerpo M )kg)
m2=0.00001*m1 #masa cuerpo m (kg)
mu=m1*m2/(m1+m2) # masa reducida kg
G=6.67430e-11 # constante gravitacional N*m^2/kg^2
k=G*m1*m2 
#CONDICIONES INICIALES

v0=float(sys.argv[1])
r1_0=np.array([0.0,0.0,0.0]) #posicion primer objeto m
v1_0=np.array([0.0,0.0,0.0]) #velocidad primer objeto m/s
r2_0=np.array([2.0,0.0,0.0]) #posicion segundo objeto m
v2_0=np.array([0.0,v0,0.0]) #velocidad segundo objeto m/s

r12=r2_0-r1_0 # distancia entre objetos
v12=v2_0-v1_0 # velocidad relativa entre objetos

#CONSTANTES DE MOVIMIENtO


#print(E)
L=mu*np.linalg.norm(np.cross(r12,v12)) #momento angular Js
#L=m1*np.linalg.norm(np.cross(r1_0,v1_0))+m2*np.linalg.norm(np.cross(r2_0,v2_0)) #momento angular Js
E=0.5*m1*np.linalg.norm(v1_0)**2 + 0.5*m2*np.linalg.norm(v2_0)**2 - k/(np.linalg.norm(r12)) #energia J
e=np.sqrt(1.0+((2*E*L**2)/(mu*k))) # excentricidad 
a=(L**2)/(mu*k*(1.0-e**2)) #longitud semieje mayor


#######MAIN CODE########

theta=np.linspace(0.0,2.0*np.pi,100)
r=(a*(1.0-e**2))/(1.0+e*np.cos(theta))-(a*(1.0-e**2))/(1.0+e)+np.linalg.norm(r12)

x1=(mu/m1)*r*np.cos(theta)
y1=(mu/m1)*r*np.sin(theta)

x2=(mu/m2)*r*np.cos(theta)
y2=(mu/m2)*r*np.sin(theta)

P1=np.column_stack((x1,y1)) # DATOS POSICION MASA M
P2=np.column_stack((x2,y2))  # DATOS POSICION MASA m
np.savetxt('posicion_M.dat',P1)
np.savetxt('posicion_m.dat',P2)

plt.plot(x1,y1,'o',color='royalblue',label=r'$posicion$ $masa$ $M$')
plt.plot(x2,y2,'salmon',label=r'$posicion$ $masa$ $m$')
plt.xlim([-5.0,5.0])
plt.ylim([-5.0,5.0])
plt.xlabel(r'$x (m)$',fontsize=15)
plt.ylabel(r'$y (m)$',fontsize=15)
plt.legend(loc='best')
plt.title(r'$Problema$ $de$ $N=2$ $cuerpos$ $M\gg m$')
plt.savefig('orbita.pdf')

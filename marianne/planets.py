""" 
Simulering av jordas bane rundt sola ved bruk av Eulers metode og Newtonsk gravitasjon. 
"""

import numpy as np 
import matplotlib.pyplot as plt 


N = 4000

#Definere tidsarray
t0 = 0
t1 = 365.25636 * 24 * 60 * 60  # Ett aar i sekunder

t = np.zeros(N) ; t[0] = t0
dt = (t1 -t0)/N

G = 6.67430e-11 

AU = 1.493e11
m_sola = 1.989e30 # kg
m_jorda = 5.972e24 # kg


# Startverdier for jorda
# 2020-Feb-28 kl. 00:00
#X =-1.385683325048748E+08 Y = 5.518939763457818E+07 Z = 3.711333408605307E+03
#VX=-1.137260147670654E+01 VY=-2.785900354076842E+01 VZ= 1.330149860683250E-03

# Initielle verdier for posisjon og hastighet
vx0 = -1.137260147670654E+01 * 1000 # m/s
vy0 = -2.785900354076842E+01 * 1000 # m/s
vz0 = 1.330149860683250E-03 # m/s

x0 = -1.385683325048748E+08 * 1000 # meter 
y0 = 5.518939763457818E+07 * 1000 # meter
z0 = 3.711333408605307E+03 * 1000 # meter


x = np.zeros(N); x[0] = x0
y = np.zeros(N); y[0] = y0
z = np.zeros(N); z[0] = z0

vx = np.zeros(N); vx[0] = vx0
vy = np.zeros(N); vy[0] = vy0
vz = np.zeros(N); vz[0] = vz0


for i in range(N-1):
    r = (x[i]**2 + y[i]**2 + z[i]**2)**(0.5)
    a = -G*m_sola/r**3

    vx[i+1] = vx[i] + a*dt*x[i]
    vy[i+1] = vy[i] + a*dt*y[i]
    vz[i+1] = vz[i] + a*dt*z[i]

    t[i+1] = t[i] + dt
    x[i+1] = x[i] + dt*vx[i+1]
    y[i+1] = y[i] + dt*vy[i+1]
    z[i+1] = z[i] + dt*vz[i]

# Plotte i AU?
x = x/AU
y = y/AU
z = z/AU

vx = vx/AU
vy = vy/AU
vz = vz/AU

# Plotte tiden i dager?
t = t/(60*60*24)

# Plotte banen
plt.plot(x[0],y[0], '*b')
plt.plot(x[-1],y[-1], '*g')
plt.plot(x,y, 'b')
plt.plot(0,0,'*y')

plt.axis('equal')
plt.show()
plt.savefig('bane.png')
plt.clf()

# Plotte hastigheter
plt.plot(t,vx, label='vx')
plt.plot(t,vy, label='vy')
plt.plot(t,vz, label='vz')

plt.legend()
plt.show() 
plt.savefig('hastigheter.png')
plt.clf()

# Plotte posisjoner
plt.plot(t,x, label='x')
plt.plot(t,y, label='y')
plt.plot(t,z, label='z')

plt.legend()
plt.show() 
plt.savefig('posisjoner.png')
plt.clf()
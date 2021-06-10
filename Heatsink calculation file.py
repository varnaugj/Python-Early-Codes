#heatsink calculation file

import math
import scipy 
from scipy import constants as const 

#simple heatsink

#values that need lookup tables:
#alpha
#nu
#k
#eps

Ts = 50     #source temp
Tamb = 25   #ambient air temp
H = 0.02     #height heatsink
L = 0.2     #length heatsink
t = 0.01   #thickness of fins
Q = 30     #source heat (watts)
b = 0.01    #base thickness
Tavg = (Ts - Tamb)/2                #average temperature
beta = 1/Tavg
alpha = 22.39*(10**(-6))            #thermal diffusivity of air at Tavg
nu = 15.52*(10**(-6))               #kinematic viscosity of air at Tavg
k = 205                             #thermal conductivity (aluminum)
eps = 0.09                                    #surface emissivity (aluminum)
sig = const.Stefan_Boltzmann                  #stefanBoltzmann const 


h1 = 1.42*(((Ts-Tamb)/H)**(1/4))        #approximation of convection coefficient based on small horizontal surfaces relative to vertical

sopt = 2.71*((const.g)*beta*(Ts - Tamb)/(L*alpha*nu))**(-1/4)     #optimum spacing of fins


h2 = (1.31*k)/sopt

A1 = H*L + t*(2*H + L)
A2 = L*(2*(H-b) + sopt) + 2*(t*H + sopt*b) + t*L    #Heat dissipation due to convection from fins to Air

Q_c1 = 2*h1*A1*(Ts - Tamb)              #Heat dissipation from some external source to heat sink

Q_c2 = h2*A2*(Ts - Tamb)

#Radiation calculations


AR2 = L*(t + sopt) + 2*(t*H + sopt*b)         #approximate solution of radiation from heatsink

#print(AR2)

Q_r1 = 2*eps*sig*A1*(Ts**4 - Tamb**4)

Q_r2 = eps*sig*AR2*(Ts**4 - Tamb**4)


print(h2)
print(Q_c2)
print(Q)

#print(Q_r2)
#print(Q_r1)

N = (1 + (Q - Q_r2 - Q_c2)/(Q_r1 + Q_r2))

W = (N-1)*sopt + N*t

print(round(N))
print(W/1000)

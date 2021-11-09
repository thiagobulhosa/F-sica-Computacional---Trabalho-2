#Thiago dos Santos
#Thiago Bulhosa

from sympy import Lambda,var,sqrt
from scipy.integrate import quad
from numpy import inf, linspace
import matplotlib.pyplot as plt

x=var("x")
o1=0.32
o2=0.296
space=linspace(0.15,0.45,100)
H01=68.7
H02=66.9
Tempo1=[]
Tempo2=[]

E1=Lambda(x,sqrt(o1*(1+x)**3+1-o1))
E2=Lambda(x,sqrt(o2*(1+x)**3+1-o2))
f1=Lambda(x,1/((1+x)*E1(x)))
f2=Lambda(x,1/((1+x)*E2(x)))
integral_E1 = quad(f1,0,inf)
integral_E2 = quad(f2,0,inf)
T1 = (1 / H01) * integral_E1[0]
T2 = (1 / H02) * integral_E2[0]

print("A variação da idade do universo é entre",T1,"e",T2,"giga-anos.")
print("\n\n")

for o in space:
    E=Lambda(x,sqrt(o*(1+x)**3+1-o))
    f=Lambda(x,1/((1+x)*E(x)))
    integral_E=quad(f,0,inf)
    Temp1=(1/H01)*integral_E[0]
    Temp2=(1/H02) *integral_E[0]
    Tempo1.append(Temp1)
    Tempo2.append(Temp2)

plt.plot(space,Tempo1,"blue",label="obj1")
plt.plot(space,Tempo2,"red",label="obj1")

plt.show()
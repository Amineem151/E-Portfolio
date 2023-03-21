

import numpy as np  ; import matplotlib.pyplot as plt ; import math ; import time

T=0.25
Omega=2*math.pi/T

nend=10

# spatial domain
xleft = -2*T ; xright = 2*T

# num of grid points  ; # x grid of n points # Time step 
m = 101  ; x, dx = np.linspace(xleft,xright,m,retstep=True)  ;


fig, axs = plt.subplots(2, 2)
def plotsol(NN,YC,Uo):
    axs[0, 0].plot(x, Uo, color='red',marker=".")
    axs[0, 0].set_title("Fig. 1")
    axs[1, 0].plot(NN, YC, color='white', marker="o",markeredgecolor='green')
    axs[1, 0].set_title("Fig. 2")
    axs[0, 1].plot(x, Uo, color='black',marker="+")
    axs[0, 1].set_title("Fig. 3")
    axs[1, 1].plot(x, Uo, color='cyan',marker="x")
    axs[1, 1].set_title("Fig. 4")

    

YC= [(4/math.pi)]
NN= [1]

Uo = (4/math.pi)*np.sin(Omega*x)
plotsol(NN,YC,Uo)
plt.show()
time.sleep(0.1)


n=2
while n <= nend:
    fig, axs = plt.subplots(2, 2)
    Uo=Uo+(4/math.pi)*(1/n)*np.sin(n*Omega*x)
    modharm=(4/math.pi)*(1/n)
    YC.append(modharm)
    NN.append(n);
    plotsol(NN,YC,Uo)
    plt.show()
    time.sleep(0.1)
    n=n+1
    
#signal 1 sinusoidal
x = np.sin(2*np.pi*f*n) # expression mathematique
plt.figure(figsize=(8,4)) #creation de la figure
plt.plot(n, x, label="sinusoïde") #Affichage du signal
plt.legend() #legende
plt.xlabel("$n$") #les axes
plt.ylabel("$x[n]$")
plt.title("signal 1 sinusoïde") #titre
plt.show() #affichage

#signal 2 sinusoidal
x = np.cos*(w*t+nu) # expression mathematique
plt.figure(figsize=(8,4)) #creation de la figure
plt.plot(n, x, label="sinusoïde") #Affichage du signal
plt.legend() #legende
plt.xlabel("$n$") #les axes
plt.ylabel("$x[n]$")
plt.title("signal 2 sinusoïde") #titre
plt.show() #affichage

print(quit)
quit()


    





from cmath import pi
from pyexpat.errors import XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING
from re import X
import stat

m=100   
piap1=0; piap2=0; piap3=0
T=2
Omega=2*pi/T    #faire 2x pi divisé par T ( on peut utiliser multiply et devide(a,b))
om==Omega
xrange(4*pi,4*T/200,2*T)  #séquences
x=-2*T:4*T/200:2*T
ST==ones 
x.getshape()    #matrix dimensions
ST=0.5*stat
zeros(x.getshape(),Float) #0 filled array
YT=[];YC=YT
for i in range(1,M+1)
     p=i-1
    n=2*p+1
    ST=ST+(4/pi^2)*(1/n^2)*cos(n*Om*x)
    YT=[YT (4/pi^2)*(1/n^2)]
    
    SC=SC+(4/pi)*(1/n)*sin(n*Om*x)
    YC=[YC (4/pi)*(1/n)]
    
    %Calcul de Pi
    piap1 = piap1 +(-1)^p/(2*p+1)
    piap2 = piap2 +(1)/(2*p+1)^2
    piap3 = piap3 +(1)/(p+1)^2

print(i)        # les loops de for

figure(1)
plot(x,SC,'xr',x,SC,'b') # plot est utilisé de la même manière qu'avec matlab
#title("CrÃ©neau") la fonction title ne peut pas etre converti en python (pas d'equivalent)
figure(2)
plot(x,ST,'xr',x,ST,'b')
figure(3)
stem(YT) #stem(YT) trace la séquence de données, YT, sous forme de tiges qui s'étendent à partir d'une ligne de base le long de l'axe des x. Les valeurs de données sont indiquées par des cercles terminant chaque tige.
figure(4)
stem(YC) #stem(YC) trace la séquence de données, YC, sous forme de tiges qui s'étendent à partir d'une ligne de base le long de l'axe des x. Les valeurs de données sont indiquées par des cercles terminant chaque tige.

piap1=abs(pi-4*piap1)
piap2=abs(pi-sqrt(8*piap2))
piap3=abs(pi-sqrt(6*piap3))
end 
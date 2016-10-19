import math as m
KB=0.9/2
KG=0.5
tan=0.2
cos=1/m.sqrt((1+tan*tan))
#d=1/cos
d=1
Ioy=(d)**3/12
Vs=0.9
BM=Ioy/Vs
GM=KB+BM-KG
sin=tan/m.sqrt((1+tan*tan))
l=GM*sin

rho=1000
g=9.8
M=0.9*rho*g*l





print('KB:',KB,' KG:',KG,' d:',d,' Ioy:',Ioy,' BM:',BM,' GM:',GM,' l:',l,' M:',M)
KB=0.9/3
KG=0.5
tan=0.2
cos=1/(1+tan*tan)
r=0.5/cos
Ioy=(2*r)**3/12
Vs=0.9
BM=Ioy/Vs
GM=KB+BM-KG
sin=tan/(1+tan)
l=GM*sin

rho=1000
g=9.8
M=rho*g*l





print('KB:',KB,' KG:',KG,' Ioy:',Ioy,' BM:',BM,' GM:',GM,' l:',l,' M:',M)
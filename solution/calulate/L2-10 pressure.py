import math as m
tan=0.2
cos=1/m.sqrt(tan*tan+1)
h1=1*0.5*cos
h2=0.8*0.5*cos
h3=(1+0.8)*0.5*cos

rho=1000
g=9.8
A1=1
A2=0.8
A3=1
F1=rho * g *h1*A1
F2=rho * g* h2*A2
F3=rho *g *h3*A3

l1=0.5-1/3.0
l2=(0.5-0.8*1/3.0)
I3=1/12.0
y3=(1+0.8)*0.5/tan
A3=1.0
l3=I3/(y3*A3)

M1=F1*l1
M2=F2*l2
M3=F3*l3

M=M2+M3-M1


print('h1:',h1,' h2:',h2,' h3:',h3,' F1:',F1,' F2:',F2,' F3:',F3,' l1:',l1,' l2:',l2,' l3:',l3,' M1:',M1,' M2:',M2,' M3:',M3,' M:',M)
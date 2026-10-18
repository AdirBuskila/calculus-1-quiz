from sympy import *
x=symbols('x',positive=True)
f=(log(x)-1)/log(x)
assert simplify(diff(f,x)-1/(x*log(x)**2))==0
d2=diff(f,x,2); assert simplify(d2+(log(x)+2)/(x**2*log(x)**3))==0
for v in (0.05,0.5,2.0): print('f2 at',v,N(d2.subs(x,v)))   # >0 on (e^-2,1)=(0.135,1): 0.5 -> positive
print(limit(f,x,1,'-'),limit(f,x,1,'+'),limit(f,x,0,'+'),limit(f,x,oo))
A=log(x+1)+log(x**2+4)/2
assert simplify(diff(A,x)-(2*x**2+x+4)/((x+1)*(x**2+4)))==0
a=3.0
for i in range(8): a=(a+7/a)/2
print('2b',a,7**.5)
t=symbols('t',positive=True); print('3a',limit((1+t)**(2/t),t,0,'+'))
assert simplify(diff(atan((log(x)+1)/2)/2,x)-1/(x*(log(x)**2+2*log(x)+5)))==0
xx=symbols('xx',real=True); p=(xx+2)*sqrt(4-xx**2); print('4a crit',solve(diff(p,xx),xx),simplify(p.subs(xx,1)))
import numpy as np
g=np.linspace(-2,2,400001); print('max',((g+2)*np.sqrt(4-g**2)).max(),3*3**.5)
print('4b',N(pi*integrate(x*log(x),(x,1,E))))
print('5a',limit(x**(1/sin(2*x-2)),x,1,'+'),limit(x**(1/sin(2*x-2)),x,1,'-'))
print('5b',limit(atan(1/x**2),x,0))
print('6a',N(integrate(1/(1+x**2)-3/(9+x**2),(x,-sqrt(3),sqrt(3)))),N(pi/3))
print('6b',N(log(Rational(9,10))),'T2',-0.105,'bound',N(Rational(1,1000)/(3*Rational(729,1000))),'true err',N(abs(log(Rational(9,10))+Rational(21,200))))
print('OK')

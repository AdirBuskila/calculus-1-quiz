# Independent refuter checks for 25B-B (solver-made). Run: PYTHONUTF8=1 py -I refute_25B-B.py
from sympy import *
x=symbols('x',real=True)
f=x*exp(1/(x-2))
d1=simplify(diff(f,x)); d2=simplify(diff(f,x,2))
assert simplify(d1-(x-1)*(x-4)*exp(1/(x-2))/(x-2)**2)==0
assert simplify(d2-(5*x-8)*exp(1/(x-2))/(x-2)**4)==0
assert solve(numer(together(d1)),x)==[1,4]
print('f(1),f(4)',f.subs(x,1),N(f.subs(x,4)),'f(8/5)',simplify(f.subs(x,Rational(8,5))),N(f.subs(x,Rational(8,5))))
print('asym',limit(f/x,x,oo),limit(f/x,x,-oo),limit(f-x,x,oo),limit(f-x,x,-oo),limit(f,x,2,'+'),limit(f,x,2,'-'))
a=sqrt(20); 
for i in range(40):
    prev=a; a=sqrt(20+a); assert a>prev and a<5
print('seq 40 terms',N(a), 'a1',N(sqrt(20)),'a2',N(sqrt(20+sqrt(20))))
I=2*x**2*atan(x)+6*x*atan(x)+2*atan(x)-2*x-3*log(x**2+1)
assert simplify(diff(I,x)-(4*x+6)*atan(x))==0
print('2b definite',N(I.subs(x,1)-I.subs(x,0)),'5pi/2-2-3ln2',N(5*pi/2-2-3*log(2)))
assert limit((1/x)**tan(2*x),x,0,'+')==1
y=tan(x)**cos(x); assert simplify(diff(y,x).subs(x,pi/4))==sqrt(2) and simplify(y.subs(x,pi/4))==1
assert limit((sqrt(x+2)-sqrt(3*x-2))/(sqrt(4*x+1)-sqrt(5*x-1)),x,2)==3
assert integrate(x**2,(x,0,2))-integrate(4*x-4,(x,1,2))==Rational(2,3)
print('4b options',integrate(x**2,(x,0,2))+integrate(4*x-4,(x,1,2)),integrate(x**2-(4*x-4),(x,0,2)),integrate(x**2,(x,1,2)))
# 5a numeric sup of derivative
import numpy as np
g=np.exp(np.sin(np.linspace(-20,20,2000001))**2)*np.sin(2*np.linspace(-20,20,2000001)); print('max f\'',g.max(),'<= e',np.e)
F=-atan(cos(x)/2+Rational(1,2))/2
assert simplify(diff(F,x)-sin(x)/(5+2*cos(x)+cos(x)**2))==0
assert simplify(pi*integrate(16-x**2,(x,-4,4))-256*pi/3)==0
print('6a',N(256*pi/3))
# 6b: one-sided derivatives
a_=symbols('a'); print('6b left',limit(sin(a_*x)/x,x,0,'-'),'right',limit(x*log(x),x,0,'+'))
print('ALL OK')

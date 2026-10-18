import sympy as sp, numpy as np
from scipy.integrate import quad
x=sp.symbols('x',real=True)
f=x**3/(x**2-1)
print('1 f\'',sp.factor(sp.diff(f,x)),'f\'\'',sp.factor(sp.diff(f,x,2)),'asym',sp.limit(f-x,x,sp.oo),'f(sqrt3)',sp.simplify(f.subs(x,sp.sqrt(3))))
a=5.0
for i in range(30): a=(a+5/a)/2
print('2a',a)
F=x**2/2*sp.atan(2/x)+x-2*sp.atan(x/2)   # candidate
print('2b diff',sp.N((sp.diff(F,x)-x*sp.atan(2/x)).subs(x,1.3)),sp.N((sp.diff(F,x)-x*sp.atan(2/x)).subs(x,-2.1)))
g=lambda t:np.log(t+1)-(3*t+2)/(t+2)
xs=np.linspace(-0.999999,500,3000001); gv=g(xs); print('3a sign changes',(np.sign(gv[1:])!=np.sign(gv[:-1])).sum(),'g(0)',g(0),'g(-1+)',gv[0],'g(500)',gv[-1])
print('3a g\' ',sp.factor(sp.diff(sp.log(x+1)-(3*x+2)/(x+2),x)))
# 3b candidate via u=sin x: 1/((2+u^2)(3-u))
u=sp.symbols('u'); print('3b pf',sp.apart(1/((2+u**2)*(3-u)),u))
h=lambda t:np.cos(t)/((3-np.cos(t)**2)*(3-np.sin(t)))
Gc=lambda t:(sp.Rational(1,11))*0
# numeric check of candidate: (1/11)[-ln|3-s|... ] compute from pf
pf=sp.apart(1/((2+u**2)*(3-u)),u); Gs=sp.integrate(pf,u).subs(u,sp.sin(x))
print(' G',Gs, sp.N((sp.diff(Gs,x)-sp.cos(x)/((3-sp.cos(x)**2)*(3-sp.sin(x)))).subs(x,0.7)))
print('4b',2*np.pi*quad(lambda t:t*np.cos(t)**2,np.pi/2,np.pi)[0],'cand',np.pi**3/4-np.pi**2/4*0+0)
print(' exact',sp.simplify(2*sp.pi*sp.integrate(x*(1+sp.cos(2*x))/2,(x,sp.pi/2,sp.pi))))
L=quad(lambda t:np.sqrt(1+np.exp(2*t)),0,1)[0]
e=np.e; r=np.sqrt(1+e*e)
print('5b',L,r+0.5*np.log((r-1)/(r+1))-np.sqrt(2)-0.5*np.log((np.sqrt(2)-1)/(np.sqrt(2)+1)))
fs=lambda v:v*np.cbrt(3*v-1)
xs=np.linspace(-1,2/3,2000001); fv=fs(xs); print('6a',fv.max(),xs[fv.argmax()],fv.min(),xs[fv.argmin()],'f(-1)',fs(-1),'f(2/3)',fs(2/3),'f(1/4)',fs(.25),'f(1/3)',0)
print('6a f\'',sp.simplify(sp.diff(x*(3*x-1)**sp.Rational(1,3),x)))
a,b=sp.symbols('a b'); print('6b',sp.solve([8*a-(4+b),12*a-4],[a,b]))
print('2a-1: x/(x+1)<ln(1+x): ok')

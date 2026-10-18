import sympy as sp, numpy as np
from scipy.integrate import quad
x=sp.symbols('x',real=True)
xs=np.linspace(0,3,300001); fv=0.8*xs-np.abs(xs-1)**0.8+2
print('1a num',fv.max(),xs[fv.argmax()],fv.min(),xs[fv.argmin()])
print('1a f(2)',0.8*2-1+2,'f(0)',0+(-1)+2,'f(3)',2.4-2**0.8+2,'f(1)',2.8-0)
for A in [0,2,5]:
  for B in [0,3]:
    a=float(A+B+2)
    for i in range(80): a=(a+(A+1)/a)/2
    print('1b',A,B,a,np.sqrt(A+1))
# 2b candidate: x^2/2 atan(x^2) - 1/4 ln(1+x^4)
F=x**2/2*sp.atan(x**2)-sp.log(1+x**4)/4
print('2b',sp.simplify(sp.diff(F,x)-x*sp.atan(x**2)))
for A in [0,3]:
 for B in [0,1,4]:
    print('3a',A,B,sp.factor(2*x**2-(2*B+3)*x+B+1))
print('3b left',sp.limit((x-sp.sin(x))/x**3,x,0,'-'),' right series',sp.series((sp.exp(sp.Symbol('p')*x)-sp.Symbol('p')*x-1)/x**2,x,0,2))
# 3b: left derivative = lim (x-sin x)/x^3=1/6 ; right: (e^{px}-px-1)/x^2 -> p^2/2, need finite & p^2/2=1/6 ? p=±1/sqrt3
print('3b p', sp.solve(sp.Symbol('q')**2/2-sp.Rational(1,6),sp.Symbol('q')))
print('4a b^2-1-2ln b min', min(b*b-1-2*np.log(b) for b in np.linspace(0.05,5,100000)))
G=sp.apart((3*x**3+x**2+4*x+8)/(x**4+4*x**2),x); print('4b',G)
cand=3*sp.log(x)/1 if False else None
for A in [0,2]:
  k=A+2
  r=quad(lambda t:k/(1+t*t)-k*t*t/2,-1,1)[0]; print('5b',A,r,k*(np.pi/2-1/3))
  print('  root check',k/(1+1)-k/2)
# 6a numeric
for h in [1e-1,1e-2,1e-3]:
  num=h-np.arcsin(h); den=quad(lambda t:np.log(1+t*t),0,h)[0]; print('6a',h,num/den)
for B in [0,1,3]:
  for C in [0,1,3]:
    V=2*np.pi*quad(lambda t:t*(t*t+B+1)**0.2,0,C+1)[0]
    u=B+1; cand=np.pi*5/6*(((C+1)**2+u)**1.2-u**1.2)
    print('6b',B,C,V,cand)

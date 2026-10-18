import sympy as sp, numpy as np
from scipy.integrate import quad
x=sp.symbols('x',real=True)
f=x**4/(x**3-1)
print('1 f\'',sp.factor(sp.diff(f,x)),'\n f\'\'',sp.factor(sp.diff(f,x,2)),'\n slant',sp.limit(f-x,x,sp.oo),'crit',sp.solve(sp.diff(f,x),x))
c=sp.Rational(4,3)**sp.Rational(1,3)
print(' f(4^(1/3))',sp.N(f.subs(x,sp.Integer(4)**sp.Rational(1,3))), 'x=',sp.N(sp.Integer(4)**sp.Rational(1,3)))
# 2a: x^3/(x^2-x+2) = x+1 + (-x-2)/(x^2-x+2)
print('2a',sp.apart(x**3/(x**2-x+2),x),sp.limit(x**3/(x**2-x+2)-x-1,x,sp.oo))
print('2b factors',sp.factor(x**2-4*x+3))
print('3a',sp.limit((sp.sqrt(1+sp.sin(x/2))-sp.sqrt(1-sp.sin(x/2)))/x,x,0))
F=(x**2/2+x)*sp.atan(x)-x/2-sp.atan(x)/2*0 # placeholder
Gc=sp.integrate(sp.Rational(1,1)*0,x)
cand=(x**2/2+x+sp.Rational(1,2))*sp.atan(x)-x/2-sp.log(1+x**2)/2
print('3b diff',sp.simplify(sp.diff(cand,x)-(x+1)*sp.atan(x)))
# 4b: shell about x=4: R=4-x, region 0<=x<=4 between y=x^2 (below?) and y=2x+8
V=2*np.pi*quad(lambda t:(4-t)*(2*t+8-t*t),0,4)[0]; print('4b',V,128*np.pi, 'x=4 intersection: 2x+8=x^2 at',sp.solve(x**2-2*x-8,x))
# 5a
p=lambda t:6*t**5-4*t+1; print('5a',p(0),p(1),p(0.5))
print('5b',sp.limit(2*(1-sp.cos(x))/x**4-1/x**2,x,0))
g=sp.cbrt(x**2-2*x); 
xs=np.linspace(-1,3,4000001); fv=np.cbrt(xs**2-2*xs); print('6a',fv.max(),xs[fv.argmax()],fv.min(),xs[fv.argmin()],'f(-1)',np.cbrt(3),'f(3)',np.cbrt(3),'f(1)',-1)
# 6b: first quadrant between y=4x^2,y=x^2/9,y=2 : x=sqrt(y/4) .. sqrt(9y)
A=quad(lambda y:3*np.sqrt(y)-np.sqrt(y)/2,0,2)[0]; print('6b',A,'cand',5/2*2/3*2**1.5, 5*np.sqrt(2)*2/3)

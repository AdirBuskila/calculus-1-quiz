from sympy import *
x,t=symbols('x t',real=True)
print(integrate((x**2+2*x)*cos(2*x),x))
print(integrate(x/((x+1)*(x**2+1)),x))
print(limit(1/log(x)-1/(x-1),x,1), limit(integrate(tan(t),(t,0,x))/(x*sin(x)),x,0))
print(integrate(abs(x**2+2-2*x-5),(x,0,6)))
f=(x**2+5)/(x+2); print([f.subs(x,v) for v in (0,1,10)])
b,a=symbols('a b'); print(limit(sin(b*x)/(x+sin(2*x)),x,0,'-'))
print(simplify(diff((x**3-1)/x**2,x,2)), solve(diff((x**3-1)/x**2,x),x))

from sympy import *
x,t=symbols('x t',real=True)
f=x*exp(1-2*x**2)
assert simplify(diff(f,x)-exp(1-2*x**2)*(1-4*x**2))==0
assert simplify(diff(f,x,2)-4*x*exp(1-2*x**2)*(4*x**2-3))==0
print(N(f.subs(x,Rational(1,2))),N(f.subs(x,sqrt(3)/2)))
a=1.0
for i in range(60): a=2*a/(a+3)
print('a60',a)
# 2b: antiderivative check numerically
F=1/(2-tan(x/2)); 
for v in (0.3,1.0,-1.0,2.0): print(N(diff(F,x).subs(x,v)),N((1/(5-4*sin(x)+3*cos(x))).subs(x,v)))
assert limit((x-integrate(cos(t**2),(t,0,x**2)))/(x**3-6*x),x,0)==Rational(-1,6)
print('3b',N(pi*integrate(x*log(x),(x,1,E))),N(pi*(E**2+1)/4))
print('4b',N(integrate(sqrt(1+Rational(9,4)*x),(x,0,1))),N((13*sqrt(13)-8)/27))
print('5a f(-1)',N(-2-3*pi/4+exp(-1)+1),'f\' min',N(minimum(6*x**2+3/(1+x**2)+exp(x),x,Interval(-50,50))) if False else 'f\'>0 termwise')
# 5b tangent from origin
a_=symbols('a',positive=True); print('5b a',solve(Eq(1/(2*sqrt(a_-1)),sqrt(a_-1)/a_),a_), 'area',1-Rational(2,3))
G=log(abs(x+1))/2-log(x**2+4*x+5)/4-atan(x+2)/2
assert simplify(diff(G,x)-1/((x+1)*(x**2+4*x+5))).subs(x,0.37)==0 or abs(N(diff(G,x).subs(x,0.37)-1/((1.37)*(0.37**2+4*0.37+5))))<1e-12
print('6b bound (0.1)^3:',N(Rational(1,3)*Rational(1,1000)/Rational(729,1000)),' with (0.01)^3 as printed:',N(Rational(1,3)*Rational(1,10**6)/Rational(729,1000)))
print('OK')

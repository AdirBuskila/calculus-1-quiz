from sympy import *
x,y=symbols('x y',real=True)
f=2*x*exp(-x**2/2)
assert simplify(diff(f,x)-2*exp(-x**2/2)*(1-x**2))==0
assert simplify(diff(f,x,2)+2*x*exp(-x**2/2)*(3-x**2))==0
print('f(1)',N(f.subs(x,1)),'f(sqrt3)',N(f.subs(x,sqrt(3))))
a=Integer(1)
for i in range(5): a=a/2+1; print(N(a),end=' ')
print()
assert simplify(diff(x**2/2-3*log(x**2+1)/2,x)-(x**3-2*x)/(x**2+1))==0
print('2b def',N(Rational(1,2)-3*log(2)/2))
print(solve([2*symbols('a')+1-(4-symbols('b')), symbols('a')+1-(2-symbols('b'))],symbols('a b')))
g=lambda z:2*z**3-z**2+z+1
print('g(-3)',g(-3),'g(0)',g(0),'disc g\'',discriminant(6*x**2-2*x+1,x))
assert limit(((x**2+5*x+4)/(x**2-3*x+7))**(2*x),x,oo)==exp(16)
print('4b',N(pi*integrate(log(x)**2,(x,1,E))),'e-2',N(E-2),'pi',N(pi),'2pi(e-2)',N(2*pi*(E-2)))
F=y-pi*x*sin(y/2); print('5a',simplify((-diff(F,x)/diff(F,y)).subs({x:1,y:pi})))
assert limit(x**(1/log(exp(x)-1)),x,0,'+')==E
h=lambda v:2*v+3*Abs(v)**Rational(2,3)
print('6a',N(h(-2)),h(-1),h(0), 'grid max/min',max(N(h(-2+i*0.0002)) for i in range(10001)),min(N(h(-2+i*0.0002)) for i in range(10001)))
print('6b',N(9**Rational(1,3)),N(2+Rational(1,12)),N(Rational(1,288)))
print('OK')

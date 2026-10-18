from sympy import *
x,a,b,p,q,u=symbols('x a b p q u',real=True)
f=exp(2*x)/x
print('Q1',factor(diff(f,x)),factor(simplify(diff(f,x,2))),solve(diff(f,x),x),solve(diff(f,x,2),x))
print(' f(1/2)',f.subs(x,Rational(1,2)),N(f.subs(x,S.Half)),' lim0+-',limit(f,x,0,'+'),limit(f,x,0,'-'),limit(f,x,oo),limit(f,x,-oo),limit(f/x,x,oo))
print(' f2 numer', simplify(diff(f,x,2)*x**3/exp(2*x)))
# 2a sequence
s=[Rational(3,2)]
for i in range(8): s.append(3-2/s[-1])
print('2a',[N(v,6) for v in s])
print(' ineq: a_{n+1}-a_n = ', factor(3-2/x-x))
# 2b
sol=solve([ -1/p**2-2*q, 2/p+q**2],[p,q],dict=True); print('2b',sol)
print(' tangent at q=-2:',2*(-2),-(-2)**2)
print('3a',limit((sin(x)/x)**(1/x**2),x,0), exp(Rational(-1,6)))
print('3b',apart((2*x**2+15)/(x*(x**2+2*x+5)),x), integrate((2*x**2+15)/(x*(x**2+2*x+5)),x))
# 4a
e1=sqrt(x**2+x+a)-sqrt(x**2-b*x)
for av,bv in [(6,-1)]:
    print('4a',limit(x*e1.subs({a:av,b:bv}),x,oo))
print(' b=-1 general', limit(x*e1.subs(b,-1),x,oo), ' b=0', limit(x*e1.subs({b:0,a:1}),x,oo))
print('4b',integrate(sin(x)*cos(x)/(1+sin(x)**2),x), simplify(diff(log(1+sin(x)**2)/2,x)-sin(x)*cos(x)/(1+sin(x)**2)))
h=(x-1)**Rational(2,3)*sin(x-1)
t=symbols('t')
print('5a',limit(((t**Rational(2,3))*sin(t))/t,t,0,'+'),limit(((t**2)**Rational(1,3)*sin(t))/t,t,0,'-'))
y=Rational(2,5)*x**Rational(5,4)-Rational(2,3)*x**Rational(3,4)
yp=diff(y,x); print('5b',simplify(1+yp**2), integrate((x**Rational(1,4)+x**Rational(-1,4))/2,(x,0,1)))
g=(x**2+a)/(x-b)
print('6a',solve([4-4*b-a, b-7],[a,b]), limit(((x**2-24)/(x-7))-x,x,oo))
print(' g\'(2)=',simplify(diff(((x**2-24)/(x-7)),x).subs(x,2)))
A=integrate(log(x+1)/sqrt(x+1),(x,0,1)); print('6b',simplify(A),N(A), N(2*sqrt(2)*log(2)-4*sqrt(2)+4))

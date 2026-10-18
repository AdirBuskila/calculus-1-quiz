from sympy import *
x,a=symbols('x a',real=True)
f=2*x**2/(x**2-1)
print('Q1',factor(diff(f,x)),factor(diff(f,x,2)),solve(diff(f,x),x),f.subs(x,0),limit(f,x,oo),limit(f,x,1,'+'),limit(f,x,1,'-'),limit(f,x,-1,'+'),limit(f,x,-1,'-'))
s=[Integer(4)]
for i in range(8): s.append(sqrt(5*s[-1]-6))
print('2a',[N(v,8) for v in s],solve(x**2-5*x+6,x))
F=x**3+exp(x)+x
print('2b',diff(F,x),N(F.subs(x,-1)),F.subs(x,0), nsolve(F,x,-0.5))
print('3a',limit((1+exp(x))**(1/x),x,oo))
print('3b',integrate(asin(x),x))
print('4a',solve(Eq(log(a),log(a)**2),a))
print('4b',solve(Eq(2*x/(1+x**2),1),x),log(2)-1)
print('5a',limit(sqrt(2+2*x+x**2)-sqrt(2-2*x+x**2),x,-oo))
print('5b',apart(x/((x**2+1)*(x+1)),x),integrate(x/((x**2+1)*(x+1)),x))
V=pi*integrate((pi/2-x)**2-cos(x)**2,(x,0,pi/2)); print('6a',simplify(V),N(V),N(pi**4/24-pi**2/4))
print(' check line>=cos', min(N(pi/2-v-cos(v)) for v in [i*pi/2/100 for i in range(101)]))
A=integrate(sqrt(x+2),(x,-2,2))-integrate(sqrt(2*x),(x,0,2)); print('6b',simplify(A))
print(' cross-check via y: ', integrate((y:=symbols('y'))**2-2+0*y -( y**2/2),(y,0,2)) if False else integrate((symbols('y')**2-2)*0+ (symbols('y')**2/2 - (symbols('y')**2-2)),(symbols('y'),0,2)))

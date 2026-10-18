import sympy as sp
x,n=sp.symbols('x n',positive=True)
# 1a
f=2*x+3*sp.cbrt(x**2)
print('1a f\'', sp.simplify(sp.diff(f,x)), ' f(0)=0; crit x=-1 f=',f.subs(x,-1))
# 1b: general A,C
for A in [0,3,9]:
  for C in [0,4,9]:
    e=((n+2)*sp.factorial(n+1)+(A+1)*n*sp.factorial(n+1))/(sp.factorial(n+1)-n*sp.factorial(n))
    # simplify manually: (n+1)!=(n+1)n!, (n+2)! = (n+2)(n+1)n!
    e=((n+2)*(n+1)+(A+1)*n*(n+1))/((n+1)-n)*sp.sin(sp.Integer(C+1)/(n+1)**2)
    print('1b',A,C,sp.limit(e,n,sp.oo), 'formula',(A+2)*(C+1))
# 2b
for B in [0,4,9]:
  for C in [0,5,9]:
    p=B+3;q=B+2
    L=sp.symbols('L')
    sols=sp.solve(sp.Eq(L,p*L/(q*L+1)),L)
    # simulate
    a=sp.Rational(C+2)
    for i in range(60): a=p*a/(q*a+1)
    print('2b',B,C,sols,float(a),'a1',C+2)
# 3a
for A in [0,3,9]:
  for B in [0,4,9]:
    f=(x+A)*(2+sp.cos((B+1)/(x+A)))
    print('3a',A,B,sp.limit(f/x,x,sp.oo),sp.limit(f-3*x,x,sp.oo),sp.limit(f-3*x,x,-sp.oo), sp.limit(f.subs(x,x-A),x,0,'+'))
# 3b
t=sp.symbols('t')
F=sp.integrate(1/(1+sp.sin(x)+3*sp.cos(x)),x)
print('3b',F); print(sp.simplify(sp.diff(F,x)-1/(1+sp.sin(x)+3*sp.cos(x))))
# 4b
print('4b',sp.integrate(sp.atan(sp.sqrt(x))**3/((x+1)*sp.sqrt(x)),x))
# 5a
for A in [0,3,9]:
  for C in [0,4,9]:
    e=(x**3+A)*(sp.sqrt(x**2+sp.sqrt(x**4+C+1))-x*sp.sqrt(2))
    print('5a',A,C,sp.limit(e,x,sp.oo), sp.N(e.subs(x,10**4),30) )
# 5b
s=sp.symbols('s')
print('5b',sp.integrate(1/sp.sin(x),(x,sp.pi/3,sp.pi/2)),sp.log(sp.sqrt(3)))
# 6a
g=1/sp.sin(x)-1/x
print('6a',sp.limit(g,x,0),sp.limit(g/x,x,0))
# 6b
for B in [0,1,3]:
  V=2*sp.pi*sp.integrate(x*sp.sin((B+1)*x)**2,(x,0,sp.pi/(B+1)))
  print('6b',B,sp.simplify(V), 'cand pi^3/(2(B+1)^2)? ',sp.pi**3/(2*(B+1)**2))

import sympy as sp
x,n=sp.symbols('x n',positive=True)
# 1
f=x**3/(x**2-1)
print(sp.factor(sp.diff(f,x)),sp.factor(sp.diff(f,x,2)),sp.N(f.subs(x,sp.sqrt(3))))
print(sp.solve(sp.diff(f,x),x), sp.limit(f/x,x,sp.oo), sp.limit(f-x,x,sp.oo))
# 2a
g=(x**2+8)/(x**4+4*x**2)
F=-2/x-sp.atan(x/2)/2
print(sp.simplify(sp.diff(F,x)-g))
# 2b
a=sp.Integer(2);seq=[a]
for i in range(3): a=sp.Rational(3)/(2+1/a);seq.append(a)
print(seq,[sp.N(s) for s in seq])
# 3a
print(sp.limit(sp.sqrt(1+n+n**2)-sp.sqrt(1-2*n+n**2),n,sp.oo))
# 3b
print(sp.N(2*sp.pi*sp.integrate(x*(sp.E-sp.exp(x)),(x,0,1))), sp.N(sp.pi*(sp.E-2)))
# 4a
t=sp.log(x); y=t**2-2*t
print([y.subs(x,v) for v in (sp.sqrt(sp.E),sp.E,sp.E**2)])
# 4b
print(sp.limit(3*x**4/(x**3+2*x+9)-3*x,x,sp.oo))
for A in (2,4): print(A,sp.limit(3*x**4/(x**3+2*x+9)-A*x,x,sp.oo))
# 5a
xx=sp.symbols('xx',real=True)
print(sp.limit(sp.exp(xx/(xx+2)),xx,-2,'-'),sp.limit(sp.atan(1/xx),xx,0,'+'))
# 5b
print(sp.simplify(sp.diff(sp.sin(x**2)/2,x)-x*sp.cos(x**2)))
# 6b
A=sp.integrate(4-1/x,(x,sp.Rational(1,4),1))+sp.integrate(4-x,(x,1,4))
print(A,sp.N(A), sp.N(sp.Rational(15,2)-sp.log(4)))

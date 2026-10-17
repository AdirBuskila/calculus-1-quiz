import sympy as sp
x,t,L,a,b,c,h=sp.symbols('x t L a b c h',real=True)
r=[]
# Q1
f=sp.exp(2*x)/x
fp=sp.diff(f,x); r.append(("Q1 f'",sp.simplify(fp-sp.exp(2*x)*(2*x-1)/x**2)==0))
fpp=sp.diff(f,x,2); r.append(("Q1 f''",sp.simplify(fpp-2*sp.exp(2*x)*(2*x**2-2*x+1)/x**3)==0))
r.append(("Q1 f(1/2)=2e",sp.simplify(f.subs(x,sp.Rational(1,2))-2*sp.E)==0))
r.append(("Q1 x->0-",sp.limit(f,x,0,'-')==-sp.oo)); r.append(("Q1 x->0+",sp.limit(f,x,0,'+')==sp.oo))
r.append(("Q1 slope -oo",sp.limit(f/x,x,-sp.oo)==0 and sp.limit(f,x,-sp.oo)==0))
r.append(("Q1 +oo",sp.limit(f/x,x,sp.oo)==sp.oo))
r.append(("Q1 f'' sign",sp.solve(2*x**2-2*x+1,x)==[] ))
# Q2a
an=[sp.Rational(3,2)]
for i in range(12): an.append(3-2/an[-1])
r.append(("Q2a incr<2",all(an[i]<an[i+1]<2 for i in range(12))))
r.append(("Q2a diff id",sp.simplify((3-2/x-x)-(2-x)*(x-1)/x)==0))
r.append(("Q2a fixed",set(sp.solve(sp.Eq(L,3-2/L),L))=={1,2}))
r.append(("Q2a L=2",abs(float(an[-1])-2)<1e-3))
# Q2b
x1,x2=sp.symbols('x1 x2')
sol=sp.solve([sp.Eq(-1/x1**2,2*x2),sp.Eq(2/x1,-x2**2)],[x1,x2],dict=True)
sol=[s for s in sol if s[x1].is_real and s[x2].is_real]
r.append(("Q2b x1,x2",sol==[{x1:-sp.Rational(1,2),x2:-2}]))
line=-4*x-4
r.append(("Q2b tangent f",sp.simplify(sp.diff(1/x,x).subs(x,-sp.Rational(1,2))+4)==0 and (1/x).subs(x,-sp.Rational(1,2))==line.subs(x,-sp.Rational(1,2))))
r.append(("Q2b tangent g",sp.diff(x**2,x).subs(x,-2)==-4 and (x**2).subs(x,-2)==line.subs(x,-2)))
# Q3a
A=sp.limit((sp.sin(x)/x)**(1/x**2),x,0)
r.append(("Q3a",sp.simplify(A-sp.exp(-sp.Rational(1,6)))==0))
# Q3b
F=3*sp.log(x)-sp.log(x**2+2*x+5)/2-sp.Rational(5,2)*sp.atan((x+1)/2)
r.append(("Q3b",sp.simplify(sp.diff(F,x)-(2*x**2+15)/(x*(x**2+2*x+5)))==0))
r.append(("Q3b coeffs",sp.simplify(3*(x**2+2*x+5)+x*(-x-6)-(2*x**2+15))==0))
F2=sp.log(x**2+2*x+5)/2+sp.Rational(5,2)*sp.atan((x+1)/2)
r.append(("Q3b inner",sp.simplify(sp.diff(F2,x)-(x+6)/(x**2+2*x+5))==0))
# Q4a
a,b=sp.symbols('a b',real=True)
r.append(("Q4a",sp.limit(x*(sp.sqrt(x**2+x+6)-sp.sqrt(x**2+x)),x,sp.oo)==3))
r.append(("Q4a b=-1",sp.limit(x*(sp.sqrt(x**2+x+6)-sp.sqrt(x**2+x)),x,sp.oo)==3 and sp.limit(x*(sp.sqrt(x**2+x+6)-sp.sqrt(x**2+x)),x,sp.oo)!=sp.oo))
# Q4b
r.append(("Q4b",sp.simplify(sp.diff(sp.log(1+sp.sin(x)**2)/2,x)-sp.sin(x)*sp.cos(x)/(1+sp.sin(x)**2))==0))
# Q5a
g=sp.cbrt((x-1)**2)*sp.sin(x-1)
r.append(("Q5a f'(1)",sp.limit(g.subs(x,1+h)/h,h,0)==0))
# Q5b
y=sp.Rational(2,5)*x**sp.Rational(5,4)-sp.Rational(2,3)*x**sp.Rational(3,4)
yp=sp.diff(y,x)
r.append(("Q5b y'",sp.simplify(yp-(x**sp.Rational(1,4)-x**sp.Rational(-1,4))/2)==0))
r.append(("Q5b 1+y'^2",sp.simplify(1+yp**2-((x**sp.Rational(1,4)+x**sp.Rational(-1,4))/2)**2)==0))
Lh=sp.integrate((x**sp.Rational(1,4)+x**sp.Rational(-1,4))/2,(x,0,1))
r.append(("Q5b L",Lh==sp.Rational(16,15)))
# Q6a
G=(x**2+a)/(x-b)
dG=sp.diff(G,x)
r.append(("Q6a g'",sp.simplify(dG-(x**2-2*b*x-a)/(x-b)**2)==0))
r.append(("Q6a",sp.simplify(dG.subs({x:2,a:-24,b:7}))==0 and sp.limit(G.subs({a:-24,b:7})-x,x,sp.oo)==7))
# Q6b
S=sp.integrate(sp.log(x+1)/sp.sqrt(x+1),(x,0,1))
r.append(("Q6b",sp.simplify(S-(2*sp.sqrt(2)*sp.log(2)-4*sp.sqrt(2)+4))==0))
for k,v in r: print(k,"OK" if v else "MISMATCH")
print("ALL OK" if all(v for _,v in r) else "FAIL")

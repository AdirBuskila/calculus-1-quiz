import sympy as sp
x,n,L,a,b,y=sp.symbols('x n L a b y',real=True)
r=[]
f=x**3/(x**2-1)
fp=sp.simplify(sp.diff(f,x)); r.append(("Q1 f' ok", sp.simplify(fp-x**2*(x**2-3)/(x**2-1)**2)==0))
fpp=sp.diff(f,x,2); r.append(("Q1 f'' ok", sp.simplify(fpp-2*x*(x**2+3)/(x**2-1)**3)==0))
r.append(("Q1 f(sqrt3)", sp.simplify(f.subs(x,sp.sqrt(3))-sp.sqrt(27)/2)==0))
r.append(("Q1 f(-sqrt3)", sp.simplify(f.subs(x,-sp.sqrt(3))+sp.sqrt(27)/2)==0))
r.append(("Q1 a", sp.limit(f/x,x,sp.oo)==1)); r.append(("Q1 b", sp.limit(f-x,x,sp.oo)==0))
r.append(("Q1 lim -1-", sp.limit(f,x,-1,'-')==-sp.oo)); r.append(("Q1 lim -1+", sp.limit(f,x,-1,'+')==sp.oo))
r.append(("Q1 lim 1-", sp.limit(f,x,1,'-')==-sp.oo)); r.append(("Q1 lim 1+", sp.limit(f,x,1,'+')==sp.oo))
g=(x**2+8)/(x**4+4*x**2)
F=-2/x-sp.atan(x/2)/2
r.append(("Q2a", sp.simplify(sp.diff(F,x)-g)==0))
an=sp.Integer(2); 
for i in range(60): an=sp.Rational(3)/(2+1/an) if i<8 else an
seq=[sp.Integer(2)]
for i in range(8): seq.append(3/(2+1/seq[-1]))
r.append(("Q2b a2=6/5 decreasing >=1", seq[1]==sp.Rational(6,5) and all(seq[i+1]<=seq[i] and seq[i]>=1 for i in range(8))))
r.append(("Q2b fixed pts", set(sp.solve(sp.Eq(L,3/(2+1/L)),L))=={1}))
r.append(("Q3a", sp.limit(sp.sqrt(1+n+n**2)-sp.sqrt(1-2*n+n**2),n,sp.oo)==sp.Rational(3,2)))
V=2*sp.pi*sp.integrate(x*(sp.E-sp.exp(x)),(x,0,1)); r.append(("Q3b", sp.simplify(V-2*sp.pi*(sp.E/2-1))==0))
h=sp.log(x)**2-2*sp.log(x)
r.append(("Q4a crit", sp.solve(sp.diff(h,x),x)==[sp.E]))
vals=[sp.simplify(h.subs(x,v)) for v in (sp.sqrt(sp.E),sp.E,sp.E**2)]
r.append(("Q4a vals", vals==[sp.Rational(-3,4),-1,0]))
r.append(("Q4b", sp.limit(3*x**4/(x**3+2*x+9)-3*x,x,sp.oo)==0 and sp.limit(3*x**4/(x**3+2*x+9)-2*x,x,sp.oo)==sp.oo and sp.limit(3*x**4/(x**3+2*x+9)-3*x-1,x,sp.oo)==-1))
r.append(("Q5a left -2", sp.limit(sp.exp(-x*(-(x+2))/(x+2)**2),x,-2,'-')==sp.oo))
r.append(("Q5a 0", (sp.limit(sp.atan(1/x),x,0,'+')==sp.pi/2) and (3!=sp.pi/2)))
r.append(("Q5b", sp.simplify(sp.diff(sp.sin(x**2)/2,x)-x*sp.cos(x**2))==0))
r.append(("Q6b area", sp.simplify(sp.integrate(4-1/x,(x,sp.Rational(1,4),1))+sp.integrate(4-x,(x,1,4))-(sp.Rational(15,2)-sp.log(4)))==0))
r.append(("Q6b S1,S2", sp.integrate(4-x,(x,1,4))==sp.Rational(9,2) and sp.simplify(3-sp.integrate(1/y,(y,1,4))-(3-sp.log(4)))==0))
r.append(("Q6a min", sp.diff(sp.exp(x)-x-1,x).subs(x,0)==0))
for k,v in r: print(k,"OK" if v else "MISMATCH")
print("ALL OK" if all(v for _,v in r) else "FAIL")

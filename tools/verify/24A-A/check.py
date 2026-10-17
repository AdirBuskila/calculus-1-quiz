# sympy check of every official answer in 24A-A. Run: PYTHONUTF8=1 py tools/verify/24A-A/check.py
import sympy as sp
x,t,n,L,a,b=sp.symbols('x t n L a b',real=True)
r=[]
def ok(name,cond): r.append((name,bool(cond)))
f=sp.exp(x)/x**2
fp=sp.diff(f,x); ok("Q1 f'",sp.simplify(fp-sp.exp(x)*(x-2)/x**3)==0)
fpp=sp.simplify(sp.diff(f,x,2)); ok("Q1 f''",sp.simplify(fpp-sp.exp(x)*(x**2-4*x+6)/x**4)==0)
ok("Q1 asym",sp.limit(f,x,0,'-')==sp.oo and sp.limit(f,x,0,'+')==sp.oo and sp.limit(f,x,sp.oo)==sp.oo and sp.limit(f,x,-sp.oo)==0)
# OFFICIAL ERROR: x^2-4x+6 has discriminant -8 < 0, so f''>0 for every x != 0 (official says f''<0 for x<0)
ok("Q1 f''>0 everywhere (official claims f''<0 for x<0: DISAGREES)", sp.Poly(x**2-4*x+6,x).discriminant()<0)
g=x**2/((x+2)*(x**2+1))
G=sp.Rational(1,5)*(4*sp.log(x+2)+sp.log(x**2+1)/2-2*sp.atan(x))
ok("Q2a",sp.simplify(sp.diff(G,x)-g)==0)
ok("Q2a coeffs",sp.simplify(sp.apart(g,x)-(sp.Rational(4,5)/(x+2)+(sp.Rational(1,5)*x-sp.Rational(2,5))/(x**2+1)))==0)
seq=[sp.Integer(1)]
for i in range(30): seq.append(6/(5-seq[-1]))
ok("Q2b 1<=a_n<2 and increasing",all(1<=seq[i]<2 and seq[i+1]>seq[i] for i in range(30)))
ok("Q2b fixed pts 2,3",set(sp.solve(sp.Eq(L,6/(5-L)),L))=={2,3})
ok("Q2b (*) a^2-5a+6>=0 for a<=2",sp.factor(a**2-5*a+6)==(a-2)*(a-3))
ok("Q3a",sp.limit((1-sp.tan(x))**(1/sp.sin(2*x)),x,0)==sp.exp(-sp.Rational(1,2)))
S=-sp.atan(sp.cos(2*x)/sp.sqrt(3))/(2*sp.sqrt(3))
ok("Q3b",sp.simplify(sp.diff(S,x)-sp.sin(2*x)/(3+sp.cos(2*x)**2))==0)
y=x**sp.Rational(2,3)*sp.exp(-x)
yp=sp.simplify(sp.diff(y,x)); ok("Q4a y' (x>0 branch)",sp.simplify(yp.subs(x,sp.Rational(2,3))) == 0)
cb=lambda v: sp.re(sp.N((sp.sign(v)*abs(v)**sp.Rational(1,3))**2*sp.exp(-v)))  # real cube-root branch of x^(2/3)
vals={v:cb(v) for v in (-3,0,sp.Rational(2,3),1)}
ok("Q4a table",abs(vals[-3]-41.8)<0.05 and vals[0]==0 and abs(vals[sp.Rational(2,3)]-0.39)<0.005 and abs(vals[1]-0.37)<0.005)
ok("Q4a max/min",max(vals.values())==vals[-3] and min(vals.values())==0)
V=sp.pi*sp.integrate(sp.atan(x),(x,0,1)); ok("Q4b",sp.simplify(V-(sp.pi**2/4-sp.pi*sp.log(2)/2))==0)
ok("Q5a (after Lopital)",sp.limit(sp.sin(x)/(2*sp.sqrt(x))/(sp.Rational(3,2)*sp.sqrt(x)),x,0,'+')==sp.Rational(1,3))
# numeric check of the integral limit
import mpmath as mp
ok("Q5a numeric",abs(mp.quad(lambda s: mp.sin(s**2),[0,mp.sqrt(1e-8)])/mp.mpf(1e-8)**1.5-1/3)<1e-4)
ok("Q5b left",sp.limit(((sp.exp(a*x)-1)/x)**2,x,0,'-')==a**2)
ok("Q5b right a!=0",sp.limit(4+sp.exp(-4/x),x,0,'+')==4 and sp.limit(5+0*x,x,0)==5)
ok("Q5b answer",set(sp.solve(sp.Eq(a**2,4),a))=={-2,2})
ok("Q6a tan x>x on (0,pi/2)",all(sp.tan(v)>v for v in [sp.Rational(k,10) for k in range(1,15)]))
h=sp.sqrt(2*x-5); ok("Q6b tangent",h.subs(x,3)==1 and sp.diff(h,x).subs(x,3)==1)
A=sp.integrate(x-2,(x,2,sp.Rational(5,2)))+sp.integrate(x-2-sp.sqrt(2*x-5),(x,sp.Rational(5,2),3)); ok("Q6b area",A==sp.Rational(1,6))
for k,v in r: print(k,"OK" if v else "MISMATCH")
print("ALL OK" if all(v for _,v in r) else "FAIL (see MISMATCH lines)")

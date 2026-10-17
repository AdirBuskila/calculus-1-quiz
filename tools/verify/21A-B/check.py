import sympy as sp
x,a,b,y,h=sp.symbols('x a b y h',real=True)
r=[]
f=x**4/(x**3-1)
fp=sp.diff(f,x); r.append(("Q1 f'",sp.simplify(fp-x**3*(x**3-4)/(x**3-1)**2)==0))
fpp=sp.diff(f,x,2); r.append(("Q1 f''",sp.simplify(fpp-6*x**2*(x**3+2)/(x**3-1)**3)==0))
c4=sp.cbrt(4); c2=sp.cbrt(2)
r.append(("Q1 f(cbrt4)",sp.simplify(f.subs(x,c4)-4*c4/3)==0))
r.append(("Q1 f(-cbrt2)",sp.simplify(f.subs(x,-c2)+2*c2/3)==0))
r.append(("Q1 asym",sp.limit(f/x,x,sp.oo)==1 and sp.limit(f-x,x,sp.oo)==0 and sp.limit(f,x,1,'+')==sp.oo and sp.limit(f,x,1,'-')==-sp.oo))
r.append(("Q1 f' num",sp.simplify(4*x**3*(x**3-1)-x**4*3*x**2-(x**6-4*x**3))==0))
# Q2a
r.append(("Q2a",sp.limit(x**3/(x**2-x+2)-x-1,x,sp.oo)==0))
r.append(("Q2a uniq",sp.solve([sp.expand((a+1)*x**3+(b-a)*x**2+(2*a-b)*x+2*b).coeff(x,3),sp.expand((b-a)).__class__(b-a)],[a,b])=={a:-1,b:-1}))
# Q2b
g=x*sp.Abs(x-3)/((x**2-4*x+3)*sp.asin(x/5))
r.append(("Q2b x=3",sp.limit(g,x,3,'+')==3/(2*sp.asin(sp.Rational(3,5))) and sp.limit(g,x,3,'-')==-3/(2*sp.asin(sp.Rational(3,5)))))
r.append(("Q2b x=1",sp.limit(g,x,1,'+')==-sp.oo and sp.limit(g,x,1,'-')==sp.oo))
r.append(("Q2b x=0",sp.limit(g,x,0,'+')==5 and sp.limit(g,x,0,'-')==5))
# Q3a
r.append(("Q3a",sp.limit((sp.sqrt(1+sp.sin(x/2))-sp.sqrt(1-sp.sin(x/2)))/x,x,0)==sp.Rational(1,2)))
# Q3b
F=(x**2/2+x+sp.Rational(1,2))*sp.atan(x)-x/2-sp.log(x**2+1)/2
r.append(("Q3b",sp.simplify(sp.diff(F,x)-(x+1)*sp.atan(x))==0))
# Q4a
a0,a1,a2,p,q,cc=sp.symbols('a0 a1 a2 p q cc',real=True)
P=lambda v:a0+a1*v+a2*v**2
r.append(("Q4a midpoint",sp.simplify((P(q)-P(p))/(q-p)-sp.diff(P(x),x).subs(x,(p+q)/2))==0))
# Q4b handwritten: correct volume about x=4
V_shell=2*sp.pi*sp.integrate((4-x)*(2*x+8-x**2),(x,0,4))
yy=sp.symbols('yy',positive=True)
V_wash=sp.pi*sp.integrate(16-(4-sp.sqrt(yy))**2,(yy,0,8))+sp.pi*sp.integrate((8-yy/2)**2-(4-sp.sqrt(yy))**2,(yy,8,16))
r.append(("Q4b shells=128pi",sp.simplify(V_shell-128*sp.pi)==0))
r.append(("Q4b washers=128pi",sp.simplify(V_wash-128*sp.pi)==0))
hand=sp.pi*(1184-sp.Rational(224,3)*sp.sqrt(2))
r.append(("Q4b handwritten final answer is WRONG (differs from 128pi)",sp.simplify(hand-128*sp.pi)!=0))
r.append(("Q4b integrand 1",sp.simplify(16-(4-sp.sqrt(yy))**2-(8*sp.sqrt(yy)-yy))==0))
r.append(("Q4b integrand 2",sp.simplify((8-yy/2)**2-(4-sp.sqrt(yy))**2-(48-9*yy+yy**2/4+8*sp.sqrt(yy)))==0))
r.append(("Q4b parts",sp.simplify(sp.integrate(8*sp.sqrt(yy)-yy,(yy,0,8))-(sp.Rational(256,3)*sp.sqrt(2)-32))==0 ))
print("part1",sp.simplify(sp.integrate(8*sp.sqrt(yy)-yy,(yy,0,8))),"part2",sp.simplify(sp.integrate(48-9*yy+yy**2/4+8*sp.sqrt(yy),(yy,8,16))))
# Q5a
ff=x**6-2*x**2+x
r.append(("Q5a",ff.subs(x,0)==0 and ff.subs(x,1)==0 and sp.diff(ff,x)==6*x**5-4*x+1))
r.append(("Q5b",sp.limit(2*(1-sp.cos(x))/x**4-1/x**2,x,0)==-sp.Rational(1,12)))
# Q6a
k=sp.cbrt(x**2-2*x)
r.append(("Q6a f'",sp.simplify(sp.diff(k,x)-(2*x-2)/(3*(x**2-2*x)**sp.Rational(2,3)))==0))
vals={v:sp.simplify(sp.real_root(v**2-2*v,3)) for v in (0,1,2,-1,3)}
r.append(("Q6a values",vals[0]==0 and vals[1]==-1 and vals[2]==0 and vals[-1]==sp.cbrt(3) and vals[3]==sp.cbrt(3)))
# numeric f' check at 1 and 3
r.append(("Q6a f'(2),f'(0) infinite",abs(sp.limit(sp.diff(sp.Pow(x**2-2*x,sp.Rational(1,3)),x),x,0,'+'))==sp.oo))
# Q6b
S=sp.integrate(4*x**2-x**2/9,(x,0,1/sp.sqrt(2)))+sp.integrate(2-x**2/9,(x,1/sp.sqrt(2),sp.sqrt(18)))
r.append(("Q6b",sp.simplify(S-10*sp.sqrt(2)/3)==0))
for kk,v in r: print(kk,"OK" if v else "MISMATCH")
print("ALL OK" if all(v for _,v in r) else "FAIL")

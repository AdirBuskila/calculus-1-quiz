import sympy as sp
x,t,y=sp.symbols('x t y',real=True)
r=[]
f=((x+2)/(x+1))**2
fp=sp.diff(f,x); r.append(("Q1 f'",sp.simplify(fp+2*(x+2)/(x+1)**3)==0))
fpp=sp.diff(f,x,2); r.append(("Q1 f''",sp.simplify(fpp-(4*x+10)/(x+1)**4)==0))
r.append(("Q1 inflection",sp.simplify(f.subs(x,-sp.Rational(5,2)))==sp.Rational(1,9)))
r.append(("Q1 min",f.subs(x,-2)==0 and sp.solve(fp,x)==[-2]))
r.append(("Q1 asym",sp.limit(f/x,x,sp.oo)==0 and sp.limit(f,x,sp.oo)==1 and sp.limit(f,x,-sp.oo)==1))
r.append(("Q1 x=-1",sp.limit(f,x,-1,'-')==sp.oo and sp.limit(f,x,-1,'+')==sp.oo))
r.append(("Q1 f'' num",sp.simplify((-2*(x+1)**3+2*(x+2)*3*(x+1)**2)/(x+1)**6-(4*x+10)/(x+1)**4)==0))
# Q3a: sign change
g=lambda v: 2*sp.sin(3*v)**2+5*sp.cbrt(1-v**2)-4*v**5
r.append(("Q3a f(0)=5",g(0)==5))
r.append(("Q3a f(1)<0 (value -3.96; official prints -3.99)",float(g(1))<0 and abs(float(g(1))+3.96)<0.005))
r.append(("Q3a f(-1)>0 (so root NOT in (-1,0))",float(g(-1))>0))
r.append(("Q3a sign change on (0,1)",float(g(0))*float(g(1))<0))
# Q3b
F=sp.log(sp.Abs((sp.log(x)-3)/(sp.log(x)-1)))/2
xv=sp.Float(5.0)
d=sp.diff(sp.log((sp.log(x)-3)/(sp.log(x)-1))/2,x)
r.append(("Q3b",sp.simplify(d-1/(x*(sp.log(x)-1)*(sp.log(x)-3)))==0))
r.append(("Q3b pf",sp.simplify(1/((t-1)*(t-3))-(sp.Rational(1,2)/(t-3)-sp.Rational(1,2)/(t-1)))==0))
# Q4a
r.append(("Q4a",sp.limit(sp.log(sp.cos(x))/sp.log(sp.cos(4*x)),x,0)==sp.Rational(1,16)))
# Q4b
V=2*sp.pi*sp.integrate((4-x)*x**2,(x,0,2))+2*sp.pi*sp.integrate((4-x)*(-2*x+8),(x,2,4))
r.append(("Q4b",V==24*sp.pi))
r.append(("Q4b parts",2*sp.pi*sp.integrate((4-x)*x**2,(x,0,2))==40*sp.pi/3 and 2*sp.pi*sp.integrate((4-x)*(-2*x+8),(x,2,4))==32*sp.pi/3))
r.append(("Q4b intersect",sp.solve(x**2+2*x-8,x)==[-4,2]))
# Q5a
h=sp.log(1+x**2)
r.append(("Q5a",h.subs(x,0)==0 and sp.simplify(h.subs(x,-1))==sp.log(2) and sp.simplify(h.subs(x,sp.sqrt(sp.E-1)))==1 and float(sp.log(2))<1))
# Q5b
a,b,c,dx=sp.symbols('a b c dx',real=True)
r.append(("Q5b right deriv",sp.limit((dx**2+b*sp.sin(2*dx))/dx,dx,0,'+')==2*b))
r.append(("Q5b left deriv",sp.limit((a*sp.exp(dx)-a)/dx,dx,0,'-')==a))
# Q6a
Fy=2*x**4+3*x**2*y**3-2*sp.sin(y)-2
r.append(("Q6a on curve",Fy.subs({x:1,y:0})==0))
dydx=-sp.diff(Fy,x)/sp.diff(Fy,y)
r.append(("Q6a slope",dydx.subs({x:1,y:0})==4))
r.append(("Q6a correct implicit 8x^3 (printed 8x^4 is a slip)",sp.diff(Fy,x)==8*x**3+6*x*y**3))
# Q6b
S1=sp.integrate((sp.Rational(3,10)*x+sp.Rational(3,2))-(-sp.Rational(1,5)*x-2),(x,0,5))
S2=2*sp.integrate(sp.sqrt(3*x-6),(x,2,5))
r.append(("Q6b S1,S2,S",S1==sp.Rational(95,4) and S2==12 and S1-S2==sp.Rational(47,4)))
r.append(("Q6b roots",sp.solve(9*x**2-210*x+825,x)==[5,sp.Rational(55,3)] and sp.solve(x**2-55*x+250,x)==[5,50]))
r.append(("Q6b line1 meets parabola at 5",sp.Rational(3,10)*5+sp.Rational(3,2)==3==sp.sqrt(3*5-6)))
for k,v in r: print(k,"OK" if v else "MISMATCH")
print("ALL OK" if all(v for _,v in r) else "FAIL")

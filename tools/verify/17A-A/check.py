import sympy as sp
x = sp.symbols('x', real=True)
xp = sp.symbols('xp', positive=True)
t = sp.symbols('t', real=True)
a = sp.symbols('a', positive=True)
r = []
y = (4 * x**2 - 2 * x - 1) / (x - 1)
r.append(("Q1 y'", sp.simplify(sp.diff(y, x) - (4 * x**2 - 8 * x + 3) / (x - 1)**2) == 0))
r.append(("Q1 crit", sorted(sp.solve(sp.Eq(4 * x**2 - 8 * x + 3, 0), x)) == [sp.Rational(1, 2), sp.Rational(3, 2)]))
r.append(("Q1 y(.5)=2,y(1.5)=10", y.subs(x, sp.Rational(1, 2)) == 2 and y.subs(x, sp.Rational(3, 2)) == 10))
r.append(("Q1 y''", sp.simplify(sp.diff(y, x, 2) - 2 / (x - 1)**3) == 0))
r.append(("Q1 slant a=4,b=2", sp.limit(y / x, x, sp.oo) == 4 and sp.limit(y - 4 * x, x, sp.oo) == 2 and sp.limit(y - 4 * x, x, -sp.oo) == 2))
r.append(("Q1 vertical", sp.limit(y, x, 1, '+') == sp.oo and sp.limit(y, x, 1, '-') == -sp.oo))
r.append(("Q1 intercepts", y.subs(x, 0) == 1 and sorted(sp.solve(sp.Eq(y, 0), x)) == sorted([(1 - sp.sqrt(5)) / 4, (1 + sp.sqrt(5)) / 4])))
# Q2a
L = sp.symbols('L')
r.append(("Q2a L=4.5", sp.solve(sp.Eq(L, L / 3 + 3), L) == [sp.Rational(9, 2)]))
r.append(("Q2a a2=10/3", sp.Integer(1) / 3 + 3 == sp.Rational(10, 3)))
seq = [sp.Integer(1)]
for _ in range(60):
    seq.append(seq[-1] / 3 + 3)
r.append(("Q2a bounded by 4.5 and increasing", all(s <= sp.Rational(9, 2) for s in seq) and all(seq[i + 1] >= seq[i] for i in range(60))))
# Q2b
F = t - 4 / sp.sqrt(5) * sp.atan(t / sp.sqrt(5))
xs = sp.symbols('xs', real=True)
Fx = sp.tan(xs) - 4 / sp.sqrt(5) * sp.atan(sp.tan(xs) / sp.sqrt(5))
r.append(("Q2b", sp.simplify(sp.diff(Fx, xs) - 1 / (sp.cos(xs)**2 + 4 * sp.cos(xs)**4)) == 0))
r.append(("Q2b integrand in t", sp.simplify(1 / (1 + t**2) / (1 / (1 + t**2) + 4 / (1 + t**2)**2) - (1 + t**2) / (5 + t**2)) == 0
          and sp.simplify((1 + t**2) / (5 + t**2) - (1 - 4 / (5 + t**2))) == 0))
# Q3a
r.append(("Q3a", sp.limit(sp.cos(xs)**(1 / (xs * sp.sin(xs))), xs, 0) == sp.exp(-sp.Rational(1, 2))))
# Q3b
yy = sp.cos(sp.pi * sp.exp(xs) / 6)
r.append(("Q3b y'(0)=-pi/12", sp.simplify(sp.diff(yy, xs).subs(xs, 0) + sp.pi / 12) == 0 and sp.simplify(yy.subs(xs, 0) - sp.sqrt(3) / 2) == 0))
approx = sp.sqrt(3) / 2 - sp.pi / 12 * sp.Rational(1, 10)
r.append(("Q3b approx 0.8398", abs(float(approx) - 0.8398) < 5e-5))
r.append(("Q3b exact value within 0.005 of the linear approximation", abs(float(yy.subs(xs, sp.Rational(1, 10))) - float(approx)) < 5e-3))  # exact is 0.8377; the linear approximation is only first order
# Q4a
f4 = (sp.sqrt(2 * xp - a) - sp.sqrt(xp)) / (xp**2 - a**2)
r.append(("Q4a limit", sp.simplify(sp.limit(f4.subs(a, 3), xp, 3) - 1 / (4 * 3 * sp.sqrt(3))) == 0))
r.append(("Q4a a=1/2", sp.solve(sp.Eq(1 / (4 * a * sp.sqrt(a)), sp.sqrt(a)), a) == [sp.Rational(1, 2)]))
# Q4b
Q = sp.integrate(sp.exp(xs) * sp.sin(sp.pi * xs), (xs, 0, 1))
r.append(("Q4b", sp.simplify(Q - sp.pi * (sp.E + 1) / (1 + sp.pi**2)) == 0))
# Q5a
fy = xp * sp.real_root((3 * xp - 12)**2, 3)
r.append(("Q5a crit 2.4", sp.solve(sp.Eq(5 * xp - 12, 0), xp) == [sp.Rational(12, 5)]))
d = sp.diff(xp * ((3 * xp - 12)**2)**sp.Rational(1, 3), xp)
r.append(("Q5a y' numeric at 5 and 1", abs(float(d.subs(xp, 5)) - float((5 * 5 - 12) / (3 * 5 - 12)**(1 / 3))) < 1e-9
          and abs(float(d.subs(xp, 3)) - float((5 * 3 - 12) / (-(3.0)**(1 / 3)))) < 1e-9))
import numpy as np
xs_ = np.linspace(0, 6, 600001)
yv = xs_ * np.cbrt((3 * xs_ - 12)**2)
r.append(("Q5a abs max at 6 = 6*cbrt36", abs(yv.max() - 6 * 36**(1 / 3)) < 1e-9 and abs(6 * 36**(1 / 3) - 19.81) < 5e-3))
r.append(("Q5a min 0 at 0 and 4", yv[0] == 0 and abs(yv[400000]) < 1e-9 and yv.min() >= 0))
v24 = 2.4 * np.cbrt((3 * 2.4 - 12)**2)
r.append(("Q5a y(2.4) approx 6.83 (official prints 6.829; exact %.4f)" % v24, abs(v24 - 6.829) < 5e-3))
# Q5b
G = xp + sp.log(xp) - sp.Rational(7, 2) * sp.atan((xp + 1) / 2)
r.append(("Q5b", sp.simplify(sp.diff(G, xp) - (xp**3 + 3 * xp**2 + 5) / (xp * (xp**2 + 2 * xp + 5))) == 0))
r.append(("Q5b polynomial division", sp.simplify((xp**3 + 3 * xp**2 + 5) / (xp * (xp**2 + 2 * xp + 5)) - 1 - (xp**2 - 5 * xp + 5) / (xp * (xp**2 + 2 * xp + 5))) == 0))
r.append(("Q5b ABC", sp.simplify(1 / xp + (-7) / (xp**2 + 2 * xp + 5) - (xp**2 - 5 * xp + 5) / (xp * (xp**2 + 2 * xp + 5))) == 0))
# Q6a
P2 = lambda v: 1 + sp.Rational(1, 2) * (v - 1) - sp.Rational(1, 8) * (v - 1)**2
v = sp.Rational(105, 100)
r.append(("Q6a P2(1.05)=1.0246875 (official prints 1.02466875)", P2(v) == sp.Rational(10246875, 10000000)))
r.append(("Q6a bound", sp.Rational(5, 100)**3 / 16 == sp.Rational(1, 128000) and float(sp.Rational(5, 100)**3 / 16) < 1e-5 and abs(float(sp.Rational(5, 100)**3 / 16) - 7.81e-6) < 1e-8))
r.append(("Q6a derivs", sp.diff(sp.sqrt(xp), xp, 3).subs(xp, 1) == sp.Rational(3, 8) and sp.diff(sp.sqrt(xp), xp, 2).subs(xp, 1) == -sp.Rational(1, 4)))
true = float(sp.sqrt(v))
r.append(("Q6a true sqrt(1.05) within 1.0246875 +- 1e-5", abs(true - 1.0246875) < 1e-5))
r.append(("Q6a printed 1.02467 +- 1e-5 would miss the true value", abs(true - 1.02467) > 1e-5))
r.append(("Q6a corrected 1.02469 +- 1e-5 covers the true value", abs(true - 1.02469) < 1e-5))
# Q6b
r.append(("Q6b", sp.integrate(sp.sqrt(32 * xp) - xp**3, (xp, 0, 2)) == sp.Rational(20, 3) and abs(20 / 3 - 6.67) < 5e-3))
r.append(("Q6b intersections", sorted(sp.solve(sp.Eq(xp**3, sp.sqrt(32 * xp)), xp)) == [2] ))
for k, v_ in r:
    print(("OK   " if v_ else "FAIL ") + k)

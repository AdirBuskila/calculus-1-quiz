import sympy as sp
x = sp.symbols('x', positive=True)
t = sp.symbols('t', real=True)
a = sp.symbols('a', real=True)
n = sp.symbols('n', positive=True, integer=True)
r = []
f = x**2 * sp.log(x)
r.append(("Q1 y'", sp.simplify(sp.diff(f, x) - x * (2 * sp.log(x) + 1)) == 0))
r.append(("Q1 crit x=1/sqrt(e)", sp.solve(sp.Eq(sp.diff(f, x), 0), x) == [1 / sp.sqrt(sp.E)]))
r.append(("Q1 y(1/sqrt e)=-1/(2e)", sp.simplify(f.subs(x, 1 / sp.sqrt(sp.E)) + 1 / (2 * sp.E)) == 0))
r.append(("Q1 y''", sp.simplify(sp.diff(f, x, 2) - (2 * sp.log(x) + 3)) == 0))
xi = sp.exp(-sp.Rational(3, 2))
r.append(("Q1 inflection x=1/sqrt(e^3)", sp.solve(sp.Eq(2 * sp.log(x) + 3, 0), x) == [xi] and sp.simplify(xi - 1 / sp.sqrt(sp.E**3)) == 0))
r.append(("Q1 y(infl)=-3/(2e^3)", sp.simplify(f.subs(x, xi) + 3 / (2 * sp.E**3)) == 0))
r.append(("Q1 lim 0+ = 0", sp.limit(f, x, 0, '+') == 0))
r.append(("Q1 lim f/x = oo", sp.limit(f / x, x, sp.oo) == sp.oo))
# Q2a numeric sandwich
r.append(("Q2a limit", sp.limit((n**2 + 2**n)**(1 / n), n, sp.oo) == 2))
r.append(("Q2a bound n^2<=2^n for n>=4", all(k**2 <= 2**k for k in range(4, 200))))
# Q2b
F = (x**3 / 3 - 2 * x**2) * sp.log(x) - x**3 / 9 + x**2
r.append(("Q2b", sp.simplify(sp.diff(F, x) - (x**2 - 4 * x) * sp.log(x)) == 0))
# Q3a
xx = sp.symbols('xx')
r.append(("Q3a", sp.limit(((1 + sp.tan(xx)) / (1 + sp.sin(xx)))**(1 / sp.sin(xx)), xx, 0) == 1))
r.append(("Q3a fixed middle line", sp.limit((sp.tan(xx) - sp.sin(xx)) / (1 + sp.sin(xx)) / sp.sin(xx), xx, 0) == 0
          and sp.simplify((sp.tan(xx) - sp.sin(xx)) / sp.sin(xx) - (1 / sp.cos(xx) - 1)) == 0))
# Q3b
r.append(("Q3b", sp.integrate(4 - 1 / x**2, (x, sp.Rational(1, 2), 1)) + sp.integrate(4 - x, (x, 1, 4)) == sp.Rational(11, 2)))
r.append(("Q3b intersections", sp.solve(sp.Eq(1 / x**2, 4), x) == [sp.Rational(1, 2)] and sp.solve(sp.Eq(1 / x**2, x), x) == [1] and sp.solve(sp.Eq(x, 4), x) == [4]))
# Q4a
g = xx + sp.sin(xx) - 1
r.append(("Q4a signs", g.subs(xx, 0) == -1 and g.subs(xx, 3).evalf() > 0))
r.append(("Q4a g'", sp.diff(g, xx) == 1 + sp.cos(xx)))
# Q4b
r.append(("Q4b", sp.integrate(sp.pi * ((25 - x**2) - 9), (x, -4, 4)) == sp.Rational(256, 3) * sp.pi))
r.append(("Q4b intersect +-4", sorted(sp.solve(sp.Eq(sp.sqrt(25 - x**2), 3), x)) == [4]))
# Q5a
xr = sp.symbols('xr', real=True)
h = sp.real_root(xr**2 + xr, 3)**2
vals = {k: sp.N(sp.real_root(k**2 + k, 3)**2) for k in [-2, -1, -0.5, 0, 3]}
r.append(("Q5a values", abs(vals[-2] - 4**(1 / 3)) < 1e-9 and abs(vals[3] - 144**(1 / 3)) < 1e-9 and vals[0] == 0 and vals[-1] == 0
          and abs(vals[-0.5] - (1 / 16)**(1 / 3)) < 1e-9))
r.append(("Q5a f(-2) is cbrt(4), not cbrt(36)", abs(vals[-2] - 36**(1 / 3)) > 1))
fp = sp.diff((x**2 + x)**sp.Rational(2, 3), x)
r.append(("Q5a crit -1/2", sp.solve(sp.Eq(2 * x + 1, 0), x) == [] and sp.Rational(-1, 2) == sp.solve(sp.Eq(2 * xr + 1, 0), xr)[0]))
import numpy as np
xs = np.linspace(-2, 3, 500001)
fv = np.cbrt((xs**2 + xs)**2)
r.append(("Q5a abs max/min", abs(fv.max() - 144**(1 / 3)) < 1e-9 and abs(xs[fv.argmax()] - 3) < 1e-9 and abs(fv.min()) < 1e-3))
# Q5b
G = sp.Rational(4, 3) * (3 + sp.sqrt(x))**sp.Rational(3, 2)
r.append(("Q5b", sp.simplify(sp.diff(G, x) - sp.sqrt(3 + sp.sqrt(x)) / sp.sqrt(x)) == 0))
# Q6a
fx = sp.tan(xx) / xx + (2 * xx**2 - 5 * xx + 2) / sp.Abs(2 * xx - 1)
r.append(("Q6a lim 0", sp.limit(sp.tan(xx) / xx + (2 * xx**2 - 5 * xx + 2) / (1 - 2 * xx), xx, 0) == 3))
r.append(("Q6a right 0.5", sp.simplify(sp.limit(sp.tan(xx) / xx + (xx - 2), xx, sp.Rational(1, 2)) - (2 * sp.tan(sp.Rational(1, 2)) - sp.Rational(3, 2))) == 0))
r.append(("Q6a left 0.5", sp.simplify(sp.limit(sp.tan(xx) / xx - (xx - 2), xx, sp.Rational(1, 2)) - (2 * sp.tan(sp.Rational(1, 2)) + sp.Rational(3, 2))) == 0))
r.append(("Q6a factor", sp.expand((2 * xx - 1) * (xx - 2) - (2 * xx**2 - 5 * xx + 2)) == 0))
xn = sp.symbols('xn', negative=True)
r.append(("Q6a no other discontinuity in [-1,1]", sp.tan(1).evalf() < 1e9 and sp.pi / 2 > 1))
# Q6b (substitute x=-1/s, s->0+)
sp_ = sp.symbols('sp_', positive=True)
def g6(av):
    xv = -1 / sp_
    return sp.limit(sp.sqrt(xv**2 + av * xv) - sp.sqrt(xv**2 + 2 * xv), sp_, 0, '+')
r.append(("Q6b limit formula a=3 -> (2-a)/2 = -1/2", sp.simplify(g6(3) + sp.Rational(1, 2)) == 0))
r.append(("Q6b a=-2 gives 2", sp.simplify(g6(-2) - 2) == 0))
for k, v in r:
    print(("OK   " if v else "FAIL ") + k)

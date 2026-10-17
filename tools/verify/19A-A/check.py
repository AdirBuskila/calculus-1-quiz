import sympy as sp, math, random
import numpy as np
x, t, a = sp.symbols('x t a', real=True)
r = []
f = sp.exp(-x) / (1 - x)
r.append(("Q1 f'", sp.simplify(sp.diff(f, x) - sp.exp(x) * x / (sp.exp(2 * x) * (x - 1) ** 2)) == 0))
r.append(("Q1 f''", sp.simplify(sp.diff(f, x, 2) + (x**2 + 1) / (sp.exp(x) * (x - 1) ** 3)) == 0))
r.append(("Q1 lim", sp.limit(f, x, 1, '+') == -sp.oo and sp.limit(f, x, 1, '-') == sp.oo and sp.limit(f, x, sp.oo) == 0))
r.append(("Q1 slope -oo", sp.limit(f / x, x, -sp.oo) == -sp.oo))
r.append(("Q1 f(0)=1", f.subs(x, 0) == 1))
r.append(("Q2a", sp.limit((sp.Integer(3) ** x + sp.Integer(7) ** (2 * x) + x / (x + 1)) ** (1 / (2 * x)), x, sp.oo) == 7))
ok = True
for i in range(3000):
    p = random.uniform(1, math.e)
    q = random.uniform(1, math.e)
    if p > q:
        p, q = q, p
    if q - p < 1e-9:
        continue
    s = (q * math.log(q) - p * math.log(p)) / (q - p)
    ok &= (1 <= s <= 2)
r.append(("Q2b random", ok))
r.append(("Q2b f'", sp.simplify(sp.diff(x * sp.log(x), x) - sp.log(x) - 1) == 0))
r.append(("Q3a", sp.limit((4 / (1 + sp.sqrt(9 + x))) ** (1 / sp.sin(x)), x, 0) == sp.exp(-sp.Rational(1, 24))))
r.append(("Q3a split", sp.simplify(4 / (1 + sp.sqrt(9 + x)) - 1 - (3 - sp.sqrt(9 + x)) / (1 + sp.sqrt(9 + x))) == 0))
Fx = -(2 * sp.tan(x) + 1) / (4 * sp.exp(2 * sp.tan(x)))
r.append(("Q3b", sp.simplify(sp.diff(Fx, x) - sp.tan(x) / (sp.cos(x) ** 2 * sp.exp(2 * sp.tan(x)))) == 0))
g = x * sp.real_root(x**2 - 1, 3)
r.append(("Q4a values", g.subs(x, 3) == 6 and g.subs(x, 1) == 0 and g.subs(x, 0) == 0))
xc = sp.sqrt(sp.Rational(3, 5))
r.append(("Q4a min", abs(float(g.subs(x, xc)) + float(540 ** (1 / 6)) / 5) < 1e-12))
gp = (5 * x**2 - 3) / (3 * (x**2 - 1) ** sp.Rational(2, 3))
r.append(("Q4a crit", sp.simplify(gp.subs(x, xc)) == 0))
xs = np.linspace(0, 3, 300001)
gv = xs * np.cbrt(xs**2 - 1)
r.append(("Q4a extrema numeric", abs(gv.max() - 6) < 1e-9 and abs(gv.min() + 540 ** (1 / 6) / 5) < 1e-8))
h = (x - 3) ** sp.sqrt(x)
r.append(("Q4b", sp.simplify(sp.diff(h, x).subs(x, 4)) == 2 and h.subs(x, 4) == 1))
r.append(("Q5a", sp.limit(1 / ((sp.sqrt(2 * x - 1) - sp.sqrt(2 * x - 3)) * sp.sqrt(x + 1)), x, sp.oo) == sp.sqrt(2)))
G = sp.log(sp.Abs(x - 1)) + sp.log(x**2 + 1) / 2
r.append(("Q5b", sp.simplify(sp.diff(G, x) - (2 * x**2 - x + 1) / ((x - 1) * (x**2 + 1))) == 0))
V = 2 * sp.pi * sp.integrate(x * (1 - (sp.exp(x) - 1)), (x, 0, sp.log(2)))
r.append(("Q6a", sp.simplify(V - 2 * sp.pi * (1 - sp.log(2)) ** 2) == 0))
V2 = sp.pi * sp.log(2) ** 2 - 2 * sp.pi * sp.integrate(x * (sp.exp(x) - 1), (x, 0, sp.log(2)))
r.append(("Q6a cyl", sp.simplify(V2 - V) == 0))
S = sp.integrate(x / 2, (x, 0, 1)) + sp.integrate(1 / x - x / 2, (x, 1, sp.sqrt(2)))
r.append(("Q6b", sp.simplify(S - sp.log(2) / 2) == 0))
for k, v in r:
    print(k, "OK" if v else "MISMATCH")
print("ALL OK" if all(v for _, v in r) else "FAIL")

import sympy as sp, math
import numpy as np
x, t, a, b, L = sp.symbols('x t a b L', real=True)
r = []
y = x**3 / (x**2 - 3)
r.append(("Q1 y'", sp.simplify(sp.diff(y, x) - x**2 * (x - 3) * (x + 3) / (x**2 - 3) ** 2) == 0))
r.append(("Q1 y''", sp.simplify(sp.diff(y, x, 2) - 6 * x * (x**2 + 9) / (x**2 - 3) ** 3) == 0))
r.append(("Q1 y(+-3)", y.subs(x, 3) == sp.Rational(9, 2) and y.subs(x, -3) == -sp.Rational(9, 2)))
s3 = sp.sqrt(3)
r.append(("Q1 lim", sp.limit(y, x, s3, '+') == sp.oo and sp.limit(y, x, s3, '-') == -sp.oo
          and sp.limit(y, x, -s3, '+') == sp.oo and sp.limit(y, x, -s3, '-') == -sp.oo))
r.append(("Q1 asym", sp.limit(y / x, x, sp.oo) == 1 and sp.limit(y - x, x, sp.oo) == 0 and sp.limit(y - x, x, -sp.oo) == 0))
r.append(("Q1 odd", sp.simplify(y.subs(x, -x) + y) == 0))
an = [2.0]
for i in range(40):
    an.append(3 * an[-1] / (2 * an[-1] + 1))
r.append(("Q2 dec in (1,2)", all(1 < an[i + 1] < an[i] <= 2 for i in range(30))))
r.append(("Q2 L", set(sp.solve(sp.Eq(L, 3 * L / (2 * L + 1)), L)) == {0, 1} and abs(an[-1] - 1) < 1e-9))
r.append(("Q2 form", sp.simplify(3 * L / (2 * L + 1) - 3 / (2 + 1 / L)) == 0))
f = sp.Integral(t * (t - 1) ** 5, (t, -3, x**3 + 1)).doit()
fp = sp.diff(f, x)
r.append(("Q3a f'", sp.simplify(fp - 3 * x**17 * (x**3 + 1)) == 0))
r.append(("Q3a signs", fp.subs(x, -2) > 0 and fp.subs(x, -sp.Rational(1, 2)) < 0 and fp.subs(x, 1) > 0))
xsn = np.linspace(-30, 0.5, 600001)
vals = np.exp(xsn) + np.sin(xsn)
nroots = int(np.sum(vals[:-1] * vals[1:] < 0))
r.append(("Q3b several roots", nroots >= 8 and math.exp(-math.pi / 2) - 1 < 0))
r.append(("Q3b x>0", bool(np.all(np.exp(np.linspace(0.001, 20, 5000)) + np.sin(np.linspace(0.001, 20, 5000)) > 0))))
r.append(("Q4a left", sp.limit(sp.sin(x) ** sp.tan(x), x, sp.pi / 2, '-') == 1))
V = sp.pi * sp.integrate(x**2 * sp.atan(x), (x, 0, 1))
corr = sp.pi**2 / 12 - sp.pi / 6 + sp.pi * sp.log(2) / 6
wrong = sp.pi**2 / 12 - sp.pi / 3 + sp.pi * sp.log(2) / 6
r.append(("Q4b V", sp.simplify(V - corr) == 0))
r.append(("Q4b printed final differs", abs(float(V - wrong)) > 0.1))
r.append(("Q4b inner", sp.integrate(x**3 / (1 + x**2), (x, 0, 1)) == sp.Rational(1, 2) - sp.log(2) / 2))
fq = x * sp.exp(x**2)
fqp = sp.diff(fq, x)
r.append(("Q5a f'", sp.simplify(fqp - sp.exp(x**2) * (1 + 2 * x**2)) == 0 and fqp.subs(x, 1) == 3 * sp.E
          and sp.simplify(fqp.subs(x, 2) - 9 * sp.exp(4)) == 0))
r.append(("Q5a incr", sp.simplify(sp.diff(fqp, x) - sp.exp(x**2) * (6 * x + 4 * x**3)) == 0))
Gx = 1 / (3 * sp.cos(x) ** 3) - 1 / sp.cos(x)
r.append(("Q5b", sp.simplify(sp.diff(Gx, x) - sp.sin(x) ** 3 / sp.cos(x) ** 4) == 0))
r.append(("Q6a", sp.integrate(1 / sp.sqrt(1 - x**2), (x, 0, sp.Rational(1, 2))) == sp.pi / 6
          and sp.simplify(1 + sp.diff(sp.sqrt(1 - x**2), x) ** 2 - 1 / (1 - x**2)) == 0))
r.append(("Q6b", sp.limit(sp.log(x) * sp.log(1 - x), x, 1, '-') == 0))
r.append(("Q6b rewrite", sp.simplify(sp.diff(sp.log(1 - x), x) / sp.diff(1 / sp.log(x), x) - x * sp.log(x) ** 2 / (1 - x)) == 0))
for k, v in r:
    print(k, "OK" if v else "MISMATCH")
print("ALL OK" if all(v for _, v in r) else "FAIL")

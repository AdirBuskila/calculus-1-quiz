import sympy as sp, math
x, t, a, b, c, h = sp.symbols('x t a b c h', real=True)
r = []
f = x * sp.exp(1 / x)
r.append(("Q1 f'", sp.simplify(sp.diff(f, x) - sp.exp(1 / x) * (x - 1) / x) == 0))
r.append(("Q1 f''", sp.simplify(sp.diff(f, x, 2) - sp.exp(1 / x) / x**3) == 0))
r.append(("Q1 f(1)=e", f.subs(x, 1) == sp.E))
r.append(("Q1 x->0+", sp.limit(f, x, 0, '+') == sp.oo))
r.append(("Q1 x->0-", sp.limit(f, x, 0, '-') == 0))
r.append(("Q1 slope", sp.limit(f / x, x, sp.oo) == 1 and sp.limit(f / x, x, -sp.oo) == 1))
r.append(("Q1 b", sp.limit(f - x, x, sp.oo) == 1 and sp.limit(f - x, x, -sp.oo) == 1))
# Q2a
def g(n):
    return (n - (n**6 - 1) ** (1 / 3)) / (1 + n**3)
r.append(("Q2a ->0", abs(g(1e4)) < 1e-3))
r.append(("Q2a limit sym", sp.limit((x - sp.real_root(x**6 - 1, 3)) / (1 + x**3), x, sp.oo) == 0))
# Q2b
yp = 3 * a * x**2 + 2 * b * x + c
ypp = 6 * a * x + 2 * b
xs = sp.solve(ypp, x)[0]
r.append(("Q2b x=-b/3a", sp.simplify(xs + b / (3 * a)) == 0))
r.append(("Q2b cond", sp.simplify(yp.subs(x, xs) - (c - b**2 / (3 * a))) == 0))
# Q3
r.append(("Q3a", sp.limit(sp.cos(x) ** (1 / sp.sin(2 * x) ** 2), x, 0) == sp.exp(-sp.Rational(1, 8))))
r.append(("Q3b", sp.simplify(sp.diff(sp.log((sp.log(x) - 3) ** 2) / 2 - sp.log((sp.log(x) - 2) ** 2) / 2, x)
                              - 1 / (x * (sp.log(x) ** 2 - 5 * sp.log(x) + 6))) == 0))
r.append(("Q3b A,B", sp.simplify(-(t - 3) + (t - 2) - 1) == 0))
# Q4a
r.append(("Q4a left", sp.simplify(1 / (sp.sqrt(2) - 1) - sp.sqrt(2)) == 1))
r.append(("Q4a right", sp.limit((sp.sqrt(1 + a * x) - sp.cos(x)) / x, x, 0, '+') == a / 2))
# Q4b
r.append(("Q4b", sp.simplify(sp.integrate(sp.cosh(x), (x, -2, 2)) - (sp.exp(2) - sp.exp(-2))) == 0))
r.append(("Q4b 1+y'^2", sp.simplify(1 + sp.sinh(x) ** 2 - sp.cosh(x) ** 2) == 0))
# Q5
u = sp.symbols('u', positive=True)
Fx = sp.log(u) / 2 - 2 * sp.log(u ** sp.Rational(1, 4) + 2)
r.append(("Q5b", sp.simplify(sp.diff(Fx, u) - 1 / (u ** sp.Rational(3, 4) * (sp.sqrt(u) + 2 * u ** sp.Rational(1, 4)))) == 0))
r.append(("Q5b A,B", sp.simplify(sp.Rational(1, 2) * (t + 2) - sp.Rational(1, 2) * t - 1) == 0))
r.append(("Q5a", abs((abs(1e-6) * math.cos(math.pi / 2 + 1e-6)) / 1e-6) < 1e-5))
# Q6
fx = sp.sqrt(x - 2) * sp.exp(-x / 2)
r.append(("Q6a f'", sp.simplify(sp.diff(fx, x) - (3 - x) / (2 * sp.sqrt(x - 2)) * sp.exp(-x / 2)) == 0))
r.append(("Q6a crit", sp.solve(sp.diff(fx, x), x) == [3]))
V = sp.pi * sp.integrate((x - 2) * sp.exp(-x), (x, 2, 3))
r.append(("Q6b", sp.simplify(V - sp.pi * (sp.exp(-2) - 2 * sp.exp(-3))) == 0))
r.append(("Q6b 0.1123", round(float(V), 4) == 0.1123))
r.append(("Q6a sign plus->minus", sp.N(sp.diff(fx, x).subs(x, sp.Rational(5, 2))) > 0 and sp.N(sp.diff(fx, x).subs(x, sp.Rational(7, 2))) < 0))
for k, v in r:
    print(k, "OK" if v else "MISMATCH")
print("ALL OK" if all(v for _, v in r) else "FAIL")

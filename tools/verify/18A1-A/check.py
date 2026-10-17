import sympy as sp
x, t = sp.symbols('x t', real=True)
xx = sp.symbols('xx', positive=True)
r = []
f = (x - 2) / sp.sqrt(x**2 + 1)
r.append(("Q1 f'", sp.simplify(sp.diff(f, x) - (2 * x + 1) / (x**2 + 1)**sp.Rational(3, 2)) == 0))
r.append(("Q1 f(-1/2)=-sqrt5", sp.simplify(f.subs(x, -sp.Rational(1, 2)) + sp.sqrt(5)) == 0))
r.append(("Q1 f'' numerator -4x^2-3x+2 (printed -2)",
          sp.simplify(sp.diff(f, x, 2) - (-4 * x**2 - 3 * x + 2) / (x**2 + 1)**sp.Rational(5, 2)) == 0))
r.append(("Q1 inflection (-3+-sqrt41)/8 (printed /16)",
          sorted(sp.solve(4 * x**2 + 3 * x - 2, x), key=float) == [(-3 - sp.sqrt(41)) / 8, (-3 + sp.sqrt(41)) / 8]))
r.append(("Q1 asymptotes", sp.limit(f, x, sp.oo) == 1 and sp.limit(f, x, -sp.oo) == -1))
F = 2 * sp.sqrt(xx) - 3 * xx**sp.Rational(1, 3) + 6 * xx**sp.Rational(1, 6) - 6 * sp.log(1 + xx**sp.Rational(1, 6))
r.append(("Q2b", sp.simplify(sp.diff(F, xx) - 1 / (xx**sp.Rational(1, 3) + sp.sqrt(xx))) == 0))
G = sp.integrate(sp.sin(sp.sqrt(t)), (t, 0, x**2))
q = G / sp.tan(2 * x**3)
r.append(("Q3a right limit 1/3", sp.limit(q, x, 0, '+') == sp.Rational(1, 3)))
r.append(("Q3a left limit -1/3 (two-sided limit does not exist)", sp.limit(q, x, 0, '-') == -sp.Rational(1, 3)))
r.append(("Q3a derivative of tan(2x^3) has cos^2", sp.simplify(sp.diff(sp.tan(2 * x**3), x) - 6 * x**2 / sp.cos(2 * x**3)**2) == 0))
a, s = sp.symbols('a s', positive=True)
sol = sp.solve([sp.Eq(a * s**2, sp.log(s)), sp.Eq(2 * a * s, 1 / s)], [a, s], dict=True)
r.append(("Q3b a=1/(2e)", any(sp.simplify(d[a] - 1 / (2 * sp.E)) == 0 for d in sol)))
r.append(("Q4a", (2 * sp.atan(2) - 1).evalf() > 0 and sp.diff(x * sp.atan(x), x).subs(x, 1) > 0))
r.append(("Q4b", sp.integrate(sp.sin(x)**2, (x, 0, sp.pi)) == sp.pi / 2))
h = sp.Abs(x**3 - 3 * x**2)
vals = {p: h.subs(x, p) for p in [1, 2, 3, 4]}
r.append(("Q5a f(1)=2 f(2)=4 f(3)=0 f(4)=16 (printed f(0) instead of f(2))", vals == {1: 2, 2: 4, 3: 0, 4: 16}))
Fi = sp.atan(2 * sp.tan(x / 2)) / 2
r.append(("Q5b", abs(float((sp.diff(Fi, x) - 1 / (5 - 3 * sp.cos(x))).subs(x, 0.7))) < 1e-12))
r.append(("Q6a", sp.integrate(2 * sp.pi * x * sp.exp(x), (x, 1, 2)) == 2 * sp.pi * sp.exp(2)))
r.append(("Q6b", sp.limit((sp.exp(3 * x) - sp.exp(2 * x))**2 / (sp.cos(5 * x) - sp.cos(x)), x, 0) == -sp.Rational(1, 12)))
for k, v in r:
    print(("OK   " if v else "FAIL ") + k)

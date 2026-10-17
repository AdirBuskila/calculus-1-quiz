import sympy as sp, math
x, t, L, a = sp.symbols('x t L a', real=True)
A, B, C = sp.symbols('A B C')
r = []
f = 2 * x**2 / (x**2 - 1)
r.append(("Q1 split", sp.simplify(f - (2 + 2 / (x**2 - 1))) == 0))
r.append(("Q1 f'", sp.simplify(sp.diff(f, x) + 4 * x / (x**2 - 1) ** 2) == 0))
r.append(("Q1 f''", sp.simplify(sp.diff(f, x, 2) - 4 * (3 * x**2 + 1) / (x**2 - 1) ** 3) == 0))
r.append(("Q1 lim", sp.limit(f, x, 1, '+') == sp.oo and sp.limit(f, x, 1, '-') == -sp.oo
          and sp.limit(f, x, -1, '+') == -sp.oo and sp.limit(f, x, -1, '-') == sp.oo))
r.append(("Q1 y=2", sp.limit(f, x, sp.oo) == 2 and sp.limit(f, x, -sp.oo) == 2))
an = [4.0]
for i in range(400):
    an.append(math.sqrt(5 * an[-1] - 6))
r.append(("Q2a dec>3", all(an[i] > an[i + 1] > 3 for i in range(30))))
r.append(("Q2a diff", sp.simplify((sp.sqrt(5 * L - 6) - L) + (L - 2) * (L - 3) / (sp.sqrt(5 * L - 6) + L)) == 0))
r.append(("Q2a fixed", set(sp.solve(sp.Eq(L, sp.sqrt(5 * L - 6)), L)) <= {2, 3} and 3 in sp.solve(sp.Eq(L, sp.sqrt(5 * L - 6)), L)))
r.append(("Q2a L=3", abs(an[-1] - 3) < 1e-6))
F = x**3 + x + sp.exp(x)
r.append(("Q2b f(-1)<0,f(0)=1", F.subs(x, -1).evalf() < 0 and F.subs(x, 0) == 1))
r.append(("Q2b f'>0", sp.simplify(sp.diff(F, x) - (3 * x**2 + 1 + sp.exp(x))) == 0))
r.append(("Q3a", sp.limit((1 + sp.exp(x)) ** (1 / x), x, sp.oo) == sp.E))
r.append(("Q3b", sp.simplify(sp.diff(x * sp.asin(x) + sp.sqrt(1 - x**2), x) - sp.asin(x)) == 0))
ln = sp.log
r.append(("Q4a roots", set(sp.solve(sp.Eq(ln(a) ** 2, ln(a)), a)) == {1, sp.E}))
fp = ln(1 + x**2)
r.append(("Q4b", sp.solve(sp.Eq(sp.diff(fp, x), 1), x) == [1] and sp.simplify(fp.subs(x, 1) - ln(2)) == 0))
r.append(("Q5a", sp.limit(sp.sqrt(2 + 2 * x + x**2) - sp.sqrt(2 - 2 * x + x**2), x, -sp.oo) == -2))
G = -sp.log((x + 1) ** 2) / 4 + sp.log(x**2 + 1) / 4 + sp.atan(x) / 2
r.append(("Q5b", sp.simplify(sp.diff(G, x) - x / ((x**2 + 1) * (x + 1))) == 0))
r.append(("Q5b ABC", sp.solve([A + B, B + C - 1, A + C], [A, B, C]) == {A: -sp.Rational(1, 2), B: sp.Rational(1, 2), C: sp.Rational(1, 2)}))
V = sp.pi * sp.integrate((sp.pi / 2 - x) ** 2 - sp.cos(x) ** 2, (x, 0, sp.pi / 2))
r.append(("Q6a", sp.simplify(V - sp.pi**2 / 4 * (-1 + sp.pi**2 / 6)) == 0))
S = sp.integrate(sp.sqrt(x + 2), (x, -2, 2)) - sp.integrate(sp.sqrt(2 * x), (x, 0, 2))
r.append(("Q6b", sp.simplify(S - sp.Rational(8, 3)) == 0))
for k, v in r:
    print(k, "OK" if v else "MISMATCH")
print("ALL OK" if all(v for _, v in r) else "FAIL")

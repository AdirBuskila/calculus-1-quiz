import sympy as sp, math
x = sp.symbols('x', real=True)
p = sp.symbols('p', positive=True)
aa = sp.symbols('aa')
r = []
f = ((x - 2) / (x - 1))**2
r.append(("Q1 f'", sp.simplify(sp.diff(f, x) - 2 * (x - 2) / (x - 1)**3) == 0))
r.append(("Q1 f''", sp.simplify(sp.diff(f, x, 2) - 2 * (5 - 2 * x) / (x - 1)**4) == 0))
r.append(("Q1 values", f.subs(x, sp.Rational(5, 2)) == sp.Rational(1, 9) and f.subs(x, 0) == 4 and f.subs(x, 2) == 0))
r.append(("Q1 limits", sp.limit(f, x, 1, '+') == sp.oo and sp.limit(f, x, 1, '-') == sp.oo and sp.limit(f, x, sp.oo) == 1))
a = sp.Integer(5)
seq = [a]
for _ in range(60):
    a = 2 - 1 / (2 + a)
    seq.append(a)
r.append(("Q2 a2, a3", seq[1] == sp.Rational(13, 7) and seq[2] == sp.Rational(47, 27)))
r.append(("Q2 decreasing from a2, >= sqrt3, limit sqrt3",
          all(seq[i + 1] < seq[i] and float(seq[i + 1]) >= math.sqrt(3) for i in range(1, 50)) and abs(float(seq[-1]) - math.sqrt(3)) < 1e-9))
r.append(("Q2 a(n+1)-a(n) = (3-a^2)/(2+a) (written with 2-a in the denominator)", sp.simplify((2 - p - 1 / (2 + p)) - (3 - p**2) / (2 + p)) == 0))
r.append(("Q3a", sp.limit(x - sp.log(1 + 2 * sp.exp(x)), x, sp.oo) == -sp.log(2)))
r.append(("Q3b V1 V2 V", sp.integrate(2 * sp.pi * p * 9, (p, 1, 2)) == 27 * sp.pi
          and sp.integrate(2 * sp.pi * p * (1 + p**3), (p, 1, 2)) == 77 * sp.pi / 5
          and sp.integrate(2 * sp.pi * p * (8 - p**3), (p, 1, 2)) == 58 * sp.pi / 5))
r.append(("Q4a tangent-free check: ln x between (x-1)/x and x-1 at x=3", sp.log(3) > sp.Rational(2, 3) and sp.log(3) < 2))
r.append(("Q4b", sp.integrate(p / 4 + 1, (p, -4, 4)) - sp.integrate(sp.sqrt(p), (p, 0, 4)) == sp.Rational(8, 3)))
r.append(("Q4b y-form", sp.integrate(p**2 - (4 * p - 4), (p, 0, 2)) == sp.Rational(8, 3)))
g = sp.sqrt(p) + 4 / p
vals = {q: g.subs(p, q) for q in [sp.Rational(1, 4), 4, 100]}
r.append(("Q5a f(1/4)=33/2 (written 17/2), f(4)=3, f(100)=251/25 (written 52/2)",
          vals == {sp.Rational(1, 4): sp.Rational(33, 2), 4: 3, 100: sp.Rational(251, 25)}))
r.append(("Q5a critical point x=4", sp.solve(sp.diff(g, p), p) == [4]))
r.append(("Q5a max 33/2 at 1/4 and min 3 at 4 (grid)", abs(max(float(g.subs(p, 0.25 + k * 0.01)) for k in range(0, 9976)) - 16.5) < 1e-9
          and abs(min(float(g.subs(p, 0.25 + k * 0.01)) for k in range(0, 9976)) - 3) < 1e-3))
r.append(("Q5b", sp.simplify(sp.diff(-sp.cos(x) + 2 * sp.cos(x)**3 / 3 - sp.cos(x)**5 / 5, x) - sp.sin(x)**5) == 0))
r.append(("Q6a left limit a^2", sp.limit(((sp.exp(aa * x) - 1) / x)**2, x, 0, '-') == aa**2))
r.append(("Q6a right limit 4", sp.limit(4 + sp.exp(-4 / p), p, 0, '+') == 4))
r.append(("Q6b", sp.simplify(sp.diff(2 * sp.sqrt(p + 1) * sp.log(p + 1) - 4 * sp.sqrt(p + 1), p) - sp.log(p + 1) / sp.sqrt(p + 1)) == 0))
for k, v in r:
    print(("OK   " if v else "FAIL ") + k)

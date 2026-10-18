# sympy verification of the SOLVED answers, sitting 20B-C (no key exists; ASCII output)
import sympy as sp
x, t = sp.symbols('x t', real=True)
n = sp.symbols('n', positive=True, integer=True)
r = []


def ok(name, cond):
    r.append((name, bool(cond)))


# Q1
f = x**3/(2*(x + 1)**2)
d1, d2 = sp.diff(f, x), sp.diff(f, x, 2)
ok("Q1 f' = x^2(x+3)/(2(x+1)^3)", sp.simplify(d1 - x**2*(x + 3)/(2*(x + 1)**3)) == 0)
ok("Q1 f'' = 3x/(x+1)^4", sp.simplify(d2 - 3*x/(x + 1)**4) == 0)
sg = lambda e, v: sp.sign(e.subs(x, v))
ok("Q1 f' signs + - + +", [sg(d1, -4), sg(d1, -2), sg(d1, -sp.Rational(1, 2)), sg(d1, 1)] == [1, -1, 1, 1])
ok("Q1 f'' signs - - +", [sg(d2, -2), sg(d2, -sp.Rational(1, 2)), sg(d2, 1)] == [-1, -1, 1])
ok("Q1 f(-3) = -27/8", f.subs(x, -3) == -sp.Rational(27, 8))
ok("Q1 x->-1 : -oo both sides", sp.limit(f, x, -1, '+') == -sp.oo and sp.limit(f, x, -1, '-') == -sp.oo)
ok("Q1 oblique y = x/2 - 1", all(sp.limit(f/x, x, s) == sp.Rational(1, 2) and sp.limit(f - x/2, x, s) == -1 for s in (sp.oo, -sp.oo)))
ok("Q1 decomposition", sp.simplify(f - (x/2 - 1 + (3*x + 2)/(2*(x + 1)**2))) == 0)
# Q2a
ok("Q2a b=1 -> 1, b=3 -> 1/2, b=5 -> 0",
   sp.limit(3**n/(3**n + 1), n, sp.oo) == 1 and sp.limit(3**n/(3**n + 3**n), n, sp.oo) == sp.Rational(1, 2) and sp.limit(3**n/(3**n + 5**n), n, sp.oo) == 0)
ok("Q2a b=2.9 -> 1, b=3.1 -> 0 (numeric n=2000)",
   abs(sp.N(sp.Integer(3)**2000/(sp.Integer(3)**2000 + sp.Rational(29, 10)**2000)) - 1) < 1e-9 and sp.N(sp.Integer(3)**2000/(sp.Integer(3)**2000 + sp.Rational(31, 10)**2000)) < 1e-9)
# Q2b
F = x**2/2 + 4*sp.log(sp.Abs(x - 1)) - sp.log(sp.Abs(x + 1))
ok("Q2b decomposition x + 4/(x-1) - 1/(x+1)", sp.simplify((x**3 + 2*x + 5)/(x**2 - 1) - (x + 4/(x - 1) - 1/(x + 1))) == 0)
ok("Q2b antiderivative", all(abs(float((sp.diff(F, x) - (x**3 + 2*x + 5)/(x**2 - 1)).subs(x, v))) < 1e-12 for v in (2.5, 0.3, -0.6, -3.0)))
# Q3a
ok("Q3a left limit 1/2", sp.limit((sp.exp(x) - 1)/sp.sin(2*x), x, 0, '-') == sp.Rational(1, 2))
ok("Q3a right limit 1/2", sp.limit(x*sp.log(x) + sp.asin(x)/(2*x), x, 0, '+') == sp.Rational(1, 2))
# Q3b
g = x*sp.sqrt(18 - x**2)
ok("Q3b g' = (18-2x^2)/sqrt(18-x^2), zero at 3", sp.simplify(sp.diff(g, x) - (18 - 2*x**2)/sp.sqrt(18 - x**2)) == 0 and sp.solve(sp.diff(g, x), x) == [-3, 3])
ok("Q3b g(0)=0, g(3)=9, g(4)=4sqrt2", g.subs(x, 0) == 0 and g.subs(x, 3) == 9 and sp.simplify(g.subs(x, 4) - 4*sp.sqrt(2)) == 0)
# Q4a
F = x*sp.log(x)**2 - 2*x*sp.log(x) + 2*x
ok("Q4a antiderivative", sp.simplify(sp.diff(F, x) - sp.log(x)**2) == 0)
# Q4b
ok("Q4b limit 1/8", sp.limit((sp.sqrt(3*x - 2) - sp.sqrt(x + 2))/(x**2 - 4), x, 2) == sp.Rational(1, 8))
# Q5a
I = sp.Integral(1/(2*x**4 + 1), (x, -1, 1)).evalf()
ok("Q5a 2/3 <= I <= 2 (I = %.4f)" % float(I), sp.Rational(2, 3) <= I <= 2)
# Q5b
ok("Q5b limit 1/3", sp.limit(sp.integrate(t**2/(1 + t**4), (t, 0, x))/x**3, x, 0) == sp.Rational(1, 3))
# Q6a
approx = 1 + 2*sp.pi/60
ok("Q6a tan48 ~ 1 + pi/30 = %.4f (true %.4f)" % (float(approx), float(sp.tan(sp.pi*48/180))), abs(float(approx) - 1.1047) < 1e-4)
ok("Q6a sec^2(pi/4) = 2", sp.simplify(sp.diff(sp.tan(x), x).subs(x, sp.pi/4)) == 2)
# Q6b
S = sp.integrate(2*x - x/2, (x, 0, 1/sp.sqrt(2))) + sp.integrate(1/x - x/2, (x, 1/sp.sqrt(2), sp.sqrt(2)))
ok("Q6b first-quadrant area = ln 2", sp.simplify(S - sp.log(2)) == 0)
ys = sp.symbols('ys', positive=True)
ok("Q6b intersections (1/sqrt2, sqrt2), (sqrt2, 1/sqrt2)", sp.solve(sp.Eq(2*x, 1/x), x) == [-sp.sqrt(2)/2, sp.sqrt(2)/2] and sp.solve(sp.Eq(x/2, 1/x), x) == [-sp.sqrt(2), sp.sqrt(2)])
bad = [nm for nm, c in r if not c]
for nm, c in r:
    print(("OK  " if c else "FAIL"), nm)
print("mismatches:", len(bad))

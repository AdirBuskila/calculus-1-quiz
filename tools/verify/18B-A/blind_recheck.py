# Blind re-derivation (solver, 2026-10-18) of every final answer in 18B-A (handwritten unnamed key). ASCII output.
import sympy as sp
x, t = sp.symbols('x t', real=True)
r = []
ok = lambda nm, c: r.append((nm, bool(c)))
# Q1
f = x**3/(x**2 - 3)
ok("Q1 f' = x^2(x^2-9)/(x^2-3)^2", sp.simplify(sp.diff(f, x) - x**2*(x**2 - 9)/(x**2 - 3)**2) == 0)
ok("Q1 max (-3,-9/2), min (3,9/2)", f.subs(x, -3) == -sp.Rational(9, 2) and f.subs(x, 3) == sp.Rational(9, 2) and sp.diff(f, x, 2).subs(x, 3) > 0)
ok("Q1 f'' = 6x(x^2+9)/(x^2-3)^3", sp.simplify(sp.diff(f, x, 2) - 6*x*(x**2 + 9)/(x**2 - 3)**3) == 0)
s3 = sp.sqrt(3)
ok("Q1 one-sided limits at +-sqrt3", [sp.limit(f, x, s3, '+'), sp.limit(f, x, s3, '-'), sp.limit(f, x, -s3, '+'), sp.limit(f, x, -s3, '-')] == [sp.oo, -sp.oo, sp.oo, -sp.oo])
ok("Q1 oblique y=x", sp.limit(f - x, x, sp.oo) == 0 and sp.limit(f/x, x, sp.oo) == 1)
# Q2
a = 2.0
for _ in range(80): a = 3*a/(2*a + 1)
ok("Q2 limit 1", abs(a - 1) < 1e-12)
# Q3a
fp = sp.diff(sp.integrate(t*(t - 1)**5, (t, -3, x**3 + 1)), x)
ok("Q3a f' = 3x^17(x^3+1)", sp.expand(fp - 3*x**17*(x**3 + 1)) == 0)
ok("Q3a signs + - +: max at -1, min at 0", [sp.sign(fp.subs(x, v)) for v in (-2, -sp.Rational(1, 2), 1)] == [1, -1, 1])
# Q3b
import math
g = lambda v: math.exp(v) + math.sin(v)
roots = sum(1 for k in range(-3000, 50) if g(k/100) * g((k + 1)/100) < 0)
ok("Q3b many roots in [-30,0.5] (not unique): %d" % roots, roots >= 8)
ok("Q3b no root for x>=0", all(g(v/10) > 0 for v in range(0, 300)))
# Q4a
ok("Q4a left limit 1, right value e -> discontinuous", sp.limit(sp.sin(x)**sp.tan(x), x, sp.pi/2, '-') == 1)
# Q4b
V = sp.pi*sp.integrate(x**2*sp.atan(x), (x, 0, 1))
ok("Q4b V = pi^2/12 - pi/6 + (pi/6)ln2 (handwritten -pi/3 is wrong -> labeled)", sp.simplify(V - (sp.pi**2/12 - sp.pi/6 + sp.pi/6*sp.log(2))) == 0)
# Q5a
fp5 = sp.diff(x*sp.exp(x**2), x)
ok("Q5a f'(1)=3e, f'(2)=9e^4, f' increasing on (1,2)", fp5.subs(x, 1) == 3*sp.E and sp.simplify(fp5.subs(x, 2) - 9*sp.exp(4)) == 0 and all(sp.diff(fp5, x).subs(x, v) > 0 for v in (1, 1.5, 2)))
# Q5b
F = 1/(3*sp.cos(x)**3) - 1/sp.cos(x)
ok("Q5b antiderivative", sp.simplify(sp.diff(F, x) - sp.sin(x)**3/sp.cos(x)**4) == 0)
# Q6a
ok("Q6a L = pi/6", sp.simplify(sp.integrate(sp.sqrt(1 + sp.diff(sp.sqrt(1 - x**2), x)**2), (x, 0, sp.Rational(1, 2))) - sp.pi/6) == 0)
# Q6b
ok("Q6b limit 0", sp.limit(sp.log(x)*sp.log(1 - x), x, 1, '-') == 0)
for nm, c in r: print(("OK  " if c else "FAIL"), nm)
print("mismatches:", sum(1 for _, c in r if not c))

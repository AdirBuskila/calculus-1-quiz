# Blind re-derivation (solver, 2026-10-18) of every final answer in 17B-A (handwritten unnamed key). ASCII output.
import sympy as sp
x, y = sp.symbols('x y', real=True)
r = []
ok = lambda nm, c: r.append((nm, bool(c)))
# Q1
f = ((x - 2)/(x - 1))**2
ok("Q1 f' = 2(x-2)/(x-1)^3", sp.simplify(sp.diff(f, x) - 2*(x - 2)/(x - 1)**3) == 0)
ok("Q1 f'' = 2(5-2x)/(x-1)^4", sp.simplify(sp.diff(f, x, 2) - 2*(5 - 2*x)/(x - 1)**4) == 0)
ok("Q1 min (2,0), inflection (5/2,1/9), intercept (0,4)", f.subs(x, 2) == 0 and f.subs(x, sp.Rational(5, 2)) == sp.Rational(1, 9) and f.subs(x, 0) == 4)
ok("Q1 asymptotes x=1 (+oo both), y=1", sp.limit(f, x, 1, '+') == sp.oo and sp.limit(f, x, 1, '-') == sp.oo and sp.limit(f, x, sp.oo) == 1 and sp.limit(f, x, -sp.oo) == 1)
# Q2
a = 5.0
seq = []
for _ in range(60): seq.append(a); a = 2 - 1/(2 + a)
ok("Q2 decreasing from a1, limit sqrt3", all(seq[i + 1] <= seq[i] for i in range(59)) and abs(seq[-1] - 3**0.5) < 1e-12)
# Q3a
ok("Q3a -ln2", sp.limit(x - sp.log(1 + 2*sp.exp(x)), x, sp.oo) == -sp.log(2))
# Q3b: region 1<=x<=2 between y=1+x^3 and y=9, about the y-axis (washers in y as an independent method)
V = sp.pi*sp.integrate((y - 1)**sp.Rational(2, 3) - 1, (y, 2, 9))
ok("Q3b V = 58pi/5 (washers in y)", sp.simplify(V - 58*sp.pi/5) == 0)
# Q4a
ok("Q4a samples", all((v - 1)/v < float(sp.log(v)) < v - 1 for v in (1.01, 2, 10, 500)))
# Q4b
ok("Q4b area 8/3 (in y)", sp.integrate(y**2 - (4*y - 4), (y, 0, 2)) == sp.Rational(8, 3))
tri = sp.Rational(1, 2)*8*2  # tangent hits x-axis at -4; triangle (-4,0),(4,0),(4,2)
ok("Q4b area 8/3 (triangle 8 minus 16/3)", tri - sp.integrate(sp.sqrt(x), (x, 0, 4)) == sp.Rational(8, 3))
# Q5a
g = sp.sqrt(x) + 4/x
cand = [sp.Rational(1, 4), 4, 100]
ok("Q5a f(1/4)=33/2 max, f(4)=3 min, f(100)=251/25", [g.subs(x, c) for c in cand] == [sp.Rational(33, 2), 3, sp.Rational(251, 25)] and sp.solve(sp.diff(g, x), x) == [4])
# Q5b
F = -sp.cos(x) + sp.Rational(2, 3)*sp.cos(x)**3 - sp.cos(x)**5/5
ok("Q5b antiderivative", sp.simplify(sp.diff(F, x) - sp.sin(x)**5) == 0)
# Q6a
a_ = sp.symbols('a', real=True)
left = sp.limit((sp.exp(2*x) - 1)**2/x**2, x, 0, '-')
ok("Q6a left limit a^2 (a=2 -> 4), right limit 4", left == 4 and sp.limit(4 + sp.exp(-4/x), x, 0, '+') == 4)
# Q6b
F = 2*sp.sqrt(x + 1)*sp.log(x + 1) - 4*sp.sqrt(x + 1)
ok("Q6b antiderivative", sp.simplify(sp.diff(F, x) - sp.log(x + 1)/sp.sqrt(x + 1)) == 0)
for nm, c in r: print(("OK  " if c else "FAIL"), nm)
print("mismatches:", sum(1 for _, c in r if not c))

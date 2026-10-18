# Blind re-derivation (solver, 2026-10-18) of every final answer in 22A-B (unknown-author worked solution). ASCII output.
import sympy as sp
x, t = sp.symbols('x t', real=True)
r = []
ok = lambda nm, c: r.append((nm, bool(c)))
dnum = lambda F, f, pts: all(abs(complex(sp.N((sp.diff(F, x) - f).subs(x, v)))) < 1e-9 for v in pts)
# Q1 x^3/(x^2-1)
f = x**3/(x**2 - 1)
ok("Q1 f' = x^2(x^2-3)/(x^2-1)^2", sp.simplify(sp.diff(f, x) - x**2*(x**2 - 3)/(x**2 - 1)**2) == 0)
ok("Q1 max (-sqrt3, -3sqrt3/2), min (sqrt3, 3sqrt3/2)", sp.simplify(f.subs(x, sp.sqrt(3)) - 3*sp.sqrt(3)/2) == 0 and sp.diff(f, x, 2).subs(x, sp.sqrt(3)) > 0 and sp.diff(f, x, 2).subs(x, -sp.sqrt(3)) < 0)
ok("Q1 f'' = 2x(x^2+3)/(x^2-1)^3", sp.simplify(sp.diff(f, x, 2) - 2*x*(x**2 + 3)/(x**2 - 1)**3) == 0)
ok("Q1 asymptotes x=+-1, y=x", sp.limit(f, x, 1, '+') == sp.oo and sp.limit(f/x, x, sp.oo) == 1 and sp.limit(f - x, x, sp.oo) == 0)
# Q2a
a = 5.0
for _ in range(60): a = (a + 5/a)/2
ok("Q2a limit sqrt5", abs(a - 5**0.5) < 1e-12)
# Q2b
F = x**2/2*sp.atan(2/x) + x - 2*sp.atan(x/2)
ok("Q2b antiderivative", dnum(F, x*sp.atan(2/x), (0.5, 1.7, 3.0, -2.2)))
# Q3a
g = sp.log(x + 1) - (3*x + 2)/(x + 2)
ok("Q3a g(0)=-1, g->+oo, g'=x^2/((x+1)(x+2)^2)", g.subs(x, 0) == -1 and sp.limit(g, x, sp.oo) == sp.oo and sp.simplify(sp.diff(g, x) - x**2/((x + 1)*(x + 2)**2)) == 0)
# Q3b
F = sp.log(sp.sin(x)**2 + 2)/22 + 3/(11*sp.sqrt(2))*sp.atan(sp.sin(x)/sp.sqrt(2)) - sp.log(3 - sp.sin(x))/11
ok("Q3b antiderivative", dnum(F, sp.cos(x)/((3 - sp.cos(x)**2)*(3 - sp.sin(x))), (0.2, 1.0, 2.5, -1.3)))
# Q4a
y = sp.exp(x/(1 - x))/(1 - sp.exp(x/(1 - x)))
ok("Q4a x=0: -+oo (2nd kind)", sp.limit(y, x, 0, '-') == sp.oo and sp.limit(y, x, 0, '+') == -sp.oo)
ok("Q4a x=1: -1 / 0 (jump, 1st kind)", sp.limit(y, x, 1, '-') == -1 and sp.limit(y, x, 1, '+') == 0)
# Q4b shells
V = 2*sp.pi*sp.integrate(x*sp.cos(x)**2, (x, sp.pi/2, sp.pi))
ok("Q4b V = pi/2 (1 + 3pi^2/4)", sp.simplify(V - sp.pi/2*(1 + 3*sp.pi**2/4)) == 0)
# Q5a
ok("Q5a samples", all(v/(v + 1) < float(sp.log(1 + v)) < v for v in (0.01, 0.5, 2, 30)))
# Q5b
L = sp.Integral(sp.sqrt(1 + sp.exp(2*x)), (x, 0, 1)).evalf()
print("Q5b exact arc length = %.6f (file prints 1.98)" % float(L))
ok("Q5b L ~ 2.0035 (file's 1.98 is wrong -> labeled)", abs(float(L) - 2.0035) < 1e-4)
# Q6a
fr = lambda v: v*sp.sign(3*v - 1)*abs(3*v - 1)**sp.Rational(1, 3)
vals = {v: sp.N(fr(v)) for v in (-1, sp.Rational(1, 4), sp.Rational(1, 3), sp.Rational(2, 3))}
grid = [sp.N(fr(sp.Rational(k, 600) - 1)) for k in range(0, 1001)]
ok("Q6a max cbrt4 at -1, min -(1/4)^(4/3) at 1/4", abs(max(grid) - 4**(1/3)) < 1e-9 and abs(min(grid) + 0.25**(4/3)) < 1e-4)
# Q6b
a_, b_ = sp.symbols('a b')
sol = sp.solve([8*a_ - 4 - b_, 12*a_ - 4], [a_, b_])
ok("Q6b a=1/3, b=-4/3", sol == {a_: sp.Rational(1, 3), b_: -sp.Rational(4, 3)})
for nm, c in r: print(("OK  " if c else "FAIL"), nm)
print("mismatches:", sum(1 for _, c in r if not c))

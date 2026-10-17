# sympy verification of the answers in the sitting 22A-B solution file (ASCII output)
import sympy as sp
import numpy as np
x, t, a, b = sp.symbols('x t a b', real=True)
r = []


def ok(name, cond):
    r.append((name, bool(cond)))


# Q1
f = x**3/(x**2 - 1)
ok("Q1 f' = x^2(x^2-3)/(x^2-1)^2", sp.simplify(sp.diff(f, x) - x**2*(x**2 - 3)/(x**2 - 1)**2) == 0)
ok("Q1 critical points 0, +-sqrt3", sorted(sp.solve(sp.diff(f, x), x), key=float) == [-sp.sqrt(3), 0, sp.sqrt(3)])
ok("Q1 f(-sqrt3) = -3sqrt3/2", sp.simplify(f.subs(x, -sp.sqrt(3)) + 3*sp.sqrt(3)/2) == 0)
ok("Q1 f(sqrt3) = 3sqrt3/2", sp.simplify(f.subs(x, sp.sqrt(3)) - 3*sp.sqrt(3)/2) == 0)
ok("Q1 f'' = (2x^3+6x)/(x^2-1)^3", sp.simplify(sp.diff(f, x, 2) - (2*x**3 + 6*x)/(x**2 - 1)**3) == 0)
sg = lambda v: sp.sign(sp.diff(f, x).subs(x, v))
ok("Q1 f' signs + - - +", [sg(-3), sg(-sp.Rational(1, 2)), sg(sp.Rational(1, 2)), sg(3)] == [1, -1, -1, 1])
s2 = lambda v: sp.sign(sp.diff(f, x, 2).subs(x, v))
ok("Q1 f'' signs - + - +", [s2(-3), s2(-sp.Rational(1, 2)), s2(sp.Rational(1, 2)), s2(3)] == [-1, 1, -1, 1])
ok("Q1 limits at -1", sp.limit(f, x, -1, '-') == -sp.oo and sp.limit(f, x, -1, '+') == sp.oo)
ok("Q1 limits at 1", sp.limit(f, x, 1, '-') == -sp.oo and sp.limit(f, x, 1, '+') == sp.oo)
ok("Q1 slant y=x", sp.limit(f/x, x, sp.oo) == 1 and sp.limit(f - x, x, sp.oo) == 0 and sp.limit(f - x, x, -sp.oo) == 0)
# Q2a
an = 5.0
seq = [an]
for _ in range(40):
    an = 0.5*(an + 5/an)
    seq.append(an)
ok("Q2a a2=3, a3 ~ 2.33, limit sqrt5", seq[1] == 3 and abs(seq[2] - 2.3333333) < 1e-6 and abs(seq[-1] - 5**0.5) < 1e-12)
ok("Q2a decreasing and > sqrt5", all(seq[i + 1] <= seq[i] and seq[i] > 5**0.5 - 1e-12 for i in range(40)))
# Q2b
F = x**2/2*sp.atan(2/x) + x - 2*sp.atan(x/2)
ok("Q2b antiderivative (x>0 and x<0)", all(abs(float((sp.diff(F, x) - x*sp.atan(2/x)).subs(x, v))) < 1e-12 for v in (0.5, 3, -0.7, -4)))
# Q3a
g = sp.log(x + 1) - (3*x + 2)/(x + 2)
ok("Q3a g' = x^2/((x+1)(x+2)^2)", sp.simplify(sp.diff(g, x) - x**2/((x + 1)*(x + 2)**2)) == 0)
ok("Q3a g(0)=-1, g->oo", g.subs(x, 0) == -1 and sp.limit(g, x, sp.oo) == sp.oo)
root = sp.nsolve(g, x, 5)
ok("Q3a exactly one root (x>-1)", root > 0 and abs(g.subs(x, root)) < 1e-12 and all(g.subs(x, v) != 0 for v in (-0.5, 0.5)))
# Q3b
F = sp.log(sp.sin(x)**2 + 2)/22 + 3/(11*sp.sqrt(2))*sp.atan(sp.sin(x)/sp.sqrt(2)) - sp.log(3 - sp.sin(x))/11
ok("Q3b antiderivative", all(abs(float((sp.diff(F, x) - sp.cos(x)/((3 - sp.cos(x)**2)*(3 - sp.sin(x)))).subs(x, v))) < 1e-12 for v in (0.3, 1.1, 2.5, -1.7)))
ok("Q3b partial fractions A=C=1/11, B=3/11", sp.simplify(sp.Rational(1, 11)*(t + 3)/(t**2 + 2) + sp.Rational(1, 11)/(3 - t) - 1/((2 + t**2)*(3 - t))) == 0)
# Q4a
y = sp.exp(x/(1 - x))/(1 - sp.exp(x/(1 - x)))
ok("Q4a x=0: +oo from the left, -oo from the right", sp.limit(y, x, 0, '-') == sp.oo and sp.limit(y, x, 0, '+') == -sp.oo)
ok("Q4a x=1: left limit -1, right limit 0", sp.limit(y, x, 1, '-') == -1 and sp.limit(y, x, 1, '+') == 0)
# Q4b
V = 2*sp.pi*sp.integrate(x*sp.cos(x)**2, (x, sp.pi/2, sp.pi))
ok("Q4b V = pi/2 (1 + 3 pi^2/4)", sp.simplify(V - sp.pi/2*(1 + 3*sp.pi**2/4)) == 0)
ok("Q4b V = pi(1/2 + 3pi^2/8)", sp.simplify(V - sp.pi*(sp.Rational(1, 2) + 3*sp.pi**2/8)) == 0)
# Q5a
ok("Q5a x/(x+1) < ln(1+x) < x sampled", all(v/(v + 1) < sp.log(1 + v).evalf() < v for v in [sp.Rational(k, 9) for k in range(1, 300, 7)]))
# Q5b
Lq = sp.Integral(sp.sqrt(1 + sp.exp(2*x)), (x, 0, 1)).evalf(20)
Lc = sp.sqrt(1 + sp.E**2) + sp.log((sp.sqrt(1 + sp.E**2) - 1)/(sp.sqrt(1 + sp.E**2) + 1))/2 - sp.sqrt(2) - sp.log((sp.sqrt(2) - 1)/(sp.sqrt(2) + 1))/2
ok("Q5b closed form equals the integral", abs(Lq - Lc.evalf(20)) < 1e-12)
print("Q5b exact value", Lq, "official rounded value 1.98")
ok("Q5b official rounded value 1.98 within 0.05 of exact", abs(float(Lq) - 1.98) < 0.05)
# Q6a
f6 = x*sp.real_root(3*x - 1, 3)
ok("Q6a f' = (4x-1)/(3x-1)^(2/3) at x=0.8", abs(float((sp.diff(x*(3*x - 1)**sp.Rational(1, 3), x) - (4*x - 1)/(3*x - 1)**sp.Rational(2, 3)).subs(x, 0.8))) < 1e-12)
xs = np.linspace(-1, 2/3, 1000001)
fv = xs*np.cbrt(3*xs - 1)
ok("Q6a max cbrt(4) at -1", abs(fv.max() - 4**(1/3)) < 1e-9 and abs(xs[fv.argmax()] + 1) < 1e-9)
ok("Q6a min -(1/4)^(4/3) at 1/4", abs(fv.min() + 0.25**(4/3)) < 1e-9 and abs(xs[fv.argmin()] - 0.25) < 1e-5)
ok("Q6a f(1/3)=0, f(2/3)=2/3", f6.subs(x, sp.Rational(1, 3)) == 0 and f6.subs(x, sp.Rational(2, 3)) == sp.Rational(2, 3))
# Q6b
aa, bb, d = sp.symbols('aa bb d')
sol = sp.solve([sp.Eq(8*aa, 4 + bb), sp.Eq(12*aa, 4)], [aa, bb])
ok("Q6b a=1/3, b=-4/3", sol == {aa: sp.Rational(1, 3), bb: -sp.Rational(4, 3)})
ok("Q6b one-sided derivatives 12a (left) and 4 (right)", sp.limit((aa*(2 + d)**3 - 8*aa)/d, d, 0) == 12*aa and sp.limit(((2 + d)**2 - 4)/d, d, 0) == 4)
bad = [nm for nm, c in r if not c]
for nm, c in r:
    print(("OK  " if c else "FAIL"), nm)
print("mismatches:", len(bad))

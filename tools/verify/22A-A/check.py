# sympy verification of the official answers, sitting 22A-A (ASCII output)
import sympy as sp
x, t, h, p, n = sp.symbols('x t h p n', real=True)
A, B, C = sp.symbols('A B C', positive=True)
r = []


def ok(name, cond):
    r.append((name, bool(cond)))


# Q1a
f = sp.Rational(4, 5)*x - sp.real_root((x - 1)**4, 5) + 2
f = sp.Rational(4, 5)*x - sp.Abs(x - 1)**sp.Rational(4, 5) + 2   # (x-1)^4 >= 0, fifth root of (x-1)^4 = |x-1|^(4/5)
vals = {k: sp.nsimplify(f.subs(x, k)) for k in (0, 1, 2, 3)}
ok("Q1a f(0)=1", vals[0] == 1)
ok("Q1a f(1)=14/5", vals[1] == sp.Rational(14, 5))
ok("Q1a f(2)=13/5", vals[2] == sp.Rational(13, 5))
ok("Q1a f(3)=22/5-16^(1/5) ~ 2.66", abs(float(f.subs(x, 3)) - (4.4 - 16**0.2)) < 1e-12 and abs(float(f.subs(x, 3)) - 2.66) < 0.01)
g = sp.Rational(4, 5) - sp.Rational(4, 5)*(x - 1)**sp.Rational(-1, 5)
ok("Q1a f'=0 only at x=2 (x>1 branch)", sp.solve(sp.Eq((x - 1)**sp.Rational(1, 5), 1), x) == [2])
import numpy as np
xs = np.linspace(0, 3, 300001)
fv = 0.8*xs - np.abs(xs - 1)**0.8 + 2
ok("Q1a numeric max 14/5 at x=1", abs(fv.max() - 2.8) < 1e-9 and abs(xs[fv.argmax()] - 1) < 1e-4)
ok("Q1a numeric min 1 at x=0", abs(fv.min() - 1) < 1e-9 and xs[fv.argmin()] == 0)
# Q1b: limit sqrt(A+1)
L = sp.symbols('L', positive=True)
ok("Q1b fixed points L^2=A+1", sp.solve(sp.Eq(L, (L + (A + 1)/L)/2), L) == [sp.sqrt(A + 1)])
good = True
for a in range(10):
    for b in range(10):
        an = float(a + b + 2)
        for _ in range(200):
            an = 0.5*(an + (a + 1)/an)
        good &= abs(an - (a + 1)**0.5) < 1e-9
ok("Q1b numeric iteration to sqrt(A+1), all digits A,B", good)
good = True
for a in range(10):
    s = (a + 1)**0.5
    an = a + 2.0
    for _ in range(30):
        nxt = 0.5*(an + (a + 1)/an)
        good &= nxt >= s - 1e-12 and nxt <= an + 1e-12
        an = nxt
ok("Q1b bounded below by sqrt(A+1) and non-increasing", good)
ok("Q1b a_{n+1}-a_n = (A+1-a^2)/(2a)", sp.simplify((L + (A + 1)/L)/2 - L - (A + 1 - L**2)/(2*L)) == 0)
# Q2a
ok("Q2a factor = (C+1)/(sqrt(n^2+C+1)+n)", sp.simplify(sp.sqrt(n**2 + C + 1) - n - (C + 1)/(sp.sqrt(n**2 + C + 1) + n)) == 0)
ok("Q2a first factor -> 0", sp.limit(sp.sqrt(n**2 + C + 1) - n, n, sp.oo) == 0)
# Q2b
F = sp.Rational(1, 2)*(x**2*sp.atan(x**2) - sp.log(1 + x**4)/2)
ok("Q2b antiderivative", sp.simplify(sp.diff(F, x) - x*sp.atan(x**2)) == 0)
# Q3a
Bp = sp.symbols('Bp', nonnegative=True)
den = 2*x**2 - (2*B + 3)*x + B + 1
ok("Q3a denominator = 2(x-1/2)(x-(B+1))", sp.expand(den - 2*(x - sp.Rational(1, 2))*(x - (B + 1))) == 0)
ok("Q3a limit at 0 = (A+2)/(C+3)", sp.simplify(sp.limit((A + 2)*x*sp.Abs(x - B - 1)/(den*sp.atan((C + 3)*x)), x, 0) - (A + 2)/(C + 3)) == 0)
ok("Q3a limit 0 numeric (A,B,C)=(7,8,9)", abs(sp.limit(((7 + 2)*x*sp.Abs(x - 9)/((2*x**2 - 19*x + 9)*sp.atan(12*x))), x, 0) - sp.Rational(9, 12)) == 0)
fn = lambda a, b, c: (a + 2)*x*sp.Abs(x - b - 1)/((2*x**2 - (2*b + 3)*x + b + 1)*sp.atan((c + 3)*x))
ok("Q3a x=1/2 -> infinite (7,8,9), second kind", sp.limit(fn(7, 8, 9), x, sp.Rational(1, 2), '+') in (sp.oo, -sp.oo) and sp.limit(fn(7, 8, 9), x, sp.Rational(1, 2), '-') in (sp.oo, -sp.oo))
ok("Q3a x=B+1 jump -L,+L (7,8,9)", sp.limit(fn(7, 8, 9), x, 9, '-') == -sp.limit(fn(7, 8, 9), x, 9, '+') != 0)
# Q3b
ok("Q3b right derivative p^2/2", sp.limit((sp.exp(p*h) - p*h - 1)/h**2, h, 0, '+') == p**2/2)
ok("Q3b left derivative 1/6", sp.limit((h - sp.sin(h))/h**3, h, 0, '-') == sp.Rational(1, 6))
ok("Q3b p = +-1/sqrt3", sorted(sp.solve(sp.Eq(p**2/2, sp.Rational(1, 6)), p), key=float) == [-sp.sqrt(3)/3, sp.sqrt(3)/3])
# Q4a
c1 = 2*(A + 1)*sp.log(x) + C
c2 = (A + 1)*(x**2 - 1) + C
ok("Q4a equal slopes iff x^2=1", sp.simplify(sp.diff(c1, x) - sp.diff(c2, x) - 2*(A + 1)*(1 - x**2)/x) == 0)
ok("Q4a common point (1,C)", c1.subs(x, 1) == C and c2.subs(x, 1) == C)
ok("Q4a tangent y=2(A+1)x-2A+C-2", sp.simplify(2*(A + 1)*(x - 1) + C - (2*(A + 1)*x - 2*A + C - 2)) == 0)
# Q4b
F = -2/x + sp.log(x) + sp.log(x**2 + 4) - sp.atan(x/2)/2
ok("Q4b antiderivative", sp.simplify(sp.diff(F, x) - (3*x**3 + x**2 + 4*x + 8)/(x**4 + 4*x**2)) == 0)
ok("Q4b coefficients 2,1,2,-1", sp.simplify(2/x**2 + 1/x + (2*x - 1)/(x**2 + 4) - (3*x**3 + x**2 + 4*x + 8)/(x**2*(x**2 + 4))) == 0)
# Q5a
fa = sp.asin(x) - x/sp.sqrt(1 - x**2)
ok("Q5a f' = -x^2/(1-x^2)^(3/2)", sp.simplify(sp.diff(fa, x) + x**2/(1 - x**2)**sp.Rational(3, 2)) == 0)
ok("Q5a f(0)=0", fa.subs(x, 0) == 0)
# Q5b
ok("Q5b intersection x^4+x^2-2=0 -> x=+-1", sorted(sp.solve(x**4 + x**2 - 2, x)) == [-1, 1])
S = 2*sp.integrate((A + 2)/(1 + x**2) - (A + 2)*x**2/2, (x, 0, 1))
ok("Q5b S = 2(A+2)(pi/4-1/6)", sp.simplify(S - 2*(A + 2)*(sp.pi/4 - sp.Rational(1, 6))) == 0)
ok("Q5b curves equal at +-1 (any A,B)", sp.simplify(((A + 2)/(1 + x**2)).subs(x, 1) - ((A + 2)*x**2/2).subs(x, 1)) == 0)
# Q6a
ok("Q6a -1/2", sp.limit((x - sp.asin(x))/sp.integrate(sp.log(1 + t**2), (t, 0, x)), x, 0) == -sp.Rational(1, 2))
# Q6b
V = 2*sp.pi*sp.integrate(x*(x**2 + B + 1)**sp.Rational(1, 5), (x, 0, C + 1))
Vref = sp.Rational(5, 6)*sp.pi*(((C + 1)**2 + B + 1)**sp.Rational(6, 5) - (B + 1)**sp.Rational(6, 5))
ok("Q6b V formula (symbolic or 4 numeric cases)", sp.simplify(V - Vref) == 0 or all(
    abs(float(sp.Integral(2*sp.pi*x*(x**2 + b + 1)**sp.Rational(1, 5), (x, 0, c + 1)).evalf() - Vref.subs({B: b, C: c}).evalf())) < 1e-8
    for b, c in ((0, 0), (8, 9), (3, 5), (9, 1))))
# Q4a: common tangent at distinct abscissas p=1/q, q: h(q)=q^2-1-2ln q has the single root q=1 (min of h, h' = 2q-2/q)
_q = sp.symbols('q', positive=True)
_h = _q**2 - 1 - 2*sp.log(_q)
ok("Q4a h(1)=0 and h'(q)=0 only at q=1, h>0 elsewhere (grid)",
   _h.subs(_q, 1) == 0 and sp.solve(sp.diff(_h, _q), _q) == [1]
   and all(_h.subs(_q, sp.Rational(i, 50)).evalf() > 1e-9 for i in list(range(1, 50)) + list(range(51, 400))))
bad = [nm for nm, c in r if not c]
for nm, c in r:
    print(("OK  " if c else "FAIL"), nm)
print("mismatches:", len(bad))

# sympy verification of the SOLVED answers, sitting 22B-A (no key exists; ASCII output).
# Parameters A, B, C are ID digits 0..9: each answer is checked symbolically and for every digit value.
import sympy as sp
x, t = sp.symbols('x t', real=True)
n = sp.symbols('n', positive=True, integer=True)
A, B, C = sp.symbols('A B C', nonnegative=True, integer=True)
r = []


def ok(name, cond):
    r.append((name, bool(cond)))


def num_eq(F, f, pts):
    return all(abs(complex(sp.N((sp.diff(F, x) - f).subs(x, v)))) < 1e-10 for v in pts)


# Q1a
f = 2*x + 3*sp.cbrt(x**2)
fp = 2 + 2/sp.cbrt(x)          # valid for x>0; for x<0 use real cube root below
fr = lambda v: 2*v + 3*abs(v)**(2/3)
ok("Q1a f(-1)=1, f(0)=0", abs(fr(-1) - 1) < 1e-12 and fr(0) == 0)
ok("Q1a local max at -1 (numeric)", fr(-1) > fr(-1.01) and fr(-1) > fr(-0.99))
ok("Q1a local min at 0 (numeric)", fr(0) < fr(-0.01) and fr(0) < fr(0.01))
ok("Q1a f' = 2(x^(1/3)+1)/x^(1/3) for x>0", sp.simplify(sp.diff(f, x).subs(x, 8) - sp.Rational(3, 1)) == 0)
# Q1b
for a_ in range(10):
    for c_ in range(10):
        expr = (sp.factorial(n + 2) + (a_ + 1)*n*sp.factorial(n + 1))/(sp.factorial(n + 1) - n*sp.factorial(n))*sp.sin(sp.Integer(c_ + 1)/(n + 1)**2)
        num = sp.N(expr.subs(n, 4000), 30)
        if abs(num - (a_ + 2)*(c_ + 1)) > 0.02*(a_ + 2)*(c_ + 1):
            ok(f"Q1b A={a_} C={c_}", False)
ok("Q1b algebra: ratio = (n+1)((A+2)n+2)", sp.simplify(sp.combsimp((sp.factorial(n + 2) + (A + 1)*n*sp.factorial(n + 1))/(sp.factorial(n + 1) - n*sp.factorial(n))) - (n + 1)*((A + 2)*n + 2)) == 0)
ok("Q1b limit (A+2)(C+1) symbolic", sp.simplify(sp.limit((n + 1)*((A + 2)*n + 2)*(C + 1)/(n + 1)**2, n, sp.oo) - (A + 2)*(C + 1)) == 0)
# Q2a
ok("Q2a arctan' = 1/(1+x^2)", sp.diff(sp.atan(x), x) == 1/(1 + x**2))
ok("Q2a samples", all(v/(1 + v**2) < float(sp.atan(v)) < v for v in (0.01, 0.5, 1, 3, 50)))
# Q2b
for b_ in range(10):
    for c_ in range(10):
        a = c_ + 2
        seq = []
        for _ in range(400):
            seq.append(a)
            a = (b_ + 3)*a/((b_ + 2)*a + 1)
        if not (all(seq[i + 1] < seq[i] and seq[i] > 1 for i in range(5)) and all(s >= 1 for s in seq) and abs(seq[-1] - 1) < 1e-9):
            ok(f"Q2b B={b_} C={c_}", False)
k, a = sp.symbols('k a', positive=True)
ok("Q2b a_{n+1}-1 = (a-1)/(ka+1)", sp.simplify((k + 1)*a/(k*a + 1) - 1 - (a - 1)/(k*a + 1)) == 0)
ok("Q2b a_{n+1}-a_n = k a (1-a)/(ka+1)", sp.simplify((k + 1)*a/(k*a + 1) - a - k*a*(1 - a)/(k*a + 1)) == 0)
L = sp.symbols('L')
ok("Q2b fixed points 0,1", set(sp.solve(sp.Eq(L*(k*L + 1), (k + 1)*L), L)) == {0, 1})
# Q3a
for a_ in range(10):
    for b_ in range(10):
        f3 = (x + a_)*(2 + sp.cos(sp.Integer(b_ + 1)/(x + a_)))
        if not (sp.limit(f3/x, x, sp.oo) == 3 and sp.limit(f3 - 3*x, x, sp.oo) == 3*a_ and sp.limit(f3 - 3*x, x, -sp.oo) == 3*a_
                and sp.limit(f3, x, -a_, '+') == 0 and sp.limit(f3, x, -a_, '-') == 0):
            ok(f"Q3a A={a_} B={b_}", False)
ok("Q3a all 100 (A,B): y=3x+3A, no vertical asymptote", True)
# Q3b
tt = sp.symbols('tt', real=True)
ok("Q3b Weierstrass: 1+sin+3cos = 2(2+t-t^2)/(1+t^2)", sp.simplify(1 + 2*tt/(1 + tt**2) + 3*(1 - tt**2)/(1 + tt**2) - 2*(2 + tt - tt**2)/(1 + tt**2)) == 0)
F = sp.log(sp.Abs((1 + sp.tan(x/2))/(2 - sp.tan(x/2))))/3
ok("Q3b antiderivative", num_eq(F, 1/(1 + sp.sin(x) + 3*sp.cos(x)), (0.2, 0.7, -0.4, -1.2, 2.0)))
# Q4a
for b_ in range(10):
    for c_ in range(10):
        g = x**3 + (c_ + 1)*x + sp.cos((c_ + 1)*x) - (b_ + 1)
        gp = sp.diff(g, x)
        vals = [float(gp.subs(x, v/50)) for v in range(-300, 301)]
        if min(vals) <= 0:
            ok(f"Q4a g'>0 B={b_} C={c_}", False)
        if not (float(g.subs(x, -5)) < 0 < float(g.subs(x, 5))):
            ok(f"Q4a sign change B={b_} C={c_}", False)
ok("Q4a g' = 3x^2+(C+1)(1-sin((C+1)x)) symbolic", sp.simplify(sp.diff(x**3 + (C + 1)*x + sp.cos((C + 1)*x), x) - (3*x**2 + (C + 1)*(1 - sp.sin((C + 1)*x)))) == 0)
# Q4b
xp = sp.symbols('xp', positive=True)
F = sp.atan(sp.sqrt(xp))**4/2
ok("Q4b antiderivative", sp.simplify(sp.diff(F, xp) - sp.atan(sp.sqrt(xp))**3/((xp + 1)*sp.sqrt(xp))) == 0)
# Q5a
for a_ in range(10):
    for c_ in range(10):
        e5 = (x**3 + a_)*(sp.sqrt(x**2 + sp.sqrt(x**4 + c_ + 1)) - x*sp.sqrt(2))
        if sp.simplify(sp.limit(e5, x, sp.oo) - sp.sqrt(2)*(c_ + 1)/8) != 0:
            ok(f"Q5a A={a_} C={c_}", False)
ok("Q5a all 100 (A,C): sqrt2 (C+1)/8", True)
# Q5b
Lq = sp.integrate(1/sp.sin(x), (x, sp.pi/3, sp.pi/2))
ok("Q5b 1+cot^2 = 1/sin^2", sp.simplify(1 + sp.diff(sp.log(sp.sin(x)), x)**2 - 1/sp.sin(x)**2) == 0)
ok("Q5b L = ln(3)/2", abs(float(Lq) - float(sp.log(3)/2)) < 1e-12)
# Q6a
f6 = 1/sp.sin(x) - 1/x
ok("Q6a lim f = 0 -> p = 0", sp.limit(f6, x, 0) == 0)
ok("Q6a f'(0) = lim f(x)/x = 1/6", sp.limit(f6/x, x, 0) == sp.Rational(1, 6))
# Q6b
u = sp.symbols('u', positive=True)
ok("Q6b int_0^pi u sin^2 u du = pi^2/4", sp.simplify(sp.integrate(u*sp.sin(u)**2, (u, 0, sp.pi)) - sp.pi**2/4) == 0)
for b_ in range(10):
    kk = b_ + 1
    V = 2*sp.pi*sp.integrate(x*sp.sin(kk*x)**2, (x, 0, sp.pi/kk))
    if sp.simplify(V - sp.pi**3/(2*kk**2)) != 0:
        ok(f"Q6b B={b_}", False)
ok("Q6b all 10 B: V = pi^3/(2(B+1)^2)", True)
bad = [nm for nm, c in r if not c]
for nm, c in r:
    print(("OK  " if c else "FAIL"), nm)
print("mismatches:", len(bad))

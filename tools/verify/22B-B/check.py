# sympy verification of the official answers, sitting 22B-B (ASCII output)
import sympy as sp
x, t, z = sp.symbols('x t z', real=True)
r = []


def ok(name, cond):
    r.append((name, bool(cond)))


# Q1
f = x*sp.exp(1 - 2*x**2)
d1, d2 = sp.diff(f, x), sp.diff(f, x, 2)
ok("Q1 f' = e^(1-2x^2)(1-4x^2)", sp.simplify(d1 - sp.exp(1 - 2*x**2)*(1 - 4*x**2)) == 0)
ok("Q1 f'' = 4x e^(1-2x^2)(4x^2-3)", sp.simplify(d2 - 4*x*sp.exp(1 - 2*x**2)*(4*x**2 - 3)) == 0)
ok("Q1 f(1/2)=sqrt(e)/2, f(-1/2)=-sqrt(e)/2", sp.simplify(f.subs(x, sp.Rational(1, 2)) - sp.sqrt(sp.E)/2) == 0 and sp.simplify(f.subs(x, -sp.Rational(1, 2)) + sp.sqrt(sp.E)/2) == 0)
sg = lambda e, v: sp.sign(e.subs(x, v))
ok("Q1 f' signs - + -", [sg(d1, -1), sg(d1, 0), sg(d1, 1)] == [-1, 1, -1])
ok("Q1 f'' signs - + - +", [sg(d2, -2), sg(d2, -sp.Rational(1, 2)), sg(d2, sp.Rational(1, 2)), sg(d2, 2)] == [-1, 1, -1, 1])
ok("Q1 f'' zeros 0, +-sqrt3/2", sorted(sp.solve(d2, x), key=float) == [-sp.sqrt(3)/2, 0, sp.sqrt(3)/2])
ok("Q1 asymptote y=0 both sides", sp.limit(f, x, sp.oo) == 0 and sp.limit(f, x, -sp.oo) == 0 and sp.limit(f/x, x, sp.oo) == 0)
# Q2a
an = 1.0
s = []
for _ in range(80):
    s.append(an)
    an = 2*an/(an + 3)
ok("Q2a a2=1/2, decreasing, positive, limit 0", s[1] == 0.5 and all(s[i + 1] < s[i] and s[i] > 0 for i in range(79)) and s[-1] < 1e-12)
L = sp.symbols('L')
ok("Q2a fixed points 0 and -1", sorted(sp.solve(sp.Eq(L, 2*L/(L + 3)), L)) == [-1, 0])
# Q2b
tt = sp.symbols('tt', real=True)
ok("Q2b universal substitution gives 2(t-2)^2/(1+t^2)", sp.simplify(5 - 4*2*tt/(1 + tt**2) + 3*(1 - tt**2)/(1 + tt**2) - 2*(tt - 2)**2/(1 + tt**2)) == 0)
F = 1/(2 - sp.tan(x/2))
ok("Q2b antiderivative", all(abs(float((sp.diff(F, x) - 1/(5 - 4*sp.sin(x) + 3*sp.cos(x))).subs(x, v))) < 1e-12 for v in (0.2, 0.9, 1.3, -1.1, 2.4)))
# Q3
ok("Q3a arcsin MVT bounds sampled", all(
    (bb - aa)/sp.sqrt(1 - aa**2) <= sp.asin(bb) - sp.asin(aa) <= (bb - aa)/sp.sqrt(1 - bb**2)
    for aa, bb in [(sp.Rational(1, 10), sp.Rational(1, 5)), (sp.Rational(1, 3), sp.Rational(9, 10)), (sp.Rational(1, 100), sp.Rational(99, 100)), (sp.Rational(1, 2), sp.Rational(3, 5))]))
V = sp.pi*sp.integrate(x*sp.log(x), (x, 1, sp.E))
ok("Q3b V = pi/4 (e^2+1)", sp.simplify(V - sp.pi/4*(sp.E**2 + 1)) == 0)
# Q4
ok("Q4a limit -1/6", sp.limit((x - sp.integrate(sp.cos(t**2), (t, 0, x**2)))/(x**3 - 6*x), x, 0) == -sp.Rational(1, 6))
Lr = sp.integrate(sp.sqrt(1 + sp.Rational(9, 4)*x), (x, 0, 1))
ok("Q4b L = 8/27((13/4)^(3/2)-1)", sp.simplify(Lr - sp.Rational(8, 27)*((sp.Rational(13, 4))**sp.Rational(3, 2) - 1)) == 0)
ok("Q4b equals numeric integral of sqrt(1+f'^2)", abs(float(Lr) - float(sp.Integral(sp.sqrt(1 + sp.diff(x**sp.Rational(3, 2), x)**2), (x, 0, 1)).evalf())) < 1e-9)
# Q5
f5 = 2*x**3 + 3*sp.atan(x) + sp.exp(x) + 1
ok("Q5a f(0)=2>0, f(-1)<0, f'>0", f5.subs(x, 0) == 2 and f5.subs(x, -1).evalf() < 0 and sp.simplify(sp.diff(f5, x) - (6*x**2 + 3/(1 + x**2) + sp.exp(x))) == 0)
aa = sp.symbols('aa', positive=True)
ok("Q5b tangent from origin at a=2", sp.solve(sp.Eq(1/(2*sp.sqrt(aa - 1)), sp.sqrt(aa - 1)/aa), aa) == [2])
S = sp.Rational(2*1, 2) - sp.integrate(sp.sqrt(x - 1), (x, 1, 2))
ok("Q5b S = 1/3", S == sp.Rational(1, 3))
# Q6
F = sp.log(sp.Abs(x + 1))/2 - sp.log(x**2 + 4*x + 5)/4 - sp.atan(x + 2)/2
ok("Q6a antiderivative", all(abs(float((sp.diff(F, x) - 1/((x + 1)*(x**2 + 4*x + 5))).subs(x, v))) < 1e-12 for v in (0.3, 1.7, -0.4, -3.2)))
ok("Q6a partial fractions 1/2, -1/2, -3/2", sp.simplify(sp.Rational(1, 2)/(x + 1) + (-x/2 - sp.Rational(3, 2))/(x**2 + 4*x + 5) - 1/((x + 1)*(x**2 + 4*x + 5))) == 0)
y = sp.log(1 + x)
ok("Q6b T2 = x - x^2/2", sp.series(y, x, 0, 3).removeO() == x - x**2/2)
ok("Q6b y''' = 2/(1+x)^3", sp.simplify(sp.diff(y, x, 3) - 2/(1 + x)**3) == 0)
base = 1/(3*sp.Rational(9, 10)**3)
bound_correct = base*sp.Rational(1, 10)**3
bound_official = base*sp.Rational(1, 100)**3
print("Q6b bound with |x|<=0.1:", float(bound_correct), " official prints (0.01)^3 ->", float(bound_official))
ok("Q6b official 4.57e-7 equals the (0.01)^3 arithmetic", abs(float(bound_official) - 4.57e-7) < 1e-9)
ok("Q6b the printed interval |x|<=0.1 gives 4.57e-4, NOT the official 4.57e-7 (key disagrees)", abs(float(bound_correct) - 4.57e-4) < 1e-6)
bad = [nm for nm, c in r if not c]
for nm, c in r:
    print(("OK  " if c else "FAIL"), nm)
print("mismatches:", len(bad))

# sympy verification of the SOLVED answers, sitting 25B-B (no key exists; ASCII output)
import sympy as sp
x, t = sp.symbols('x t', real=True)
r = []


def ok(name, cond):
    r.append((name, bool(cond)))


def num_eq(F, f, pts):
    return all(abs(complex(sp.N((sp.diff(F, x) - f).subs(x, v)))) < 1e-10 for v in pts)


# Q1 f = x e^(1/(x-2))
f = x*sp.exp(1/(x - 2))
d1, d2 = sp.diff(f, x), sp.diff(f, x, 2)
ok("Q1 f' = e^(1/(x-2)) (x-1)(x-4)/(x-2)^2", sp.simplify(d1 - sp.exp(1/(x - 2))*(x - 1)*(x - 4)/(x - 2)**2) == 0)
ok("Q1 f'' = e^(1/(x-2)) (5x-8)/(x-2)^4", sp.simplify(d2 - sp.exp(1/(x - 2))*(5*x - 8)/(x - 2)**4) == 0)
sg = lambda e, v: sp.sign(sp.N(e.subs(x, v)))
ok("Q1 f' signs + - - +", [sg(d1, 0), sg(d1, 1.5), sg(d1, 3), sg(d1, 5)] == [1, -1, -1, 1])
ok("Q1 f'' signs - + +", [sg(d2, 1), sg(d2, 1.8), sg(d2, 3)] == [-1, 1, 1])
ok("Q1 f(1)=1/e, f(4)=4 sqrt(e), f(8/5)=8/5 e^(-5/2)", f.subs(x, 1) == sp.exp(-1) and sp.simplify(f.subs(x, 4) - 4*sp.sqrt(sp.E)) == 0
   and sp.simplify(f.subs(x, sp.Rational(8, 5)) - sp.Rational(8, 5)*sp.exp(-sp.Rational(5, 2))) == 0)
ok("Q1 x->2+ : +oo, x->2- : 0", sp.limit(f, x, 2, '+') == sp.oo and sp.limit(f, x, 2, '-') == 0)
ok("Q1 oblique y = x+1 both sides", all(sp.limit(f/x, x, s) == 1 and sp.limit(f - x, x, s) == 1 for s in (sp.oo, -sp.oo)))
# Q2a
a = sp.sqrt(20.0)
seq = []
for _ in range(60):
    seq.append(a)
    a = (20 + a)**0.5
ok("Q2a increasing, below 5, limit 5", all(seq[i] < seq[i + 1] < 5 for i in range(10)) and all(s <= 5 for s in seq) and abs(seq[-1] - 5) < 1e-12)
L = sp.symbols('L')
ok("Q2a fixed points 5, -4", sorted(sp.solve(L**2 - L - 20, L)) == [-4, 5])
# Q2b
F = (2*x**2 + 6*x + 2)*sp.atan(x) - 2*x - 3*sp.log(1 + x**2)
ok("Q2b antiderivative", sp.simplify(sp.diff(F, x) - (4*x + 6)*sp.atan(x)) == 0)
# Q3a
ok("Q3a limit = 1", sp.limit((1/x)**sp.tan(2*x), x, 0, '+') == 1)
ok("Q3a tan2x ln x -> 0", sp.limit(sp.tan(2*x)*sp.log(x), x, 0, '+') == 0)
# Q3b
y = sp.tan(x)**sp.cos(x)
p = sp.pi/4
ok("Q3b y(pi/4)=1, y'(pi/4)=sqrt2", abs(sp.N(y.subs(x, p)) - 1) < 1e-12 and abs(sp.N(sp.diff(y, x).subs(x, p) - sp.sqrt(2))) < 1e-12)
# Q4a
ok("Q4a limit = 3", sp.limit((sp.sqrt(x + 2) - sp.sqrt(3*x - 2))/(sp.sqrt(4*x + 1) - sp.sqrt(5*x - 1)), x, 2) == 3)
# Q4b
tan_line = 4*x - 4
ok("Q4b tangent y=4x-4", sp.expand(4 + 4*(x - 2) - tan_line) == 0)
S = sp.integrate(x**2, (x, 0, 2)) - sp.integrate(tan_line, (x, 1, 2))
S2 = sp.integrate(x**2, (x, 0, 1)) + sp.integrate(x**2 - tan_line, (x, 1, 2))
ok("Q4b area 2/3 (two ways)", S == sp.Rational(2, 3) and S2 == sp.Rational(2, 3))
# Q5a
g = sp.exp(sp.sin(x)**2)
gp = sp.diff(g, x)
ok("Q5a g' = e^(sin^2 x) sin 2x", sp.simplify(gp - sp.exp(sp.sin(x)**2)*sp.sin(2*x)) == 0)
import random
random.seed(1)
ok("Q5a |g'| <= e on samples", all(abs(float(gp.subs(x, random.uniform(-20, 20)))) <= float(sp.E) for _ in range(400)))
ok("Q5a inequality on random a<b", all(
    float(g.subs(x, bb) - g.subs(x, aa)) <= float(sp.E*(bb - aa)) + 1e-12
    for aa, bb in [sorted((random.uniform(-9, 9), random.uniform(-9, 9))) for _ in range(300)]))
# Q5b
F = -sp.atan((sp.cos(x) + 1)/2)/2
ok("Q5b antiderivative", num_eq(F, sp.sin(x)/(5 + 2*sp.cos(x) + sp.cos(x)**2), (0.3, 1.1, 2.5, -0.7, 4.0)))
# Q6a
V = sp.pi*sp.integrate((25 - x**2) - 9, (x, -4, 4))
ok("Q6a V = 256 pi / 3", sp.simplify(V - 256*sp.pi/3) == 0)
# Q6b
aa = sp.symbols('a', real=True)
left = sp.limit(sp.sin(aa*x)/x, x, 0, '-')
right = sp.limit(x**2*sp.log(x)/x, x, 0, '+')
ok("Q6b continuity at 0 for every a", sp.limit(x**2*sp.log(x), x, 0, '+') == 0)
ok("Q6b f'_-(0)=a, f'_+(0)=0 -> a=0", sp.simplify(left - aa) == 0 and right == 0)
bad = [nm for nm, c in r if not c]
for nm, c in r:
    print(("OK  " if c else "FAIL"), nm)
print("mismatches:", len(bad))

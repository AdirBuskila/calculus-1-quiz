# sympy verification of the official answers, sitting 24A-B (ASCII output)
import sympy as sp
x, y, n, L, a = sp.symbols('x y n L a', real=True)
s = sp.Symbol('s')
r = []


def ok(name, cond):
    r.append((name, bool(cond)))


# Q1
f = x**2*sp.exp(x)
ok("Q1 f'", sp.simplify(sp.diff(f, x) - (2*x + x**2)*sp.exp(x)) == 0)
ok("Q1 critical points 0,-2", sorted(sp.solve(sp.diff(f, x), x)) == [-2, 0])
ok("Q1 f'' = e^x(x^2+4x+2)", sp.simplify(sp.diff(f, x, 2) - sp.exp(x)*(x**2 + 4*x + 2)) == 0)
ok("Q1 inflection -2+-sqrt2", sorted(sp.solve(x**2 + 4*x + 2, x), key=sp.N) == [-2 - sp.sqrt(2), -2 + sp.sqrt(2)])
ok("Q1 f''(0)>0 (min), f''(-2)<0 (max)", sp.diff(f, x, 2).subs(x, 0) > 0 and sp.diff(f, x, 2).subs(x, -2) < 0)
ok("Q1 f/x -> +oo", sp.limit(f/x, x, sp.oo) == sp.oo)
ok("Q1 lim -oo = 0", sp.limit(f, x, -sp.oo) == 0)
# Q2a
g = (x**2 + 2*x + 3)/((x - 1)*(x**2 + 4*x + 4))
ok("Q2a decomposition", sp.simplify(sp.Rational(2, 3)/(x - 1) + sp.Rational(1, 3)/(x + 2) - 1/(x + 2)**2 - g) == 0)
F = sp.Rational(2, 3)*sp.log(x - 1) + sp.Rational(1, 3)*sp.log(x + 2) + 1/(x + 2)
ok("Q2a antiderivative", sp.simplify(sp.diff(F, x) - g) == 0)
# Q2b
seq = [sp.Integer(4)]
for i in range(30):
    seq.append(sp.sqrt(seq[-1] + 20))
ok("Q2b a2 = sqrt24, increasing, bounded by 5", seq[1] == sp.sqrt(24) and all(seq[i] <= seq[i + 1] for i in range(30)) and all(v <= 5 for v in seq))
ok("Q2b L^2-L-20 roots -4, 5", sorted(sp.solve(sp.Eq(L**2 - L - 20, 0), L)) == [-4, 5])
ok("Q2b numerically -> 5", abs(seq[-1].evalf() - 5) < 1e-6)
# Q3a
ok("Q3a e^2", sp.limit(((n**2 + 5*n - 2)/(n**2 + 3*n - 2))**n, n, sp.oo) == sp.exp(2))
ok("Q3a rewrite", sp.simplify(1 + 2*n/(n**2 + 3*n - 2) - (n**2 + 5*n - 2)/(n**2 + 3*n - 2)) == 0 and sp.simplify(2*n/(n**2 + 3*n - 2) - 2/(n + 3 - 2/n)) == 0)
# Q3b
ok("Q3b intersection x=4", sp.solve(sp.Eq(x - 2, 4 - sp.sqrt(x)), x) == [4])
Vw = sp.pi*sp.integrate((4 - sp.sqrt(x))**2 - (x - 2)**2, (x, 2, 4))
ok("Q3b washers ~ 7.752 pi", abs(sp.N(Vw/sp.pi) - 7.752) < 5e-4)
ok("Q3b washer integrand expansion", sp.expand((4 - sp.sqrt(x))**2 - (x - 2)**2 - (16 - 8*sp.sqrt(x) + x - x**2 + 4*x - 4)) == 0)
Vs = 2*sp.pi*(sp.integrate(((4 - y)**2 - 2)*y, (y, 2, 4 - sp.sqrt(2))) + sp.integrate(y*y, (y, 0, 2)))
ok("Q3b shells == washers", sp.simplify(Vs - Vw) == 0)
ok("Q3b shell integrand 14y-8y^2+y^3", sp.expand(((4 - y)**2 - 2)*y - (14*y - 8*y**2 + y**3)) == 0)
ok("Q3b ~ 24.352", abs(sp.N(Vw) - 24.352) < 2e-3)
# Q4a
h = x*sp.exp(1/x)
ok("Q4a h'", sp.simplify(sp.diff(h, x) - sp.exp(1/x)*(x - 1)/x) == 0)
vals = [h.subs(x, sp.Rational(1, 2)), h.subs(x, 1), h.subs(x, 3)]
ok("Q4a values 3.694, 2.718, 4.187", abs(sp.N(vals[0]) - 3.694) < 1e-3 and abs(sp.N(vals[1]) - 2.718) < 1e-3 and abs(sp.N(vals[2]) - 4.187) < 1e-3)
ok("Q4a max 3e^(1/3), min e", max(vals, key=sp.N) == 3*sp.exp(sp.Rational(1, 3)) and min(vals, key=sp.N) == sp.E)
# Q4b
k = sp.sqrt(2 - 2*x)
ok("Q4b slope -1/2 at x=-1, f(-1)=2", sp.solve(sp.Eq(sp.diff(k, x), -sp.Rational(1, 2)), x) == [-1] and k.subs(x, -1) == 2)
tang = sp.Rational(3, 2) - x/2
ok("Q4b tangent y=1.5-0.5x with x-intercept 3", sp.simplify(2 - sp.Rational(1, 2)*(x + 1) - tang) == 0 and sp.solve(tang, x) == [3])
ok("Q4b area 4/3", sp.integrate(tang - k, (x, -1, 1)) + sp.integrate(tang, (x, 1, 3)) == sp.Rational(4, 3))
ok("Q4b area 4/3 (second form)", sp.integrate(tang, (x, -1, 3)) - sp.integrate(k, (x, -1, 1)) == sp.Rational(4, 3))
# Q5a
ok("Q5a", sp.simplify(sp.diff(sp.log(sp.log(x)**2 + 1)/2, x) - sp.log(x)/(x*(sp.log(x)**2 + 1))) == 0)
# Q5b
ok("Q5b b=2", sp.limit(sp.atan(2*x)/x, x, 0, '-') == 2)
ok("Q5b right limit at 2 = 1", sp.limit(4*(x - sp.sqrt(3*x - 2))/(x - 2), x, 2, '+') == 1)
ok("Q5b a=-1/2", sp.solve(sp.Eq(2*a + 2, 1), a) == [-sp.Rational(1, 2)])
ok("Q5b factorization", sp.simplify(4*(x - sp.sqrt(3*x - 2))/(x - 2) - 4*(x - 1)/(x + sp.sqrt(3*x - 2))) == 0)
# Q6a
f6 = 2**sp.sqrt(x) + sp.atan(2*x) - 5
ok("Q6a f(0) = -4 (2^0 = 1)", f6.subs(x, 0) == -4)
ok("Q6a f' formula", sp.simplify(sp.diff(f6, x) - (2**sp.sqrt(x)*sp.log(2)/(2*sp.sqrt(x)) + 2/(1 + 4*x**2))) == 0)
ok("Q6a limit +oo", sp.limit(f6, x, sp.oo) == sp.oo)
# Q6b
den = sp.integrate(s*sp.cos(s**2), (s, 0, x**2))
ok("Q6b limit +oo", sp.limit(sp.sin(x)**2/den, x, 0, '+') == sp.oo)
ok("Q6b L'Hopital step", sp.simplify(sp.diff(sp.sin(x)**2, x)/sp.diff(den, x) - 2*sp.sin(x)*sp.cos(x)/(2*x*x**2*sp.cos(x**4))) == 0)
for kk, v in r:
    print(kk, "OK" if v else "MISMATCH")
print("ALL OK" if all(v for _, v in r) else "FAIL")
# Q6b mismatch probe: the PRINTED limit (numerator x^4) vs the official solution's limit (numerator sin^2 x)
printed = sp.limit(x**4/den, x, 0, '+')
print("Q6b printed limit (x^4 numerator) =", printed, "| official solution computes sin^2 x numerator = +oo -> labeled fix ships 2")
assert printed == 2, "Q6b printed limit must be 2"
assert sp.simplify(sp.diff(x**4, x)/sp.diff(den, x) - 2/sp.cos(x**4)) == 0, "Q6b solver L'Hopital step"
print("Q6b solver answer 2: OK")

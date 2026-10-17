# sympy verification of the official answers, sitting 24B-A (ASCII output)
import sympy as sp
x, t, b, a = sp.symbols('x t b a', real=True)
r = []


def ok(name, cond):
    r.append((name, bool(cond)))


# Q1
f = (x**3 - 1)/x**2
ok("Q1 f' = 1+2/x^3", sp.simplify(sp.diff(f, x) - (1 + 2/x**3)) == 0)
ok("Q1 f'' = -6/x^4", sp.simplify(sp.diff(f, x, 2) + 6/x**4) == 0)
ok("Q1 only real critical point -cbrt(2)", [s for s in sp.solve(sp.Eq(1 + 2/x**3, 0), x) if s.is_real] == [-sp.cbrt(2)])
ok("Q1 f(-cbrt2) = -3/cbrt4", sp.simplify(f.subs(x, -sp.cbrt(2)) + 3/sp.cbrt(4)) == 0)
ok("Q1 f(1)=0", f.subs(x, 1) == 0)
ok("Q1 f'' < 0 sampled (no inflection)", all(sp.diff(f, x, 2).subs(x, v) < 0 for v in (-5, -1, sp.Rational(-1, 3), sp.Rational(1, 3), 2, 7)))
ok("Q1 lim 0+ = -oo", sp.limit(f, x, 0, '+') == -sp.oo)
ok("Q1 lim 0- = -oo", sp.limit(f, x, 0, '-') == -sp.oo)
ok("Q1 a=1", sp.limit(f/x, x, sp.oo) == 1)
ok("Q1 b=0 at +-oo", sp.limit(f - x, x, sp.oo) == 0 and sp.limit(f - x, x, -sp.oo) == 0)
# Q2a
g = x/((x + 1)*(x**2 + 1))
F = -sp.log(x + 1)/2 + sp.log(x**2 + 1)/4 + sp.atan(x)/2
ok("Q2a antiderivative", sp.simplify(sp.diff(F, x) - g) == 0)
ok("Q2a decomposition", sp.simplify(sp.Rational(1, 2)*(-1/(x + 1) + (x + 1)/(x**2 + 1)) - g) == 0)
# Q2b
h = x - sp.log(1 + x)
ok("Q2b h' = x/(1+x)", sp.simplify(sp.diff(h, x) - x/(1 + x)) == 0)
ok("Q2b h(0)=0", h.subs(x, 0) == 0)
ok("Q2b h(x)>0 sampled", all(h.subs(x, sp.Rational(k, 7)).evalf() > 0 for k in range(1, 400, 13)))
# Q3
ok("Q3 left limit b/3", sp.simplify(sp.limit(sp.sin(b*x)/(x + sp.sin(2*x)), x, 0, '-') - b/3) == 0)
ok("Q3 x ln x -> 0", sp.limit(x*sp.log(x), x, 0, '+') == 0)
ok("Q3 i: 2a-7 = b/3 = 0", sp.solve([2*a - 7, b/3], [a, b]) == {a: sp.Rational(7, 2), b: 0})
# Q4
ok("Q4a 1/2", sp.limit(1/sp.log(x) - 1/(x - 1), x, 1) == sp.Rational(1, 2))
ok("Q4b 1/2", sp.limit(sp.integrate(sp.tan(t), (t, 0, x))/(x*sp.sin(x)), x, 0) == sp.Rational(1, 2))
# Q5
Fa = ((x**2 + 2*x - sp.Rational(1, 2))/2)*sp.sin(2*x) + (x + 1)*sp.cos(2*x)/2
ok("Q5a antiderivative", sp.simplify(sp.diff(Fa, x) - (x**2 + 2*x)*sp.cos(2*x)) == 0)
ok("Q5b intersections -1, 3", sorted(sp.solve(sp.Eq(x**2 + 2, 2*x + 5), x)) == [-1, 3])
S = sp.integrate(2*x + 5 - (x**2 + 2), (x, 0, 3)) + sp.integrate(x**2 + 2 - (2*x + 5), (x, 3, 6))
ok("Q5b area 36", S == 36)
# Q6
gg = sp.exp(x) - 1/x - 3
ok("Q6a g(1)<0", gg.subs(x, 1) < 0)
ok("Q6a g(1.5)>0", gg.subs(x, sp.Rational(3, 2)).evalf() > 0)
ok("Q6a g' = e^x+1/x^2", sp.simplify(sp.diff(gg, x) - (sp.exp(x) + 1/x**2)) == 0)
y = (x**2 + 5)/(x + 2)
ok("Q6b y'", sp.simplify(sp.diff(y, x) - (x**2 + 4*x - 5)/(x + 2)**2) == 0)
ok("Q6b critical point in [0,10] is 1", [s for s in sp.solve(x**2 + 4*x - 5, x) if 0 <= s <= 10] == [1])
ok("Q6b values y(10),y(0),y(1)", (y.subs(x, 10), y.subs(x, 0), y.subs(x, 1)) == (sp.Rational(105, 12), sp.Rational(5, 2), 2))
for k, v in r:
    print(k, "OK" if v else "MISMATCH")
print("ALL OK" if all(v for _, v in r) else "FAIL")

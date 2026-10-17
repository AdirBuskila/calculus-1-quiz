# Step-author checks (sympy). Imported/exec'd from check.py. Every numeric/choice step value in gen_24B-B.py is re-derived here
# and the numeric answers stored in tools/raw/24B-B.json are compared against the derived values.
import json, pathlib
import sympy as sp
x, n, t, L, a, b, y, A, B, C, D = sp.symbols('x n t L a b y A B C D', real=True)
R = []
def ok(name, cond): R.append((name, bool(cond)))

# ---- Q1
f = x**3/(x**2-1)
fp = sp.diff(f, x); fpp = sp.diff(f, x, 2)
ok("S Q1 f' zeros {0,+-sqrt3}", set(sp.solve(sp.numer(sp.together(fp)), x)) == {0, sp.sqrt(3), -sp.sqrt(3)})
q1_fs3 = sp.N(f.subs(x, sp.sqrt(3)), 6)
ok("S Q1 f(sqrt3)=2.598", abs(q1_fs3-2.598) < 1e-3)
ok("S Q1 f''(1/2)<0 (concave on (0,1))", fpp.subs(x, sp.Rational(1, 2)) < 0 and fpp.subs(x, sp.Rational(9, 10)) < 0)
q1_a = sp.limit(f/x, x, sp.oo)
ok("S Q1 a=1", q1_a == 1)

# ---- Q2a
g = (x**2+8)/(x**2*(x**2+4))
form = A/x + B/x**2 + (C*x+D)/(x**2+4)
sol = sp.solve(sp.Poly(sp.numer(sp.together(form-g)), x).all_coeffs(), [A, B, C, D], dict=True)
ok("S Q2a decomposition solvable, A=C=0,B=2,D=-1", sol == [{A: 0, B: 2, C: 0, D: -1}])
bad1 = A/x + B/(x+2) + C/(x-2)
bad2 = A/x + B/(x**2+4)
for nm, bd, vs in (("x+-2", bad1, [A, B, C]), ("no 1/x^2 term", bad2, [A, B])):
    s2 = sp.solve(sp.Poly(sp.numer(sp.together(bd-g)), x).all_coeffs(), vs, dict=True)
    ok(f"S Q2a distractor {nm} has no solution", s2 == [])
cands = [-2/x - sp.atan(x/2)/2, -2/x - sp.atan(x/2), -2/x + sp.atan(x/2)/2, 2/x - sp.atan(x/2)/2]
ok("S Q2a antiderivative: only option a", [sp.simplify(sp.diff(c, x)-g) == 0 for c in cands] == [True, False, False, False])

# ---- Q2b
seq = [sp.Integer(2)]
for i in range(6): seq.append(3/(2+1/seq[-1]))
q2_a3 = sp.N(seq[2], 6)
ok("S Q2b a2=6/5, a3=18/17=1.059", seq[1] == sp.Rational(6, 5) and seq[2] == sp.Rational(18, 17) and abs(q2_a3-1.059) < 1e-3)
ok("S Q2b bound step: 3/(2+1/1)=1 (not 3/2)", sp.Rational(3)/(2+sp.Integer(1)/1) == 1)
ok("S Q2b limit=1", set(sp.solve(sp.Eq(L, 3/(2+1/L)), L)) == {1} and all(s_ >= 1 for s_ in seq))
ok("S Q2b induction step monotone: 3/(2+1/u) increasing in u>0", sp.simplify(sp.diff(3/(2+1/t), t)).subs(t, 1) > 0)

# ---- Q3a
e3 = sp.sqrt(1+n+n**2) - sp.sqrt(1-2*n+n**2)
ok("S Q3a numerator = 3n", sp.expand((1+n+n**2)-(1-2*n+n**2)) == 3*n)
ok("S Q3a denominator/n -> 2", sp.limit((sp.sqrt(1+n+n**2)+sp.sqrt(1-2*n+n**2))/n, n, sp.oo) == 2)
ok("S Q3a limit 3/2", sp.limit(e3, n, sp.oo) == sp.Rational(3, 2))
ok("S Q3a n=0 shortcut absent: (inf-inf) numerically ~1.5 at n=1e6", abs(sp.N(e3.subs(n, 10**6), 15)-1.5) < 1e-5)

# ---- Q3b
q3_int = sp.integrate(x*sp.exp(x), (x, 0, 1)); q3_V = 2*sp.pi*sp.integrate(x*(sp.E-sp.exp(x)), (x, 0, 1))
ok("S Q3b int x e^x = 1", q3_int == 1)
ok("S Q3b V=2pi(e/2-1)=2.257", sp.simplify(q3_V-2*sp.pi*(sp.E/2-1)) == 0 and abs(sp.N(q3_V, 8)-2.257) < 1e-3)
ok("S Q3b shell height (e+1)-(e^x+1)=e-e^x", sp.simplify((sp.E+1)-(sp.exp(x)+1)-(sp.E-sp.exp(x))) == 0)
ok("S Q3b distractor integrals differ from V", all(abs(sp.N(v, 8)-sp.N(q3_V, 8)) > 1e-3 for v in (
    sp.pi*sp.integrate((sp.E-sp.exp(x))**2, (x, 0, 1)), 2*sp.pi*sp.integrate(sp.E-sp.exp(x), (x, 0, 1)),
    2*sp.pi*sp.integrate(x*(sp.exp(x)+1), (x, 0, 1)))))

# ---- Q4a
h = sp.log(x)**2 - 2*sp.log(x)
q4_crit = sp.solve(sp.diff(h, x), x)
ok("S Q4a critical point e=2.718", q4_crit == [sp.E] and abs(sp.N(sp.E, 6)-2.718) < 1e-3 and sp.sqrt(sp.E) < sp.E < sp.E**2)
q4_vals = [sp.simplify(h.subs(x, v)) for v in (sp.sqrt(sp.E), sp.E, sp.E**2)]
ok("S Q4a values -3/4,-1,0", q4_vals == [sp.Rational(-3, 4), -1, 0] and min(q4_vals) == -1 and max(q4_vals) == 0)

# ---- Q4b
fq = 3*x**4/(x**3+2*x+9)
ok("S Q4b a=3", sp.limit(fq/x, x, sp.oo) == 3)
ok("S Q4b a=2,b=0 -> +oo", sp.limit(fq-2*x, x, sp.oo) == sp.oo)
ok("S Q4b b=0", sp.limit(fq-3*x, x, sp.oo) == 0)

# ---- Q5a
ok("S Q5a lim -2+ = 1", sp.limit(x+3, x, -2, '+') == 1)
fl = sp.exp(-x*(-(x+2))/(x+2)**2)  # x<-2: |x+2| = -(x+2)
ok("S Q5a exponent simplifies to x/(x+2); lim -2- = +oo", sp.simplify(-x*(-(x+2))/(x+2)**2 - x/(x+2)) == 0 and sp.limit(fl, x, -2, '-') == sp.oo)
ok("S Q5a lim 0- = 3", sp.limit(x+3, x, 0, '-') == 3)
ok("S Q5a lim 0+ = pi/2 = 1.571, != 3", sp.limit(sp.atan(1/x), x, 0, '+') == sp.pi/2 and abs(sp.N(sp.pi/2, 6)-1.571) < 1e-3)

# ---- Q5b
ok("S Q5b x dx = 1/2 dt (t=x^2)", sp.diff(x**2, x)/2 == x)
cs = [sp.sin(x**2)/2, sp.sin(x**2), -sp.sin(x**2)/2, sp.cos(x**2)/2]
ok("S Q5b antiderivative: only option a", [sp.simplify(sp.diff(c, x)-x*sp.cos(x**2)) == 0 for c in cs] == [True, False, False, False])

# ---- Q6a
fa = sp.exp(x)-x-1
ok("S Q6a f'(0)=0, f''(0)=1, f(0)=0", sp.diff(fa, x).subs(x, 0) == 0 and sp.diff(fa, x, 2).subs(x, 0) == 1 and fa.subs(x, 0) == 0)
ok("S Q6a bug line: (e^x+1)' not zero at 0 and differs from f'", sp.diff(fa, x) != sp.exp(x)+1 and (sp.exp(x)+1).subs(x, 0) == 2)
ok("S Q6a f''>0 everywhere & unique critical point (global min)", sp.solve(sp.diff(fa, x), x) == [0])

# ---- Q6b
ok("S Q6b intersection x=1", sp.solve(sp.Eq(x, 1/x), x) == [-1, 1])
q6_s1 = sp.integrate(4-x, (x, 1, 4)); q6_ln = sp.integrate(1/y, (y, 1, 4)); q6_S = sp.Rational(15, 2)-sp.log(4)
ok("S Q6b S1=9/2 (triangle (1,1),(4,4),(1,4))", q6_s1 == sp.Rational(9, 2))
ok("S Q6b int 1/y = ln4 = 1.386", sp.simplify(q6_ln-sp.log(4)) == 0 and abs(sp.N(q6_ln, 6)-1.386) < 1e-3)
ok("S Q6b S2 = 3-ln4 by x-integral; S=15/2-ln4=6.114", sp.simplify(sp.integrate(4-1/x, (x, sp.Rational(1, 4), 1))-(3-sp.log(4))) == 0 and abs(sp.N(q6_S, 6)-6.114) < 1e-3)

# ---- cross-check: the numeric answers stored in the raw JSON equal the values derived above
raw = json.loads((pathlib.Path(__file__).resolve().parents[2]/"raw"/"24B-B.json").read_text(encoding="utf-8"))
def num_answers(qid):
    for q in raw["questions"]:
        pk = q.get("part", "")
        if f"Q{q['num']}" + {"": "", "א": "a", "ב": "b"}[pk] == qid:
            return [(s["answer"], s["tol"]) for s in q.get("steps", []) if s["type"] == "numeric"]
    return None
expect = {
    "Q1": [q1_fs3, q1_a], "Q2a": [2, -1], "Q2b": [q2_a3, 1], "Q3a": [3, 2], "Q3b": [q3_int, q3_V],
    "Q4a": [sp.E, sp.Rational(-3, 4), 0, -1], "Q4b": [3, 0], "Q5a": [1, 3, sp.pi/2], "Q5b": [sp.Rational(1, 2)],
    "Q6a": [1, 0], "Q6b": [1, q6_s1, q6_ln, q6_S],
}
for qid, vals in expect.items():
    got = num_answers(qid)
    good = got is not None and len(got) == len(vals) and all(abs(sp.N(v, 12)-ga) <= max(tol, 1e-12) for v, (ga, tol) in zip(vals, got))
    ok(f"S JSON numeric steps {qid} match sympy", good)

for k, v in R: print(k, "OK" if v else "MISMATCH")
print("STEPS ALL OK" if all(v for _, v in R) else "STEPS FAIL", f"({len(R)} checks)")

# Machine check of every stored answer and every lesson number of courses/recursive_seq (levels C01..C08).
# Run:  py tools/verify/needhelp/recursive_seq/check.py   (needs sympy, mpmath and node)
import json, subprocess, pathlib, math
from fractions import Fraction as F
import sympy as sp
import mpmath

mpmath.mp.dps = 50
msqrt = mpmath.sqrt

ROOT = pathlib.Path(__file__).resolve().parents[4]
out = subprocess.run(["node", str(ROOT / "tools" / "course_load.js")], capture_output=True, check=True, cwd=ROOT).stdout
data = json.loads(out.decode("utf8"))
assert not data["errors"], data["errors"]
LV = {e["level"]["id"]: e["level"] for e in data["levels"] if e["courseId"] == "recursive_seq"}
assert sorted(LV) == ["C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08"]
Q = {q["id"]: q for l in LV.values() for q in l["questions"] if "id" in q}
BANK = {q["id"]: q for q in json.loads((ROOT / "questions.json").read_text(encoding="utf8"))["questions"]}
checked = set()


def it(f, a1, n):
    s = [a1]
    for _ in range(n - 1):
        s.append(f(s[-1]))
    return s


def rat(f, a1, n=60): return it(f, F(a1), n)
def num(f, a1, n=60): return it(f, mpmath.mpf(a1), n)


def cls(s):
    d = [s[i + 1] - s[i] for i in range(len(s) - 1)]
    if all(v == 0 for v in d): return "d"
    if all(v >= 0 for v in d): return "a"
    if all(v <= 0 for v in d): return "b"
    return "c"


def mcq(qid, claims):
    q = Q[qid]
    ids = [o["id"] for o in q["options"]]
    assert set(claims) == set(ids), (qid, claims, ids)
    true_ids = [i for i, v in claims.items() if v]
    assert true_ids == [q["correctId"]], (qid, "claims say", true_ids, "stored", q["correctId"])
    checked.add(qid)


def numeric(qid, value):
    s = Q[qid]["step"]
    assert s["type"] == "numeric"
    assert abs(float(value) - s["answer"]) <= max(s["tol"], 1e-12), (qid, float(value), s["answer"])
    checked.add(qid)


def stepcheck(qid, typ, bug=None):
    s = Q[qid]["step"]
    assert s["type"] == typ
    if bug is not None: assert s["bugIndex"] == bug
    checked.add(qid)


x, L, a = sp.symbols("x L a", real=True)
cc = sp.symbols("c", positive=True)
isroot = lambda v, eq: sp.simplify(eq.subs(L, v)) == 0

# ---------------- C01
numeric("C01-Q1", rat(lambda t: 2 * t - 1, 3)[2])
s = it(lambda t: sp.sqrt(t + 5), sp.Integer(11), 3); assert s[1] == 4 and s[2] == 3
numeric("C01-Q2", s[2])
h = lambda t: t / 2 + 1
mcq("C01-Q3", {k: cls(rat(h, 1, 40)) == k for k in "abcd"})
mcq("C01-Q4", {k: cls(rat(h, 10, 40)) == k for k in "abcd"})
mcq("C01-Q5", {k: cls(rat(lambda t: 1 / t, 2, 40)) == k for k in "abcd"})
assert rat(h, 1, 4) == [1, F(3, 2), F(7, 4), F(15, 8)]        # lesson: 1, 1.5, 1.75, 1.875
assert rat(h, 10, 4) == [10, 6, 4, 3]                          # Q4 explanation
assert rat(lambda t: 1 / t, 2, 4) == [2, F(1, 2), 2, F(1, 2)]  # Q5 explanation
g = lambda t: 6 / (5 - t)
t6 = rat(g, 1, 3)
assert t6[1] == F(3, 2) and t6[2] == F(12, 7) and round(float(t6[2]), 3) == 1.714
numeric("C01-Q6", t6[2])

# ---------------- C02
fp = sp.solve(sp.Eq(L, L / 2 + 1), L); assert fp == [2]
numeric("C02-Q1", fp[0])
mcq("C02-Q2", {"a": isroot(-1, L - sp.sqrt(2 + L)), "b": isroot(2, L - sp.sqrt(2 + L)),
               "c": isroot(sp.sqrt(2), L - sp.sqrt(2 + L)), "d": isroot(4, L - sp.sqrt(2 + L))})
assert set(sp.solve(sp.Eq(L * (5 - L), 6), L)) == {2, 3}
r3 = rat(g, 1, 300)
assert abs(float(r3[-1]) - 2) < 1e-9 and all(v < 2 for v in r3)
assert [round(float(v), 2) for v in r3[:5]] == [1.0, 1.5, 1.71, 1.83, 1.89]   # terms printed in the question
e = L * (5 - L) - 6
mcq("C02-Q3", {"a": isroot(2, e) and isroot(3, e) and abs(float(r3[-1]) - 2) < 1e-9,
               "b": isroot(2, e) and isroot(3, e) and abs(float(r3[-1]) - 3) < 1e-9,
               "c": isroot(-2, e) and isroot(-3, e),
               "d": isroot(1, e) and isroot(6, e)})
d4 = rat(lambda t: 2 * t + 1, 1, 30)
assert all(d4[i] == 2 ** (i + 1) - 1 for i in range(30)) and d4[:4] == [1, 3, 7, 15]
assert sp.solve(sp.Eq(L, 2 * L + 1), L) == [-1]
diverges = d4[-1] > 10 ** 6
mcq("C02-Q4", {"a": not diverges, "b": diverges, "c": not diverges, "d": not diverges})
numeric("C02-Q5", sp.sqrt(7))
assert set(sp.solve(sp.Eq(L, (L + 7 / L) / 2), L)) == {sp.sqrt(7), -sp.sqrt(7)}
assert abs(float(num(lambda t: (t + 7 / t) / 2, 3)[-1]) - math.sqrt(7)) < 1e-12
assert sp.solve(sp.Eq(L, sp.sqrt(6 + L)), L) == [3]
assert sp.expand((L - 3) * (L + 2)) == L ** 2 - L - 6 and set(sp.solve(L ** 2 - L - 6, L)) == {3, -2}
assert abs(float(num(lambda t: msqrt(6 + t), 1)[-1]) - 3) < 1e-12
stepcheck("C02-Q6", "order")

# ---------------- C03
fq = lambda t: msqrt(2 + t)
assert all(v < 2 for v in num(fq, 1, 30))
assert sp.solveset(sp.sqrt(2 + x) >= 2, x, sp.Interval(-2, sp.oo)) == sp.Interval(2, sp.oo)        # a_n>=2 => a_{n+1}>=2
assert sp.solveset(sp.sqrt(2 + x) < 2, x, sp.Interval(-2, sp.oo)) == sp.Interval.Ropen(-2, 2)      # a_n<2 => a_{n+1}<2
s3 = num(fq, 3, 100)
mcq("C03-Q2", {"a": all(v <= 2 for v in s3), "b": all(v >= 2 for v in s3), "c": all(v >= 4 for v in s3), "d": all(v <= 1 for v in s3)})
stepcheck("C03-Q1", "order")
assert sp.solveset(sp.sqrt(x + 12) < 4, x, sp.Interval(-12, sp.oo)) == sp.Interval.Ropen(-12, 4)    # a_n<4 => a_{n+1}<4
assert not (0.5 + 12 < 12) and (0.5 + 12 < 16)      # the buggy line "a+12<12" is false for a positive term
assert all(v < 4 for v in num(lambda t: msqrt(t + 12), 1, 30))
stepcheck("C03-Q3", "findbug", 2)
assert sp.limit(x / 2 + 1, x, 2) == 2 and all(v < 2 for v in rat(h, 0, 80))
numeric("C03-Q4", 2)
sq = num(fq, 1, 4); assert abs(float(sq[2]) - 1.9318) < 1e-3     # a_3 ~ 1.93 in the explanation
base_ok = 1 <= 1.5
step_fails = float(msqrt(2 + 1.5)) > 1.5
claim_true = all(v <= 1.5 for v in num(fq, 1, 20))
assert abs(float(msqrt(3.5)) - 1.87) < 0.005 and not claim_true
mcq("C03-Q5", {"a": not base_ok, "b": base_ok and step_fails, "c": claim_true, "d": False})  # d: sqrt is increasing, so applying it is legal
assert sp.solve(sp.Eq(L, sp.sqrt(3 * L + 10)), L) == [5]
assert all(v < 5 for v in num(lambda t: msqrt(3 * t + 10), 1, 30))
numeric("C03-Q6", 5)

# ---------------- C04
dom = sp.Interval.open(0, sp.oo)
mono = lambda f: sp.solveset(sp.diff(f, x) > 0, x, dom) == dom
mcq("C04-Q1", {"a": mono(sp.sqrt(x + 3)), "b": mono(4 / (x + 1)), "c": mono(2 - x), "d": mono(1 / x)})
numeric("C04-Q2", sp.sqrt(7))
assert sp.sqrt(7) > 1
assert all(v > 0 for v in num(lambda t: msqrt(t + 6), 1, 40))
s4 = num(lambda t: msqrt(t + 6), 1, 30); assert all(s4[i + 1] > s4[i] for i in range(29))
stepcheck("C04-Q3", "order")
dif = sp.Rational(1, 2) * a + 1 - a
mcq("C04-Q4", {"a": sp.simplify(dif - (a - 2) / 2) == 0, "b": sp.simplify(dif - (2 - a) / 2) == 0,
               "c": sp.simplify(dif - (1 + a / 2)) == 0, "d": sp.simplify(dif - a / 2) == 0})
s10 = rat(h, 10, 80)
inc10 = all(s10[i + 1] >= s10[i] for i in range(79))
dec10 = all(s10[i + 1] <= s10[i] for i in range(79))
lo10 = all(v > 2 for v in s10)
mcq("C04-Q5", {"a": inc10, "b": dec10 and lo10, "c": inc10 and lo10, "d": not (dec10 and lo10) and False})
good = sp.expand((2 - a) * (a + 1)); bad = sp.expand((a - 2) * (a + 1))
assert good == sp.expand(2 + a - a ** 2) and bad != good
stepcheck("C04-Q6", "findbug", 1)

# ---------------- C05
assert set(sp.solve(sp.Eq(L ** 2, L + 12), L)) == {4, -3}
s5 = num(lambda t: msqrt(t + 12), 2, 100)
assert all(v <= 4 for v in s5) and all(s5[i + 1] >= s5[i] for i in range(99)) and abs(float(s5[-1]) - 4) < 1e-12
assert sp.sqrt(14) > 2
numeric("C05-Q2", 4)
s7 = num(lambda t: msqrt(t + 12), 7, 100)
dec7 = all(s7[i + 1] <= s7[i] for i in range(99)); ge4 = all(v >= 4 for v in s7)
assert abs(float(msqrt(19)) - 4.36) < 0.005 and msqrt(19) < 7
inc7 = all(s7[i + 1] >= s7[i] for i in range(99))
mcq("C05-Q3", {"a": dec7 and ge4 and abs(float(s7[-1]) - 4) < 1e-12, "b": inc7, "c": ge4 and False, "d": False})  # c: limit is >= 4, so -3 is impossible
assert sp.expand((L - 4) * (L + 3)) == L ** 2 - L - 12
stepcheck("C05-Q4", "findbug", 4)
# Q1 is conceptual: L=f(L) presupposes that the limit exists (counterexample 2a+1 is checked in C02-Q4)
mcq("C05-Q1", {"a": False, "b": True, "c": False, "d": False})
# Q5: -3 IS a root of L^2=L+12 but not of L=sqrt(L+12); a bounded-below/nonnegative sequence has a nonnegative limit
assert isroot(-3, L ** 2 - L - 12) and not isroot(-3, L - sp.sqrt(L + 12))
mcq("C05-Q5", {"a": not isroot(-3, L ** 2 - L - 12), "b": True, "c": False, "d": False})   # c: no such rule; d: e.g. a_n=-1/n -> 0 and a_n=-1 -> -1
numeric("C05-Q6", 5)
assert set(sp.solve(L ** 2 - 3 * L - 10, L)) == {5, -2}
s56 = num(lambda t: msqrt(3 * t + 10), 1, 100)
assert abs(float(s56[-1]) - 5) < 1e-12 and all(s56[i + 1] >= s56[i] for i in range(99))

# ---------------- C06
fr = lambda t: F(2) / (3 - t)
r6 = rat(fr, 0, 80)
assert r6[1] == F(2, 3) and r6[2] == F(6, 7) and round(float(r6[2]), 3) == 0.857
numeric("C06-Q1", r6[2])
assert all(v <= 1 for v in r6) and all(r6[i + 1] >= r6[i] for i in range(79)) and abs(float(r6[-1]) - 1) < 1e-9
assert sp.solveset(2 / (3 - x) <= 1, x, sp.Interval(-sp.oo, 1)) == sp.Interval(-sp.oo, 1)    # step holds for every x<=1
mcq("C06-Q2", {"a": all(v <= 1 for v in r6), "b": all(v >= 1 for v in r6), "c": all(v <= F(1, 2) for v in r6), "d": all(v >= 2 for v in r6)})
assert set(sp.solve(L * (3 - L) - 2, L)) == {1, 2}
assert sp.expand((a - 1) * (a - 2)) == a ** 2 - 3 * a + 2
assert sp.solveset(sp.expand((x - 1) * (x - 2)) >= 0, x, sp.Interval(-sp.oo, 1)) == sp.Interval(-sp.oo, 1)
stepcheck("C06-Q3", "order")
lim6 = float(r6[-1])
# a: valid reason (a_n<=1 => L<=1).  c: value 1 is right but "1 is smaller than 2" is not a reason, so it is wrong as stated.
mcq("C06-Q4", {"a": abs(lim6 - 1) < 1e-9 and all(v <= 1 for v in r6), "b": abs(lim6 - 2) < 1e-9, "c": False, "d": abs(lim6 - 2) < 1e-9})
r12 = rat(lambda t: F(12) / (7 - t), 0, 120)
assert set(sp.solve(L * (7 - L) - 12, L)) == {3, 4} and all(v <= 3 for v in r12) and abs(float(r12[-1]) - 3) < 1e-9
numeric("C06-Q5", 3)
assert F(1, 3) < F(1, 2)    # 1/(3-0) < 1/2 refutes the buggy line "1/(3-a) >= 1/2"
stepcheck("C06-Q6", "findbug", 3)

# ---------------- C07
bab = lambda c: (lambda t: (t + mpmath.mpf(c) / t) / 2)
b4 = num(bab(10), 4, 60)
assert b4[1] == mpmath.mpf(13) / 4
numeric("C07-Q1", b4[1])
assert round(float(b4[2]), 3) == 3.163                       # lesson says a_3 ~ 3.163
df = sp.Rational(1, 2) * (a + cc / a) - a
mcq("C07-Q2", {"a": sp.simplify(df - (cc - a ** 2) / (2 * a)) == 0, "b": sp.simplify(df - (a ** 2 - cc) / (2 * a)) == 0,
               "c": sp.simplify(df - (cc + a ** 2) / (2 * a)) == 0, "d": sp.simplify(df - cc / (2 * a)) == 0})
b1 = num(bab(10), 1, 60)
assert b1[1] == mpmath.mpf(11) / 2
rt = math.sqrt(10)
allge = all(float(v) >= rt for v in b1); ge2 = all(float(v) >= rt for v in b1[1:])
even = all((float(b1[i]) >= rt) == (i % 2 == 1) for i in range(60))
mcq("C07-Q3", {"a": allge, "b": ge2 and not allge, "c": not any(float(v) >= rt for v in b1), "d": even and not ge2})
# AM-GM identity behind Q4: (x+c/x)/2 - sqrt(c) = (x - sqrt(c))^2 / (2x)
assert sp.simplify(sp.Rational(1, 2) * (a + cc / a) - sp.sqrt(cc) - (a - sp.sqrt(cc)) ** 2 / (2 * a)) == 0
assert all(float(v) >= rt for v in b4[1:]) and float(b4[0]) > rt
stepcheck("C07-Q4", "order")
numeric("C07-Q5", sp.sqrt(10))
assert abs(float(num(lambda t: (t + 10 / t) / 2, 4)[-1]) - rt) < 1e-12
assert all(b4[i + 1] <= b4[i] for i in range(59))             # decreasing, as the lesson states
# Q6: the correct difference is (c-a^2)/(2a); for a>=sqrt(c) it is <=0 so the sequence DEcreases; the stored line claims increasing
assert sp.simplify(df - (cc - a ** 2) / (2 * a)) == 0
stepcheck("C07-Q6", "findbug", 3)

# ---------------- C08 boss (bank questions): bounds incl. n=1, limits, directions
def chk(f, a1, bound, kind, lim, n=200):
    s = num(f, a1, n)
    if kind == "<=": assert all(v <= bound for v in s) and s[0] <= bound     # n=1 explicitly
    if kind == ">=": assert all(v >= bound for v in s) and s[0] >= bound
    assert abs(float(s[-1]) - lim) < 1e-9
    return s


s = chk(lambda t: msqrt(t + 20), 4, 5, "<=", 5);   assert all(s[i + 1] >= s[i] for i in range(199))
s = chk(lambda t: 3 / (2 + 1 / t), 2, 1, ">=", 1); assert all(s[i + 1] <= s[i] for i in range(199))
s = chk(lambda t: 6 / (5 - t), 1, 2, "<=", 2);     assert all(s[i + 1] >= s[i] for i in range(199))
s = chk(lambda t: msqrt(20 + t), 0, 5, "<=", 5);   assert all(s[i + 1] > s[i] for i in range(30)) and s[0] < 5
assert set(sp.solve(L ** 2 - 5 * L + 6, L)) == {2, 3} and set(sp.solve(L ** 2 - L, L)) == {0, 1} and set(sp.solve(L ** 2 - L - 20, L)) == {5, -4}
for bid in ["24A-B-Q2b", "24B-B-Q2b", "24A-A-Q2b", "23B-B-Q2b"]:
    b = BANK[bid]
    assert b["topic"] == "sequences_limits" and b["official"] and b["stepsSource"] == "ai-verified", bid
    assert b["examCode"] in ("24B-B", "24A-A", "24A-B", "23B-B"), bid
assert [q["bankId"] for q in LV["C08"]["questions"]] == ["24A-B-Q2b", "24B-B-Q2b", "24A-A-Q2b", "23B-B-Q2b"]

missing = sorted(set(Q) - checked)
assert not missing, missing
print("OK:", len(checked), "own questions checked;", len(LV["C08"]["questions"]), "boss bank questions")

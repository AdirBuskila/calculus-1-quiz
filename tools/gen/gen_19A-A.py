# -*- coding: utf-8 -*-
"""Generator for tools/raw/19A-A.json -- calculus-1 (20151), semester A 2019, moed A, version 1 (26/02/2019).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_19A-A.py

Source: sitting 19A-A, pp.1-8 (typed exam with the official worked solution after every question; p.1 is the cover).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Figures inside solutions: Q1 graph (p.3), Q6b region (p.8).
- Q4a: the official min value is -(1/5)*540^(1/6); transcribed as printed (checked numerically).
- Q6a: the official cylinder-minus-shells set-up is transcribed as printed (equivalent to 2*pi*int x(2-e^x)).

Checks (tools/verify/19A-A/check.py, sympy + a numeric grid for Q4a): every derivative, limit, asymptote,
extremum, partial-fraction coefficient, antiderivative, tangent line, volume and area matches the official
answer. 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "19A-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
$$f(x)=\frac{e^{-x}}{1-x}=-\frac{1}{e^x(x-1)}$$
**תחום ההגדרה:** $(-\infty,1)\cup(1,+\infty)$.
**אסימפטוטה אנכית** $x=1$:
$$\lim_{x\to1^+}\frac{-1}{e^x(x-1)}=\left[\frac{-1}{0^+}\right]=-\infty,\qquad\lim_{x\to1^-}\frac{-1}{e^x(x-1)}=\left[\frac{-1}{0^-}\right]=+\infty$$
**אסימפטוטה אופקית** ב-$+\infty$: $y=0$:
$$\lim_{x\to+\infty}\frac{-1}{e^x(x-1)}=\left[\frac{-1}{+\infty}\right]=0$$
**אין אסימפטוטה משופעת ב-$-\infty$:**
$$\lim_{x\to-\infty}\frac{f(x)}{x}=\lim_{x\to-\infty}\frac{e^{-x}}{1-x}\cdot\frac1x=\lim_{x\to-\infty}\frac{-e^{-x}}{x(x-1)}=\left[\frac{\infty}{\infty}\right]=\lim_{x\to-\infty}\frac{\left(-e^{-x}\right)'}{\left(x^2-x\right)'}=$$
$$=\lim_{x\to-\infty}\frac{e^{-x}}{2x-1}=\left[\frac{\infty}{\infty}\right]=\lim_{x\to-\infty}\frac{\left(e^{-x}\right)'}{(2x-1)'}=\lim_{x\to-\infty}\frac{-e^{-x}}{2}=-\infty$$
$$f'(x)=\left(-\frac{1}{e^x(x-1)}\right)'=\frac{e^xx}{e^{2x}(x-1)^2}$$
תחומי עלייה: $(0,1),(1,+\infty)$. תחומי ירידה: $(-\infty,0)$. נקודת מינימום מקומי: $x=0$, $f(0)=1$.
$$f''(x)=\left(-\frac{1}{e^x(x-1)}\right)''=\left(\frac{x}{e^x(x-1)^2}\right)'=\frac{e^x(x-1)^2-xe^x(x-1)^2-xe^x2(x-1)}{e^{2x}(x-1)^4}=$$
$$=\frac{(x-1)-x(x-1)-2x}{e^x(x-1)^3}=-\frac{x^2+1}{e^x(x-1)^3}$$
קמורה ב: $(-\infty,1)$. קעורה ב: $(1,+\infty)$. אין נקודת פיתול.
![גרף הפונקציה y = e^(−x)/(1−x) עם האסימפטוטה האנכית x=1, האסימפטוטה y=0 מימין והמינימום ב-(0,1)](images/exams/19A-A-Q1-graph.png)
"""

SOL2A = r"""
$$\sqrt[2n]{7^{2n}}\le\sqrt[2n]{3^n+7^{2n}+\frac{n}{n+1}}\le\sqrt[2n]{7^{2n}+7^{2n}+7^{2n}}$$
$$7\le\sqrt[2n]{3^n+7^{2n}+\frac{n}{n+1}}\le7\cdot\sqrt[2n]{3}$$
$$\lim_{n\to\infty}\sqrt[2n]{3}=1$$
לכן לפי משפט הסנדוויץ'
$$\lim_{n\to\infty}\sqrt[2n]{3^n+7^{2n}+\frac{n}{n+1}}=7$$
"""

SOL2B = r"""
$f(x)=x\ln x$ רציפה ב-$[a,b]$ וגזירה ב-$(a,b)$ כאשר $1\le a<b\le e$. לפי משפט לגרנז' קיים $c\in(a,b)$ כך ש-$f'(c)=\frac{f(b)-f(a)}{b-a}$.
$f'(x)=(x\ln x)'=\ln x+1$, אז מתקיים $\ln c+1=\frac{b\ln b-a\ln a}{b-a}$.
פונקציה $\ln x+1$ מונוטונית עולה ממש ב-$[1,e]$, אז
$$1=\ln1+1\le\ln a+1<\ln c+1<\ln b+1\le\ln e+1=2,$$
ז"א $1\le\frac{b\ln b-a\ln a}{b-a}\le2$.
"""

SOL3A = r"""
$$L=\lim_{x\to0}\left(\frac{4}{1+\sqrt{9+x}}\right)^{\frac{1}{\sin x}}=\left[1^{\infty}\right]=\lim_{x\to0}\left(1+\frac{3-\sqrt{9+x}}{1+\sqrt{9+x}}\right)^{\frac{1+\sqrt{9+x}}{3-\sqrt{9+x}}\cdot\frac{3-\sqrt{9+x}}{1+\sqrt{9+x}}\cdot\frac{1}{\sin x}}$$
$$\lim_{x\to0}\left(1+\frac{3-\sqrt{9+x}}{1+\sqrt{9+x}}\right)^{\frac{1+\sqrt{9+x}}{3-\sqrt{9+x}}}=e,$$
$$\lim_{x\to0}\left(\frac{3-\sqrt{9+x}}{1+\sqrt{9+x}}\right)\frac{1}{\sin x}=\lim_{x\to0}\frac{1}{\left(1+\sqrt{9+x}\right)\left(3+\sqrt{9+x}\right)}\cdot\frac{(-x)}{\sin x}=\frac{1}{4\cdot6}\cdot(-1)=-\frac{1}{24}$$
$$L=e^{\left(-\frac{1}{24}\right)}$$
"""

SOL3B = r"""
$$\int\frac{\tan x}{\cos^2x\cdot e^{2\tan x}}dx=\left|t=\tan x,\ dt=\frac{1}{\cos^2x}dx\right|=\int te^{-2t}dt=\left|u=t,\ v'=e^{-2t}\Rightarrow u'=1,\ v=-\frac12e^{-2t}\right|=$$
$$=-\frac12te^{-2t}+\frac12\int e^{-2t}dt=-\frac12te^{-2t}-\frac14e^{-2t}+C=-\frac12\tan x\,e^{-2\tan x}-\frac14e^{-2\tan x}+C=-\frac{2\tan x+1}{4e^{2\tan x}}+C$$
"""

SOL4A = r"""
$$f'(x)=\left(x\left(x^2-1\right)^{\frac13}\right)'=\left(x^2-1\right)^{\frac13}+x\frac13\left(x^2-1\right)^{-\frac23}2x=\frac{3x^2-3+2x^2}{3\left(x^2-1\right)^{\frac23}}=$$
$$=\frac{5x^2-3}{3\left(x^2-1\right)^{\frac23}}=\frac{5\left(x-\sqrt{\frac35}\right)\left(x+\sqrt{\frac35}\right)}{3(x-1)^{\frac23}(x+1)^{\frac23}}$$
נקודות חשודות לקיצון ב-$(0,3)$ הן $x=1,\ x=\sqrt{\frac35}$.
$$f(1)=1\sqrt[3]{1^2-1}=0,\quad f(3)=3\sqrt[3]{3^2-1}=6,\quad f(0)=0\sqrt[3]{0^2-1}=0,$$
$$f\left(\sqrt{\frac35}\right)=\sqrt{\frac35}\sqrt[3]{\frac35-1}=-\sqrt{\frac35}\sqrt[3]{\frac25}=-\sqrt[6]{\frac{3^3}{5^3}\cdot\frac{2^2}{5^2}}=-\frac15\sqrt[6]{540}$$
אז הערך הגדול ביותר הוא $6$ והערך הקטן ביותר הוא $-\frac15\sqrt[6]{540}$.
"""

SOL4B = r"""
$$f'(x)=\left((x-3)^{\sqrt x}\right)'=\left(e^{\sqrt x\ln(x-3)}\right)'=(x-3)^{\sqrt x}\left(\frac{1}{2\sqrt x}\ln(x-3)+\frac{\sqrt x}{x-3}\right)$$
$$f'(4)=(4-3)^{\sqrt4}\left(\frac{1}{2\sqrt4}\ln(4-3)+\frac{\sqrt4}{4-3}\right)=2$$
$$f(4)=(4-3)^{\sqrt4}=1$$
משוואת המשיק לגרף של הפונקציה היא $y=1+2(x-4)$.
"""

SOL5A = r"""
$$\lim_{x\to+\infty}\frac{1}{\left(\sqrt{2x-1}-\sqrt{2x-3}\right)\sqrt{x+1}}=\lim_{x\to+\infty}\frac{\sqrt{2x-1}+\sqrt{2x-3}}{\left(\sqrt{2x-1}-\sqrt{2x-3}\right)\left(\sqrt{2x-1}+\sqrt{2x-3}\right)\sqrt{x+1}}=$$
$$=\lim_{x\to+\infty}\frac{\sqrt{2x-1}+\sqrt{2x-3}}{(2x-1-2x+3)\sqrt{x+1}}=\lim_{x\to+\infty}\frac{\sqrt{2x-1}+\sqrt{2x-3}}{2\sqrt{x+1}}=$$
$$=\lim_{x\to+\infty}\frac{\sqrt x\left(\sqrt{2-\frac1x}+\sqrt{2-\frac3x}\right)}{\sqrt x\,2\sqrt{1+\frac1x}}=\lim_{x\to+\infty}\frac{\sqrt{2-\frac1x}+\sqrt{2-\frac3x}}{2\sqrt{1+\frac1x}}=\frac{2\sqrt2}{2}=\sqrt2$$
"""

SOL5B = r"""
$$\frac{2x^2-x+1}{(x-1)\left(x^2+1\right)}=\frac{A}{x-1}+\frac{Bx+C}{x^2+1}=\frac{A\left(x^2+1\right)+(Bx+C)(x-1)}{(x-1)\left(x^2+1\right)}$$
$$2x^2-x+1=(A+B)x^2+(-B+C)x+(A-C)$$
$$A=1,\ B=1,\ C=0$$
$$\int\frac{2x^2-x+1}{(x-1)\left(x^2+1\right)}dx=\int\left(\frac{1}{x-1}+\frac{x}{x^2+1}\right)dx=\ln|x-1|+\frac12\ln\left(x^2+1\right)+C$$
"""

SOL6A = r"""
$$V=\pi(\ln2)^2-2\pi\int_0^{\ln2}x\left(e^x-1\right)dx=\pi(\ln2)^2+\pi x^2\Big|_0^{\ln2}-2\pi\int_0^{\ln2}xe^x\,dx=$$
$$=\left|u=x,\ v'=e^x\Rightarrow u'=1,\ v=e^x\right|=2\pi(\ln2)^2-2\pi xe^x\Big|_0^{\ln2}+2\pi\int_0^{\ln2}e^x\,dx=$$
$$=2\pi(\ln2)^2-4\pi\ln2+2\pi e^x\Big|_0^{\ln2}=2\pi(\ln2)^2-4\pi\ln2+4\pi-2\pi=2\pi\left((\ln2)^2-2\ln2+1\right)=2\pi(1-\ln2)^2$$
"""

SOL6B = r"""
![התחום הכלוא בין הישרים y = x, y = x/2 וההיפרבולה y = 1/x](images/exams/19A-A-Q6b-fig.png)
$$S=\int_0^1\left(x-\frac12x\right)dx+\int_1^{\sqrt2}\left(\frac1x-\frac12x\right)dx=\int_0^1\frac12x\,dx+\int_1^{\sqrt2}\frac1x\,dx-\int_1^{\sqrt2}\frac12x\,dx=$$
$$=\frac14x^2\Big|_0^1+\ln|x|\Big|_1^{\sqrt2}-\frac14x^2\Big|_1^{\sqrt2}=\frac14+\ln\sqrt2-\frac12+\frac14=\frac12\ln2$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $y=\frac{e^{-x}}{1-x}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, נקודות קיצון, "
      "תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1),

    Q(2, "computation", "sequences_limits",
      r"חשבו את הגבול $\lim_{n\to\infty}\sqrt[2n]{3^n+7^{2n}+\frac{n}{n+1}}$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "mean_value_theorems",
      r"הוכיחו את אי-השוויון הבא: $1\le\frac{b\ln b-a\ln a}{b-a}\le2$ כאשר $1\le a<b\le e$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\left(\frac{4}{1+\sqrt{9+x}}\right)^{\frac{1}{\sin x}}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\tan x}{\cos^2x\cdot e^{2\tan x}}\,dx$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "extrema_optimization",
      r"חשבו את הערך הגדול ביותר ואת הערך הקטן ביותר של הפונקציה $f(x)=x\sqrt[3]{x^2-1}$ בקטע $[0,3]$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "derivatives_tangents",
      r"מצאו את משוואת המשיק לגרף של הפונקציה $f(x)=(x-3)^{\sqrt{x}}$ בנקודה $x=4$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to+\infty}\frac{1}{\sqrt{2x-1}-\sqrt{2x-3}}\cdot\frac{1}{\sqrt{x+1}}$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{2x^2-x+1}{(x-1)\left(x^2+1\right)}\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "definite_integrals",
      r"מצאו את נפח הגוף, הנוצר על-ידי סיבוב סביב ציר ה-$Y$ של התחום הכלוא בין הקווים הבאים: "
      r"$y=e^x-1,\ y=1,\ x=0$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "definite_integrals",
      r"חשבו את השטח הכלוא בין הקווים הבאים: $y=x,\ y=\frac{x}{2},\ y=\frac1x\ (x>0)$.",
      SOL6B, part="ב", points=10),
]

# ---- steps / rubric / pitfalls (ai-draft); every value below is computed or asserted with sympy ----
import sympy as sp

IDS = "abcdef"
_rot = [0]
x, t, a, b = sp.symbols('x t a b', real=True)
n = sp.Symbol('n', positive=True)
R = sp.Rational
TOPSRC = {}


def T(e):
    """TeX of a sympy expression, wrapped in $...$."""
    return "$" + sp.latex(e) + "$"


def rub(*items):
    return [{"text": s, "points": p} for s, p in items]


def _opts(vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def ch(prompt, good, bads, explain):
    """choice step; the correct option rotates through the positions a, b, c, ..."""
    k = _rot[0] % (len(bads) + 1)
    _rot[0] += 1
    vals = list(bads)
    vals.insert(k, good)
    assert len(set(vals)) == len(vals), "duplicate options"
    return {"type": "choice", "prompt": prompt, "options": _opts(vals), "correctId": IDS[k], "explain": explain}


def chx(prompt, good, bads, ok, explain):
    """choice over sympy expressions: ok(e) must hold for the good one and fail for every distractor."""
    assert ok(good), "good option fails its test"
    for e in bads:
        assert not ok(e), "distractor passes the test: %s" % e
    return ch(prompt, T(good), [T(e) for e in bads], explain)


def num(prompt, val, explain, tol=0.001):
    v = sp.N(val, 15)
    f = float(v)
    ans = int(round(f)) if abs(f - round(f)) < 1e-12 else round(f, 4)
    return {"type": "numeric", "prompt": prompt, "answer": ans, "tol": tol, "explain": explain}


def order(prompt, lines, explain):
    return {"type": "order", "prompt": prompt, "lines": lines, "explain": explain}


def findbug(prompt, lines, idx, explain):
    return {"type": "findbug", "prompt": prompt, "lines": lines, "bugIndex": idx, "explain": explain}


def add(num_, part=None, **kw):
    for q in questions:
        if q["num"] == num_ and q.get("part") == part:
            assert not q.get("hold"), "held item"
            q.update(kw)
            return
    raise KeyError((num_, part))


def same(e1, e2):
    return sp.simplify(e1 - e2) == 0

# ===== Q1: y = e^{-x}/(1-x) =====
f1 = sp.exp(-x)/(1 - x)
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, x*sp.exp(-x)/(x - 1)**2) and same(f1pp, -(x**2 + 1)*sp.exp(-x)/(x - 1)**3)
assert sp.solve(sp.numer(sp.together(f1p)), x) == [0] and f1.subs(x, 0) == 1
assert f1p.subs(x, -1) < 0 and f1p.subs(x, R(1, 2)) > 0 and f1p.subs(x, 2) > 0
assert f1pp.subs(x, 0) > 0 and f1pp.subs(x, -5) > 0 and f1pp.subs(x, 2) < 0 and sp.solve(f1pp, x) == []
assert sp.limit(f1, x, 1, '+') == -sp.oo and sp.limit(f1, x, 1, '-') == sp.oo
assert sp.limit(f1, x, sp.oo) == 0 and sp.limit(f1, x, -sp.oo) == sp.oo and sp.limit(f1/x, x, -sp.oo) == -sp.oo

add(1,
    rubric=rub(("תחום הגדרה $x\\neq1$ ואסימפטוטה אנכית $x=1$ עם הגבולות החד-צדדיים ($-\\infty$ מימין, $+\\infty$ משמאל)", 4),
               ("אסימפטוטה אופקית $y=0$ ב-$+\\infty$ ובדיקה שאין אסימפטוטה משופעת ב-$-\\infty$", 4),
               ("נגזרת $f'(x)=\\frac{xe^{-x}}{(x-1)^2}$, תחומי עליה וירידה ומינימום מקומי $(0,1)$", 5),
               ("$f''(x)=-\\frac{x^2+1}{e^x(x-1)^3}$, קמירות ב-$(-\\infty,1)$, קעירות ב-$(1,\\infty)$ וללא נקודות פיתול", 5),
               ("שרטוט הגרף בהתאם לכל הנתונים", 2)),
    rubricSource="ai-draft",
    pitfalls=["לטעון לאסימפטוטה אופקית ב-$-\\infty$: שם $f\\to+\\infty$ מהר מכל ישר, ולכן אין אסימפטוטה בכלל.",
              "לכלול את $x=1$ בתחומי הקמירות או העליה.",
              "לטעון לנקודת פיתול ב-$x=1$: $f''$ משנה שם סימן, אבל $x=1$ אינה בתחום ההגדרה."],
    steps=[
        chx("מהי הנגזרת של $y=\\frac{e^{-x}}{1-x}$?", x*sp.exp(-x)/(x - 1)**2,
            [x*sp.exp(-x)/(x - 1), (x - 2)*sp.exp(-x)/(x - 1)**2, -x*sp.exp(-x)/(x - 1)**2],
            lambda e: same(e, f1p),
            "כלל המנה: $\\frac{-e^{-x}(1-x)+e^{-x}}{(1-x)^2}=\\frac{xe^{-x}}{(x-1)^2}$ (אומת ב-sympy)."),
        num("מהו ערך הפונקציה בנקודת המינימום המקומי $x=0$?", 1, "$f(0)=\\frac{e^0}{1}=1$."),
        ch("מה סימן $f''(x)=-\\frac{x^2+1}{e^x(x-1)^3}$ בכל אחד מתחומי ההגדרה?",
           "חיובית עבור $x<1$ (קמורה) ושלילית עבור $x>1$ (קעורה), ללא נקודות פיתול",
           ["שלילית עבור $x<1$ וחיובית עבור $x>1$", "חיובית בכל תחום ההגדרה", "מתאפסת ב-$x=0$ ולכן ב-$0$ יש נקודת פיתול"],
           "המונה $x^2+1>0$ ו-$e^x>0$, לכן הסימן נקבע לפי $-(x-1)^3$; ואין אפסים (נבדק ב-sympy)."),
        ch("מהן האסימפטוטות של $y$?", "אנכית $x=1$ ואופקית $y=0$ ב-$+\\infty$ בלבד",
           ["אנכית $x=1$ ואופקית $y=0$ בשני הכיוונים", "אנכית $x=1$ בלבד", "אנכית $x=1$ ומשופעת ב-$-\\infty$"],
           "ב-$-\\infty$: $f\\to+\\infty$ ו-$\\frac{f(x)}{x}\\to-\\infty$, ולכן אין שם אסימפטוטה (אומת ב-sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q2a: sandwich =====
nn = sp.Symbol('nn', positive=True)
a2 = lambda k: (3**k + 7**(2*k) + R(k, k + 1))**R(1, 2*k)
for k in (1, 2, 5, 10):
    assert 7 <= a2(k) <= 7*3**R(1, 2*k)
assert sp.limit(3**(1/(2*nn)), nn, sp.oo) == 1
sw_ok = lambda e: all(abs(float(sp.N(e.subs(nn, k) - (3*7**(2*k))**R(1, 2*k)))) < 1e-9 for k in (1, 2, 3))

add(2, "א",
    rubric=rub(("חסם תחתון: $\\sqrt[2n]{7^{2n}}=7$", 2),
               ("חסם עליון: החלפת כל אחד משלושת המחוברים ב-$7^{2n}$ והוצאת שורש, כלומר $7\\sqrt[2n]{3}$", 3),
               ("$\\lim_{n\\to\\infty}\\sqrt[2n]{3}=1$", 2),
               ("משפט הסנדוויץ' וערך הגבול $7$", 3)),
    rubricSource="ai-draft",
    pitfalls=["להציב $n\\to\\infty$ בכל מחובר בנפרד: $7^{2n}$ שולט, אבל צריך סנדוויץ' כדי להצדיק זאת.",
              "לכתוב חסם עליון שאינו גדול מהביטוי המקורי: $\\frac{n}{n+1}<1\\le7^{2n}$ ו-$3^n\\le7^{2n}$ נדרשים.",
              "להוציא שורש $2n$ מהמכפלה $3\\cdot7^{2n}$ ולקבל $\\sqrt[2n]{3}\\cdot7$ ולא $3\\cdot7$."],
    steps=[
        ch("באיזו שיטה פותר הפתרון הרשמי את הגבול?", "משפט הסנדוויץ' עם חסם תחתון $7$ וחסם עליון $7\\sqrt[2n]{3}$",
           ["לופיטל על הביטוי", "הצבה ישירה של $n=\\infty$ בכל מחובר", "מבחן המנה לסדרות"],
           "השורש ממעלה $2n$ של סכום אינו נגזר בקלות, ולכן חוסמים בין שני ביטויים בעלי אותו גבול."),
        chx("מהו החסם העליון $\\sqrt[2n]{7^{2n}+7^{2n}+7^{2n}}$ כפונקציה של $n$?", 7*3**(1/(2*nn)),
            [7*3**(1/nn), 3*7**(1/(2*nn)), 7*3**(2*nn)], sw_ok,
            "$\\sqrt[2n]{3\\cdot7^{2n}}=7\\cdot3^{\\frac{1}{2n}}$ (נבדק נומרית ב-sympy עבור $n=1,2,3$)."),
        num("מהו $\\lim_{n\\to\\infty}\\sqrt[2n]{3}$?", 1, "$3^{\\frac{1}{2n}}\\to3^0=1$ (sympy)."),
        num("מהו ערך הגבול?", 7, "משפט הסנדוויץ': $7\\le a_n\\le7\\cdot3^{\\frac1{2n}}\\to7$."),
    ],
    stepsSource="ai-draft")

# ===== Q2b: Lagrange, f = x ln x =====
f2 = x*sp.log(x)
f2p = sp.diff(f2, x)
assert same(f2p, sp.log(x) + 1) and f2p.subs(x, 1) == 1 and f2p.subs(x, sp.E) == 2
assert sp.diff(f2p, x).subs(x, 2) > 0
L2 = ["נגדיר $f(x)=x\\ln x$, רציפה ב-$[a,b]$ וגזירה ב-$(a,b)$; לפי משפט לגרנז' קיימת $c\\in(a,b)$ עם $f'(c)=\\frac{f(b)-f(a)}{b-a}$.",
      "$f'(x)=\\ln x+1$, ולכן $\\ln c+1=\\frac{b\\ln b-a\\ln a}{b-a}$.",
      "$\\ln x+1$ עולה ממש ב-$[1,e]$, ולכן $1=\\ln1+1\\le\\ln c+1\\le\\ln e+1=2$.",
      "מכאן $1\\le\\frac{b\\ln b-a\\ln a}{b-a}\\le2$."]
L2b = list(L2)
L2b[2] = "$\\ln x+1$ עולה ממש ב-$[1,e]$, ולכן $1=\\ln1+1\\le\\ln c+1\\le\\ln e+1=3$."

add(2, "ב",
    rubric=rub(("הגדרת $f(x)=x\\ln x$ ובדיקת רציפות וגזירות על $[a,b]$", 2),
               ("הפעלת משפט לגרנז': $f'(c)=\\frac{f(b)-f(a)}{b-a}$", 2),
               ("חישוב $f'(x)=\\ln x+1$", 2),
               ("מונוטוניות $\\ln x+1$ וחסימה בין $f'(1)=1$ ל-$f'(e)=2$", 3),
               ("המסקנה", 1)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח את כלל המכפלה: $(x\\ln x)'=\\ln x+x\\cdot\\frac1x=\\ln x+1$.",
              "לשכוח לנמק ש-$\\ln x+1$ עולה, ולכן $c\\in(a,b)\\subseteq[1,e]$ נותן $1\\le\\ln c+1\\le2$.",
              "טעות בערך הקצה: $\\ln e+1=2$ ולא $1$ או $3$."],
    steps=[
        chx("מהי הנגזרת של $f(x)=x\\ln x$?", sp.log(x) + 1, [sp.log(x), 1/x, x*sp.log(x) + 1], lambda e: same(e, f2p),
            "כלל המכפלה: $1\\cdot\\ln x+x\\cdot\\frac1x=\\ln x+1$ (אומת ב-sympy)."),
        num("מהו $f'(e)=\\ln e+1$?", 2, "$\\ln e=1$ ולכן $f'(e)=2$."),
        order("סדרו את שלבי ההוכחה.", L2, "לגרנז', חישוב הנגזרת, חסימה באמצעות מונוטוניות, מסקנה. כל שלב נשען על קודמו."),
        findbug("בהוכחה שורה אחת שגויה. מצאו אותה.", L2b, 2,
                "$\\ln e+1=1+1=2$ ולא $3$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q3a: lim (4/(1+sqrt(9+x)))^(1/sin x) =====
base3 = 4/(1 + sp.sqrt(9 + x))
expo3 = sp.log(base3)/sp.sin(x)
e3 = sp.limit(expo3, x, 0)
assert e3 == R(-1, 24) and same(sp.limit(base3**(1/sp.sin(x)), x, 0), sp.exp(R(-1, 24)))
inner3 = (3 - sp.sqrt(9 + x))/((1 + sp.sqrt(9 + x))*sp.sin(x))
assert sp.limit(inner3, x, 0) == R(-1, 24) and sp.limit(base3, x, 0) == 1

add(3, "א",
    rubric=rub(("זיהוי $1^{\\infty}$ והצגת הבסיס כ-$1+\\frac{3-\\sqrt{9+x}}{1+\\sqrt{9+x}}$", 3),
               ("הגבול המפורסם $\\left(1+u\\right)^{1/u}\\to e$", 2),
               ("חישוב המעריך $\\lim\\frac{3-\\sqrt{9+x}}{(1+\\sqrt{9+x})\\sin x}=-\\frac1{24}$ (כפל בצמוד ו-$\\frac{x}{\\sin x}\\to1$)", 3),
               ("הערך הסופי $e^{-1/24}$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לטעון שהגבול הוא $1$ כי הבסיס שואף ל-$1$.",
              "לשכוח את הסימן במונה $3-\\sqrt{9+x}=\\frac{-x}{3+\\sqrt{9+x}}$ ולקבל $+\\frac1{24}$.",
              "לשכוח את הגורם $\\frac{x}{\\sin x}\\to1$ בחישוב המעריך."],
    steps=[
        ch("מה סוג הצורה הלא מסוימת של $\\left(\\frac{4}{1+\\sqrt{9+x}}\\right)^{1/\\sin x}$ כאשר $x\\to0$?", "$1^{\\infty}$",
           ["$0^0$", "$\\infty^0$", "$\\frac00$"],
           "הבסיס $\\frac{4}{1+3}=1$ והמעריך $\\frac1{\\sin x}\\to\\pm\\infty$."),
        num("מהו הגבול של המעריך החדש $\\frac{3-\\sqrt{9+x}}{(1+\\sqrt{9+x})\\sin x}$ כאשר $x\\to0$? (עשרוני)", e3,
            "$3-\\sqrt{9+x}=\\frac{-x}{3+\\sqrt{9+x}}$ ולכן הגבול $-\\frac{1}{4\\cdot6}=-\\frac1{24}\\approx-0.04167$ (sympy)."),
        num("מהו ערך הגבול המבוקש? (עשרוני)", sp.exp(R(-1, 24)), "$L=e^{-1/24}\\approx0.9592$ (sympy).", tol=0.0005),
    ],
    stepsSource="ai-draft")

# ===== Q3b: int tan x / (cos^2 x e^{2 tan x}) =====
g3b = sp.tan(x)/(sp.cos(x)**2*sp.exp(2*sp.tan(x)))
F3b = -(2*sp.tan(x) + 1)/(4*sp.exp(2*sp.tan(x)))
assert same(sp.diff(F3b, x), g3b)
tq = sp.Symbol('tq', real=True)
F3w = [-(2*sp.tan(x) - 1)/(4*sp.exp(2*sp.tan(x))), (2*sp.tan(x) + 1)/(4*sp.exp(2*sp.tan(x))), -(2*sp.tan(x) + 1)/(2*sp.exp(2*sp.tan(x)))]
tint_ok = lambda e: same(sp.expand(e), sp.expand(tq*sp.exp(-2*tq)))

add(3, "ב",
    rubric=rub(("הצבה $t=\\tan x$ עם $dt=\\frac{dx}{\\cos^2x}$", 3),
               ("מעבר ל-$\\int te^{-2t}dt$", 1),
               ("אינטגרציה בחלקים: $u=t$, $dv=e^{-2t}dt$", 4),
               ("חזרה ל-$x$: $-\\frac{2\\tan x+1}{4e^{2\\tan x}}+C$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח לזהות את $\\frac{dx}{\\cos^2x}$ כ-$dt$.",
              "בבחירת $v$ לשכוח את המקדם: $\\int e^{-2t}dt=-\\frac12e^{-2t}$.",
              "טעות סימן באינטגרל הנותר: $+\\frac12\\int e^{-2t}dt=-\\frac14e^{-2t}$."],
    steps=[
        ch("איזו הצבה מתאימה לאינטגרל $\\int\\frac{\\tan x}{\\cos^2x\\cdot e^{2\\tan x}}dx$?", "$t=\\tan x$",
           ["$t=\\cos x$", "$t=e^{2\\tan x}$", "$t=\\cos^2x$"],
           "$dt=\\frac{dx}{\\cos^2x}$ מופיע באינטגרל, וכל השאר ביטוי ב-$\\tan x$."),
        chx("מהו האינטגרנד אחרי ההצבה (האינטגרל ב-$dt$)?", tq*sp.exp(-2*tq),
            [tq*sp.exp(2*tq), tq**2*sp.exp(-2*tq), sp.exp(-2*tq)], tint_ok,
            "$\\frac{\\tan x}{e^{2\\tan x}}\\cdot\\frac{dx}{\\cos^2x}=te^{-2t}dt$."),
        chx("מהו האינטגרל? (בלי הקבוע)", F3b, F3w, lambda e: same(sp.diff(e, x), g3b),
            "$-\\frac12te^{-2t}-\\frac14e^{-2t}$ עם $t=\\tan x$. הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-draft")

# ===== Q4a: extrema of x * cbrt(x^2-1) on [0,3] =====
import mpmath as mpm
mpm.mp.dps = 30
fcb = lambda v: v*sp.real_root(v**2 - 1, 3)
fcb_m = lambda v: v*mpm.cbrt(v**2 - 1) if v**2 >= 1 else -v*mpm.cbrt(1 - v**2)
dfm = lambda v: mpm.diff(fcb_m, v)
fp_form = lambda v: (5*v**2 - 3)/(3*(sp.real_root(v**2 - 1, 3))**2)
for v in (R(1, 2), R(3, 10), 2, R(5, 2)):
    assert abs(float(dfm(mpm.mpf(v.p)/v.q if hasattr(v, 'p') else mpm.mpf(v))) - float(sp.N(fp_form(v)))) < 1e-8
cp4 = sp.sqrt(R(3, 5))
v4 = {0: sp.N(fcb(0), 15), 1: sp.N(fcb(1), 15), 3: sp.N(fcb(3), 15), 'c': sp.N(fcb(cp4), 15)}
assert abs(float(v4['c']) + float(sp.root(540, 6))/5) < 1e-9 and abs(float(v4[3]) - 6) < 1e-9 and v4[0] == 0 and v4[1] == 0
assert min(v4.values()) == v4['c'] and max(v4.values()) == v4[3]

add(4, "א",
    rubric=rub(("נגזרת $f'(x)=\\frac{5x^2-3}{3\\left(x^2-1\\right)^{2/3}}$", 3),
               ("נקודות חשודות: $x=\\sqrt{\\frac35}$ ($f'=0$) ו-$x=1$ (הנגזרת לא מוגדרת, הפונקציה מוגדרת)", 3),
               ("ערכי הפונקציה בנקודות החשודות ובקצוות: $0,\\,-\\frac15\\sqrt[6]{540},\\,0,\\,6$", 2),
               ("מקסימום $6$ ומינימום $-\\frac15\\sqrt[6]{540}$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח את $x=1$ כנקודה חשודה: שם המכנה מתאפס אבל $f(1)=0$ מוגדרת.",
              "לחשב $\\sqrt[3]{\\frac35-1}$ כשורש של מספר שלילי בצורה שגויה; השורש הממשי הוא $-\\sqrt[3]{\\frac25}$.",
              "לשכוח לבדוק את הקצוות $x=0$ ו-$x=3$."],
    steps=[
        num("מהו ערך $x$ בקטע $(0,3)$ שבו $f'(x)=0$? (עשרוני)", cp4, "$5x^2-3=0$ נותן $x=\\sqrt{\\frac35}\\approx0.7746$."),
        ch("מדוע $x=1$ נבדקת כנקודה חשודה?", "הנגזרת לא מוגדרת שם אבל הפונקציה מוגדרת",
           ["הנגזרת מתאפסת שם", "הפונקציה לא מוגדרת שם", "זו נקודת קצה של הקטע"],
           "ב-$x=1$ המכנה $\\left(x^2-1\\right)^{2/3}$ מתאפס, אבל $f(1)=0$ מוגדרת. הנגזרת מתאפסת ב-$\\sqrt{\\frac35}$ בלבד, ו-$1$ אינה קצה של $[0,3]$."),
        num("מהו $f\\left(\\sqrt{\\frac35}\\right)$? (עשרוני)", v4['c'], "$-\\frac15\\sqrt[6]{540}\\approx-0.5707$ (sympy)."),
        num("מהו הערך הגדול ביותר של הפונקציה בקטע?", 6, "$f(3)=3\\sqrt[3]{8}=6$, הגדול מבין $0,\\,-0.5707,\\,0,\\,6$."),
    ],
    stepsSource="ai-draft")

# ===== Q4b: tangent of (x-3)^sqrt(x) at x=4 =====
f4 = (x - 3)**sp.sqrt(x)
f4p = sp.diff(f4, x)
assert f4.subs(x, 4) == 1 and sp.simplify(f4p.subs(x, 4)) == 2
tang_ok = lambda e: e.subs(x, 4) == 1 and sp.diff(e, x) == 2

add(4, "ב",
    rubric=rub(("כתיבה כ-$e^{\\sqrt x\\ln(x-3)}$ (או גזירה לוגריתמית)", 3),
               ("נגזרת $f'(x)=(x-3)^{\\sqrt x}\\left(\\frac{\\ln(x-3)}{2\\sqrt x}+\\frac{\\sqrt x}{x-3}\\right)$", 3),
               ("ערכים $f(4)=1$ ו-$f'(4)=2$", 2),
               ("משוואת המשיק $y=1+2(x-4)$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לגזור כאילו המעריך קבוע (כלל חזקה) או כאילו הבסיס קבוע (כלל מעריכית).",
              "לשכוח את הנגזרת של $\\sqrt x\\ln(x-3)$ כמכפלה.",
              "לשכוח ש-$\\ln(4-3)=0$ ולכן האיבר הראשון מתאפס."],
    steps=[
        ch("באיזו שיטה גוזר הפתרון הרשמי את $(x-3)^{\\sqrt x}$?", "כותב $e^{\\sqrt x\\ln(x-3)}$ וגוזר עם כלל השרשרת והמכפלה",
           ["כלל החזקה: $\\sqrt x\\,(x-3)^{\\sqrt x-1}$", "כלל המעריכית: $(x-3)^{\\sqrt x}\\ln(x-3)$", "גוזר את הבסיס בלבד"],
           "הפתרון הרשמי כותב $e^{\\sqrt x\\ln(x-3)}$. כלל החזקה תקף רק כשהמעריך קבוע וכלל המעריכית רק כשהבסיס קבוע, וכאן שניהם תלויים ב-$x$."),
        num("מהו $f(4)$?", 1, "$(4-3)^{\\sqrt4}=1$."),
        num("מהו שיפוע המשיק $f'(4)$?", 2, "$1\\cdot\\left(\\frac{\\ln1}{4}+\\frac{2}{1}\\right)=2$ (sympy)."),
        chx("מהי משוואת המשיק בנקודה $x=4$?", 1 + 2*(x - 4), [1 + (x - 4), 2 + 2*(x - 4), 1 - 2*(x - 4)], tang_ok,
            "המשיק עובר דרך $(4,1)$ עם שיפוע $2$: $y=1+2(x-4)$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q5a: lim 1/((sqrt(2x-1)-sqrt(2x-3)) sqrt(x+1)) =====
orig5 = 1/((sp.sqrt(2*x - 1) - sp.sqrt(2*x - 3))*sp.sqrt(x + 1))
simp5 = (sp.sqrt(2*x - 1) + sp.sqrt(2*x - 3))/(2*sp.sqrt(x + 1))
for v in (3, 10, 50):
    assert abs(float(sp.N(orig5.subs(x, v) - simp5.subs(x, v)))) < 1e-9
assert sp.limit(simp5, x, sp.oo) == sp.sqrt(2)
num_ok5 = lambda e: all(abs(float(sp.N(e.subs(x, v) - orig5.subs(x, v)))) < 1e-9 for v in (3, 10, 50))
bads5 = [(sp.sqrt(2*x - 1) + sp.sqrt(2*x - 3))/sp.sqrt(x + 1), (sp.sqrt(2*x - 1) - sp.sqrt(2*x - 3))/(2*sp.sqrt(x + 1)),
         (sp.sqrt(2*x - 1) + sp.sqrt(2*x - 3))/(2*(x + 1))]
assert num_ok5(simp5) and not any(num_ok5(w) for w in bads5)

add(5, "א",
    rubric=rub(("כפל בצמוד $\\sqrt{2x-1}+\\sqrt{2x-3}$", 3),
               ("פישוט המכנה $(2x-1)-(2x-3)=2$", 2),
               ("הוצאת $\\sqrt x$ מהמונה והמכנה וצמצום", 3),
               ("ערך הגבול $\\sqrt2$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לטעות בחישוב $(2x-1)-(2x-3)$: התוצאה $2$ ולא $-4$.",
              "להציב $\\infty$ ישירות במכנה $\\sqrt{2x-1}-\\sqrt{2x-3}$ (צורה $\\infty-\\infty$) בלי כפל בצמוד.",
              "לשכוח שמוציאים $\\sqrt x$ גם מהמכנה $\\sqrt{x+1}$."],
    steps=[
        ch("איך מתמודדים עם $\\sqrt{2x-1}-\\sqrt{2x-3}$ במכנה כאשר $x\\to\\infty$?", "כפל בצמוד $\\sqrt{2x-1}+\\sqrt{2x-3}$",
           ["לופיטל ישירות", "כפל ב-$\\sqrt{2x-1}-\\sqrt{2x-3}$", "העלאה בריבוע של הביטוי כולו"],
           "כפל בצמוד נותן הפרש ריבועים $(2x-1)-(2x-3)=2$. כפל בביטוי עצמו או הריבוע לא מבטלים את השורשים."),
        num("מהו $(2x-1)-(2x-3)$?", 2, "$2x-1-2x+3=2$."),
        chx("מהו הביטוי אחרי הכפל בצמוד והפישוט?", simp5, bads5, num_ok5,
            "$\\frac{\\sqrt{2x-1}+\\sqrt{2x-3}}{2\\sqrt{x+1}}$ (נבדק נומרית ב-sympy מול הביטוי המקורי ב-$x=3,10,50$)."),
        num("מהו ערך הגבול? (עשרוני)", sp.sqrt(2), "$\\frac{2\\sqrt2}{2}=\\sqrt2\\approx1.4142$ (sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q5b: partial fractions =====
g5 = (2*x**2 - x + 1)/((x - 1)*(x**2 + 1))
A5, B5, C5 = sp.symbols('A5 B5 C5')
s5 = sp.solve(sp.Poly(sp.expand(A5*(x**2 + 1) + (B5*x + C5)*(x - 1) - (2*x**2 - x + 1)), x).all_coeffs(), [A5, B5, C5], dict=True)[0]
assert s5 == {A5: 1, B5: 1, C5: 0}
F5 = sp.log(x - 1) + sp.log(x**2 + 1)/2
assert same(sp.diff(F5, x), g5)
F5w = [sp.log(x - 1) + sp.log(x**2 + 1), sp.log(x - 1) + sp.atan(x), 2*sp.log(x - 1) + sp.log(x**2 + 1)/2]

add(5, "ב",
    rubric=rub(("פירוק $\\frac{A}{x-1}+\\frac{Bx+C}{x^2+1}$", 2),
               ("השוואת מקדמים: $A+B=2$, $-B+C=-1$, $A-C=1$", 3),
               ("הפתרון $A=1$, $B=1$, $C=0$", 2),
               ("אינטגרציה: $\\ln|x-1|+\\frac12\\ln\\left(x^2+1\\right)+C$", 3)),
    rubricSource="ai-draft",
    pitfalls=["לכתוב מונה קבוע $\\frac{B}{x^2+1}$ במקום מונה לינארי $Bx+C$.",
              "לשכוח את הגורם $\\frac12$ באינטגרל $\\int\\frac{x}{x^2+1}dx=\\frac12\\ln\\left(x^2+1\\right)$.",
              "לכתוב $\\ln(x-1)$ בלי ערך מוחלט כשהתחום כולל גם $x<1$."],
    steps=[
        num("מהו המקדם $A$ בפירוק? (הצבת $x=1$)", s5[A5], "$2-1+1=A\\cdot2$ ולכן $A=1$ (sympy)."),
        num("מהו המקדם $B$?", s5[B5], "מהמקדם של $x^2$: $A+B=2$ ולכן $B=1$."),
        num("מהו המקדם $C$?", s5[C5], "מהמקדם החופשי: $A-C=1$ ולכן $C=0$ (sympy)."),
        chx("מהו האינטגרל? (עבור $x>1$, בלי הקבוע)", F5, F5w, lambda e: same(sp.diff(e, x), g5),
            "$\\int\\left(\\frac{1}{x-1}+\\frac{x}{x^2+1}\\right)dx=\\ln(x-1)+\\frac12\\ln\\left(x^2+1\\right)$. הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-draft")

# ===== Q6a: volume about the y-axis =====
V6 = sp.integrate(2*sp.pi*x*(1 - (sp.exp(x) - 1)), (x, 0, sp.log(2)))
assert same(V6, 2*sp.pi*(1 - sp.log(2))**2)
cyl6 = sp.pi*sp.log(2)**2
assert same(cyl6 - 2*sp.pi*sp.integrate(x*(sp.exp(x) - 1), (x, 0, sp.log(2))), V6)
xe6 = sp.integrate(x*sp.exp(x), (x, 0, sp.log(2)))
assert same(xe6, 2*sp.log(2) - 1)
vk = lambda g: abs(float(sp.N(sp.integrate(g, (x, 0, sp.log(2))) - V6))) < 1e-9
bads6 = [2*sp.pi*x*(sp.exp(x) - 1), 2*sp.pi*x*(1 + sp.exp(x) - 1), sp.pi*x**2*(2 - sp.exp(x))]
assert vk(2*sp.pi*x*(2 - sp.exp(x))) and not any(vk(w) for w in bads6)
assert sp.solve(sp.Eq(sp.exp(x) - 1, 1), x) == [sp.log(2)]

add(6, "א",
    rubric=rub(("גבולות התחום: $x=0$ עד $x=\\ln2$ (חיתוך $e^x-1=1$)", 2),
               ("הצבת נפח בשיטת הקונכיות או כהפרש גליל פחות קונכיות", 4),
               ("אינטגרציה בחלקים של $\\int xe^xdx$", 2),
               ("הערך $V=2\\pi(1-\\ln2)^2$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח את הגורם $x$ (רדיוס הקונכייה) באינטגרנד.",
              "לקחת גובה קונכייה $e^x-1$ במקום $1-\\left(e^x-1\\right)$: התחום נמצא בין העקומה לישר $y=1$.",
              "לחשב את הנפח של הגליל $\\pi(\\ln2)^2$ בלבד, בלי להחסיר את מה שמתחת לעקומה."],
    steps=[
        num("מהו ערך $x$ שבו $y=e^x-1$ פוגש את $y=1$? (עשרוני)", sp.log(2), "$e^x=2$ ולכן $x=\\ln2\\approx0.6931$."),
        chx("מהו האינטגרנד בשיטת הקונכיות (אינטגרציה על $x$ מ-$0$ עד $\\ln2$)?", 2*sp.pi*x*(2 - sp.exp(x)), bads6, vk,
            "רדיוס $x$, גובה $1-\\left(e^x-1\\right)=2-e^x$. רק האינטגרנד הנכון נותן את הנפח הרשמי (נבדק ב-sympy)."),
        num("מהו $\\int_0^{\\ln2}xe^x\\,dx$? (עשרוני)", xe6, "$\\left(xe^x-e^x\\right)\\Big|_0^{\\ln2}=2\\ln2-2+1=2\\ln2-1\\approx0.3863$ (sympy)."),
        num("מהו הנפח? (עשרוני)", V6, "$V=2\\pi(1-\\ln2)^2\\approx0.5916$ (sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q6b: area between y=x, y=x/2, y=1/x =====
S6 = sp.integrate(x - x/2, (x, 0, 1)) + sp.integrate(1/x - x/2, (x, 1, sp.sqrt(2)))
assert same(S6, sp.log(2)/2)
assert sp.solve(sp.Eq(x, 1/x), x) == [1] or sorted(sp.solve(sp.Eq(x**2, 1), x))[-1] == 1
assert sp.solve(sp.Eq(x/2, 1/x), x)[-1] == sp.sqrt(2)
assert (1/R(3, 2) < R(3, 2)) and (1/R(1, 2) > R(1, 2))  # above y=1/x for x>1 it is y=x; the bound switches at x=1

add(6, "ב",
    rubric=rub(("נקודות החיתוך: $x=1$ (בין $y=x$ ל-$y=\\frac1x$) ו-$x=\\sqrt2$ (בין $y=\\frac x2$ ל-$y=\\frac1x$)", 3),
               ("פיצול התחום ב-$x=1$ וקביעת הגבול העליון בכל קטע", 2),
               ("חישוב שני האינטגרלים: $\\frac14$ ו-$\\ln\\sqrt2-\\frac14$", 3),
               ("הערך $S=\\frac12\\ln2$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לא לפצל את התחום: הגבול העליון משתנה מ-$y=x$ ל-$y=\\frac1x$ ב-$x=1$.",
              "להשתמש בגבול העליון $x=2$ בטעות: ההיפרבולה פוגשת את $y=\\frac x2$ ב-$x=\\sqrt2$.",
              "לשכוח ש-$\\int\\frac{dx}{x}=\\ln x$ ו-$\\ln\\sqrt2=\\frac12\\ln2$."],
    steps=[
        num("באיזה ערך $x$ חיובי מתחתכים $y=x$ ו-$y=\\frac1x$?", 1, "$x=\\frac1x$ נותן $x^2=1$ ולכן $x=1$ (בתחום $x>0$)."),
        num("באיזה ערך $x$ מתחתכים $y=\\frac x2$ ו-$y=\\frac1x$? (עשרוני)", sp.sqrt(2), "$\\frac x2=\\frac1x$ נותן $x^2=2$ ולכן $x=\\sqrt2\\approx1.4142$."),
        num("מהו $\\int_0^1\\left(x-\\frac x2\\right)dx$? (עשרוני)", R(1, 4), "$\\frac14x^2\\Big|_0^1=\\frac14$."),
        num("מהו השטח הכלוא? (עשרוני)", S6, "$\\frac14+\\left(\\ln\\sqrt2-\\frac12+\\frac14\\right)=\\frac12\\ln2\\approx0.3466$ (sympy).", tol=0.0005),
    ],
    stepsSource="ai-draft")


exam = {
    "examCode": "19A-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ט, מועד א' (גרסה 1)",
    "year": 2019,
    "examDate": "26/02/2019",
    "sourceFile": "calculus-1/19A-A exam+solution.pdf",
    "solutionFile": "calculus-1/19A-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

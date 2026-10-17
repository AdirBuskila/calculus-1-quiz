# -*- coding: utf-8 -*-
"""Generator for tools/raw/24B-A.json -- calculus-1 (20151), semester A 2024, moed B (03/04/2024).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24B-A.py

Source: sitting 24B-A, pp.1-7 (exam with the official solution after each question; Q1, Q3, Q4a, Q5a are
handwritten, the rest typed). Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Q1 is one item (single instruction list); the handwritten sketch is shipped as images/exams/24B-A-Q1-sketch.png.
- Q1: the handwritten convexity table only shows the sign of f'' (negative on both sides, no inflection); the words
  'convex (downward)' and the endpoint-free summary are the transcriber's reading of that table.
- Q1 solution: the official page writes f''' = -6/x^4 where f'' is meant; transcribed as f''.
- Q3 is split into four items (printed roman numerals i-iv, stored as parts א-ד); the official solution computes both one-sided limits once, so the
  shared computation is repeated in each part.
- Q3: the middle limit of the left-sided computation is printed with x->0+ in the official page; written as 0^- here.
- Q5b: the official page prints "x_2=-1, x_2=3" (second index is a typo for x_1,x_2); transcribed as x_1,x_2.
- Q6b: the official page writes f'(x) where y'(x) is meant; transcribed as y'.

Checks (tools/verify/24B-A/check.py, sympy): every derivative, limit, integral, area and extremum value matches
the official answers. 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24B-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**תחום הגדרה:** $x\neq 0$.
**נקודות חיתוך עם הצירים:** חיתוך עם ציר ה-$x$: $x=1$, כי $\frac{x^3-1}{x^2}=0$, כלומר הנקודה $(1,0)$. אין חיתוך עם ציר ה-$y$.
**נגזרת:** $f(x)=\frac{x^3-1}{x^2}=\frac{x^3}{x^2}-\frac{1}{x^2}=x-\frac{1}{x^2}$, ו-$f'(x)=1+\frac{2}{x^3}=0\Rightarrow x=-\sqrt[3]{2}$. $f''(x)=-\frac{6}{x^4}=0\Rightarrow\emptyset$.
**תחומי עליה וירידה:** $f'>0$ כאשר $x<-\sqrt[3]{2}$ או $x>0$ (הפונקציה עולה); $f'<0$ כאשר $-\sqrt[3]{2}<x<0$ (הפונקציה יורדת).
**קיצון:** $\left(-\sqrt[3]{2},\,\frac{-3}{\sqrt[3]{4}}\right)$ (נקודת מקסימום מקומי).
**תחומי קמירות וקעירות, נקודות פיתול:** $f''<0$ משני צדי $x=0$ (אין שינוי סימן ב-$f''$), לכן הפונקציה קמורה (כלפי מטה) בכל תחום ההגדרה ואין נקודות פיתול.
**אסימפטוטות אנכיות:** $x=0$. מתקיים $\lim_{x\to0^+}\frac{x^3-1}{x^2}=-\infty$ וגם $\lim_{x\to0^-}\frac{x^3-1}{x^2}=-\infty$, ולכן $x=0$ היא אסימפטוטה אנכית.
**אסימפטוטות משופעות, ב-$\infty$:**
$$a=\lim_{x\to\infty}\frac{f(x)}{x}=\lim_{x\to\infty}\frac{x^3-1}{x^2}\cdot\frac{1}{x}=\lim_{x\to\infty}\frac{x^3-1}{x^3}=1$$
$$b=\lim_{x\to\infty}\left(f(x)-ax\right)=\lim_{x\to\infty}\left(\frac{x^3-1}{x^2}-1\cdot x\right)=\lim_{x\to\infty}\frac{-1}{x^2}=0$$
אסימפטוטה משופעת ב-$\infty$: $y=1x+0$. באופן דומה ב-$-\infty$: $y=x$.
**שרטוט:**
![שרטוט הגרף של הפונקציה עם האסימפטוטות x=0 ו-y=x](images/exams/24B-A-Q1-sketch.png)
"""

SOL2A = r"""
$$\int\frac{x}{(x+1)(x^2+1)}dx\overset{(*)}{=}\frac{1}{2}\int\left(\frac{-1}{x+1}+\frac{x+1}{x^2+1}\right)dx=-\frac{1}{2}\ln|x+1|+\frac{1}{4}\int\frac{2x+2}{x^2+1}dx$$
$$=-\frac{1}{2}\ln|x+1|+\frac{1}{4}\ln|x^2+1|+\frac{1}{4}\cdot 2\cdot\arctan x+c$$
"""

SOL2B = r"""
נרצה להוכיח ש-$\ln(1+x)<x$. כעת נגדיר את פונקציית העזר $f(x)=x-\ln(1+x)$ ונוכיח כי $f(x)>0$ לכל $x>0$.
אכן, $f(0)=0$, $f$ גזירה לכל $x>0$ והנגזרת היא $f'(x)=1-\frac{1}{1+x}=\frac{x}{1+x}>0$.
אזי $f'(x)>0$ לכל $x>0$, ולכן $f$ עולה בקטע $[0,\infty)$, כלומר, $f(x)>f(0)=0$ לכל $x>0$.
"""

CTX3 = r"""נתונה פונקציה:
$$f(x)=\begin{cases}\frac{\sin bx}{x+\sin 2x}, & x<0\\ 2a-7, & x=0\\ x\ln x, & x>0\end{cases}$$
מצאו (אם קיימים) את כל הערכים של הפרמטרים $a,b$ ממשיים עבורם:
אם לא קיימים ערכים כנדרש, רשום "לא קיימים" והסבר מדוע."""

SOL3_COMMON = r"""נחשב את הגבולות החד-צדדיים בנקודה $x=0$:
$$\lim_{x\to0^-}f(x)=\lim_{x\to0^-}\frac{\sin bx}{x+\sin 2x}=\lim_{x\to0^-}\frac{\frac{\sin bx}{x}}{1+\frac{\sin 2x}{x}}=\frac{b}{3}$$
(כאשר $\frac{\sin bx}{x}\to b$ ו-$\frac{\sin 2x}{x}\to 2$.)
$$f(0)=2a-7$$
$$\lim_{x\to0^+}x\ln x\ \text{``}0\cdot\infty\text{''}=\lim_{x\to0^+}\frac{\ln x}{\frac{1}{x}}\ \overset{\text{L'H}}{=}\ \lim_{x\to0^+}\frac{\frac{1}{x}}{-\frac{1}{x^2}}=\lim_{x\to0^+}(-x)=0$$
"""

SOL3I = SOL3_COMMON + r"""
$f$ רציפה ב-$0$ אם הגבול בנקודה קיים ושווה לערך הפונקציה בנקודה:
$$2a-7=\frac{b}{3}=0\ \longrightarrow\ b=0,\ a=\frac{7}{2}=3.5$$
"""

SOL3II = SOL3_COMMON + r"""
אי רציפות סליקה: הגבול קיים אך שונה מערך הפונקציה בנקודה:
$$\lim_{x\to0^+}f(x)=\lim_{x\to0^-}f(x)\neq f(0)$$
$$0=\frac{b}{3}\neq 2a-7$$
$$b=0,\quad a\neq\frac{7}{2}$$
"""

SOL3III = SOL3_COMMON + r"""
אי רציפות ממין 1: הגבולות החד-צדדיים קיימים אך שונים:
$$\lim_{x\to0^+}f(x)\neq\lim_{x\to0^-}f(x)$$
$$0\neq\frac{b}{3}\ \to\ b\neq0,\quad a\in\mathbb{R}$$
"""

SOL3IV = SOL3_COMMON + r"""
עבור כל ערך של $a$ ו-$b$ הגבולות החד-צדדיים קיימים. לכן אין ערכים של $a$ ו-$b$ עבורם נקבל אי רציפות ממין II.
"""

SOL4A = r"""
$$\lim_{x\to1}\left(\frac{1}{\ln x}-\frac{1}{x-1}\right)=\lim_{x\to1}\frac{x-1-\ln x}{\ln x\cdot(x-1)}\quad\left\{\text{``}\tfrac{0}{0}\text{''}\right\}\ \overset{\text{L'H}}{=}$$
$$=\lim_{x\to1}\frac{1-\frac{1}{x}}{\frac{1}{x}(x-1)+\ln x}=\lim_{x\to1}\frac{x-1}{x-1+x\ln x}\quad\left\{\text{``}\tfrac{0}{0}\text{''}\right\}\ \overset{\text{L'H}}{=}$$
$$=\lim_{x\to1}\frac{1}{1+\ln x+x\cdot\frac{1}{x}}=\frac{1}{2}.$$
"""

SOL4B = r"""
$$\lim_{x\to0}\frac{\int_0^x\tan t\,dt}{x\sin x}\overset{(*)}{=}\lim_{x\to0}\frac{\tan x}{\sin x+x\cos x}\overset{(**)}{=}\lim_{x\to0}\frac{\frac{\tan x}{x}}{\frac{\sin x}{x}+\cos x}=\frac{1}{2}$$
"""

SOL5A = r"""
אינטגרציה בחלקים עם $u=x^2+2x,\ v'=\cos 2x,\ u'=2x+2,\ v=\frac{\sin 2x}{2}$:
$$\int(x^2+2x)\cos 2x\,dx=(x^2+2x)\cdot\frac{\sin 2x}{2}-\int\frac{(2x+2)\sin 2x}{2}\,dx$$
באינטגרל הנותר, אינטגרציה בחלקים נוספת עם $u=x+1,\ v'=\sin 2x,\ u'=1,\ v=-\frac{\cos 2x}{2}$:
$$=\frac{x^2+2x}{2}\sin 2x+\frac{(x+1)\cos 2x}{2}-\int\frac{\cos 2x}{2}\,dx=\frac{x^2+2x-0.5}{2}\sin 2x+\frac{(x+1)\cos 2x}{2}+c$$
"""

SOL5B = r"""
$$x^2+2=2x+5,\quad x^2-2x-3=0,\quad x_1=-1,\ x_2=3$$
$$S=\int_0^3\left(2x+5-(x^2+2)\right)dx+\int_3^6\left(x^2+2-(2x+5)\right)dx=$$
$$=\left(3x+x^2-\frac{x^3}{3}\right)\Big|_0^3+\left(-3x-x^2+\frac{x^3}{3}\right)\Big|_3^6=36$$
"""

SOL6A = r"""
נגדיר פונקציה $g(x)=e^x-\frac{1}{x}-3$ ו-$x\in(1,1.5)$: $g$ גזירה לכל $x\in(1,1.5)$ ו-$g'(x)=e^x+\frac{1}{x^2}>0$.
הנגזרת תמיד חיובית ולכן הפונקציה מונוטונית עולה.
$$g(1)=e-4<0,\qquad g(1.5)=e^{1.5}-\frac{2}{3}-3>0$$
לכן: למשוואה $e^x-\frac{1}{x}-3=0$ יש פתרון יחיד $c$ בקטע $(1,1.5)$.
"""

SOL6B = r"""
$$x^2+4x-5=0,\ x=-5,\ x=1,\qquad y'(x)=\frac{x^2+4x-5}{(x+2)^2},\qquad D(y)=(-\infty,-2)\cup(-2,+\infty)$$
$$y(10)=\frac{105}{12},\quad y(0)=\frac{5}{2},\quad y(1)=2$$
$$y_{max}=y(10)=\frac{105}{12},\qquad y_{min}=y(1)=2$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה: $f(x)=\frac{x^3-1}{x^2}$ על פי הסעיפים הבאים: תחום הגדרה, חיתוך עם הצירים, תחומי עליה וירידה, "
      "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{x}{(x+1)(x^2+1)}\,dx$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "mean_value_theorems",
      r"הוכיחו $\ln(1+x)<x$ לכל $x>0$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "continuity", r"$f(x)$ תהיה רציפה ב-$x=0$.",
      SOL3I, part="א", points=5, contextId="c3"),
    Q(3, "computation", "continuity", r"$x=0$ תהיה נק' אי-רציפות סליקה.",
      SOL3II, part="ב", points=5, contextId="c3"),
    Q(3, "computation", "continuity", r"$x=0$ תהיה נק' אי-רציפות מסוג ראשון של $f(x)$.",
      SOL3III, part="ג", points=5, contextId="c3"),
    Q(3, "computation", "continuity", r"$x=0$ תהיה נק' אי-רציפות מסוג שני של $f(x)$.",
      SOL3IV, part="ד", points=5, contextId="c3"),

    Q(4, "computation", "lhopital_taylor",
      r"חשבו את הגבול: $\lim_{x\to1}\left(\frac{1}{\ln x}-\frac{1}{x-1}\right)$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "lhopital_taylor",
      r"חשבו את הגבול: $\lim_{x\to0}\frac{\int_0^x\tan t\,dt}{x\sin x}$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int(x^2+2x)\cos 2x\,dx$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "definite_integrals",
      r"מצאו את השטח החסום בין הקווים: $y=x^2+2,\ y=2x+5,\ x=0,\ x=6$.",
      SOL5B, part="ב", points=10),

    Q(6, "proof", "continuity",
      r"הוכיחו כי למשוואה $e^x-\frac{1}{x}-3=0$ יש פתרון יחיד בקטע $(1,1.5)$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "extrema_optimization",
      r"מצאו את המינימום והמקסימום המוחלטים של $y=\frac{x^2+5}{x+2}$ בקטע $[0,10]$.",
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

# ===== Q1: f = (x^3-1)/x^2 =====
f1 = (x**3 - 1)/x**2
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, 1 + 2/x**3) and same(f1pp, -6/x**4)
crit1 = [s for s in sp.solve(sp.Eq(f1p, 0), x) if s.is_real]
assert crit1 == [-sp.cbrt(2)]
xc1 = crit1[0]
fc1 = sp.simplify(f1.subs(x, xc1))
assert same(fc1, -3/sp.cbrt(4))
assert all(f1pp.subs(x, v) < 0 for v in (-5, -1, R(-1, 3), R(1, 3), 2, 7))
sl1 = sp.limit(f1/x, x, sp.oo)
ic1 = sp.limit(f1 - x, x, sp.oo)
assert (sl1, ic1) == (1, 0) and sp.limit(f1 - x, x, -sp.oo) == 0

add(1,
    rubric=rub(("תחום הגדרה ($x\\neq0$) ונקודת חיתוך עם ציר ה-$x$: $(1,0)$, ללא חיתוך עם ציר ה-$y$", 3),
               ("נגזרת $f'(x)=1+\\frac{2}{x^3}$, נקודה קריטית $x=-\\sqrt[3]{2}$ ותחומי עליה וירידה", 5),
               ("סיווג הקיצון (מקסימום מקומי) וחישוב ערכו", 3),
               ("$f''(x)=-\\frac{6}{x^4}<0$: קמירות כלפי מטה בכל התחום, ללא נקודות פיתול", 3),
               ("אסימפטוטה אנכית $x=0$ ואסימפטוטה משופעת $y=x$", 4),
               ("שרטוט הגרף בהתאם לכל הנתונים", 2)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח ש-$x=0$ מחוץ לתחום ההגדרה, ולכן לחלק את תחומי העליה והירידה גם דרכו או להתייחס אליה כנקודת קיצון.",
              "לטעון לנקודת פיתול ב-$x=0$ רק כי $f''$ לא מוגדרת שם. $f''<0$ משני צדי $0$, אין שינוי סימן ולכן אין פיתול.",
              "לפשט לא נכון את $f$: צריך לכתוב $f(x)=x-\\frac{1}{x^2}$ לפני הגזירה, ואז האסימפטוטה המשופעת $y=x$ נראית מיד."],
    steps=[
        chx("מהי הנגזרת של $f(x)=\\frac{x^3-1}{x^2}=x-\\frac{1}{x^2}$?", 1 + 2/x**3,
            [1 - 2/x**3, 1 + 2/x**2, 1 - 1/x**3], lambda e: same(e, f1p),
            "$f(x)=x-x^{-2}$ ולכן $f'(x)=1+2x^{-3}=1+\\frac{2}{x^3}$ (אומת ב-sympy)."),
        num("מהו ערך $x$ של הנקודה הקריטית היחידה של $f$? (עשרוני)", xc1,
            "$1+\\frac{2}{x^3}=0$ נותן $x^3=-2$, כלומר $x=-\\sqrt[3]{2}\\approx-1.2599$.", tol=0.001),
        num("מהו הערך $f\\left(-\\sqrt[3]{2}\\right)$ בנקודת המקסימום המקומי? (עשרוני)", fc1,
            "$f=-\\frac{3}{\\sqrt[3]{4}}\\approx-1.8899$.", tol=0.001),
        ch("מה סימן $f''(x)=-\\frac{6}{x^4}$ בתחום ההגדרה?",
           "שלילי בכל תחום ההגדרה, ולכן אין נקודות פיתול",
           ["חיובי בכל תחום ההגדרה", "שלילי עבור $x<0$ וחיובי עבור $x>0$ ולכן $x=0$ נקודת פיתול", "מתאפס ב-$x=-\\sqrt[3]{2}$"],
           "$x^4>0$ לכל $x\\neq0$, לכן $f''<0$ והפונקציה קמורה כלפי מטה בכל תחום ההגדרה (נבדק ב-sympy)."),
        ch("מהי האסימפטוטה המשופעת של $f$ ב-$+\\infty$?", "$y=x$",
           ["$y=x+1$", "$y=x-1$", "$y=2x$", "אין אסימפטוטה משופעת"],
           "$m=\\lim\\frac{f(x)}{x}=1$ ו-$k=\\lim(f(x)-x)=\\lim\\left(-\\frac{1}{x^2}\\right)=0$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q2a: x/((x+1)(x^2+1)) =====
g2 = x/((x + 1)*(x**2 + 1))
A_, B_, C_ = sp.symbols('A B C')
sol2 = sp.solve(sp.Poly(sp.expand(A_*(x**2 + 1) + (B_*x + C_)*(x + 1) - x), x).all_coeffs(), [A_, B_, C_], dict=True)[0]
assert sol2 == {A_: R(-1, 2), B_: R(1, 2), C_: R(1, 2)}
F2 = -sp.log(x + 1)/2 + sp.log(x**2 + 1)/4 + sp.atan(x)/2
assert same(sp.diff(F2, x), g2)
# the wrong forms cannot represent g2
bad_forms = [A_*(x**2 + 1) + B_*(x + 1) - x, A_*(x**2 + 1) + B_*x*(x + 1) - x]
for bf in bad_forms:
    assert sp.solve(sp.Poly(sp.expand(bf), x).all_coeffs(), [A_, B_], dict=True) == []
F2w = [sp.log(x + 1)/2 + sp.log(x**2 + 1)/4 + sp.atan(x)/2, -sp.log(x + 1)/2 - sp.log(x**2 + 1)/4 + sp.atan(x)/2,
       -sp.log(x + 1)/2 + sp.log(x**2 + 1)/2 + sp.atan(x)]

add(2, "א",
    rubric=rub(("פירוק לשברים חלקיים בצורה $\\frac{A}{x+1}+\\frac{Bx+C}{x^2+1}$", 3),
               ("חישוב המקדמים $A=-\\frac{1}{2}$, $B=C=\\frac{1}{2}$", 3),
               ("אינטגרציה של $\\frac{1}{x+1}$ ושל $\\frac{2x}{x^2+1}$ כלוגריתמים", 2),
               ("אינטגרל $\\frac{1}{x^2+1}$ כ-$\\arctan x$ ותשובה סופית עם $+c$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לכתוב $\\frac{A}{x+1}+\\frac{B}{x^2+1}$ במקום מונה לינארי $Bx+C$ מעל הגורם הריבועי, ואז אין פתרון למערכת.",
              "לאנטגרל $\\int\\frac{x+1}{x^2+1}dx$ לתת רק לוגריתם ולשכוח את החלק $\\int\\frac{1}{x^2+1}dx=\\arctan x$."],
    steps=[
        ch("איזה פירוק לשברים חלקיים מתאים ל-$\\frac{x}{(x+1)(x^2+1)}$?",
           "$\\frac{A}{x+1}+\\frac{Bx+C}{x^2+1}$",
           ["$\\frac{A}{x+1}+\\frac{B}{x^2+1}$", "$\\frac{A}{x+1}+\\frac{Bx}{x^2+1}$"],
           "$x^2+1$ אי-פריק, לכן מעליו מונה לינארי. בשתי האפשרויות האחרות מערכת המקדמים חסרת פתרון (אומת ב-sympy)."),
        num("מהו המקדם $A$ בפירוק? (עשרוני)", sol2[A_],
            "הצבת $x=-1$ ב-$x=A(x^2+1)+(Bx+C)(x+1)$ נותנת $-1=2A$, כלומר $A=-\\frac{1}{2}$.", tol=0.0005),
        chx("מהו האינטגרל? (בתחום $x>-1$, בלי הקבוע)", F2, F2w, lambda e: same(sp.diff(e, x), g2),
            "אחרי הפירוק מקבלים $-\\frac{1}{2}\\ln(x+1)+\\frac{1}{4}\\ln(x^2+1)+\\frac{1}{2}\\arctan x$; הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-draft")

# ===== Q2b: ln(1+x) < x =====
h2 = x - sp.log(1 + x)
h2p = sp.diff(h2, x)
assert same(h2p, x/(1 + x)) and h2.subs(x, 0) == 0
L2 = ["נגדיר $f(x)=x-\\ln(1+x)$ ונוכיח ש-$f(x)>0$ לכל $x>0$.",
      "מתקיים $f(0)=0$ ו-$f'(x)=1-\\frac{1}{1+x}=\\frac{x}{1+x}$.",
      "לכל $x>0$ מתקיים $f'(x)>0$, ולכן $f$ עולה ממש בקטע $[0,\\infty)$.",
      "לכן $f(x)>f(0)=0$ לכל $x>0$, כלומר $\\ln(1+x)<x$."]
L2b = list(L2)
L2b[1] = "מתקיים $f(0)=0$ ו-$f'(x)=1-(1+x)=-x$."
assert not same(1 - (1 + x), h2p)

add(2, "ב",
    rubric=rub(("הגדרת פונקציית עזר מתאימה $f(x)=x-\\ln(1+x)$ והמטרה $f(x)>0$", 2),
               ("חישוב $f(0)=0$", 1),
               ("חישוב הנגזרת $f'(x)=\\frac{x}{1+x}$ והצגת חיוביותה לכל $x>0$", 4),
               ("מסקנה: $f$ עולה ולכן $f(x)>f(0)=0$ ומכאן אי-השוויון", 3)),
    rubricSource="ai-draft",
    pitfalls=["להציב כמה ערכים מספריים ל-$x$ ולהסיק שאי-השוויון נכון. זו לא הוכחה.",
              "לשכוח לבדוק את $f(0)=0$, שבלעדיו מונוטוניות לבדה לא נותנת $f(x)>0$.",
              "טעות בנגזרת של $\\ln(1+x)$: היא $\\frac{1}{1+x}$ ולא $\\frac{1}{x}$."],
    steps=[
        ch("איזו פונקציית עזר מגדיר הפתרון הרשמי כדי להוכיח את אי-השוויון?", "$f(x)=x-\\ln(1+x)$",
           ["$f(x)=x+\\ln(1+x)$", "$f(x)=x\\cdot\\ln(1+x)$", "$f(x)=e^x-1-x$"],
           "הפתרון הרשמי מוכיח ש-$x-\\ln(1+x)>0$, כלומר מגדיר $f(x)=x-\\ln(1+x)$."),
        num("מהו הערך של $f'(1)$ עבור פונקציית העזר? (עשרוני)", h2p.subs(x, 1),
            "$f'(x)=\\frac{x}{1+x}$ ולכן $f'(1)=\\frac{1}{2}=0.5$.", tol=0.0005),
        order("סדרו את שלבי ההוכחה.", L2, "הגדרה, ערך ונגזרת, חיוביות הנגזרת ומונוטוניות, ובסוף המסקנה. כל שלב נשען על קודמו."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L2b, 1,
                "הנגזרת של $x-\\ln(1+x)$ היא $1-\\frac{1}{1+x}$ ולא $1-(1+x)$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q3: continuity of f with parameters a,b =====
left3 = sp.limit(sp.sin(b*x)/(x + sp.sin(2*x)), x, 0, '-')
right3 = sp.limit(x*sp.log(x), x, 0, '+')
assert sp.simplify(left3 - b/3) == 0 and right3 == 0
s3 = sp.solve([2*a - 7, b/3], [a, b], dict=True)[0]
assert s3 == {a: R(7, 2), b: 0}
lt = lambda bv: sp.limit(sp.sin(bv*x)/(x + sp.sin(2*x)), x, 0, '-')
assert lt(6) == 2 and lt(-9) == -3 and lt(3) == 1


def kind3(av, bv):
    L, Rr, f0 = lt(bv), 0, 2*av - 7
    if L == Rr == f0:
        return "cont"
    if L == Rr:
        return "removable"
    return "first"


assert kind3(R(7, 2), 0) == "cont" and kind3(4, 0) == "removable" and kind3(0, 0) == "removable"
assert all(kind3(av, 3) == "first" for av in (0, R(7, 2), 10))
assert kind3(R(7, 2), 1) == "first" and kind3(1, 0) != "first"

add(3, "א",
    rubric=rub(("חישוב הגבול השמאלי $\\frac{b}{3}$ (לפי $\\frac{\\sin bx}{x}\\to b$ ו-$\\frac{\\sin2x}{x}\\to2$)", 2),
               ("חישוב הגבול הימני $\\lim_{x\\to0^+}x\\ln x=0$ (לופיטל)", 1),
               ("דרישת רציפות $2a-7=\\frac{b}{3}=0$", 1),
               ("פתרון: $b=0$, $a=\\frac{7}{2}$", 1)),
    rubricSource="ai-draft",
    pitfalls=["להשאיר את $x\\ln x$ כ-$0\\cdot\\infty$ בלי להפוך למנה ולהפעיל לופיטל.",
              "לדרוש רק שהגבול השמאלי שווה ל-$f(0)$ ולשכוח את הגבול הימני."],
    steps=[
        num("מהו $\\lim_{x\\to0^-}\\frac{\\sin bx}{x+\\sin2x}$ עבור $b=6$?", lt(6),
            "$\\frac{\\sin6x}{x}\\to6$ ו-$1+\\frac{\\sin2x}{x}\\to3$, לכן הגבול הוא $\\frac{6}{3}=2$ (בכלל: $\\frac{b}{3}$)."),
        num("מהו $\\lim_{x\\to0^+}x\\ln x$?", right3, "$x\\ln x=\\frac{\\ln x}{1/x}\\to\\frac{1/x}{-1/x^2}=-x\\to0$."),
        num("מהו הערך של $b$ המבטיח רציפות?", s3[b], "הגבול הימני הוא $0$, לכן $\\frac{b}{3}=0$ ו-$b=0$."),
        num("מהו הערך של $a$ המבטיח רציפות? (עשרוני)", s3[a], "$f(0)=2a-7=0$, לכן $a=\\frac{7}{2}=3.5$."),
    ],
    stepsSource="ai-draft")

add(3, "ב",
    rubric=rub(("חישוב שני הגבולות החד-צדדיים: $\\frac{b}{3}$ ו-$0$", 2),
               ("תנאי אי-רציפות סליקה: הגבולות שווים, לכן $b=0$", 1),
               ("הגבול שונה מ-$f(0)=2a-7$, לכן $a\\neq\\frac{7}{2}$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח שבאי-רציפות סליקה הגבול חייב להתקיים (שני הצדדים שווים) ורק להיות שונה מ-$f(0)$.",
              "לכתוב $a=\\frac{7}{2}$ כתנאי: זה בדיוק מקרה הרציפות ולא הסליקה."],
    steps=[
        num("מהו הערך של $b$ שבו שני הגבולות החד-צדדיים שווים?", 0, "הגבול הימני $0$, השמאלי $\\frac{b}{3}$, לכן $b=0$."),
        ch("מה התנאי על $a$ לאי-רציפות סליקה (כאשר $b=0$)?", "$a\\neq\\frac{7}{2}$",
           ["$a=\\frac{7}{2}$", "$a=0$ בלבד", "$a>\\frac{7}{2}$ בלבד"],
           "הגבול הוא $0$ ו-$f(0)=2a-7$. סליקה כאשר $2a-7\\neq0$, כלומר $a\\neq\\frac{7}{2}$. לדוגמה $a=0$ ו-$a=4$ שניהם מתאימים (נבדק ב-sympy)."),
    ],
    stepsSource="ai-draft")

add(3, "ג",
    rubric=rub(("חישוב הגבולות החד-צדדיים $\\frac{b}{3}$ ו-$0$", 2),
               ("תנאי אי-רציפות ממין ראשון: גבולות סופיים ושונים, כלומר $b\\neq0$", 2),
               ("$a$ אינו משפיע, לכן $a\\in\\mathbb{R}$", 1)),
    rubricSource="ai-draft",
    pitfalls=["להוסיף תנאי על $a$: הערך $f(0)$ אינו משפיע על קיום הגבולות החד-צדדיים.",
              "לבלבל בין ממין ראשון (גבולות חד-צדדיים סופיים ושונים) לבין סליקה (שווים)."],
    steps=[
        num("מהו $\\lim_{x\\to0^-}f(x)$ עבור $b=3$?", lt(3), "הגבול השמאלי הוא $\\frac{b}{3}=1$, והימני $0$, כלומר שונים."),
        ch("אילו ערכי פרמטרים נותנים אי-רציפות ממין ראשון?", "$b\\neq0$ ו-$a$ ממשי כלשהו",
           ["$b=0$ ו-$a\\neq\\frac{7}{2}$", "$b\\neq0$ ו-$a=\\frac{7}{2}$ בלבד", "לא קיימים ערכים כאלה"],
           "גבולות חד-צדדיים סופיים ושונים כאשר $\\frac{b}{3}\\neq0$, ללא תלות ב-$a$ (נבדק ב-sympy עבור $a=0,\\frac72,10$ עם $b=3$)."),
    ],
    stepsSource="ai-draft")

add(3, "ד",
    rubric=rub(("חישוב הגבולות החד-צדדיים: שניהם קיימים וסופיים לכל $a,b$", 3),
               ("מסקנה: אין ערכים שנותנים אי-רציפות ממין שני, והסבר", 2)),
    rubricSource="ai-draft",
    pitfalls=["לכתוב ערכים כלשהם של $b$ בלי לבדוק שהגבול השמאלי $\\frac{b}{3}$ סופי לכל $b$.",
              "לא לנמק: התשובה \"לא קיימים\" דורשת הסבר שהגבולות החד-צדדיים תמיד סופיים."],
    steps=[
        num("מהו $\\lim_{x\\to0^-}f(x)$ עבור $b=-9$?", lt(-9), "הגבול הוא $\\frac{b}{3}=-3$, ערך סופי."),
        ch("האם קיימים $a,b$ שעבורם $x=0$ אי-רציפות ממין שני?",
           "לא, כי שני הגבולות החד-צדדיים קיימים וסופיים לכל $a,b$",
           ["כן, כאשר $b\\neq0$", "כן, כאשר $a=\\frac{7}{2}$", "כן, כאשר $b=0$"],
           "הגבול השמאלי הוא $\\frac{b}{3}$ והימני $0$, שניהם סופיים תמיד, ולכן אין אי-רציפות ממין שני."),
    ],
    stepsSource="ai-draft")

# ===== Q4a: lim 1/ln x - 1/(x-1) =====
g4a = (x - 1 - sp.log(x))/(sp.log(x)*(x - 1))
assert sp.limit(g4a, x, 1) == R(1, 2) and sp.limit(1/sp.log(x) - 1/(x - 1), x, 1) == R(1, 2)
assert (sp.limit(x - 1 - sp.log(x), x, 1), sp.limit(sp.log(x)*(x - 1), x, 1)) == (0, 0)
den4 = sp.diff(x - 1 + x*sp.log(x), x)
assert same(den4, 2 + sp.log(x)) and den4.subs(x, 1) == 2
L4 = ["$\\lim_{x\\to1}\\left(\\frac{1}{\\ln x}-\\frac{1}{x-1}\\right)=\\lim_{x\\to1}\\frac{x-1-\\ln x}{\\ln x\\cdot(x-1)}$, מסוג $\\frac{0}{0}$.",
      "לפי לופיטל: $\\lim_{x\\to1}\\frac{1-\\frac{1}{x}}{\\frac{1}{x}(x-1)+\\ln x}=\\lim_{x\\to1}\\frac{x-1}{x-1+x\\ln x}$, שוב מסוג $\\frac{0}{0}$.",
      "לפי לופיטל שוב: $\\lim_{x\\to1}\\frac{1}{1+\\ln x+1}=\\frac{1}{2}$."]
assert sp.limit((x - 1)/(x - 1 + x*sp.log(x)), x, 1) == R(1, 2)

add(4, "א",
    rubric=rub(("העברה למכנה משותף: $\\frac{x-1-\\ln x}{\\ln x\\cdot(x-1)}$ וזיהוי $\\frac{0}{0}$", 3),
               ("הפעלה ראשונה של לופיטל וצמצום ל-$\\frac{x-1}{x-1+x\\ln x}$", 3),
               ("הפעלה שנייה של לופיטל", 2),
               ("ערך הגבול $\\frac{1}{2}$", 2)),
    rubricSource="ai-draft",
    pitfalls=["להפעיל לופיטל על הפרש $\\infty-\\infty$ בלי להעביר קודם למנה.",
              "לעצור אחרי לופיטל אחד: הביטוי $\\frac{x-1}{x-1+x\\ln x}$ עדיין מסוג $\\frac{0}{0}$.",
              "טעות בנגזרת של $\\ln x\\cdot(x-1)$: צריך כלל מכפלה."],
    steps=[
        ch("מה סוג הצורה הלא מסוימת של $\\frac{x-1-\\ln x}{\\ln x\\cdot(x-1)}$ כאשר $x\\to1$?", "$\\frac{0}{0}$",
           ["$\\frac{\\infty}{\\infty}$", "$1^\\infty$", "$0\\cdot\\infty$"],
           "המונה $x-1-\\ln x\\to0$ והמכנה $\\ln x\\cdot(x-1)\\to0$ (אומת ב-sympy)."),
        num("אחרי הפעלת לופיטל הראשונה מתקבל $\\frac{x-1}{x-1+x\\ln x}$. מהי הנגזרת של המכנה $x-1+x\\ln x$ בנקודה $x=1$?",
            den4.subs(x, 1), "הנגזרת היא $1+\\ln x+1=2+\\ln x$, ובנקודה $x=1$ היא $2$."),
        num("מהו ערך הגבול? (עשרוני)", R(1, 2), "$\\frac{1}{2}=0.5$ (sympy: ערך הגבול המקורי)."),
        order("סדרו את שלבי החישוב.", L4, "מכנה משותף, לופיטל ראשון, לופיטל שני. כל שלב מקבל את הביטוי שהתקבל בקודמו."),
    ],
    stepsSource="ai-draft")

# ===== Q4b: lim int_0^x tan / (x sin x) =====
assert sp.limit(sp.integrate(sp.tan(t), (t, 0, x))/(x*sp.sin(x)), x, 0) == R(1, 2)
assert sp.limit(sp.sin(x)/x + sp.cos(x), x, 0) == 2 and sp.limit(sp.tan(x)/x, x, 0) == 1
dnum = sp.diff(sp.integrate(sp.tan(t), (t, 0, x)), x)
assert same(dnum, sp.tan(x))

add(4, "ב",
    rubric=rub(("זיהוי צורה $\\frac{0}{0}$ והפעלת לופיטל", 3),
               ("גזירת המונה לפי המשפט היסודי: $\\tan x$, וגזירת המכנה $\\sin x+x\\cos x$", 3),
               ("חלוקה ב-$x$ וחישוב $\\frac{\\tan x/x}{\\sin x/x+\\cos x}\\to\\frac{1}{1+1}$", 3),
               ("ערך הגבול $\\frac{1}{2}$", 1)),
    rubricSource="ai-draft",
    pitfalls=["לגזור את האינטגרל כאילו הגבול התחתון תלוי ב-$x$, או לחשב אותו ישירות במקום להשתמש במשפט היסודי.",
              "לשכוח כלל מכפלה במכנה $x\\sin x$.",
              "לטעות בגבול $\\lim\\left(\\frac{\\sin x}{x}+\\cos x\\right)$: הוא $2$ ולא $1$."],
    steps=[
        ch("מהי הנגזרת (לפי $x$) של המונה $\\int_0^x\\tan t\\,dt$?", "$\\tan x$",
           ["$\\sec^2x$", "$x\\tan x$", "$\\ln|\\cos x|$"],
           "לפי המשפט היסודי של החשבון האינטגרלי, $\\frac{d}{dx}\\int_0^xg(t)\\,dt=g(x)$ (אומת ב-sympy)."),
        num("מהו $\\lim_{x\\to0}\\left(\\frac{\\sin x}{x}+\\cos x\\right)$?", 2, "$1+1=2$ (sympy)."),
        num("מהו ערך הגבול? (עשרוני)", R(1, 2), "$\\frac{\\tan x/x}{\\sin x/x+\\cos x}\\to\\frac{1}{2}$."),
    ],
    stepsSource="ai-draft")

# ===== Q5a: int (x^2+2x) cos 2x =====
Fa5 = ((x**2 + 2*x - R(1, 2))/2)*sp.sin(2*x) + (x + 1)*sp.cos(2*x)/2
assert same(sp.diff(Fa5, x), (x**2 + 2*x)*sp.cos(2*x))
defv5 = sp.integrate((x**2 + 2*x)*sp.cos(2*x), (x, 0, sp.pi/4))
assert abs(sp.N(Fa5.subs(x, sp.pi/4) - Fa5.subs(x, 0) - defv5)) < 1e-12
assert sp.degree(x**2 + 2*x, x) == 2 and sp.degree(sp.diff(x**2 + 2*x, x), x) == 1 and sp.degree(sp.integrate(x**2 + 2*x, x), x) == 3

add(5, "א",
    rubric=rub(("בחירה נכונה לאינטגרציה בחלקים: $u=x^2+2x$ ו-$v'=\\cos2x$", 2),
               ("חלק ראשון: $\\frac{(x^2+2x)\\sin2x}{2}-\\int(x+1)\\sin2x\\,dx$", 3),
               ("חלק שני באינטגרל הנותר, עם $u=x+1$", 3),
               ("איחוד התוצאה וקבוע האינטגרציה", 2)),
    rubricSource="ai-draft",
    pitfalls=["לבחור $u=\\cos2x$ ו-$v'=x^2+2x$: הדרגה של הפולינום עולה במקום לרדת והאינטגרל מסתבך.",
              "לשכוח את הגורם $\\frac{1}{2}$ באינטגרל של $\\cos2x$ ($v=\\frac{\\sin2x}{2}$).",
              "שגיאת סימן בשלב השני, כאשר $v=-\\frac{\\cos2x}{2}$."],
    steps=[
        ch("איזו בחירה באינטגרציה בחלקים מורידה את דרגת הפולינום בכל שלב?",
           "$u=x^2+2x,\\ v'=\\cos2x$",
           ["$u=\\cos2x,\\ v'=x^2+2x$"],
           "בבחירה הראשונה $u'=2x+2$ מדרגה 1; בשנייה $v=\\frac{x^3}{3}+x^2$ מדרגה 3, כלומר הדרגה עולה (הדרגות נבדקו ב-sympy)."),
        num("כמה פעמים צריך להפעיל אינטגרציה בחלקים כאן?", 2, "אחרי הפעם הראשונה נשאר $\\int(x+1)\\sin2x\\,dx$ עם פולינום מדרגה 1, ופעם שנייה מורידה אותו לקבוע."),
        num("כבדיקה: מהו הערך של $\\int_0^{\\pi/4}(x^2+2x)\\cos2x\\,dx$? (עשרוני)", defv5,
            "מציבים את הקדומה $\\frac{x^2+2x-0.5}{2}\\sin2x+\\frac{(x+1)\\cos2x}{2}$ בין $0$ ל-$\\frac{\\pi}{4}$ (sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q5b: area =====
inter5 = sorted(sp.solve(sp.Eq(x**2 + 2, 2*x + 5), x))
assert inter5 == [-1, 3]
S1 = sp.integrate(2*x + 5 - (x**2 + 2), (x, 0, 3))
S2 = sp.integrate(x**2 + 2 - (2*x + 5), (x, 3, 6))
assert (S1, S2, S1 + S2) == (9, 27, 36)

add(5, "ב",
    rubric=rub(("מציאת נקודות החיתוך של הפרבולה והישר: $x=-1$ ו-$x=3$, ובחירת $x=3$ הנמצא בקטע $[0,6]$", 4),
               ("פיצול השטח ל-$[0,3]$ ו-$[3,6]$ לפי מי העליון", 3),
               ("חישוב שני האינטגרלים וסכומם $36$", 3)),
    rubricSource="ai-draft",
    pitfalls=["לחשב $\\int_0^6(2x+5-x^2-2)dx$ בלי לפצל: שם הפרבולה מעל הישר ולכן מתקבל שטח מסומן ולא שטח.",
              "לכלול את נקודת החיתוך $x=-1$ שמחוץ ל-$[0,6]$."],
    steps=[
        num("באיזה ערך של $x$ בקטע $[0,6]$ נפגשים הפרבולה והישר?", 3, "$x^2-2x-3=0$ נותן $x=3$ או $x=-1$; רק $x=3$ בקטע (sympy)."),
        num("מהו השטח בין הישר לפרבולה בקטע $[0,3]$ (הישר למעלה)?", S1, "$\\left(3x+x^2-\\frac{x^3}{3}\\right)\\Big|_0^3=9$."),
        num("מהו השטח בקטע $[3,6]$ (הפרבולה למעלה)?", S2, "$\\left(-3x-x^2+\\frac{x^3}{3}\\right)\\Big|_3^6=27$."),
        num("מהו השטח הכולל?", S1 + S2, "$9+27=36$."),
    ],
    stepsSource="ai-draft")

# ===== Q6a: unique root of e^x - 1/x - 3 in (1,1.5) =====
g6 = sp.exp(x) - 1/x - 3
g6p = sp.diff(g6, x)
assert same(g6p, sp.exp(x) + 1/x**2)
assert g6.subs(x, 1) == sp.E - 4 and sp.N(g6.subs(x, R(3, 2))) > 0 and sp.N(g6.subs(x, 1)) < 0
L6 = ["נגדיר $g(x)=e^x-\\frac{1}{x}-3$ בקטע $(1,1.5)$.",
      "$g'(x)=e^x+\\frac{1}{x^2}>0$ לכל $x$ בקטע, ולכן $g$ עולה ממש.",
      "$g(1)=e-4<0$ וגם $g(1.5)=e^{1.5}-\\frac{2}{3}-3>0$.",
      "לפי משפט ערך הביניים יש שורש בקטע, והמונוטוניות הממשית מבטיחה שהוא יחיד."]
L6b = list(L6)
L6b[1] = "$g'(x)=e^x-\\frac{1}{x^2}>0$ לכל $x$ בקטע, ולכן $g$ עולה ממש."
assert not same(sp.exp(x) - 1/x**2, g6p)

add(6, "א",
    rubric=rub(("הגדרת $g(x)=e^x-\\frac{1}{x}-3$ ורציפותה בקטע", 2),
               ("נגזרת חיובית $g'(x)=e^x+\\frac{1}{x^2}>0$ ולכן מונוטוניות עולה", 3),
               ("סימנים הפוכים בקצוות: $g(1)<0<g(1.5)$", 3),
               ("מסקנה: קיום לפי ערך הביניים ויחידות לפי מונוטוניות", 2)),
    rubricSource="ai-draft",
    pitfalls=["להסתפק במשפט ערך הביניים: הוא נותן קיום בלבד, ויחידות דורשת מונוטוניות (או משפט רול).",
              "טעות סימן בנגזרת של $-\\frac{1}{x}$: היא $+\\frac{1}{x^2}$.",
              "לא לחשב את ערכי הקצוות, או להסתפק בהערכה בלי להראות את הסימן."],
    steps=[
        num("מהו $g(1)$ עבור $g(x)=e^x-\\frac{1}{x}-3$? (עשרוני)", g6.subs(x, 1), "$g(1)=e-1-3=e-4\\approx-1.2817<0$."),
        num("מהו $g(1.5)$? (עשרוני)", g6.subs(x, R(3, 2)), "$e^{1.5}-\\frac{2}{3}-3\\approx0.8149>0$."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L6b, 1,
                "הנגזרת של $-\\frac{1}{x}$ היא $+\\frac{1}{x^2}$, לא $-\\frac{1}{x^2}$ (נבדק ב-sympy), וכך נגזרת $g$ מובטחת להיות חיובית."),
    ],
    stepsSource="ai-draft")

# ===== Q6b: abs max/min of (x^2+5)/(x+2) on [0,10] =====
y6 = (x**2 + 5)/(x + 2)
c6 = [s for s in sp.solve(sp.numer(sp.together(sp.diff(y6, x))), x) if 0 <= s <= 10]
assert c6 == [1]
vals6 = {v: y6.subs(x, v) for v in (0, 1, 10)}
assert vals6 == {0: R(5, 2), 1: 2, 10: R(105, 12)}
assert min(vals6.values()) == 2 and max(vals6.values()) == R(105, 12)

add(6, "ב",
    rubric=rub(("נגזרת $y'=\\frac{x^2+4x-5}{(x+2)^2}$ ונקודות קריטיות $x=1$ ו-$x=-5$", 3),
               ("פסילת $x=-5$ (מחוץ לקטע $[0,10]$)", 1),
               ("חישוב $y$ בקצוות ובנקודה הקריטית: $2.5$, $2$, $\\frac{105}{12}$", 4),
               ("קביעה: מינימום $2$ ב-$x=1$ ומקסימום $\\frac{105}{12}$ ב-$x=10$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לכלול את $x=-5$ כנקודה חשודה אף שהיא מחוץ לקטע.",
              "לשכוח לבדוק את קצוות הקטע ולהסתפק בקיצון המקומי.",
              "לשכוח שהמכנה $x+2$ מתאפס ב-$x=-2$ (מחוץ לקטע, אך כדאי לוודא)."],
    steps=[
        num("מהו ערך $x$ בקטע $[0,10]$ שבו $y'=0$?", c6[0], "$x^2+4x-5=0$ נותן $x=1$ או $x=-5$; רק $x=1$ בקטע."),
        num("מהו $y(0)$? (עשרוני)", vals6[0], "$y(0)=\\frac{5}{2}=2.5$."),
        num("מהו $y(10)$? (עשרוני)", vals6[10], "$y(10)=\\frac{105}{12}=8.75$."),
        ch("מהם המינימום והמקסימום המוחלטים בקטע $[0,10]$?",
           "מינימום $2$ (ב-$x=1$) ומקסימום $\\frac{105}{12}$ (ב-$x=10$)",
           ["מינימום $\\frac{5}{2}$ (ב-$x=0$) ומקסימום $\\frac{105}{12}$", "מינימום $2$ ומקסימום $\\frac{5}{2}$", "מינימום $0$ ומקסימום $\\frac{105}{12}$"],
           "הערכים הם $y(0)=2.5$, $y(1)=2$, $y(10)=8.75$; הקטן ביותר $2$ והגדול ביותר $\\frac{105}{12}$ (sympy)."),
    ],
    stepsSource="ai-draft")


exam = {
    "examCode": "24B-A",
    "examLabel": "מבחן סוף סמסטר א' תשפ\"ד, מועד ב'",
    "year": 2024,
    "examDate": "03/04/2024",
    "sourceFile": "calculus-1/24B-A exam+solution.pdf",
    "solutionFile": "calculus-1/24B-A exam+solution.pdf",
    "contexts": {"c3": {"kind": "text", "title": "שאלה 3", "text": CTX3}},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

# -*- coding: utf-8 -*-
"""Generator for tools/raw/24A-A.json -- calculus-1 (20151), semester B 2024, moed A (19/03/2024).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24A-A.py

Source: sitting 24A-A, pp.1-7 (typed exam with the official worked solution after each "פתרון" label).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each). Weight of every question 20%.

Transcription notes
- Official solution transcribed in full, as printed. Rubric and steps are intentionally not written.
- Q1: the official solution claims y''<0 for x<0 (concave down there), but y''=e^x(x^2-4x+6)/x^4 has a
  quadratic with negative discriminant, so y''>0 for every x!=0 (tools/verify/24A-A/check.py). Final-answer error ->
  "הפתרון הרשמי עם תיקון" label, solutionSource solved, official False (standing label rule, 2026-10-18). The
  official graph is right (convex on both branches) and is kept.
- Figures: Q1 official graph (p.2), Q4b official sketch (p.5), Q6b official figure (p.7).

Checks (tools/verify/24A-A/check.py, sympy): every derivative, limit, integral, extremum table, volume, tangent and
area matches the official answers except the Q1 convexity claim above.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24A-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**הפתרון הרשמי עם תיקון:** בפתרון הרשמי נכתב בסעיף ג שעבור $x<0$ מתקיים $y''<0$ והפונקציה קמורה (כלפי מטה). זה שגוי: $y''=\frac{e^x\left(x^2-4x+6\right)}{x^4}$ והגורם $x^2-4x+6=(x-2)^2+2$ חיובי תמיד, ולכן $y''>0$ לכל $x\neq0$ והגרף קעור כלפי מעלה בשני הענפים (כפי שגם רואים בגרף הרשמי). סעיף ג להלן מתוקן; שאר הפתרון כפי שפורסם. התיקון נבדק (sympy).
**א. תחום הגדרה:** $D=\{x\neq 0\}$. אין נקודות חיתוך עם צירי הקואורדינטות.
**ב.** $f'(x)=\frac{e^x(x^2-2x)}{x^4}=\frac{e^x\cdot x(x-2)}{x^4}=\frac{e^x\cdot(x-2)}{x^3}$. מכאן רואים שהנגזרת מתאפסת רק ב-$x=2$ ובנוסף $y'>0$ כאשר $x<0\ \cup\ x>2$ וגם $y'<0$ כאשר $0<x<2$. הנקודה $x=2$ היא נקודת מינימום מקומי.
**ג.** $y''=\frac{e^x(x^2-4x+6)}{x^4}$. אין נקודות פיתול. בנוסף, $y''>0$ עבור $x>0$ וגם עבור $x<0$, ולכן בשני התחומים הפונקציה קעורה (כלפי מעלה, $\cup$): הדיסקרימיננטה של $x^2-4x+6$ היא $16-24<0$, כך שהגורם הזה חיובי תמיד, וגם $e^x>0$ ו-$x^4>0$.
**ד.** $\begin{cases}\lim_{x\to0^-}\frac{e^x}{x^2}=+\infty\\ \lim_{x\to0^+}\frac{e^x}{x^2}=+\infty\end{cases}$ ולכן קו ישר $x=0$ (ציר ה-$y$) מהווה אסימפטוטה אנכית לגרף הפונקציה.
$\begin{cases}\lim_{x\to+\infty}f(x)=\lim_{x\to+\infty}\frac{e^x}{x^2}=+\infty\\ \lim_{x\to-\infty}f(x)=\lim_{x\to-\infty}\frac{e^x}{x^2}=0\end{cases}$ ולכן קו ישר $y=0$ מהווה אסימפטוטה אופקית לגרף הפונקציה במינוס אינסוף.

![הגרף הרשמי של הפונקציה](images/exams/24A-A-Q1-graph.png)
"""

SOL2A = r"""
$$\frac{x^2}{(x+2)(x^2+1)}=\frac{A}{x+2}+\frac{Bx+C}{x^2+1}$$
$$x^2=A(x^2+1)+(Bx+C)(x+2)$$
הצבת $x=-2$ נותנת $4=5A$; מקדמי $x^2$ נותנים $A+B=1$; מקדמי $x$ נותנים $2B+C=0$.
$$A=\frac{4}{5},\quad B=\frac{1}{5},\quad C=-\frac{2}{5}$$
$$\int\frac{x^2\,dx}{(x+2)(x^2+1)}=\frac{1}{5}\int\left(\frac{4}{x+2}+\frac{x-2}{x^2+1}\right)dx=\frac{1}{5}\left(4\ln|x+2|+\frac{1}{2}\ln(x^2+1)-2\arctan x\right)+C$$
"""

SOL2B = r"""
נוכיח באמצעות שיטת האינדוקציה ש-$a_n\le 2$ לכל $n$ טבעי, כלומר נוכיח שסדרה חסומה מלמעלה:
בסיס האינדוקציה: $n=1,\ a_1=1\le 2$.
שלב האינדוקציה: נניח ש-$a_n\le 2$ ומכאן נוכיח שגם $a_{n+1}\le 2$.
$$a_n\le 2\iff -a_n\ge -2\iff 5-a_n\ge 3\iff\{5-a_n>0\}\Rightarrow\frac{1}{5-a_n}\le\frac{1}{3}$$
$$\frac{6}{5-a_n}\le\frac{6}{3}\Rightarrow\frac{6}{5-a_n}\le 2\Rightarrow a_{n+1}\le 2$$
קיבלנו: $\forall n\in\mathbb{N}\ \ a_n\le 2$.
נוכיח שסדרה עולה מונוטונית: צריך לבדוק שאי-השוויון $a_{n+1}\ge a_n$ אמת לכל $n$ טבעי. לפי הגדרה רקורסיבית $a_{n+1}=\frac{6}{5-a_n}$, לכן יש לבדוק אי-השוויון:
$$\frac{6}{5-a_n}\ge a_n$$
אי-השוויון זה שקול לאי-השוויון הבא:
$$a_n^2-5a_n+6\ge 0\quad(*)$$
פתרון של אי-השוויון $x^2-5x+6\ge 0,\ x\in\mathbb{R}$ (פרבולה מחייכת, וחותכת ציר ה-$X$ בנקודות $x_1=2,\ x_2=3$): $x\in(-\infty,2]\cup[3,\infty)$.
קודם הוכחנו ש-$a_n\le 2$ לכן אי-השוויון $(*)$ אמת.
הוכחנו שסדרה חסומה מלמעלה ועולה מונוטונית לכן לפי משפט ויירשטראס קיים גבול $\lim_{n\to\infty}a_n=L$. לפי תכונות גבולות:
$$\lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}\frac{6}{5-a_n},\qquad L=\frac{6}{5-L}$$
$$L^2-5L+6=0,\quad L_1=2,\quad L_2=3$$
ברור ש-$L_2=3$ לא מתאים, לכן:
$$\lim_{n\to\infty}a_n=2$$
"""

SOL3A = r"""
$$\lim_{x\to0}(1-\tan x)^{\frac{1}{\sin 2x}}=\lim_{x\to0}(1-\tan x)^{-\frac{1}{\tan x}\cdot\frac{(-\tan x)}{\sin 2x}}=e^{\lim_{x\to0}\frac{-\sin x}{2\sin x\cos x\cos x}}=e^{-\frac{1}{2}}=\frac{1}{\sqrt{e}}$$
"""

SOL3B = r"""
$$\int\frac{\sin 2x}{3+\cos^2 2x}dx=\{t=\cos 2x,\ dt=-2\sin 2x\,dx\}=-\frac{1}{2}\int\frac{dt}{3+t^2}=$$
$$=-\frac{1}{2\sqrt{3}}\arctan\frac{t}{\sqrt{3}}+c=-\frac{1}{2\sqrt{3}}\arctan\frac{\cos 2x}{\sqrt{3}}+c$$
"""

SOL4A = r"""
$$y=x^{2/3}e^{-x}\ \Rightarrow\ y'=\frac{2}{3}\cdot\frac{e^{-x}}{\sqrt[3]{x}}-x^{2/3}e^{-x}=e^{-x}\cdot\frac{2-3x}{3\sqrt[3]{x}},\qquad y'=0\ \Rightarrow\ x=\frac{2}{3}$$
הנגזרת לא מוגדרת בנקודה $x=0$. לכן הנקודות החשודות הפנימיות הן $x=0$, $x=\frac{2}{3}$.

| $x$ | $-3$ | $0$ | $2/3$ | $1$ |
|---|---|---|---|---|
| $y$ | $41.8$ | $0$ | $0.39$ | $0.37$ |

$$y_{min}=y(0)=0$$
$$y_{max}=y(-3)=41.8$$
"""

SOL4B = r"""
![שרטוט רשמי של התחום](images/exams/24A-A-Q4b-sketch.png)
$$V=\pi\int_0^1 y^2\,dx=\pi\int_0^1\arctan x\,dx=\left|\begin{matrix}u=\arctan x & du=\frac{dx}{1+x^2}\\ dv=dx & v=x\end{matrix}\right|=$$
$$=\pi x\arctan x\Big|_0^1-\pi\int_0^1\frac{x\,dx}{1+x^2}=\frac{\pi^2}{4}-\frac{\pi}{2}\int_0^1\frac{2x\,dx}{1+x^2}=\frac{\pi^2}{4}-\frac{\pi}{2}\int_0^1\frac{d(1+x^2)}{1+x^2}=$$
$$=\frac{\pi^2}{4}-\frac{\pi}{2}\ln(1+x^2)\Big|_0^1=\frac{\pi^2}{4}-\frac{\pi}{2}\ln 2$$
"""

SOL5A = r"""
$$\lim_{x\to0^+}\frac{\int_0^{\sqrt{x}}\sin(t^2)\,dt}{x^{\frac{3}{2}}}=\left\{\frac{0}{0}\right\}=\lim_{x\to0^+}\frac{\sin x\cdot\frac{1}{2\sqrt{x}}}{\frac{3}{2}x^{\frac{1}{2}}}=\lim_{x\to0^+}\frac{\sin x}{3x}=\frac{1}{3}$$
"""

SOL5B = r"""
$$\lim_{x\to0^-}x^{-2}(e^{ax}-1)^2=\lim_{x\to0^-}\frac{(e^{ax}-1)^2}{x^2}=\lim_{x\to0^-}\left(\frac{e^{ax}-1}{x}\right)^2=\left(\lim_{x\to0^-}\frac{e^{ax}-1}{x}\right)^2=\left(\lim_{x\to0^-}\frac{ae^{ax}}{1}\right)^2=a^2$$
$$\lim_{x\to0^+}\left(4+e^{-\frac{a^2}{x}}\right)=\begin{cases}5, & a=0\\ 4, & a\neq0\end{cases}$$
$$a^2=b=4$$
תשובה: $b=4,\quad a=\pm2$
"""

SOL6A = r"""
הפונקציה $f(x)=\tan x$ מקיימת את כל התנאים של משפט לגרנז' בתחום $0<x<\frac{\pi}{2}$.
לכן קיימת נקודה $c$ בקטע $(0,x)$, שבה מתקיים:
$$f'(c)=\frac{\tan x-\tan 0}{x-0}\ \Rightarrow\ \frac{1}{\cos^2 c}=\frac{\tan x}{x}.$$
לכן $\cos^2 c<1$ ואז $\frac{1}{\cos^2 c}>1$. מכאן נובע $\frac{\tan x}{x}>1$, כלומר $\tan x>x$.
"""

SOL6B = r"""
נמצא את משוואת הישר המשיק העובר דרך הנקודה $x=3$: $y(3)=1,\ y'=\frac{1}{\sqrt{2x-5}},\ y'(3)=1$, נקבל ישר המשיק: $y-1=1(x-3)\Rightarrow y=x-2$.
חישוב השטח:
$$s=s_1+s_2=\int_2^{5/2}(x-2)\,dx+\int_{5/2}^{3}\left(x-2-\sqrt{2x-5}\right)dx=$$
$$=\frac{(x-2)^2}{2}\Big|_2^3-\frac{(2x-5)^{3/2}}{3}\Big|_{5/2}^3=\frac{1}{6}$$

![הציור הרשמי](images/exams/24A-A-Q6b-fig.png)
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=\frac{e^x}{x^2}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, תחומי עליה וירידה, "
      "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20, solutionSource="solved", official=False),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{x^2\,dx}{(x+2)(x^2+1)}$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "sequences_limits",
      "נתונה הסדרה: " r"$a_1=1,\ a_{n+1}=\frac{6}{5-a_n}$." "\nהוכיחו כי הסדרה מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0}(1-\tan x)^{\frac{1}{\sin 2x}}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\sin 2x\,dx}{3+\cos^2 2x}$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "extrema_optimization",
      r"מצאו את ערך מקסימלי ואת הערך מינימלי של הפונקציה $y=x^{2/3}e^{-x}$ בקטע סגור $[-3,1]$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר מסיבוב של התחום המישורי הכלוא בין הקווים: $y=\sqrt{\arctan(x)},\ y=0,\ x=0,\ x=1$ סביב ציר ה-$X$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "lhopital_taylor",
      r"חשבו את הגבול הבא: $\lim_{x\to0^+}\frac{\int_0^{\sqrt{x}}\sin(t^2)\,dt}{x^{\frac{3}{2}}}$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "continuity",
      r"נתונה הפונקציה: $f(x)=\begin{cases}x^{-2}\left(e^{ax}-1\right)^2 & x<0\\ b & x=0\\ 4+e^{-a^2/x} & x>0\end{cases}$"
      "\n" r"מצאו לאלו ערכים של פרמטרים $a$ ו-$b$, פונקציה $f(x)$ תהיה רציפה בנקודה $x=0$?",
      SOL5B, part="ב", points=10),

    Q(6, "proof", "mean_value_theorems",
      r"הוכיחו שמתקיים $\tan x>x$ עבור $0<x<\frac{\pi}{2}$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "definite_integrals",
      r"מצאו את השטח הכלוא בין ציר ה-$X$, גרף של הפונקציה $y=\sqrt{2x-5}$ והמשיק שלו בנקודה $x=3$.",
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
    """TeX of a sympy expression, wrapped in $...$; the internal positive symbol 'xp' is printed as x."""
    if hasattr(e, "free_symbols"):
        e = e.subs({s: x for s in e.free_symbols if s.name == "xp"})
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

# ===== Q1: y = e^x / x^2 (released from hold: the solution now carries the corrected convexity) =====
_rot_before_q1 = _rot[0]  # Q1's choice steps must not shift the rotation of the items that already had steps
f1 = sp.exp(x)/x**2
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, sp.exp(x)*(x - 2)/x**3) and same(f1pp, sp.exp(x)*(x**2 - 4*x + 6)/x**4)
assert sp.solve(sp.numer(sp.together(f1p)), x) == [2] and f1.subs(x, 2) == sp.exp(2)/4
assert f1p.subs(x, -1) > 0 and f1p.subs(x, 1) < 0 and f1p.subs(x, 3) > 0
assert sp.discriminant(x**2 - 4*x + 6, x) == -8 and sp.expand((x - 2)**2 + 2) == x**2 - 4*x + 6
assert all(f1pp.subs(x, v) > 0 for v in (-5, -1, R(1, 2), 1, 2, 10)) and sp.solve(f1pp, x) == []
assert sp.limit(f1, x, 0, '+') == sp.oo and sp.limit(f1, x, 0, '-') == sp.oo
assert sp.limit(f1, x, -sp.oo) == 0 and sp.limit(f1, x, sp.oo) == sp.oo and sp.limit(f1/x, x, sp.oo) == sp.oo

add(1,
    rubric=rub(("תחום הגדרה $x\\neq0$, ללא חיתוכים עם הצירים ($e^x>0$)", 2),
               ("אסימפטוטה אנכית $x=0$ ($+\\infty$ משני הצדדים)", 3),
               ("התנהגות באינסוף: אסימפטוטה אופקית $y=0$ ב-$-\\infty$, וללא אסימפטוטה ב-$+\\infty$", 3),
               ("נגזרת $f'(x)=\\frac{e^x(x-2)}{x^3}$, תחומי עליה וירידה", 5),
               ("מינימום מקומי $\\left(2,\\frac{e^2}{4}\\right)$", 2),
               ("$f''(x)=\\frac{e^x\\left(x^2-4x+6\\right)}{x^4}>0$: קעורה כלפי מעלה בשני הענפים וללא נקודות פיתול", 4),
               ("שרטוט הגרף בהתאם לכל הנתונים", 1)),
    rubricSource="ai-draft",
    pitfalls=["לטעון שהגרף קעור כלפי מטה עבור $x<0$: $x^2-4x+6=(x-2)^2+2>0$ ולכן $f''>0$ בכל תחום ההגדרה.",
              "לכלול את $x=0$ בתחומי העליה והירידה.",
              "לטעון לאסימפטוטה אופקית ב-$+\\infty$: שם $f(x)=\\frac{e^x}{x^2}\\to+\\infty$."],
    steps=[
        chx("מהי הנגזרת של $y=\\frac{e^x}{x^2}$?", sp.exp(x)*(x - 2)/x**3,
            [sp.exp(x)*(x + 2)/x**3, sp.exp(x)*(x - 2)/x**2, sp.exp(x)/x**3], lambda e: same(e, f1p),
            "כלל המנה: $\\frac{e^xx^2-2xe^x}{x^4}=\\frac{e^x(x-2)}{x^3}$ (אומת ב-sympy)."),
        num("מהו ערך הפונקציה בנקודת המינימום המקומי $x=2$? (עשרוני)", f1.subs(x, 2), "$f(2)=\\frac{e^2}{4}\\approx1.8473$ (sympy).", tol=0.001),
        ch("מה סימן $f''(x)=\\frac{e^x\\left(x^2-4x+6\\right)}{x^4}$?", "חיובי בכל תחום ההגדרה, ולכן אין נקודות פיתול",
           ["שלילי עבור $x<0$ וחיובי עבור $x>0$", "שלילי בכל תחום ההגדרה", "מתאפס ב-$x=2$ ולכן שם נקודת פיתול"],
           "$x^2-4x+6=(x-2)^2+2>0$ (דיסקרימיננטה שלילית), ו-$e^x>0$, $x^4>0$ (אומת ב-sympy)."),
        ch("מהן האסימפטוטות של $y$?", "אנכית $x=0$ ואופקית $y=0$ ב-$-\\infty$ בלבד",
           ["אנכית $x=0$ ואופקית $y=0$ בשני הכיוונים", "אנכית $x=0$ בלבד", "אנכית $x=0$ ומשופעת ב-$+\\infty$"],
           "ב-$+\\infty$: $\\frac{e^x}{x^2}\\to\\infty$ ו-$\\frac{f(x)}{x}\\to\\infty$, ולכן אין אסימפטוטה; ב-$-\\infty$: $f\\to0$ (sympy)."),
    ],
    stepsSource="ai-draft")
_rot[0] = _rot_before_q1

# ===== Q2a: x^2/((x+2)(x^2+1)) =====
g2 = x**2/((x + 2)*(x**2 + 1))
A_, B_, C_ = sp.symbols('A B C')
sol2 = sp.solve(sp.Poly(sp.expand(A_*(x**2 + 1) + (B_*x + C_)*(x + 2) - x**2), x).all_coeffs(), [A_, B_, C_], dict=True)[0]
assert sol2 == {A_: R(4, 5), B_: R(1, 5), C_: R(-2, 5)}
assert same(g2, sol2[A_]/(x + 2) + (sol2[B_]*x + sol2[C_])/(x**2 + 1))
for bf in (A_*(x**2 + 1) + B_*(x + 2) - x**2, A_*(x**2 + 1) + B_*x*(x + 2) - x**2):
    assert sp.solve(sp.Poly(sp.expand(bf), x).all_coeffs(), [A_, B_], dict=True) == []

add(2, "א",
    rubric=rub(("פירוק לשברים חלקיים בצורה $\\frac{A}{x+2}+\\frac{Bx+C}{x^2+1}$", 3),
               ("חישוב המקדמים $A=\\frac45$, $B=\\frac15$, $C=-\\frac25$", 3),
               ("אינטגרציה של השברים: לוגריתמים ו-$\\arctan x$", 3),
               ("תשובה סופית עם $+C$", 1)),
    rubricSource="ai-verified",
    pitfalls=["לכתוב מונה קבוע מעל $x^2+1$ במקום $Bx+C$, ואז אין פתרון למערכת.",
              "לפצל את $\\frac{x-2}{x^2+1}$ לא נכון: $\\int\\frac{x}{x^2+1}=\\frac12\\ln(x^2+1)$ ו-$\\int\\frac{2}{x^2+1}=2\\arctan x$.",
              "לטעות בהשוואת מקדמים: הכפלת $Bx$ ב-$x$ נותנת $Bx^2$, ולכן מהמקדם של $x^2$ מתקבל $A+B=1$ (לא $A=1$)."],
    steps=[
        ch("איזה פירוק לשברים חלקיים מתאים ל-$\\frac{x^2}{(x+2)(x^2+1)}$?",
           "$\\frac{A}{x+2}+\\frac{Bx+C}{x^2+1}$",
           ["$\\frac{A}{x+2}+\\frac{B}{x^2+1}$", "$\\frac{A}{x+2}+\\frac{Bx}{x^2+1}$"],
           "$x^2+1$ אי-פריק ולכן מונה לינארי מלא. בשתי האפשרויות האחרות מערכת המקדמים חסרת פתרון (אומת ב-sympy)."),
        num("מהו $A$? (עשרוני)", sol2[A_], "הצבת $x=-2$: $4=5A$ ולכן $A=\\frac45=0.8$.", tol=0.0005),
        num("מהו $B$? (עשרוני)", sol2[B_], "מקדמי $x^2$: $A+B=1$ ולכן $B=\\frac15=0.2$.", tol=0.0005),
        num("מהו $C$? (עשרוני)", sol2[C_], "מקדמי $x$: $2B+C=0$ ולכן $C=-\\frac25=-0.4$.", tol=0.0005),
    ],
    stepsSource="ai-verified")

# ===== Q2b: a_{n+1} = 6/(5-a_n), a_1 = 1 =====
seq = [sp.Integer(1)]
for _ in range(40):
    seq.append(6/(5 - seq[-1]))
assert all(seq[i] < seq[i + 1] <= 2 for i in range(30))
assert seq[1] == R(3, 2) and seq[2] == R(12, 7)
Ls = sp.Symbol('L', real=True)
assert sorted(sp.solve(sp.Eq(Ls, 6/(5 - Ls)), Ls)) == [2, 3]
assert 6/(5 - 3) == 3
L2 = ["נוכיח באינדוקציה ש-$a_n\\le2$: $a_1=1\\le2$, ואם $a_n\\le2$ אז $5-a_n\\ge3$ ולכן $a_{n+1}=\\frac{6}{5-a_n}\\le2$.",
      "הסדרה עולה: $a_{n+1}\\ge a_n$ שקול ל-$a_n^2-5a_n+6\\ge0$, וזה נכון כי $a_n\\le2$.",
      "סדרה עולה וחסומה מלעיל מתכנסת, ונסמן $L=\\lim_{n\\to\\infty}a_n$.",
      "$L=\\frac{6}{5-L}$ ולכן $L^2-5L+6=0$, כלומר $L=2$ או $L=3$; כיוון ש-$a_n\\le2$, מתקבל $L=2$."]
L2b = list(L2)
L2b[3] = "$L=\\frac{6}{5-L}$ ולכן $L^2-5L-6=0$, כלומר $L=2$ או $L=3$; כיוון ש-$a_n\\le2$, מתקבל $L=2$."
assert not same(Ls**2 - 5*Ls - 6, Ls**2 - 5*Ls + 6) and same(Ls*(5 - Ls) - 6, -(Ls**2 - 5*Ls + 6))

add(2, "ב",
    rubric=rub(("הוכחת חסם מלעיל $a_n\\le2$ באינדוקציה", 3),
               ("הוכחת עליה: $\\frac{6}{5-a_n}\\ge a_n\\iff a_n^2-5a_n+6\\ge0$, נכון כי $a_n\\le2$", 3),
               ("מסקנה: מתכנסת (סדרה עולה וחסומה)", 1),
               ("משוואת הגבול $L=\\frac{6}{5-L}$, שורשים $2,3$", 2),
               ("פסילת $L=3$ והגבול $2$", 1)),
    rubricSource="ai-verified",
    pitfalls=["להכפיל באי-שוויון ב-$5-a_n$ בלי לוודא שהוא חיובי. כאן $5-a_n\\ge3>0$ הודות לחסם.",
              "לא לפסול את $L=3$: שני השורשים מקיימים את משוואת הגבול, והחסם $a_n\\le2$ הוא שפוסל את $3$.",
              "להוכיח עליה לפני החסם, ואז אי-השוויון $a_n^2-5a_n+6\\ge0$ לא מובטח."],
    steps=[
        num("מהו $a_2$ בסדרה $a_{n+1}=\\frac{6}{5-a_n}$, $a_1=1$? (עשרוני)", seq[1], "$a_2=\\frac{6}{4}=1.5$.", tol=0.0005),
        num("מהו $a_3$? (עשרוני)", seq[2], "$a_3=\\frac{6}{5-1.5}=\\frac{12}{7}\\approx1.7143$.", tol=0.001),
        ch("מדוע נפסל הפתרון $L=3$ של $L^2-5L+6=0$?",
           "כל איברי הסדרה קטנים או שווים ל-$2$, ולכן $L\\le2$",
           ["$3$ אינו פתרון של $L^2-5L+6=0$", "הסדרה יורדת ולכן $L<a_1=1$", "$\\frac{6}{5-3}$ אינו מוגדר"],
           "השורשים הם $2$ ו-$3$ (sympy), $\\frac{6}{5-3}=3$ מוגדר, והסדרה עולה. הנימוק הוא החסם $a_n\\le2$."),
        order("סדרו את שלבי ההוכחה.", L2,
              "החסם קודם, כי ההוכחה של העליה משתמשת בו; אחר כך התכנסות; ובסוף משוואת הגבול ובחירת השורש."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L2b, 3,
                "מ-$L=\\frac{6}{5-L}$ מקבלים $L(5-L)=6$, כלומר $L^2-5L+6=0$ ולא $L^2-5L-6=0$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: lim (1 - tan x)^(1/sin 2x) = e^(-1/2) =====
assert sp.limit(1 - sp.tan(x), x, 0) == 1
assert sp.limit(-sp.tan(x)/sp.sin(2*x), x, 0) == R(-1, 2)
assert sp.limit((1 - sp.tan(x))**(1/sp.sin(2*x)), x, 0) == sp.exp(R(-1, 2))

add(3, "א",
    rubric=rub(("זיהוי צורה $1^\\infty$", 2),
               ("כתיבה כ-$\\left((1-\\tan x)^{-1/\\tan x}\\right)^{-\\tan x/\\sin2x}$ או דרך $e^{\\lim\\frac{\\ln(1-\\tan x)}{\\sin2x}}$", 3),
               ("חישוב גבול המעריך $\\frac{-\\tan x}{\\sin2x}\\to-\\frac12$", 3),
               ("תשובה $e^{-1/2}=\\frac{1}{\\sqrt e}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להציב ישר ולקבל $1^\\infty=1$: זו צורה לא מסוימת.",
              "לטעות בגבול המעריך: $\\sin2x=2\\sin x\\cos x$ ולכן $\\frac{-\\tan x}{\\sin2x}\\to-\\frac12$ ולא $-1$.",
              "לשכוח את הסימן המינוס בשבר $\\frac{-\\tan x}{\\sin2x}$."],
    steps=[
        ch("מה סוג הצורה הלא מסוימת של $(1-\\tan x)^{1/\\sin2x}$ כאשר $x\\to0$?", "$1^\\infty$",
           ["$0\\cdot\\infty$", "$\\infty^0$", "$0^0$"],
           "הבסיס $1-\\tan x\\to1$ והמעריך $\\frac{1}{\\sin2x}\\to\\pm\\infty$ (sympy)."),
        num("מהו $\\lim_{x\\to0}\\frac{-\\tan x}{\\sin2x}$? (עשרוני)", R(-1, 2), "$\\frac{-\\tan x}{2\\sin x\\cos x}=\\frac{-1}{2\\cos^2x}\\to-\\frac12$.", tol=0.0005),
        num("מהו ערך הגבול? (עשרוני)", sp.exp(R(-1, 2)), "$e^{-1/2}\\approx0.6065$.", tol=0.001),
    ],
    stepsSource="ai-verified")

# ===== Q3b: int sin2x / (3 + cos^2 2x) =====
I3 = sp.sin(2*x)/(3 + sp.cos(2*x)**2)
F3 = -sp.atan(sp.cos(2*x)/sp.sqrt(3))/(2*sp.sqrt(3))
assert same(sp.diff(F3, x), I3)
sub3 = -1/(2*(3 + t**2))  # t = cos 2x, sin2x dx = -dt/2
assert same(sub3.subs(t, sp.cos(2*x))*sp.diff(sp.cos(2*x), x), I3)
v3 = sp.integrate(I3, (x, 0, sp.pi/4))
assert abs(sp.N(v3 - (F3.subs(x, sp.pi/4) - F3.subs(x, 0)))) < 1e-12

add(3, "ב",
    rubric=rub(("הצבה $t=\\cos2x$, $dt=-2\\sin2x\\,dx$", 3),
               ("מעבר ל-$-\\frac12\\int\\frac{dt}{3+t^2}$", 3),
               ("אינטגרל מסוג $\\arctan$: $-\\frac{1}{2\\sqrt3}\\arctan\\frac{t}{\\sqrt3}$", 3),
               ("חזרה ל-$x$ וקבוע אינטגרציה", 1)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את הגורם $-\\frac12$ מ-$dt=-2\\sin2x\\,dx$.",
              "לכתוב $\\arctan t$ במקום $\\frac{1}{\\sqrt3}\\arctan\\frac{t}{\\sqrt3}$: הקבוע במכנה הוא $3$ ולא $1$.",
              "לשכוח שהצבה שוברת את הגורם הפנימי: $\\cos^2 2x=t^2$ ולא $\\cos^2x$."],
    steps=[
        chx("אחרי ההצבה $t=\\cos2x$, מהו האינטגרנד ב-$t$ (כלומר $\\int\\ldots\\,dt$)?", sub3,
            [1/(2*(3 + t**2)), -1/(3 + t**2), -t/(2*(3 + t**2))],
            lambda e: same(e.subs(t, sp.cos(2*x))*sp.diff(sp.cos(2*x), x), I3),
            "$dt=-2\\sin2x\\,dx$ ולכן $\\sin2x\\,dx=-\\frac{dt}{2}$ ומתקבל $-\\frac{1}{2(3+t^2)}$ (נבדק ב-sympy)."),
        num("מהו המקדם של $\\arctan\\frac{t}{\\sqrt3}$ בקדומה? (עשרוני)", -1/(2*sp.sqrt(3)),
            "$-\\frac12\\cdot\\frac{1}{\\sqrt3}=-\\frac{1}{2\\sqrt3}\\approx-0.2887$.", tol=0.001),
        num("כבדיקה: מהו $\\int_0^{\\pi/4}\\frac{\\sin2x}{3+\\cos^22x}dx$? (עשרוני)", v3,
            "הערך הוא $\\frac{\\pi}{12\\sqrt3}\\approx0.1512$ (חישוב ב-sympy).", tol=0.001),
    ],
    stepsSource="ai-verified")

# ===== Q4a: y = x^(2/3) e^(-x) on [-3,1] =====
y4 = sp.Abs(x)**R(2, 3)*sp.exp(-x)
xpos = sp.Symbol('xp', positive=True)
dy = sp.diff(xpos**R(2, 3)*sp.exp(-xpos), xpos)
assert sp.solve(dy, xpos) == [R(2, 3)] and sp.limit(dy, xpos, 0, '+') == sp.oo
vv = {-3: y4.subs(x, -3), 0: y4.subs(x, 0), R(2, 3): y4.subs(x, R(2, 3)), 1: y4.subs(x, 1)}
assert max(vv, key=lambda k: sp.N(vv[k])) == -3 and min(vv, key=lambda k: sp.N(vv[k])) == 0
assert abs(sp.N(vv[-3]) - 41.8) < 0.05

add(4, "א",
    rubric=rub(("נגזרת $y'=e^{-x}\\cdot\\frac{2-3x}{3\\sqrt[3]{x}}$ ונקודה קריטית $x=\\frac23$", 3),
               ("זיהוי $x=0$ כנקודה חשודה (הנגזרת לא מוגדרת)", 2),
               ("חישוב הערך בנקודות $-3,0,\\frac23,1$", 3),
               ("מקסימום $y(-3)\\approx41.8$ ומינימום $y(0)=0$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את $x=0$, שבו הנגזרת לא מוגדרת אך הפונקציה כן, והוא נקודת המינימום.",
              "לחשב $(-3)^{2/3}$ לא נכון: $\\sqrt[3]{(-3)^2}=\\sqrt[3]{9}$, חיובי.",
              "לא לבדוק את קצוות הקטע $-3$ ו-$1$."],
    steps=[
        ch("אילו נקודות פנימיות בקטע $(-3,1)$ חשודות בקיצון?",
           "$x=0$ (הנגזרת לא מוגדרת) ו-$x=\\frac23$ (הנגזרת מתאפסת)",
           ["$x=\\frac23$ בלבד", "$x=0$ בלבד", "$x=-3$ ו-$x=1$ בלבד"],
           "$y'=0$ רק ב-$x=\\frac23$ ו-$y'\\to\\infty$ כש-$x\\to0$, כלומר לא מוגדרת ב-$0$ (sympy). הקצוות אינם נקודות פנימיות."),
        num("מהו $y(-3)=\\sqrt[3]{9}\\,e^3$? (עשרוני)", vv[-3], "$\\sqrt[3]{9}\\approx2.0801$ ו-$e^3\\approx20.0855$, ומכפלתם $\\approx41.78$.", tol=0.1),
        num("מהו $y\\left(\\frac23\\right)$? (עשרוני)", vv[R(2, 3)], "$\\left(\\frac23\\right)^{2/3}e^{-2/3}\\approx0.3918$.", tol=0.001),
        ch("מהם המקסימום והמינימום המוחלטים בקטע $[-3,1]$?",
           "מקסימום $y(-3)\\approx41.8$, מינימום $y(0)=0$",
           ["מקסימום $y\\left(\\frac23\\right)\\approx0.39$, מינימום $y(0)=0$", "מקסימום $y(-3)\\approx41.8$, מינימום $y(1)\\approx0.37$", "מקסימום $y(1)\\approx0.37$, מינימום $y(0)=0$"],
           "הערכים: $41.78$, $0$, $0.3918$, $0.3679$ (sympy). הגדול ביותר ב-$-3$ והקטן ביותר ב-$0$."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: volume of revolution of y = sqrt(arctan x), 0..1 about the x-axis =====
V4 = sp.pi*sp.integrate(sp.atan(x), (x, 0, 1))
assert same(V4, sp.pi**2/4 - sp.pi*sp.log(2)/2)
true4 = sp.N(sp.pi*sp.Integral(sp.atan(x), (x, 0, 1)))
bad4 = [sp.N(sp.pi*sp.Integral(sp.sqrt(sp.atan(x)), (x, 0, 1))), sp.N(2*sp.pi*sp.Integral(x*sp.sqrt(sp.atan(x)), (x, 0, 1))),
        sp.N(sp.pi*sp.Integral(sp.atan(x)**2, (x, 0, 1)))]
assert all(abs(bb - true4) > 0.01 for bb in bad4)
I4 = sp.integrate(sp.atan(x), (x, 0, 1))

add(4, "ב",
    rubric=rub(("נוסחת הדיסקות $V=\\pi\\int_0^1y^2\\,dx=\\pi\\int_0^1\\arctan x\\,dx$", 3),
               ("אינטגרציה בחלקים עם $u=\\arctan x$, $v'=1$", 3),
               ("חישוב $\\int\\frac{x}{1+x^2}dx=\\frac12\\ln(1+x^2)$", 2),
               ("הצבת הגבולות ותשובה $\\frac{\\pi^2}{4}-\\frac{\\pi}{2}\\ln2$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח לרבע: $y^2=\\arctan x$, והשורש נעלם.",
              "להשתמש בקליפות $2\\pi\\int xy\\,dx$ כשהסיבוב סביב ציר ה-$x$.",
              "לא לזכור שאפשר לבצע בחלקים עם $v'=1$ על $\\arctan x$."],
    steps=[
        ch("איזה אינטגרל נותן את הנפח בסיבוב סביב ציר ה-$x$?", "$\\pi\\int_0^1\\arctan x\\,dx$",
           ["$\\pi\\int_0^1\\sqrt{\\arctan x}\\,dx$", "$2\\pi\\int_0^1x\\sqrt{\\arctan x}\\,dx$", "$\\pi\\int_0^1\\arctan^2x\\,dx$"],
           "סיבוב סביב ציר ה-$x$: דיסקות, $V=\\pi\\int y^2dx$ עם $y^2=\\arctan x$. הערכים המספריים של האפשרויות האחרות שונים (נבדק ב-sympy)."),
        num("מהו $\\int_0^1\\arctan x\\,dx$? (עשרוני)", I4, "$\\frac{\\pi}{4}-\\frac{\\ln2}{2}\\approx0.4388$.", tol=0.001),
        num("מהו הנפח $V=\\frac{\\pi^2}{4}-\\frac{\\pi}{2}\\ln2$? (עשרוני)", V4, "$\\pi\\cdot0.4388\\approx1.3785$.", tol=0.001),
    ],
    stepsSource="ai-verified")

# ===== Q5a: lim int_0^sqrt(x) sin(t^2) dt / x^(3/2) =====
tt = sp.Symbol('tt', positive=True)
numer5 = sp.Integral(sp.sin(tt**2), (tt, 0, sp.sqrt(xpos)))
dnum5 = sp.diff(numer5, xpos).doit()
assert same(dnum5, sp.sin(xpos)/(2*sp.sqrt(xpos)))
assert abs(sp.N(numer5.subs(xpos, sp.Rational(1, 10**4))/sp.Rational(1, 10**4)**R(3, 2)) - 1/3) < 1e-3
assert sp.limit(dnum5/sp.diff(xpos**R(3, 2), xpos), xpos, 0, '+') == R(1, 3)

add(5, "א",
    rubric=rub(("זיהוי $\\frac00$ והפעלת לופיטל", 3),
               ("גזירת המונה לפי המשפט היסודי וכלל השרשרת: $\\sin x\\cdot\\frac{1}{2\\sqrt x}$", 3),
               ("גזירת המכנה $\\frac32\\sqrt x$ וצמצום ל-$\\frac{\\sin x}{3x}$", 2),
               ("ערך הגבול $\\frac13$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את כלל השרשרת של הגבול העליון $\\sqrt x$ (הגורם $\\frac{1}{2\\sqrt x}$).",
              "להציב $t^2\\to x$ בתוך האינטגרנד: בגבול העליון $\\sqrt x$ מתקבל $\\sin\\left((\\sqrt x)^2\\right)=\\sin x$.",
              "לטעות בנגזרת המכנה: $\\left(x^{3/2}\\right)'=\\frac32x^{1/2}$."],
    steps=[
        ch("מה סוג הצורה הלא מסוימת של $\\frac{\\int_0^{\\sqrt x}\\sin(t^2)dt}{x^{3/2}}$ כאשר $x\\to0^+$?", "$\\frac00$",
           ["$\\frac\\infty\\infty$", "$1^\\infty$", "$0\\cdot\\infty$"],
           "המונה הוא אינטגרל על קטע שמתכווץ ל-$0$ והמכנה $x^{3/2}\\to0$."),
        chx("מהי הנגזרת של המונה לפי $x$?", sp.sin(xpos)/(2*sp.sqrt(xpos)),
            [sp.sin(xpos), sp.sin(xpos)/sp.sqrt(xpos), sp.cos(xpos)/(2*sp.sqrt(xpos))], lambda e: same(e, dnum5),
            "משפט יסודי עם כלל שרשרת: $\\sin\\left((\\sqrt x)^2\\right)\\cdot\\frac{1}{2\\sqrt x}=\\frac{\\sin x}{2\\sqrt x}$ (אומת ב-sympy)."),
        num("מהו ערך הגבול? (עשרוני)", R(1, 3), "$\\frac{\\sin x/(2\\sqrt x)}{\\frac32\\sqrt x}=\\frac{\\sin x}{3x}\\to\\frac13$.", tol=0.0005),
    ],
    stepsSource="ai-verified")

# ===== Q5b: continuity at 0 with parameters =====
def left5(av):
    return sp.limit(x**-2*(sp.exp(av*x) - 1)**2, x, 0, '-')


def right5(av):
    return sp.limit(4 + sp.exp(-av**2/x), x, 0, '+')


assert left5(3) == 9 and right5(3) == 4 and right5(0) == 5
assert (left5(2), right5(2), left5(-2), right5(-2)) == (4, 4, 4, 4)
assert (left5(0), right5(0)) == (0, 5) and left5(4) == 16

add(5, "ב",
    rubric=rub(("הגבול משמאל: $\\left(\\lim\\frac{e^{ax}-1}{x}\\right)^2=a^2$", 3),
               ("הגבול מימין: $4$ כאשר $a\\ne0$ (ו-$5$ כאשר $a=0$)", 3),
               ("דרישת הרציפות $a^2=b=4$", 2),
               ("תשובה: $b=4$, $a=\\pm2$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את המקרה $a=0$ בגבול הימני, שבו $e^{-a^2/x}=1$ והגבול $5$ ולא $4$.",
              "לקבל $a=2$ בלבד ולשכוח את $a=-2$.",
              "לחשב את הגבול השמאלי כ-$a$ במקום $a^2$ (הביטוי בריבוע)."],
    steps=[
        num("מהו $\\lim_{x\\to0^-}x^{-2}\\left(e^{ax}-1\\right)^2$ עבור $a=3$?", left5(3), "$\\left(\\frac{e^{ax}-1}{x}\\right)^2\\to a^2=9$."),
        num("מהו $\\lim_{x\\to0^+}\\left(4+e^{-a^2/x}\\right)$ עבור $a\\neq0$?", right5(3), "$-\\frac{a^2}{x}\\to-\\infty$, לכן $e^{-a^2/x}\\to0$ והגבול $4$."),
        num("מהו הערך של $b$?", 4, "הגבול הימני הוא $4$ ולכן $b=4$."),
        ch("מהם ערכי $a$ האפשריים?", "$a=2$ או $a=-2$",
           ["$a=2$ בלבד", "$a=0$", "$a=4$ או $a=-4$"],
           "דרוש $a^2=4$. עבור $a=0$ הגבול הימני $5$ והשמאלי $0$; עבור $a=\\pm4$ השמאלי $16$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: tan x > x via Lagrange =====
assert same(sp.diff(sp.tan(x), x), 1/sp.cos(x)**2)
assert all(1/sp.cos(v)**2 > 1 for v in (R(1, 10), R(1, 2), 1, R(3, 2)))
L6 = ["הפונקציה $\\tan$ רציפה וגזירה בקטע $[0,x]$ לכל $0<x<\\frac\\pi2$, ולכן מתקיימים תנאי משפט לגרנז'.",
      "קיימת $c\\in(0,x)$ כך ש-$\\frac{1}{\\cos^2c}=\\frac{\\tan x-\\tan0}{x-0}=\\frac{\\tan x}{x}$.",
      "כיוון ש-$0<\\cos^2c<1$ מתקיים $\\frac{1}{\\cos^2c}>1$.",
      "לכן $\\frac{\\tan x}{x}>1$, כלומר $\\tan x>x$."]
L6b = list(L6)
L6b[2] = "כיוון ש-$0<\\cos^2c<1$ מתקיים $\\frac{1}{\\cos^2c}<1$."

add(6, "א",
    rubric=rub(("בחירת $f(x)=\\tan x$ על הקטע $[0,x]$ ובדיקת תנאי לגרנז' (רציפות וגזירות)", 3),
               ("כתיבת השוויון $f'(c)=\\frac{\\tan x-\\tan0}{x-0}$ עם $f'(c)=\\frac{1}{\\cos^2c}$", 3),
               ("הערכה $0<\\cos^2c<1\\Rightarrow\\frac{1}{\\cos^2c}>1$", 3),
               ("מסקנה $\\tan x>x$", 1)),
    rubricSource="ai-verified",
    pitfalls=["להפעיל לגרנז' על קטע שבו $\\tan$ אינה רציפה: חייבים להישאר ב-$\\left[0,x\\right]$ עם $x<\\frac\\pi2$.",
              "לשכוח שהאי-שוויון $\\frac{1}{\\cos^2c}>1$ דורש $c\\neq0$, והנקודה $c$ בקטע הפתוח $(0,x)$.",
              "לטעות בנגזרת של $\\tan$: היא $\\frac{1}{\\cos^2x}$ ולא $\\frac{1}{\\sin^2x}$."],
    steps=[
        chx("מהי הנגזרת של $\\tan x$?", 1/sp.cos(x)**2,
            [1/sp.sin(x)**2, -1/sp.cos(x)**2, sp.cos(x)], lambda e: same(e, sp.diff(sp.tan(x), x)),
            "$\\tan'x=\\frac{1}{\\cos^2x}$ (אומת ב-sympy)."),
        order("סדרו את שלבי ההוכחה.", L6, "בדיקת התנאים, משפט לגרנז', הערכת $\\frac{1}{\\cos^2c}$, מסקנה. כל שלב מסתמך על קודמו."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L6b, 2,
                "כש-$0<\\cos^2c<1$ ההופכי גדול מ-$1$, לא קטן (נבדק ב-sympy בנקודות לדוגמה)."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: area between x-axis, y = sqrt(2x-5) and its tangent at x = 3 =====
f6 = sp.sqrt(2*x - 5)
assert sp.diff(f6, x).subs(x, 3) == 1 and f6.subs(x, 3) == 1
tan6 = x - 2
assert same(tan6, 1 + 1*(x - 3)) and sp.solve(tan6, x) == [2] and sp.solve(f6, x) == [R(5, 2)]
S6 = sp.integrate(tan6, (x, 2, 3)) - sp.integrate(f6, (x, R(5, 2), 3))
assert S6 == R(1, 6)

add(6, "ב",
    rubric=rub(("שיפוע המשיק $y'(3)=1$ ומשוואתו $y=x-2$", 3),
               ("חיתוכים עם ציר ה-$x$: משיק ב-$x=2$, עקום ב-$x=\\frac52$", 2),
               ("הצבת השטח כשטח משולש/אינטגרל של המשיק פחות האינטגרל של העקום", 3),
               ("חישוב $\\frac12-\\frac13=\\frac16$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח שהעקום מתחיל ב-$x=\\frac52$ ולא ב-$x=2$, ולכן הפרש האינטגרלים נעשה בשני קטעים שונים.",
              "לטעות בנגזרת השורש: $\\left(\\sqrt{2x-5}\\right)'=\\frac{1}{\\sqrt{2x-5}}$ (כלל שרשרת, הגורם $2$ מצטמצם).",
              "לחשב $\\int_2^3\\left(x-2-\\sqrt{2x-5}\\right)dx$ כשהעקום לא מוגדר לפני $\\frac52$."],
    steps=[
        num("מהו שיפוע המשיק לעקום $y=\\sqrt{2x-5}$ ב-$x=3$?", sp.diff(f6, x).subs(x, 3), "$y'=\\frac{1}{\\sqrt{2x-5}}$ ולכן $y'(3)=1$."),
        chx("מהי משוואת המשיק $y=\\ ?$", x - 2, [x - 1, 2*x - 5, x - 3], lambda e: same(e, tan6),
            "המשיק עובר ב-$(3,1)$ עם שיפוע $1$: $y-1=x-3$ כלומר $y=x-2$."),
        num("באיזה ערך $x$ חותך המשיק את ציר ה-$x$?", 2, "$x-2=0$ נותן $x=2$."),
        num("מהו השטח? (עשרוני)", S6, "$\\int_2^3(x-2)dx-\\int_{5/2}^3\\sqrt{2x-5}\\,dx=\\frac12-\\frac13=\\frac16\\approx0.1667$.", tol=0.001),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "24A-A",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ד, מועד א'",
    "year": 2024,
    "examDate": "19/03/2024",
    "sourceFile": "calculus-1/24A-A exam+solution.pdf",
    "solutionFile": "calculus-1/24A-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

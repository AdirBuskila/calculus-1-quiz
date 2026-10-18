# -*- coding: utf-8 -*-
"""Generator for tools/raw/17A-A.json -- calculus-1 (20151), semester A 2017, moed A (printed date 25.06.17).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_17A-A.py

Source: sitting 17A-A, pp.1-7 (typed exam; the official worked solution follows every question).
Part A (mandatory): Q1 (20%). Part B: choose 4 of Q2-Q6 (each split into parts a/b, 10% each).

Transcription notes
- Q1: the sketch printed in the official solution is cropped as a figure; sign diagrams are transcribed as sentences.
- Q4a: the printed text carries the function definition and, separately, "for which a is f continuous at x=a?"
  (each followed by "(10%)"); merged into one part a whose solution holds both the limit and the value of a.
- Q4b: the printed stem has a stray "Q" after dx ("dxQ"); the solution names the integral Q. Stem written with dx.
- Q6a: the official solution computes P2(1.05) as 1.02466875 and concludes 1.02467 +- 1e-5. The correct value is
  1.0246875 and the interval must be 1.02469 +- 1e-5 (the true sqrt(1.05)=1.024695 lies outside the printed one).
  Final-answer error: shipped with the "הפתרון הרשמי עם תיקון" label, solutionSource solved, official:false.

Checks: tools/verify/17A-A/check.py (sympy), 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "17A-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**תחום הגדרה:** $x\in(-\infty,1)\cup(1,\infty)$.
**אסימפטוטה אנכית:** $x=1$:
$$\lim_{x\to1^+}\frac{4x^2-2x-1}{x-1}=\frac1{0^+}=+\infty$$
$$\lim_{x\to1^-}\frac{4x^2-2x-1}{x-1}=\frac1{0^-}=-\infty$$
**אסימפטוטה משופעת:**
$$a_\pm=\lim_{x\to\pm\infty}\frac{4x^2-2x-1}{x(x-1)}=4$$
$$b_\pm=\lim_{x\to\pm\infty}\left(\frac{4x^2-2x-1}{x-1}-4x\right)=\lim_{x\to\pm\infty}\frac{2x-1}{x-1}=2$$
$$y=4x+2$$
**תחומי עלייה וירידה, נקודות קיצון:**
$$y'=\frac{(8x-2)(x-1)-\left(4x^2-2x-1\right)}{(x-1)^2}=\frac{4x^2-8x+3}{(x-1)^2}=0$$
$$x_1=\frac12,\quad x_2=\frac32$$
סימני נגזרת: חיובית ב-$x<\frac12$ (עולה), שלילית ב-$\frac12<x<1$ וב-$1<x<\frac32$ (יורדת), חיובית ב-$x>\frac32$ (עולה).
$$y_{max}=y(0.5)=2,\quad y_{min}=y(1.5)=10$$
**תחומי קמירות וקעירות, נקודות פיתול:**
$$y''=\frac{2}{(x-1)^3}$$
סימני נגזרת שנייה: שלילית ב-$x<1$ (קעורה, $\cap$), חיובית ב-$x>1$ (קמורה, $\cup$). אין נקודת פיתול.
נקודות חיתוך עם צירים: $(0,1)$, $\left(\frac{1+\sqrt5}{4},0\right)$, $\left(\frac{1-\sqrt5}{4},0\right)$.
![שרטוט הגרף של y = (4x² − 2x − 1)/(x − 1) עם האסימפטוטה האנכית x = 1 והאסימפטוטה המשופעת y = 4x + 2](images/exams/17A-A-Q1-graph.png)
"""

SOL2A = r"""
נוכיח שהסדרה חסומה: $a_n\le4.5$.
בסיס האינדוקציה: $a_1=1\le4.5$.
הנחת האינדוקציה: $a_n\le4.5$. מכאן:
$$\frac{a_n}{3}\le1.5\ \Rightarrow\ \frac{a_n}{3}+3\le4.5\ \Rightarrow\ a_{n+1}\le4.5$$
לפי עיקרון האינדוקציה הוכחנו שלכל $n$ מתקיים $a_n\le4.5$.
נוכיח שהסדרה עולה מונוטונית:
בסיס האינדוקציה: $a_2=\frac{10}{3}\ge1=a_1$.
הנחת האינדוקציה: $a_{n+1}\ge a_n$. מכאן:
$$\frac{a_{n+1}}{3}\ge\frac{a_n}{3}\ \Rightarrow\ \frac{a_{n+1}}{3}+3\ge\frac{a_n}{3}+3\ \Rightarrow\ a_{n+2}\ge a_{n+1}$$
לפי עיקרון האינדוקציה הוכחנו שלכל $n$ מתקיים $a_{n+1}\ge a_n$.
הוכחנו שהסדרה חסומה מלמעלה ועולה מונוטונית, לכן לפי משפט ווירשטרס היא מתכנסת. נחשב גבול:
$$\lim_{n\to\infty}a_{n+1}=\frac13\lim_{n\to\infty}a_n+3,\quad L=\frac13L+3,\quad\frac23L=3,\quad L=4.5$$
"""

SOL2B = r"""
$$\int\frac{dx}{\cos^2x+4\cos^4x}=\left\{\begin{matrix}\tan x=t,\quad x=\arctan t,\quad dx=\frac{dt}{1+t^2}\\\cos^2x=\frac1{1+t^2}\end{matrix}\right\}=$$
$$=\int\frac{\frac{dt}{1+t^2}}{\frac1{1+t^2}+\frac4{\left(1+t^2\right)^2}}=\int\frac{\left(1+t^2\right)dt}{5+t^2}=\int\left(1-\frac4{5+t^2}\right)dt=$$
$$=t-\frac4{\sqrt5}\arctan\frac t{\sqrt5}=\tan x-\frac4{\sqrt5}\arctan\frac{\tan x}{\sqrt5}+C$$
"""

SOL3A = r"""
$$p=(\cos x)^{\frac1{x\sin x}},\qquad\ln p=\frac1{x\sin x}\ln\cos x$$
$$\ln p=\frac{\ln\cos x}{x\sin x},\qquad\lim_{x\to0}\ln p=\lim_{x\to0}\frac{\ln\cos x}{x\sin x}=\left[\frac00\right]=\lim_{x\to0}\frac{\frac{-\sin x}{\cos x}}{\sin x+x\cos x}=$$
$$=\lim_{x\to0}\frac{-\sin x}{\cos x\left(\sin x+x\cos x\right)}=\lim_{x\to0}\frac{-1}{\cos x\left(1+\frac x{\sin x}\cos x\right)}=-\frac12$$
$$p=e^{-0.5}$$
"""

SOL3B = r"""
$$y=\cos\left(\frac{\pi e^x}{6}\right)$$
$$\Delta x=0.1,\quad x_0=0$$
$$y(0)=\frac{\sqrt3}{2},\qquad y'(x)=-\frac\pi6e^x\sin\frac{\pi e^x}{6},\qquad y'(0)=-\frac\pi6\sin\frac\pi6=-\frac\pi{12}$$
$$y(0.1)-y(0)\approx y'(0)\Delta x$$
$$y(0.1)\approx y(0)+y'(0)\Delta x=\frac{\sqrt3}{2}-\frac\pi{12}\cdot0.1\approx0.8398\approx0.84$$
"""

SOL4A = r"""
$$\lim_{x\to a}\frac{\sqrt{2x-a}-\sqrt x}{x^2-a^2}=\lim_{x\to a}\frac{2x-a-x}{(x-a)(x+a)\left(\sqrt{2x-a}+\sqrt x\right)}=$$
$$=\lim_{x\to a}\frac{x-a}{(x-a)(x+a)\left(\sqrt{2x-a}+\sqrt x\right)}=\lim_{x\to a}\frac1{(x+a)\left(\sqrt{2x-a}+\sqrt x\right)}=$$
$$=\frac1{4a\sqrt a}$$
הפונקציה רציפה בנקודה $x=a$ כאשר הגבול שווה לערך הפונקציה בנקודה:
$$\frac1{4a\sqrt a}=\sqrt a,\quad4a^2=1,\quad a=0.5$$
"""

SOL4B = r"""
$$Q=\int_0^1e^x\sin(\pi x)\,dx=\left\{\begin{matrix}u=\sin(\pi x),&dv=e^x\,dx\\du=\pi\cos\pi x\,dx,&v=e^x\end{matrix}\right\}=$$
$$=\left(e^x\sin(\pi x)\right)\Big|_0^1-\pi\int_0^1e^x\cos\pi x\,dx=\left\{\begin{matrix}u=\cos(\pi x),&dv=e^x\,dx\\du=-\pi\sin\pi x\,dx,&v=e^x\end{matrix}\right\}=$$
$$=e^1\sin(\pi)-e^0\sin0-\pi\left\{\left(e^x\cos(\pi x)\right)\Big|_0^1+\pi\int_0^1e^x\sin\pi x\,dx\right\}=$$
$$=\pi(e+1)-\pi^2Q$$
$$Q=\frac{\pi(e+1)}{1+\pi^2}$$
"""

SOL5A = r"""
$$y'=\sqrt[3]{(3x-12)^2}+\frac23x\frac{3}{\sqrt[3]{3x-12}}$$
$$y'=\frac{3x-12+2x}{\sqrt[3]{3x-12}}=\frac{5x-12}{\sqrt[3]{3x-12}}$$
תחום הגדרה של הנגזרת: $x\ne4$. בנקודה $x=4$ הפונקציה מוגדרת, לכן $x=4$ היא נקודה חשודה.
$$y'=0\ \Rightarrow\ x=2.4$$
$$y(0)=0,\qquad y(2.4)\cong6.829,\quad y(4)=0,\quad y(6)\cong19.81$$
$$y_{max}=y(6)=6\cdot\sqrt[3]{36}\cong19.81$$
$$y_{min}=y(0)=y(4)=0$$
"""

SOL5B = r"""
$$\frac{x^3+3x^2+5}{x\left(x^2+2x+5\right)}=1+\frac{x^2-5x+5}{x\left(x^2+2x+5\right)}$$
$$\frac{x^2-5x+5}{x\left(x^2+2x+5\right)}=\frac Ax+\frac{Bx+C}{x^2+2x+5}$$
$$x^2-5x+5=A\left(x^2+2x+5\right)+x(Bx+C)$$
$$x=0\ \Rightarrow\ 5=5A,\quad A=1$$
$$x^2:\quad1=A+B,\quad B=0$$
$$x:\quad-5=2A+C,\quad C=-7$$
$$\int\frac{\left(x^3+3x^2+5\right)dx}{x\left(x^2+2x+5\right)}=\int\left(1+\frac1x-\frac7{(x+1)^2+4}\right)dx=x+\ln|x|-\frac72\arctan\frac{x+1}{2}+C$$
"""

SOL6A = r"""
הפתרון הרשמי עם תיקון: בפתרון הרשמי חושב $P_2(1.05)=1.02466875$ והתשובה נכתבה כ-$1.02467\pm10^{-5}$. הערך הנכון הוא $P_2(1.05)=1.0246875$, והתשובה היא $1.02469\pm10^{-5}$ (הערך המדויק $\sqrt{1.05}=1.024695\ldots$ אינו נמצא בקטע שנכתב בפתרון הרשמי). התיקון נבדק (sympy).
$$f(x)=\sqrt x,\quad f(1)=1$$
$$f'(x)=\frac1{2\sqrt x},\quad f'(1)=\frac12$$
$$f''(x)=-\frac1{4\sqrt{x^3}},\quad f''(1)=-\frac14$$
$$f'''(x)=\frac3{8\sqrt{x^5}},\quad f'''(c)=\frac3{8\sqrt{c^5}}$$
$$P_2(x)=1+0.5(x-1)-\frac18(x-1)^2$$
$$\sqrt{1.05}\approx P_2(1.05)=1+0.5(0.05)-\frac18(0.05)^2=1.0246875$$
$$|R_2|=\frac{(0.05)^3}{16\sqrt{c^5}}\le\frac{(0.05)^3}{16}=7.81\cdot10^{-6}<10^{-5}$$
$$\sqrt{1.05}\approx1.02469\pm10^{-5}$$
"""

SOL6B = r"""
נקודות חיתוך בין הקווים: $x=0$, $x=2$:
$$S=\int_0^2\left(\sqrt{32x}-x^3\right)dx=\left(\sqrt{32}\cdot\frac{2\sqrt{x^3}}{3}-\frac{x^4}{4}\right)\Bigg|_0^2=\frac{32}{3}-4\approx6.67$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה הבאה $y=\frac{4x^2-2x-1}{x-1}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, "
      "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.", SOL1),

    Q(2, "proof", "sequences_limits",
      r"נתונה הסדרה $a_1=1,\ a_{n+1}=\frac{a_n}{3}+3$. הוכח שהסדרה מתכנסת וחשב את גבולה.",
      SOL2A, part="א", points=10),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{dx}{\cos^2x+4\cos^4x}$.", SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to0}(\cos x)^{\frac1{x\sin x}}$.", SOL3A, part="א", points=10),

    Q(3, "computation", "derivatives_tangents",
      r"חשבו בקירוב באמצעות דיפרנציאל $\cos\left(\frac{\pi e^{0.1}}{6}\right)$. "
      r"(ידוע כי $\sin(\pi/6)=0.5$, $\cos(\pi/6)=\sqrt3/2$).", SOL3B, part="ב", points=10),

    Q(4, "computation", "continuity",
      r"נתונה הפונקציה $f(x)$ עם פרמטר $a>0$: "
      r"$f(x)=\begin{cases}\dfrac{\sqrt{2x-a}-\sqrt x}{x^2-a^2},&x\ne a\\[2mm]\sqrt a,&x=a\end{cases}$. "
      r"עבור איזה ערך של פרמטר $a$ הפונקציה רציפה בנקודה $x=a$?", SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"חשבו: $\int_0^1e^x\sin(\pi x)\,dx$.", SOL4B, part="ב", points=10),

    Q(5, "computation", "extrema_optimization",
      r"מצאו מינימום ומקסימום מוחלטים של הפונקציה $y=x\cdot\sqrt[3]{(3x-12)^2}$ בקטע $[0,6]$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int\frac{\left(x^3+3x^2+5\right)dx}{x\left(x^2+2x+5\right)}$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "lhopital_taylor",
      r"מצאו פולינום טיילור מסדר שני לפונקציה $f(x)=\sqrt x$ סביב נקודה $x_0=1$, חשב בעזרת הפולינום בקירוב "
      r"$\sqrt{1.05}$ והערך את שגיאת החישוב.", SOL6A, part="א", points=10,
      solutionSource="solved", official=False),

    Q(6, "computation", "definite_integrals",
      r"חשבו שטח הכלוא בין גרפים של פונקציות $y=x^3$ ו-$y=\sqrt{32x}$.", SOL6B, part="ב", points=10),
]

# ---- steps / rubric / pitfalls (ai-draft); every value below is computed or asserted with sympy ----
import sympy as sp

IDS = "abcdef"
_rot = [0]
x, t, a, b = sp.symbols('x t a b', real=True)
n = sp.Symbol('n', positive=True)
R = sp.Rational
SYMNAMES = {}  # display names for scratch symbols (set where they are defined)
TOPSRC = {}


def T(e):
    """TeX of a sympy expression, wrapped in $...$."""
    return "$" + sp.latex(e, symbol_names=SYMNAMES) + "$"


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

# ===== Q1: y = (4x^2-2x-1)/(x-1) =====
f1 = (4*x**2 - 2*x - 1)/(x - 1)
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, (4*x**2 - 8*x + 3)/(x - 1)**2) and same(f1pp, 2/(x - 1)**3)
crit1 = sorted(sp.solve(sp.numer(sp.together(f1p)), x))
assert crit1 == [R(1, 2), R(3, 2)]
assert (f1.subs(x, R(1, 2)), f1.subs(x, R(3, 2))) == (2, 10)
assert f1p.subs(x, 0) > 0 and f1p.subs(x, R(6, 5)) < 0 and f1p.subs(x, 2) > 0
assert sp.limit(f1/x, x, sp.oo) == 4 and sp.limit(f1 - 4*x, x, sp.oo) == 2 and sp.limit(f1 - 4*x, x, -sp.oo) == 2
assert sp.limit(f1, x, 1, '+') == sp.oo and sp.limit(f1, x, 1, '-') == -sp.oo

add(1,
    rubric=rub(("תחום הגדרה $x\\neq1$ ואסימפטוטה אנכית $x=1$ עם הגבולות החד-צדדיים $\\pm\\infty$", 4),
               ("אסימפטוטה משופעת $y=4x+2$ (שיפוע $4$ ופרמטר חופשי $2$)", 4),
               ("נגזרת $y'=\\frac{4x^2-8x+3}{(x-1)^2}$, נקודות קריטיות $\\frac12,\\frac32$ ותחומי עליה וירידה", 5),
               ("ערכי הקיצון: מקסימום מקומי $2$ ומינימום מקומי $10$", 3),
               ("$y''=\\frac{2}{(x-1)^3}$: קעירות עבור $x<1$, קמירות עבור $x>1$, ללא נקודות פיתול", 3),
               ("חיתוכים עם הצירים ושרטוט", 1)),
    rubricSource="ai-verified",
    pitfalls=["להתייחס ל-$x=1$ כאל נקודת קיצון או חלק מתחום העליה והירידה, למרות שהיא מחוץ לתחום ההגדרה.",
              "לחשב את האסימפטוטה המשופעת בלי הפרמטר החופשי: הוא $\\lim\\left(f(x)-4x\\right)=2$ ולא $0$.",
              "לטעון לנקודת פיתול ב-$x=1$: $y''$ אמנם משנה שם סימן, אבל $x=1$ אינה בתחום ההגדרה."],
    steps=[
        chx("מהי הנגזרת של $y=\\frac{4x^2-2x-1}{x-1}$?", (4*x**2 - 8*x + 3)/(x - 1)**2,
            [(4*x**2 - 8*x - 3)/(x - 1)**2, (4*x**2 - 8*x + 3)/(x - 1), (8*x - 2)/(x - 1)**2],
            lambda e: same(e, f1p),
            "כלל המנה: $\\frac{(8x-2)(x-1)-(4x^2-2x-1)}{(x-1)^2}=\\frac{4x^2-8x+3}{(x-1)^2}$ (אומת ב-sympy)."),
        num("מהו ערך $x$ הקטן מבין שתי הנקודות הקריטיות? (עשרוני)", crit1[0],
            "$4x^2-8x+3=0$ נותן $x=\\frac12$ או $x=\\frac32$."),
        num("מהו הערך של $y$ בנקודת המקסימום המקומי $x=\\frac12$?", 2, "$y\\left(\\frac12\\right)=\\frac{1-1-1}{-\\frac12}=2$ (sympy)."),
        num("מהו הערך של $y$ בנקודת המינימום המקומי $x=\\frac32$?", 10, "$y\\left(\\frac32\\right)=\\frac{9-3-1}{\\frac12}=10$ (sympy)."),
        ch("מהי האסימפטוטה המשופעת של $y$?", "$y=4x+2$",
           ["$y=4x$", "$y=4x-2$", "$y=4x+1$", "אין אסימפטוטה משופעת"],
           "$\\lim\\frac{y}{x}=4$ ו-$\\lim(y-4x)=\\lim\\frac{2x-1}{x-1}=2$ (אומת ב-sympy, ב-$+\\infty$ וב-$-\\infty$)."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: a_{n+1} = a_n/3 + 3, a_1 = 1 =====
seq = [R(1)]
for _ in range(5):
    seq.append(seq[-1]/3 + 3)
assert all(seq[i] < seq[i + 1] <= R(9, 2) for i in range(5)) and seq[1] == R(10, 3)
L2a = sp.Symbol('L')
assert sp.solve(sp.Eq(L2a, L2a/3 + 3), L2a) == [R(9, 2)]
BP = ["בסיס: $a_1=1\\le4.5$. הנחה: $a_n\\le4.5$.",
      "מכאן $\\frac{a_n}{3}\\le1.5$, ולכן $a_{n+1}=\\frac{a_n}{3}+3\\le4.5$.",
      "לפי עיקרון האינדוקציה $a_n\\le4.5$ לכל $n$."]
MP = ["בסיס: $a_2=\\frac{10}{3}\\ge1=a_1$.",
      "הנחת האינדוקציה: $a_{n+1}\\ge a_n$.",
      "מכאן $\\frac{a_{n+1}}{3}+3\\ge\\frac{a_n}{3}+3$, כלומר $a_{n+2}\\ge a_{n+1}$.",
      "לפי עיקרון האינדוקציה $a_{n+1}\\ge a_n$ לכל $n$."]
MPb = list(MP)
MPb[2] = "מכאן $\\frac{a_{n+1}}{3}+3\\ge\\frac{a_n}{3}+3$, כלומר $a_{n+2}\\le a_{n+1}$."

add(2, "א",
    rubric=rub(("הוכחה באינדוקציה שהסדרה חסומה מלמעלה: $a_n\\le4.5$", 3),
               ("הוכחה באינדוקציה שהסדרה עולה: $a_{n+1}\\ge a_n$", 3),
               ("מסקנה: סדרה עולה וחסומה מתכנסת (ווירשטראס)", 1),
               ("מעבר לגבול במשוואת הנסיגה: $L=\\frac{L}{3}+3$ ו-$L=4.5$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לחשב את הגבול מהמשוואה $L=\\frac{L}{3}+3$ בלי להוכיח קודם שהגבול קיים.",
              "להוכיח רק חסימות או רק מונוטוניות: שתיהן נדרשות כדי להפעיל את משפט ווירשטראס.",
              "בצעד האינדוקציה של המונוטוניות להניח את מה שצריך להוכיח במקום להניח $a_{n+1}\\ge a_n$ ולהסיק $a_{n+2}\\ge a_{n+1}$."],
    steps=[
        ch("על איזה משפט נשען הפתרון הרשמי כדי להוכיח שהסדרה מתכנסת?",
           "סדרה עולה וחסומה מלמעלה מתכנסת (ווירשטראס)",
           ["סדרה שאיבריה חיוביים מתכנסת", "כל סדרה חסומה מתכנסת", "אם $a_{n+1}-a_n\\to0$ הסדרה מתכנסת"],
           "הפתרון מוכיח חסימות מלמעלה ומונוטוניות עולה. שלוש האפשרויות האחרות שגויות: הסדרה $(-1)^n$ חסומה ולא מתכנסת, ו-$\\sqrt n$ חיובית ו-$a_{n+1}-a_n\\to0$ אך אינה מתכנסת."),
        num("מהו $a_2$? (עשרוני)", seq[1], "$a_2=\\frac13+3=\\frac{10}{3}\\approx3.3333$."),
        num("מהו גבול הסדרה?", R(9, 2), "$L=\\frac{L}{3}+3$ נותן $\\frac23L=3$, כלומר $L=4.5$ (sympy)."),
        order("סדרו את הוכחת החסימות באינדוקציה.", BP, "בסיס והנחה, צעד האינדוקציה, מסקנה. הצעד נשען על ההנחה והמסקנה על הצעד."),
        findbug("בהוכחת המונוטוניות שורה אחת שגויה. מצאו אותה.", MPb, 2,
                "מהאי-שוויון $\\frac{a_{n+1}}{3}+3\\ge\\frac{a_n}{3}+3$ מקבלים $a_{n+2}\\ge a_{n+1}$ ולא $\\le$."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: int dx/(cos^2 + 4cos^4) =====
g2b = 1/(sp.cos(x)**2 + 4*sp.cos(x)**4)
F2b = sp.tan(x) - 4/sp.sqrt(5)*sp.atan(sp.tan(x)/sp.sqrt(5))
assert same(sp.diff(F2b, x), g2b)
tt = sp.Symbol('tt', positive=True)
SYMNAMES[tt] = "t"
assert same(((1 + tt**2)/(5 + tt**2)), 1 - 4/(5 + tt**2))
sub2b = (1/(1 + tt**2))/(1/(1 + tt**2) + 4/(1 + tt**2)**2)
assert same(sub2b, (1 + tt**2)/(5 + tt**2))
F2w = [sp.tan(x) - 4/sp.sqrt(5)*sp.atan(sp.tan(x)), sp.tan(x) + 4/sp.sqrt(5)*sp.atan(sp.tan(x)/sp.sqrt(5)),
       sp.tan(x) - R(4, 5)*sp.atan(sp.tan(x)/sp.sqrt(5))]

add(2, "ב",
    rubric=rub(("בחירת ההצבה $t=\\tan x$ וחישוב $dx$ ו-$\\cos^2x$ באמצעותה", 3),
               ("העברה לאינטגרל רציונלי $\\int\\frac{1+t^2}{5+t^2}dt$", 3),
               ("פירוק $1-\\frac{4}{5+t^2}$ ואינטגרציה (פולינום ו-$\\arctan$)", 2),
               ("חזרה למשתנה המקורי ותשובה סופית עם $+c$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את הגורם $dx=\\frac{dt}{1+t^2}$ בהצבה.",
              "לשכוח לחלק ב-$\\sqrt5$ בתוך ה-$\\arctan$, או לכתוב $\\frac{4}{5}$ במקום $\\frac{4}{\\sqrt5}$ כמקדם.",
              "לא לפרק את המנה: $\\frac{1+t^2}{5+t^2}$ מדרגה שווה ויש לפרק לפני האינטגרציה."],
    steps=[
        ch("איזו הצבה משתמש בה הפתרון הרשמי?", "$t=\\tan x$", ["$t=\\sin x$", "$t=\\cos x$", "$t=\\tan\\frac{x}{2}$"],
           "הפתרון מציב $t=\\tan x$ כך ש-$\\cos^2x=\\frac{1}{1+t^2}$ ו-$dx=\\frac{dt}{1+t^2}$."),
        chx("לאיזה אינטגרל מגיעים אחרי ההצבה? (מהי הפונקציה בתוך האינטגרל ב-$dt$)", (1 + tt**2)/(5 + tt**2),
            [(1 + tt**2)/(1 + 4*tt**2), 1/(5 + tt**2), (1 + tt**2)/(4 + tt**2)],
            lambda e: same(e, sub2b),
            "$\\frac{\\frac{1}{1+t^2}}{\\frac{1}{1+t^2}+\\frac{4}{(1+t^2)^2}}=\\frac{1+t^2}{5+t^2}$ (אומת ב-sympy)."),
        chx("מהו האינטגרל? (בלי הקבוע)", F2b, F2w, lambda e: same(sp.diff(e, x), g2b),
            "$\\int\\left(1-\\frac{4}{5+t^2}\\right)dt=t-\\frac{4}{\\sqrt5}\\arctan\\frac{t}{\\sqrt5}$. הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: lim (cos x)^(1/(x sin x)) =====
lim3a = sp.limit(sp.log(sp.cos(x))/(x*sp.sin(x)), x, 0)
assert lim3a == R(-1, 2) and sp.limit(sp.cos(x)**(1/(x*sp.sin(x))), x, 0) == sp.exp(R(-1, 2))
assert sp.limit(sp.log(sp.cos(x)), x, 0) == 0 and sp.limit(x*sp.sin(x), x, 0) == 0

add(3, "א",
    rubric=rub(("לוגריתם והפיכה למנה: $\\ln p=\\frac{\\ln\\cos x}{x\\sin x}$", 3),
               ("זיהוי $\\frac{0}{0}$ והפעלת לופיטל נכונה", 3),
               ("פישוט וחישוב $\\lim\\ln p=-\\frac12$", 2),
               ("חזרה לגבול המקורי $e^{-1/2}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לטעון שהגבול הוא $1$ בגלל $\\cos x\\to1$. הצורה $1^{\\infty}$ אינה מסוימת.",
              "לשכוח להעלות את הגבול של $\\ln p$ בחזקת $e$ בסוף.",
              "טעות בנגזרת המכנה: $(x\\sin x)'=\\sin x+x\\cos x$ (כלל מכפלה)."],
    steps=[
        ch("מה סוג הצורה הלא מסוימת של $(\\cos x)^{\\frac{1}{x\\sin x}}$ כאשר $x\\to0$?", "$1^{\\infty}$",
           ["$0^0$", "$\\infty^0$", "$\\frac00$"],
           "הבסיס $\\cos x\\to1$ והמעריך $\\frac{1}{x\\sin x}\\to\\infty$."),
        num("מהו $\\lim_{x\\to0}\\ln p$ כאשר $\\ln p=\\frac{\\ln\\cos x}{x\\sin x}$? (עשרוני)", lim3a,
            "לופיטל: $\\frac{-\\tan x}{\\sin x+x\\cos x}\\to\\frac{-1}{1+1}=-\\frac12$ (sympy)."),
        num("מהו הגבול המבוקש $\\lim_{x\\to0}(\\cos x)^{\\frac{1}{x\\sin x}}$? (עשרוני)", sp.exp(R(-1, 2)),
            "$p=e^{\\ln p}\\to e^{-1/2}\\approx0.6065$ (sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: differential of cos(pi e^x / 6) =====
y3 = sp.cos(sp.pi*sp.exp(x)/6)
y3p = sp.diff(y3, x)
assert same(y3p.subs(x, 0), -sp.pi/12) and y3.subs(x, 0) == sp.sqrt(3)/2
approx3 = sp.N(y3.subs(x, 0) + y3p.subs(x, 0)*R(1, 10), 15)
assert abs(float(approx3) - 0.8398) < 5e-5

add(3, "ב",
    rubric=rub(("הגדרת הפונקציה $y=\\cos\\frac{\\pi e^x}{6}$ והנקודה $x_0=0$, $\\Delta x=0.1$", 2),
               ("חישוב $y(0)=\\frac{\\sqrt3}{2}$", 2),
               ("חישוב הנגזרת $y'(0)=-\\frac{\\pi}{12}$ (כלל שרשרת)", 3),
               ("הצבה בנוסחת הדיפרנציאל וערך מקורב $\\approx0.84$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את גורם השרשרת $\\frac{\\pi}{6}e^x$ בגזירה.",
              "לחשב $\\Delta y$ בלבד ולשכוח להוסיף את $y(x_0)$.",
              "לשכוח את סימן המינוס בנגזרת הקוסינוס."],
    steps=[
        num("מהו $y(0)=\\cos\\frac{\\pi}{6}$? (עשרוני)", y3.subs(x, 0), "$\\frac{\\sqrt3}{2}\\approx0.8660$."),
        num("מהו $y'(0)$? (עשרוני)", y3p.subs(x, 0), "$y'(x)=-\\frac{\\pi}{6}e^x\\sin\\frac{\\pi e^x}{6}$ ולכן $y'(0)=-\\frac{\\pi}{6}\\cdot\\frac12=-\\frac{\\pi}{12}\\approx-0.2618$."),
        num("מהו הערך המקורב $y(0.1)\\approx y(0)+y'(0)\\Delta x$? (עשרוני)", approx3, "$0.8660-0.02618\\approx0.8398$ (sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: continuity with parameter a =====
def g4(av, xv):
    return (sp.sqrt(2*xv - av) - sp.sqrt(xv))/(xv**2 - av**2)
a4 = sp.Symbol('a4', positive=True)
for av in (R(1, 2), 1, 2, 5):
    assert sp.simplify(sp.limit(g4(av, x), x, av) - 1/(4*av*sp.sqrt(av))) == 0
assert sp.solve(sp.Eq(1/(4*a4*sp.sqrt(a4)), sp.sqrt(a4)), a4) == [R(1, 2)]
lim_ok = lambda e: all(sp.simplify(e.subs(a, av) - sp.limit(g4(av, x), x, av)) == 0 for av in (1, 2, 5))

add(4, "א",
    rubric=rub(("כפל בצמוד ופישוט המונה $2x-a-x=x-a$", 3),
               ("צמצום $x-a$ וחישוב הגבול $\\frac{1}{4a\\sqrt a}$", 3),
               ("דרישת רציפות: הגבול שווה ל-$\\sqrt a$", 2),
               ("פתרון המשוואה: $a=\\frac12$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להפעיל הצבה ישירה ולהישאר עם $\\frac00$ בלי לכפול בצמוד.",
              "לשכוח שיש לפרק גם את המכנה: $x^2-a^2=(x-a)(x+a)$.",
              "לבדוק רציפות רק לפי קיום הגבול, בלי להשוות אותו לערך $f(a)=\\sqrt a$."],
    steps=[
        ch("איך מתמודדים עם הצורה $\\frac00$ בגבול $\\frac{\\sqrt{2x-a}-\\sqrt x}{x^2-a^2}$ כאשר $x\\to a$?",
           "כפל המונה והמכנה בצמוד $\\sqrt{2x-a}+\\sqrt x$ ופירוק $x^2-a^2$",
           ["הצבה $x=a$ ישירות", "העלאה בריבוע של שני האגפים", "כפל בצמוד $\\sqrt{2x-a}-\\sqrt x$"],
           "כפל בצמוד $\\sqrt{2x-a}+\\sqrt x$ נותן מונה $2x-a-x=x-a$ שמצטמצם עם גורם המכנה $(x-a)$. הצבה ישירה נותנת $\\frac00$, וכפל בצמוד השני רק מחזיר את הביטוי המקורי בריבוע."),
        chx("מהו הגבול כאשר $x\\to a$? (עבור $a>0$)", 1/(4*a*sp.sqrt(a)),
            [1/(2*a*sp.sqrt(a)), 1/(4*a**2), 1/(8*a*sp.sqrt(a))], lim_ok,
            "אחרי הצמצום $\\frac{1}{(x+a)\\left(\\sqrt{2x-a}+\\sqrt x\\right)}\\to\\frac{1}{2a\\cdot2\\sqrt a}=\\frac{1}{4a\\sqrt a}$ (נבדק ב-sympy ל-$a=1,2,5$)."),
        num("מהו הערך של $a$ שעבורו הפונקציה רציפה? (עשרוני)", R(1, 2), "$\\frac{1}{4a\\sqrt a}=\\sqrt a$ נותן $4a^2=1$ ולכן $a=0.5$ (sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: int_0^1 e^x sin(pi x) =====
Q4 = sp.integrate(sp.exp(x)*sp.sin(sp.pi*x), (x, 0, 1))
assert same(Q4, sp.pi*(sp.E + 1)/(1 + sp.pi**2))
bnd = (sp.exp(x)*sp.cos(sp.pi*x)).subs(x, 1) - (sp.exp(x)*sp.cos(sp.pi*x)).subs(x, 0)
assert same(bnd, -sp.E - 1)
rel_ok = lambda rhs: abs(float(sp.N(Q4 - rhs(Q4)))) < 1e-9
assert rel_ok(lambda Q: sp.pi*(sp.E + 1) - sp.pi**2*Q)
for w in (lambda Q: sp.pi*(sp.E - 1) - sp.pi**2*Q, lambda Q: sp.pi*(sp.E + 1) + sp.pi**2*Q, lambda Q: -sp.pi*(sp.E + 1) - sp.pi**2*Q):
    assert not rel_ok(w)

add(4, "ב",
    rubric=rub(("אינטגרציה בחלקים ראשונה ($u=\\sin\\pi x$, $dv=e^xdx$), האיבר החוצץ מתאפס", 3),
               ("אינטגרציה בחלקים שנייה ($u=\\cos\\pi x$) וחזרה לאינטגרל המקורי", 3),
               ("משוואה ב-$Q$: $Q=\\pi(e+1)-\\pi^2Q$", 2),
               ("פתרון: $Q=\\frac{\\pi(e+1)}{1+\\pi^2}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["באינטגרציה בחלקים השנייה להחליף את התפקידים ($u=e^x$) ולחזור בדיוק לאינטגרל המקורי בלי להתקדם.",
              "טעות סימן ב-$\\left(e^x\\cos\\pi x\\right)\\Big|_0^1=-e-1$.",
              "לשכוח להעביר את $\\pi^2Q$ לאגף השני ולחלק ב-$1+\\pi^2$."],
    steps=[
        num("מהו הערך של $\\left(e^x\\sin\\pi x\\right)\\Big|_0^1$ באינטגרציה בחלקים הראשונה?", 0, "$e\\sin\\pi-e^0\\sin0=0$."),
        num("מהו הערך של $\\left(e^x\\cos\\pi x\\right)\\Big|_0^1$? (עשרוני)", bnd, "$e\\cos\\pi-\\cos0=-e-1\\approx-3.7183$ (sympy)."),
        ch("איזו משוואה מקבלים ל-$Q=\\int_0^1e^x\\sin\\pi x\\,dx$ אחרי שתי האינטגרציות בחלקים?",
           "$Q=\\pi(e+1)-\\pi^2Q$", ["$Q=\\pi(e-1)-\\pi^2Q$", "$Q=\\pi(e+1)+\\pi^2Q$", "$Q=-\\pi(e+1)-\\pi^2Q$"],
           "$Q=0-\\pi\\left\\{(-e-1)+\\pi Q\\right\\}=\\pi(e+1)-\\pi^2Q$. הערך המספרי של $Q$ מקיים את המשוואה הזו ולא את האחרות (נבדק ב-sympy)."),
        num("מהו הערך של $Q$? (עשרוני)", Q4, "$Q=\\frac{\\pi(e+1)}{1+\\pi^2}\\approx1.0747$ (בדיקה נומרית ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q5a: absolute extrema of x*((3x-12)^2)^(1/3) on [0,6] =====
y5 = x*((3*x - 12)**2)**R(1, 3)
y5p = lambda xv: sp.diff(y5, x).subs(x, xv)
assert abs(float(y5p(R(12, 5)))) < 1e-9
vals5 = {v: sp.N(y5.subs(x, v), 12) for v in (0, R(12, 5), 4, 6)}
assert abs(vals5[R(12, 5)] - 6.829) < 5e-3 and abs(vals5[6] - 19.81) < 5e-3 and vals5[0] == 0 and abs(vals5[4]) < 1e-9
assert max(vals5.values()) == vals5[6] and min(vals5.values()) == vals5[0]
assert abs(float(sp.N(y5p(5) - (5*5 - 12)/sp.real_root(3*5 - 12, 3)))) < 1e-9
assert abs(float(sp.N(y5p(1) - (5*1 - 12)/sp.real_root(3*1 - 12, 3)))) < 1e-9

add(5, "א",
    rubric=rub(("נגזרת $y'=\\frac{5x-12}{\\sqrt[3]{3x-12}}$", 3),
               ("נקודות חשודות: $x=2.4$ ($y'=0$) ו-$x=4$ (הנגזרת לא מוגדרת והפונקציה מוגדרת)", 3),
               ("ערכי הפונקציה בנקודות החשודות ובקצוות הקטע", 2),
               ("מקסימום מוחלט $6\\sqrt[3]{36}\\approx19.81$ ומינימום מוחלט $0$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לא לכלול את $x=4$ כנקודה חשודה: שם הנגזרת לא מוגדרת אבל הפונקציה כן.",
              "לשכוח לבדוק את קצוות הקטע $x=0$ ו-$x=6$.",
              "להסיק שהמינימום המוחלט הוא ב-$x=2.4$, שם יש מקסימום מקומי, ולא בנקודות שבהן הפונקציה מתאפסת."],
    steps=[
        num("מהו ערך $x$ שבו $y'=0$? (עשרוני)", R(12, 5), "$5x-12=0$ נותן $x=2.4$."),
        ch("מדוע $x=4$ נבדקת כנקודה חשודה?", "הנגזרת לא מוגדרת שם אבל הפונקציה מוגדרת",
           ["הנגזרת מתאפסת שם", "זו נקודת קצה של הקטע", "הפונקציה לא מוגדרת שם"],
           "ב-$x=4$ המכנה $\\sqrt[3]{3x-12}$ מתאפס, אבל $y(4)=0$ מוגדרת. הנגזרת מתאפסת רק ב-$x=2.4$, ו-$4$ אינה קצה של הקטע $[0,6]$."),
        num("מהו $y(2.4)$? (עשרוני)", vals5[R(12, 5)], "$y(2.4)=2.4\\cdot\\sqrt[3]{4.8^2}\\approx6.829$ (sympy)."),
        num("מהו המקסימום המוחלט של הפונקציה בקטע? (עשרוני)", vals5[6], "הערך בקצה $x=6$: $6\\sqrt[3]{36}\\approx19.81$, הגדול מבין $0,\\,6.829,\\,0,\\,19.81$."),
        num("מהו המינימום המוחלט של הפונקציה בקטע?", 0, "$y(0)=y(4)=0$ והערכים האחרים חיוביים."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: rational integral =====
g5 = (x**3 + 3*x**2 + 5)/(x*(x**2 + 2*x + 5))
rem5 = sp.simplify(g5 - 1)
assert same(rem5, (x**2 - 5*x + 5)/(x*(x**2 + 2*x + 5)))
A5, B5, C5 = sp.symbols('A5 B5 C5')
s5 = sp.solve(sp.Poly(sp.expand(A5*(x**2 + 2*x + 5) + x*(B5*x + C5) - (x**2 - 5*x + 5)), x).all_coeffs(), [A5, B5, C5], dict=True)[0]
assert s5 == {A5: 1, B5: 0, C5: -7}
F5 = x + sp.log(x) - R(7, 2)*sp.atan((x + 1)/2)
assert same(sp.diff(F5, x), g5)
F5w = [x + sp.log(x) - 7*sp.atan((x + 1)/2), x + sp.log(x) - R(7, 4)*sp.atan((x + 1)/2), x + sp.log(x) + R(7, 2)*sp.atan((x + 1)/2)]

add(5, "ב",
    rubric=rub(("חילוק פולינומים (דרגות שוות): $1+\\frac{x^2-5x+5}{x(x^2+2x+5)}$", 2),
               ("פירוק לשברים חלקיים $\\frac{A}{x}+\\frac{Bx+C}{x^2+2x+5}$", 2),
               ("חישוב המקדמים $A=1$, $B=0$, $C=-7$", 3),
               ("השלמה לריבוע, $\\arctan$ ותשובה סופית עם $+c$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לפרק לשברים חלקיים בלי לחלק קודם: דרגת המונה שווה לדרגת המכנה.",
              "ברכיב $\\frac{7}{(x+1)^2+4}$ לשכוח ש-$\\int\\frac{du}{u^2+4}=\\frac12\\arctan\\frac u2$, ולכן המקדם הסופי $\\frac72$ ולא $7$."],
    steps=[
        ch("מה הצעד הראשון בפתרון $\\int\\frac{x^3+3x^2+5}{x(x^2+2x+5)}dx$?",
           "חילוק פולינומים, כי דרגת המונה שווה לדרגת המכנה",
           ["הצבה $t=x^2+2x+5$", "אינטגרציה בחלקים", "פירוק ישיר לשברים חלקיים בלי חילוק"],
           "המכנה $x^3+2x^2+5x$ והמונה מאותה דרגה, ולכן מפרידים חלק שלם: $1+\\frac{x^2-5x+5}{x(x^2+2x+5)}$ (sympy). לפירוק ישיר אין פתרון, וההצבה אינה מפשטת את המונה."),
        num("מהו המקדם $A$ בפירוק $\\frac{A}{x}+\\frac{Bx+C}{x^2+2x+5}$?", s5[A5], "הצבת $x=0$ נותנת $5=5A$ ולכן $A=1$."),
        num("מהו המקדם $C$?", s5[C5], "מהמקדם של $x$: $-5=2A+C$ ולכן $C=-7$ (sympy)."),
        chx("מהו האינטגרל? (עבור $x>0$, בלי הקבוע)", F5, F5w, lambda e: same(sp.diff(e, x), g5),
            "$\\int\\left(1+\\frac1x-\\frac{7}{(x+1)^2+4}\\right)dx=x+\\ln x-\\frac72\\arctan\\frac{x+1}{2}$. הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: Taylor of sqrt(x) at 1 =====
fs = sp.sqrt(x)
P2 = sum(sp.diff(fs, x, k).subs(x, 1)/sp.factorial(k)*(x - 1)**k for k in range(3))
assert same(P2, 1 + (x - 1)/2 - (x - 1)**2/8)
P2v = P2.subs(x, R(105, 100))
assert P2v == R(10246875, 10000000)
rem_bound = sp.diff(fs, x, 3).subs(x, 1)/sp.factorial(3)*R(5, 100)**3
assert rem_bound == R(5, 100)**3/16 and 7.8e-6 < float(rem_bound) < 1e-5
assert abs(float(sp.sqrt(R(105, 100))) - float(P2v)) < float(rem_bound)

add(6, "א",
    rubric=rub(("נגזרות $f'(1)=\\frac12$, $f''(1)=-\\frac14$ וערך $f(1)=1$", 3),
               ("פולינום טיילור $P_2(x)=1+\\frac12(x-1)-\\frac18(x-1)^2$", 2),
               ("הערך המקורב $P_2(1.05)=1.0246875$", 2),
               ("שארית לגרנז' עם $f'''$ וחסם $\\frac{0.05^3}{16}<10^{-5}$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לחלק ב-$2$ במקום ב-$2!$ במקדם הריבועי: המקדם הוא $\\frac{f''(1)}{2}=-\\frac18$.",
              "לחשב את החסם בעזרת $f''$ במקום $f'''$: שארית של פולינום מסדר שני דורשת את הנגזרת השלישית.",
              "להעריך את $f'''(c)$ בנקודה כלשהי במקום לחסום אותה מלמעלה בקטע ($c\\ge1$ נותן $f'''(c)\\le\\frac38$)."],
    steps=[
        num("מהו המקדם של $(x-1)^2$ בפולינום טיילור $P_2$? (עשרוני)", R(-1, 8), "$\\frac{f''(1)}{2!}=\\frac{-1/4}{2}=-\\frac18=-0.125$ (sympy)."),
        {"type": "numeric", "prompt": "מהו הערך המקורב $P_2(1.05)$? (דיוק של שבע ספרות אחרי הנקודה)", "answer": 1.0246875, "tol": 0.0000005,
         "explain": "$1+0.5\\cdot0.05-\\frac18\\cdot0.05^2=1.0246875$ (sympy)."},
        chx("מהו חסם השגיאה לפי שארית לגרנז' עבור $x=1.05$?", rem_bound,
            [R(5, 100)**3/6, R(5, 100)**3/8, R(5, 100)**2/16], lambda e: e == rem_bound,
            "$\\frac{f'''(c)}{3!}(0.05)^3\\le\\frac{3/8}{6}(0.05)^3=\\frac{0.05^3}{16}\\approx7.81\\cdot10^{-6}$. שאר האפשרויות מתקבלות ממקדם או מחזקה שגויים."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: area between y=x^3 and y=sqrt(32x) =====
S6 = sp.integrate(sp.sqrt(32*x) - x**3, (x, 0, 2))
assert S6 == R(20, 3) and sp.solve(sp.Eq(x**5, 32), x)[0] == 2
assert sp.sqrt(32) > 1 and sp.integrate(sp.sqrt(32*x), (x, 0, 2)) == R(32, 3)

add(6, "ב",
    rubric=rub(("נקודות החיתוך $x=0$ ו-$x=2$", 2),
               ("קביעת הפונקציה העליונה בקטע ($\\sqrt{32x}$) והצבת האינטגרל", 3),
               ("מציאת הפונקציה הקדומה $\\sqrt{32}\\cdot\\frac{2\\sqrt{x^3}}{3}-\\frac{x^4}{4}$", 3),
               ("הצבת הגבולות והשטח $\\frac{20}{3}\\approx6.67$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להחסיר בסדר הפוך (התחתונה פחות העליונה) ולקבל שטח שלילי.",
              "לשכוח את נקודת החיתוך $x=0$, או לטעות בצמצום $x^6=32x$ ל-$x^5=32$."],
    steps=[
        num("מהו ערך $x$ החיובי שבו מתחתכים הגרפים?", 2, "$x^3=\\sqrt{32x}$ נותן $x^6=32x$, כלומר $x^5=32$ ו-$x=2$."),
        ch("איזה גרף נמצא למעלה בקטע $(0,2)$?", "$y=\\sqrt{32x}$", ["$y=x^3$", "הגרפים מתחלפים בקטע", "שני הגרפים זהים בקטע"],
           "לדוגמה ב-$x=1$: $\\sqrt{32}\\approx5.66>1=x^3$, ואין נקודת חיתוך נוספת בקטע."),
        num("מהו $\\int_0^2\\sqrt{32x}\\,dx$? (עשרוני)", R(32, 3), "$\\sqrt{32}\\cdot\\frac{2}{3}\\cdot2^{3/2}=\\frac{32}{3}\\approx10.667$ (sympy)."),
        num("מהו השטח הכלוא? (עשרוני)", S6, "$\\frac{32}{3}-\\frac{2^4}{4}=\\frac{32}{3}-4=\\frac{20}{3}\\approx6.667$ (sympy)."),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "17A-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ז, מועד א'",
    "year": 2017,
    "examDate": "25/06/2017",
    "sourceFile": "calculus-1/17A-A exam+solution.pdf",
    "solutionFile": "calculus-1/17A-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

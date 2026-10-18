# -*- coding: utf-8 -*-
"""Generator for tools/raw/21B-B.json -- calculus-1 (20151), semester B 2021 (תשפ"א), moed B.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_21B-B.py

Source: sitting 21B-B, pp.1-7 ("פתרונות מלאים למועד ב'": the question text, where printed, followed by the worked
solution; no separate exam file exists). Both source trees hold the identical file.

What the file does and does not contain
- Q1 (20%), Q3, Q4, Q5: stem and official solution are printed.
- Q2 is NOT in the file at all (p.1 ends with Q1 and p.3 starts with Q3). Held, reason "not-in-source".
- Q6a / Q6b: only the worked solution is printed, the question stems are not. The solutions are kept in raw next to
  the hold so the orchestrator can ship them once a stem is approved. Held, reason "stem-not-printed".
- Arbiter re-search 2026-10-18: the BSC and C24-BSC copies differ in file hash but render identically page by page
  (7 pages, same text); a text search of every other calculus-1 PDF in both trees (exams, practice sheets, summaries)
  finds no copy of the Q2 or Q6 stems (scanned files are not text-searchable). Holds kept; Adir must supply the stems.

Transcription notes
- Q1 sketch (p.2) and Q4b sketch (p.5) are shipped as figures inside the solutions.
- Q3a: the official solution is written in English and is kept as printed. Its conclusion "c in (-1,0)" is wrong
  (f(0)=5>0 and f(1)<0, f(-1)>0, so the sign change is on (0,1)); the printed f(1) = -3.99 is also off (-3.96).
  Final-line error -> "הפתרון הרשמי עם תיקון" label, solutionSource solved, official False.
- Q3b: the printed middle line drops a "ln" in "0.5 ln|t-3| - 0.5|t-1|"; restored silently (logged in ASK_ADIR).
- Q6a (held): the printed implicit derivative starts with 8x^4; d/dx(2x^4)=8x^3. The final slope 4 is unchanged;
  corrected silently (logged).

Checks (tools/verify/21B-B/check.py, sympy): every derivative, limit, extremum, parameter, integral, volume and area
matches the official answer, except the two slips named above. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "21B-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**I.**
1. $D(y)=(-\infty,-1)\cup(-1,\infty)$.
2. $\lim_{x\to-1^-}y=\lim_{x\to-1^+}y=+\infty$, לכן $x=-1$ נקודת אי-רציפות מסוג שני.
3. $k=\lim_{x\to\pm\infty}\frac{y}{x}=\lim_{x\to\pm\infty}\frac{(x+2)^2}{x(x+1)^2}=0,\quad b=\lim_{x\to\pm\infty}(y-kx)=\lim_{x\to\pm\infty}\frac{(x+2)^2}{(x+1)^2}=1$. הישרים $x=-1$ ו-$y=1$ הם אסימפטוטות.
4. $y\ge0$.
**II.**
1. $y'=2\frac{x+2}{x+1}\left(-\frac{1}{(x+1)^2}\right)=\frac{-2(x+2)}{(x+1)^3}$.
2. $x=-2$ נקודה קריטית.
3. $y$ עולה ב-$(-2,-1)$ ויורדת ב-$(-\infty,-2)$ וב-$(-1,\infty)$; $x=-2$ נקודת מינימום, $y(-2)=0$.
**III.**
1. $y''=\frac{-2(x+1)^3+2(x+2)3(x+1)^2}{(x+1)^6}=\frac{4x+10}{(x+1)^4}$.
2. $x=-\frac{5}{2}$.
3. $y''>0$ עבור $x>-\frac{5}{2}$, $y''<0$ עבור $x<-\frac{5}{2}$. נקודת פיתול: $\left(-\frac{5}{2},\frac{1}{9}\right)$.
![שרטוט הגרף של y = ((x+2)/(x+1))^2 עם האסימפטוטות x=-1 ו-y=1 והמינימום ב-x=-2](images/exams/21B-B-Q1-graph.png)
"""

SOL3A = r"""
**הפתרון הרשמי עם תיקון:** בפתרון הרשמי נכתב שהשורש נמצא בקטע $(-1,0)$ ושהערך $f(1)\approx-3.99$. אך $f(0)=5>0$, ו-$f(-1)\approx4.04>0$ (אין שינוי סימן בקטע $[-1,0]$), ואילו $f(1)\approx-3.96<0$. לכן שינוי הסימן הוא בקטע $(0,1)$ והשורש $c$ נמצא ב-$(0,1)$. להלן הפתרון הרשמי עם התיקון הזה.
$f(x)=2\sin^2(3x)+5\sqrt[3]{1-x^2}-4x^5$
Continues function for all $x$.
$f(0)=5,\quad f(1)=2\sin^2(3)-4\approx-3.96<0$
Therefore there exist $c\in(0,1)$ such that $f(c)=0$
$c$ is a root of $f(x)$.
"""

SOL3B = r"""
$$\int\frac{dx}{x(\ln x-1)(\ln x-3)}=\left[t=\ln x,\quad dt=\frac{dx}{x}\right]=\int\frac{dt}{(t-1)(t-3)}$$
$$\frac{1}{(t-1)(t-3)}=\frac{0.5}{t-3}-\frac{0.5}{t-1}$$
$$\int\frac{dt}{(t-3)(t-1)}=\int\left(\frac{0.5}{t-3}-\frac{0.5}{t-1}\right)dt=0.5\ln|t-3|-0.5\ln|t-1|=0.5\ln\left|\frac{t-3}{t-1}\right|$$
$$\int\frac{dx}{x(\ln x-1)(\ln x-3)}=0.5\ln\left|\frac{\ln x-3}{\ln x-1}\right|+c$$
"""

SOL4A = r"""
$$\lim_{x\to0}\frac{\ln\cos x}{\ln\cos4x}=\left(\frac{0}{0}\right)=\lim_{x\to0}\frac{\frac{-\sin x}{\cos x}}{\frac{-4\sin4x}{\cos4x}}=\frac{1}{4}\lim_{x\to0}\frac{\tan x}{\tan4x}=\left(\frac{0}{0}\right)=$$
$$=\frac{1}{4}\lim_{x\to0}\frac{\frac{1}{\cos^2x}}{\frac{4}{\cos^24x}}=\frac{1}{4}\lim_{x\to0}\frac{\cos^24x}{4\cos^2x}=\frac{1}{16}$$
"""

SOL4B = r"""
![שרטוט התחום הכלוא בין y=x^2, y=-2x+8 וציר ה-x, והישר X=4 שסביבו מסובבים](images/exams/21B-B-Q4b-region.png)
$$V=V_1+V_2=2\pi\int_0^2(4-x)x^2dx+2\pi\int_2^4(4-x)(-2x+8)dx=$$
$$2\pi\int_0^2\left(4x^2-x^3\right)dx+4\pi\int_2^4(4-x)^2dx=$$
$$=2\pi\left(\frac{4x^3}{3}-\frac{x^4}{4}\right)\Big|_0^2+4\pi\frac{(4-x)^3}{-3}\Big|_2^4=$$
$$=2\pi\left(\frac{32}{3}-\frac{16}{4}\right)-\frac{4\pi}{3}(0-8)=\frac{40\pi}{3}+\frac{32\pi}{3}=\frac{72\pi}{3}=24\pi$$
"""

SOL5A = r"""
נמצא את הנקודות הקריטיות:
$$f(x)=\ln(1+x^2)\ \Rightarrow\ f'(x)=\frac{2x}{1+x^2}=0\ \Rightarrow\ x=0$$
נמצא את הערכים של הפונקציה בנקודה $x=0$ ובקצוות של הקטע:
$f(0)=0$ (min), $f(-1)=\ln2$, $f(\sqrt{e-1})=\ln(e)=1$ (max).
"""

SOL5B = r"""
בודקים את הרציפות של הפונקציה בנקודה $x=0$:
$$\lim_{x\to0^+}\left(x^2+b\sin2x+c\right)=c,\qquad \lim_{x\to0^-}\left(ae^x\right)=a$$
לכן $a=c$.
נמצא את הנגזרות החד-צדדיות בנקודה $x=0$:
$$f'_+(0)=\lim_{\Delta x\to0^+}\frac{(\Delta x)^2+b\sin2\Delta x+c-a}{\Delta x}=\lim_{\Delta x\to0^+}\frac{(\Delta x)^2+b\sin2\Delta x}{\Delta x}=$$
$$=\lim_{\Delta x\to0^+}\left(\Delta x+\frac{b\sin2\Delta x}{\Delta x}\right)=\lim_{\Delta x\to0^+}\left(\Delta x+\frac{2b\sin2\Delta x}{2\Delta x}\right)=2b$$
$$f'_-(0)=\lim_{\Delta x\to0^-}\frac{ae^{\Delta x}-a}{\Delta x}=a\cdot\lim_{\Delta x\to0^-}\frac{e^{\Delta x}-1}{\Delta x}=a\cdot1=a$$
לכן $a=2b=c$.
"""

# Held items: the file prints only the worked solution of Q6; the stem is not printed (Q2 is absent altogether).
SOL6A_HELD = r"""
ראשית, יש לבדוק שהנקודה אכן נמצאת על הגרף של הפונקציה ומקיימת את המשוואה הנתונה: $2x^4+3x^2y^3-2\sin y=2$.
לאחר מכן, נגזור את המשוואה ונקבל
$$8x^3+6xy^3+9x^2y^2\frac{dy}{dx}-2\cos y\,\frac{dy}{dx}=0$$
$$8x^3+6xy^3=\frac{dy}{dx}\left(2\cos y-9x^2y^2\right)$$
$$\frac{dy}{dx}=\frac{8x^3+6xy^3}{2\cos y-9x^2y^2}\ \Rightarrow\ \frac{dy}{dx}(1,0)=4$$
$$y-0=4(x-1)\ \Rightarrow\ y=4x-4$$
"""

SOL6B_HELD = r"""
נמצא קודם נקודות חיתוך בין הפרבולה לבין הקווים הישרים ואחר כך את השטח המבוקש.
$$\frac{3}{10}x+\frac{3}{2}=\sqrt{3x-6}\ \Rightarrow\ 3x+15=10\sqrt{3x-6}$$
$$9x^2-210x+825=0\ \Rightarrow\ x_1=5$$
$$-\frac{1}{5}x-2=-\sqrt{3x-6}\ \Rightarrow\ x+10=5\sqrt{3x-6}$$
$$x^2-55x+250=0\ \Rightarrow\ x_1=5$$
$$S_1=\int_0^5\left(\frac{3}{10}x+\frac{3}{2}-\left(-\frac{1}{5}x-2\right)\right)dx=\int_0^5\left(\frac{1}{2}x+\frac{7}{2}\right)dx=\left(\frac{x^2}{4}+\frac{7}{2}x\right)\Big|_0^5=23.75$$
$$S_2=2\int_2^5\sqrt{3x-6}\,dx=2\left(\frac{1}{3}\frac{(3x-6)^{\frac32}}{\frac32}\right)\Big|_2^5=\frac{4}{9}\left((3x-6)^{\frac32}\right)\Big|_2^5=12$$
$$S=S_1-S_2=11.75$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $y=\left(\frac{x+2}{x+1}\right)^2$ לפי הסעיפים הבאים: תחום הגדרה, תחומי עליה/ירידה, נקודות קיצון, "
      "קמירות ונקודות פיתול, אסימפטוטות, שרטטו את גרף הפונקציה.",
      SOL1, points=20),

    {"num": 2, "kind": "computation", "hold": "not-in-source"},

    Q(3, "proof", "continuity",
      r"הוכיחו שלמשוואה $2\sin^2(3x)+5\sqrt[3]{1-x^2}-4x^5=0$ קיים שורש ממשי.",
      SOL3A, part="א", solutionSource="solved", official=False),

    Q(3, "computation", "indefinite_integrals",
      r"מצאו את האינטגרל $\int\frac{dx}{x(\ln x-1)(\ln x-3)}$.",
      SOL3B, part="ב"),

    Q(4, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to0}\frac{\ln\cos x}{\ln\cos4x}$.",
      SOL4A, part="א"),

    Q(4, "computation", "definite_integrals",
      r"מצאו את נפח הגוף המתקבל כסיבוב התחום הכלוא בין הקווים $y=x^2,\ y=-2x+8$ ו-$y=0$ כאשר $x\ge0$ סביב הציר $X=4$. "
      "צייר את התחום המסובב והסבר את פעולותיך.",
      SOL4B, part="ב"),

    Q(5, "computation", "extrema_optimization",
      r"נתונה הפונקציה $f(x)=\ln\left(1+x^2\right)$. מצאו את הערך הגדול ביותר ואת הערך הקטן ביותר שלה בקטע $\left[-1,\sqrt{e-1}\right]$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "derivatives_tangents",
      r"נתונה הפונקציה $f(x)=\begin{cases}ae^x, & x\le0\\ x^2+b\sin2x+c, & x>0\end{cases}$, כאשר $a,b,c\in\mathbb{R}$ פרמטרים. "
      r"עבור אילו ערכים של $a,b,c\in\mathbb{R}$ הפונקציה $f(x)$ תהיה גזירה ב-$x=0$.",
      SOL5B, part="ב", points=10),

    {"num": 6, "part": "א", "kind": "computation", "topic": "derivatives_tangents",
     "hold": "stem-not-printed", "solution": SOL6A_HELD.strip("\n"), "solutionSource": "official-pdf"},

    {"num": 6, "part": "ב", "kind": "computation", "topic": "definite_integrals",
     "hold": "stem-not-printed", "solution": SOL6B_HELD.strip("\n"), "solutionSource": "official-pdf"},
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

# (Q2, Q6a and Q6b are held in this sitting: no rubric or steps are written for them.)

# ===== Q1: y = ((x+2)/(x+1))^2 =====
f1 = ((x + 2)/(x + 1))**2
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, -2*(x + 2)/(x + 1)**3) and same(f1pp, (4*x + 10)/(x + 1)**4)
assert sp.solve(sp.numer(sp.together(f1p)), x) == [-2] and sp.solve(sp.numer(sp.together(f1pp)), x) == [R(-5, 2)]
assert f1.subs(x, -2) == 0 and f1.subs(x, R(-5, 2)) == R(1, 9)
assert f1p.subs(x, -3) < 0 and f1p.subs(x, R(-3, 2)) > 0 and f1p.subs(x, 0) < 0
assert f1pp.subs(x, -3) < 0 and f1pp.subs(x, 0) > 0 and f1pp.subs(x, -2) > 0
assert sp.limit(f1, x, -1, '+') == sp.oo and sp.limit(f1, x, -1, '-') == sp.oo
assert sp.limit(f1, x, sp.oo) == 1 and sp.limit(f1, x, -sp.oo) == 1

add(1,
    rubric=rub(("תחום הגדרה $x\\neq-1$ ואסימפטוטה אנכית $x=-1$ ($+\\infty$ משני הצדדים)", 5),
               ("אסימפטוטה אופקית $y=1$ ב-$\\pm\\infty$ (שיפוע $0$)", 3),
               ("נגזרת $y'=\\frac{-2(x+2)}{(x+1)^3}$, תחומי עליה וירידה ומינימום ב-$x=-2$ שערכו $0$", 5),
               ("$y''=\\frac{4x+10}{(x+1)^4}$ ותחומי קמירות וקעירות", 4),
               ("נקודת פיתול $\\left(-\\frac52,\\frac19\\right)$", 2),
               ("שרטוט הגרף בהתאם לכל הנתונים", 1)),
    rubricSource="ai-draft",
    pitfalls=["לכלול את $x=-1$ בתחום ההגדרה או לסמן שם נקודת קיצון.",
              "לבלבל בין תחומי העליה והירידה: $y$ עולה ב-$(-2,-1)$ ויורדת ב-$(-\\infty,-2)$ וב-$(-1,\\infty)$.",
              "לטעות בערך בנקודת הפיתול: $y\\left(-\\frac52\\right)=\\left(\\frac{-1/2}{-3/2}\\right)^2=\\frac19$."],
    steps=[
        chx("מהי הנגזרת של $y=\\left(\\frac{x+2}{x+1}\\right)^2$?", -2*(x + 2)/(x + 1)**3,
            [2*(x + 2)/(x + 1)**3, -2*(x + 2)/(x + 1)**2, 2*(x + 2)/(x + 1)], lambda e: same(e, f1p),
            "כלל השרשרת: $2\\cdot\\frac{x+2}{x+1}\\cdot\\frac{-1}{(x+1)^2}=\\frac{-2(x+2)}{(x+1)^3}$ (אומת ב-sympy)."),
        ch("מה סוג הנקודה $x=-2$?", "מינימום מקומי (ומוחלט) שערכו $0$",
           ["מקסימום מקומי", "נקודת פיתול", "נקודה שאינה בתחום ההגדרה"],
           "$y'$ שלילית משמאל ל-$-2$ וחיובית מימין לה, ו-$y(-2)=0$ כשהפונקציה אי-שלילית (sympy)."),
        num("באיזה ערך $x$ משנה $y''$ סימן? (עשרוני)", R(-5, 2), "$4x+10=0$ נותן $x=-\\frac52=-2.5$."),
        num("מהו ערך הפונקציה בנקודת הפיתול? (עשרוני)", R(1, 9), "$y\\left(-\\frac52\\right)=\\frac19\\approx0.1111$ (sympy)."),
        ch("מהן האסימפטוטות של $y$?", "אנכית $x=-1$ ואופקית $y=1$",
           ["אנכית $x=-1$ בלבד", "אנכית $x=-1$ ומשופעת $y=x$", "אנכית $x=-2$ ואופקית $y=1$"],
           "$\\lim_{x\\to-1}y=+\\infty$ משני הצדדים ו-$\\lim_{x\\to\\pm\\infty}y=1$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q3a: a root of 2 sin^2(3x) + 5 cbrt(1-x^2) - 4x^5 =====
f3 = lambda v: 2*sp.sin(3*v)**2 + 5*sp.real_root(1 - v**2, 3) - 4*v**5
assert f3(0) == 5 and abs(float(sp.N(f3(1))) - (-3.96)) < 5e-3 and float(sp.N(f3(-1))) > 4
assert float(sp.N(f3(1))) < 0
lo, hi = 0.0, 1.0
for _ in range(60):
    mid = (lo + hi)/2
    if float(sp.N(f3(mid))) > 0:
        lo = mid
    else:
        hi = mid
assert 0 < lo < 1 and abs(float(sp.N(f3(lo)))) < 1e-6
L3 = ["הפונקציה $f(x)=2\\sin^2(3x)+5\\sqrt[3]{1-x^2}-4x^5$ רציפה לכל $x$.",
      "$f(0)=5>0$ ו-$f(1)=2\\sin^2 3-4\\approx-3.96<0$.",
      "לפי משפט ערך הביניים קיים $c\\in(0,1)$ עם $f(c)=0$, כלומר שורש ממשי."]
L3b = list(L3)
L3b[1] = "$f(0)=5>0$ ו-$f(1)=2\\sin^2 3-4\\approx3.96>0$."

add(3, "א",
    rubric=rub(("הגדרת $f$ ונימוק לרציפות על כל הממשיים", 2),
               ("חישוב $f(0)=5>0$", 2),
               ("חישוב $f(1)=2\\sin^23-4<0$", 3),
               ("הפעלת משפט ערך הביניים והמסקנה שקיים שורש ממשי", 3)),
    rubricSource="ai-draft",
    pitfalls=["לבחור קטע שבו אין החלפת סימן: $f(-1)\\approx4.04>0$ ו-$f(0)=5>0$, ולכן הקטע $[-1,0]$ אינו מתאים.",
              "לא לנמק רציפות לפני הפעלת משפט ערך הביניים (השורש $\\sqrt[3]{1-x^2}$ רציף לכל $x$).",
              "לחשב את $f(1)$ בלי לשים לב ש-$\\sin^23<1$ ולכן $2\\sin^23-4<0$."],
    steps=[
        num("מהו $f(0)$?", 5, "$2\\sin^20+5\\sqrt[3]{1}-0=5$."),
        num("מהו $f(1)=2\\sin^23-4$? (עשרוני)", f3(1), "$\\sin^23\\approx0.0199$ ולכן $f(1)\\approx-3.96$ (sympy).", tol=0.01),
        ch("באיזה קטע מבטיח משפט ערך הביניים שורש?", "$(0,1)$, כי $f(0)>0>f(1)$",
           ["$(-1,0)$, כי $f(-1)<0<f(0)$", "$(-1,1)$ בלבד, בלי בדיקת הסימנים", "$(1,2)$, כי $f(1)<0$"],
           "$f(-1)\\approx4.04>0$ ו-$f(0)=5>0$, ולכן אין החלפת סימן ב-$[-1,0]$. ההחלפה היא ב-$[0,1]$ (sympy)."),
        findbug("בנימוק שורה אחת שגויה. מצאו אותה.", L3b, 1,
                "$f(1)=2\\sin^23-4\\approx-3.96<0$, לא חיובי; בלי הסימן השלילי אין החלפת סימן."),
    ],
    stepsSource="ai-draft")

# ===== Q3b: int dx / (x (ln x - 1)(ln x - 3)) =====
g3b = 1/(x*(sp.log(x) - 1)*(sp.log(x) - 3))
F3b = sp.log(sp.Abs((sp.log(x) - 3)/(sp.log(x) - 1)))/2
Fpos = sp.log((sp.log(x) - 3)/(sp.log(x) - 1))/2
assert same(sp.diff(Fpos, x), g3b)
tq = sp.Symbol('tq', real=True)
pf_ok = lambda e: same(e, 1/((tq - 1)*(tq - 3)))
pf_good = R(1, 2)/(tq - 3) - R(1, 2)/(tq - 1)
assert pf_ok(pf_good)
F3w = [sp.log((sp.log(x) - 3)*(sp.log(x) - 1))/2, sp.log((sp.log(x) - 3)/(sp.log(x) - 1)), sp.log((sp.log(x) - 1)/(sp.log(x) - 3))/2]

add(3, "ב",
    rubric=rub(("הצבה $t=\\ln x$ עם $dt=\\frac{dx}{x}$", 3),
               ("פירוק לשברים חלקיים $\\frac{0.5}{t-3}-\\frac{0.5}{t-1}$", 3),
               ("אינטגרציה לוגריתמית", 2),
               ("חזרה ל-$x$: $0.5\\ln\\left|\\frac{\\ln x-3}{\\ln x-1}\\right|+c$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח את $\\frac{dx}{x}$ ולא להבחין שהוא $dt$.",
              "טעות בסימן הפירוק: $\\frac{1}{(t-1)(t-3)}=\\frac{0.5}{t-3}-\\frac{0.5}{t-1}$ ולא עם הסימנים ההפוכים.",
              "לשכוח ערכים מוחלטים בתוך הלוגריתם."],
    steps=[
        ch("איזו הצבה מתאימה לאינטגרל $\\int\\frac{dx}{x(\\ln x-1)(\\ln x-3)}$?", "$t=\\ln x$", ["$t=x$", "$t=e^x$", "$t=\\frac1x$"],
           "הגורם $\\frac{dx}{x}$ מופיע באינטגרל ושאר הביטוי תלוי ב-$\\ln x$ בלבד, ולכן $t=\\ln x$."),
        chx("מהו הפירוק לשברים חלקיים של $\\frac{1}{(t-1)(t-3)}$?", pf_good,
            [R(1, 2)/(tq - 1) - R(1, 2)/(tq - 3), 1/(tq - 3) - 1/(tq - 1), R(1, 2)/(tq - 3) + R(1, 2)/(tq - 1)], pf_ok,
            "$\\frac{A}{t-3}+\\frac{B}{t-1}$ עם $A=\\frac12$, $B=-\\frac12$ (אומת ב-sympy)."),
        chx("מהו האינטגרל? (עבור התחום $\\ln x>3$, בלי הקבוע)", Fpos, F3w, lambda e: same(sp.diff(e, x), g3b),
            "$\\frac12\\ln|t-3|-\\frac12\\ln|t-1|=\\frac12\\ln\\left|\\frac{t-3}{t-1}\\right|$. הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-draft")

# ===== Q4a: lim ln cos x / ln cos 4x =====
assert sp.limit(sp.log(sp.cos(x))/sp.log(sp.cos(4*x)), x, 0) == R(1, 16)
assert sp.limit(sp.tan(x)/sp.tan(4*x), x, 0) == R(1, 4)
assert same(sp.diff(sp.log(sp.cos(x)), x), -sp.tan(x))
assert sp.limit(sp.log(sp.cos(x)), x, 0) == 0 and sp.limit(sp.log(sp.cos(4*x)), x, 0) == 0

add(4, "א",
    rubric=rub(("זיהוי $\\frac00$ והפעלת לופיטל", 3),
               ("נגזרות $\\left(\\ln\\cos x\\right)'=-\\tan x$ ו-$\\left(\\ln\\cos4x\\right)'=-4\\tan4x$", 2),
               ("שוב $\\frac00$ והפעלת לופיטל שנייה על $\\frac{\\tan x}{\\tan4x}$", 3),
               ("ערך הגבול $\\frac1{16}$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח את גורם השרשרת $4$ בנגזרת של $\\ln\\cos4x$.",
              "לעצור אחרי לופיטל אחד: $\\frac{\\tan x}{\\tan4x}$ עדיין $\\frac00$.",
              "לשכוח את הגורם $\\frac14$ שמוצא החוצה: הגבול הוא $\\frac14\\cdot\\frac14$."],
    steps=[
        ch("מה סוג הצורה הלא מסוימת של $\\frac{\\ln\\cos x}{\\ln\\cos4x}$ כאשר $x\\to0$?", "$\\frac00$",
           ["$\\frac\\infty\\infty$", "$1^{\\infty}$", "$0\\cdot\\infty$"],
           "$\\cos x\\to1$ ולכן $\\ln\\cos x\\to0$, וכנ\"ל במכנה (אומת ב-sympy)."),
        num("מהו $\\lim_{x\\to0}\\frac{\\tan x}{\\tan4x}$? (עשרוני)", R(1, 4), "לופיטל: $\\frac{1/\\cos^2x}{4/\\cos^24x}\\to\\frac14$ (sympy)."),
        num("מהו ערך הגבול המבוקש? (עשרוני)", R(1, 16), "$\\frac14\\cdot\\frac14=\\frac1{16}=0.0625$ (sympy).", tol=0.0005),
    ],
    stepsSource="ai-draft")

# ===== Q4b: shells about x = 4 =====
V1 = 2*sp.pi*sp.integrate((4 - x)*x**2, (x, 0, 2))
V2 = 2*sp.pi*sp.integrate((4 - x)*(-2*x + 8), (x, 2, 4))
V4 = V1 + V2
assert sp.solve(sp.Eq(x**2, -2*x + 8), x) == [-4, 2] or sorted(sp.solve(sp.Eq(x**2, -2*x + 8), x)) == [-4, 2]
assert V1 == 2*sp.pi*R(20, 3) and V2 == R(32, 3)*sp.pi and V4 == 24*sp.pi
assert sp.solve(sp.Eq(-2*x + 8, 0), x) == [4]
# cross-check by washers in y (inner radius 4-sqrt(y), outer radius 4-(8-y)/2 = y/2)
yw = sp.Symbol('yw', positive=True)
Vwash = sp.pi*sp.integrate((4 - sp.sqrt(yw))**2 - (yw/2)**2, (yw, 0, 4))
assert sp.simplify(Vwash - V4) == 0

add(4, "ב",
    rubric=rub(("נקודת החיתוך של $y=x^2$ עם $y=-2x+8$: $x=2$, וחיתוך הישר עם ציר $x$ ב-$x=4$", 2),
               ("בחירת קונכיות וקביעת רדיוס $4-x$", 3),
               ("חישוב $V_1=\\frac{40\\pi}{3}$ עבור $0\\le x\\le2$", 2),
               ("חישוב $V_2=\\frac{32\\pi}{3}$ עבור $2\\le x\\le4$", 2),
               ("סכום: $V=24\\pi$", 1)),
    rubricSource="ai-draft",
    pitfalls=["לקחת רדיוס $x$ במקום $4-x$: הסיבוב הוא סביב הישר $X=4$ ולא סביב ציר ה-$y$.",
              "לשכוח לפצל לשני קטעים: הגבול העליון משתנה ב-$x=2$ מהפרבולה לישר.",
              "לשכוח את הגורם $2\\pi$ של הקונכייה."],
    steps=[
        num("מהו ערך $x$ החיובי שבו הפרבולה פוגשת את הישר $y=-2x+8$?", 2, "$x^2+2x-8=0$ נותן $x=2$ או $x=-4$; רק $x=2\\ge0$ (sympy)."),
        ch("מהו רדיוס הקונכייה במרחק $x$ מהציר $y$ כשמסובבים סביב $X=4$?", "$4-x$",
           ["$x$", "$x-4$ (שלילי בתחום)", "$4+x$"],
           "המרחק של הנקודה $x$ מהישר $X=4$ הוא $4-x\\ge0$ בתחום $0\\le x\\le4$."),
        num("מהו $\\frac{V_1}{\\pi}$ עבור $V_1=2\\pi\\int_0^2(4-x)x^2dx$? (עשרוני)", R(40, 3), "$2\\left(\\frac{32}{3}-4\\right)=\\frac{40}{3}\\approx13.333$ (sympy)."),
        num("מהו $\\frac{V_2}{\\pi}$ עבור $V_2=2\\pi\\int_2^4(4-x)(-2x+8)dx$? (עשרוני)", R(32, 3), "$4\\int_2^4(4-x)^2dx=4\\cdot\\frac83=\\frac{32}{3}\\approx10.667$ (sympy)."),
        num("מהו נפח הגוף? (עשרוני)", V4, "$V=\\frac{40\\pi}{3}+\\frac{32\\pi}{3}=24\\pi\\approx75.398$ (sympy, ובדיקה בשיטת הדסקיות).", tol=0.01),
    ],
    stepsSource="ai-draft")

# ===== Q5a: extrema of ln(1+x^2) on [-1, sqrt(e-1)] =====
f5 = sp.log(1 + x**2)
assert sp.solve(sp.diff(f5, x), x) == [0]
assert (f5.subs(x, 0), f5.subs(x, -1), sp.simplify(f5.subs(x, sp.sqrt(sp.E - 1)))) == (0, sp.log(2), 1)
assert sp.log(2) < 1

add(5, "א",
    rubric=rub(("נגזרת $f'(x)=\\frac{2x}{1+x^2}$ והנקודה הקריטית $x=0$", 3),
               ("ערכי הפונקציה: $f(0)=0$, $f(-1)=\\ln2$", 2),
               ("$f\\left(\\sqrt{e-1}\\right)=\\ln e=1$", 3),
               ("מסקנה: מקסימום $1$ ומינימום $0$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח לבדוק את שני הקצוות של הקטע.",
              "להסיק שהמקסימום הוא $\\ln2$ (הקצה השמאלי) בלי לחשב את הקצה הימני: $\\ln2\\approx0.693<1$.",
              "לחשב $f\\left(\\sqrt{e-1}\\right)=\\ln\\left(1+(e-1)\\right)=\\ln e=1$ בצורה שגויה."],
    steps=[
        num("מהו ערך $x$ שבו $f'(x)=0$?", 0, "$\\frac{2x}{1+x^2}=0$ נותן $x=0$."),
        num("מהו $f(-1)=\\ln2$? (עשרוני)", sp.log(2), "$\\ln2\\approx0.6931$."),
        num("מהו $f\\left(\\sqrt{e-1}\\right)$?", 1, "$\\ln\\left(1+e-1\\right)=\\ln e=1$ (sympy)."),
        ch("מהם המינימום והמקסימום המוחלטים בקטע?", "מינימום $0$ ב-$x=0$ ומקסימום $1$ ב-$x=\\sqrt{e-1}$",
           ["מינימום $0$ ומקסימום $\\ln2$", "מינימום $\\ln2$ ומקסימום $1$", "מינימום $0$ ומקסימום $e$"],
           "הערכים הם $0,\\,0.693,\\,1$; הקטן ביותר $0$ והגדול ביותר $1$."),
    ],
    stepsSource="ai-draft")

# ===== Q5b: differentiability with parameters =====
def diffable(av, bv, cv):
    return av == cv and av == 2*bv


assert diffable(2, 1, 2) and not diffable(1, 1, 1) and not diffable(2, 1, 1) and not diffable(1, 2, 1)
# sympy cross-check of the one-sided derivatives: right = 2b, left = a
bs, as_ = sp.symbols('bs as_')
assert sp.diff(x**2 + bs*sp.sin(2*x), x).subs(x, 0) == 2*bs and sp.diff(as_*sp.exp(x), x).subs(x, 0) == as_

add(5, "ב",
    rubric=rub(("דרישת רציפות ב-$x=0$: $a=c$", 3),
               ("נגזרת ימנית $f'_+(0)=2b$ (עם $\\frac{\\sin2\\Delta x}{\\Delta x}\\to2$)", 3),
               ("נגזרת שמאלית $f'_-(0)=a$", 2),
               ("השוואה: $a=2b=c$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לבדוק רק את הנגזרות החד-צדדיות ולשכוח את דרישת הרציפות $a=c$.",
              "לשכוח את הגורם $2$ בגבול $\\lim\\frac{\\sin2\\Delta x}{\\Delta x}=2$.",
              "לטעות בנגזרת השמאלית: $\\lim\\frac{ae^{\\Delta x}-a}{\\Delta x}=a$."],
    steps=[
        ch("מה תנאי הרציפות ב-$x=0$?", "$a=c$", ["$a=b$", "$c=0$", "$a=2b$"],
           "הגבול משמאל $a\\cdot e^0=a$ והגבול מימין $0+b\\sin0+c=c$, לכן $a=c$."),
        num("מהי הנגזרת הימנית $f'_+(0)$ עבור $b=3$?", 6, "$\\lim\\left(\\Delta x+\\frac{b\\sin2\\Delta x}{\\Delta x}\\right)=2b=6$ (sympy)."),
        num("מהי הנגזרת השמאלית $f'_-(0)$ עבור $a=5$?", 5, "$a\\cdot\\lim\\frac{e^{\\Delta x}-1}{\\Delta x}=a=5$."),
        ch("אילו תנאים על $a,b,c$ מבטיחים גזירות ב-$x=0$?", "$a=2b=c$",
           ["$a=b=c$", "$a=c$ בלבד", "$a=2b$ בלבד"],
           "דרושות רציפות ($a=c$) ושוויון נגזרות חד-צדדיות ($a=2b$). למשל $(a,b,c)=(1,1,1)$ רציפה אבל $f'_-=1\\neq2=f'_+$ (נבדק)."),
    ],
    stepsSource="ai-draft")


exam = {
    "examCode": "21B-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"א, מועד ב'",
    "year": 2021,
    "examDate": "",
    "sourceFile": "calculus-1/21B-B full solutions.pdf",
    "solutionFile": "calculus-1/21B-B full solutions.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

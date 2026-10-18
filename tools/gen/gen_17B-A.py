# -*- coding: utf-8 -*-
"""Generator for tools/raw/17B-A.json -- calculus-1 (20151), semester A 2017, moed B (06/03/2017).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_17B-A.py

Source: sitting 17B-A. Exam: 2 typed pages. Solution: 5 handwritten pages, author not stated (labelled
"student-solution", official:false, confidence med; it needs the refuter pass). The Hebrew connecting words of the
handwritten pages are only partly legible, so the prose is a reconstruction of the written mathematics, and every
formula is checked (tools/verify/17B-A/check.py, sympy + numeric).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (Q2 one part; Q3-Q6 a/b parts, 10% each).

Transcription notes
- Q1/Q3b/Q4b: the handwritten sketches are cropped as figures inside the solutions (no names on them).
- Q2: the handwritten difference a(n+1)-a(n) has the denominator written "2-a_n"; it must be 2+a_n (the numerator
  3-a_n^2 is right, and the sign conclusion is unchanged). Silent, intermediate; logged in docs/ASK_ADIR.md.
- Q3b: the handwritten V2 line reads "9pi * integral" where it must be "2pi * integral" (the value 77pi/5 is right).
  Silent, intermediate; logged.
- Q4a: the handwritten range "1<x<X" for the Lagrange point is c, written as c.
- Q5a: FINAL-ANSWER error in the handwritten solution: f(1/4) is written 17/2 (it is 1/2+16 = 33/2), f(100) is
  written 52/5 = "52/2" and the maximum is declared at x=100. Correct values f(1/4)=33/2, f(4)=3, f(100)=251/25, so
  the maximum is 33/2 at x=1/4 and the minimum 3 at x=4. Shipped corrected with the
  "הפתרון שבמקור (לא רשמי) עם תיקון" label (the key is not official), solutionSource solved, official:false (sympy + grid check).

Checks: tools/verify/17B-A/check.py. No code in this sitting.
Blind re-check (solver, 2026-10-18): tools/verify/17B-A/blind_recheck.py re-derives every final answer
independently (sympy); all agree with the shipped answers (the labeled fix included), so confidence is high.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "17B-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "student-solution", "official": False, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**תחום ההגדרה:** $D(f)=\{x\in\mathbb R,\ x\neq1\}$. חיתוך עם הצירים: $(2,0)$ ו-$(0,4)$.
**אסימפטוטה אנכית** $x=1$: $\lim_{x\to1^+}f(x)=\lim_{x\to1^-}f(x)=+\infty$.
**אסימפטוטה משופעת / אופקית:**
$$a=\lim_{x\to\infty}\frac{f(x)}{x}=\lim_{x\to\infty}\frac{(x-2)^2}{x(x-1)^2}=0,\qquad b=\lim_{x\to\infty}f(x)=\lim_{x\to\infty}\frac{(x-2)^2}{(x-1)^2}=1$$
לכן $y=1$ היא אסימפטוטה אופקית (משני הצדדים, $\pm\infty$).
**עלייה וירידה:**
$$f'(x)=2\cdot\frac{x-2}{x-1}\cdot\frac{x-1-(x-2)}{(x-1)^2}=2\cdot\frac{x-2}{(x-1)^3}$$
טבלת סימנים של $f'$: חיובית ב-$x<1$ (עולה), שלילית ב-$1<x<2$ (יורדת), חיובית ב-$x>2$ (עולה). מינימום ב-$x=2$, $f(2)=0$.
**קמירות ונקודות פיתול:**
$$f''(x)=2\cdot\frac{(x-1)^3-(x-2)\cdot3(x-1)^2}{(x-1)^6}=2\cdot\frac{x-1-3(x-2)}{(x-1)^4}=2\cdot\frac{-2x+5}{(x-1)^4}$$
טבלת סימנים של $f''$: חיובית ב-$x<1$ (קמורה, $\cup$), חיובית ב-$1<x<\frac52$ (קמורה, $\cup$), שלילית ב-$x>\frac52$ (קעורה, $\cap$). נקודת פיתול ב-$x=\frac52$, $f\left(\frac52\right)=\frac19$.
**שרטוט:**
![סקיצה של הגרף של y = ((x−2)/(x−1))² עם האסימפטוטה האנכית x=1, האסימפטוטה האופקית y=1 והמינימום ב-x=2](images/exams/17B-A-Q1-sketch.png)
"""

SOL2 = r"""
$a_1=5,\quad a_{n+1}=2-\frac{1}{2+a_n}$. נחשב: $a_2=2-\frac17=\frac{13}{7}$, $a_3=2-\frac{1}{2+\frac{13}{7}}=2-\frac{7}{27}=\frac{47}{27}$.
**חסימות:** נראה באינדוקציה שמתקיים $\sqrt3\le a_n\le2$ לכל $n\ge2$. עבור $n=2$: $\sqrt3\le a_2\le2$. אם $\sqrt3\le a_k\le2$ אז
$$2+\sqrt3\le2+a_k\le4\ \Rightarrow\ \frac14\le\frac{1}{2+a_k}\le\frac{1}{2+\sqrt3}=2-\sqrt3$$
$$2-(2-\sqrt3)\le2-\frac{1}{2+a_k}\le2-\frac14\ \Rightarrow\ \sqrt3\le a_{k+1}\le2$$
**מונוטוניות:** נראה שהסדרה יורדת.
$$a_{n+1}-a_n=2-a_n-\frac{1}{2+a_n}=\frac{(2-a_n)(2+a_n)-1}{2+a_n}=\frac{3-a_n^2}{2+a_n}$$
מכיוון ש-$\sqrt3\le a_n\le2$ מתקיים $a_{n+1}-a_n\le0$.
לכן הסדרה יורדת וחסומה מלרע, ולכן מתכנסת (מ-$n=2$ ואילך, ובהכרח גם כולה). נסמן $\lim_{n\to\infty}a_n=L$:
$$L=2-\frac{1}{2+L}\ \Leftrightarrow\ L=\frac{4+2L-1}{2+L}\ \Leftrightarrow\ L^2=3\ \Leftrightarrow\ L_1=\sqrt3,\quad L_2=-\sqrt3$$
מכיוון ש-$\sqrt3\le a_n$ לא מתקבל $L_2$, ולכן $\lim_{n\to\infty}a_n=\sqrt3$.
"""

SOL3A = r"""
$$\lim_{x\to+\infty}\left(x-\ln\left(1+2e^x\right)\right)=\{\infty-\infty\}=\lim_{x\to+\infty}\left[\ln e^x-\ln\left(1+2e^x\right)\right]=\lim_{x\to+\infty}\ln\frac{e^x}{1+2e^x}=\ln\lim_{x\to+\infty}\frac{e^x}{1+2e^x}=\ln\frac12=-\ln2$$
"""

SOL3B = r"""
$y=1+x^3$, $x=1$, $y=9$: $9=1+x^3\Rightarrow x^3=8\Rightarrow x=2$.
![סקיצה של התחום בין y = 1 + x³, x = 1 ו-y = 9 וסיבובו סביב ציר ה-y](images/exams/17B-A-Q3b-sketch.png)
$V=V_1-V_2$:
$$V_1=2\pi\int_1^2x\cdot9\,dx=9\pi x^2\Big|_1^2=27\pi$$
$$V_2=2\pi\int_1^2x\left(1+x^3\right)dx=2\pi\int_1^2\left(x+x^4\right)dx=2\pi\left(\frac{x^2}{2}+\frac{x^5}{5}\right)\Big|_1^2=2\pi\left(2+\frac{32}{5}-\frac12-\frac15\right)=2\pi\cdot\frac{20+64-5-2}{10}=\frac{77\pi}{5}$$
$$V=27\pi-\frac{77\pi}{5}=\frac{58\pi}{5}$$
"""

SOL4A = r"""
נגדיר $f(x)=\ln x$ על $[1,x]$. הפונקציה $f$ רציפה ב-$[1,x]$ וגזירה ב-$(1,x)$, $f'(x)=\frac1x$, ולכן לפי משפט לגרנז' $f(x)-f(1)=f'(c)(x-1)$ עבור $1<c<x$, כלומר
$$\ln x-\ln1=\frac1c(x-1),\qquad1<c<x$$
$$\ln x=\frac1c(x-1)\ \Rightarrow\ \frac{x-1}{x}<\ln x<x-1$$
(כי $\frac1x<\frac1c<1$.)
"""

SOL4B = r"""
$y=\sqrt x$, נקודה $(4,2)$. משוואת המשיק: $y-2=y'(4)(x-4)$, ומכאן $y-2=\frac{1}{2\sqrt4}(x-4)=\frac{x-4}{4}$, כלומר $x=4y-4$.
![סקיצה: הגרף של y = √x, המשיק בנקודה (4,2) והתחום הכלוא עם ציר ה-x](images/exams/17B-A-Q4b-sketch.png)
$$S=\int_0^2\left(y^2-(4y-4)\right)dy=\left(\frac{y^3}{3}-2y^2+4y\right)\Big|_0^2=\frac83-8+8=\frac83$$
"""

SOL5A = r"""
**הפתרון שבמקור (לא רשמי) עם תיקון:** בפתרון הכתוב ערכי הפונקציה בשני קצות הקטע מחושבים בטעות ($f\left(\frac14\right)$ נכתב $\frac{17}{2}$, $f(100)$ נכתב $\frac{52}{2}$) והמקסימום נקבע ב-$x=100$. הערכים הנכונים הם $f\left(\frac14\right)=\frac12+16=\frac{33}{2}$ ו-$f(100)=10+\frac{1}{25}=\frac{251}{25}$, ולכן המקסימום המוחלט הוא $\frac{33}{2}$ ב-$x=\frac14$. הערך $f(4)=3$ והמינימום המוחלט נכונים. התיקון נבדק (sympy).
$$f'(x)=\frac{1}{2\sqrt x}-\frac{4}{x^2}=\frac{x^{\frac32}-8}{2x^2}=0\ \Rightarrow\ x^{\frac32}=8\ \Rightarrow\ x=4$$
$$f\left(\tfrac14\right)=\frac12+16=\frac{33}{2},\qquad f(4)=2+1=3,\qquad f(100)=10+\frac{1}{25}=\frac{251}{25}$$
$$\max_{\left[\frac14,100\right]}f(x)=\frac{33}{2}=f\left(\tfrac14\right),\qquad\min_{\left[\frac14,100\right]}f(x)=3=f(4)$$
"""

SOL5B = r"""
$$\int\sin^5x\,dx=\left|\begin{matrix}t=\cos x\\dt=-\sin x\,dx\\\sin^4x=\left(1-\cos^2x\right)^2\end{matrix}\right|=-\int\left(1-t^2\right)^2dt=-\int\left(1-2t^2+t^4\right)dt=-t+\frac{2t^3}{3}-\frac{t^5}{5}+C=-\cos x+\frac23\cos^3x-\frac15\cos^5x+C$$
"""

SOL6A = r"""
$$\lim_{x\to0^-}f(x)=\lim_{x\to0^-}\left(\frac{e^{ax}-1}{x}\right)^2=\lim_{x\to0^-}\left(a\cdot\frac{e^{ax}-1}{ax}\right)^2=a^2$$
$$\lim_{x\to0^+}f(x)=\lim_{x\to0^+}\left(4+e^{-\frac{a^2}{x}}\right)=4$$
לכן $a^2=b=4$, כלומר הפונקציה רציפה אם ורק אם $b=4$ ו-$a=\pm2$.
"""

SOL6B = r"""
$$\int\frac{\ln(x+1)}{\sqrt{x+1}}\,dx=\left|\begin{matrix}u=\ln(x+1)&du=\frac{dx}{x+1}\\dv=\frac{dx}{\sqrt{x+1}}&v=2\sqrt{x+1}\end{matrix}\right|=2\sqrt{x+1}\ln(x+1)-2\int\frac{dx}{\sqrt{x+1}}=2\sqrt{x+1}\ln(x+1)-4\sqrt{x+1}+C$$
"""

HEAD1 = (r"חקרו את הפונקציה הבאה $y=\left(\frac{x-2}{x-1}\right)^2$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, "
         "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.")

questions = [
    Q(1, "computation", "function_investigation", HEAD1, SOL1),

    Q(2, "proof", "sequences_limits",
      r"הוכיחו כי הסדרה $a_1=5,\ a_{n+1}=2-\frac{1}{2+a_n}$ מתכנסת וחשבו את הגבול שלה.",
      SOL2, points=20),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to+\infty}\left(x-\ln\left(1+2e^x\right)\right)$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום המישורי הכלוא בין הקווים $y=1+x^3,\ x=1,\ y=9$ סביב ציר ה-$y$.",
      SOL3B, part="ב", points=10),

    Q(4, "proof", "mean_value_theorems",
      r"הוכיחו כי $\frac{x-1}{x}<\ln x<x-1$ לכל $x>1$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"מצאו את השטח הכלוא בין: ציר ה-$x$, הגרף של $y=\sqrt x$ והמשיק שלו בנקודה $(4,2)$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "extrema_optimization",
      r"מצאו מינימום ומקסימום מוחלטים של הפונקציה $f(x)=\sqrt x+\frac4x$ בקטע $[0.25,100]$.",
      SOL5A, part="א", points=10,
      solutionSource="solved", official=False),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int\sin^5x\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "continuity",
      r"עבור אילו ערכים של $a,b$ תהיה הפונקציה "
      r"$f(x)=\begin{cases}x^{-2}\left(e^{ax}-1\right)^2,&x<0\\[1mm]b,&x=0\\[1mm]4+e^{-a^2/x},&x>0\end{cases}$ "
      r"רציפה בנקודה $x=0$?",
      SOL6A, part="א", points=10),

    Q(6, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int\frac{\ln(x+1)}{\sqrt{x+1}}\,dx$.",
      SOL6B, part="ב", points=10),
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

# ===== Q1: y = ((x-2)/(x-1))^2 =====
f1 = ((x - 2)/(x - 1))**2
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, 2*(x - 2)/(x - 1)**3) and same(f1pp, 2*(5 - 2*x)/(x - 1)**4)
assert sp.solve(sp.numer(sp.together(f1p)), x) == [2] and sp.solve(sp.numer(sp.together(f1pp)), x) == [R(5, 2)]
assert f1.subs(x, 2) == 0 and f1.subs(x, R(5, 2)) == R(1, 9)
assert f1p.subs(x, 0) > 0 and f1p.subs(x, R(3, 2)) < 0 and f1p.subs(x, 3) > 0
assert f1pp.subs(x, 2) > 0 and f1pp.subs(x, 3) < 0 and f1pp.subs(x, 0) > 0
assert sp.limit(f1, x, sp.oo) == 1 and sp.limit(f1, x, -sp.oo) == 1
assert sp.limit(f1, x, 1, '+') == sp.oo and sp.limit(f1, x, 1, '-') == sp.oo

add(1,
    rubric=rub(("תחום הגדרה $x\\neq1$, חיתוכים עם הצירים, אסימפטוטה אנכית $x=1$ ($+\\infty$ משני הצדדים)", 5),
               ("אסימפטוטה אופקית $y=1$ משני הכיוונים (ובדיקה שאין משופעת)", 3),
               ("נגזרת $f'(x)=\\frac{2(x-2)}{(x-1)^3}$, תחומי עליה וירידה ומינימום ב-$x=2$", 5),
               ("$f''(x)=\\frac{2(5-2x)}{(x-1)^4}$ ותחומי קמירות וקעירות", 4),
               ("נקודת פיתול $\\left(\\frac52,\\frac19\\right)$", 2),
               ("שרטוט הגרף בהתאם לכל הנתונים", 1)),
    rubricSource="ai-verified",
    pitfalls=["לכלול את $x=1$ בתחום ההגדרה או לסמן שם נקודת קיצון.",
              "לשכוח שהאסימפטוטה האופקית $y=1$ מתקבלת בשני הכיוונים $x\\to\\pm\\infty$.",
              "לטעון שגם $x=1$ היא נקודת פיתול רק כי $f''$ לא מוגדרת שם: נקודת הפיתול היחידה היא $x=\\frac52$, שם $f''$ משנה סימן."],
    steps=[
        chx("מהי הנגזרת של $y=\\left(\\frac{x-2}{x-1}\\right)^2$?", 2*(x - 2)/(x - 1)**3,
            [2*(x - 2)/(x - 1)**2, 2*(x - 2)/(x - 1), -2*(x - 2)/(x - 1)**3], lambda e: same(e, f1p),
            "כלל השרשרת: $2\\cdot\\frac{x-2}{x-1}\\cdot\\frac{1}{(x-1)^2}=\\frac{2(x-2)}{(x-1)^3}$ (אומת ב-sympy)."),
        ch("מה סוג הנקודה $x=2$?", "מינימום מקומי (ומוחלט) שערכו $0$",
           ["מקסימום מקומי", "נקודת פיתול", "נקודה שאינה קיצון"],
           "$f'$ חיובית אחרי $x=2$ ושלילית לפניה (בין $1$ ל-$2$), ו-$f(2)=0$, והפונקציה אי-שלילית (sympy)."),
        num("באיזה ערך $x$ משנה $f''$ סימן (נקודת הפיתול)? (עשרוני)", R(5, 2), "$f''=0$ כאשר $5-2x=0$, כלומר $x=\\frac52$."),
        num("מהו ערך הפונקציה בנקודת הפיתול? (עשרוני)", R(1, 9), "$f\\left(\\frac52\\right)=\\left(\\frac{1/2}{3/2}\\right)^2=\\frac19\\approx0.1111$."),
        ch("מהן האסימפטוטות של $y$?", "אנכית $x=1$ ואופקית $y=1$",
           ["אנכית $x=1$ בלבד", "אנכית $x=1$ ומשופעת $y=x$", "אנכית $x=2$ ואופקית $y=1$"],
           "$\\lim_{x\\to1}f=+\\infty$ משני הצדדים, ו-$\\lim_{x\\to\\pm\\infty}f=1$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q2: a_1 = 5, a_{n+1} = 2 - 1/(2+a_n) =====
sq = [R(5)]
for _ in range(6):
    sq.append(2 - 1/(2 + sq[-1]))
assert sq[1] == R(13, 7) and sq[2] == R(47, 27)
assert all(sq[i] > sq[i + 1] for i in range(len(sq) - 1)) and all(sp.sqrt(3) <= v <= 2 for v in sq[1:])
aa = sp.Symbol('aa', positive=True)
SYMNAMES[aa] = "a_n"
assert same(2 - 1/(2 + aa) - aa, (3 - aa**2)/(2 + aa))
L2 = sp.Symbol('L2', real=True)
assert sorted(sp.solve(sp.Eq(L2, 2 - 1/(2 + L2)), L2), key=float) == [-sp.sqrt(3), sp.sqrt(3)]
# the induction step: a in [sqrt3, 2] maps into [sqrt3, 2]
assert 2 - 1/(2 + sp.sqrt(3)) == sp.sqrt(3) or same(2 - 1/(2 + sp.sqrt(3)), sp.sqrt(3))
assert 2 - R(1, 4) < 2
P2 = ["נראה באינדוקציה ש-$\\sqrt3\\le a_n\\le2$ לכל $n\\ge2$.",
      "מכאן $a_{n+1}-a_n=\\frac{3-a_n^2}{2+a_n}\\le0$, כלומר הסדרה יורדת.",
      "סדרה יורדת וחסומה מלרע מתכנסת; נסמן את גבולה $L$.",
      "במעבר לגבול $L=2-\\frac{1}{2+L}$, כלומר $L^2=3$.",
      "מכיוון ש-$a_n\\ge\\sqrt3$ מתקבל $L=\\sqrt3$."]
P2b = list(P2)
P2b[1] = "מכאן $a_{n+1}-a_n=\\frac{a_n^2-3}{2+a_n}\\le0$, כלומר הסדרה יורדת."
assert same(sp.Integer(0) + (aa**2 - 3)/(2 + aa), -(2 - 1/(2 + aa) - aa))
assert ((sp.sqrt(3)**2 - 3)/(2 + sp.sqrt(3)) == 0) and ((2**2 - 3)/(2 + 2) > 0)  # wrong form is >= 0 on [sqrt3, 2]

add(2,
    rubric=rub(("חסימות באינדוקציה: $\\sqrt3\\le a_n\\le2$ לכל $n\\ge2$", 6),
               ("מונוטוניות: $a_{n+1}-a_n=\\frac{3-a_n^2}{2+a_n}\\le0$, הסדרה יורדת", 6),
               ("מסקנה: סדרה יורדת וחסומה מלרע מתכנסת", 2),
               ("משוואת הגבול $L^2=3$ ופסילת $-\\sqrt3$ לפי החסם, גבול $\\sqrt3$", 6)),
    rubricSource="ai-verified",
    pitfalls=["לטעון חסימות כבר מ-$n=1$: $a_1=5>2$, ולכן החסם מתחיל רק מ-$a_2$.",
              "לחשב את הגבול מהמשוואה בלי להוכיח התכנסות, או להשאיר את שני הפתרונות $\\pm\\sqrt3$ בלי לפסול את $-\\sqrt3$.",
              "לבדוק מונוטוניות לפי הדוגמאות $a_1>a_2>a_3$ בלבד, בלי להוכיח את הסימן של $a_{n+1}-a_n$ לכל $n$."],
    steps=[
        num("מהו $a_2$? (עשרוני)", sq[1], "$a_2=2-\\frac{1}{7}=\\frac{13}{7}\\approx1.8571$ (sympy)."),
        chx("מהו ההפרש $a_{n+1}-a_n$?", (3 - aa**2)/(2 + aa),
            [(aa**2 - 3)/(2 + aa), (3 - aa**2)/(2 - aa), (1 - aa**2)/(2 + aa)], lambda e: same(e, 2 - 1/(2 + aa) - aa),
            "$2-a_n-\\frac{1}{2+a_n}=\\frac{(2-a_n)(2+a_n)-1}{2+a_n}=\\frac{3-a_n^2}{2+a_n}$ (אומת ב-sympy)."),
        ch("מדוע ההפרש $a_{n+1}-a_n$ אי-חיובי?", "כי $a_n\\ge\\sqrt3$ ולכן $3-a_n^2\\le0$ והמכנה חיובי",
           ["כי $a_n\\le2$ ולכן $3-a_n^2\\ge0$", "כי $a_1>a_2$ בלבד", "כי הסדרה חסומה מלעיל"],
           "מהחסם התחתון $a_n\\ge\\sqrt3$ מקבלים $3-a_n^2\\le0$, והמכנה $2+a_n>0$. בדיקה של איבר אחד אינה מוכיחה לכל $n$."),
        order("סדרו את שלבי ההוכחה.", P2,
              "החסימות באה ראשונה כי המונוטוניות נשענת על $a_n\\ge\\sqrt3$; ההתכנסות נובעת משתיהן; ורק אחריה מחשבים את הגבול ופוסלים את $-\\sqrt3$."),
        findbug("בהוכחה שורה אחת שגויה. מצאו אותה.", P2b, 1,
                "ההפרש הוא $\\frac{3-a_n^2}{2+a_n}$ ולא $\\frac{a_n^2-3}{2+a_n}$; עם הסימן ההפוך האי-שוויון $\\le0$ אינו נובע מ-$a_n\\ge\\sqrt3$ (נבדק ב-sympy)."),
        num("מהו גבול הסדרה? (עשרוני)", sp.sqrt(3), "$L^2=3$ ו-$L\\ge\\sqrt3>0$ ולכן $L=\\sqrt3\\approx1.7321$."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: lim x - ln(1+2e^x) =====
lim3a = sp.limit(x - sp.log(1 + 2*sp.exp(x)), x, sp.oo)
assert lim3a == -sp.log(2) and sp.limit(sp.exp(x)/(1 + 2*sp.exp(x)), x, sp.oo) == R(1, 2)

add(3, "א",
    rubric=rub(("זיהוי הצורה $\\infty-\\infty$", 2),
               ("כתיבה $x=\\ln e^x$ ואיחוד ללוגריתם אחד $\\ln\\frac{e^x}{1+2e^x}$", 4),
               ("חישוב הגבול הפנימי $\\frac12$ (רציפות הלוגריתם)", 2),
               ("הערך הסופי $\\ln\\frac12=-\\ln2$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לטעון שהגבול הוא $0$ או $-\\infty$ כי \"$\\infty-\\infty$\". זו צורה לא מסוימת.",
              "לשכוח שאחרי האיחוד הגבול הפנימי הוא $\\frac12$ ולא $\\frac{1}{2e^x}$ או $1$."],
    steps=[
        ch("איך הפתרון הרשמי מתמודד עם הצורה $\\infty-\\infty$?", "כותב $x=\\ln e^x$ ומאחד לוגריתם אחד של מנה",
           ["כופל בצמוד", "מפעיל לופיטל ישירות על הפרש", "מציב $x=\\infty$ ישירות"],
           "$x-\\ln(1+2e^x)=\\ln\\frac{e^x}{1+2e^x}$. הצבה ישירה נותנת צורה לא מסוימת, ואין כאן שורשים לכפל בצמוד."),
        num("מהו $\\lim_{x\\to\\infty}\\frac{e^x}{1+2e^x}$? (עשרוני)", R(1, 2), "מחלקים ב-$e^x$: $\\frac{1}{e^{-x}+2}\\to\\frac12$ (sympy)."),
        num("מהו ערך הגבול המבוקש? (עשרוני)", lim3a, "$\\ln\\frac12=-\\ln2\\approx-0.6931$ (sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: shells, y = 1 + x^3, x = 1, y = 9 about the y-axis =====
V3 = sp.integrate(2*sp.pi*x*(9 - (1 + x**3)), (x, 1, 2))
assert same(V3, 58*sp.pi/5)
assert sp.integrate(2*sp.pi*x*9, (x, 1, 2)) == 27*sp.pi and same(sp.integrate(2*sp.pi*x*(1 + x**3), (x, 1, 2)), 77*sp.pi/5)
assert sp.solve(sp.Eq(1 + x**3, 9), x) == [2]
vok = lambda g: abs(float(sp.N(sp.integrate(g, (x, 1, 2)) - V3))) < 1e-9

add(3, "ב",
    rubric=rub(("נקודת החיתוך של $y=1+x^3$ עם $y=9$: $x=2$ (גבולות האינטגרציה $1$ ו-$2$)", 2),
               ("בחירת שיטת הקונכיות הגליליות ורדיוס $x$", 2),
               ("הצבת האינטגרל $2\\pi\\int_1^2x\\left(9-1-x^3\\right)dx$ (או הפרש $V_1-V_2$)", 3),
               ("חישוב ותשובה $V=\\frac{58\\pi}{5}$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לחבר את הנפחים $V_1+V_2$ במקום להפחית: התחום נמצא בין העקומה לישר $y=9$.",
              "לשכוח את הגורם $x$ (רדיוס הקונכייה) באינטגרנד.",
              "לקחת גבולות אינטגרציה $0$ עד $2$ במקום $1$ עד $2$ (הישר $x=1$ חוסם את התחום)."],
    steps=[
        num("מהו ערך $x$ שבו $y=1+x^3$ פוגש את $y=9$?", 2, "$x^3=8$ ולכן $x=2$."),
        chx("מהו האינטגרנד בשיטת הקונכיות (האינטגרציה על $x$ מ-$1$ עד $2$)?", 2*sp.pi*x*(9 - (1 + x**3)),
            [2*sp.pi*x*(9 + 1 + x**3), sp.pi*x**2*(9 - (1 + x**3)), 2*sp.pi*(9 - (1 + x**3))], vok,
            "רדיוס הקונכייה $x$, גובהה $9-(1+x^3)$ והיקפה $2\\pi x$. רק האינטגרנד הנכון נותן את $V$ (נבדק ב-sympy)."),
        num("מהו $V_1=2\\pi\\int_1^2x\\cdot9\\,dx$, מחולק ב-$\\pi$?", 27, "$9\\pi x^2\\Big|_1^2=27\\pi$, כלומר $27$ ב-$\\pi$ (sympy)."),
        num("מהו נפח הגוף? (עשרוני)", V3, "$V=27\\pi-\\frac{77\\pi}{5}=\\frac{58\\pi}{5}\\approx36.44$ (sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: (x-1)/x < ln x < x-1 =====
L4 = ["נגדיר $f(t)=\\ln t$ על הקטע $[1,x]$, כאשר $x>1$.",
      "הפונקציה רציפה ב-$[1,x]$ וגזירה ב-$(1,x)$ עם $f'(t)=\\frac1t$.",
      "לפי משפט לגרנז' קיים $c\\in(1,x)$ המקיים $\\ln x-\\ln1=\\frac1c(x-1)$.",
      "מכיוון ש-$1<c<x$ מתקיים $\\frac1x<\\frac1c<1$.",
      "לכן $\\frac{x-1}{x}<\\ln x<x-1$."]
L4b = list(L4)
L4b[3] = "מכיוון ש-$1<c<x$ מתקיים $1<\\frac1c<\\frac1x$."
cc, xx = sp.symbols('cc xx', positive=True)
assert all(sp.Rational(1, 3) < sp.Rational(1, 1) / v < 1 for v in (R(3, 2), 2))  # 1/c lies in (1/x, 1) for c in (1, x=3)
assert not (1 < 1/R(2) < 1/R(3))

add(4, "א",
    rubric=rub(("הגדרת $f(t)=\\ln t$ על $[1,x]$ ובדיקת רציפות וגזירות", 3),
               ("הפעלת משפט לגרנז': $\\ln x=\\frac{x-1}{c}$ עבור $c\\in(1,x)$", 3),
               ("חסימת $\\frac1c$ בין $\\frac1x$ ל-$1$", 2),
               ("הכפלה ב-$(x-1)>0$ ומסקנת אי-השוויון", 2)),
    rubricSource="ai-verified",
    pitfalls=["להפעיל את משפט לגרנז' על קטע $[0,x]$: $\\ln t$ לא מוגדרת ולא רציפה ב-$0$.",
              "להפוך את כיוון אי-השוויון כשעוברים ל-$\\frac1c$ (היפוך מתקבל ב-$c\\mapsto\\frac1c$).",
              "לבדוק את אי-השוויון בכמה ערכים של $x$ ולהסיק ממנו הוכחה."],
    steps=[
        ch("על איזה קטע מפעיל הפתרון הרשמי את משפט לגרנז' עבור $f(t)=\\ln t$?", "$[1,x]$",
           ["$[0,x]$", "$[-1,x]$", "$[x,2x]$"],
           "הפתרון משתמש ב-$\\ln1=0$ ולכן הקטע $[1,x]$. הפונקציה $\\ln t$ לא מוגדרת ב-$0$ ולכן אינה רציפה ב-$[0,x]$ או ב-$[-1,x]$, וב-$[x,2x]$ לא מתקבלת $\\ln x$."),
        order("סדרו את שלבי ההוכחה.", L4,
              "הגדרה, בדיקת התנאים, הפעלת משפט לגרנז', חסימת $\\frac1c$ ומסקנה. כל שלב מסתמך על קודמו."),
        findbug("בהוכחה שורה אחת שגויה. מצאו אותה.", L4b, 3,
                "מ-$1<c<x$ מקבלים (בהיפוך) $\\frac1x<\\frac1c<1$ ולא $1<\\frac1c<\\frac1x$; למשל $c=2$, $x=3$ נותן $\\frac12$ שאינו גדול מ-$1$."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: area between sqrt(x), its tangent at (4,2), and the x-axis =====
tang = 2 + (x - 4)*sp.diff(sp.sqrt(x), x).subs(x, 4)
assert same(tang, x/4 + 1) and sp.solve(sp.Eq(tang, 0), x) == [-4]
yy = sp.Symbol('yy', real=True)
SYMNAMES[yy] = "y"
S4 = sp.integrate(yy**2 - (4*yy - 4), (yy, 0, 2))
assert S4 == R(8, 3)
# cross-check in x: area under sqrt(x) on [0,4] minus the triangle under the tangent from -4 to 4... done via the y-integral above
assert sp.integrate(tang, (x, -4, 4)) - sp.integrate(sp.sqrt(x), (x, 0, 4)) == S4
sok = lambda g: sp.integrate(g, (yy, 0, 2)) == R(8, 3)
for w in (4*yy - 4 - yy**2, yy**2 - 4*yy, yy**2 - 4*yy - 4):
    assert not sok(w)

add(4, "ב",
    rubric=rub(("שיפוע המשיק $y'(4)=\\frac14$ ומשוואת המשיק $y=\\frac{x}{4}+1$ (או $x=4y-4$)", 3),
               ("זיהוי התחום וקביעת גבולות האינטגרציה (ב-$y$ מ-$0$ עד $2$)", 3),
               ("אינטגרל $\\int_0^2\\left(y^2-(4y-4)\\right)dy$ והפונקציה הקדומה", 2),
               ("ערך השטח $\\frac83$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחשב את השיפוע כ-$\\frac{1}{\\sqrt4}$ במקום $\\frac{1}{2\\sqrt4}$.",
              "להחסיר בסדר הפוך בין הגרף למשיק (אינטגרציה על $y$: הגרף $x=y^2$ מימין למשיק $x=4y-4$).",
              "לשכוח שהמשיק פוגש את ציר ה-$x$ ב-$x=-4$ ולא ב-$x=0$."],
    steps=[
        num("מהו שיפוע המשיק לגרף $y=\\sqrt x$ בנקודה $(4,2)$? (עשרוני)", R(1, 4), "$y'(4)=\\frac{1}{2\\sqrt4}=\\frac14$."),
        num("באיזה ערך $x$ פוגש המשיק את ציר ה-$x$?", -4, "המשיק $y=\\frac{x}{4}+1$ מתאפס ב-$x=-4$ (sympy)."),
        chx("איזה אינטגרנד מחשב את השטח כאשר מבצעים אינטגרציה על $y$ מ-$0$ עד $2$?", yy**2 - (4*yy - 4),
            [4*yy - 4 - yy**2, yy**2 - 4*yy, yy**2 - 4*yy - 4], sok,
            "בגובה $y$ הגרף ב-$x=y^2$ והמשיק ב-$x=4y-4$, והגרף מימין. רק האינטגרנד הנכון נותן שטח חיובי $\\frac83$ (נבדק ב-sympy)."),
        num("מהו השטח? (עשרוני)", S4, "$\\left(\\frac{y^3}{3}-2y^2+4y\\right)\\Big|_0^2=\\frac83\\approx2.6667$ (sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q5a: absolute extrema of sqrt(x) + 4/x on [1/4, 100] =====
f5 = sp.sqrt(x) + 4/x
assert sp.solve(sp.Eq(sp.diff(f5, x), 0), x) == [4]
v5 = {k: f5.subs(x, k) for k in (R(1, 4), 4, 100)}
assert v5 == {R(1, 4): R(33, 2), 4: 3, 100: R(251, 25)}
assert max(v5.values()) == R(33, 2) and min(v5.values()) == 3

add(5, "א",
    rubric=rub(("נגזרת $f'(x)=\\frac{1}{2\\sqrt x}-\\frac{4}{x^2}$ ומציאת הנקודה הקריטית", 3),
               ("הנקודה $x=4$ בתוך הקטע; ערך $f(4)=3$", 2),
               ("ערכי הקצוות $f\\left(\\frac14\\right)=\\frac{33}{2}$ ו-$f(100)=\\frac{251}{25}$", 3),
               ("מסקנה: מקסימום מוחלט $\\frac{33}{2}$, מינימום מוחלט $3$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחשב את $f\\left(\\frac14\\right)$ כ-$\\frac{17}{2}$ ולקבוע בטעות שהמקסימום בקצה הימני: $f\\left(\\frac14\\right)=\\frac12+16=\\frac{33}{2}$.",
              "לשכוח לבדוק את קצות הקטע ולהסתפק בנקודה הקריטית.",
              "לפתור $x^{3/2}=8$ בטעות: $x=8^{2/3}=4$."],
    steps=[
        num("מהו ערך $x$ שבו $f'(x)=0$?", 4, "$\\frac{1}{2\\sqrt x}=\\frac{4}{x^2}$ נותן $x^{3/2}=8$ ולכן $x=4$ (sympy)."),
        num("מהו $f\\left(\\frac14\\right)$? (עשרוני)", v5[R(1, 4)], "$\\sqrt{\\frac14}+16=\\frac12+16=16.5$."),
        num("מהו $f(100)$? (עשרוני)", v5[100], "$10+\\frac{4}{100}=10.04$."),
        ch("מהם המינימום והמקסימום המוחלטים בקטע?", "מינימום $3$ ב-$x=4$ ומקסימום $\\frac{33}{2}$ ב-$x=\\frac14$",
           ["מינימום $3$ ומקסימום $\\frac{251}{25}$ ב-$x=100$", "מינימום $\\frac{251}{25}$ ומקסימום $\\frac{33}{2}$", "מינימום $3$ ומקסימום $3$"],
           "הערכים הם $\\frac{33}{2}=16.5$, $3$, $10.04$; הקטן ביותר $3$ והגדול ביותר $16.5$ (sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: int sin^5 =====
g5b = sp.sin(x)**5
F5b = -sp.cos(x) + R(2, 3)*sp.cos(x)**3 - sp.cos(x)**5/5
assert same(sp.diff(F5b, x), g5b)
t5 = sp.Symbol('t5', real=True)
SYMNAMES[t5] = "t"
assert same(sp.expand(-(1 - t5**2)**2), -1 + 2*t5**2 - t5**4)
F5w = [-sp.cos(x) + R(2, 3)*sp.cos(x)**3 + sp.cos(x)**5/5, sp.cos(x) - R(2, 3)*sp.cos(x)**3 + sp.cos(x)**5/5,
       -sp.cos(x) + sp.cos(x)**3 - sp.cos(x)**5/5]
tok = lambda e: same(sp.expand(e), sp.expand(-(1 - t5**2)**2))

add(5, "ב",
    rubric=rub(("זיהוי חזקה אי-זוגית והצבה $t=\\cos x$ עם $dt=-\\sin x\\,dx$", 3),
               ("$\\sin^4x=\\left(1-\\cos^2x\\right)^2$ והמעבר ל-$-\\int\\left(1-t^2\\right)^2dt$", 3),
               ("פתיחת הסוגריים ואינטגרציה איבר איבר", 2),
               ("חזרה ל-$x$ ותשובה עם $+C$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את סימן המינוס הנובע מ-$dt=-\\sin x\\,dx$.",
              "לכתוב $\\sin^4x=1-\\cos^4x$ במקום $\\left(1-\\cos^2x\\right)^2$.",
              "לשכוח לחזור למשתנה $x$ בסוף."],
    steps=[
        ch("איזו הצבה מתאימה לאינטגרל $\\int\\sin^5x\\,dx$?", "$t=\\cos x$, כי החזקה של הסינוס אי-זוגית",
           ["$t=\\sin x$", "$t=\\tan x$", "$t=\\tan\\frac x2$"],
           "מפרידים גורם $\\sin x\\,dx=-dt$ ושאר הסינוסים הופכים לפולינום ב-$\\cos x$. ההצבה $t=\\sin x$ אינה עובדת: אין גורם $\\cos x\\,dx$ באינטגרל."),
        chx("מהו האינטגרנד אחרי ההצבה $t=\\cos x$ (האינטגרל ב-$dt$)?", -(1 - t5**2)**2,
            [(1 - t5**2)**2, -(1 + t5**2)**2, -(1 - t5**2)], tok,
            "$\\sin^5x\\,dx=\\left(1-\\cos^2x\\right)^2\\sin x\\,dx=-(1-t^2)^2dt$ (אומת ב-sympy)."),
        chx("מהו האינטגרל? (בלי הקבוע)", F5b, F5w, lambda e: same(sp.diff(e, x), g5b),
            "$-t+\\frac{2t^3}{3}-\\frac{t^5}{5}$ עם $t=\\cos x$. הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: continuity with parameters a, b =====
def left6(av):
    return sp.limit((sp.exp(av*x) - 1)**2/x**2, x, 0, '-')
assert left6(3) == 9 and left6(-2) == 4 and left6(R(1, 2)) == R(1, 4)
assert sp.limit(4 + sp.exp(-3**2/x), x, 0, '+') == 4 and sp.limit(4 + sp.exp(-(-2)**2/x), x, 0, '+') == 4
assert sp.solve(sp.Eq(a**2, 4), a) in ([-2, 2], [2, -2])

add(6, "א",
    rubric=rub(("הגבול השמאלי $\\lim_{x\\to0^-}\\left(\\frac{e^{ax}-1}{x}\\right)^2=a^2$", 3),
               ("הגבול הימני $4+\\lim e^{-a^2/x}=4$", 3),
               ("תנאי הרציפות $a^2=b=4$", 2),
               ("פתרון: $b=4$ ו-$a=\\pm2$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את הפתרון $a=-2$: $a^2=4$ נותן שני ערכים.",
              "לטעות בגבול הימני: עבור $a\\neq0$ המעריך $-\\frac{a^2}{x}\\to-\\infty$ כאשר $x\\to0^+$, ולכן $e^{-a^2/x}\\to0$.",
              "לא להשוות את הגבולות גם לערך $f(0)=b$."],
    steps=[
        num("מהו הגבול השמאלי $\\lim_{x\\to0^-}f(x)$ עבור $a=3$?", left6(3), "$\\left(\\frac{e^{3x}-1}{x}\\right)^2\\to3^2=9$ (בכלל: $a^2$; sympy)."),
        num("מהו הגבול הימני $\\lim_{x\\to0^+}f(x)$ עבור $a=3$?", 4, "$e^{-9/x}\\to0$ כאשר $x\\to0^+$ ולכן הגבול $4$ (sympy)."),
        ch("אילו ערכים מבטיחים רציפות ב-$x=0$?", "$b=4$ ו-$a=2$ או $a=-2$",
           ["$b=4$ ו-$a=2$ בלבד", "$b=2$ ו-$a=2$", "$b=0$ ו-$a=0$"],
           "הרציפות דורשת $a^2=4=b$. עבור $a=0$ הגבול השמאלי $0$ והימני $5$, ולכן אין רציפות."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: int ln(x+1)/sqrt(x+1) =====
g6 = sp.log(x + 1)/sp.sqrt(x + 1)
F6 = 2*sp.sqrt(x + 1)*sp.log(x + 1) - 4*sp.sqrt(x + 1)
assert same(sp.diff(F6, x), g6)
F6w = [2*sp.sqrt(x + 1)*sp.log(x + 1) - 2*sp.sqrt(x + 1), 2*sp.sqrt(x + 1)*sp.log(x + 1) + 4*sp.sqrt(x + 1),
       sp.sqrt(x + 1)*sp.log(x + 1) - 4*sp.sqrt(x + 1)]

add(6, "ב",
    rubric=rub(("בחירת אינטגרציה בחלקים: $u=\\ln(x+1)$, $dv=\\frac{dx}{\\sqrt{x+1}}$", 3),
               ("$du=\\frac{dx}{x+1}$ ו-$v=2\\sqrt{x+1}$", 2),
               ("האינטגרל הנותר $-2\\int\\frac{dx}{\\sqrt{x+1}}=-4\\sqrt{x+1}$", 3),
               ("תשובה סופית עם $+C$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לבחור $u=\\frac{1}{\\sqrt{x+1}}$: אז האינטגרל הנותר מסובך יותר.",
              "לכתוב $v=\\sqrt{x+1}$ בלי הגורם $2$.",
              "לשכוח את האיבר השני $-4\\sqrt{x+1}$."],
    steps=[
        ch("איך בוחרים את $u$ ו-$dv$ באינטגרל $\\int\\frac{\\ln(x+1)}{\\sqrt{x+1}}dx$?",
           "$u=\\ln(x+1)$ ו-$dv=\\frac{dx}{\\sqrt{x+1}}$",
           ["$u=\\frac{1}{\\sqrt{x+1}}$ ו-$dv=\\ln(x+1)\\,dx$", "$u=\\sqrt{x+1}$ ו-$dv=\\ln(x+1)\\,dx$", "$u=x+1$ ו-$dv=\\frac{\\ln(x+1)}{\\sqrt{x+1}}dx$"],
           "בבחירת הפתרון הרשמי $du=\\frac{dx}{x+1}$ ו-$v=2\\sqrt{x+1}$, והאינטגרל הנותר פשוט. בבחירות האחרות צריך את הפונקציה הקדומה של $\\ln(x+1)$ או של הביטוי כולו, ואין בהן פישוט."),
        chx("מהו האינטגרל? (בלי הקבוע)", F6, F6w, lambda e: same(sp.diff(e, x), g6),
            "$2\\sqrt{x+1}\\ln(x+1)-2\\int\\frac{dx}{\\sqrt{x+1}}=2\\sqrt{x+1}\\ln(x+1)-4\\sqrt{x+1}$. הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "17B-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ז, מועד ב'",
    "year": 2017,
    "examDate": "06/03/2017",
    "sourceFile": "calculus-1/17B-A exam.pdf",
    "solutionFile": "calculus-1/17B-A handwritten-solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

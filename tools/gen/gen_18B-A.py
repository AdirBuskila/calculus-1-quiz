# -*- coding: utf-8 -*-
"""Generator for tools/raw/18B-A.json -- calculus-1 (20151), semester A 2018, moed B (05/02/2018).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_18B-A.py

Source: sitting 18B-A. Exam: 2 typed pages. Solution: 4 handwritten pages, author not stated (labelled
"student-solution", official:false, confidence med; it needs the refuter pass). The Hebrew connecting words of the
handwritten pages are only partly legible, so the prose is a reconstruction of the written mathematics and every
formula is checked (tools/verify/18B-A/check.py, sympy + numeric).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (10% per part; Q2 is one part).

Transcription notes
- Q1 sketch (handwritten p.1) is shipped as a figure inside the solution (a stray label was whited out).
- Q1: the handwritten one-sided limits at x=-sqrt(3) have the signs swapped (+oo / -oo); corrected (y is odd). Silent,
  intermediate; logged in docs/ASK_ADIR.md.
- Q3b: the handwritten words are barely legible; the solution is existence by IVT on [-pi/2, 0] (as written) plus the
  reasoning that there are infinitely many roots (written: sin x takes all values in [-1,1] while 0<e^x<1 for x<0).
  The "not unique" reading is checked numerically (>= 8 roots in [-30, 0.5]). Logged in ASK_ADIR.
- Q4b: FINAL-ANSWER ERROR in the handwritten solution (-pi/3 instead of -pi/6); shipped corrected with the
  "הפתרון שבמקור (לא רשמי) עם תיקון" label (the key is not official), solutionSource solved, official:false (sympy: pi^2/12 - pi/6 + (pi/6) ln 2).
- Q6b: the handwritten L'Hopital line drops the factor x (x -> 1, so harmless); the factor is restored. Silent, logged.

Checks: tools/verify/18B-A/check.py (sympy), 0 mismatches. No code in this sitting.
Blind re-check (solver, 2026-10-18): tools/verify/18B-A/blind_recheck.py re-derives every final answer
independently (sympy); all agree with the shipped answers (the labeled fix included), so confidence is high.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "18B-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "student-solution", "official": False, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**תחום ההגדרה:** $D=(-\infty,-\sqrt3)\cup(-\sqrt3,\sqrt3)\cup(\sqrt3,\infty)$.
**חיתוך עם הצירים:** $y=0\Leftrightarrow x=0$, ולכן החיתוך היחיד הוא $(0,0)$. הפונקציה אי-זוגית: $y(-x)=-y(x)$.
**אסימפטוטות אנכיות** $x=\pm\sqrt3$:
$$\lim_{x\to\sqrt3^+}y=+\infty,\quad\lim_{x\to\sqrt3^-}y=-\infty,\qquad\lim_{x\to-\sqrt3^+}y=+\infty,\quad\lim_{x\to-\sqrt3^-}y=-\infty$$
**אסימפטוטה משופעת** $y=kx+b$ ב-$\pm\infty$:
$$k=\lim_{x\to\pm\infty}\frac{y}{x}=\lim_{x\to\pm\infty}\frac{x^2}{x^2-3}=1,\qquad b=\lim_{x\to\pm\infty}(y-kx)=\lim_{x\to\pm\infty}\left(\frac{x^3}{x^2-3}-x\right)=\lim_{x\to\pm\infty}\frac{3x}{x^2-3}=0$$
לכן $y=x$ היא אסימפטוטה משופעת (משני הצדדים).
**מונוטוניות וקיצון:**
$$y'=\frac{3x^2\left(x^2-3\right)-x^3\cdot2x}{\left(x^2-3\right)^2}=\frac{x^4-9x^2}{\left(x^2-3\right)^2}=\frac{x^2(x-3)(x+3)}{\left(x^2-3\right)^2}$$
טבלת סימנים של $y'$: חיובית ב-$x<-3$ (עולה), שלילית ב-$-3<x<-\sqrt3$, ב-$-\sqrt3<x<\sqrt3$ (גם סביב $x=0$) וב-$\sqrt3<x<3$ (יורדת), חיובית ב-$x>3$ (עולה).
מקסימום מקומי ב-$x=-3$: $y(-3)=-\frac92$. מינימום מקומי ב-$x=3$: $y(3)=\frac92$.
**קמירות ונקודות פיתול:**
$$y''=\frac{\left(4x^3-18x\right)\left(x^2-3\right)^2-\left(x^4-9x^2\right)\cdot2\left(x^2-3\right)\cdot2x}{\left(x^2-3\right)^4}=\frac{\left(4x^3-18x\right)\left(x^2-3\right)-4x\left(x^4-9x^2\right)}{\left(x^2-3\right)^3}=$$
$$=\frac{4x^5-30x^3+54x-4x^5+36x^3}{\left(x^2-3\right)^3}=\frac{6x^3+54x}{\left(x^2-3\right)^3}=\frac{6x\left(x^2+9\right)}{\left(x-\sqrt3\right)^3\left(x+\sqrt3\right)^3}$$
טבלת סימנים של $y''$: שלילית ב-$x<-\sqrt3$ (קעורה), חיובית ב-$-\sqrt3<x<0$ (קמורה), שלילית ב-$0<x<\sqrt3$ (קעורה), חיובית ב-$x>\sqrt3$ (קמורה). נקודת הפיתול היחידה: $(0,0)$.
![שרטוט הגרף של y = x³/(x²−3) עם האסימפטוטות x=±√3 ו-y=x, המקסימום ב-x=−3 והמינימום ב-x=3](images/exams/18B-A-Q1-graph.png)
"""

SOL2 = r"""
נחשב: $a_1=2,\ a_2=\frac65,\ a_3=\frac{18}{17},\dots$ ונרשום $a_{n+1}=\frac{3}{2+\frac{1}{a_n}}$.
**חסימות:** נוכיח באינדוקציה ש-$1<a_n<2$ לכל $n\ge1$. עבור $n=1$ זה נכון. אם $1<a_n<2$ אז
$$\frac12<\frac{1}{a_n}<1\ \Rightarrow\ \frac52<2+\frac{1}{a_n}<3\ \Rightarrow\ \frac13<\frac{1}{2+\frac{1}{a_n}}<\frac25\ \Rightarrow\ 1<\frac{3}{2+\frac{1}{a_n}}<\frac65<2$$
ז"א $1<a_{n+1}<2$.
**מונוטוניות:** נראה שהסדרה יורדת:
$$\frac{a_{n+1}}{a_n}=\frac{3}{2a_n+1}$$
מ-$1<a_n<2$ נקבל $3<2a_n+1<5$, ולכן $\frac15<\frac{1}{2a_n+1}<\frac13$ ו-$\frac{a_{n+1}}{a_n}<1$.
הסדרה יורדת וחסומה מלמטה, ולכן מתכנסת. נסמן $\lim_{n\to\infty}a_n=L$ ונעבור לגבול בנוסחת הנסיגה $a_{n+1}=\frac{3a_n}{2a_n+1}$:
$$L=\frac{3L}{2L+1}\ \Rightarrow\ 2L^2+L=3L\ \Rightarrow\ L^2-L=0$$
מכיוון ש-$a_n>1$, לא ייתכן $L=0$, ולכן הגבול הוא $L=1$.
"""

SOL3A = r"""
$$f(x)=\int_{-3}^{x^3+1}t(t-1)^5\,dt$$
תחום ההגדרה: $(-\infty,\infty)$. לפי משפט היסוד של החשבון האינטגרלי וכלל השרשרת:
$$f'(x)=t(t-1)^5\Big|_{t=x^3+1}\cdot3x^2=\left(x^3+1\right)\left(x^3\right)^5\cdot3x^2=3x^{17}\left(x^3+1\right)$$
$$3x^{17}\left(x^3+1\right)=0\ \Rightarrow\ x_1=0,\quad x_2=-1$$
טבלת סימנים של $f'$: חיובית ב-$x<-1$ (עולה), שלילית ב-$-1<x<0$ (יורדת), חיובית ב-$x>0$ (עולה).
לכן ל-$f$ יש קיצון מקומי ב-$x=-1$ (מקסימום) וב-$x=0$ (מינימום).
"""

SOL3B = r"""
הפונקציה $f(x)=e^x+\sin x$ רציפה על כל הממשיים.
$f(0)=1>0$ ו-$f\left(-\frac\pi2\right)<0$ כי $\sin\left(-\frac\pi2\right)=-1$ ו-$e^{-\frac\pi2}<1$. לכן לפי משפט ערך הביניים יש פתרון בקטע $\left[-\frac\pi2,0\right]$, כלומר למשוואה $e^x+\sin x=0$ יש לפחות פתרון אחד.
**הפתרון אינו יחיד:** עבור $x\ge0$ מתקיים $e^x\ge1\ge-\sin x$, ושוויון בשני האי-שוויונות בו-זמנית אינו אפשרי (ב-$x=0$ מתקיים $\sin0=0$), ולכן $f(x)>0$ ואין שם פתרונות. עבור $x<0$ מתקיים $0<e^x<1$, ו-$\sin x$ מקבלת את כל הערכים בין $-1$ ל-$1$ שוב ושוב. בכל קטע $\left[-\frac\pi2-2\pi k,\,-2\pi k\right]$ (עבור $k=0,1,2,\dots$) מתקיים $f\left(-\frac\pi2-2\pi k\right)=e^{-\frac\pi2-2\pi k}-1<0$ ו-$f(-2\pi k)=e^{-2\pi k}>0$, ולכן לפי משפט ערך הביניים יש בכל קטע פתרון. למשוואה יש אם כן אינסוף פתרונות, והפתרון אינו יחיד.
"""

SOL4A = r"""
נמצא את הגבולות החד-צדדיים של $f$ ב-$x=\frac\pi2$.
$$\lim_{x\to\frac\pi2^-}f(x)=\lim_{x\to\frac\pi2^-}(\sin x)^{\tan x}=\{1^\infty\}=A$$
$$\ln A=\lim_{x\to\frac\pi2^-}\tan x\cdot\ln(\sin x)=\lim_{x\to\frac\pi2^-}\frac{\ln\sin x}{\cot x}=\lim_{x\to\frac\pi2^-}\frac{\frac{\cos x}{\sin x}}{-\frac{1}{\sin^2x}}=-\lim_{x\to\frac\pi2^-}\cos x\sin x=0\ \Rightarrow\ A=1$$
$$\lim_{x\to\frac\pi2^+}f(x)=\lim_{x\to\frac\pi2^+}e=e$$
הגבולות החד-צדדיים קיימים וסופיים אך שונים ($1\ne e$), ולכן $f$ אינה רציפה ב-$x=\frac\pi2$ (אי-רציפות מסוג ראשון, קפיצה).
"""

SOL4B = r"""
**הפתרון שבמקור (לא רשמי) עם תיקון:** בפתרון הכתוב התוצאה הסופית היא $\frac{\pi^2}{12}-\frac\pi3+\frac\pi6\ln2$. בהצבת הגבולות בשורה האחרונה מתקבל $\frac12-\frac12\ln2$ ולא $1-\frac12\ln2$, ולכן המקדם של $\pi$ הוא $-\frac16$ ולא $-\frac13$. הפתרון המתוקן נבדק (sympy).
$$V=\pi\int_0^1\left(x\sqrt{\arctan x}\right)^2dx=\pi\int_0^1x^2\arctan x\,dx=\left|\begin{matrix}u=\arctan x&du=\frac{dx}{1+x^2}\\dv=x^2dx&v=\frac{x^3}{3}\end{matrix}\right|=\pi\left(\frac{x^3}{3}\arctan x\Big|_0^1-\frac13\int_0^1\frac{x^3dx}{1+x^2}\right)=$$
$$=\pi\left(\frac13\cdot\frac\pi4-\frac13\int_0^1\left(x-\frac{x}{1+x^2}\right)dx\right)=\pi\left(\frac{\pi}{12}-\frac13\left(\frac{x^2}{2}-\frac12\ln\left(1+x^2\right)\right)\Big|_0^1\right)=\pi\left(\frac\pi{12}-\frac13\left(\frac12-\frac12\ln2\right)\right)=$$
$$=\frac{\pi^2}{12}-\frac\pi6+\frac\pi6\ln2$$
"""

SOL5A = r"""
נגדיר $f(x)=xe^{x^2}$. הפונקציה רציפה על $[a,b]$ וגזירה על $(a,b)$, ולכן לפי משפט לגרנז' קיימת $c\in(a,b)$ כך ש-$\frac{f(b)-f(a)}{b-a}=f'(c)$.
$$f'(x)=e^{x^2}+x\cdot e^{x^2}\cdot2x=e^{x^2}\left(1+2x^2\right)$$
$$\frac{be^{b^2}-ae^{a^2}}{b-a}=e^{c^2}\left(1+2c^2\right),\qquad1<a<c<b<2$$
$f'(x)=e^{x^2}\left(1+2x^2\right)$ עולה ממש עבור $x>0$ (מכפלה של שתי פונקציות חיוביות עולות), ולכן מ-$1<c<2$ נקבל
$$3e=f'(1)<e^{c^2}\left(1+2c^2\right)<f'(2)=9e^4$$
כלומר $3e<\frac{be^{b^2}-ae^{a^2}}{b-a}<9e^4$.
"""

SOL5B = r"""
$$\int\frac{\sin^3x}{\cos^4x}dx=\left|\begin{matrix}t=\cos x\\dt=-\sin x\,dx\end{matrix}\right|=\int\frac{\sin^2x\cdot\sin x\,dx}{\cos^4x}=-\int\frac{1-t^2}{t^4}dt=\frac{1}{3t^3}-\frac1t+C=\frac{1}{3\cos^3x}-\frac{1}{\cos x}+C$$
"""

SOL6A = r"""
$$y=\sqrt{1-x^2}\ \Rightarrow\ y'=\frac{-x}{\sqrt{1-x^2}}\ \Rightarrow\ 1+(y')^2=\frac{x^2}{1-x^2}+1=\frac{1}{1-x^2}$$
$$L=\int_0^{0.5}\sqrt{1+(y')^2}\,dx=\int_0^{0.5}\frac{1}{\sqrt{1-x^2}}\,dx=\arcsin x\Big|_0^{0.5}=\arcsin0.5=\frac\pi6$$
"""

SOL6B = r"""
$$\lim_{x\to1^-}\ln x\cdot\ln(1-x)=\{0\cdot\infty\}=\lim_{x\to1^-}\frac{\ln(1-x)}{\frac{1}{\ln x}}=\lim_{x\to1^-}\frac{-\frac{1}{1-x}}{-\frac{1}{\ln^2x}\cdot\frac1x}=\lim_{x\to1^-}\frac{x\ln^2x}{1-x}=\left\{\frac00\right\}=\lim_{x\to1^-}\frac{\ln^2x+2\ln x}{-1}=0$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה הבאה $y=\frac{x^3}{x^2-3}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, תחומי עליה וירידה, "
      "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1),

    Q(2, "proof", "sequences_limits",
      r"נתונה הסדרה: $a_1=2,\quad a_{n+1}=\frac{3a_n}{2a_n+1}$. הוכיחו כי הסדרה מונוטונית וחסומה וחשבו את גבולה.",
      SOL2, points=10),

    Q(3, "computation", "extrema_optimization",
      r"מצאו את כל ערכי $x$ שבהם לפונקציה $f(x)=\int_{-3}^{x^3+1}t\cdot(t-1)^5\,dt$ יש קיצון מקומי.",
      SOL3A, part="א", points=10),

    Q(3, "proof", "continuity",
      r"הראו שלמשוואה $e^x+\sin x=0$ קיים פתרון. האם הוא יחיד?",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "continuity",
      r"בדקו האם הפונקציה $f(x)=\begin{cases}(\sin x)^{\tan x}, & 0<x<0.5\pi\\[1mm] e, & x\ge0.5\pi\end{cases}$ רציפה ב-$x=0.5\pi$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      "מצאו את נפח הגוף הנוצר על ידי הסיבוב סביב ציר ה-$X$ של הצורה המישורית הכלואה בין הקווים הבאים: "
      r"$y=x\sqrt{\arctan x},\ y=0,\ x=1$.",
      SOL4B, part="ב", points=10,
      solutionSource="solved"),

    Q(5, "proof", "mean_value_theorems",
      r"הוכיחו את אי-השוויון $3e<\frac{be^{b^2}-ae^{a^2}}{b-a}<9e^4$ כאשר $1<a<b<2$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int\frac{\sin^3x}{\cos^4x}\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "definite_integrals",
      r"מצאו את אורך הקשת של $y=\sqrt{1-x^2}$ כאשר $0\le x\le0.5$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to1^-}\ln x\cdot\ln(1-x)$.",
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

# ===== Q1: y = x^3/(x^2-3) =====
f1 = x**3/(x**2 - 3)
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, x**2*(x**2 - 9)/(x**2 - 3)**2) and same(f1pp, 6*x*(x**2 + 9)/(x**2 - 3)**3)
assert same(f1.subs(x, -x), -f1)
assert sp.solve(sp.numer(sp.together(f1p)), x) == [-3, 0, 3] or sorted(sp.solve(sp.numer(sp.together(f1p)), x)) == [-3, 0, 3]
assert f1.subs(x, 3) == R(9, 2) and f1.subs(x, -3) == -R(9, 2)
assert f1p.subs(x, -4) > 0 and f1p.subs(x, -2) < 0 and f1p.subs(x, 1) < 0 and f1p.subs(x, 2) < 0 and f1p.subs(x, 4) > 0
assert sp.solve(sp.numer(sp.together(f1pp)), x) == [0]
s3 = sp.sqrt(3)
assert f1pp.subs(x, -3) < 0 and f1pp.subs(x, -1) > 0 and f1pp.subs(x, 1) < 0 and f1pp.subs(x, 3) > 0
assert sp.limit(f1/x, x, sp.oo) == 1 and sp.limit(f1 - x, x, sp.oo) == 0 and sp.limit(f1 - x, x, -sp.oo) == 0
assert sp.limit(f1, x, s3, '+') == sp.oo and sp.limit(f1, x, s3, '-') == -sp.oo

add(1,
    rubric=rub(("תחום הגדרה $x\\neq\\pm\\sqrt3$, חיתוך יחיד $(0,0)$ ואי-זוגיות הפונקציה", 3),
               ("אסימפטוטות אנכיות $x=\\pm\\sqrt3$ עם הגבולות החד-צדדיים", 4),
               ("אסימפטוטה משופעת $y=x$ ב-$\\pm\\infty$", 3),
               ("נגזרת $y'=\\frac{x^2(x^2-9)}{(x^2-3)^2}$, תחומי עליה וירידה, מקסימום ב-$x=-3$ ומינימום ב-$x=3$", 5),
               ("$y''=\\frac{6x(x^2+9)}{(x^2-3)^3}$, תחומי קמירות וקעירות ונקודת הפיתול $(0,0)$", 4),
               ("שרטוט הגרף בהתאם לכל הנתונים", 1)),
    rubricSource="ai-draft",
    pitfalls=["לטעון ש-$x=0$ היא נקודת קיצון כי $y'(0)=0$: $y'$ אינה משנה סימן ב-$0$ (גורם $x^2$), והנקודה היא נקודת פיתול.",
              "לבלבל את סימני הגבולות החד-צדדיים באסימפטוטות האנכיות; הסימן נקבע לפי סימן המכנה $x^2-3$ משני צדי $\\pm\\sqrt3$.",
              "לכלול את $x=\\pm\\sqrt3$ בתחומי העליה והירידה או בתחומי הקמירות."],
    steps=[
        chx("מהי הנגזרת של $y=\\frac{x^3}{x^2-3}$?", x**2*(x**2 - 9)/(x**2 - 3)**2,
            [x**2*(x**2 + 9)/(x**2 - 3)**2, x**2*(x**2 - 9)/(x**2 - 3), 3*x**2/(2*x)],
            lambda e: same(e, f1p),
            "כלל המנה: $\\frac{3x^2(x^2-3)-2x^4}{(x^2-3)^2}=\\frac{x^4-9x^2}{(x^2-3)^2}$ (אומת ב-sympy)."),
        num("מהו ערך הפונקציה בנקודת המינימום המקומי $x=3$? (עשרוני)", R(9, 2), "$y(3)=\\frac{27}{6}=4.5$ (sympy)."),
        ch("מה סוג הנקודה $x=0$?", "נקודת פיתול (ולא קיצון)",
           ["מקסימום מקומי", "מינימום מקומי", "נקודה שאינה בתחום ההגדרה"],
           "$y'(0)=0$ אך $y'$ שלילית משני צדי $0$ (אין שינוי סימן), ו-$y''$ משנה סימן ב-$0$ (sympy)."),
        ch("מהן האסימפטוטות של $y$?", "אנכיות $x=\\pm\\sqrt3$ ומשופעת $y=x$",
           ["אנכית $x=0$ ומשופעת $y=x$", "אנכיות $x=\\pm\\sqrt3$ ואופקית $y=0$", "אנכיות $x=\\pm3$ ומשופעת $y=x$"],
           "המכנה מתאפס ב-$x=\\pm\\sqrt3$; $\\lim\\frac{y}{x}=1$ ו-$\\lim(y-x)=\\lim\\frac{3x}{x^2-3}=0$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q2: a_1 = 2, a_{n+1} = 3a_n/(2a_n+1) =====
sq = [R(2)]
for _ in range(7):
    sq.append(3*sq[-1]/(2*sq[-1] + 1))
assert sq[1] == R(6, 5) and sq[2] == R(18, 17)
assert all(sq[i] > sq[i + 1] > 1 for i in range(len(sq) - 1))
aa = sp.Symbol('aa', positive=True)
assert same((3*aa/(2*aa + 1))/aa, 3/(2*aa + 1))
assert 3/(2*R(11, 10) + 1) < 1 and 3/(2*R(19, 10) + 1) < 1
L2 = sp.Symbol('L2', real=True)
assert sorted(sp.solve(sp.Eq(L2, 3*L2/(2*L2 + 1)), L2)) == [0, 1]
P2 = ["נוכיח באינדוקציה ש-$1<a_n\\le2$ לכל $n$.",
      "מכאן $\\frac{a_{n+1}}{a_n}=\\frac{3}{2a_n+1}<1$, כלומר הסדרה יורדת.",
      "סדרה יורדת וחסומה מלמטה מתכנסת; נסמן את גבולה $L$.",
      "במעבר לגבול $L=\\frac{3L}{2L+1}$, כלומר $L^2-L=0$.",
      "מכיוון ש-$a_n>1$ לא ייתכן $L=0$, ולכן $L=1$."]
P2b = list(P2)
P2b[4] = "מכיוון ש-$a_n<2$ לא ייתכן $L=0$, ולכן $L=1$."
assert 0 < 2 and all(v <= 2 for v in sq)  # the bound a_n<2 alone does not exclude L=0

add(2,
    rubric=rub(("חסימות באינדוקציה: $1<a_n\\le2$ (הפתרון הרשמי כותב $a_n<2$, אך $a_1=2$)", 3),
               ("מונוטוניות: $\\frac{a_{n+1}}{a_n}=\\frac{3}{2a_n+1}<1$, הסדרה יורדת", 3),
               ("מסקנה: סדרה יורדת וחסומה מלמטה מתכנסת", 1),
               ("משוואת הגבול $L^2-L=0$ ופסילת $L=0$ בעזרת $a_n>1$, ולכן $L=1$", 3)),
    rubricSource="ai-draft",
    pitfalls=["לחשב את הגבול מהמשוואה $L=\\frac{3L}{2L+1}$ בלי להוכיח קודם התכנסות, ולהשאיר גם את $L=0$.",
              "לפסול את $L=0$ בעזרת החסם העליון $a_n<2$ במקום החסם התחתון $a_n>1$.",
              "להשתמש ביחס $\\frac{a_{n+1}}{a_n}<1$ בלי לדעת ש-$a_n>0$.",
              "לכתוב $a_n<2$ ממש לכל $n$: $a_1=2$, והחסם העליון מתקיים כאי-שוויון חלש."],
    steps=[
        num("מהו $a_2$? (עשרוני)", sq[1], "$a_2=\\frac{3\\cdot2}{2\\cdot2+1}=\\frac65=1.2$."),
        chx("מהו היחס $\\frac{a_{n+1}}{a_n}$?", 3/(2*aa + 1), [3/(2*aa - 1), 3*aa/(2*aa + 1), 1/(2*aa + 1)],
            lambda e: same(e, (3*aa/(2*aa + 1))/aa),
            "$\\frac{a_{n+1}}{a_n}=\\frac{3a_n}{(2a_n+1)a_n}=\\frac{3}{2a_n+1}$ (אומת ב-sympy)."),
        ch("מדוע היחס $\\frac{3}{2a_n+1}$ קטן מ-$1$?", "כי $a_n>1$ ולכן $2a_n+1>3$",
           ["כי $a_n<2$ ולכן $2a_n+1<5$", "כי $a_1=2$", "כי $a_n$ חיובית בלבד"],
           "החסם התחתון $a_n>1$ נותן מכנה גדול מ-$3$. החסם העליון לא עוזר, ו-$a_n>0$ בלבד לא מספיק (עבור $a_n$ קטן מ-$1$ היחס גדול מ-$1$)."),
        order("סדרו את שלבי ההוכחה.", P2,
              "החסימות ראשונה כי המונוטוניות והפסילה של $L=0$ נשענות עליה; ההתכנסות נובעת משתיהן ורק אחריה פותרים את משוואת הגבול."),
        findbug("בהוכחה שורה אחת שגויה. מצאו אותה.", P2b, 4,
                "החסם העליון $a_n<2$ אינו שולל את $L=0$; השלילה נובעת מהחסם התחתון $a_n>1$."),
        num("מהו גבול הסדרה?", 1, "$L^2-L=0$ ו-$L\\ge1$ ולכן $L=1$ (sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q3a: extrema of f(x) = int_{-3}^{x^3+1} t (t-1)^5 dt =====
tq = sp.Symbol('tq', real=True)
Fq = sp.integrate(tq*(tq - 1)**5, tq)
fx3 = Fq.subs(tq, x**3 + 1)
f3p = sp.diff(fx3, x)
assert same(f3p, 3*x**17*(x**3 + 1))
assert sorted(sp.solve(f3p, x)) == [-1, 0] or sorted(sp.solve(sp.Eq(x**17*(x**3 + 1), 0), x)) == [-1, 0]
assert f3p.subs(x, -2) > 0 and f3p.subs(x, R(-1, 2)) < 0 and f3p.subs(x, 1) > 0

add(3, "א",
    rubric=rub(("משפט היסוד וכלל השרשרת: $f'(x)=g(x^3+1)\\cdot3x^2$ עבור $g(t)=t(t-1)^5$", 4),
               ("פישוט ל-$f'(x)=3x^{17}(x^3+1)$ והנקודות הקריטיות $x=0,-1$", 2),
               ("טבלת סימנים של $f'$", 2),
               ("מסקנה: מקסימום ב-$x=-1$ ומינימום ב-$x=0$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח את גורם השרשרת $3x^2$ (נגזרת הגבול העליון).",
              "לפתור קודם את האינטגרל במקום להשתמש במשפט היסוד.",
              "להסיק קיצון בכל נקודה שבה $f'=0$ בלי לבדוק החלפת סימן."],
    steps=[
        chx("מהי הנגזרת של $f(x)=\\int_{-3}^{x^3+1}t(t-1)^5dt$?", 3*x**17*(x**3 + 1),
            [x**17*(x**3 + 1), 3*x**2*(x**3 + 1)*(x**3 + 1)**5, (x**3 + 1)*x**15],
            lambda e: same(e, f3p),
            "$f'(x)=(x^3+1)\\left((x^3+1)-1\\right)^5\\cdot3x^2=3x^{17}(x^3+1)$ (אומת ב-sympy)."),
        num("מהו ערך $x$ השלילי שבו $f'(x)=0$?", -1, "$x^3+1=0$ נותן $x=-1$; והשני $x=0$."),
        ch("מה סוגי הקיצון של $f$?", "מקסימום ב-$x=-1$ ומינימום ב-$x=0$",
           ["מינימום ב-$x=-1$ ומקסימום ב-$x=0$", "מקסימום בשתי הנקודות", "קיצון רק ב-$x=-1$"],
           "$f'$ חיובית לפני $-1$, שלילית בין $-1$ ל-$0$, וחיובית אחרי $0$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q3b: e^x + sin x = 0 =====
fe = lambda v: sp.exp(v) + sp.sin(v)
assert fe(0) == 1 and float(sp.N(fe(-sp.pi/2))) < 0 and abs(float(sp.N(fe(-sp.pi/2))) - (-0.7921)) < 1e-3
assert all(float(sp.N(fe(-sp.pi/2 - 2*sp.pi*k))) < 0 and float(sp.N(fe(-2*sp.pi*k))) > 0 for k in range(0, 5))
# f is not monotone: f' = e^x + cos x changes sign
fpe = lambda v: sp.exp(v) + sp.cos(v)
assert float(sp.N(fpe(-sp.pi))) < 0 and float(sp.N(fpe(0))) > 0
L3 = ["הפונקציה $f(x)=e^x+\\sin x$ רציפה על כל הממשיים.",
      "$f(0)=1>0$ ו-$f\\left(-\\frac\\pi2\\right)=e^{-\\pi/2}-1<0$, כי $e^{-\\pi/2}<1$.",
      "לפי משפט ערך הביניים קיים פתרון בקטע $\\left[-\\frac\\pi2,0\\right]$."]
L3b = list(L3)
L3b[1] = "$f(0)=1>0$ ו-$f\\left(-\\frac\\pi2\\right)=e^{-\\pi/2}-1>0$, כי $e^{-\\pi/2}>1$."
assert float(sp.N(sp.exp(-sp.pi/2))) < 1

add(3, "ב",
    rubric=rub(("רציפות $f(x)=e^x+\\sin x$ על כל הממשיים", 1),
               ("מציאת שני ערכים בעלי סימנים הפוכים: $f(0)>0$ ו-$f\\left(-\\frac\\pi2\\right)<0$", 3),
               ("הפעלת משפט ערך הביניים וקיום פתרון", 2),
               ("הפתרון אינו יחיד: בכל קטע $\\left[-\\frac\\pi2-2\\pi k,-2\\pi k\\right]$ יש פתרון, ולכן אינסוף פתרונות", 4)),
    rubricSource="ai-draft",
    pitfalls=["להסיק יחידות מכך ש-$e^x$ עולה: הסכום $e^x+\\sin x$ אינו מונוטוני.",
              "לטעון ש-$f\\left(-\\frac\\pi2\\right)>0$ בגלל $e^{-\\pi/2}>1$; בפועל $e^{-\\pi/2}<1$.",
              "לשכוח לציין שמשפט ערך הביניים דורש רציפות בקטע סגור."],
    steps=[
        num("מהו $f(0)=e^0+\\sin0$?", 1, "$f(0)=1>0$."),
        num("מהו $f\\left(-\\frac\\pi2\\right)=e^{-\\pi/2}-1$? (עשרוני)", fe(-sp.pi/2), "$e^{-\\pi/2}\\approx0.2079$ ולכן $f\\left(-\\frac\\pi2\\right)\\approx-0.7921<0$ (sympy).", tol=0.001),
        findbug("בנימוק לקיום פתרון שורה אחת שגויה. מצאו אותה.", L3b, 1,
                "$e^{-\\pi/2}<1$, ולכן $f\\left(-\\frac\\pi2\\right)=e^{-\\pi/2}-1<0$, לא חיובי."),
        ch("האם הפתרון יחיד?", "לא: בכל קטע $\\left[-\\frac\\pi2-2\\pi k,-2\\pi k\\right]$ יש פתרון ולכן יש אינסוף פתרונות",
           ["כן, כי $e^x$ פונקציה עולה", "כן, כי $f(x)>0$ לכל $x<0$", "לא, אך יש בדיוק שני פתרונות"],
           "בכל קטע כזה $f$ משנה סימן (מ-$e^{-\\pi/2-2\\pi k}-1<0$ ל-$e^{-2\\pi k}>0$), ולכן יש פתרון בכל קטע. $f$ אינה מונוטונית: $f'(-\\pi)<0<f'(0)$ (sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q4a: continuity of (sin x)^(tan x) at pi/2 =====
import mpmath as mpm
lnA = lambda xv: mpm.tan(xv)*mpm.log(mpm.sin(xv))
assert abs(lnA(mpm.pi/2 - mpm.mpf('1e-6'))) < 1e-5
assert abs(mpm.power(mpm.sin(mpm.pi/2 - mpm.mpf('1e-6')), mpm.tan(mpm.pi/2 - mpm.mpf('1e-6'))) - 1) < 1e-5

add(4, "א",
    rubric=rub(("זיהוי הצורה $1^{\\infty}$ בגבול השמאלי והעברה ללוגריתם", 3),
               ("חישוב $\\ln A=\\lim\\frac{\\ln\\sin x}{\\cot x}=0$ (לופיטל), ולכן $A=1$", 3),
               ("הגבול הימני $e$", 1),
               ("מסקנה: $1\\neq e$, לכן אי-רציפות (קפיצה, ממין ראשון)", 3)),
    rubricSource="ai-draft",
    pitfalls=["לבדוק רק את הגבול משמאל ולהשוות אותו ל-$e$ בלי לחשב אותו נכון: הוא $1$ ולא $e$.",
              "לטעון ש-$1^{\\infty}=1$ ללא חישוב; זו צורה לא מסוימת.",
              "לקבוע \"לא רציפה\" בלי לציין שמדובר באי-רציפות מסוג ראשון."],
    steps=[
        ch("מה סוג הצורה של $(\\sin x)^{\\tan x}$ כאשר $x\\to\\frac\\pi2^-$?", "$1^{\\infty}$",
           ["$0^0$", "$\\infty^0$", "$0^{\\infty}$"],
           "$\\sin x\\to1$ ו-$\\tan x\\to+\\infty$ משמאל ל-$\\frac\\pi2$."),
        num("מהו $\\lim_{x\\to\\frac\\pi2^-}\\ln A=\\lim\\tan x\\cdot\\ln\\sin x$?", 0,
            "$\\frac{\\ln\\sin x}{\\cot x}\\to-\\lim\\cos x\\sin x=0$ (נבדק נומרית ב-mpmath)."),
        num("מהו הגבול השמאלי $\\lim_{x\\to\\frac\\pi2^-}(\\sin x)^{\\tan x}$?", 1, "$A=e^0=1$."),
        ch("מה מסקנת הבדיקה?", "לא רציפה: הגבולות החד-צדדיים $1$ ו-$e$ שונים",
           ["רציפה, כי הגבול הימני שווה ל-$f\\left(\\frac\\pi2\\right)=e$", "רציפה, כי הגבול השמאלי $1$", "לא רציפה, כי אחד הגבולות אינסופי"],
           "הגבול הימני $e=f\\left(\\frac\\pi2\\right)$ אבל השמאלי $1\\neq e$, ולכן אין רציפות; שני הגבולות סופיים ולכן זו קפיצה."),
    ],
    stepsSource="ai-draft")

# ===== Q4b: volume, y = x*sqrt(arctan x) about x-axis =====
I4 = sp.integrate(x**2*sp.atan(x), (x, 0, 1))
V4 = sp.pi*I4
assert same(V4, sp.pi**2/12 - sp.pi/6 + sp.pi*sp.log(2)/6)
rem4 = sp.integrate(x**3/(1 + x**2), (x, 0, 1))
assert same(rem4, R(1, 2) - sp.log(2)/2)
vo = lambda g: abs(float(sp.N(sp.integrate(g, (x, 0, 1)) - I4))) < 1e-9
assert vo(x**2*sp.atan(x))
for w in (x*sp.atan(x), x**2*sp.sqrt(sp.atan(x)), 2*x**2*sp.atan(x)):
    assert not vo(w)

add(4, "ב",
    rubric=rub(("נוסחת נפח סיבוב סביב ציר $x$: $\\pi\\int_0^1\\left(x\\sqrt{\\arctan x}\\right)^2dx=\\pi\\int_0^1x^2\\arctan x\\,dx$", 3),
               ("אינטגרציה בחלקים: $u=\\arctan x$, $dv=x^2dx$", 3),
               ("האינטגרל הנותר $\\int_0^1\\frac{x^3}{1+x^2}dx=\\frac12-\\frac12\\ln2$ (חילוק פולינומים)", 2),
               ("הערך הסופי $V=\\frac{\\pi^2}{12}-\\frac\\pi6+\\frac\\pi6\\ln2$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח לרבע את הרדיוס: $\\left(x\\sqrt{\\arctan x}\\right)^2=x^2\\arctan x$.",
              "טעות הצבת גבולות בשורה האחרונה: $\\frac13\\left(\\frac12-\\frac12\\ln2\\right)=\\frac16-\\frac16\\ln2$ ולכן המקדם של $\\pi$ הוא $-\\frac16$.",
              "לשכוח לחלק את $\\frac{x^3}{1+x^2}$ ל-$x-\\frac{x}{1+x^2}$ לפני האינטגרציה."],
    steps=[
        chx("איזה אינטגרנד (ב-$x$ מ-$0$ עד $1$) מתאים לנפח החלוקות $\\frac{V}{\\pi}$?", x**2*sp.atan(x),
            [x*sp.atan(x), x**2*sp.sqrt(sp.atan(x)), 2*x**2*sp.atan(x)], vo,
            "סיבוב סביב ציר $x$: $V=\\pi\\int y^2dx$ ו-$y^2=x^2\\arctan x$. שאר האינטגרנדים נותנים ערך אחר (נבדק ב-sympy)."),
        num("מהו $\\int_0^1\\frac{x^3}{1+x^2}dx$? (עשרוני)", rem4, "$\\int_0^1\\left(x-\\frac{x}{1+x^2}\\right)dx=\\frac12-\\frac12\\ln2\\approx0.1534$ (sympy)."),
        num("מהו $\\int_0^1x^2\\arctan x\\,dx$? (עשרוני)", I4, "$\\frac{\\pi}{12}-\\frac13\\left(\\frac12-\\frac12\\ln2\\right)=\\frac{\\pi}{12}-\\frac16+\\frac{\\ln2}{6}\\approx0.2107$ (sympy)."),
        num("מהו נפח הגוף? (עשרוני)", V4, "$V=\\pi\\cdot0.2107\\approx0.662$, כלומר $\\frac{\\pi^2}{12}-\\frac\\pi6+\\frac\\pi6\\ln2$ (sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q5a: Lagrange inequality =====
f5 = x*sp.exp(x**2)
f5p = sp.diff(f5, x)
assert same(f5p, sp.exp(x**2)*(1 + 2*x**2))
assert same(f5p.subs(x, 1), 3*sp.E) and same(f5p.subs(x, 2), 9*sp.exp(4))
assert sp.simplify(sp.diff(f5p, x)) is not None and all(sp.diff(f5p, x).subs(x, v) > 0 for v in (R(1, 2), 1, 2))
L5 = ["נגדיר $f(x)=xe^{x^2}$, רציפה ב-$[a,b]$ וגזירה ב-$(a,b)$; לפי משפט לגרנז' קיימת $c\\in(a,b)$ עם $\\frac{f(b)-f(a)}{b-a}=f'(c)$.",
      "$f'(x)=e^{x^2}\\left(1+2x^2\\right)$, ולכן הביטוי שווה ל-$e^{c^2}\\left(1+2c^2\\right)$ עבור $1<c<2$.",
      "$f'$ עולה ממש עבור $x>0$, ולכן $f'(1)<f'(c)<f'(2)$.",
      "מכאן $3e<\\frac{be^{b^2}-ae^{a^2}}{b-a}<9e^4$."]
L5b = list(L5)
L5b[1] = "$f'(x)=e^{x^2}\\left(1+x^2\\right)$, ולכן הביטוי שווה ל-$e^{c^2}\\left(1+c^2\\right)$ עבור $1<c<2$."
assert not same(f5p, sp.exp(x**2)*(1 + x**2)) and same((sp.exp(x**2)*(1 + x**2)).subs(x, 1), 2*sp.E)

add(5, "א",
    rubric=rub(("הגדרת $f(x)=xe^{x^2}$ ובדיקת רציפות וגזירות על $[a,b]$", 2),
               ("הפעלת משפט לגרנז': הביטוי שווה ל-$f'(c)$ עבור $c\\in(a,b)$", 2),
               ("חישוב הנגזרת $f'(x)=e^{x^2}\\left(1+2x^2\\right)$", 2),
               ("מונוטוניות $f'$ בקטע וחסימה: $f'(1)=3e$ ו-$f'(2)=9e^4$", 3),
               ("מסקנת אי-השוויון", 1)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח לנמק ש-$f'$ עולה בקטע; בלי זה אי אפשר לחסום את $f'(c)$ בין $f'(1)$ ל-$f'(2)$.",
              "לגזור את $xe^{x^2}$ בלי כלל המכפלה ובלי גורם השרשרת $2x$.",
              "להסתפק ב-$a<c<b$ ולשכוח ש-$1<a<b<2$ נותן $1<c<2$."],
    steps=[
        chx("מהי הנגזרת של $f(x)=xe^{x^2}$?", sp.exp(x**2)*(1 + 2*x**2),
            [sp.exp(x**2)*(1 + x**2), sp.exp(x**2)*(1 + 2*x), 2*x**2*sp.exp(x**2)], lambda e: same(e, f5p),
            "כלל המכפלה והשרשרת: $e^{x^2}+x\\cdot e^{x^2}\\cdot2x=e^{x^2}\\left(1+2x^2\\right)$ (אומת ב-sympy)."),
        num("מהו $f'(1)$? (עשרוני)", f5p.subs(x, 1), "$f'(1)=3e\\approx8.1548$ (sympy)."),
        num("מהו $f'(2)$? (עשרוני)", f5p.subs(x, 2), "$f'(2)=9e^4\\approx491.38$ (sympy).", tol=0.01),
        order("סדרו את שלבי ההוכחה.", L5, "הפעלת לגרנז', חישוב הנגזרת, חסימת $f'(c)$ באמצעות מונוטוניות, מסקנה. כל שלב נשען על קודמו."),
        findbug("בהוכחה שורה אחת שגויה. מצאו אותה.", L5b, 1,
                "הנגזרת היא $e^{x^2}\\left(1+2x^2\\right)$; עם $1+x^2$ מתקבל $f'(1)=2e$ ולא $3e$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q5b: int sin^3/cos^4 =====
g5b = sp.sin(x)**3/sp.cos(x)**4
F5b = 1/(3*sp.cos(x)**3) - 1/sp.cos(x)
assert same(sp.diff(F5b, x), g5b)
t5 = sp.Symbol('t5', positive=True)
assert same(-(1 - t5**2)/t5**4, -1/t5**4 + 1/t5**2)
F5w = [1/(3*sp.cos(x)**3) + 1/sp.cos(x), -1/(3*sp.cos(x)**3) + 1/sp.cos(x), 1/(3*sp.cos(x)**3) - sp.cos(x)]
tok = lambda e: same(e, -(1 - t5**2)/t5**4)

add(5, "ב",
    rubric=rub(("הצבה $t=\\cos x$ עם $dt=-\\sin x\\,dx$", 3),
               ("$\\sin^2x=1-t^2$ והמעבר ל-$-\\int\\frac{1-t^2}{t^4}dt$", 3),
               ("אינטגרציה איבר איבר: $\\frac{1}{3t^3}-\\frac1t$", 2),
               ("חזרה ל-$x$ ותשובה עם $+C$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח את המינוס מ-$dt=-\\sin x\\,dx$.",
              "לא להפריד גורם $\\sin x\\,dx$ ולנסות להציב $t=\\sin x$.",
              "טעות באינטגרציה של $t^{-4}$ ו-$t^{-2}$: $\\int t^{-4}dt=-\\frac{1}{3t^3}$ ו-$\\int t^{-2}dt=-\\frac1t$."],
    steps=[
        ch("איזו הצבה מתאימה לאינטגרל $\\int\\frac{\\sin^3x}{\\cos^4x}dx$?", "$t=\\cos x$, כי החזקה של הסינוס אי-זוגית",
           ["$t=\\sin x$", "$t=\\tan x$", "$t=\\cos^4x$"],
           "מפרידים $\\sin x\\,dx=-dt$ ו-$\\sin^2x=1-t^2$. ההצבה $t=\\sin x$ אינה נותנת גורם $\\cos x\\,dx$."),
        chx("מהו האינטגרנד אחרי ההצבה $t=\\cos x$ (האינטגרל ב-$dt$)?", -(1 - t5**2)/t5**4,
            [(1 - t5**2)/t5**4, -(1 + t5**2)/t5**4, -(1 - t5**2)/t5**2], tok,
            "$\\frac{\\sin^2x\\cdot\\sin x\\,dx}{\\cos^4x}=\\frac{(1-t^2)(-dt)}{t^4}$ (אומת ב-sympy)."),
        chx("מהו האינטגרל? (בלי הקבוע)", F5b, F5w, lambda e: same(sp.diff(e, x), g5b),
            "$-\\int\\left(t^{-4}-t^{-2}\\right)dt=\\frac{1}{3t^3}-\\frac1t$ עם $t=\\cos x$. הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-draft")

# ===== Q6a: arc length of sqrt(1-x^2) on [0, 0.5] =====
y6 = sp.sqrt(1 - x**2)
assert same(sp.diff(y6, x), -x/sp.sqrt(1 - x**2)) and same(1 + sp.diff(y6, x)**2, 1/(1 - x**2))
L6 = sp.integrate(1/sp.sqrt(1 - x**2), (x, 0, R(1, 2)))
assert L6 == sp.pi/6

add(6, "א",
    rubric=rub(("נגזרת $y'=\\frac{-x}{\\sqrt{1-x^2}}$", 2),
               ("חישוב $1+(y')^2=\\frac{1}{1-x^2}$", 3),
               ("נוסחת אורך הקשת: $\\int_0^{0.5}\\frac{dx}{\\sqrt{1-x^2}}$", 2),
               ("$\\arcsin$ והערך $\\frac\\pi6$", 3)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח את השורש בנוסחה $L=\\int\\sqrt{1+(y')^2}dx$.",
              "לטעות בחישוב $1+\\frac{x^2}{1-x^2}$: זה $\\frac{1}{1-x^2}$ ולא $\\frac{1+x^2}{1-x^2}$.",
              "לחשב $\\arcsin(0.5)$ במעלות או כ-$\\frac\\pi3$."],
    steps=[
        chx("מהו הביטוי $1+(y')^2$?", 1/(1 - x**2), [(1 + x**2)/(1 - x**2), 1/(1 + x**2), 1 - x**2],
            lambda e: same(e, 1 + sp.diff(y6, x)**2),
            "$1+\\frac{x^2}{1-x^2}=\\frac{1}{1-x^2}$ (אומת ב-sympy)."),
        num("מהו ערך אורך הקשת? (עשרוני)", L6, "$\\int_0^{0.5}\\frac{dx}{\\sqrt{1-x^2}}=\\arcsin0.5=\\frac\\pi6\\approx0.5236$ (sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q6b: lim_{x->1-} ln x * ln(1-x) =====
lim6 = sp.limit(sp.log(x)*sp.log(1 - x), x, 1, '-')
assert lim6 == 0
g6 = x*sp.log(x)**2/(1 - x)
lh6 = sp.diff(sp.log(1 - x), x)/sp.diff(1/sp.log(x), x)
assert same(lh6, g6)
assert sp.limit(g6, x, 1, '-') == 0 and sp.limit(sp.log(x), x, 1, '-') == 0 and sp.limit(sp.log(1 - x), x, 1, '-') == -sp.oo

add(6, "ב",
    rubric=rub(("זיהוי הצורה $0\\cdot\\infty$", 2),
               ("הפיכה למנה $\\frac{\\ln(1-x)}{1/\\ln x}$ ולופיטל ראשון", 3),
               ("פישוט ל-$\\frac{x\\ln^2x}{1-x}$ וזיהוי $\\frac00$", 3),
               ("לופיטל שני וערך הגבול $0$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לכתוב \"$0\\cdot\\infty=0$\" בלי חישוב: זו צורה לא מסוימת.",
              "בחירת המנה ההפוכה $\\frac{\\ln x}{1/\\ln(1-x)}$, שהנגזרת שלה מסובכת יותר.",
              "טעות בנגזרת של $\\frac{1}{\\ln x}$: היא $-\\frac{1}{x\\ln^2x}$."],
    steps=[
        ch("מה סוג הצורה של $\\ln x\\cdot\\ln(1-x)$ כאשר $x\\to1^-$?", "$0\\cdot\\infty$",
           ["$\\infty-\\infty$", "$1^{\\infty}$", "$\\frac00$"],
           "$\\ln x\\to0$ ו-$\\ln(1-x)\\to-\\infty$ (נבדק ב-sympy)."),
        chx("מהו הביטוי אחרי לופיטל ראשון על $\\frac{\\ln(1-x)}{1/\\ln x}$ ופישוט?", g6,
            [x*sp.log(x)/(1 - x), sp.log(x)**2/(1 - x), x*sp.log(x)**2*(1 - x)], lambda e: same(e, lh6),
            "$\\frac{-\\frac{1}{1-x}}{-\\frac{1}{x\\ln^2x}}=\\frac{x\\ln^2x}{1-x}$, וזו צורה $\\frac00$ (אומת ב-sympy)."),
        num("מהו ערך הגבול?", 0, "לופיטל שני: $\\frac{\\ln^2x+2\\ln x}{-1}\\to0$ (sympy)."),
    ],
    stepsSource="ai-draft")


exam = {
    "examCode": "18B-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ח, מועד ב'",
    "year": 2018,
    "examDate": "05/02/2018",
    "sourceFile": "calculus-1/18B-A exam.pdf",
    "solutionFile": "calculus-1/18B-A handwritten-solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

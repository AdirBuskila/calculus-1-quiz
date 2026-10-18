# -*- coding: utf-8 -*-
"""Generator for tools/raw/20A-A.json -- calculus-1 (20151), semester A 2020, moed A (20/02/2020).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_20A-A.py

Source: sitting 20A-A, pp.1-6 (typed exam with the official worked solution after every question).
Part A (mandatory): Q1 (20%). Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Q1 sketch (p.3 top) is shipped as a figure inside the solution.
- Q6a/Q6b share the function of Q6; the stem is repeated in both parts.
- Q6a: the official solution treats only x=3 (the endpoint x=2 is not discussed); transcribed as printed.

Checks (tools/verify/20A-A/check.py, sympy): derivatives, limits, asymptotes, partial fractions, antiderivatives,
arc length, the continuity parameter and the solid of revolution all match the official answers. 0 mismatches.
No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20A-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**תחום ההגדרה:** $x\neq 0$. מיון אי-רציפות ב-$x=0$:
$$\lim_{x\to0^+}xe^{\frac1x}=\lim_{x\to0^+}\frac{e^{\frac1x}}{\frac1x}=\left[\frac{\infty}{\infty}\right]=\lim_{x\to0^+}\frac{\left(e^{\frac1x}\right)'}{\left(\frac1x\right)'}=\lim_{x\to0^+}\frac{-\frac{1}{x^2}e^{\frac1x}}{-\frac{1}{x^2}}=\lim_{x\to0^+}e^{\frac1x}=+\infty$$
$$\lim_{x\to0^-}xe^{\frac1x}=\lim_{x\to0^-}\frac{e^{\frac1x}}{\frac1x}=\left[\frac{0}{\infty}\right]=0$$
אז $x=0$ היא נקודת אי-רציפות מסוג שני. לכן $x=0$ היא אסימפטוטה אנכית.
**אסימפטוטות משופעות/אופקיות** $y=ax+b$:
$$a=\lim_{x\to\pm\infty}\frac{xe^{\frac1x}}{x}=\lim_{x\to\pm\infty}e^{\frac1x}=1,$$
$$b=\lim_{x\to\pm\infty}\left(xe^{\frac1x}-x\right)=\{\infty-\infty\}=\lim_{t\to0}\left(\frac1te^t-\frac1t\right)=\lim_{t\to0}\frac{e^t-1}{t}=\lim_{t\to0}\frac{e^t}{1}=1$$
לכן $y=x+1$ היא אסימפטוטה משופעת.
**חקירה עם הנגזרת הראשונה:** תחומי עלייה וירידה, נקודות קיצון.
$$f'(x)=\left(xe^{\frac1x}\right)'=e^{\frac1x}-\frac{x}{x^2}e^{\frac1x}=e^{\frac1x}\frac{x-1}{x}$$
טבלת סימנים של $f'$: חיובית ב-$x<0$ (עולה), שלילית ב-$0<x<1$ (יורדת), חיובית ב-$x>1$ (עולה).
נקודת מינימום מקומי: $x=1$, $f(1)=e$.
**תחומי קמירות, נקודות פיתול:**
$$f''(x)=\left(e^{\frac1x}\left(1-\frac1x\right)\right)'=-\frac{1}{x^2}e^{\frac1x}\left(1-\frac1x\right)+e^{\frac1x}\frac{1}{x^2}=e^{\frac1x}\frac{1}{x^2}\left(-1+\frac1x+1\right)=e^{\frac1x}\frac{1}{x^3}$$
טבלת סימנים של $f''$: שלילית ב-$x<0$ (קעורה, $\\cap$), חיובית ב-$x>0$ (קמורה, $\\cup$). אין נקודות פיתול כי $x=0$ אינה בתחום ההגדרה.
סקיצה של הגרף:
![סקיצה של הגרף y = x·exp(1/x) עם האסימפטוטה האנכית x=0, האסימפטוטה המשופעת y=x+1 והמינימום ב-x=1](images/exams/20A-A-Q1-graph.png)
"""

SOL2A = r"""
נציין כי $-1\le\cos 2n\le 1$ והביטוי
$$\lim_{n\to\infty}\frac{n+\sqrt[3]{1-n^6}}{1+n^3}=\lim_{n\to\infty}\frac{\frac{1}{n^2}+\sqrt[3]{\frac{1}{n^9}-\frac{1}{n^3}}}{\frac{1}{n^3}+1}=0$$
לכן
$$\lim_{n\to\infty}\frac{n+\sqrt[3]{1-n^6}}{1+n^3}\cos 2n=0$$
"""

SOL2B = r"""
התנאי שלפונקציה (פולינום) יש משיק אופקי הוא $y'=0$. התנאי שבאותה נקודה לגרף הפונקציה יש פיתול אומר ש-$y''=0$. אז באותה נקודה $x$ מתקיים $3ax^2+2bx+c=0$ ו-$6ax+2b=0$. לכן $x=-\frac{b}{3a}$ ומהצבה נקבל
$$3a\left(-\frac{b}{3a}\right)^2+2b\left(-\frac{b}{3a}\right)+c=0\ \Rightarrow\ -\frac{b^2}{3a}+c=0$$
או $b^2=3ac$.
"""

SOL3A = r"""
$$\lim_{x\to0}(\cos x)^{\frac{1}{\sin^2(2x)}}=\{1^{\infty}\}=\lim_{x\to0}\left(1+\cos x-1\right)^{\frac{1}{\sin^2(2x)}}=$$
$$=\lim_{x\to0}\left(1+\cos x-1\right)^{\frac{1}{\cos x-1}\cdot\frac{\cos x-1}{\sin^2(2x)}}=\lim_{x\to0}\left(1+\cos x-1\right)^{\frac{1}{\cos x-1}\cdot\frac{-2\sin^2\frac{x}{2}}{\sin^2(2x)}}=e^{\frac{-2\cdot\frac14}{4}}=e^{-\frac18}$$
"""

SOL3B = r"""
$$\int\frac{dx}{x\left(\ln^2x-5\ln x+6\right)}=\begin{vmatrix}t=\ln x\\dt=\frac{dx}{x}\end{vmatrix}=\int\frac{dt}{t^2-5t+6}=\int\frac{dt}{(t-2)(t-3)}$$
$$\frac{1}{(t-2)(t-3)}=\frac{A}{t-2}+\frac{B}{t-3}=\frac{A(t-3)+B(t-2)}{(t-2)(t-3)}\ \Rightarrow\ A=-1,\ B=1$$
$$\int\frac{dt}{(t-2)(t-3)}=\int\left(-\frac{1}{t-2}+\frac{1}{t-3}\right)dt=-\ln|t-2|+\ln|t-3|+C=\ln\left|\frac{t-3}{t-2}\right|+C$$
$$\int\frac{dx}{x\left(\ln^2x-5\ln x+6\right)}=\ln\left|\frac{\ln x-3}{\ln x-2}\right|+C$$
"""

SOL4A = r"""
נמצא את הגבולות החד-צדדיים:
$$\lim_{x\to0^-}f(x)=\lim_{x\to0^-}\left(\frac{1}{\sqrt{2-x}-1}-\sqrt{2-x}\right)=\frac{1}{\sqrt2-1}-\sqrt2=\frac{1-\sqrt2\left(\sqrt2-1\right)}{\sqrt2-1}=1$$
$$\lim_{x\to0^+}f(x)=\lim_{x\to0^+}\frac{\sqrt{1+ax}-1+1-\cos x}{x}=\lim_{x\to0^+}\left(\frac{\sqrt{1+ax}-1}{x}+\frac{2\sin^2\frac{x}{2}}{x}\right)=\frac12a+0=\frac{a}{2}$$
הפונקציה תהיה רציפה ב-$x=0$ אם $\frac{a}{2}=1$ ולכן $a=2$.
"""

SOL4B = r"""
נמצא את אורך הקשת לפי הנוסחה: $l=\int_{-2}^{2}\sqrt{1+(y')^2}\,dx$.
$$y'=\frac{e^x-e^{-x}}{2},$$
$$1+(y')^2=1+\left(\frac{e^x-e^{-x}}{2}\right)^2=1+\frac{e^{2x}-2+e^{-2x}}{4}=\frac{e^{2x}+2+e^{-2x}}{4}=\left(\frac{e^x+e^{-x}}{2}\right)^2,$$
$$l=\int_{-2}^{2}\sqrt{1+(y')^2}\,dx=\int_{-2}^{2}\frac{e^x+e^{-x}}{2}\,dx=2\int_{0}^{2}\frac{e^x+e^{-x}}{2}\,dx=\left(e^x-e^{-x}\right)\Big|_0^2=e^2-e^{-2}$$
"""

SOL5A = r"""
נבדוק את הגזירות של $f$ לפי ההגדרה:
$$f'(a)=\lim_{\Delta x\to0}\frac{f(a+\Delta x)-f(a)}{\Delta x}=\lim_{\Delta x\to0}\frac{|a+\Delta x-a|\,g(a+\Delta x)-|a-a|\,g(a)}{\Delta x}=$$
$$=\lim_{\Delta x\to0}\frac{|\Delta x|\,g(a+\Delta x)}{\Delta x}=\lim_{\Delta x\to0}\frac{|\Delta x|}{\Delta x}\,g(a+\Delta x)=0,$$
כי הביטוי $\frac{|\Delta x|}{\Delta x}$ חסום $-1\le\frac{|\Delta x|}{\Delta x}\le1$ ו-$g(a+\Delta x)$ שואף ל-$0$, כי $g(x)$ רציפה.
"""

SOL5B = r"""
$$\int\frac{dx}{\sqrt[4]{x^3}\left(\sqrt{x}+2\sqrt[4]{x}\right)}=\begin{vmatrix}x=t^4\\dx=4t^3dt\end{vmatrix}=\int\frac{4t^3dt}{t^3\left(t^2+2t\right)}=4\int\frac{dt}{t(t+2)},$$
$$\frac{1}{t(t+2)}=\frac{A}{t}+\frac{B}{t+2}=\frac{A(t+2)+Bt}{t(t+2)},\quad A=\frac12,\ B=-\frac12,$$
$$\int\frac{dx}{\sqrt[4]{x^3}\left(\sqrt{x}+2\sqrt[4]{x}\right)}=2\int\left(\frac1t-\frac{1}{t+2}\right)dt=2\left(\ln|t|-\ln|t+2|\right)+C=2\left(\ln\left|\sqrt[4]{x}\right|-\ln\left|\sqrt[4]{x}+2\right|\right)+C=$$
$$=\frac12\ln x-2\ln\left(\sqrt[4]{x}+2\right)+C$$
"""

SOL6A = r"""
תחום ההגדרה של הפונקציה הוא $x\in[2,\infty)$. נחקור את הפונקציה לקיצון מקומי.
$$f'(x)=\frac{1}{2\sqrt{x-2}}e^{-\frac x2}-\frac12\sqrt{x-2}\,e^{-\frac x2}=\frac{1}{2\sqrt{x-2}}e^{-\frac x2}\left(1-x+2\right)=\frac{3-x}{2\sqrt{x-2}}e^{-\frac x2},$$
הנקודה $x=3$ היא נקודת המקסימום המקומי כי $f'(3)=0$ והנגזרת משנה את הסימן במעבר דרך $x=3$ מפלוס למינוס.
"""

SOL6B = r"""
נמצא את נפח הגוף לפי שיטת הפרוסות כאשר $2\le x\le3$. לכן
$$V=\pi\int_2^3(x-2)e^{-x}dx=\begin{vmatrix}u=x-2&du=dx\\dv=e^{-x}dx&v=-e^{-x}\end{vmatrix}=\pi\left(-(x-2)e^{-x}\Big|_2^3+\int_2^3e^{-x}dx\right)=$$
$$=\pi\left(-e^{-3}-e^{-x}\Big|_2^3\right)=\pi\left(e^{-2}-2e^{-3}\right)$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $y=x\cdot e^{\frac{1}{x}}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, נקודות קיצון, "
      "תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1),

    Q(2, "computation", "sequences_limits",
      r"חשבו את הגבול $\lim_{n\to\infty}\frac{n+\sqrt[3]{1-n^6}}{1+n^3}\cos(2n)$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "function_investigation",
      r"נתון כי לפונקציה (פולינום) $y=ax^3+bx^2+cx+d$ כאשר $a\neq0$ יש משיק אופקי ונקודת פיתול עבור אותו ערך של $x$. "
      r"הוכיחו כי מתקיים השוויון $b^2=3ac$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0}(\cos x)^{\frac{1}{\sin^2(2x)}}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{dx}{x\left(\ln^2x-5\ln x+6\right)}$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "continuity",
      r"עבור איזה ערך של הפרמטר $a>0$ הפונקציה "
      r"$f(x)=\begin{cases}\dfrac{1}{\sqrt{2-x}-1}-\sqrt{2-x}, & x\le0\\[2mm] \dfrac{\sqrt{1+ax}-\cos x}{x}, & x>0\end{cases}$"
      " רציפה ב-$x=0$?",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"חשבו את אורך הקשת של העקומה $y=\cosh x$ בתחום $-2\le x\le2$. ניזכר: $\cosh x=\frac{e^x+e^{-x}}{2}$.",
      SOL4B, part="ב", points=10),

    Q(5, "proof", "derivatives_tangents",
      r"נתון כי פונקציה $g(x)$ רציפה ב-$x=a$ ו-$g(a)=0$. הוכיחו כי פונקציה $f(x)=|x-a|\,g(x)$ גזירה ב-$x=a$ ומצאו את $f'(a)$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{dx}{\sqrt[4]{x^3}\left(\sqrt{x}+2\sqrt[4]{x}\right)}$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "extrema_optimization",
      r"נתונה הפונקציה $f(x)=\sqrt{x-2}\,e^{-\frac{x}{2}}$. חקרו את הפונקציה לקיצון מקומי (לוקלי).",
      SOL6A, part="א", points=10),

    Q(6, "computation", "definite_integrals",
      r"נתונה הפונקציה $f(x)=\sqrt{x-2}\,e^{-\frac{x}{2}}$. מצאו את נפח הגוף הנוצר כסיבוב של התחום החסום על ידי גרף הפונקציה, "
      r"ציר ה-$x$ והישר $x=b$ כאשר $x=b$ היא נקודת המקסימום המקומי שמצאתם בסעיף א' סביב ציר ה-$x$.",
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
SYMNAMES = {}  # display names for scratch symbols (filled where they are defined)


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



# ===== Q1: f = x e^(1/x) =====
f1 = x*sp.exp(1/x)
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, sp.exp(1/x)*(x - 1)/x) and same(f1pp, sp.exp(1/x)/x**3)
assert sp.solve(f1p, x) == [1] and f1.subs(x, 1) == sp.E
assert f1p.subs(x, -1) > 0 and f1p.subs(x, R(1, 2)) < 0 and f1p.subs(x, 2) > 0
assert f1pp.subs(x, -1) < 0 and f1pp.subs(x, 1) > 0
assert sp.limit(f1, x, 0, '+') == sp.oo and sp.limit(f1, x, 0, '-') == 0
assert sp.limit(f1/x, x, sp.oo) == 1 and sp.limit(f1 - x, x, sp.oo) == 1 and sp.limit(f1 - x, x, -sp.oo) == 1

add(1,
    rubric=rub((r"תחום הגדרה $x\neq0$ ומיון אי-רציפות ב-$x=0$: הגבול מימין $+\infty$ ומשמאל $0$, ולכן מסוג שני עם אסימפטוטה אנכית", 4),
               (r"אסימפטוטה משופעת $y=x+1$ ב-$\pm\infty$ (חישוב $a=1$, $b=1$)", 4),
               (r"נגזרת $f'(x)=e^{1/x}\frac{x-1}{x}$, טבלת סימנים ומינימום מקומי $f(1)=e$", 5),
               (r"$f''(x)=\frac{e^{1/x}}{x^3}$, קעירות ב-$x<0$ וקמירות ב-$x>0$, ללא נקודות פיתול", 4),
               ("שרטוט הגרף בהתאם לכל הנתונים", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לטעון ש-$x=0$ היא אסימפטוטה אנכית משני הצדדים. משמאל $f(x)\to0$, ורק מימין $f\to+\infty$.",
              r"לחשב את חותך האסימפטוטה בטעות כ-$0$: $\lim\left(xe^{1/x}-x\right)=\lim\frac{e^t-1}{t}=1$ בהצבה $t=\frac1x$.",
              r"לראות בנקודה $x=0$ נקודת פיתול כי $f''$ מחליפה סימן, אף ש-$x=0$ אינה בתחום ההגדרה."],
    steps=[
        chx(r"מהי הנגזרת של $f(x)=xe^{1/x}$?", sp.exp(1/x)*(x - 1)/x,
            [sp.exp(1/x)*(x + 1)/x, sp.exp(1/x)*(x - 1)/x**2, sp.exp(1/x)],
            lambda e: same(e, f1p), r"כלל המכפלה: $f'(x)=e^{1/x}-\frac{1}{x}e^{1/x}=e^{1/x}\frac{x-1}{x}$ (אומת ב-sympy)."),
        num(r"מהו הערך $f(1)$ בנקודת המינימום המקומי? (עשרוני)", f1.subs(x, 1), r"$f(1)=1\cdot e^1=e\approx2.7183$."),
        chx(r"מהי הנגזרת השנייה של $f$?", sp.exp(1/x)/x**3, [sp.exp(1/x)/x**2, -sp.exp(1/x)/x**3, sp.exp(1/x)*(x - 1)/x**3],
            lambda e: same(e, f1pp), r"גוזרים את $f'(x)=e^{1/x}\left(1-\frac{1}{x}\right)$ ומקבלים $f''(x)=\frac{e^{1/x}}{x^3}$, שסימנה כסימן $x$ (אומת ב-sympy)."),
        ch(r"כיצד מתנהגת הפונקציה ליד $x=0$?", r"אי-רציפות מסוג שני: מימין $f\to+\infty$ ומשמאל $f\to0$",
           [r"אי-רציפות סליקה, כי שני הגבולות החד-צדדיים שווים", r"אי-רציפות מסוג ראשון, כי שני הגבולות החד-צדדיים סופיים",
            r"אסימפטוטה אנכית משני הצדדים, כי $f\to\infty$ משני הצדדים"],
           r"$\lim_{x\to0^+}xe^{1/x}=+\infty$ ו-$\lim_{x\to0^-}xe^{1/x}=0$ (אומת ב-sympy)."),
        ch(r"מהי האסימפטוטה המשופעת של $f$ ב-$\pm\infty$?", "$y=x+1$", ["$y=x$", "$y=x-1$", "$y=x+e$"],
           r"$a=\lim e^{1/x}=1$ ו-$b=\lim\left(xe^{1/x}-x\right)=\lim_{t\to0}\frac{e^t-1}{t}=1$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: limit of a sequence times cos(2n) =====
n_ = sp.Symbol('n', positive=True)
rat2 = (n_ - (n_**6 - 1)**R(1, 3))/(1 + n_**3)   # the real cube root of 1-n^6 is -(n^6-1)^(1/3)
assert sp.limit(rat2, n_, sp.oo) == 0
assert abs(float(rat2.subs(n_, 10**6))) < 1e-5

add(2, "א",
    rubric=rub((r"שימוש בחסימות $-1\le\cos2n\le1$", 2),
               (r"חישוב הגבול $\lim\frac{n+\sqrt[3]{1-n^6}}{1+n^3}=0$ באמצעות חלוקה בחזקה הגבוהה", 5),
               (r"מסקנה: מכפלה של סדרה חסומה בסדרה השואפת ל-$0$ שואפת ל-$0$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לטעון שהגבול אינו קיים כי $\cos2n$ אינה מתכנסת. מכפלה בסדרה שואפת ל-$0$ מבטלת את התנודה.",
              r"לחלק ב-$n^3$ ולטעות בפירוק $\sqrt[3]{1-n^6}\sim-n^2$."],
    steps=[
        num(r"מהו גבול הסדרה $\frac{n+\sqrt[3]{1-n^6}}{1+n^3}$?", 0, r"המונה מסדר $n^2$ והמכנה מסדר $n^3$, לכן הגבול $0$ (נבדק ב-sympy)."),
        ch(r"מהו גבול הסדרה $\frac{n+\sqrt[3]{1-n^6}}{1+n^3}\cos(2n)$?", "$0$",
           [r"אינו קיים, כי $\cos2n$ אינה מתכנסת", "$1$", r"קיים ושווה לערך כלשהו בין $-1$ ל-$1$"],
           r"$\left|a_n\cos2n\right|\le|a_n|\to0$, ולכן לפי כלל הסנדוויץ' הגבול הוא $0$."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: b^2 = 3ac =====
a2, b2, c2 = sp.symbols('a b c')
y2 = a2*x**3 + b2*x**2 + c2*x
x0 = sp.solve(sp.diff(y2, x, 2), x)[0]
assert x0 == -b2/(3*a2)
assert same(sp.diff(y2, x).subs(x, x0), c2 - b2**2/(3*a2))
assert sp.solve(sp.Eq(c2 - b2**2/(3*a2), 0), c2) == [b2**2/(3*a2)]
P2 = [r"משיק אופקי אומר $y'=3ax^2+2bx+c=0$, ופיתול אומר $y''=6ax+2b=0$, באותו ערך $x$.",
      r"מ-$6ax+2b=0$ ומ-$a\neq0$ מקבלים $x=-\frac{b}{3a}$.",
      r"מציבים ב-$y'=0$: $3a\cdot\frac{b^2}{9a^2}-\frac{2b^2}{3a}+c=0$, כלומר $-\frac{b^2}{3a}+c=0$.",
      r"מכאן $b^2=3ac$."]
P2b = list(P2)
P2b[1] = r"מ-$6ax+2b=0$ ומ-$a\neq0$ מקבלים $x=-\frac{b}{2a}$."
assert sp.solve(6*a2*x + 2*b2, x) != [-b2/(2*a2)]

add(2, "ב",
    rubric=rub((r"תנאי משיק אופקי $y'=0$ ותנאי פיתול $y''=0$ בנקודה אחת", 3),
               (r"פתרון $y''=0$: $x=-\frac{b}{3a}$ (שימוש ב-$a\neq0$)", 3),
               (r"הצבה ב-$y'=0$ ופישוט עד $c=\frac{b^2}{3a}$", 3),
               (r"מסקנה $b^2=3ac$", 1)),
    rubricSource="ai-verified",
    pitfalls=[r"להשתמש בתנאי $y'=0$ בלבד, בלי התנאי השני $y''=0$ שקובע את $x$.",
              r"לחלק ב-$a$ בלי לציין ש-$a\neq0$, או לטעות במקדם ב-$x=-\frac{b}{3a}$."],
    steps=[
        chx(r"מהו ערך $x$ שבו $y''=6ax+2b$ מתאפסת?", -b2/(3*a2), [-b2/(2*a2), -b2/(6*a2), -2*b2/(3*a2)],
            lambda e: same(e - x0, 0), r"$6ax+2b=0$ נותן $x=-\frac{2b}{6a}=-\frac{b}{3a}$ (אומת ב-sympy)."),
        num(r"עבור $a=2$ ו-$b=6$ מצאו את $c$ המקיים את התנאי של הנקודה.", sp.Rational(6**2, 3*2),
            r"$c=\frac{b^2}{3a}=\frac{36}{6}=6$, כלומר $b^2=3ac$ ($36=3\cdot2\cdot6$)."),
        order("סדרו את שלבי ההוכחה.", P2, "קודם שני התנאים, אחר כך חילוץ $x$ מהתנאי השני, הצבה בראשון ומסקנה. כל שלב נשען על קודמו."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", P2b, 1,
                r"$6ax+2b=0$ נותן $x=-\frac{2b}{6a}=-\frac{b}{3a}$, לא $-\frac{b}{2a}$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: lim (cos x)^(1/sin^2 2x) =====
ex3 = sp.limit((sp.cos(x) - 1)/sp.sin(2*x)**2, x, 0)
assert ex3 == R(-1, 8) and sp.limit(sp.log(sp.cos(x))/sp.sin(2*x)**2, x, 0) == R(-1, 8)
assert abs(float(sp.N(((sp.cos(x))**(1/sp.sin(2*x)**2)).subs(x, R(1, 1000)))) - float(sp.exp(R(-1, 8)))) < 1e-5

add(3, "א",
    rubric=rub((r"זיהוי צורה $1^{\infty}$ ובניית החזקה $\frac{1}{\cos x-1}\cdot\frac{\cos x-1}{\sin^2 2x}$", 4),
               (r"חישוב $\lim\frac{\cos x-1}{\sin^22x}=-\frac18$ (באמצעות $1-\cos x=2\sin^2\frac x2$)", 4),
               (r"מסקנה: הגבול $e^{-1/8}$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לכתוב $1^{\infty}=1$.",
              r"לטעות בקירוב $\sin^22x\approx4x^2$ ולקבל $-\frac{1}{4}$ או $-\frac{1}{2}$ במקום $-\frac18$."],
    steps=[
        ch(r"מהי צורת אי-הוודאות של $\lim_{x\to0}(\cos x)^{\frac{1}{\sin^22x}}$?", r"$1^{\infty}$", [r"$0^0$", r"$\infty^0$", r"$\frac{0}{0}$"],
           r"הבסיס $\cos x\to1$ והחזקה $\frac{1}{\sin^22x}\to\infty$."),
        num(r"מהו $\lim_{x\to0}\frac{\cos x-1}{\sin^22x}$? (עשרוני)", ex3, r"$\cos x-1\approx-\frac{x^2}{2}$ ו-$\sin^22x\approx4x^2$, לכן הגבול $-\frac{1}{8}=-0.125$."),
        num(r"מהו הגבול המבוקש? (עשרוני)", sp.exp(ex3), r"$e^{-1/8}\approx0.8825$."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: int dx / (x (ln^2 x - 5 ln x + 6)) =====
g3b = 1/(x*(sp.log(x)**2 - 5*sp.log(x) + 6))
F3 = sp.log((sp.log(x) - 3)/(sp.log(x) - 2))
assert same(sp.diff(F3, x), g3b)
F3w = [sp.log((sp.log(x) - 2)/(sp.log(x) - 3)), sp.log(sp.log(x) - 3) + sp.log(sp.log(x) - 2), sp.log(sp.log(x)**2 - 5*sp.log(x) + 6)]
A3, B3 = sp.symbols('A B')
s3 = sp.solve(sp.Poly(sp.expand(A3*(t - 3) + B3*(t - 2) - 1), t).all_coeffs(), [A3, B3], dict=True)[0]
assert s3 == {A3: -1, B3: 1}
assert sp.factor(t**2 - 5*t + 6) == (t - 2)*(t - 3)

add(3, "ב",
    rubric=rub((r"הצבה $t=\ln x$, $dt=\frac{dx}{x}$", 3),
               (r"פירוק המכנה $t^2-5t+6=(t-2)(t-3)$ ושברים חלקיים: $A=-1$, $B=1$", 4),
               (r"אינטגרציה וחזרה ל-$x$: $\ln\left|\frac{\ln x-3}{\ln x-2}\right|+C$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לשכוח את $\frac{1}{x}$ שהופך ל-$dt$ ולהשאיר $x$ באינטגרל.",
              r"להחליף את סימני $A$ ו-$B$ ולקבל את ההופכי בתוך הלוגריתם."],
    steps=[
        ch("איזו הצבה משתמש הפתרון הרשמי?", r"$t=\ln x$", [r"$t=x$", r"$t=\ln^2x$", r"$t=\frac{1}{x}$"],
           r"הפתרון הרשמי מציב $t=\ln x$, ולכן $dt=\frac{dx}{x}$ והאינטגרל נהיה $\int\frac{dt}{t^2-5t+6}$."),
        num(r"בפירוק $\frac{1}{(t-2)(t-3)}=\frac{A}{t-2}+\frac{B}{t-3}$, מהו $A$?", s3[A3], r"הצבת $t=2$ ב-$1=A(t-3)+B(t-2)$ נותנת $1=-A$, כלומר $A=-1$."),
        num(r"מהו $B$?", s3[B3], r"הצבת $t=3$ נותנת $1=B$."),
        chx(r"מהי הפונקציה הקדומה (בתחום $\ln x>3$, בלי הקבוע)?", F3, F3w, lambda e: same(sp.diff(e, x), g3b),
            r"$-\ln|t-2|+\ln|t-3|=\ln\left|\frac{t-3}{t-2}\right|$ עם $t=\ln x$. הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: continuity parameter =====
ap = sp.Symbol('a', positive=True)
Lft = sp.limit(1/(sp.sqrt(2 - x) - 1) - sp.sqrt(2 - x), x, 0, '-')
Rgt = sp.limit((sp.sqrt(1 + ap*x) - sp.cos(x))/x, x, 0, '+')
assert sp.simplify(Lft - 1) == 0 and sp.simplify(Rgt - ap/2) == 0 and sp.solve(sp.Eq(ap/2, 1), ap) == [2]

add(4, "א",
    rubric=rub((r"הגבול השמאלי: $\frac{1}{\sqrt2-1}-\sqrt2=1$", 3),
               (r"הגבול הימני: פיצול ל-$\frac{\sqrt{1+ax}-1}{x}+\frac{1-\cos x}{x}$ וחישוב $\frac{a}{2}$", 4),
               (r"השוואה: $\frac{a}{2}=1$ ולכן $a=2$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לשכוח שההגדרה ב-$x=0$ היא מהענף $x\le0$, ולכן גם $f(0)=1$ ולא רק הגבול השמאלי.",
              r"לחשב את $\lim\frac{\sqrt{1+ax}-\cos x}{x}$ בלי פיצול ולקבל $\frac{0}{0}$ בלי לפתור."],
    steps=[
        num(r"מהו הגבול השמאלי $\lim_{x\to0^-}f(x)$?", Lft, r"$\frac{1}{\sqrt2-1}-\sqrt2=\sqrt2+1-\sqrt2=1$ (נבדק ב-sympy)."),
        ch(r"מהו הגבול הימני $\lim_{x\to0^+}\frac{\sqrt{1+ax}-\cos x}{x}$?", r"$\frac{a}{2}$", ["$a$", "$0$", "$2a$"],
           r"$\frac{\sqrt{1+ax}-1}{x}\to\frac{a}{2}$ ו-$\frac{1-\cos x}{x}\to0$ (נבדק ב-sympy עבור $a$ סמלי)."),
        num(r"מהו $a$ שעבורו $f$ רציפה ב-$x=0$?", 2, r"$\frac{a}{2}=1$ נותן $a=2$."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: arc length of cosh =====
ch_ = (sp.exp(x) + sp.exp(-x))/2
sh_ = (sp.exp(x) - sp.exp(-x))/2
assert same(sp.diff(ch_, x), sh_) and same(1 + sh_**2, ch_**2)
len4 = sp.integrate(ch_, (x, -2, 2))
assert sp.simplify(len4 - (sp.exp(2) - sp.exp(-2))) == 0

add(4, "ב",
    rubric=rub((r"נוסחת אורך הקשת $l=\int_{-2}^{2}\sqrt{1+(y')^2}\,dx$ ונגזרת $y'=\frac{e^x-e^{-x}}{2}$", 3),
               (r"$1+(y')^2=\left(\frac{e^x+e^{-x}}{2}\right)^2$ והוצאת שורש", 4),
               (r"אינטגרציה וחישוב $l=e^2-e^{-2}$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"להוציא שורש מ-$\left(\frac{e^x+e^{-x}}{2}\right)^2$ בלי לשים לב שהביטוי חיובי, ולכתוב ערך מוחלט מיותר.",
              r"לשכוח שהקטע הוא $[-2,2]$ ולחשב רק מ-$0$ עד $2$ בלי להכפיל ב-$2$ (הפונקציה זוגית)."],
    steps=[
        chx(r"מהו $1+(y')^2$ עבור $y=\frac{e^x+e^{-x}}{2}$?", ch_**2, [sh_**2, ch_, 1 + sh_],
            lambda e: same(e, 1 + sh_**2), r"$1+\frac{e^{2x}-2+e^{-2x}}{4}=\frac{e^{2x}+2+e^{-2x}}{4}=\left(\frac{e^x+e^{-x}}{2}\right)^2$ (אומת ב-sympy)."),
        num(r"מהו אורך הקשת? (עשרוני)", len4, r"$\int_{-2}^{2}\frac{e^x+e^{-x}}{2}dx=e^2-e^{-2}\approx7.2537$."),
    ],
    stepsSource="ai-verified")

# ===== Q5a: differentiability of |x-a| g(x) =====
hh = sp.Symbol('h', real=True)
assert sp.limit(sp.Abs(hh)/hh, hh, 0, '+') == 1 and sp.limit(sp.Abs(hh)/hh, hh, 0, '-') == -1
assert sp.limit(sp.Abs(hh)*hh/hh, hh, 0) == 0
Q5 = [r"מההגדרה $f'(a)=\lim_{\Delta x\to0}\frac{f(a+\Delta x)-f(a)}{\Delta x}$, ומתקיים $f(a)=|0|\cdot g(a)=0$.",
      r"לכן $\frac{f(a+\Delta x)-f(a)}{\Delta x}=\frac{|\Delta x|}{\Delta x}\,g(a+\Delta x)$.",
      r"הגורם $\frac{|\Delta x|}{\Delta x}$ חסום בין $-1$ ל-$1$, ו-$g(a+\Delta x)\to g(a)=0$ כי $g$ רציפה ב-$a$.",
      r"מכפלה של חסום בשואף ל-$0$ שואפת ל-$0$, ולכן $f$ גזירה ב-$a$ ו-$f'(a)=0$."]
Q5b = list(Q5)
Q5b[1] = r"לכן $\frac{f(a+\Delta x)-f(a)}{\Delta x}=\frac{|\Delta x|}{\Delta x}\,g(a)$."

add(5, "א",
    rubric=rub((r"שימוש בהגדרת הנגזרת וחישוב $f(a)=0$", 2),
               (r"פישוט מנת ההפרשים ל-$\frac{|\Delta x|}{\Delta x}g(a+\Delta x)$", 3),
               (r"נימוק: הגורם הראשון חסום והשני שואף ל-$0$ (רציפות $g$ ו-$g(a)=0$)", 3),
               (r"מסקנה: $f$ גזירה ו-$f'(a)=0$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לטעון ש-$|x-a|$ אינה גזירה ב-$a$ ולכן גם המכפלה אינה גזירה. כאן הגורם $g(x)$ מתאפס ב-$a$.",
              r"לחשב את הגבול של $\frac{|\Delta x|}{\Delta x}$ בנפרד ולטעון שהוא לא קיים, בלי להשתמש בכך שהוא חסום."],
    steps=[
        ch(r"מה ידוע על $\frac{|\Delta x|}{\Delta x}$ כאשר $\Delta x\to0$?", r"אין לו גבול (הוא $1$ מימין ו-$-1$ משמאל), אך הוא חסום",
           [r"הגבול שלו הוא $1$", r"הגבול שלו הוא $0$", r"הוא אינו חסום"],
           r"הביטוי שווה $1$ עבור $\Delta x>0$ ו-$-1$ עבור $\Delta x<0$ (נבדק ב-sympy), ולכן חסום ללא גבול."),
        order("סדרו את שלבי ההוכחה.", Q5, "קודם ההגדרה ו-$f(a)$, אחר כך פישוט מנת ההפרשים, אחר כך נימוק הגבול ולבסוף המסקנה. כל שלב נשען על קודמו."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", Q5b, 1,
                r"$f(a+\Delta x)=|\Delta x|\,g(a+\Delta x)$ ולכן הגורם הוא $g(a+\Delta x)$ ולא $g(a)$ (שהוא $0$ ומוחק את כל הביטוי בלי הצדקה)."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: integral with fourth root =====
tp = sp.Symbol('tp', positive=True)
xp = sp.Symbol('xp', positive=True)
SYMNAMES.update({tp: "t", xp: "x"})
integrand5 = 1/(xp**R(3, 4)*(sp.sqrt(xp) + 2*xp**R(1, 4)))
sub5 = sp.simplify(integrand5.subs(xp, tp**4)*sp.diff(tp**4, tp))
assert same(sub5, 4/(tp*(tp + 2)))
A5, B5 = sp.symbols('A B')
s5 = sp.solve(sp.Poly(sp.expand(A5*(tp + 2) + B5*tp - 1), tp).all_coeffs(), [A5, B5], dict=True)[0]
assert s5 == {A5: R(1, 2), B5: R(-1, 2)}
F5 = sp.log(xp)/2 - 2*sp.log(xp**R(1, 4) + 2)
assert same(sp.diff(F5, xp), integrand5)
F5w = [sp.log(xp) - 2*sp.log(xp**R(1, 4) + 2), sp.log(xp)/2 + 2*sp.log(xp**R(1, 4) + 2), sp.log(xp)/2 - 2*sp.log(sp.sqrt(xp) + 2)]

add(5, "ב",
    rubric=rub((r"הצבה $x=t^4$, $dx=4t^3dt$", 3),
               (r"פישוט האינטגרנד ל-$\frac{4}{t(t+2)}$ ופירוק לשברים חלקיים ($A=\frac12$, $B=-\frac12$)", 4),
               (r"אינטגרציה וחזרה ל-$x$: $\frac12\ln x-2\ln\left(\sqrt[4]{x}+2\right)+C$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לבחור הצבה שאינה מבטלת את כל השורשים בבת אחת (למשל $t=\sqrt{x}$ בלבד); הדרוש הוא $x=t^4$.",
              r"לשכוח את הגורם $4t^3$ של $dx$ או את הגורם $4$ בפירוק."],
    steps=[
        ch("איזו הצבה משתמש הפתרון הרשמי?", r"$x=t^4$", [r"$x=t^2$", r"$t=\ln x$", r"$x=t^3$"],
           r"הפתרון הרשמי מציב $x=t^4$ כך שגם $\sqrt{x}=t^2$ וגם $\sqrt[4]{x}=t$ הופכים לחזקות שלמות."),
        chx(r"מהו האינטגרנד אחרי ההצבה $x=t^4$ (כולל $dx=4t^3dt$)?", 4/(tp*(tp + 2)), [1/(tp*(tp + 2)), 4/(tp**2*(tp + 2)), 4*tp/(tp + 2)],
            lambda e: same(e, sub5), r"$\frac{4t^3}{t^3\left(t^2+2t\right)}=\frac{4}{t(t+2)}$ (אומת ב-sympy)."),
        num(r"בפירוק $\frac{1}{t(t+2)}=\frac{A}{t}+\frac{B}{t+2}$, מהו $A$?", s5[A5], r"הצבת $t=0$ ב-$1=A(t+2)+Bt$ נותנת $1=2A$, כלומר $A=\frac12$."),
        chx(r"מהי הפונקציה הקדומה (בתחום $x>0$, בלי הקבוע)?", F5, F5w, lambda e: same(sp.diff(e, xp), integrand5),
            r"$2\left(\ln t-\ln(t+2)\right)=\frac12\ln x-2\ln\left(\sqrt[4]{x}+2\right)$; הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: local extremum of sqrt(x-2) e^(-x/2) =====
f6 = sp.sqrt(x - 2)*sp.exp(-x/2)
f6p = sp.diff(f6, x)
assert same(f6p, (3 - x)/(2*sp.sqrt(x - 2))*sp.exp(-x/2))
assert sp.solve(f6p, x) == [3]
assert f6p.subs(x, R(5, 2)) > 0 and f6p.subs(x, 4) < 0
assert abs(float(f6.subs(x, 3)) - float(sp.exp(R(-3, 2)))) < 1e-12

add(6, "א",
    rubric=rub((r"תחום הגדרה $x\ge2$", 1),
               (r"נגזרת $f'(x)=\frac{3-x}{2\sqrt{x-2}}e^{-x/2}$", 4),
               (r"הנקודה הקריטית $x=3$ ובדיקת סימן הנגזרת משני צדיה", 3),
               (r"מסקנה: מקסימום מקומי ב-$x=3$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לשכוח את תחום ההגדרה $x\ge2$ ולבדוק נקודות מחוץ אליו.",
              r"לטעות בכיוון החלפת הסימן: $f'>0$ לפני $x=3$ ו-$f'<0$ אחריה, כלומר מקסימום ולא מינימום."],
    steps=[
        chx(r"מהי הנגזרת של $f(x)=\sqrt{x-2}\,e^{-x/2}$?", (3 - x)/(2*sp.sqrt(x - 2))*sp.exp(-x/2),
            [(x - 3)/(2*sp.sqrt(x - 2))*sp.exp(-x/2), (3 - x)/(2*sp.sqrt(x - 2))*sp.exp(x/2), (3 - x)/sp.sqrt(x - 2)*sp.exp(-x/2)],
            lambda e: same(e, f6p), r"כלל המכפלה: $\frac{e^{-x/2}}{2\sqrt{x-2}}-\frac{\sqrt{x-2}}{2}e^{-x/2}=\frac{(3-x)e^{-x/2}}{2\sqrt{x-2}}$ (אומת ב-sympy)."),
        num(r"מהי הנקודה הקריטית של $f$ בתחום $x>2$?", 3, r"$3-x=0$ נותן $x=3$."),
        ch(r"איך משתנה סימן $f'$ במעבר דרך $x=3$ ומה סוג הקיצון?", r"מחיובי לשלילי, ולכן מקסימום מקומי",
           [r"משלילי לחיובי, ולכן מינימום מקומי", r"מחיובי לשלילי, ולכן מינימום מקומי", r"אינו משתנה, ולכן אין קיצון"],
           r"עבור $2<x<3$ נקבל $f'>0$ ועבור $x>3$ נקבל $f'<0$ (נבדק ב-sympy), כלומר מקסימום מקומי."),
        num(r"מהו הערך $f(3)$? (עשרוני)", f6.subs(x, 3), r"$f(3)=\sqrt1\cdot e^{-3/2}=e^{-1.5}\approx0.2231$."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: solid of revolution =====
sq6 = f6**2
assert same(sq6, (x - 2)*sp.exp(-x))
G6 = -(x - 1)*sp.exp(-x)
assert same(sp.diff(G6, x), (x - 2)*sp.exp(-x))
G6w = [(x - 1)*sp.exp(-x), -(x - 2)*sp.exp(-x), -x*sp.exp(-x)]
V6int = sp.integrate((x - 2)*sp.exp(-x), (x, 2, 3))
assert sp.simplify(V6int - (sp.exp(-2) - 2*sp.exp(-3))) == 0
V6 = sp.pi*V6int

add(6, "ב",
    rubric=rub((r"נוסחת הנפח $V=\pi\int_2^3f^2(x)\,dx$ והגבולות $2\le x\le3$", 3),
               (r"פישוט $f^2(x)=(x-2)e^{-x}$ ואינטגרציה בחלקים", 4),
               (r"הצבת הגבולות: $V=\pi\left(e^{-2}-2e^{-3}\right)$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לשכוח את ההעלאה בריבוע ולחשב $\pi\int f\,dx$.",
              r"להשתמש בגבולות לא נכונים: התחום מתחיל ב-$x=2$ (קצה תחום ההגדרה) ונגמר ב-$x=3$."],
    steps=[
        chx(r"מהו $f^2(x)$ עבור $f(x)=\sqrt{x-2}\,e^{-x/2}$?", (x - 2)*sp.exp(-x), [sp.sqrt(x - 2)*sp.exp(-x), (x - 2)*sp.exp(-x/2), (x - 2)**2*sp.exp(-x)],
            lambda e: same(e, sq6), r"$f^2=(x-2)e^{-x}$ (אומת ב-sympy)."),
        chx(r"מהי פונקציה קדומה של $(x-2)e^{-x}$?", G6, G6w, lambda e: same(sp.diff(e, x), (x - 2)*sp.exp(-x)),
            r"באינטגרציה בחלקים: $-(x-2)e^{-x}-e^{-x}=-(x-1)e^{-x}$. הנגזרת של כל אפשרות נבדקה ב-sympy."),
        num(r"מהו $\int_2^3(x-2)e^{-x}dx$? (עשרוני)", V6int, r"$G(3)-G(2)=-2e^{-3}+e^{-2}\approx0.0358$."),
        num(r"מהו הנפח $V=\pi\int_2^3(x-2)e^{-x}dx$? (עשרוני)", V6, r"$V=\pi\left(e^{-2}-2e^{-3}\right)\approx0.1123$."),
    ],
    stepsSource="ai-verified")

exam = {
    "examCode": "20A-A",
    "examLabel": "מבחן סוף סמסטר א' תש\"פ, מועד א'",
    "year": 2020,
    "examDate": "20/02/2020",
    "sourceFile": "calculus-1/20A-A exam+solution.pdf",
    "solutionFile": "calculus-1/20A-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

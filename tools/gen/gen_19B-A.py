# -*- coding: utf-8 -*-
"""Generator for tools/raw/19B-A.json -- calculus-1 (20151), semester A 2019, moed B (27/03/2019).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_19B-A.py

Source: sitting 19B-A, pp.1-7 (typed exam with the official worked solution after every question).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Figures inside solutions: Q1 graph (p.2), Q6a region (p.7), Q6b region (p.7).
- The Q1 solution is the printed text; its sign tables are given in words.

Checks (tools/verify/19B-A/check.py, sympy): every derivative, limit, asymptote, partial-fraction coefficient,
antiderivative, tangent line, volume and area matches the official answer. 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "19B-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
$$f(x)=\frac{2x^2}{x^2-1}=2+\frac{2}{x^2-1}$$
**תחום ההגדרה:** $(-\infty,-1)\cup(-1,1)\cup(1,+\infty)$.
**אסימפטוטה אנכית** $x=1$:
$$\lim_{x\to1^+}\frac{2x^2}{x^2-1}=\left[\frac{2}{0^+}\right]=+\infty,\qquad\lim_{x\to1^-}\frac{2x^2}{x^2-1}=\left[\frac{2}{0^-}\right]=-\infty$$
**אסימפטוטה אנכית** $x=-1$:
$$\lim_{x\to-1^+}\frac{2x^2}{x^2-1}=\left[\frac{2}{0^-}\right]=-\infty,\qquad\lim_{x\to-1^-}\frac{2x^2}{x^2-1}=\left[\frac{2}{0^+}\right]=+\infty$$
**אסימפטוטה אופקית** ב-$+\infty$ וב-$-\infty$: $y=2$:
$$\lim_{x\to\pm\infty}\frac{2x^2}{x^2-1}=\lim_{x\to\pm\infty}\left(2+\frac{2}{x^2-1}\right)=\left[2+\frac{2}{+\infty}\right]=2$$
$$f'(x)=\left(2+\frac{2}{x^2-1}\right)'=\frac{-4x}{\left(x^2-1\right)^2}$$
תחומי עלייה: $(-\infty,-1),(-1,0)$. תחומי ירידה: $(0,1),(1,+\infty)$. נקודת מקסימום מקומי: $x=0$, $f(0)=0$.
$$f''(x)=\left(\frac{-4x}{\left(x^2-1\right)^2}\right)'=\frac{-4\left(x^2-1\right)^2+4x\cdot2\left(x^2-1\right)2x}{\left(x^2-1\right)^4}=\frac{4\left(-x^2+1+4x^2\right)}{\left(x^2-1\right)^3}=\frac{4\left(3x^2+1\right)}{\left(x^2-1\right)^3}$$
קמורה ב: $(-\infty,-1),(1,+\infty)$. קעורה ב: $(-1,1)$. אין נקודת פיתול.
![גרף הפונקציה y = 2x²/(x²−1) עם האסימפטוטות x=1, x=−1, y=2 והמקסימום ב-(0,0)](images/exams/19B-A-Q1-graph.png)
"""

SOL2A = r"""
סדרה $\{a_n\}_{n=1}^\infty$ חסומה מלמטה כי $a_n>3$ לכל $n\in\mathbb{N}$.
הוכחה על ידי אינדוקציה מתמטית: $n=1$: $a_1=4>3$. נניח ש-$a_k>3$. יש להוכיח ש-$a_{k+1}>3$.
$$a_{k+1}=\sqrt{5a_k-6}>\sqrt{5\cdot3-6}=3$$
סדרה $\{a_n\}_{n=1}^\infty$ מונוטונית יורדת:
$$a_{n+1}-a_n=\sqrt{5a_n-6}-a_n=\frac{5a_n-6-a_n^2}{\sqrt{5a_n-6}+a_n}=-\frac{(a_n-2)(a_n-3)}{\sqrt{5a_n-6}+a_n}<0$$
כי $a_n>3$. אז סדרה $\{a_n\}_{n=1}^\infty$ מונוטונית יורדת.
סדרה $\{a_n\}_{n=1}^\infty$ מונוטונית יורדת וחסומה מלמטה, אז $\{a_n\}_{n=1}^\infty$ מתכנסת. ז"א קיים $L\ge3$ כך ש-$L=\lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}a_n$.
$$L=\lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}\sqrt{5a_n-6}=\sqrt{5L-6}\ \Rightarrow\ L=\sqrt{5L-6}$$
$$L^2-5L+6=0,\ L\ge3\ \Rightarrow\ L=3$$
"""

SOL2B = r"""
נניח ש-$f(x)=x^3+x+e^x$, המשוואה $f(x)=0$ היא שקולה למשוואה הנתונה.
$$f(-1)=(-1)^3+(-1)+e^{(-1)}=-2+\frac1e<-2+1=-1<0$$
$$f(0)=0^3+0+e^0=1>0$$
$f(x)$ רציפה ב-$[-1,0]$ ו-$f(-1)\cdot f(0)<0$, אז לפי משפט על ערך הביניים קיים $c\in(-1,0)$ כך ש-$f(c)=0$. ז"א למשוואה הנתונה קיים פתרון $x=c$.
$f'(x)=\left(x^3+x+e^x\right)'=3x^2+1+e^x$. אז $f'(x)>0$ ב-$(-\infty,+\infty)$, ז"א $f(x)$ מונוטונית עולה ממש ב-$(-\infty,+\infty)$. קיבלנו ש-$f(x)$ חח"ע ב-$(-\infty,+\infty)$. אז $f(x)=0$ רק כאשר $x=c$.
ז"א למשוואה הנתונה קיים פתרון אחד בלבד $x=c$.
"""

SOL3A = r"""
$$\lim_{x\to+\infty}\left(1+e^x\right)^{\frac1x}=\left[\infty^0\right]=\lim_{x\to+\infty}e^{\frac1x\ln\left(1+e^x\right)}$$
$$\lim_{x\to+\infty}\frac1x\ln\left(1+e^x\right)=\lim_{x\to+\infty}\frac{\ln\left(1+e^x\right)}{x}=\left[\frac{\infty}{\infty}\right]=\lim_{x\to+\infty}\frac{\left(\ln\left(1+e^x\right)\right)'}{(x)'}=$$
$$=\lim_{x\to+\infty}\frac{\frac{e^x}{1+e^x}}{1}=\lim_{x\to+\infty}\frac{e^x}{1+e^x}=\lim_{x\to+\infty}\frac{1}{e^{-x}+1}=\frac{1}{0+1}=1$$
$$\lim_{x\to+\infty}\left(1+e^x\right)^{\frac1x}=e^1=e$$
"""

SOL3B = r"""
$$\int\arcsin x\,dx=\left[u=\arcsin x,\ v'=1\Rightarrow u'=\frac{1}{\sqrt{1-x^2}},\ v=x\right]=$$
$$=x\arcsin x-\int\frac{x}{\sqrt{1-x^2}}\,dx=x\arcsin x+\frac12\int\frac{\left(1-x^2\right)'}{\sqrt{1-x^2}}\,dx=x\arcsin x+\sqrt{1-x^2}+C$$
"""

SOL4A = r"""
הפונקציה רציפה ב-$x=0$, אם $\lim_{x\to0^-}g(x)=\lim_{x\to0^+}g(x)=g(0)$.
$$\lim_{x\to0^-}g(x)=\lim_{x\to0^-}\left(\ln\left(a+x^2\right)\right)^2=(\ln a)^2,\qquad g(0)=(\ln a)^2$$
$$\lim_{x\to0^+}g(x)=\lim_{x\to0^+}\ln\left(a+e^{-\frac1x}\right)=\ln a$$
$$(\ln a)^2=\ln a\ \Rightarrow\ (\ln a)^2-\ln a=0\ \Rightarrow\ \ln a(\ln a-1)=0$$
ז"א $\ln a=0$ או $\ln a=1$ ז"א $a=1$ או $a=e$.
אם $x\in(-\infty,0)$, $g(x)=\ln^2\left(a+x^2\right)$ רציפה כפונקציה אלמנטרית.
אם $x\in(0,+\infty)$, $g(x)=\ln\left(a+e^{-\frac1x}\right)$ רציפה כפונקציה אלמנטרית.
אז הפונקציה $g(x)$ רציפה ב-$\mathbb{R}$ עבור $a=1$ או $a=e$.
"""

SOL4B = r"""
$$y=1\cdot x-7\ \Rightarrow\ f'(x_0)=1\ \Rightarrow\ \frac{2x_0}{1+x_0^2}=1\ \Rightarrow\ x_0=1,\quad f(1)=\ln2$$
$$y=f(1)+f'(1)(x-1)\ \Rightarrow\ y=\ln2+(x-1)\ \Rightarrow\ y=x+(\ln2-1)$$
משוואת המשיק לגרף של הפונקציה היא $y=x+(\ln2-1)$.
"""

SOL5A = r"""
$$\lim_{x\to-\infty}\left(\sqrt{2+2x+x^2}-\sqrt{2-2x+x^2}\right)=\lim_{x\to-\infty}\frac{2+2x+x^2-2+2x-x^2}{\sqrt{2+2x+x^2}+\sqrt{2-2x+x^2}}=$$
$$=\lim_{x\to-\infty}\frac{4x}{\sqrt{2+2x+x^2}+\sqrt{2-2x+x^2}}=\lim_{x\to-\infty}\frac{4x}{|x|\left(\sqrt{\frac{2}{x^2}+\frac2x+1}+\sqrt{\frac{2}{x^2}-\frac2x+1}\right)}=$$
$$=\lim_{x\to-\infty}\frac{4}{-\left(\sqrt{\frac{2}{x^2}+\frac2x+1}+\sqrt{\frac{2}{x^2}-\frac2x+1}\right)}=\frac{4}{-\left(\sqrt1+\sqrt1\right)}=-2$$
"""

SOL5B = r"""
$$\frac{x}{\left(x^2+1\right)(x+1)}=\frac{A}{x+1}+\frac{Bx+C}{x^2+1}=\frac{A\left(x^2+1\right)+(Bx+C)(x+1)}{\left(x^2+1\right)(x+1)}$$
$$x=A\left(x^2+1\right)+(Bx+C)(x+1)=(A+B)x^2+(B+C)x+(A+C)$$
$$(A+B)=0,\ (B+C)=1,\ (A+C)=0\ \Rightarrow\ A=-\frac12,\ B=\frac12,\ C=\frac12$$
$$\int\frac{x}{\left(x^2+1\right)(x+1)}dx=\int\left(\frac{-\frac12}{x+1}+\frac{\frac12x+\frac12}{x^2+1}\right)dx=$$
$$=-\frac12\int\frac{1}{x+1}dx+\frac14\int\frac{2x}{x^2+1}dx+\frac12\int\frac{1}{x^2+1}dx=-\frac12\ln|x+1|+\frac14\ln\left(x^2+1\right)+\frac12\arctan x+C$$
"""

SOL6A = r"""
$$V=\pi\int_0^{\frac\pi2}\left(\left(\frac\pi2-x\right)^2-(\cos x)^2\right)dx=\pi\int_0^{\frac\pi2}\left(\left(x-\frac\pi2\right)^2-\frac12-\frac12\cos2x\right)dx=$$
$$=\pi\left(-\frac13\left(\frac\pi2-x\right)^3-\frac12x-\frac14\sin2x\right)\Bigg|_0^{\frac\pi2}=\pi\left(-\frac12\cdot\frac\pi2+\frac13\left(\frac\pi2\right)^3\right)=\frac{\pi^2}{4}\left(-1+\frac16\pi^2\right)$$
![התחום הכלוא בין y = cos x לבין הישר y = π/2 − x וציר ה-y, שמסתובב סביב ציר ה-x](images/exams/19B-A-Q6a-fig.png)
"""

SOL6B = r"""
$$S=\int_{-2}^{2}\sqrt{x+2}\,dx-\int_0^2\sqrt{2x}\,dx=\left(\frac23(x+2)^{\frac32}\right)\Bigg|_{-2}^{2}-\sqrt2\left(\frac23(x)^{\frac32}\right)\Bigg|_0^2=$$
$$=\frac23(4)^{\frac32}-\sqrt2\,\frac23(2)^{\frac32}=\frac23(8-4)=\frac83$$
![התחום הכלוא בין y = √(x+2), y = √(2x) וציר ה-x](images/exams/19B-A-Q6b-fig.png)
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $y=\frac{2x^2}{x^2-1}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, נקודות קיצון, "
      "תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1),

    Q(2, "proof", "sequences_limits",
      r"הוכיחו כי הסדרה $a_{n+1}=\sqrt{5a_n-6},\quad a_1=4$ מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "continuity",
      r"הוכח כי למשוואה $x^3+e^x=-x$ קיים פתרון אחד בלבד.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to+\infty}\left(1+e^x\right)^{\frac{1}{x}}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\arcsin x\,dx$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "continuity",
      r"נתונה הפונקציה $g(x)=\begin{cases}\ln\left(a+e^{-\frac1x}\right), & x>0\\[2mm] \ln^2\left(a+x^2\right), & x\le0\end{cases}$"
      r", כאשר $a>0$. עבור אילו ערכי $a$ הפונקציה $g$ רציפה ב-$\mathbb{R}$?",
      SOL4A, part="א", points=10),

    Q(4, "computation", "derivatives_tangents",
      r"מצאו את משוואת המשיק לגרף של הפונקציה $f(x)=\ln\left(1+x^2\right)$ המקביל לישר $x-y=7$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to-\infty}\left(\sqrt{2+2x+x^2}-\sqrt{2-2x+x^2}\right)$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{x}{\left(x^2+1\right)(x+1)}\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "definite_integrals",
      r"מצאו את נפח הגוף, הנוצר על-ידי סיבוב סביב ציר ה-$X$ של התחום הכלוא בין הקווים הבאים: "
      r"$y=\cos x,\ y=\frac\pi2-x$ כאשר $0\le x\le\frac\pi2$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "definite_integrals",
      r"חשבו את השטח הכלוא בין הקווים הבאים: $y=\sqrt{x+2},\ y=\sqrt{2x}$ ו-$y=0$.",
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



# ===== Q1: f = 2x^2/(x^2-1) =====
f1 = 2*x**2/(x**2 - 1)
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1, 2 + 2/(x**2 - 1)) and same(f1p, -4*x/(x**2 - 1)**2) and same(f1pp, 4*(3*x**2 + 1)/(x**2 - 1)**3)
assert sp.solve(f1p, x) == [0] and f1.subs(x, 0) == 0
assert f1p.subs(x, R(-1, 2)) > 0 and f1p.subs(x, -3) > 0 and f1p.subs(x, R(1, 2)) < 0 and f1p.subs(x, 3) < 0
assert f1pp.subs(x, 0) < 0 and f1pp.subs(x, 3) > 0 and f1pp.subs(x, -3) > 0
assert sp.limit(f1, x, 1, '+') == sp.oo and sp.limit(f1, x, 1, '-') == -sp.oo
assert sp.limit(f1, x, -1, '+') == -sp.oo and sp.limit(f1, x, -1, '-') == sp.oo
assert sp.limit(f1, x, sp.oo) == 2 and sp.limit(f1, x, -sp.oo) == 2

add(1,
    rubric=rub((r"תחום הגדרה $x\neq\pm1$ וכתיבה $f(x)=2+\frac{2}{x^2-1}$", 2),
               (r"אסימפטוטות אנכיות $x=1$, $x=-1$ (גבולות חד-צדדיים) ואופקית $y=2$", 5),
               (r"נגזרת $f'(x)=\frac{-4x}{(x^2-1)^2}$, תחומי עליה וירידה ומקסימום מקומי $f(0)=0$", 5),
               (r"$f''(x)=\frac{4(3x^2+1)}{(x^2-1)^3}$, קמירות וקעירות וקביעה שאין נקודות פיתול", 5),
               ("שרטוט הגרף בהתאם לכל הנתונים", 3)),
    rubricSource="ai-draft",
    pitfalls=[r"לקבוע נקודת פיתול רק כי $f''$ מחליפה סימן ב-$x=\pm1$. הנקודות האלה אינן בתחום ההגדרה.",
              r"לשכוח שהסימן של $f'$ ושל $f''$ נקבע גם לפי המכנה: הנגזרת עולה ב-$(-\infty,-1)$ וב-$(-1,0)$ ויורדת ב-$(0,1)$ וב-$(1,\infty)$.",
              r"לבלבל בין הגבול ב-$1^+$ ($+\infty$) לבין הגבול ב-$1^-$ ($-\infty$) ולשרטט את הענפים הפוך."],
    steps=[
        chx(r"מהי הנגזרת של $f(x)=\frac{2x^2}{x^2-1}$?", -4*x/(x**2 - 1)**2, [4*x/(x**2 - 1)**2, -4*x/(x**2 - 1), -2*x/(x**2 - 1)**2],
            lambda e: same(e, f1p), r"בכתיבה $f=2+\frac{2}{x^2-1}$ מקבלים $f'=-\frac{2\cdot2x}{(x^2-1)^2}=\frac{-4x}{(x^2-1)^2}$ (אומת ב-sympy)."),
        ch(r"מהם תחומי העלייה והירידה וסוג הקיצון?", r"עולה ב-$(-\infty,-1)$ וב-$(-1,0)$, יורדת ב-$(0,1)$ וב-$(1,\infty)$; מקסימום מקומי ב-$x=0$",
           [r"יורדת ב-$(-\infty,-1)$ וב-$(-1,0)$, עולה ב-$(0,1)$ וב-$(1,\infty)$; מינימום מקומי ב-$x=0$",
            r"עולה ב-$(-\infty,0)$ כולל $x=-1$, יורדת ב-$(0,\infty)$; מקסימום מקומי ב-$x=0$", r"עולה בכל תחום ההגדרה; אין קיצון"],
           r"סימן $f'$ הוא סימן $-x$ (המכנה חיובי), ולכן $f'>0$ עבור $x<0$ ו-$f'<0$ עבור $x>0$ (נבדק ב-sympy), עם מקסימום ב-$x=0$."),
        num(r"מהו הערך $f(0)$ בנקודת המקסימום המקומי?", 0, r"$f(0)=\frac{0}{-1}=0$."),
        chx(r"מהי הנגזרת השנייה של $f$?", 4*(3*x**2 + 1)/(x**2 - 1)**3, [4*(3*x**2 - 1)/(x**2 - 1)**3, 4*(3*x**2 + 1)/(x**2 - 1)**2, 12*x/(x**2 - 1)**3],
            lambda e: same(e, f1pp), r"גוזרים את $\frac{-4x}{(x^2-1)^2}$ בכלל המנה ומקבלים $\frac{4(3x^2+1)}{(x^2-1)^3}$ (אומת ב-sympy)."),
        ch("מהן האסימפטוטות של הגרף?", r"אנכיות $x=1$ ו-$x=-1$, ואופקית $y=2$ ב-$\pm\infty$",
           [r"אנכית $x=1$ בלבד, ואופקית $y=2$", r"אנכיות $x=\pm1$ ואופקית $y=0$", r"אנכיות $x=\pm1$ ואסימפטוטה משופעת"],
           r"$\lim_{x\to\pm1}|f|=\infty$ ו-$\lim_{x\to\pm\infty}f=2$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q2a: a_{n+1} = sqrt(5 a_n - 6), a_1 = 4 =====
aa = sp.Symbol('aa', positive=True)
sq = sp.sqrt(5*aa - 6)
assert same(sq - aa, -(aa - 2)*(aa - 3)/(sq + aa))
seq2 = [sp.Integer(4)]
for _ in range(300):
    seq2.append(sp.N(sp.sqrt(5*seq2[-1] - 6), 40))
assert all(seq2[i] > seq2[i + 1] > 3 for i in range(100)) and abs(float(seq2[-1]) - 3) < 1e-9
assert sp.simplify(sp.sqrt(5*4 - 6) - sp.sqrt(14)) == 0
assert set(sp.solve(sp.Eq(Lx := sp.Symbol('L'), sp.sqrt(5*Lx - 6)), Lx)) == {2, 3} or sp.solve(sp.Eq(Lx, sp.sqrt(5*Lx - 6)), Lx) == [2, 3]
S2 = [r"נוכיח באינדוקציה ש-$a_n>3$: עבור $n=1$ מתקיים $a_1=4>3$.",
      r"אם $a_k>3$ אז $a_{k+1}=\sqrt{5a_k-6}>\sqrt{5\cdot3-6}=3$.",
      r"$a_{n+1}-a_n=-\frac{(a_n-2)(a_n-3)}{\sqrt{5a_n-6}+a_n}<0$ כי $a_n>3$, ולכן הסדרה יורדת.",
      r"סדרה יורדת וחסומה מלמטה מתכנסת, ונסמן את גבולה ב-$L\ge3$.",
      r"מנוסחת הנסיגה $L=\sqrt{5L-6}$, כלומר $L^2-5L+6=0$. מ-$L\ge3$ נקבל $L=3$."]
S2b = list(S2)
S2b[4] = r"מנוסחת הנסיגה $L=\sqrt{5L-6}$, כלומר $L^2-5L+6=0$. נקבל $L=2$."

add(2, "א",
    rubric=rub((r"הוכחה באינדוקציה ש-$a_n>3$ (בסיס וצעד)", 3),
               (r"הצגת $a_{n+1}-a_n=-\frac{(a_n-2)(a_n-3)}{\sqrt{5a_n-6}+a_n}<0$ ומסקנה שהסדרה יורדת", 3),
               (r"התכנסות (מונוטונית וחסומה) והגדרת הגבול $L\ge3$", 1),
               (r"מעבר לגבול: $L^2-5L+6=0$ ובחירה נכונה $L=3$", 3)),
    rubricSource="ai-draft",
    pitfalls=[r"לבחור $L=2$ בלי להשתמש בחסימה $L\ge3$ שבאה מהאינדוקציה.",
              r"להכפיל בצמוד בלי לבדוק שהמכנה $\sqrt{5a_n-6}+a_n$ חיובי.",
              r"להניח התכנסות ולעבור לגבול בנוסחת הנסיגה לפני שהוכחנו מונוטוניות וחסימות."],
    steps=[
        num(r"מהו $a_2$? (עשרוני)", sp.sqrt(14), r"$a_2=\sqrt{5\cdot4-6}=\sqrt{14}\approx3.7417$."),
        chx(r"מהו $a_{n+1}-a_n$ אחרי כפל בצמוד?", -(aa - 2)*(aa - 3)/(sq + aa),
            [(aa - 2)*(aa - 3)/(sq + aa), -(aa - 2)*(aa + 3)/(sq + aa), -(aa - 2)*(aa - 3)/(sq - aa)],
            lambda e: same(e, sq - aa), r"$\frac{(5a_n-6)-a_n^2}{\sqrt{5a_n-6}+a_n}=-\frac{(a_n-2)(a_n-3)}{\sqrt{5a_n-6}+a_n}$ (אומת ב-sympy)."),
        order("סדרו את שלבי ההוכחה.", S2, "חסימה באינדוקציה, אחר כך מונוטוניות (שנשענת על החסימה), התכנסות, ולבסוף מציאת הגבול. כל שלב נשען על קודמו."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", S2b, 4,
                r"הפתרון $L=2$ אינו מקיים $L\ge3$; מהחסימה מהאינדוקציה נובע $L=3$."),
        num(r"מהו גבול הסדרה?", 3, r"$L=3$ (התקרבות מספרית: $a_{300}$ שונה מ-$3$ בפחות מ-$10^{-9}$)."),
    ],
    stepsSource="ai-draft")

# ===== Q2b: exactly one solution of x^3 + e^x = -x =====
f2 = x**3 + x + sp.exp(x)
f2p = sp.diff(f2, x)
assert same(f2p, 3*x**2 + 1 + sp.exp(x)) and all(f2p.subs(x, v) > 0 for v in (-5, -1, 0, 3))
assert sp.simplify(f2.subs(x, -1) - (-2 + sp.exp(-1))) == 0 and f2.subs(x, -1) < 0 and f2.subs(x, 0) == 1
P2 = [r"נגדיר $f(x)=x^3+x+e^x$; המשוואה שקולה ל-$f(x)=0$.",
      r"$f(-1)=-2+\frac{1}{e}<0$ ו-$f(0)=1>0$, ו-$f$ רציפה, ולכן לפי משפט ערך הביניים קיים $c\in(-1,0)$ עם $f(c)=0$.",
      r"$f'(x)=3x^2+1+e^x>0$ לכל $x$, ולכן $f$ עולה ממש בכל $\mathbb{R}$.",
      r"$f$ עולה ממש ולכן חד-חד-ערכית, כלומר $f(x)=0$ רק ב-$x=c$."]
P2b = list(P2)
P2b[1] = r"$f(-1)=-2+e>0$ ו-$f(0)=1>0$, ו-$f$ רציפה, ולכן לפי משפט ערך הביניים קיים $c\in(-1,0)$ עם $f(c)=0$."
assert f2.subs(x, -1) < 0 < (-2 + sp.E)

add(2, "ב",
    rubric=rub((r"העברת אגפים והגדרת $f(x)=x^3+x+e^x$", 2),
               (r"חישוב $f(-1)<0$ ו-$f(0)>0$ והפעלת משפט ערך הביניים: קיים פתרון", 4),
               (r"חישוב $f'(x)=3x^2+1+e^x>0$: $f$ עולה ממש", 2),
               (r"מסקנה: $f$ חד-חד-ערכית ולכן הפתרון יחיד", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"להראות רק קיום (ערך ביניים) ולשכוח הוכחת יחידות.",
              r"לחשב $f(-1)$ בטעות כ-$-2+e$ ולא $-2+e^{-1}$, כך שהסימן יוצא חיובי והמשפט אינו חל."],
    steps=[
        chx(r"מהי הנגזרת של $f(x)=x^3+x+e^x$?", 3*x**2 + 1 + sp.exp(x), [3*x**2 + 1 + x*sp.exp(x - 1), 3*x**2 + x + sp.exp(x), 3*x**2 + 1 - sp.exp(x)],
            lambda e: same(e, f2p), r"$f'(x)=3x^2+1+e^x$, וכל הסכום חיובי לכל $x$ (אומת ב-sympy)."),
        num(r"מהו $f(-1)$? (עשרוני)", f2.subs(x, -1), r"$f(-1)=-1-1+e^{-1}=-2+\frac{1}{e}\approx-1.6321<0$."),
        num(r"מהו $f(0)$?", f2.subs(x, 0), r"$f(0)=0+0+e^0=1>0$."),
        ch(r"איזה משפט מבטיח שקיים פתרון בקטע $(-1,0)$ לאחר שנמצא שינוי סימן?", "משפט ערך הביניים",
           ["משפט רול", "משפט לגראנז'", "משפט פרמה"],
           r"רק משפט ערך הביניים מבטיח אפס לפונקציה רציפה שמחליפה סימן. משפט רול נותן אפס של הנגזרת, לגראנז' נקודה עם שיפוע נתון ופרמה נקודות קיצון."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", P2b, 1,
                r"$f(-1)=-1-1+e^{-1}=-2+\frac1e$ ולא $-2+e$. הערך השלילי הוא מה שמאפשר להפעיל את משפט ערך הביניים."),
    ],
    stepsSource="ai-draft")

# ===== Q3a: lim (1+e^x)^(1/x) =====
assert sp.limit(sp.log(1 + sp.exp(x))/x, x, sp.oo) == 1
assert same(sp.diff(sp.log(1 + sp.exp(x)), x), sp.exp(x)/(1 + sp.exp(x)))
assert abs(float(sp.N((1 + sp.exp(x)).subs(x, 60)**(R(1, 60)))) - float(sp.E)) < 0.05

add(3, "א",
    rubric=rub((r"זיהוי צורה $\infty^0$ והעברה לחזקת $e$: $e^{\frac{1}{x}\ln(1+e^x)}$", 3),
               (r"לופיטל על $\frac{\ln(1+e^x)}{x}$: $\frac{e^x}{1+e^x}\to1$", 5),
               (r"מסקנה: הגבול $e$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לכתוב $\infty^0=1$ בלי חישוב; זו אי-ודאות.",
              r"לשכוח לחלק מונה ומכנה ב-$e^x$ בחישוב $\lim\frac{e^x}{1+e^x}$ ולטעות להסיק $\infty$."],
    steps=[
        ch(r"מהי צורת אי-הוודאות של $\lim_{x\to+\infty}(1+e^x)^{\frac1x}$?", r"$\infty^0$", [r"$1^{\infty}$", r"$0^0$", r"$\frac{\infty}{\infty}$"],
           r"הבסיס $1+e^x\to\infty$ והחזקה $\frac{1}{x}\to0$."),
        chx(r"מהי נגזרת $\ln(1+e^x)$ (המונה בלופיטל)?", sp.exp(x)/(1 + sp.exp(x)), [1/(1 + sp.exp(x)), sp.exp(x), 1/sp.exp(x)],
            lambda e: same(e, sp.exp(x)/(1 + sp.exp(x))), r"כלל השרשרת: $\frac{1}{1+e^x}\cdot e^x$ (אומת ב-sympy)."),
        num(r"מהו $\lim_{x\to+\infty}\frac{\ln(1+e^x)}{x}$?", 1, r"$\frac{e^x}{1+e^x}=\frac{1}{e^{-x}+1}\to1$ (נבדק ב-sympy)."),
        num(r"מהו הגבול המבוקש? (עשרוני)", sp.E, r"$e^1=e\approx2.7183$."),
    ],
    stepsSource="ai-draft")

# ===== Q3b: int arcsin x dx =====
F3b = x*sp.asin(x) + sp.sqrt(1 - x**2)
assert same(sp.diff(F3b, x), sp.asin(x))
F3bw = [x*sp.asin(x) - sp.sqrt(1 - x**2), x*sp.asin(x) + 1/sp.sqrt(1 - x**2), x*sp.asin(x) + sp.sqrt(1 - x**2)/2]
def0 = sp.integrate(sp.asin(x), (x, 0, R(1, 2)))
assert sp.simplify(def0 - (sp.pi/12 + sp.sqrt(3)/2 - 1)) == 0

add(3, "ב",
    rubric=rub((r"בחירת אינטגרציה בחלקים עם $u=\arcsin x$, $v'=1$", 3),
               (r"נגזרת $u'=\frac{1}{\sqrt{1-x^2}}$ ו-$v=x$", 2),
               (r"חישוב האינטגרל הנותר $\int\frac{x}{\sqrt{1-x^2}}dx=-\sqrt{1-x^2}$", 3),
               (r"תשובה $x\arcsin x+\sqrt{1-x^2}+C$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לטעות בסימן ולכתוב $x\arcsin x-\sqrt{1-x^2}$.",
              r"לשכוח שהנגזרת של $\arcsin x$ היא $\frac{1}{\sqrt{1-x^2}}$ ולא $\frac{1}{1+x^2}$."],
    steps=[
        ch(r"כיצד בוחר הפתרון הרשמי את $u$ ו-$v'$ באינטגרציה בחלקים?", r"$u=\arcsin x$, $v'=1$", [r"$u=1$, $v'=\arcsin x$", r"$u=x$, $v'=\arcsin x$", r"$u=\arcsin x$, $v'=x$"],
           r"אין לנו קדומה ידועה של $\arcsin x$, אבל נגזרתו פשוטה; לכן $u=\arcsin x$ ו-$v'=1$, כלומר $v=x$."),
        chx(r"מהי $u'=\left(\arcsin x\right)'$?", 1/sp.sqrt(1 - x**2), [1/(1 + x**2), 1/sp.sqrt(1 + x**2), -1/sp.sqrt(1 - x**2)],
            lambda e: same(e, sp.diff(sp.asin(x), x)), r"נגזרת הארקסינוס היא $\frac{1}{\sqrt{1-x^2}}$ (אומת ב-sympy)."),
        chx(r"מהי הפונקציה הקדומה של $\arcsin x$ (בתחום $-1<x<1$)?", F3b, F3bw, lambda e: same(sp.diff(e, x), sp.asin(x)),
            r"$x\arcsin x-\int\frac{x}{\sqrt{1-x^2}}dx=x\arcsin x+\sqrt{1-x^2}$; הנגזרת של כל אפשרות נבדקה ב-sympy."),
        num(r"מהו $\int_0^{1/2}\arcsin x\,dx$? (עשרוני)", def0, r"$\left[x\arcsin x+\sqrt{1-x^2}\right]_0^{1/2}=\frac{\pi}{12}+\frac{\sqrt3}{2}-1\approx0.1278$."),
    ],
    stepsSource="ai-draft")

# ===== Q4a: continuity parameter a =====
a_ = sp.Symbol('a_', positive=True)
cond = sp.Eq(sp.log(a_)**2, sp.log(a_))
assert set(sp.solve(cond, a_)) == {1, sp.E}
good = lambda av: sp.simplify(sp.log(av)**2 - sp.log(av)) == 0
assert good(1) and good(sp.E) and not good(sp.exp(-1)) and not good(2)
for alt in [sp.Eq(sp.log(a_), 0), sp.Eq(sp.log(a_)**2, 1), sp.Eq(a_**2, a_)]:
    assert set(sp.solve(alt, a_)) != {1, sp.E}

add(4, "א",
    rubric=rub((r"גבול שמאלי ו-$g(0)$: $(\ln a)^2$", 2),
               (r"גבול ימני: $\ln\left(a+e^{-1/x}\right)\to\ln a$ כאשר $x\to0^+$", 3),
               (r"משוואה $(\ln a)^2=\ln a$ ופתרון $a=1$ או $a=e$", 3),
               (r"רציפות בשאר הנקודות (פונקציה אלמנטרית) ומסקנה", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לצמצם את $\ln a$ משני האגפים ולהפסיד את הפתרון $a=1$.",
              r"לשכוח שהגבול $e^{-1/x}\to0$ כאשר $x\to0^+$ (ולא $\infty$)."],
    steps=[
        ch(r"איזו משוואה על $a$ מבטיחה רציפות ב-$x=0$?", r"$(\ln a)^2=\ln a$", [r"$\ln a=0$", r"$(\ln a)^2=1$", r"$a^2=a$"],
           r"הגבול השמאלי ו-$g(0)$ הם $(\ln a)^2$, והגבול הימני הוא $\ln a$; דורשים שוויון. לכל אחת מהאפשרויות האחרות קבוצת הפתרונות שונה מ-$\{1,e\}$ (נבדק ב-sympy)."),
        num(r"מהו הערך הקטן מבין הערכים של $a$ המקיימים את המשוואה?", 1, r"$\ln a(\ln a-1)=0$ נותן $\ln a=0$, כלומר $a=1$."),
        num(r"מהו הערך הגדול? (עשרוני)", sp.E, r"$\ln a=1$ נותן $a=e\approx2.7183$."),
    ],
    stepsSource="ai-draft")

# ===== Q4b: tangent parallel to x - y = 7 =====
f4 = sp.log(1 + x**2)
f4p = sp.diff(f4, x)
assert same(f4p, 2*x/(1 + x**2)) and sp.solve(sp.Eq(f4p, 1), x) == [1]
tan4 = lambda k: sp.simplify((f4.subs(x, 1) - 1 - k)) == 0      # y = x + k touches the curve at the unique point x=1 of slope 1
kgood = sp.log(2) - 1
assert tan4(kgood) and not tan4(sp.log(2)) and not tan4(-sp.log(2) - 1) and not tan4(1 - sp.log(2))

add(4, "ב",
    rubric=rub((r"השיפוע הנדרש $1$ (הישר $y=x-7$)", 2),
               (r"נגזרת $f'(x)=\frac{2x}{1+x^2}$ ופתרון $f'(x_0)=1$: $x_0=1$", 4),
               (r"חישוב $f(1)=\ln2$", 1),
               (r"משוואת המשיק $y=x+\ln2-1$", 3)),
    rubricSource="ai-draft",
    pitfalls=[r"לקחת שיפוע $-1$ כי $x-y=7$ נראה עם מינוס; כאן $y=x-7$ ולכן השיפוע $1$.",
              r"לחשב את החותך כ-$\ln2$ במקום $f(1)-f'(1)\cdot1=\ln2-1$."],
    steps=[
        num(r"מהו השיפוע של הישר $x-y=7$?", 1, r"$y=x-7$, ולכן השיפוע $1$."),
        chx(r"מהי הנגזרת של $f(x)=\ln(1+x^2)$?", 2*x/(1 + x**2), [1/(1 + x**2), 2*x/(1 + x), 2/(1 + x**2)], lambda e: same(e, f4p),
            r"כלל השרשרת: $\frac{1}{1+x^2}\cdot2x$ (אומת ב-sympy)."),
        num(r"באיזה $x_0$ מתקיים $f'(x_0)=1$?", 1, r"$\frac{2x}{1+x^2}=1$ נותן $(x-1)^2=0$, כלומר $x_0=1$ היחיד."),
        num(r"מהו $f(1)$? (עשרוני)", f4.subs(x, 1), r"$f(1)=\ln2\approx0.6931$."),
        ch("מהי משוואת המשיק?", r"$y=x+\ln2-1$", [r"$y=x+\ln2$", r"$y=x-\ln2-1$", r"$y=x+1-\ln2$"],
           r"$y=f(1)+f'(1)(x-1)=\ln2+x-1$. רק לערך הזה הישר עובר דרך $(1,\ln2)$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-draft")

# ===== Q5a: limit at -infinity =====
g5 = sp.sqrt(2 + 2*x + x**2) - sp.sqrt(2 - 2*x + x**2)
assert sp.limit(g5, x, -sp.oo) == -2 and sp.limit(g5, x, sp.oo) == 2
assert same((2 + 2*x + x**2) - (2 - 2*x + x**2), 4*x)
assert abs(float(sp.N(g5.subs(x, -10**6))) + 2) < 1e-5

add(5, "א",
    rubric=rub((r"כפל בצמוד והמונה $(2+2x+x^2)-(2-2x+x^2)=4x$", 3),
               (r"הוצאת $|x|$ מהשורשים, ובמעבר ל-$-\infty$ נקבל $|x|=-x$", 3),
               (r"חישוב הגבול $\frac{4}{-(1+1)}=-2$", 4)),
    rubricSource="ai-draft",
    pitfalls=[r"לכתוב $\sqrt{x^2}=x$ כאשר $x\to-\infty$ ולקבל $+2$ במקום $-2$.",
              r"להשאיר $\infty-\infty$ בלי כפל בצמוד."],
    steps=[
        chx(r"מהו המונה אחרי הכפל בצמוד?", 4*x, [4, 4*x**2, 2*x], lambda e: same(e, (2 + 2*x + x**2) - (2 - 2*x + x**2)),
            r"$(2+2x+x^2)-(2-2x+x^2)=4x$ (אומת ב-sympy)."),
        ch(r"מהו $\sqrt{x^2}$ כאשר $x\to-\infty$?", r"$|x|=-x$", ["$x$", "$x^2$", r"$-|x|$"],
           r"שורש ריבועי אינו שלילי, ועבור $x<0$ מתקיים $|x|=-x$."),
        num(r"מהו הגבול ב-$-\infty$?", -2, r"$\frac{4x}{|x|\left(\sqrt{\cdot}+\sqrt{\cdot}\right)}=\frac{-4}{1+1}=-2$ (נבדק ב-sympy וגם בהצבה $x=-10^6$)."),
    ],
    stepsSource="ai-draft")

# ===== Q5b: int x/((x^2+1)(x+1)) =====
g5b = x/((x**2 + 1)*(x + 1))
A5, B5, C5 = sp.symbols('A B C')
sol5 = sp.solve(sp.Poly(sp.expand(A5*(x**2 + 1) + (B5*x + C5)*(x + 1) - x), x).all_coeffs(), [A5, B5, C5], dict=True)[0]
assert sol5 == {A5: R(-1, 2), B5: R(1, 2), C5: R(1, 2)}
F5 = -sp.log(x + 1)/2 + sp.log(x**2 + 1)/4 + sp.atan(x)/2
assert same(sp.diff(F5, x), g5b)
for bf in [A5*(x**2 + 1) + B5*(x + 1) - x, A5*(x**2 + 1) + B5*x*(x + 1) - x]:
    assert sp.solve(sp.Poly(sp.expand(bf), x).all_coeffs(), [A5, B5], dict=True) == []
F5w = [sp.log(x + 1)/2 + sp.log(x**2 + 1)/4 + sp.atan(x)/2, -sp.log(x + 1)/2 - sp.log(x**2 + 1)/4 + sp.atan(x)/2,
       -sp.log(x + 1)/2 + sp.log(x**2 + 1)/2 + sp.atan(x)]

add(5, "ב",
    rubric=rub((r"פירוק לשברים חלקיים $\frac{A}{x+1}+\frac{Bx+C}{x^2+1}$ ומערכת מקדמים", 3),
               (r"פתרון $A=-\frac12$, $B=C=\frac12$", 3),
               (r"אינטגרציה של שלושת החלקים: שני לוגריתמים ו-$\arctan$", 3),
               (r"תשובה סופית עם $+C$", 1)),
    rubricSource="ai-draft",
    pitfalls=[r"לכתוב מונה קבוע $B$ מעל $x^2+1$ ולהיתקע במערכת בלי פתרון.",
              r"לשכוח שחלק מהמונה $\frac{x+1}{x^2+1}$ נותן גם $\arctan x$ ולא רק לוגריתם."],
    steps=[
        ch(r"איזה פירוק מתאים ל-$\frac{x}{(x^2+1)(x+1)}$?", r"$\frac{A}{x+1}+\frac{Bx+C}{x^2+1}$", [r"$\frac{A}{x+1}+\frac{B}{x^2+1}$", r"$\frac{A}{x+1}+\frac{Bx}{x^2+1}$"],
           r"$x^2+1$ אי-פריק, לכן מעליו מונה לינארי. בשתי האפשרויות האחרות למערכת המקדמים אין פתרון (אומת ב-sympy)."),
        num(r"מהו $A$?", sol5[A5], r"הצבת $x=-1$ ב-$x=A(x^2+1)+(Bx+C)(x+1)$ נותנת $-1=2A$, כלומר $A=-\frac12$."),
        num(r"מהו $B$?", sol5[B5], r"מהשוואת מקדמי $x^2$: $A+B=0$, ולכן $B=\frac12$."),
        num(r"מהו $C$?", sol5[C5], r"מהשוואת המקדמים החופשיים: $A+C=0$, ולכן $C=\frac12$."),
        chx(r"מהי הפונקציה הקדומה (בתחום $x>-1$, בלי הקבוע)?", F5, F5w, lambda e: same(sp.diff(e, x), g5b),
            r"$-\frac12\ln(x+1)+\frac14\ln(x^2+1)+\frac12\arctan x$; הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-draft")

# ===== Q6a: volume of revolution (washers) =====
V6 = sp.pi*sp.integrate((sp.pi/2 - x)**2 - sp.cos(x)**2, (x, 0, sp.pi/2))
assert sp.simplify(V6 - sp.pi**2/4*(-1 + sp.pi**2/6)) == 0
i61 = sp.integrate((sp.pi/2 - x)**2, (x, 0, sp.pi/2))
i62 = sp.integrate(sp.cos(x)**2, (x, 0, sp.pi/2))
assert sp.simplify(i61 - sp.pi**3/24) == 0 and sp.simplify(i62 - sp.pi/4) == 0
assert all(sp.N((sp.pi/2 - xv) - sp.cos(xv)) > 0 for xv in (0.1, 0.5, 1.0, 1.4))

add(6, "א",
    rubric=rub((r"זיהוי שהתחום בין שני גרפים והצבת הנוסחה $V=\pi\int(R^2-r^2)dx$ עם $R=\frac\pi2-x$ ו-$r=\cos x$", 4),
               (r"חישוב $\int_0^{\pi/2}\left(\frac\pi2-x\right)^2dx=\frac{\pi^3}{24}$", 2),
               (r"חישוב $\int_0^{\pi/2}\cos^2x\,dx=\frac{\pi}{4}$ (באמצעות $\cos^2x=\frac{1+\cos2x}{2}$)", 2),
               (r"חיבור התוצאה $V=\pi\left(\frac{\pi^3}{24}-\frac{\pi}{4}\right)$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לחשב $\pi\int\left(R-r\right)^2dx$ במקום $\pi\int\left(R^2-r^2\right)dx$.",
              r"להחליף בין הרדיוס החיצוני לפנימי: בקטע הנתון $\frac\pi2-x\ge\cos x$ ולכן הישר הוא החיצוני."],
    steps=[
        ch(r"מהם הרדיוס החיצוני $R$ והפנימי $r$ של הדיסקה בסיבוב סביב ציר ה-$x$?", r"$R=\frac\pi2-x$ ו-$r=\cos x$", [r"$R=\cos x$ ו-$r=\frac\pi2-x$", r"$R=\frac\pi2-x$ ו-$r=0$", r"$R=\frac\pi2-x+\cos x$ ו-$r=0$"],
           r"בקטע $[0,\frac\pi2]$ מתקיים $\frac\pi2-x\ge\cos x$ (נבדק ב-sympy בכמה נקודות), לכן הישר חיצוני והקוסינוס פנימי."),
        num(r"מהו $\int_0^{\pi/2}\left(\frac\pi2-x\right)^2dx$? (עשרוני)", i61, r"$\frac{(\pi/2)^3}{3}=\frac{\pi^3}{24}\approx1.2919$."),
        num(r"מהו $\int_0^{\pi/2}\cos^2x\,dx$? (עשרוני)", i62, r"$\cos^2x=\frac{1+\cos2x}{2}$ ולכן האינטגרל $\frac{\pi}{4}\approx0.7854$."),
        num(r"מהו הנפח $V$? (עשרוני)", V6, r"$V=\pi\left(\frac{\pi^3}{24}-\frac{\pi}{4}\right)\approx1.5912$."),
    ],
    stepsSource="ai-draft")

# ===== Q6b: area between sqrt(x+2), sqrt(2x), y=0 =====
xs = sp.Symbol('xs', real=True)
inter = sp.solve(sp.Eq(sp.sqrt(xs + 2), sp.sqrt(2*xs)), xs)
assert inter == [2]
I1 = sp.integrate(sp.sqrt(x + 2), (x, -2, 2))
I2 = sp.integrate(sp.sqrt(2*x), (x, 0, 2))
assert (I1, sp.simplify(I2)) == (R(16, 3), R(8, 3)) and sp.simplify(I1 - I2 - R(8, 3)) == 0
area = sp.integrate(sp.sqrt(x + 2), (x, -2, 0)) + sp.integrate(sp.sqrt(x + 2) - sp.sqrt(2*x), (x, 0, 2))
assert sp.simplify(area - R(8, 3)) == 0
bad_vals = [I1 + I2, sp.integrate(sp.sqrt(x + 2) - sp.sqrt(2*x), (x, 0, 2)), sp.integrate(sp.sqrt(x + 2), (x, -2, 0))]
assert all(abs(float(v) - 8/3) > 1e-6 for v in bad_vals)

add(6, "ב",
    rubric=rub((r"נקודת החיתוך של $y=\sqrt{x+2}$ ו-$y=\sqrt{2x}$: $x=2$", 2),
               (r"הצגת השטח כהפרש: $\int_{-2}^{2}\sqrt{x+2}\,dx-\int_0^2\sqrt{2x}\,dx$", 3),
               (r"חישוב שני האינטגרלים: $\frac{16}{3}$ ו-$\frac{8}{3}$", 3),
               (r"מסקנה: $S=\frac{8}{3}$", 2)),
    rubricSource="ai-draft",
    pitfalls=[r"לקחת רק את הקטע $[0,2]$ ולהתעלם מהחלק $-2\le x\le0$ שבו התחום יושב ישירות מעל ציר ה-$x$.",
              r"לחבר את שני האינטגרלים במקום לחסר את הקטן."],
    steps=[
        num(r"באיזה $x$ נחתכים הגרפים $y=\sqrt{x+2}$ ו-$y=\sqrt{2x}$?", 2, r"$x+2=2x$ נותן $x=2$."),
        ch("כיצד מתבטא השטח?", r"$\int_{-2}^{2}\sqrt{x+2}\,dx-\int_0^2\sqrt{2x}\,dx$",
           [r"$\int_{-2}^{2}\sqrt{x+2}\,dx+\int_0^2\sqrt{2x}\,dx$", r"$\int_0^2\left(\sqrt{x+2}-\sqrt{2x}\right)dx$", r"$\int_{-2}^{0}\sqrt{x+2}\,dx$"],
           r"התחום הוא ההפרש בין השטח מתחת ל-$\sqrt{x+2}$ בקטע $[-2,2]$ לשטח מתחת ל-$\sqrt{2x}$ בקטע $[0,2]$. שלוש האפשרויות האחרות נותנות ערכים שונים מ-$\frac83$ (נבדק ב-sympy)."),
        num(r"מהו $\int_{-2}^{2}\sqrt{x+2}\,dx$? (עשרוני)", I1, r"$\frac23(x+2)^{3/2}\Big|_{-2}^{2}=\frac23\cdot8=\frac{16}{3}\approx5.3333$."),
        num(r"מהו $\int_0^2\sqrt{2x}\,dx$? (עשרוני)", I2, r"$\sqrt2\cdot\frac23x^{3/2}\Big|_0^2=\frac{8}{3}\approx2.6667$."),
        num(r"מהו השטח הכלוא? (עשרוני)", area, r"$\frac{16}{3}-\frac{8}{3}=\frac83\approx2.6667$."),
    ],
    stepsSource="ai-draft")

exam = {
    "examCode": "19B-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ט, מועד ב'",
    "year": 2019,
    "examDate": "27/03/2019",
    "sourceFile": "calculus-1/19B-A exam+solution.pdf",
    "solutionFile": "calculus-1/19B-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

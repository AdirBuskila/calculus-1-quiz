# -*- coding: utf-8 -*-
"""Generator for tools/raw/23B-B.json -- calculus-1 (20151), semester B 2023, moed B (10/07/2023).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23B-B.py

Source: sitting 23B-B, pp.1-7 (typed exam with the official worked solution after each question).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each). Weight of every question 20%.

Transcription notes
- Official solution transcribed in full, as printed. Rubric and steps are intentionally not written.
- Q1: the official graph (p.2) is shipped as a figure.
- Q2b (as printed): the text says the sequence is bounded above "by 6" and then proves a_n<5; transcribed as printed.
- Q5b (as printed): the middle expression "x - ln(1+x^2)" uses x where the substitution variable t belongs; the final
  answer x - ln(1+e^(2x)) + C is correct (tools/verify/23B-B/check.py).

Checks (tools/verify/23B-B/check.py, sympy): every derivative, limit, integral, volume and arc length matches the
official answers; the final answers have 0 mismatches.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23B-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
$y=xe^{\frac{1}{x}}$
**א. תחום הגדרה** $D=\{x\neq0\}$. אין נקודות חיתוך עם צירי הקואורדינטות.
**ב.** $y'=e^{\frac{1}{x}}-\frac{1}{x}e^{\frac{1}{x}}=e^{\frac{1}{x}}\left(1-\frac{1}{x}\right)$. מכאן רואים שהנגזרת מתאפסת רק ב-$x=1$ ובנוסף $y'>0$ כאשר $x<0\cup x>1$ וגם $y'<0$ כאשר $0<x<1$. הנקודה היא נקודת מינימום מקומי.
**ג.** $y''=e^{\frac{1}{x}}\left(-\frac{1}{x^2}+\frac{1}{x^3}+\frac{1}{x^2}\right)=e^{\frac{1}{x}}\cdot\frac{1}{x^3}$. אין נקודות פיתול. בנוסף, $y''>0$ עבור $x>0$ וכאן הפונקציה קעורה (כלפי מעלה) ו-$y''<0$ עבור $x<0$ וכאן הפונקציה קמורה (כלפי מטה).
**ד.** $\begin{cases}\lim_{x\to0^-}xe^{1/x}=0\\ \lim_{x\to0^+}xe^{1/x}=+\infty\end{cases}$ ולכן קו ישר $x=0$ (ציר ה-$y$) מהווה אסימפטוטה אנכית לגרף הפונקציה.
$\begin{cases}\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim_{x\to\pm\infty}e^{1/x}=1\\ \lim_{x\to\pm\infty}(f(x)-1x)=\lim_{x\to\pm\infty}x\left(e^{1/x}-1\right)=1\end{cases}$ ולכן קו ישר $y=x+1$ מהווה אסימפטוטה משופעת לגרף הפונקציה גם בפלוס וגם במינוס אינסוף.

![הגרף הרשמי של הפונקציה](images/exams/23B-B-Q1-graph.png)
"""

SOL2A = r"""
$$\int\frac{1}{2+\cos x}dx=\left[t=\tan\frac{x}{2},\quad\cos x=\frac{1-t^2}{1+t^2},\ dx=\frac{2}{1+t^2}dt\right]=\int\frac{1}{2+\frac{1-t^2}{1+t^2}}\cdot\frac{2}{1+t^2}dt=$$
$$=2\int\frac{1}{2+2t^2+1-t^2}dt=2\int\frac{1}{t^2+3}dt=\frac{2}{\sqrt{3}}\arctan\frac{t}{\sqrt{3}}=\frac{2}{\sqrt{3}}\arctan\frac{\tan\frac{x}{2}}{\sqrt{3}}+c$$
"""

SOL2B = r"""
נתונה הסדרה $a_1=0,\ a_{n+1}=\sqrt{20+a_n}$. הוכיחו כי הסדרה מתכנסת וחישבו את הגבול של הסדרה.
נוכיח באינדוקציה שהסדרה עולה $a_{n+1}>a_n\ge0$.
בדיקה עבור $n=1$: $a_2=\sqrt{20}>a_1=0\ge0$.
הנחת האינדוקציה: $a_{n+1}>a_n\ge0$.
צריך להוכיח: $a_{n+2}>a_{n+1}\ge0$.
$$a_{n+1}>a_n\ge0\Rightarrow a_{n+1}+20>a_n+20\ge20\Rightarrow\sqrt{a_{n+1}+20}>\sqrt{a_n+20}\ge\sqrt{20}\Rightarrow a_{n+2}>a_{n+1}\ge0$$
נוכיח באינדוקציה הסדרה חסומה מלמעלה על ידי 6: $a_n<5$.
בדיקה עבור $n=1$: $a_2=\sqrt{20}<5$.
הנחת האינדוקציה: $a_n<5$.
צריך להוכיח: $a_{n+1}<5$.
$$a_n<5\Rightarrow a_n+20<25\Rightarrow\sqrt{a_n+20}<\sqrt{25}\Rightarrow a_{n+1}<5$$
הסדרה עולה וחסומה מלמעלה לכן היא מתכנסת. נסמן $\lim_{n\to\infty}a_n=L$.
$$a_{n+1}=\sqrt{20+a_n}\Rightarrow\lim_{n\to\infty}a_n=\lim_{n\to\infty}\sqrt{20+a_n}\Rightarrow L=\sqrt{20+L}\Rightarrow L^2-L-20=0$$
$L_1=5$, $L_2=-4$ ($\varnothing$).
תשובה: $\lim_{n\to\infty}a_n=5$
"""

SOL3A = r"""
$$\lim_{x\to0}\frac{x^4}{\int_0^{x^2}\ln(1+3t)\,dt}=\left\{\frac{0}{0}\right\}=\lim_{x\to0}\frac{4x^3}{\ln(1+3x^2)\cdot2x}=\lim_{x\to0}\frac{2x^2}{\ln(1+3x^2)}\left\{\frac{0}{0}\right\}$$
$$=\lim_{x\to0}\frac{4}{\frac{1}{1+3x^2}\cdot6}=\frac{2}{3}$$
"""

SOL3B = r"""
$$\lim_{x\to0^+}f(x)=\lim_{x\to0^+}\ln\left(a+e^{-\frac{1}{x}}\right)=\ln a,\qquad f(0)=\ln^2a$$
על מנת שפונקציה תהיה רציפה יש לקיים:
$$\lim_{x\to0^+}f(x)=f(0)\Rightarrow\ln a=\ln^2a\Rightarrow\ln a(\ln a-1)=0$$
$$\ln a=0\Rightarrow a=1;\quad\ln a=1\Rightarrow a=e$$
"""

SOL4A = r"""
**דרך א'**
נגדיר פונקציה $f(x)=\arcsin x$. הפונקציה מקיימת את משפט לגרנז', כלומר רציפה בקטע $x\in[0,a]$, גזירה בקטע $x\in(0,a)$, כלומר קיימת נקודה $c\in(0,a)$, כך שמתקיים $f'(c)=\frac{f(a)-f(0)}{a-0}$. גזור את הפונקציה. נקבל: $f'(c)=\frac{1}{\sqrt{1-c^2}}$, כלומר $\frac{1}{\sqrt{1-c^2}}=\frac{\arcsin a-\arcsin0}{a-0}$, לכן מתקיים $1<\frac{\arcsin a-\arcsin0}{a-0}<\frac{1}{\sqrt{1-a^2}}$, מ.ש.ל.

**דרך ב'**
נגדיר פונקציה $f(x)=\arcsin x-x$ נגזור את הפונקציה. נקבל: $f'(x)=\frac{1}{\sqrt{1-x^2}}-1$.
נראה ש: $f'(x)>0,\ \forall0<x<1$:
$$0<x<1\Rightarrow0<x^2<1\Rightarrow0<1-x^2<1\Rightarrow\frac{1}{1-x^2}>1\Rightarrow\frac{1}{1-x^2}-1>0$$
לכן $f'(x)>0$ בקטע $(0,1)$, לכן הפונקציה עולה. אבל $f(0)=\arcsin0-0=0$ ומכאן $f(x)=\arcsin x-x>0\Rightarrow\arcsin x>x\Rightarrow\arcsin a>a$.
אם נגדיר עכשיו $g(x)=\frac{x}{\sqrt{1-x^2}}-\arcsin x$, אז
$$g'(x)=\frac{1}{(1-x^2)^{\frac{3}{2}}}-\frac{1}{(1-x^2)^{\frac{1}{2}}}=\frac{x^2}{(1-x^2)^{\frac{3}{2}}}>0.$$
לכן $g(x)$ עולה בקטע $(0,1)$ אבל $g(0)=0$ ולכן $g(x)=\frac{x}{\sqrt{1-x^2}}-\arcsin x>0\Rightarrow\frac{a}{\sqrt{1-a^2}}-\arcsin a>0$ ולכן בסה"כ מתקיים:
$$a<\arcsin a<\frac{a}{\sqrt{1-a^2}}.$$
"""

SOL4B = r"""
נפח גוף סיבוב סביב ציר $Y$ הוא לפי הנוסחה: $V=2\pi\int_a^bxf(x)\,dx$.
נבדוק את הנק' החיתוך $x^2=2x$. נקבל ב-$x=0,\ x=2$ ובקטע $[0,2]$ מתקיים $2x\ge x^2$.
$$V=2\pi\int_0^2x\left[2x-x^2\right]dx=2\pi\int_0^2\left[2x^2-x^3\right]dx=2\pi\left[\frac{2}{3}x^3-\frac{x^4}{4}\right]\Big|_0^2=\frac{8}{3}\pi$$
לכן $\frac{8}{3}\pi$.
"""

SOL5A = r"""
$$\lim_{x\to+\infty}\frac{\ln\left(1+\frac{1}{x}\right)}{\sin\left(\frac{3}{x}\right)}=\left\{\frac{0}{0}\right\}=\lim_{x\to+\infty}\frac{\frac{1}{1+\frac{1}{x}}\left(-\frac{1}{x^2}\right)}{\cos\left(\frac{3}{x}\right)\left(-\frac{3}{x^2}\right)}=\frac{1}{3}$$
"""

SOL5B = r"""
$$\int\frac{e^{-x}-e^x}{e^{-x}+e^x}dx=\int\frac{e^{-x}+e^x-e^x-e^x}{e^{-x}+e^x}dx$$
$$=\int dx-2\int\frac{e^x}{e^{-x}+e^x}dx=\left|\begin{matrix}t=e^x\\ dt=e^xdx\end{matrix}\right|$$
$$=x-2\int\frac{1}{\frac{1}{t}+t}dt=x-2\int\frac{1}{\frac{1+t^2}{t}}dt=x-2\int\frac{t}{1+t^2}dt$$
$$=x-\ln(1+x^2)+C=x-\ln\left(1+e^{2x}\right)+C$$
"""

SOL6A = r"""
$$L=\int_a^b\sqrt{1+\left(f'(x)\right)^2}\,dx=\int_{\frac{\pi}{3}}^{\frac{\pi}{2}}\sqrt{1+\frac{\cos^2x}{\sin^2x}}\,dx=\int_{\frac{\pi}{3}}^{\frac{\pi}{2}}\frac{1}{\sin x}\,dx=\ln\left|\tan\frac{x}{2}\right|\Big|_{\frac{\pi}{3}}^{\frac{\pi}{2}}$$
$$=\ln1-\ln\frac{1}{\sqrt{3}}=0.5493$$
"""

SOL6B = r"""
נסמן: $f(x)=\arctan x+x^3+x^5-2$.
פונקציה רציפה בקטע $[0,1]$ מקבלת סימנים שונים בקצוות הקטע: $f(0)=-2<0$, $f(1)=\frac{\pi}{4}>0$, לכן קיימת לפחות נקודה אחת $x=c,\ (0<c<1)$ כך ש-$f(c)=0$.
נוכיח כי הפתרון הוא יחיד. נגזרת של הפונקציה חיובית $\left(f'(x)=\frac{1}{1+x^2}+3x^2+5x^4>0\right)$, לכן הפונקציה מונוטונית עולה וחותכת ציר ה-$X$ פעם אחד בלבד.
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=xe^{\frac{1}{x}}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, "
      "תחומי עליה וירידה, נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{1}{2+\cos x}\,dx$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "sequences_limits",
      r"נתונה הסדרה: $a_1=0,\ a_{n+1}=\sqrt{20+a_n}$." "\nהוכיחו כי הסדרה מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "lhopital_taylor",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\frac{x^4}{\int_0^{x^2}\ln(1+3t)\,dt}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "continuity",
      r"נתונה הפונקציה $f(x)=\begin{cases}\ln\left(a+e^{-\frac{1}{x}}\right), & x>0\\ \ln^2\left(a+x^2\right), & x\le0\end{cases}$, כאשר $a>0$."
      "\n" r"עבור אילו ערכי $a$ הפונקציה רציפה ב-$x=0$?",
      SOL3B, part="ב", points=10),

    Q(4, "proof", "mean_value_theorems",
      r"הוכיחו את אי השוויון הבא עבור $0<a<1$: $a<\arcsin(a)<\frac{a}{\sqrt{1-a^2}}$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר מסיבוב של התחום המישורי הכלוא בין הקווים: $y=2x,\ y=x^2$ סביב ציר ה-$Y$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to+\infty}\frac{\ln\left(1+\frac{1}{x}\right)}{\sin\left(\frac{3}{x}\right)}$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{e^{-x}-e^x}{e^{-x}+e^x}\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "definite_integrals",
      r"חשבו את אורך הקשת המוגדרת ע״י $f(x)=\ln(\sin x)$ בתחום $\frac{\pi}{3}\le x\le\frac{\pi}{2}$.",
      SOL6A, part="א", points=10),

    Q(6, "proof", "continuity",
      r"הוכיחו כי למשוואה $\arctan x+x^3+x^5-2=0$ קיים שורש ממשי והוא יחיד.",
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

# ===== Q1: f = x e^(1/x) =====
f1 = x*sp.exp(1/x)
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, sp.exp(1/x)*(1 - 1/x)) and same(f1pp, sp.exp(1/x)/x**3)
assert sp.solve(f1p, x) == [1]
assert f1pp.subs(x, 1) > 0
assert (sp.limit(f1/x, x, sp.oo), sp.limit(f1/x, x, -sp.oo)) == (1, 1)
assert (sp.limit(f1 - x, x, sp.oo), sp.limit(f1 - x, x, -sp.oo)) == (1, 1)
assert sp.limit(f1, x, 0, '-') == 0 and sp.limit(f1, x, 0, '+') == sp.oo

add(1,
    rubric=rub(("תחום הגדרה $x\\neq0$ וללא חיתוך עם הצירים", 2),
               ("נגזרת $f'(x)=e^{1/x}\\left(1-\\frac1x\\right)$, נקודה קריטית $x=1$ ותחומי עליה וירידה", 5),
               ("סיווג $x=1$ כמינימום מקומי", 2),
               ("$f''(x)=\\frac{e^{1/x}}{x^3}$: קמירות וקעירות, ללא נקודות פיתול", 3),
               ("אסימפטוטה אנכית $x=0$ (מימין בלבד)", 3),
               ("אסימפטוטה משופעת $y=x+1$ בשני הכיוונים", 3),
               ("שרטוט הגרף", 2)),
    rubricSource="ai-verified",
    pitfalls=["לטעון שהישר $x=0$ הוא אסימפטוטה משני הצדדים: משמאל $f\\to0$, ורק מימין $f\\to\\infty$.",
              "לשכוח את הגזירה של $e^{1/x}$ עם כלל שרשרת: $\\left(e^{1/x}\\right)'=-\\frac{1}{x^2}e^{1/x}$.",
              "לחשב את $b=\\lim\\left(f(x)-x\\right)$ בלי להפוך ל-$\\frac{e^{1/x}-1}{1/x}$, ולכן לטעות ולקבל $0$ במקום $1$."],
    steps=[
        chx("מהי הנגזרת של $f(x)=xe^{1/x}$?", sp.exp(1/x)*(1 - 1/x),
            [sp.exp(1/x)*(1 + 1/x), sp.exp(1/x), sp.exp(1/x)*(1 - 1/x**2)], lambda e: same(e, f1p),
            "כלל מכפלה: $e^{1/x}+x\\cdot\\left(-\\frac{1}{x^2}\\right)e^{1/x}=e^{1/x}\\left(1-\\frac1x\\right)$ (אומת ב-sympy)."),
        num("מהו ערך הפונקציה בנקודת המינימום המקומי $x=1$? (עשרוני)", f1.subs(x, 1),
            "$f'(x)=0$ רק ב-$x=1$, ו-$f(1)=e\\approx2.718$.", tol=0.001),
        ch("מה סימן $f''(x)=\\frac{e^{1/x}}{x^3}$?",
           "שלילי עבור $x<0$ וחיובי עבור $x>0$, ואין נקודות פיתול",
           ["חיובי בכל תחום ההגדרה", "שלילי בכל תחום ההגדרה", "מתאפס ב-$x=1$, ולכן זו נקודת פיתול"],
           "$e^{1/x}>0$ ולכן הסימן הוא סימן $x^3$. השינוי נעשה ב-$x=0$ שמחוץ לתחום, ולכן אין פיתול (אומת ב-sympy)."),
        ch("מה נכון לגבי הישר $x=0$?", "אסימפטוטה אנכית מימין בלבד (משמאל $f\\to0$)",
           ["אסימפטוטה אנכית משני הצדדים", "אין אסימפטוטה אנכית", "אסימפטוטה אנכית משמאל בלבד"],
           "$\\lim_{x\\to0^+}xe^{1/x}=\\infty$ ו-$\\lim_{x\\to0^-}xe^{1/x}=0$ (sympy)."),
        ch("מהי האסימפטוטה המשופעת ב-$\\pm\\infty$?", "$y=x+1$",
           ["$y=x$", "$y=x-1$", "$y=1$"],
           "$m=\\lim e^{1/x}=1$ ו-$k=\\lim x\\left(e^{1/x}-1\\right)=1$ (אומת ב-sympy בשני הכיוונים)."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: int 1/(2+cos x) dx (Weierstrass) =====
I2 = 1/(2 + sp.cos(x))
W2 = 1/(2 + (1 - t**2)/(1 + t**2))*2/(1 + t**2)
assert same(W2, 2/(t**2 + 3))
v2 = sp.integrate(I2, (x, 0, sp.pi/2))
assert abs(sp.N(v2) - sp.N(sp.pi/(3*sp.sqrt(3)))) < 1e-12
assert same(sp.diff(2/sp.sqrt(3)*sp.atan(sp.tan(x/2)/sp.sqrt(3)), x), I2)

add(2, "א",
    rubric=rub(("הצבה $t=\\tan\\frac x2$ עם $\\cos x=\\frac{1-t^2}{1+t^2}$ ו-$dx=\\frac{2}{1+t^2}dt$", 3),
               ("פישוט האינטגרנד ל-$\\frac{2}{t^2+3}$", 3),
               ("אינטגרל $\\arctan$: $\\frac{2}{\\sqrt3}\\arctan\\frac{t}{\\sqrt3}$", 3),
               ("חזרה ל-$x$ וקבוע אינטגרציה", 1)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את הגורם $\\frac{2}{1+t^2}$ מ-$dx$.",
              "לכתוב $\\arctan t$ במקום $\\frac{1}{\\sqrt3}\\arctan\\frac{t}{\\sqrt3}$.",
              "לשכוח שההצבה $t=\\tan\\frac x2$ לא מוגדרת ב-$x=\\pi+2\\pi k$; כאן המכנה $2+\\cos x$ אינו מתאפס ולכן הקדומה נשארת תקפה."],
    steps=[
        chx("אחרי ההצבה $t=\\tan\\frac x2$ מהו האינטגרנד ב-$t$ (כלומר $\\int\\ldots\\,dt$)?", 2/(t**2 + 3),
            [2/(t**2 + 1), 1/(t**2 + 3), 2/(3 - t**2)], lambda e: same(e, W2),
            "$\\frac{1}{2+\\frac{1-t^2}{1+t^2}}\\cdot\\frac{2}{1+t^2}=\\frac{2}{t^2+3}$ (אומת ב-sympy)."),
        num("מהו המקדם של $\\arctan\\frac{t}{\\sqrt3}$ בקדומה? (עשרוני)", 2/sp.sqrt(3), "$2\\cdot\\frac{1}{\\sqrt3}\\approx1.1547$.", tol=0.001),
        num("כבדיקה: מהו $\\int_0^{\\pi/2}\\frac{dx}{2+\\cos x}$? (עשרוני)", v2, "$\\frac{\\pi}{3\\sqrt3}\\approx0.6046$.", tol=0.001),
    ],
    stepsSource="ai-verified")

# ===== Q2b: a_1 = 0, a_{n+1} = sqrt(20 + a_n) =====
sq = [sp.Integer(0)]
for _ in range(40):
    sq.append(sp.sqrt(20 + sq[-1]))
assert all(0 <= sq[i] < sq[i + 1] < 5 for i in range(12))
a2 = sq[1]
Ls = sp.Symbol('L', real=True)
assert sorted(sp.solve(Ls**2 - Ls - 20, Ls)) == [-4, 5] and sp.sqrt(-4 + 20) == 4
L2 = ["נוכיח באינדוקציה ש-$0\\le a_n\\le a_{n+1}$ וש-$a_n<5$ לכל $n$: הסדרה עולה וחסומה מלעיל.",
      "סדרה עולה וחסומה מלעיל מתכנסת; נסמן $L=\\lim_{n\\to\\infty}a_n$.",
      "$L=\\sqrt{20+L}$, ולכן $L^2-L-20=0$.",
      "$L=5$ או $L=-4$; כיוון ש-$a_n\\ge0$, $L\\ne-4$ ולכן $L=5$."]
L2b = list(L2)
L2b[2] = "$L=\\sqrt{20+L}$, ולכן $L^2=20-L$, כלומר $L^2+L-20=0$."
assert not same(Ls**2 + Ls - 20, Ls**2 - Ls - 20)

add(2, "ב",
    rubric=rub(("הוכחה באינדוקציה שהסדרה עולה ואי-שלילית", 3),
               ("הוכחה באינדוקציה שהסדרה חסומה מלעיל ב-$5$", 3),
               ("מסקנה: מתכנסת (סדרה מונוטונית וחסומה)", 1),
               ("משוואת הגבול $L=\\sqrt{20+L}$ ופתרונה", 2),
               ("פסילת $L=-4$ והגבול $5$", 1)),
    rubricSource="ai-verified",
    pitfalls=["לחשב את הגבול מהמשוואה בלי להוכיח קודם התכנסות.",
              "לא לפסול את $L=-4$ אף שאיברי הסדרה אי-שליליים.",
              "בשלב האינדוקציה לחסם: להשתמש בהנחה $a_n<5$ ולהסיק $\\sqrt{a_n+20}<\\sqrt{25}=5$, ולא להניח את המסקנה."],
    steps=[
        num("מהו $a_2$ בסדרה $a_1=0$, $a_{n+1}=\\sqrt{20+a_n}$? (עשרוני)", a2, "$a_2=\\sqrt{20}\\approx4.4721$.", tol=0.001),
        ch("מדוע נפסל הפתרון $L=-4$ של $L^2-L-20=0$?",
           "כל איברי הסדרה אי-שליליים, ולכן הגבול אינו שלילי",
           ["$-4$ אינו שורש של $L^2-L-20=0$", "$\\sqrt{20+L}$ אינו מוגדר עבור $L=-4$", "הסדרה יורדת ולכן הגבול שלילי"],
           "השורשים הם $5$ ו-$-4$ (sympy) ו-$\\sqrt{20-4}=4$ מוגדר. הסדרה עולה מ-$0$, ולכן הגבול אינו שלילי."),
        order("סדרו את שלבי ההוכחה.", L2, "קודם עליה וחסימות, אחר כך התכנסות, אחר כך משוואת הגבול ובחירת השורש."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L2b, 2,
                "העלאה בריבוע של $L=\\sqrt{20+L}$ נותנת $L^2=20+L$, כלומר $L^2-L-20=0$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: lim x^4 / int_0^(x^2) ln(1+3t) dt = 2/3 =====
den3 = sp.Integral(sp.log(1 + 3*t), (t, 0, x**2))
dden3 = sp.diff(den3, x).doit()
assert same(dden3, 2*x*sp.log(1 + 3*x**2))
assert sp.limit(x**4/sp.integrate(sp.log(1 + 3*t), (t, 0, x**2)), x, 0) == R(2, 3)
assert sp.limit(sp.integrate(sp.log(1 + 3*t), (t, 0, x**2)), x, 0) == 0

add(3, "א",
    rubric=rub(("זיהוי $\\frac00$ והפעלת לופיטל", 2),
               ("גזירת המכנה לפי המשפט היסודי וכלל השרשרת: $2x\\ln(1+3x^2)$", 3),
               ("צמצום ל-$\\frac{2x^2}{\\ln(1+3x^2)}$, שוב $\\frac00$, ולופיטל שני", 3),
               ("ערך הגבול $\\frac23$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את הגורם $2x$ מכלל השרשרת של הגבול העליון $x^2$.",
              "לעצור אחרי לופיטל אחד: $\\frac{2x^2}{\\ln(1+3x^2)}$ עדיין $\\frac00$.",
              "לחשב את האינטגרל במפורש במקום להשתמש במשפט היסודי."],
    steps=[
        ch("מה סוג הצורה הלא מסוימת של $\\frac{x^4}{\\int_0^{x^2}\\ln(1+3t)dt}$ כאשר $x\\to0$?", "$\\frac00$",
           ["$\\frac\\infty\\infty$", "$1^\\infty$", "$0\\cdot\\infty$"],
           "$x^4\\to0$ והאינטגרל על קטע $[0,x^2]$ שמתכווץ שואף ל-$0$ (sympy)."),
        chx("מהי הנגזרת של המכנה $\\int_0^{x^2}\\ln(1+3t)\\,dt$ לפי $x$?", 2*x*sp.log(1 + 3*x**2),
            [sp.log(1 + 3*x**2), x**2*sp.log(1 + 3*x**2), 2*x*sp.log(1 + 3*x)], lambda e: same(e, dden3),
            "משפט יסודי וכלל שרשרת: $\\ln\\left(1+3x^2\\right)\\cdot(x^2)'=2x\\ln(1+3x^2)$ (אומת ב-sympy)."),
        num("מהו ערך הגבול? (עשרוני)", R(2, 3), "אחרי לופיטל שני: $\\frac{4x}{\\frac{6x}{1+3x^2}}\\to\\frac23\\approx0.6667$.", tol=0.001),
    ],
    stepsSource="ai-verified")

# ===== Q3b: continuity at 0, parameter a =====
aa = sp.Symbol('aa', positive=True)
Lg = sp.Symbol('Lg', real=True)
assert sorted(sp.solve(Lg - Lg**2, Lg)) == [0, 1]
assert sp.limit(sp.log(aa + sp.exp(-1/x)), x, 0, '+') == sp.log(aa)
assert sp.log(sp.E).simplify() == 1
sols_a = [sp.exp(v) for v in (0, 1)]
assert sols_a == [1, sp.E]
for bad in (Lg - 2*Lg, Lg, Lg**2):
    assert sp.solve(bad, Lg) == [0]
assert (sp.log(sp.exp(2)) - sp.log(sp.exp(2))**2) != 0

add(3, "ב",
    rubric=rub(("הגבול הימני $\\lim_{x\\to0^+}\\ln\\left(a+e^{-1/x}\\right)=\\ln a$", 3),
               ("הערך בנקודה $f(0)=\\ln^2a$ ומשוואת הרציפות $\\ln a=\\ln^2a$", 3),
               ("פתרון: $\\ln a\\,(\\ln a-1)=0$", 2),
               ("תשובה: $a=1$ או $a=e$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחלק את המשוואה $\\ln a=\\ln^2a$ ב-$\\ln a$ ולאבד את הפתרון $a=1$.",
              "להשוות גם את הגבול השמאלי: הוא שווה ל-$f(0)$ מראש, כי שם הפונקציה היא $\\ln^2(a+x^2)$.",
              "לטעות בגבול הימני: $e^{-1/x}\\to0$ כאשר $x\\to0^+$."],
    steps=[
        ch("איזו משוואה מבטיחה רציפות ב-$x=0$?", "$\\ln a=\\ln^2a$",
           ["$\\ln a=2\\ln a$", "$\\ln a=0$", "$\\ln^2a=0$"],
           "הגבול הימני $\\ln a$ שווה ל-$f(0)=\\ln^2a$. שלוש האפשרויות האחרות נותנות רק $a=1$ (נבדק ב-sympy)."),
        num("מהו $f(0)=\\ln^2\\left(a+0\\right)$ עבור $a=e$?", 1, "$\\ln^2e=1^2=1$, ושווה לגבול הימני $\\ln e=1$."),
        ch("אילו ערכי $a$ מבטיחים רציפות?", "$a=1$ או $a=e$",
           ["$a=1$ בלבד", "$a=e$ בלבד", "$a=1$ או $a=e^2$"],
           "$\\ln a(\\ln a-1)=0$ נותן $\\ln a=0$ או $\\ln a=1$, כלומר $a=1$ או $a=e$. עבור $a=e^2$: $\\ln a=2\\neq4$."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: a < arcsin a < a/sqrt(1-a^2) =====
fa = sp.asin(x) - x
ga = x/sp.sqrt(1 - x**2) - sp.asin(x)
assert same(sp.diff(fa, x), 1/sp.sqrt(1 - x**2) - 1)
assert same(sp.diff(ga, x), x**2/(1 - x**2)**R(3, 2))
assert not same(sp.diff(ga, x), x/(1 - x**2)**R(3, 2))
assert sp.N(sp.diff(fa, x).subs(x, R(3, 5))) == 0.25
L4 = ["נגדיר $f(x)=\\arcsin x-x$; $f'(x)=\\frac{1}{\\sqrt{1-x^2}}-1>0$ בקטע $(0,1)$ ו-$f(0)=0$, לכן $\\arcsin a>a$.",
      "נגדיר $g(x)=\\frac{x}{\\sqrt{1-x^2}}-\\arcsin x$.",
      "$g'(x)=\\frac{x^2}{(1-x^2)^{3/2}}>0$ בקטע $(0,1)$, ולכן $g$ עולה ממש.",
      "$g(0)=0$ ולכן $g(a)>0$, כלומר $\\arcsin a<\\frac{a}{\\sqrt{1-a^2}}$."]
L4b = list(L4)
L4b[2] = "$g'(x)=\\frac{x}{(1-x^2)^{3/2}}>0$ בקטע $(0,1)$, ולכן $g$ עולה ממש."

add(4, "א",
    rubric=rub(("פונקציית עזר $f(x)=\\arcsin x-x$ והנגזרת $f'(x)=\\frac{1}{\\sqrt{1-x^2}}-1>0$", 3),
               ("מסקנה $\\arcsin a>a$ מ-$f(0)=0$ ומונוטוניות", 2),
               ("פונקציית עזר $g(x)=\\frac{x}{\\sqrt{1-x^2}}-\\arcsin x$ ונגזרתה $\\frac{x^2}{(1-x^2)^{3/2}}>0$", 3),
               ("מסקנה $\\arcsin a<\\frac{a}{\\sqrt{1-a^2}}$ מ-$g(0)=0$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להוכיח רק אחד משני אי-השוויונות.",
              "טעות בנגזרת של $\\frac{x}{\\sqrt{1-x^2}}$: התוצאה היא $\\frac{1}{(1-x^2)^{3/2}}$, ולכן $g'=\\frac{1}{(1-x^2)^{3/2}}-\\frac{1}{(1-x^2)^{1/2}}=\\frac{x^2}{(1-x^2)^{3/2}}$.",
              "לשכוח את $f(0)=0$ ו-$g(0)=0$ שבלעדיהם מונוטוניות לא נותנת סימן."],
    steps=[
        num("מהו $f'\\left(\\frac35\\right)$ עבור $f(x)=\\arcsin x-x$? (עשרוני)", sp.diff(fa, x).subs(x, R(3, 5)),
            "$\\frac{1}{\\sqrt{1-\\frac{9}{25}}}-1=\\frac54-1=0.25>0$.", tol=0.0005),
        num("מהו $g'\\left(\\frac12\\right)$ עבור $g(x)=\\frac{x}{\\sqrt{1-x^2}}-\\arcsin x$? (עשרוני)", sp.diff(ga, x).subs(x, R(1, 2)),
            "$g'(x)=\\frac{x^2}{(1-x^2)^{3/2}}$ ולכן $g'\\left(\\frac12\\right)=\\frac{0.25}{0.75^{1.5}}\\approx0.3849$.", tol=0.001),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L4b, 2,
                "הנגזרת הנכונה היא $\\frac{x^2}{(1-x^2)^{3/2}}$ ולא $\\frac{x}{(1-x^2)^{3/2}}$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: shells about the y-axis, between y = 2x and y = x^2 =====
x4 = sorted(sp.solve(sp.Eq(x**2, 2*x), x))
assert x4 == [0, 2] and all(2*v >= v**2 for v in (0, R(1, 2), 1, R(3, 2), 2))
V4 = 2*sp.pi*sp.integrate(x*(2*x - x**2), (x, 0, 2))
assert V4 == 8*sp.pi/3
I4 = sp.integrate(2*x**2 - x**3, (x, 0, 2))
assert I4 == R(4, 3)
cands4 = [2*sp.pi*sp.integrate(x*(x**2 - 2*x), (x, 0, 2)), sp.pi*sp.integrate((2*x)**2 - (x**2)**2, (x, 0, 2)),
          2*sp.pi*sp.integrate(x**2*(2*x - x**2), (x, 0, 2))]
assert all(sp.simplify(c - V4) != 0 for c in cands4)

add(4, "ב",
    rubric=rub(("נקודות חיתוך $x=0$ ו-$x=2$ וקביעה ש-$2x\\ge x^2$ בקטע", 3),
               ("נוסחת הקליפות $V=2\\pi\\int_0^2x\\left(2x-x^2\\right)dx$", 3),
               ("חישוב האינטגרל $\\frac43$", 2),
               ("תשובה $V=\\frac{8\\pi}{3}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להשתמש בנוסחת הדיסקות $\\pi\\int y^2$ כשהסיבוב סביב ציר ה-$y$ והפונקציות ב-$x$.",
              "לכתוב את ההפרש בסדר הפוך ($x^2-2x$) ולקבל נפח שלילי.",
              "לשכוח את הגורם $x$ (רדיוס הקליפה) בתוך האינטגרל."],
    steps=[
        num("מהו ערך $x$ החיובי שבו נפגשים $y=2x$ ו-$y=x^2$?", x4[1], "$x^2=2x$ נותן $x=0$ או $x=2$."),
        ch("איזה אינטגרל נותן את נפח הסיבוב סביב ציר ה-$y$?", "$2\\pi\\int_0^2x\\left(2x-x^2\\right)dx$",
           ["$2\\pi\\int_0^2x\\left(x^2-2x\\right)dx$", "$\\pi\\int_0^2\\left((2x)^2-\\left(x^2\\right)^2\\right)dx$", "$2\\pi\\int_0^2x^2\\left(2x-x^2\\right)dx$"],
           "קליפות: רדיוס $x$, גובה $2x-x^2\\ge0$. ערכי שלוש האפשרויות האחרות שונים מ-$\\frac{8\\pi}{3}$ (חושב ב-sympy)."),
        num("מהו $\\int_0^2\\left(2x^2-x^3\\right)dx$? (עשרוני)", I4, "$\\left(\\frac{2x^3}{3}-\\frac{x^4}{4}\\right)\\Big|_0^2=\\frac{16}{3}-4=\\frac43\\approx1.3333$.", tol=0.001),
        num("מהו הנפח $V$? (עשרוני)", V4, "$V=2\\pi\\cdot\\frac43=\\frac{8\\pi}{3}\\approx8.3776$.", tol=0.001),
    ],
    stepsSource="ai-verified")

# ===== Q5a: lim_{x->inf} ln(1+1/x)/sin(3/x) =====
assert sp.limit(sp.log(1 + 1/x)/sp.sin(3/x), x, sp.oo) == R(1, 3)
assert sp.limit(sp.log(1 + 1/x), x, sp.oo) == 0 and sp.limit(sp.sin(3/x), x, sp.oo) == 0

add(5, "א",
    rubric=rub(("זיהוי $\\frac00$ כש-$x\\to\\infty$", 2),
               ("לופיטל: גזירת המונה והמכנה עם כלל שרשרת", 4),
               ("צמצום $\\frac{-1/x^2}{-3/x^2}$ והצבה", 2),
               ("ערך הגבול $\\frac13$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את כלל השרשרת: $\\left(\\frac1x\\right)'=-\\frac{1}{x^2}$ מופיע גם במונה וגם במכנה.",
              "לשכוח את הגורם הפנימי $-\\frac{3}{x^2}$ בגזירת $\\sin\\frac3x$, ולקבל $\\frac{-1/(x^2+x)}{\\cos(3/x)}\\to0$ במקום $\\frac13$.",
              "להתבלבל בין הצורה כשהמשתנה הולך לאינסוף לבין הצורה כשהוא הולך ל-$0$."],
    steps=[
        ch("מה סוג הצורה הלא מסוימת של $\\frac{\\ln\\left(1+\\frac1x\\right)}{\\sin\\left(\\frac3x\\right)}$ כאשר $x\\to+\\infty$?", "$\\frac00$",
           ["$\\frac\\infty\\infty$", "$1^\\infty$", "$\\infty\\cdot0$"],
           "$\\ln\\left(1+\\frac1x\\right)\\to\\ln1=0$ ו-$\\sin\\frac3x\\to\\sin0=0$ (sympy)."),
        num("מהו ערך הגבול? (עשרוני)", R(1, 3), "אחרי לופיטל: $\\frac{\\frac{1}{1+1/x}}{3\\cos(3/x)}\\to\\frac13\\approx0.3333$.", tol=0.0005),
    ],
    stepsSource="ai-verified")

# ===== Q5b: int (e^-x - e^x)/(e^-x + e^x) dx =====
I5 = (sp.exp(-x) - sp.exp(x))/(sp.exp(-x) + sp.exp(x))
F5 = x - sp.log(1 + sp.exp(2*x))
assert same(sp.diff(F5, x), I5)
v5 = sp.integrate(I5, (x, 0, 1))
assert abs(sp.N(v5 - (F5.subs(x, 1) - F5.subs(x, 0)))) < 1e-12

add(5, "ב",
    rubric=rub(("כתיבת המונה כ-$\\left(e^{-x}+e^x\\right)-2e^x$ ופיצול ל-$1-\\frac{2e^x}{e^{-x}+e^x}$", 3),
               ("הצבה $t=e^x$ והגעה ל-$\\int\\frac{t}{t^2+1}dt$", 3),
               ("חישוב $\\frac12\\ln\\left(1+t^2\\right)$ עם המקדם $2$", 2),
               ("תשובה $x-\\ln\\left(1+e^{2x}\\right)+C$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח לכפול את המונה והמכנה ב-$e^x$ (או לעבוד עם $t=e^x$) ולהישאר עם $e^{-x}$.",
              "לכתוב $\\ln\\left(1+x^2\\right)$ במקום $\\ln\\left(1+e^{2x}\\right)$: צריך להחזיר את $t=e^x$.",
              "לשכוח את הגורם $2$ שלפני האינטגרל השני."],
    steps=[
        chx("איזו הצגה של האינטגרנד מתאימה לפיצול?", 1 - 2*sp.exp(x)/(sp.exp(-x) + sp.exp(x)),
            [1 + 2*sp.exp(x)/(sp.exp(-x) + sp.exp(x)), 1 - sp.exp(x)/(sp.exp(-x) + sp.exp(x)), -1 + 2*sp.exp(x)/(sp.exp(-x) + sp.exp(x))],
            lambda e: same(e, I5), "$\\frac{e^{-x}-e^x}{e^{-x}+e^x}=\\frac{\\left(e^{-x}+e^x\\right)-2e^x}{e^{-x}+e^x}=1-\\frac{2e^x}{e^{-x}+e^x}$ (אומת ב-sympy)."),
        chx("מהי הקדומה? (בלי הקבוע)", F5,
            [x - sp.log(1 + sp.exp(x)), x - 2*sp.log(1 + sp.exp(2*x)), x - sp.log(1 + x**2)],
            lambda e: same(sp.diff(e, x), I5), "אחרי $t=e^x$: $x-2\\cdot\\frac12\\ln(1+t^2)=x-\\ln\\left(1+e^{2x}\\right)$; הנגזרת של כל אפשרות נבדקה ב-sympy."),
        num("כבדיקה: מהו $\\int_0^1\\frac{e^{-x}-e^x}{e^{-x}+e^x}dx$? (עשרוני)", v5,
            "$1-\\ln\\frac{1+e^2}{2}\\approx-0.4337$ (חושב ב-sympy).", tol=0.001),
    ],
    stepsSource="ai-verified")

# ===== Q6a: arc length of ln(sin x) on [pi/3, pi/2] =====
f6 = sp.log(sp.sin(x))
samples6 = (R(11, 10), R(13, 10), R(3, 2))
integrand6 = lambda e: all(abs(sp.N(e.subs(x, v) - sp.sqrt(1 + sp.diff(f6, x)**2).subs(x, v))) < 1e-9 for v in samples6)
L6 = sp.N(sp.Integral(sp.sqrt(1 + sp.diff(f6, x)**2), (x, sp.pi/3, sp.pi/2)))
assert abs(L6 - sp.N(sp.log(sp.sqrt(3)))) < 1e-8 and abs(L6 - 0.5493) < 1e-4
assert same(sp.diff(f6, x), sp.cot(x))

add(6, "א",
    rubric=rub(("נוסחת אורך הקשת $L=\\int_a^b\\sqrt{1+f'(x)^2}dx$ ונגזרת $f'(x)=\\cot x$", 3),
               ("פישוט $\\sqrt{1+\\cot^2x}=\\frac{1}{\\sin x}$ (חיובי בקטע)", 3),
               ("אינטגרל $\\int\\frac{dx}{\\sin x}=\\ln\\left|\\tan\\frac x2\\right|$", 2),
               ("הצבת הגבולות ותשובה $\\ln\\sqrt3\\approx0.5493$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את ההעלאה בריבוע של $f'$ בתוך השורש.",
              "לכתוב $\\sqrt{1+\\cot^2x}=\\cot x$ או $\\csc^2x$ במקום $\\frac{1}{\\sin x}$: צריך שורש של $\\csc^2x$.",
              "לשכוח שהקדומה של $\\frac{1}{\\sin x}$ היא $\\ln\\left|\\tan\\frac x2\\right|$ ולא $\\ln|\\sin x|$."],
    steps=[
        num("מהו $f'\\left(\\frac\\pi3\\right)$ עבור $f(x)=\\ln(\\sin x)$? (עשרוני)", sp.cot(sp.pi/3), "$f'(x)=\\cot x$ ו-$\\cot\\frac\\pi3=\\frac{1}{\\sqrt3}\\approx0.5774$.", tol=0.001),
        chx("מהו $\\sqrt{1+f'(x)^2}$ בקטע $\\left[\\frac\\pi3,\\frac\\pi2\\right]$?", 1/sp.sin(x),
            [1/sp.cos(x), sp.cos(x)/sp.sin(x), sp.sin(x)], integrand6,
            "$1+\\cot^2x=\\frac{1}{\\sin^2x}$ ובקטע $\\sin x>0$ ולכן השורש הוא $\\frac{1}{\\sin x}$ (נבדק ב-sympy בנקודות בקטע)."),
        num("מהו אורך הקשת? (עשרוני)", L6, "$\\ln\\left|\\tan\\frac x2\\right|\\Big|_{\\pi/3}^{\\pi/2}=\\ln1-\\ln\\frac{1}{\\sqrt3}\\approx0.5493$.", tol=0.001),
    ],
    stepsSource="ai-verified")

# ===== Q6b: unique real root of arctan x + x^3 + x^5 - 2 =====
f6b = sp.atan(x) + x**3 + x**5 - 2
f6bp = sp.diff(f6b, x)
assert same(f6bp, 1/(1 + x**2) + 3*x**2 + 5*x**4)
assert f6b.subs(x, 0) == -2 and same(f6b.subs(x, 1), sp.pi/4)
assert all(sp.N(f6bp.subs(x, v)) > 0 for v in (-3, -1, 0, R(1, 2), 2))
L6b_ = ["$f(x)=\\arctan x+x^3+x^5-2$ רציפה בקטע $[0,1]$.",
        "$f(0)=-2<0$ ו-$f(1)=\\frac\\pi4>0$, לכן לפי משפט ערך הביניים יש שורש ב-$(0,1)$.",
        "$f'(x)=\\frac{1}{1+x^2}+3x^2+5x^4>0$ לכל $x$, ולכן $f$ עולה ממש.",
        "פונקציה עולה ממש חותכת את ציר ה-$x$ לכל היותר פעם אחת, ולכן השורש יחיד."]
L6b_bug = list(L6b_)
L6b_bug[2] = "$f'(x)=\\frac{1}{1+x^2}+3x^2-5x^4>0$ לכל $x$, ולכן $f$ עולה ממש."
assert not same(1/(1 + x**2) + 3*x**2 - 5*x**4, f6bp)

add(6, "ב",
    rubric=rub(("הגדרת $f(x)=\\arctan x+x^3+x^5-2$ ורציפותה", 2),
               ("$f(0)=-2<0$ ו-$f(1)=\\frac\\pi4>0$ וקיום שורש לפי ערך הביניים", 3),
               ("נגזרת חיובית $f'(x)=\\frac{1}{1+x^2}+3x^2+5x^4>0$", 3),
               ("מסקנה: $f$ עולה ממש ולכן השורש יחיד", 2)),
    rubricSource="ai-verified",
    pitfalls=["להסתפק בערך הביניים: הוא נותן קיום בלבד, ויחידות דורשת מונוטוניות.",
              "לטעות בנגזרת של $\\arctan x$: היא $\\frac{1}{1+x^2}$.",
              "להראות $f'>0$ רק בקטע $(0,1)$ ולא על כל הישר, ולכן לא לשלול שורשים אחרים מחוץ לקטע."],
    steps=[
        num("מהו $f(0)$ עבור $f(x)=\\arctan x+x^3+x^5-2$?", f6b.subs(x, 0), "$\\arctan0+0+0-2=-2$."),
        num("מהו $f(1)$? (עשרוני)", f6b.subs(x, 1), "$\\frac\\pi4+1+1-2=\\frac\\pi4\\approx0.7854$.", tol=0.001),
        ch("מה מבטיח שהשורש יחיד?", "$f'(x)>0$ לכל $x$, ולכן $f$ עולה ממש",
           ["$f$ רציפה בקטע $[0,1]$", "$f(0)<0<f(1)$", "$f(1)>0$"],
           "רציפות וסימנים הפוכים נותנים קיום בלבד. יחידות נובעת ממונוטוניות חזקה, וזו נובעת מ-$f'>0$ (נבדק ב-sympy בנקודות שונות)."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L6b_bug, 2,
                "הנגזרת הנכונה היא $\\frac{1}{1+x^2}+3x^2+5x^4$ ולא עם $-5x^4$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "23B-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ג, מועד ב'",
    "year": 2023,
    "examDate": "10/07/2023",
    "sourceFile": "calculus-1/23B-B exam+solution.pdf",
    "solutionFile": "calculus-1/23B-B exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

# -*- coding: utf-8 -*-
"""Generator for tools/raw/25B-B.json -- calculus-1 (20151), semester B 2025, moed B (11/08/2025).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_25B-B.py

Source: sitting 25B-B, pp.1-2 (scanned exam only, NO solution or key anywhere). Six questions, 25% each,
solve 4 (Q1 is a single 25% investigation; Q2-Q6 have a 13% and a 12% part).

Solutions: written by the solver (2026-10-18), solutionSource "solved", official False, confidence high. No partial
evidence exists (no key, no tutor marks). Every answer is checked in tools/verify/25B-B/check.py (sympy, 0 mismatches);
the Q1 graph is rendered by tools/verify/25B-B/plot_q1.py (images/exams/25B-B-Q1-graph.png).
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25B-B.json"
SOL = {}


def Q(num, kind, topic, question, part=None, points=None):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": SOL[(num, part)].strip("\n"),
         "solutionSource": "solved", "official": False, "confidence": "high"}
    if part:
        q["part"] = part
    if points:
        q["points"] = points
    return q



SOL[(1, None)] = r"""
**א. תחום הגדרה:** $x\neq2$.
**ב. נקודות חיתוך עם הצירים:** $f(x)=0\iff x=0$ (כי $e^{\frac{1}{x-2}}>0$), ולכן נקודת החיתוך היחידה היא $(0,0)$.
**ג. תחומי עליה וירידה, נקודות קיצון:**
$$f'(x)=e^{\frac{1}{x-2}}+x\cdot e^{\frac{1}{x-2}}\cdot\left(-\frac{1}{(x-2)^2}\right)=e^{\frac{1}{x-2}}\cdot\frac{(x-2)^2-x}{(x-2)^2}=e^{\frac{1}{x-2}}\cdot\frac{(x-1)(x-4)}{(x-2)^2}$$
$f'(x)=0$ עבור $x=1$ ו-$x=4$. טבלת סימן של $f'$: חיובית כאשר $x<1$, שלילית כאשר $1<x<2$ וגם $2<x<4$, וחיובית כאשר $x>4$.
$f$ עולה ב-$(-\infty,1)$ וב-$(4,\infty)$, ויורדת ב-$(1,2)$ וב-$(2,4)$.
נקודת מקסימום מקומי: $\left(1,\frac{1}{e}\right)$. נקודת מינימום מקומי: $\left(4,4\sqrt{e}\right)$.
**ד. תחומי קמירות וקעירות, נקודות פיתול:**
$$f''(x)=e^{\frac{1}{x-2}}\left(-\frac{1}{(x-2)^2}\cdot\frac{x^2-5x+4}{(x-2)^2}+\frac{x+2}{(x-2)^3}\right)=e^{\frac{1}{x-2}}\cdot\frac{(x+2)(x-2)-\left(x^2-5x+4\right)}{(x-2)^4}=e^{\frac{1}{x-2}}\cdot\frac{5x-8}{(x-2)^4}$$
טבלת סימן של $f''$: שלילית כאשר $x<\frac{8}{5}$ (הגרף קעור, $\cap$), חיובית כאשר $\frac{8}{5}<x<2$ וגם $x>2$ (הגרף קמור, $\cup$).
נקודת פיתול: $\left(\frac{8}{5},\frac{8}{5}e^{-\frac{5}{2}}\right)\approx(1.6,\ 0.13)$.
**ה. אסימפטוטות:**
1. אנכית: כאשר $x\to2^+$ מתקיים $\frac{1}{x-2}\to+\infty$ ולכן $\lim_{x\to2^+}f(x)=+\infty$: הישר $x=2$ הוא אסימפטוטה אנכית (מימין). כאשר $x\to2^-$ מתקיים $\frac{1}{x-2}\to-\infty$ ולכן $\lim_{x\to2^-}f(x)=2\cdot0=0$ (הגרף מתקרב לנקודה $(2,0)$ שאינה שייכת לגרף).
2. משופעת $y=ax+b$ ב-$\pm\infty$:
$$a=\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim_{x\to\pm\infty}e^{\frac{1}{x-2}}=e^0=1$$
$$b=\lim_{x\to\pm\infty}\left(f(x)-x\right)=\lim_{x\to\pm\infty}x\left(e^{\frac{1}{x-2}}-1\right)=\lim_{x\to\pm\infty}\frac{e^{\frac{1}{x-2}}-1}{\frac{1}{x-2}}\cdot\frac{x}{x-2}=1\cdot1=1$$
(השתמשנו בגבול $\lim_{u\to0}\frac{e^u-1}{u}=1$ עם $u=\frac{1}{x-2}\to0$.) לכן $y=x+1$ היא אסימפטוטה משופעת ב-$\pm\infty$.
**ו. שרטוט:**
![גרף הפונקציה f(x)=x e^(1/(x-2)): מקסימום ב-(1,1/e), מינימום ב-(4,4√e), פיתול ב-x=8/5, אסימפטוטות x=2 (מימין) ו-y=x+1](images/exams/25B-B-Q1-graph.png)
"""

SOL[(2, "א")] = r"""
**חסימות מלמעלה:** נוכיח באינדוקציה ש-$0<a_n<5$.
בסיס: $a_1=\sqrt{20}<\sqrt{25}=5$.
צעד: אם $0<a_n<5$ אז $a_{n+1}=\sqrt{20+a_n}<\sqrt{20+5}=5$, וכמובן $a_{n+1}>0$.
**מונוטוניות:** הסדרה עולה, כי
$$a_{n+1}>a_n\iff20+a_n>a_n^2\iff a_n^2-a_n-20<0\iff(a_n-5)(a_n+4)<0$$
והאי-שוויון האחרון מתקיים כי $0<a_n<5$.
**הגבול:** הסדרה עולה וחסומה מלמעלה ולכן מתכנסת. נסמן $\lim_{n\to\infty}a_n=L$ ונעבור לגבול בנוסחת הנסיגה:
$$L=\sqrt{20+L}\ \Rightarrow\ L^2-L-20=0\ \Rightarrow\ (L-5)(L+4)=0$$
מכיוון ש-$a_n>0$ מתקיים $L\ge0$, ולכן $L=5$:
$$\lim_{n\to\infty}a_n=5$$
"""

SOL[(2, "ב")] = r"""
אינטגרציה בחלקים עם $u=\arctan x$, $dv=(4x+6)\,dx$. נבחר את הפונקציה הקדומה $v=2x^2+6x+2=2\left(x^2+1\right)+6x$ (מותר להוסיף קבוע ל-$v$, והבחירה הזו מקצרת את החישוב):
$$\int(4x+6)\arctan x\,dx=\left(2x^2+6x+2\right)\arctan x-\int\frac{2\left(x^2+1\right)+6x}{1+x^2}\,dx=$$
$$=\left(2x^2+6x+2\right)\arctan x-\int\left(2+\frac{6x}{1+x^2}\right)dx=\left(2x^2+6x+2\right)\arctan x-2x-3\ln\left(1+x^2\right)+C$$
"""

SOL[(3, "א")] = r"""
זהו גבול מהצורה $\infty^0$. נכתוב
$$\left(\frac{1}{x}\right)^{\tan2x}=e^{\tan2x\cdot\ln\frac{1}{x}}=e^{-\tan2x\cdot\ln x}$$
ונחשב את הגבול של המעריך (צורה $0\cdot\infty$, ואחר כך כלל לופיטל):
$$\lim_{x\to0^+}\tan2x\cdot\ln x=\lim_{x\to0^+}\frac{\ln x}{\cot2x}\left[\frac{\infty}{\infty}\right]=\lim_{x\to0^+}\frac{\frac{1}{x}}{-\frac{2}{\sin^22x}}=\lim_{x\to0^+}\left(-\frac{\sin^22x}{2x}\right)=\lim_{x\to0^+}\left(-\frac{\sin2x}{2x}\cdot\sin2x\right)=-1\cdot0=0$$
לכן
$$\lim_{x\to0^+}\left(\frac{1}{x}\right)^{\tan2x}=e^{0}=1$$
"""

SOL[(3, "ב")] = r"""
בנקודה $x=\frac{\pi}{4}$: $y\left(\frac{\pi}{4}\right)=1^{\frac{\sqrt{2}}{2}}=1$.
גזירה לוגריתמית: $\ln y=\cos x\cdot\ln(\tan x)$, ולכן
$$\frac{y'}{y}=-\sin x\cdot\ln(\tan x)+\cos x\cdot\frac{1}{\tan x}\cdot\frac{1}{\cos^2x}=-\sin x\cdot\ln(\tan x)+\frac{1}{\sin x}$$
$$y'=(\tan x)^{\cos x}\left(\frac{1}{\sin x}-\sin x\cdot\ln(\tan x)\right)$$
$$y'\left(\frac{\pi}{4}\right)=1\cdot\left(\frac{1}{\frac{\sqrt{2}}{2}}-\frac{\sqrt{2}}{2}\cdot\ln1\right)=\sqrt{2}$$
משוואת המשיק:
$$y-1=\sqrt{2}\left(x-\frac{\pi}{4}\right)\quad\Longleftrightarrow\quad y=\sqrt{2}\,x+1-\frac{\sqrt{2}\,\pi}{4}$$
"""

SOL[(4, "א")] = r"""
צורה $\frac{0}{0}$. נכפיל את המונה ואת המכנה בצמודים:
$$\sqrt{x+2}-\sqrt{3x-2}=\frac{(x+2)-(3x-2)}{\sqrt{x+2}+\sqrt{3x-2}}=\frac{2(2-x)}{\sqrt{x+2}+\sqrt{3x-2}}$$
$$\sqrt{4x+1}-\sqrt{5x-1}=\frac{(4x+1)-(5x-1)}{\sqrt{4x+1}+\sqrt{5x-1}}=\frac{2-x}{\sqrt{4x+1}+\sqrt{5x-1}}$$
לכן, אחרי צמצום $2-x\neq0$:
$$\lim_{x\to2}\frac{\sqrt{x+2}-\sqrt{3x-2}}{\sqrt{4x+1}-\sqrt{5x-1}}=\lim_{x\to2}\frac{2\left(\sqrt{4x+1}+\sqrt{5x-1}\right)}{\sqrt{x+2}+\sqrt{3x-2}}=\frac{2(3+3)}{2+2}=3$$
"""

SOL[(4, "ב")] = r"""
משוואת המשיק בנקודה $(2,4)$: $f'(x)=2x$, $f'(2)=4$, ולכן $y-4=4(x-2)$, כלומר $y=4x-4$. המשיק חותך את ציר ה-$X$ ב-$x=1$.
התחום חסום מלמעלה על ידי הפרבולה, ומלמטה על ידי ציר ה-$X$ (עבור $0\le x\le1$) ועל ידי המשיק (עבור $1\le x\le2$). לכן
$$S=\int_0^2x^2\,dx-\int_1^2(4x-4)\,dx=\frac{x^3}{3}\Big|_0^2-\left(2x^2-4x\right)\Big|_1^2=\frac{8}{3}-\left(0-(-2)\right)=\frac{8}{3}-2=\frac{2}{3}$$
(האינטגרל השני הוא שטח המשולש שקודקודיו $(1,0)$, $(2,0)$, $(2,4)$, כלומר $\frac{1\cdot4}{2}=2$.)
"""

SOL[(5, "א")] = r"""
נגדיר $f(x)=e^{\sin^2x}$. הפונקציה רציפה וגזירה בכל $\mathbb{R}$, ו-
$$f'(x)=e^{\sin^2x}\cdot2\sin x\cos x=e^{\sin^2x}\sin2x$$
לפי משפט לגרנז' על הקטע $[a,b]$ קיימת $c\in(a,b)$ כך ש-
$$e^{\sin^2b}-e^{\sin^2a}=f'(c)(b-a)=e^{\sin^2c}\sin2c\cdot(b-a)$$
מכיוון ש-$\sin^2c\le1$ ו-$\sin2c\le1$, מתקיים $e^{\sin^2c}\sin2c\le e^{\sin^2c}\le e$ (אם $\sin2c<0$ המכפלה שלילית וודאי קטנה מ-$e$). מכיוון ש-$b-a>0$:
$$e^{\sin^2b}-e^{\sin^2a}\le e(b-a)$$
"""

SOL[(5, "ב")] = r"""
הצבה $t=\cos x$, $dt=-\sin x\,dx$:
$$\int\frac{\sin x\,dx}{5+2\cos x+\cos^2x}=-\int\frac{dt}{t^2+2t+5}=-\int\frac{dt}{(t+1)^2+4}=-\frac{1}{2}\arctan\frac{t+1}{2}+C=-\frac{1}{2}\arctan\frac{\cos x+1}{2}+C$$
"""

SOL[(6, "א")] = r"""
נקודות החיתוך של חצי המעגל עם הישר: $\sqrt{25-x^2}=3\iff x^2=16\iff x=\pm4$. בקטע $-4\le x\le4$ חצי המעגל נמצא מעל הישר $y=3$.
שיטת הטבעות (דיסקה עם חור):
$$V=\pi\int_{-4}^{4}\left(\left(\sqrt{25-x^2}\right)^2-3^2\right)dx=\pi\int_{-4}^{4}\left(16-x^2\right)dx=2\pi\left(16x-\frac{x^3}{3}\right)\Big|_0^4=2\pi\left(64-\frac{64}{3}\right)=\frac{256\pi}{3}$$
"""

SOL[(6, "ב")] = r"""
**רציפות ב-$x=0$:** $f(0)=\sin0=0$, $\lim_{x\to0^-}\sin(ax)=0$, ו-$\lim_{x\to0^+}x^2\ln x=0$ (לפי לופיטל: $\lim_{x\to0^+}\frac{\ln x}{x^{-2}}=\lim_{x\to0^+}\frac{x^{-1}}{-2x^{-3}}=\lim_{x\to0^+}\left(-\frac{x^2}{2}\right)=0$). לכן $f$ רציפה ב-$0$ לכל $a$.
**נגזרות חד-צדדיות:**
$$f'_-(0)=\lim_{x\to0^-}\frac{\sin(ax)-0}{x}=a$$
(עבור $a\neq0$: $a\cdot\frac{\sin(ax)}{ax}\to a$; עבור $a=0$ המונה זהותית $0$ והגבול $0=a$.)
$$f'_+(0)=\lim_{x\to0^+}\frac{x^2\ln x-0}{x}=\lim_{x\to0^+}x\ln x=0$$
$f$ גזירה ב-$0$ אם ורק אם $f'_-(0)=f'_+(0)$, כלומר $a=0$ (ואז $f'(0)=0$).
"""


questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=x\cdot e^{\frac{1}{x-2}}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, "
      "תחומי עליה וירידה, נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.", points=25),

    Q(2, "proof", "sequences_limits",
      "נתונה הסדרה: " r"$a_1=\sqrt{20}$ ו-$a_{n+1}=\sqrt{20+a_n}$." "\nהוכיחו כי הסדרה מתכנסת וחשבו את גבולה.",
      part="א", points=13),
    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int(4x+6)\arctan x\,dx$.", part="ב", points=12),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0^+}\left(\frac{1}{x}\right)^{\tan 2x}$.", part="א", points=13),
    Q(3, "computation", "derivatives_tangents",
      r"מצאו את משוואת המשיק של גרף הפונקציה: $y=(\tan x)^{\cos x}$ בנקודה $x=\frac{\pi}{4}$.", part="ב", points=12),

    Q(4, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to2}\frac{\sqrt{x+2}-\sqrt{3x-2}}{\sqrt{4x+1}-\sqrt{5x-1}}$.", part="א", points=13),
    Q(4, "computation", "definite_integrals",
      r'חשבו את שטח התחום שחסום ע"י גרף הפונקציה $f(x)=x^2$, הישר המשיק לגרף הפונקציה $f(x)$ בנקודה $(2,4)$ וציר ה-$X$.',
      part="ב", points=12),

    Q(5, "proof", "mean_value_theorems",
      r"הוכיחו כי מתקיים האי שוויון: $e^{\sin^2 b}-e^{\sin^2 a}\le e(b-a)$, עבור $-\infty<a<b<\infty$.",
      part="א", points=13),
    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\sin(x)\,dx}{5+2\cos(x)+\cos^2(x)}$.", part="ב", points=12),

    Q(6, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום הכלוא בין חצי המעגל $y=\sqrt{25-x^2}$ לבין הישר $y=3$ סביב ציר ה-$X$.",
      part="א", points=13),
    Q(6, "computation", "derivatives_tangents",
      r"נתונה הפונקציה $f(x)=\begin{cases}\sin(ax), & x\le0\\ x^2\ln(x), & x>0\end{cases}$ כאשר $a$ הוא פרמטר ממשי. "
      r"עבור אילו ערכי $a$ הפונקציה תהיה גזירה בנקי $x=0$?",
      part="ב", points=12),
]

# ---- steps / rubric / pitfalls (ai-draft); every value below is computed or asserted with sympy ----
import sympy as sp

IDS = "abcdef"
_rot = [0]
x, t, a, b = sp.symbols('x t a b', real=True)
R = sp.Rational
PTS = (0.35, 0.8, 1.3, 1.9, 2.6, 3.4)


def T(e):
    """TeX of a sympy expression, wrapped in $...$."""
    return "$" + sp.latex(e, ln_notation=True) + "$"


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


def same(e1, e2, pts=PTS, var=None):
    """True iff the two expressions agree (numerically, >= 3 valid sample points) and are never seen to differ."""
    v = var if var is not None else x
    ok_pts = 0
    for p in pts:
        try:
            d = complex(sp.N(e1.subs(v, p) - e2.subs(v, p), 30))
        except Exception:
            continue
        if d != d:
            continue
        if abs(d) > 1e-9:
            return False
        ok_pts += 1
    return ok_pts >= 3


def chx(prompt, good, bads, ok, explain):
    """choice over sympy expressions: ok(e) must hold for the good one and fail for every distractor."""
    assert ok(good), "good option fails its test"
    for e in bads:
        assert not ok(e), "distractor passes the test: %s" % e
    return ch(prompt, T(good), [T(e) for e in bads], explain)


def num(prompt, val, explain, tol=0.001, nd=4):
    f = float(sp.N(val, 30))
    ans = int(round(f)) if abs(f - round(f)) < 1e-12 else round(f, nd)
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


def lim_iter(f, a1, n=40):
    """first n terms of a recursive sequence, exact rationals/floats via sympy Float(50)."""
    seq = [sp.N(a1, 50)]
    for _ in range(n - 1):
        seq.append(sp.N(f(seq[-1]), 50))
    return seq


# ===== Q1: f = x e^{1/(x-2)} =====
E2 = sp.exp(1/(x - 2))
f1 = x*E2
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, E2*(x - 1)*(x - 4)/(x - 2)**2) and same(f1pp, E2*(5*x - 8)/(x - 2)**4)
assert sp.simplify(f1p.subs(x, 1)) == 0 and sp.simplify(f1p.subs(x, 4)) == 0
assert sp.solve(sp.Eq(5*x - 8, 0), x) == [R(8, 5)]
fmax1 = sp.simplify(f1.subs(x, 1)); fmin1 = sp.simplify(f1.subs(x, 4))
assert sp.simplify(fmax1 - sp.exp(-1)) == 0 and sp.simplify(fmin1 - 4*sp.sqrt(sp.E)) == 0
assert sp.limit(f1/x, x, sp.oo) == 1 and sp.limit(f1 - x, x, sp.oo) == 1 and sp.limit(f1 - x, x, -sp.oo) == 1
assert sp.limit(f1, x, 2, '+') == sp.oo and sp.limit(f1, x, 2, '-') == 0

add(1,
    rubric=rub(("תחום הגדרה ($x\\neq2$) ונקודת החיתוך היחידה עם הצירים $(0,0)$", 3),
               ("נגזרת $f'(x)=e^{\\frac{1}{x-2}}\\frac{(x-1)(x-4)}{(x-2)^2}$, נקודות קריטיות $x=1,4$, תחומי עליה וירידה וסיווג הקיצון: מקסימום מקומי $\\left(1,\\frac{1}{e}\\right)$ ומינימום מקומי $\\left(4,4\\sqrt{e}\\right)$", 9),
               ("נגזרת שנייה $f''(x)=e^{\\frac{1}{x-2}}\\frac{5x-8}{(x-2)^4}$, קמירות וקעירות ונקודת פיתול ב-$x=\\frac{8}{5}$", 5),
               ("אסימפטוטה אנכית $x=2$ (מימין) ואסימפטוטה משופעת $y=x+1$", 5),
               ("שרטוט הגרף בהתאם לכל הנתונים", 3)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח שבנגזרת של מכפלה $x\\cdot e^{\\frac{1}{x-2}}$ יש גם נגזרת הפנים $-\\frac{1}{(x-2)^2}$ של המעריך.",
              "לטעות בגבול החד-צדדי ב-$x=2$: משמאל $e^{\\frac{1}{x-2}}\\to0$ ולכן $f\\to0$ (אין אסימפטוטה), ורק מימין $f\\to+\\infty$.",
              "לחשב את האסימפטוטה המשופעת בלי הגבול $\\lim_{u\\to0}\\frac{e^u-1}{u}=1$ ולהסיק בטעות $b=0$."],
    steps=[
        chx("מהי הנגזרת של $f(x)=x\\cdot e^{\\frac{1}{x-2}}$?", E2*(x - 1)*(x - 4)/(x - 2)**2,
            [E2*(x - 1)*(x + 4)/(x - 2)**2, E2*(x - 1)*(x - 4)/(x - 2), E2*(x + 1)*(x - 4)/(x - 2)**2],
            lambda e: same(e, f1p),
            "גזירת מכפלה: $f'=e^{\\frac{1}{x-2}}\\left(1-\\frac{x}{(x-2)^2}\\right)=e^{\\frac{1}{x-2}}\\frac{(x-1)(x-4)}{(x-2)^2}$ (אומת ב-sympy)."),
        num("מהו ערך הפונקציה בנקודת המקסימום המקומי $x=1$? (עשרוני)", fmax1,
            "$f(1)=e^{-1}\\approx0.3679$."),
        num("מהו ערך הפונקציה בנקודת המינימום המקומי $x=4$? (עשרוני)", fmin1,
            "$f(4)=4e^{\\frac{1}{2}}=4\\sqrt{e}\\approx6.5949$."),
        num("באיזה $x$ מתאפסת $f''(x)=e^{\\frac{1}{x-2}}\\frac{5x-8}{(x-2)^4}$ ומשנה סימן? (עשרוני)", R(8, 5),
            "$5x-8=0$ נותן $x=\\frac{8}{5}=1.6$; שם $f''$ משנה סימן משלילי לחיובי, ולכן זו נקודת פיתול."),
        ch("מהי האסימפטוטה המשופעת של $f$ ב-$\\pm\\infty$?", "$y=x+1$",
           ["$y=x$", "$y=x-1$", "$y=x+2$", "אין אסימפטוטה משופעת"],
           "$a=\\lim\\frac{f}{x}=\\lim e^{\\frac{1}{x-2}}=1$ ו-$b=\\lim x\\left(e^{\\frac{1}{x-2}}-1\\right)=1$, כי $\\frac{e^u-1}{u}\\to1$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: a_1 = sqrt(20), a_{n+1} = sqrt(20 + a_n) =====
seq2 = lim_iter(lambda v: sp.sqrt(20 + v), sp.sqrt(20))
assert all(v < 5 for v in seq2) and all(seq2[i + 1] > seq2[i] for i in range(len(seq2) - 1))
for bd in (4, R(9, 2), R(49, 10)):
    assert any(v >= bd for v in seq2), bd
L_ = sp.Symbol('L', positive=True)
assert sp.solve(sp.Eq(L_, sp.sqrt(20 + L_)), L_) == [5]
an = sp.Symbol('a_n', real=True)
assert sp.expand((an - 5)*(an + 4) - (an**2 - an - 20)) == 0
assert sp.expand((an - 4)*(an + 5) - (an**2 - an - 20)) != 0

L2a = [r"חסימות באינדוקציה: $a_1=\sqrt{20}<5$, ואם $0<a_n<5$ אז $a_{n+1}=\sqrt{20+a_n}<\sqrt{25}=5$; לכן $0<a_n<5$ לכל $n$.",
       r"מונוטוניות: $a_{n+1}>a_n\iff(a_n-5)(a_n+4)<0$, וזה מתקיים כי $0<a_n<5$; לכן הסדרה עולה.",
       r"הסדרה עולה וחסומה מלמעלה, ולכן מתכנסת לגבול $L$.",
       r"מנוסחת הנסיגה $L=\sqrt{20+L}$, כלומר $(L-5)(L+4)=0$, ומכיוון ש-$L\ge0$ מתקבל $L=5$."]

add(2, "א",
    rubric=rub(("הוכחת חסם עליון $a_n<5$ באינדוקציה (בסיס וצעד)", 4),
               ("הוכחת מונוטוניות: $a_{n+1}>a_n\\iff(a_n-5)(a_n+4)<0$ והסקה שהסדרה עולה", 4),
               ("הסקה שסדרה עולה וחסומה מתכנסת", 1),
               ("מעבר לגבול בנוסחת הנסיגה ופתרון $L^2-L-20=0$", 3),
               ("פסילת $L=-4$ ומסקנה $L=5$", 1)),
    rubricSource="ai-verified",
    pitfalls=["לפתור את משוואת הגבול $L=\\sqrt{20+L}$ בלי להוכיח קודם שהגבול קיים.",
              "לשכוח לפסול את הפתרון $L=-4$ אף שכל איברי הסדרה חיוביים.",
              "להוכיח מונוטוניות לפני החסימות: האי-שוויון $(a_n-5)(a_n+4)<0$ נשען על $0<a_n<5$."],
    steps=[
        ch("איזה חסם עליון, מבין האפשרויות, מתקיים לכל איברי הסדרה (והוא גם הגבול)?", "$a_n<5$",
           ["$a_n<4$", "$a_n<4.5$", "$a_n<4.9$"],
           "$a_1=\\sqrt{20}\\approx4.47$ כבר עובר את $4$; האיברים עוברים גם את $4.5$ ו-$4.9$, ורק $5$ נשמר לכל $n$ (נבדק ב-40 האיברים הראשונים)."),
        chx("מהו הביטוי $P(a_n)$ שבו $a_{n+1}>a_n\\iff 20+a_n>a_n^2\\iff P(a_n)<0$?", (an - 5)*(an + 4),
            [(an - 4)*(an + 5), (an - 5)*(an - 4), (an + 5)*(an + 4)],
            lambda e: sp.expand(e - (an**2 - an - 20)) == 0,
            "$20+a_n>a_n^2\\iff a_n^2-a_n-20<0$, ואת זה מפרקים ל-$(a_n-5)(a_n+4)$ (נבדק ב-sympy)."),
        order("סדרו את שלבי ההוכחה.", L2a,
              "קודם החסימות (הן נחוצות לאי-השוויון במונוטוניות), אחר כך המונוטוניות, אחריהן ההתכנסות, ולבסוף חישוב הגבול."),
        num("מהו גבול הסדרה? (הפתרון החיובי של $L^2-L-20=0$)", 5,
            "$(L-5)(L+4)=0$, ומכיוון שהאיברים חיוביים $L=5$."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: int (4x+6) arctan x dx =====
g2b = (4*x + 6)*sp.atan(x)
F2b = (2*x**2 + 6*x + 2)*sp.atan(x) - 2*x - 3*sp.log(1 + x**2)
assert same(sp.diff(F2b, x), g2b)
rem2b = (2*x**2 + 6*x + 2)/(1 + x**2)
assert same(rem2b, 2 + 6*x/(1 + x**2))
def2b = sp.N(F2b.subs(x, 1) - F2b.subs(x, 0), 30)
assert abs(def2b - sp.N(sp.Integral(g2b, (x, 0, 1)), 30)) < 1e-12

add(2, "ב",
    rubric=rub(("בחירת $u=\\arctan x$ ו-$dv=(4x+6)\\,dx$", 3),
               ("נוסחת האינטגרציה בחלקים עם $v=2x^2+6x+2$", 3),
               ("פישוט האינטגרנד הנותר ל-$2+\\frac{6x}{1+x^2}$", 3),
               ("אינטגרציה: $2x+3\\ln(1+x^2)$ ותשובה סופית עם $+C$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לבחור $u=4x+6$ ו-$dv=\\arctan x\\,dx$: אז צריך קודם לחשב קדומה של $\\arctan x$ והחישוב מסתבך.",
              "לשכוח את הפירוק $2x^2+6x+2=2\\left(x^2+1\\right)+6x$ בפישוט, ולהשאיר אינטגרל מורכב יותר.",
              "לשכוח את הגורם $\\frac{1}{2}$ באינטגרל $\\int\\frac{6x}{1+x^2}dx=3\\ln(1+x^2)$."],
    steps=[
        ch("איזו בחירה של $u$ ו-$dv$ משמש הפתרון באינטגרציה בחלקים?",
           "$u=\\arctan x$, $dv=(4x+6)\\,dx$",
           ["$u=4x+6$, $dv=\\arctan x\\,dx$", "$u=(4x+6)\\arctan x$, $dv=dx$", "$u=\\arctan x$, $dv=\\frac{dx}{1+x^2}$"],
           "גוזרים את $\\arctan x$ (הנגזרת רציונלית) ומאנטגרלים את הפולינום; הבחירה ההפוכה דורשת קדומה של $\\arctan x$."),
        chx("לאחר האינטגרציה בחלקים נשאר האינטגרל של $\\frac{2x^2+6x+2}{1+x^2}$. מהו פישוטו?", 2 + 6*x/(1 + x**2),
            [2 + 6/(1 + x**2), 2 + 6*x/(1 + x), 6*x/(1 + x**2)],
            lambda e: same(e, rem2b),
            "$2x^2+6x+2=2(x^2+1)+6x$, ולכן המנה היא $2+\\frac{6x}{1+x^2}$ (נבדק ב-sympy)."),
        chx("מהי התוצאה (בלי הקבוע)?", F2b,
            [(2*x**2 + 6*x + 2)*sp.atan(x) - 2*x - 6*sp.log(1 + x**2),
             (2*x**2 + 6*x + 2)*sp.atan(x) + 2*x + 3*sp.log(1 + x**2),
             (2*x**2 + 6*x)*sp.atan(x) - 2*x - 3*sp.log(1 + x**2)],
            lambda e: same(sp.diff(e, x), g2b),
            "$\\int\\frac{6x}{1+x^2}dx=3\\ln(1+x^2)$; רק האפשרות הנכונה מזדהה עם האינטגרנד אחרי גזירה (נבדק ב-sympy)."),
        num("מהו הערך של האינטגרל המסוים $\\int_0^1(4x+6)\\arctan x\\,dx$? (עשרוני)", def2b,
            "$F(1)-F(0)=\\frac{5\\pi}{2}-2-3\\ln2\\approx3.7745$."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: lim (1/x)^{tan 2x}, x -> 0+ =====
assert sp.limit(sp.tan(2*x)*sp.log(x), x, 0, '+') == 0
assert sp.limit((1/x)**sp.tan(2*x), x, 0, '+') == 1
lh3a = (1/x)/(-2/sp.sin(2*x)**2)
assert same(lh3a, -sp.sin(2*x)**2/(2*x))
assert sp.limit(-sp.sin(2*x)**2/(2*x), x, 0, '+') == 0

add(3, "א",
    rubric=rub(("זיהוי הצורה $\\infty^0$ וכתיבה כ-$e^{\\tan2x\\cdot\\ln\\frac{1}{x}}$", 3),
               ("הפיכת $\\tan2x\\cdot\\ln x$ למנה $\\frac{\\ln x}{\\cot2x}$ מהצורה $\\frac{\\infty}{\\infty}$", 2),
               ("הפעלת לופיטל וקבלת $-\\frac{\\sin^22x}{2x}$", 4),
               ("חישוב גבול המעריך $0$", 2),
               ("תשובה סופית $e^0=1$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להניח ש-$\\infty^0=\\infty$ או $\\infty^0=0$ במקום לפתור את הצורה הלא מוגדרת בעזרת $e^{\\ln}$.",
              "לשכוח את סימן המינוס: $\\ln\\frac{1}{x}=-\\ln x$.",
              "להפעיל לופיטל על $\\tan2x\\cdot\\ln x$ ישירות, בלי להפוך אותו קודם למנה."],
    steps=[
        ch("מהי הצורה הלא מוגדרת של $\\lim_{x\\to0^+}\\left(\\frac{1}{x}\\right)^{\\tan2x}$?", "$\\infty^0$",
           ["$1^\\infty$", "$0^0$", "$\\frac{0}{0}$"],
           "הבסיס $\\frac{1}{x}\\to+\\infty$ והמעריך $\\tan2x\\to0$."),
        chx("אחרי הפיכת המעריך ל-$\\frac{\\ln x}{\\cot2x}$ והפעלת לופיטל, מהי המנה $\\frac{(\\ln x)'}{(\\cot2x)'}$ אחרי פישוט?",
            -sp.sin(2*x)**2/(2*x),
            [sp.sin(2*x)**2/(2*x), -sp.sin(2*x)**2/x, -sp.sin(2*x)/(2*x)],
            lambda e: same(e, lh3a, pts=(0.2, 0.4, 0.7, 1.1, 1.4)),
            "$(\\ln x)'=\\frac{1}{x}$ ו-$(\\cot2x)'=-\\frac{2}{\\sin^22x}$, ולכן המנה היא $-\\frac{\\sin^22x}{2x}$ (נבדק ב-sympy)."),
        num("מהו $\\lim_{x\\to0^+}\\tan2x\\cdot\\ln x$?", 0,
            "$-\\frac{\\sin^22x}{2x}=-\\frac{\\sin2x}{2x}\\cdot\\sin2x\\to-1\\cdot0=0$."),
        num("מהו הגבול $\\lim_{x\\to0^+}\\left(\\frac{1}{x}\\right)^{\\tan2x}$?", 1,
            "הגבול הוא $e^{-0}=e^0=1$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: tangent to y = (tan x)^{cos x} at pi/4 =====
y3 = sp.tan(x)**sp.cos(x)
yp3 = y3*(sp.diff(sp.cos(x)*sp.log(sp.tan(x)), x))
assert abs(sp.N(y3.subs(x, sp.pi/4)) - 1) < 1e-12
slope3 = sp.simplify(yp3.subs(x, sp.pi/4))
assert sp.simplify(slope3 - sp.sqrt(2)) == 0
PTS3 = (0.35, 0.6, 0.8, 1.0, 1.2)
assert same(sp.diff(y3, x), yp3, pts=PTS3)
tl = sp.sqrt(2)*x + 1 - sp.sqrt(2)*sp.pi/4
tl_ok = lambda e: abs(sp.N(e.subs(x, sp.pi/4) - 1)) < 1e-12 and abs(sp.N(sp.diff(e, x) - sp.sqrt(2))) < 1e-12

add(3, "ב",
    rubric=rub(("חישוב ערך הפונקציה בנקודה: $y\\left(\\frac{\\pi}{4}\\right)=1$", 1),
               ("גזירה לוגריתמית: $\\ln y=\\cos x\\ln(\\tan x)$", 3),
               ("$\\frac{y'}{y}=-\\sin x\\ln(\\tan x)+\\frac{1}{\\sin x}$ ופישוט האיבר השני", 3),
               ("חישוב $y'\\left(\\frac{\\pi}{4}\\right)=\\sqrt{2}$", 2),
               ("משוואת המשיק $y=\\sqrt{2}x+1-\\frac{\\sqrt{2}\\pi}{4}$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לגזור $(\\tan x)^{\\cos x}$ ככוח עם מעריך קבוע, או כמעריכית עם בסיס קבוע, במקום גזירה לוגריתמית.",
              "לשכוח את גורם $y$: $\\frac{y'}{y}$ הוא הנגזרת של $\\ln y$, ולכן צריך להכפיל חזרה ב-$y$.",
              "לשכוח ש-$\\ln\\tan\\frac{\\pi}{4}=0$, ולכן האיבר הראשון בנגזרת מתאפס בנקודה."],
    steps=[
        num("מהו ערך הפונקציה $y=(\\tan x)^{\\cos x}$ ב-$x=\\frac{\\pi}{4}$?", 1,
            "$\\tan\\frac{\\pi}{4}=1$ ולכן $y=1^{\\frac{\\sqrt{2}}{2}}=1$."),
        chx("מהי הנגזרת של $\\ln y=\\cos x\\cdot\\ln(\\tan x)$, כלומר $\\frac{y'}{y}$?",
            -sp.sin(x)*sp.log(sp.tan(x)) + 1/sp.sin(x),
            [-sp.sin(x)*sp.log(sp.tan(x)) + 1/sp.cos(x), sp.sin(x)*sp.log(sp.tan(x)) + 1/sp.sin(x),
             -sp.sin(x)/sp.tan(x) + sp.log(sp.tan(x))],
            lambda e: same(e, sp.diff(sp.cos(x)*sp.log(sp.tan(x)), x), pts=PTS3),
            "$\\left(\\ln\\tan x\\right)'=\\frac{1}{\\tan x\\cos^2x}=\\frac{1}{\\sin x\\cos x}$, ולכן האיבר השני הוא $\\cos x\\cdot\\frac{1}{\\sin x\\cos x}=\\frac{1}{\\sin x}$ (נבדק ב-sympy)."),
        num("מהו השיפוע $y'\\left(\\frac{\\pi}{4}\\right)$? (עשרוני)", sp.sqrt(2),
            "$y'=1\\cdot\\left(\\frac{1}{\\sin\\frac{\\pi}{4}}-\\sin\\frac{\\pi}{4}\\cdot\\ln1\\right)=\\sqrt{2}\\approx1.4142$."),
        chx("מהי משוואת המשיק בנקודה $x=\\frac{\\pi}{4}$?", tl,
            [x/sp.sqrt(2) + 1 - sp.pi/(4*sp.sqrt(2)), sp.sqrt(2)*x + 1, sp.sqrt(2)*x - sp.sqrt(2)*sp.pi/4],
            tl_ok,
            "המשיק עובר דרך $\\left(\\frac{\\pi}{4},1\\right)$ בשיפוע $\\sqrt{2}$: $y-1=\\sqrt{2}\\left(x-\\frac{\\pi}{4}\\right)$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: conjugate limit =====
num4 = sp.sqrt(x + 2) - sp.sqrt(3*x - 2)
den4 = sp.sqrt(4*x + 1) - sp.sqrt(5*x - 1)
P4 = (1.2, 2.0, 2.5, 3.1, 4.0)
cn = 2*(2 - x)/(sp.sqrt(x + 2) + sp.sqrt(3*x - 2))
cd = (2 - x)/(sp.sqrt(4*x + 1) + sp.sqrt(5*x - 1))
assert same(num4, cn, pts=P4) and same(den4, cd, pts=P4)
red4 = 2*(sp.sqrt(4*x + 1) + sp.sqrt(5*x - 1))/(sp.sqrt(x + 2) + sp.sqrt(3*x - 2))
assert same(num4/den4, red4, pts=P4) and sp.limit(num4/den4, x, 2) == 3 and red4.subs(x, 2) == 3

add(4, "א",
    rubric=rub(("זיהוי הצורה $\\frac{0}{0}$", 1),
               ("הכפלה בצמוד במונה: $\\frac{2(2-x)}{\\sqrt{x+2}+\\sqrt{3x-2}}$", 3),
               ("הכפלה בצמוד במכנה: $\\frac{2-x}{\\sqrt{4x+1}+\\sqrt{5x-1}}$", 3),
               ("צמצום הגורם $2-x\\neq0$", 3),
               ("הצבת $x=2$ ותשובה $3$", 3)),
    rubricSource="ai-verified",
    pitfalls=["להפעיל לופיטל על ארבעה שורשים: אפשרי אבל מסורבל ופגיע לטעויות. הכפלה בצמוד קצרה יותר.",
              "לחשב $(x+2)-(3x-2)$ בטעות: הנכון $4-2x=2(2-x)$.",
              "לשכוח לצמצם את $2-x$ לפני ההצבה ולהישאר עם $\\frac{0}{0}$."],
    steps=[
        ch("מהי הצורה הלא מוגדרת של הגבול ב-$x\\to2$?", "$\\frac{0}{0}$",
           ["$\\frac{\\infty}{\\infty}$", "$\\infty-\\infty$", "$1^\\infty$"],
           "המונה: $\\sqrt{4}-\\sqrt{4}=0$, המכנה: $\\sqrt{9}-\\sqrt{9}=0$."),
        chx("מהו המונה $\\sqrt{x+2}-\\sqrt{3x-2}$ אחרי הכפלה בצמוד?", cn,
            [(2 - x)/(sp.sqrt(x + 2) + sp.sqrt(3*x - 2)), 2*(x - 2)/(sp.sqrt(x + 2) + sp.sqrt(3*x - 2)),
             2*(2 - x)/(sp.sqrt(x + 2) - sp.sqrt(3*x - 2))],
            lambda e: same(e, num4, pts=P4),
            "$(x+2)-(3x-2)=4-2x=2(2-x)$, והמכנה הוא סכום השורשים (נבדק ב-sympy)."),
        chx("מהו המכנה $\\sqrt{4x+1}-\\sqrt{5x-1}$ אחרי הכפלה בצמוד?", cd,
            [2*(2 - x)/(sp.sqrt(4*x + 1) + sp.sqrt(5*x - 1)), (x - 2)/(sp.sqrt(4*x + 1) + sp.sqrt(5*x - 1)),
             (2 - x)/(sp.sqrt(4*x + 1) - sp.sqrt(5*x - 1))],
            lambda e: same(e, den4, pts=P4),
            "$(4x+1)-(5x-1)=2-x$ (נבדק ב-sympy)."),
        num("מהו הגבול? (אחרי צמצום $2-x$ מציבים $x=2$)", 3,
            "$\\frac{2(3+3)}{2+2}=3$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: area between parabola, tangent at (2,4) and the x-axis =====
tan4 = 4*x - 4
S4 = sp.integrate(x**2, (x, 0, 2)) - sp.integrate(tan4, (x, 1, 2))
assert S4 == R(2, 3) and sp.solve(tan4, x) == [1] and sp.diff(x**2, x).subs(x, 2) == 4
v1 = sp.integrate(x**2, (x, 0, 2)) + sp.integrate(tan4, (x, 1, 2))
v2 = sp.integrate(x**2 - tan4, (x, 0, 2))
v3 = sp.integrate(x**2, (x, 1, 2))
assert (v1, v2, v3) == (R(14, 3), R(8, 3), R(7, 3))

add(4, "ב",
    rubric=rub(("משוואת המשיק ב-$(2,4)$: $y=4x-4$", 3),
               ("נקודת החיתוך של המשיק עם ציר ה-$X$: $x=1$", 1),
               ("בניית השטח: $\\int_0^2x^2dx-\\int_1^2(4x-4)dx$ (או שטח המשולש)", 4),
               ("חישוב $S=\\frac{8}{3}-2=\\frac{2}{3}$", 4)),
    rubricSource="ai-verified",
    pitfalls=["לחשב $\\int_0^2(x^2-(4x-4))dx$: בקטע $[0,1]$ המשיק מתחת לציר ה-$X$, והתחום נחסם שם בציר ולא במשיק.",
              "לחבר במקום לחסר את שטח המשולש מתחת למשיק.",
              "לשכוח שהמשיק חותך את ציר ה-$X$ ב-$x=1$ ולא בראשית."],
    steps=[
        num("מהו שיפוע המשיק לפרבולה $f(x)=x^2$ בנקודה $(2,4)$?", 4, "$f'(x)=2x$, ולכן $f'(2)=4$."),
        num("באיזה $x$ חותך המשיק $y=4x-4$ את ציר ה-$X$?", 1, "$4x-4=0$ נותן $x=1$."),
        ch("איזה ביטוי נותן את שטח התחום?", r"$S=\int_0^2x^2\,dx-\int_1^2(4x-4)\,dx$",
           [r"$S=\int_0^2x^2\,dx+\int_1^2(4x-4)\,dx$", r"$S=\int_0^2\left(x^2-(4x-4)\right)dx$", r"$S=\int_1^2x^2\,dx$"],
           "מתחת לפרבולה בקטע $[0,2]$ נמצא שטח $\\frac{8}{3}$, ומתוכו מוציאים את המשולש מתחת למשיק. ערכי ארבע האפשרויות: $\\frac{2}{3}$, $\\frac{14}{3}$, $\\frac{8}{3}$, $\\frac{7}{3}$ (נבדק ב-sympy)."),
        num("מהו שטח התחום? (עשרוני)", S4, "$\\frac{8}{3}-2=\\frac{2}{3}\\approx0.6667$."),
    ],
    stepsSource="ai-verified")

# ===== Q5a: Lagrange, e^{sin^2 b} - e^{sin^2 a} <= e (b-a) =====
f5 = sp.exp(sp.sin(x)**2)
f5p = sp.exp(sp.sin(x)**2)*sp.sin(2*x)
assert same(sp.diff(f5, x), f5p)
import numpy as _np
_g = _np.linspace(-10, 10, 200001)
assert abs(_np.exp(_np.sin(_g)**2).max() - float(sp.E)) < 1e-6

L5 = [r"הפונקציה $f(x)=e^{\sin^2x}$ רציפה וגזירה ב-$\mathbb{R}$, ו-$f'(x)=e^{\sin^2x}\sin2x$.",
      r"לפי משפט לגרנז' קיימת $c\in(a,b)$ כך ש-$e^{\sin^2b}-e^{\sin^2a}=f'(c)(b-a)$.",
      r"מתקיים $f'(c)=e^{\sin^2c}\sin2c\le e$, כי $\sin2c\le1$ ו-$e^{\sin^2c}\le e$.",
      r"מכיוון ש-$b-a>0$ מתקבל $e^{\sin^2b}-e^{\sin^2a}\le e(b-a)$."]
L5b = list(L5)
L5b[1] = r"לפי משפט לגרנז' קיימת $c\in(a,b)$ כך ש-$e^{\sin^2b}-e^{\sin^2a}=\frac{f'(c)}{b-a}$."

add(5, "א",
    rubric=rub(("הגדרת $f(x)=e^{\\sin^2x}$ ובדיקת רציפות וגזירות בכל קטע $[a,b]$", 3),
               ("חישוב הנגזרת $f'(x)=e^{\\sin^2x}\\sin2x$", 3),
               ("הפעלת משפט לגרנז' וקבלת $f(b)-f(a)=f'(c)(b-a)$", 3),
               ("חסם $f'(c)\\le e$ (מ-$\\sin2c\\le1$ ו-$e^{\\sin^2c}\\le e$)", 3),
               ("הכפלה ב-$b-a>0$ והמסקנה", 1)),
    rubricSource="ai-verified",
    pitfalls=["לגזור $e^{\\sin^2x}$ בלי כלל שרשרת מלא: הנגזרת היא $e^{\\sin^2x}\\cdot2\\sin x\\cos x$.",
              "לחשוש מכך ש-$\\sin2c$ שלילי: החסם $\\sin2c\\le1$ נכון גם אז, והמכפלה פשוט קטנה מ-$e$.",
              "להפעיל את המשפט בלי לציין ש-$f$ גזירה בכל הישר ולכן בכל קטע $[a,b]$."],
    steps=[
        chx("איזו פונקציה $f$ מקיימת $f(b)-f(a)=e^{\\sin^2b}-e^{\\sin^2a}$ לכל $a,b$?", f5,
            [sp.exp(sp.sin(x)), sp.sin(x)**2, sp.exp(x)],
            lambda e: same(sp.diff(e, x), sp.diff(f5, x)),
            "הפונקציה היא $f(x)=e^{\\sin^2x}$ (עד כדי קבוע); ההפרש שלה בין $b$ ל-$a$ הוא בדיוק אגף שמאל של האי-שוויון."),
        chx("מהי הנגזרת $f'(x)$?", f5p,
            [sp.exp(sp.sin(x)**2)*2*sp.sin(x), sp.exp(sp.sin(x)**2)*sp.cos(2*x), sp.exp(sp.sin(x)**2)*sp.sin(x)**2],
            lambda e: same(e, sp.diff(f5, x)),
            "כלל שרשרת: $\\left(e^{\\sin^2x}\\right)'=e^{\\sin^2x}\\cdot2\\sin x\\cos x=e^{\\sin^2x}\\sin2x$ (נבדק ב-sympy)."),
        num("מהו הערך המקסימלי של $e^{\\sin^2c}$? (עשרוני)", sp.E,
            "$\\sin^2c\\le1$, ולכן $e^{\\sin^2c}\\le e\\approx2.7183$, והערך מתקבל ב-$\\sin^2c=1$ (נבדק על רשת צפופה)."),
        order("סדרו את שלבי ההוכחה.", L5,
              "הגדרת הפונקציה והנגזרת, אחר כך משפט לגרנז' (שמגדיר את $c$), אחר כך חסם על $f'(c)$, ולבסוף כפל ב-$b-a$."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L5b, 1,
                "משפט לגרנז' נותן $f(b)-f(a)=f'(c)(b-a)$, לא $\\frac{f'(c)}{b-a}$ (שיפוע המיתר $\\frac{f(b)-f(a)}{b-a}$ הוא שווה ל-$f'(c)$)."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: int sin x / (5 + 2cos x + cos^2 x) =====
g5 = sp.sin(x)/(5 + 2*sp.cos(x) + sp.cos(x)**2)
F5 = -sp.atan((sp.cos(x) + 1)/2)/2
assert same(sp.diff(F5, x), g5)
tt = sp.Symbol('t', real=True)
PX5 = (0.3, 0.7, 1.1, 1.9, 2.4)

add(5, "ב",
    rubric=rub(("הצבה $t=\\cos x$, $dt=-\\sin x\\,dx$", 3),
               ("העברת האינטגרל ל-$-\\int\\frac{dt}{t^2+2t+5}$", 2),
               ("השלמה לריבוע $t^2+2t+5=(t+1)^2+4$", 2),
               ("אינטגרל מסוג $\\arctan$: $-\\frac{1}{2}\\arctan\\frac{t+1}{2}$", 3),
               ("הצבה חוזרת $t=\\cos x$ וקבוע האינטגרציה", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את סימן המינוס שנובע מ-$dt=-\\sin x\\,dx$.",
              "לאנטגרל $\\frac{1}{(t+1)^2+4}$ כ-$\\arctan(t+1)$ ולשכוח את הגורם $\\frac{1}{2}$ ואת החלוקה ב-$2$ בתוך הארקטנגנס.",
              "לנסות הצבה אוניברסלית: מסובך הרבה יותר, כי $\\sin x\\,dx$ ו-$\\cos x$ מרמזים על $t=\\cos x$."],
    steps=[
        ch("איזו הצבה משמש הפתרון?", "$t=\\cos x$",
           ["$t=\\sin x$", "$t=\\tan\\frac{x}{2}$", "$t=5+2\\cos x$"],
           "המונה $\\sin x\\,dx$ הוא $-dt$, והמכנה כולו פולינום ב-$\\cos x$."),
        chx("מהו האינטגרנד אחרי ההצבה $t=\\cos x$ (כלומר $e(t)\\,dt$ שווה לביטוי המקורי)?", -1/(tt**2 + 2*tt + 5),
            [1/(tt**2 + 2*tt + 5), -1/(tt**2 + 2*tt + 4), -tt/(tt**2 + 2*tt + 5)],
            lambda e: same(e.subs(tt, sp.cos(x))*(-sp.sin(x)), g5, pts=PX5),
            "$\\sin x\\,dx=-dt$ ו-$5+2\\cos x+\\cos^2x=t^2+2t+5$ (נבדק ב-sympy)."),
        chx("מהי הצורה של $t^2+2t+5$ אחרי השלמה לריבוע?", (tt + 1)**2 + 4,
            [(tt + 1)**2 + 5, (tt + 1)**2 + 3, (tt - 1)**2 + 4],
            lambda e: sp.expand(e - (tt**2 + 2*tt + 5)) == 0,
            "$(t+1)^2=t^2+2t+1$, ולכן צריך להוסיף $4$ (נבדק ב-sympy)."),
        chx("מהי התוצאה (בלי הקבוע)?", F5,
            [sp.atan((sp.cos(x) + 1)/2)/2, -sp.atan(sp.cos(x) + 1)/2, -sp.atan((sp.cos(x) + 1)/2)],
            lambda e: same(sp.diff(e, x), g5),
            "$\\int\\frac{dt}{(t+1)^2+4}=\\frac{1}{2}\\arctan\\frac{t+1}{2}$, ועם המינוס מקבלים את התשובה (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: washer volume =====
V6 = sp.pi*sp.integrate(25 - x**2 - 9, (x, -4, 4))
assert sorted(sp.solve(sp.Eq(25 - x**2, 9), x)) == [-4, 4]
assert sp.simplify(V6 - 256*sp.pi/3) == 0 and sp.integrate(16 - x**2, (x, -4, 4)) == R(256, 3)

add(6, "א",
    rubric=rub(("נקודות החיתוך של חצי המעגל עם הישר: $x=\\pm4$", 3),
               ("בחירת שיטת הטבעות: $\\pi\\int\\left(R^2-r^2\\right)dx$ עם $R=\\sqrt{25-x^2}$, $r=3$", 4),
               ("פישוט האינטגרנד ל-$16-x^2$", 2),
               ("חישוב האינטגרל $\\frac{256}{3}$", 2),
               ("תשובה סופית $V=\\frac{256\\pi}{3}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחשב $\\pi\\int\\left(\\sqrt{25-x^2}-3\\right)^2dx$: זה לא נפח של טבעת, כי הפרש הרדיוסים אינו הפרש הריבועים.",
              "לחשב נפח מ-$-5$ עד $5$ במקום בין נקודות החיתוך $\\pm4$.",
              "לשכוח את הגורם $\\pi$ בתשובה."],
    steps=[
        num("מהו ערך $x$ החיובי שבו $\\sqrt{25-x^2}=3$?", 4, "$25-x^2=9$ נותן $x^2=16$, ולכן $x=\\pm4$."),
        chx("מהו האינטגרנד של שיטת הטבעות, $R^2-r^2$ (עם $R=\\sqrt{25-x^2}$ ו-$r=3$)?", 16 - x**2,
            [(sp.sqrt(25 - x**2) - 3)**2, 25 - x**2 - 3, 25 - x**2 + 9],
            lambda e: same(e, 25 - x**2 - 9, pts=(0.3, 0.9, 1.7, 2.5, 3.2)),
            "$R^2-r^2=25-x^2-9=16-x^2$ (נבדק ב-sympy)."),
        num("מהו $\\int_{-4}^{4}\\left(16-x^2\\right)dx$? (עשרוני)", R(256, 3),
            "$2\\left(16x-\\frac{x^3}{3}\\right)\\Big|_0^4=2\\left(64-\\frac{64}{3}\\right)=\\frac{256}{3}\\approx85.333$.", tol=0.01),
        num("מהו הנפח $V$? (עשרוני)", V6,
            "$V=\\frac{256\\pi}{3}\\approx268.08$.", tol=0.05, nd=3),
    ],
    stepsSource="ai-verified")

# ===== Q6b: differentiability at 0, f = sin(ax) (x<=0), x^2 ln x (x>0) =====
assert sp.limit(sp.sin(a*x), x, 0, '-') == 0 and sp.limit(x**2*sp.log(x), x, 0, '+') == 0
assert sp.limit(sp.sin(a*x)/x, x, 0, '-') == a and sp.limit(x**2*sp.log(x)/x, x, 0, '+') == 0
assert sp.solve(sp.Eq(a, 0), a) == [0]

add(6, "ב",
    rubric=rub(("בדיקת רציפות ב-$x=0$: שלושה ערכים שווים $0$ לכל $a$", 3),
               ("נגזרת שמאלית $f'_-(0)=\\lim\\frac{\\sin(ax)}{x}=a$", 3),
               ("נגזרת ימנית $f'_+(0)=\\lim x\\ln x=0$", 3),
               ("השוואה: גזירות אם ורק אם $a=0$", 3)),
    rubricSource="ai-verified",
    pitfalls=["להסיק מרציפות שהפונקציה גזירה: כאן $f$ רציפה לכל $a$ אבל גזירה רק עבור $a=0$.",
              "להשאיר את $\\lim x\\ln x$ כ-$0\\cdot\\infty$ בלי לבדוק שהוא $0$.",
              "לגזור את שני הענפים ולהציב $x=0$ בנגזרת הימנית $2x\\ln x+x$ במקום לחשב לפי הגדרה."],
    steps=[
        ch("עבור אילו ערכי $a$ הפונקציה רציפה ב-$x=0$?", "לכל $a$ ממשי",
           ["רק עבור $a=0$", "רק עבור $a>0$", "לאף ערך של $a$"],
           "$f(0)=\\sin0=0$, $\\lim_{x\\to0^-}\\sin(ax)=0$ ו-$\\lim_{x\\to0^+}x^2\\ln x=0$, לכל $a$ (אומת ב-sympy)."),
        num("מהי הנגזרת השמאלית $f'_-(0)=\\lim_{x\\to0^-}\\frac{\\sin(ax)}{x}$ עבור $a=3$?", 3,
            "$\\frac{\\sin3x}{x}=3\\cdot\\frac{\\sin3x}{3x}\\to3$; בכלל $f'_-(0)=a$."),
        num("מהי הנגזרת הימנית $f'_+(0)=\\lim_{x\\to0^+}\\frac{x^2\\ln x}{x}=\\lim x\\ln x$?", 0,
            "$x\\ln x=\\frac{\\ln x}{1/x}\\to0$ (לופיטל)."),
        num("מהו הערך של $a$ שעבורו $f$ גזירה ב-$0$?", 0, "גזירות דורשת $f'_-(0)=f'_+(0)$, כלומר $a=0$."),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "25B-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ה, מועד ב'",
    "year": 2025,
    "examDate": "11/08/2025",
    "sourceFile": "calculus-1/25B-B exam (scan).pdf",
    "solutionFile": "",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

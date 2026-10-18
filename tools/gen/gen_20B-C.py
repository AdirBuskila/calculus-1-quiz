# -*- coding: utf-8 -*-
"""Generator for tools/raw/20B-C.json -- calculus-1 (20151), semester C (summer) 2020, moed B (27/10/2020).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_20B-C.py

Source: sitting 20B-C, pp.1-2 (typed exam only, NO solution or key anywhere). The header lists the course as a joint
exam for electrical/electronics engineering AND computer science, so it is in scope. Six questions, 20% each,
Q1 mandatory, choose 4 of Q2-Q6 (a/b parts 10% each).

Transcription fix (2026-10-18, arbiter): the Q3a cases environment had a backslash-space where the double-backslash row break is meant
(the three cases rendered on one row); the printed exam (p.1) shows three rows.

Solutions: written by the solver (2026-10-18), solutionSource "solved", official False, confidence high. No partial
evidence exists (no key, no tutor marks). Every answer is checked in tools/verify/20B-C/check.py (sympy, 0 mismatches).
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20B-C.json"
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
**תחום הגדרה:** $x\neq-1$. נקודת חיתוך עם הצירים: $(0,0)$.
**עליה וירידה, נקודות קיצון:**
$$f'(x)=\frac{3x^2\cdot2(x+1)^2-x^3\cdot4(x+1)}{4(x+1)^4}=\frac{3x^2(x+1)-2x^3}{2(x+1)^3}=\frac{x^2(x+3)}{2(x+1)^3}$$
$f'(x)=0$ עבור $x=-3$ ו-$x=0$. טבלת סימן של $f'$: חיובית כאשר $x<-3$, שלילית כאשר $-3<x<-1$, חיובית כאשר $-1<x<0$ וגם $x>0$ (ב-$x=0$ הנגזרת מתאפסת בלי להחליף סימן).
$f$ עולה ב-$(-\infty,-3)$ וב-$(-1,\infty)$, ויורדת ב-$(-3,-1)$.
נקודת מקסימום מקומי: $\left(-3,-\frac{27}{8}\right)$. ב-$x=0$ אין קיצון.
**קמירות ונקודות פיתול:** נכתוב $x^3=(x+1)^3-3(x+1)^2+3(x+1)-1$, ולכן
$$f(x)=\frac{1}{2}\left((x+1)-3+\frac{3}{x+1}-\frac{1}{(x+1)^2}\right)\ \Rightarrow\ f''(x)=\frac{1}{2}\left(\frac{6}{(x+1)^3}-\frac{6}{(x+1)^4}\right)=\frac{3x}{(x+1)^4}$$
טבלת סימן של $f''$: שלילית כאשר $x<-1$ וגם $-1<x<0$ (הגרף קעור, $\cap$), חיובית כאשר $x>0$ (הגרף קמור, $\cup$).
נקודת פיתול: $(0,0)$ (שם גם $f'(0)=0$: משיק אופקי בנקודת הפיתול).
**אסימפטוטות:**
1. אנכית $x=-1$: המונה שואף ל-$-1$ והמכנה ל-$0^+$, ולכן $\lim_{x\to-1^\pm}f(x)=-\infty$.
2. משופעת: מהפירוק שלמעלה, $f(x)=\frac{x}{2}-1+\frac{3x+2}{2(x+1)^2}$, והשבר האחרון שואף ל-$0$ כאשר $x\to\pm\infty$. כלומר
$$a=\lim_{x\to\pm\infty}\frac{f(x)}{x}=\frac{1}{2},\qquad b=\lim_{x\to\pm\infty}\left(f(x)-\frac{x}{2}\right)=-1$$
והישר $y=\frac{x}{2}-1$ הוא אסימפטוטה משופעת ב-$\pm\infty$.
**שרטוט:**
![גרף הפונקציה f(x)=x^3/(2(x+1)^2): מקסימום ב-(-3,-27/8), פיתול ב-(0,0), אסימפטוטות x=-1 ו-y=x/2-1](images/exams/20B-C-Q1-graph.png)
"""

SOL[(2, "א")] = r"""
נבחין בשלושה מקרים:
**$0<b<3$:** נחלק ב-$3^n$: $\frac{3^n}{3^n+b^n}=\frac{1}{1+\left(\frac{b}{3}\right)^n}\to\frac{1}{1+0}=1$, כי $0<\frac{b}{3}<1$.
**$b=3$:** $\frac{3^n}{3^n+3^n}=\frac{1}{2}$ לכל $n$, והגבול $\frac{1}{2}$.
**$b>3$:** נחלק ב-$b^n$: $\frac{3^n}{3^n+b^n}=\frac{\left(\frac{3}{b}\right)^n}{\left(\frac{3}{b}\right)^n+1}\to\frac{0}{0+1}=0$, כי $0<\frac{3}{b}<1$.
$$\lim_{n\to\infty}\frac{3^n}{3^n+b^n}=\begin{cases}1, & 0<b<3\\ \frac{1}{2}, & b=3\\ 0, & b>3\end{cases}$$
"""

SOL[(2, "ב")] = r"""
חילוק פולינומים: $x^3+2x+5=x\left(x^2-1\right)+3x+5$, ולכן $\frac{x^3+2x+5}{x^2-1}=x+\frac{3x+5}{(x-1)(x+1)}$.
פירוק לשברים חלקיים: $\frac{3x+5}{(x-1)(x+1)}=\frac{A}{x-1}+\frac{B}{x+1}$, כלומר $3x+5=A(x+1)+B(x-1)$.
$x=1$: $8=2A\Rightarrow A=4$. $x=-1$: $2=-2B\Rightarrow B=-1$.
$$\int\frac{x^3+2x+5}{x^2-1}\,dx=\int\left(x+\frac{4}{x-1}-\frac{1}{x+1}\right)dx=\frac{x^2}{2}+4\ln|x-1|-\ln|x+1|+C$$
"""

SOL[(3, "א")] = r"""
נחשב את הגבולות החד-צדדיים ב-$x=0$ ונשווה ל-$f(0)=\frac{1}{2}$.
$$\lim_{x\to0^-}\frac{e^x-1}{\sin2x}=\lim_{x\to0^-}\frac{e^x-1}{x}\cdot\frac{2x}{\sin2x}\cdot\frac{1}{2}=1\cdot1\cdot\frac{1}{2}=\frac{1}{2}$$
$$\lim_{x\to0^+}\left(x\ln x+\frac{\arcsin x}{2x}\right)=0+\frac{1}{2}\cdot1=\frac{1}{2}$$
כאן $\lim_{x\to0^+}x\ln x=\lim_{x\to0^+}\frac{\ln x}{\frac{1}{x}}=\lim_{x\to0^+}\frac{\frac{1}{x}}{-\frac{1}{x^2}}=\lim_{x\to0^+}(-x)=0$ (לופיטל), ו-$\lim_{x\to0}\frac{\arcsin x}{x}=\lim_{x\to0}\frac{\frac{1}{\sqrt{1-x^2}}}{1}=1$.
שני הגבולות החד-צדדיים שווים ל-$\frac{1}{2}=f(0)$, ולכן **הפונקציה רציפה ב-$x=0$**.
"""

SOL[(3, "ב")] = r"""
$f$ רציפה בקטע הסגור $[0,4]$ (שם $18-x^2>0$), ולכן מקבלת בו מקסימום ומינימום.
$$f'(x)=\sqrt{18-x^2}+x\cdot\frac{-2x}{2\sqrt{18-x^2}}=\frac{18-2x^2}{\sqrt{18-x^2}}$$
$f'(x)=0\iff x^2=9$, ובקטע: $x=3$.
ערכי הפונקציה בנקודה החשודה ובקצוות:
$$f(0)=0,\qquad f(3)=3\sqrt{9}=9,\qquad f(4)=4\sqrt{2}\approx5.66$$
הערך המקסימלי הוא $9$ (ב-$x=3$) והערך המינימלי הוא $0$ (ב-$x=0$).
"""

SOL[(4, "א")] = r"""
אינטגרציה בחלקים עם $u=\ln^2x$, $dv=dx$: $du=\frac{2\ln x}{x}dx$, $v=x$.
$$\int\ln^2x\,dx=x\ln^2x-2\int\ln x\,dx$$
ושוב בחלקים ($u=\ln x$, $dv=dx$): $\int\ln x\,dx=x\ln x-\int x\cdot\frac{1}{x}dx=x\ln x-x$. לכן
$$\int\ln^2x\,dx=x\ln^2x-2x\ln x+2x+C$$
"""

SOL[(4, "ב")] = r"""
צורה $\frac{0}{0}$. נכפיל בצמוד:
$$\frac{\sqrt{3x-2}-\sqrt{x+2}}{x^2-4}=\frac{(3x-2)-(x+2)}{(x-2)(x+2)\left(\sqrt{3x-2}+\sqrt{x+2}\right)}=\frac{2(x-2)}{(x-2)(x+2)\left(\sqrt{3x-2}+\sqrt{x+2}\right)}$$
$$\lim_{x\to2}\frac{\sqrt{3x-2}-\sqrt{x+2}}{x^2-4}=\lim_{x\to2}\frac{2}{(x+2)\left(\sqrt{3x-2}+\sqrt{x+2}\right)}=\frac{2}{4\cdot(2+2)}=\frac{1}{8}$$
"""

SOL[(5, "א")] = r"""
עבור $x\in[-1,1]$ מתקיים $0\le x^4\le1$, ולכן $1\le2x^4+1\le3$ ו-
$$\frac{1}{3}\le\frac{1}{2x^4+1}\le1$$
לפי תכונת המונוטוניות של האינטגרל המסוים (אורך הקטע $2$):
$$\frac{1}{3}\cdot2\le\int_{-1}^{1}\frac{dx}{2x^4+1}\le1\cdot2\quad\Longrightarrow\quad\frac{2}{3}\le\int_{-1}^{1}\frac{dx}{2x^4+1}\le2$$
"""

SOL[(5, "ב")] = r"""
המונה $\int_0^x\frac{t^2}{1+t^4}dt$ והמכנה $x^3$ שואפים ל-$0$, והמונה גזיר לפי המשפט היסודי. לפי כלל לופיטל:
$$\lim_{x\to0}\frac{\int_0^x\frac{t^2}{1+t^4}\,dt}{x^3}=\lim_{x\to0}\frac{\frac{x^2}{1+x^4}}{3x^2}=\lim_{x\to0}\frac{1}{3\left(1+x^4\right)}=\frac{1}{3}$$
"""

SOL[(6, "א")] = r"""
קירוב לינארי: $\tan(x_0+\Delta x)\approx\tan x_0+dy$, כאשר $dy=\frac{1}{\cos^2x_0}\,\Delta x$.
$x_0=\frac{\pi}{4}=45^\circ$, $\Delta x=3^\circ=\frac{3\pi}{180}=\frac{\pi}{60}$ (ברדיאנים!), $\tan\frac{\pi}{4}=1$, $\frac{1}{\cos^2\frac{\pi}{4}}=2$.
$$\tan48^\circ\approx1+2\cdot\frac{\pi}{60}=1+\frac{\pi}{30}\approx1.1047$$
(לשם השוואה, $\tan48^\circ=1.1106\ldots$)
"""

SOL[(6, "ב")] = r"""
נקודות החיתוך ברביע הראשון: $2x=\frac{1}{x}\Rightarrow x=\frac{1}{\sqrt{2}}$ (הנקודה $\left(\frac{1}{\sqrt{2}},\sqrt{2}\right)$), ו-$\frac{x}{2}=\frac{1}{x}\Rightarrow x=\sqrt{2}$ (הנקודה $\left(\sqrt{2},\frac{1}{\sqrt{2}}\right)$). שני הישרים נחתכים בראשית.
התחום חסום מלמטה על ידי $y=\frac{x}{2}$, ומלמעלה על ידי $y=2x$ (עבור $0\le x\le\frac{1}{\sqrt{2}}$) ועל ידי $y=\frac{1}{x}$ (עבור $\frac{1}{\sqrt{2}}\le x\le\sqrt{2}$):
$$S=\int_0^{1/\sqrt{2}}\left(2x-\frac{x}{2}\right)dx+\int_{1/\sqrt{2}}^{\sqrt{2}}\left(\frac{1}{x}-\frac{x}{2}\right)dx=\frac{3x^2}{4}\Big|_0^{1/\sqrt{2}}+\left(\ln x-\frac{x^2}{4}\right)\Big|_{1/\sqrt{2}}^{\sqrt{2}}=$$
$$=\frac{3}{8}+\left(\ln\sqrt{2}-\ln\frac{1}{\sqrt{2}}\right)-\left(\frac{2}{4}-\frac{1}{8}\right)=\frac{3}{8}+\ln2-\frac{3}{8}=\ln2$$
הערה: ברביע השלישי יש תחום סימטרי (סימטריה ביחס לראשית) עם אותו שטח $\ln2$; התשובה המקובלת לשאלה היא שטח התחום האחד, $\ln2$.
"""


questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=\frac{x^3}{2(x+1)^2}$ לפי הסעיפים הבאים: תחום הגדרה, תחומי עליה/ירידה, נקודות קיצון, "
      "קמירות ונקודות פיתול, אסימפטוטות. שרטטו את גרף הפונקציה.", points=20),

    Q(2, "computation", "sequences_limits",
      r"חשבו את גבול הסדרה $\lim_{n\to\infty}\frac{3^n}{3^n+b^n}$, כאשר $b>0$ הוא פרמטר ממשי.",
      part="א", points=10),
    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{x^3+2x+5}{x^2-1}\,dx$.", part="ב", points=10),

    Q(3, "computation", "continuity",
      "האם הפונקציה\n"
      r"$$f(x)=\begin{cases}\frac{e^x-1}{\sin 2x}, & x<0\\ \frac{1}{2}, & x=0\\ x\cdot\ln x+\frac{\arcsin x}{2x}, & x>0\end{cases}$$"
      "\n" r"רציפה ב-$x=0$?", part="א", points=10),
    Q(3, "computation", "extrema_optimization",
      r"מצאו את הערך המקסימלי ואת הערך המינימלי של הפונקציה $f(x)=x\sqrt{18-x^2}$ בקטע $[0,4]$.",
      part="ב", points=10),

    Q(4, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\ln^2 x\,dx$.", part="א", points=10),
    Q(4, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to2}\frac{\sqrt{3x-2}-\sqrt{x+2}}{x^2-4}$.", part="ב", points=10),

    Q(5, "proof", "definite_integrals",
      r"הוכיחו את אי-השוויון הבא: $\frac{2}{3}\le\int_{-1}^{1}\frac{1}{2x^4+1}\,dx\le2$.", part="א", points=10),
    Q(5, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to0}\frac{1}{x^3}\int_0^x\frac{t^2}{1+t^4}\,dt$.", part="ב", points=10),

    Q(6, "computation", "derivatives_tangents",
      r"בעזרת דיפרנציאל של הפונקציה $y=\tan x$ בנקודה $x=\frac{\pi}{4}$ חשבו בקירוב את $\tan 48^\circ$.",
      part="א", points=10),
    Q(6, "computation", "definite_integrals",
      r"חשבו את השטח הכלוא בין הקווים $y=2x,\quad y=\frac{x}{2},\quad y=\frac{1}{x}$.", part="ב", points=10),
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



# ===== Q1: f = x^3/(2(x+1)^2) =====
f1 = x**3/(2*(x + 1)**2)
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, x**2*(x + 3)/(2*(x + 1)**3)) and same(f1pp, 3*x/(x + 1)**4)
assert f1.subs(x, -3) == R(-27, 8)
assert f1p.subs(x, R(-1, 2)) > 0 and f1p.subs(x, R(1, 2)) > 0 and f1p.subs(x, 0) == 0
assert f1pp.subs(x, R(-1, 2)) < 0 and f1pp.subs(x, R(1, 2)) > 0
assert f1p.subs(x, -4) > 0 and f1p.subs(x, -2) < 0
assert (sp.limit(f1/x, x, sp.oo), sp.limit(f1 - x/2, x, sp.oo)) == (R(1, 2), -1)
for (m_, k_) in [(R(1, 2), 0), (R(1, 2), 1), (1, -1)]:
    assert (m_, k_) != (R(1, 2), -1)

add(1,
    rubric=rub((r"תחום הגדרה $x\neq-1$ ונקודת חיתוך עם הצירים $(0,0)$", 2),
               (r"נגזרת $f'(x)=\frac{x^2(x+3)}{2(x+1)^3}$, נקודות קריטיות $x=-3,0$ וטבלת סימנים", 5),
               (r"סיווג הקיצון: מקסימום מקומי ב-$x=-3$ עם $f(-3)=-\frac{27}{8}$, ללא קיצון ב-$x=0$", 3),
               (r"$f''(x)=\frac{3x}{(x+1)^4}$, קמירות וקעירות ונקודת פיתול $(0,0)$", 4),
               (r"אסימפטוטה אנכית $x=-1$ ואסימפטוטה משופעת $y=\frac{x}{2}-1$", 4),
               ("שרטוט הגרף בהתאם לכל הנתונים", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"להכריז על קיצון ב-$x=0$ רק כי $f'(0)=0$. הנגזרת חיובית משני הצדדים ולכן אין קיצון, ויש שם נקודת פיתול.",
              r"לשכוח שהאסימפטוטה האנכית $x=-1$ שואפת ל-$-\infty$ משני הצדדים (המכנה ריבועי).",
              r"לחשב את האסימפטוטה המשופעת בלי חילוק פולינומים או בלי הגבול $\lim(f(x)-\frac{x}{2})$ ולקבל חותך שגוי."],
    steps=[
        chx(r"מהי הנגזרת של $f(x)=\frac{x^3}{2(x+1)^2}$?", x**2*(x + 3)/(2*(x + 1)**3),
            [x**2*(x + 3)/(2*(x + 1)**2), x**2*(x - 3)/(2*(x + 1)**3), x**2*(x + 3)/((x + 1)**3)],
            lambda e: same(e, f1p), r"כלל המנה נותן $f'(x)=\frac{3x^2(x+1)-2x^3}{2(x+1)^3}=\frac{x^2(x+3)}{2(x+1)^3}$ (אומת ב-sympy)."),
        num(r"מהו הערך $f(-3)$ בנקודת המקסימום המקומי?", f1.subs(x, -3),
            r"$f(-3)=\frac{-27}{2\cdot4}=-\frac{27}{8}=-3.375$."),
        ch(r"מה קורה בנקודה $x=0$, שבה $f'(0)=0$?",
           r"אין קיצון (הנגזרת חיובית משני הצדדים), ו-$f''$ מחליפה סימן ולכן זו נקודת פיתול עם משיק אופקי",
           ["מינימום מקומי", "מקסימום מקומי", r"נקודת אי-רציפות כי $x=0$ מחוץ לתחום ההגדרה"],
           r"$f'>0$ משני צדי $0$ ולכן אין קיצון. $f''<0$ משמאל ו-$f''>0$ מימין, כלומר פיתול (נבדק ב-sympy)."),
        chx(r"מהי הנגזרת השנייה של $f$?", 3*x/(x + 1)**4, [3*x/(x + 1)**3, 3/(x + 1)**4, 6*x/(x + 1)**4],
            lambda e: same(e, f1pp), r"הנגזרת השנייה היא $f''(x)=\frac{3x}{(x+1)^4}$; היא מתאפסת רק ב-$x=0$ (אומת ב-sympy)."),
        ch(r"מהי האסימפטוטה המשופעת של $f$ ב-$\pm\infty$?", r"$y=\frac{x}{2}-1$",
           [r"$y=\frac{x}{2}$", r"$y=\frac{x}{2}+1$", r"$y=x-1$"],
           r"$a=\lim\frac{f(x)}{x}=\frac{1}{2}$ ו-$b=\lim\left(f(x)-\frac{x}{2}\right)=-1$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: lim 3^n/(3^n+b^n) =====


def frac_lim(bv, n_=400):
    return float(R(3)**n_/(R(3)**n_ + R(bv)**n_))


assert abs(frac_lim(2) - 1) < 1e-9 and abs(frac_lim(3) - 0.5) < 1e-12 and frac_lim(5) < 1e-9

add(2, "א",
    rubric=rub((r"חלוקה בחזקה הדומיננטית והצגת הגבול כ-$\frac{1}{1+\left(\frac{b}{3}\right)^n}$", 3),
               (r"המקרה $0<b<3$: הגבול $1$", 2),
               (r"המקרה $b=3$: הגבול $\frac{1}{2}$", 2),
               (r"המקרה $b>3$: הגבול $0$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לבדוק רק ערך אחד של $b$ ולא לפצל לשלושה מקרים לפי היחס בין $b$ ל-$3$.",
              r"לשכוח את המקרה $b=3$, שבו המנה קבועה $\frac{1}{2}$ ולא שואפת ל-$0$ או ל-$1$."],
    steps=[
        num(r"מהו הגבול כאשר $b=2$?", frac_lim(2), r"$\frac{1}{1+(2/3)^n}\to\frac{1}{1+0}=1$."),
        num(r"מהו הגבול כאשר $b=3$?", frac_lim(3), r"$\frac{3^n}{3^n+3^n}=\frac{1}{2}$ לכל $n$."),
        ch(r"מהו הגבול כאשר $b>3$?", "$0$", ["$1$", r"$\frac{1}{2}$", r"$\infty$"],
           r"$\frac{3^n}{3^n+b^n}=\frac{(3/b)^n}{(3/b)^n+1}\to\frac{0}{0+1}=0$ כי $0<\frac{3}{b}<1$."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: integral (x^3+2x+5)/(x^2-1) =====
g2 = (x**3 + 2*x + 5)/(x**2 - 1)
quo, rem = sp.div(x**3 + 2*x + 5, x**2 - 1, x)
assert (quo, rem) == (x, 3*x + 5)
A_, B_ = sp.symbols('A B')
s2 = sp.solve(sp.Poly(sp.expand(A_*(x + 1) + B_*(x - 1) - (3*x + 5)), x).all_coeffs(), [A_, B_], dict=True)[0]
assert s2 == {A_: 4, B_: -1}
F2 = x**2/2 + 4*sp.log(x - 1) - sp.log(x + 1)
assert same(sp.diff(F2, x), g2)
F2w = [x**2/2 + 4*sp.log(x - 1) + sp.log(x + 1), x**2/2 - 4*sp.log(x - 1) - sp.log(x + 1), x**3/3 + 2*x**2/2 + 5*x]

add(2, "ב",
    rubric=rub(("חילוק פולינומים: מנה $x$ ושארית $3x+5$", 3),
               (r"פירוק $\frac{3x+5}{(x-1)(x+1)}=\frac{A}{x-1}+\frac{B}{x+1}$", 2),
               (r"חישוב המקדמים $A=4$, $B=-1$", 2),
               (r"אינטגרציה וכתיבת התשובה $\frac{x^2}{2}+4\ln|x-1|-\ln|x+1|+C$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לפרק לשברים חלקיים בלי לחלק קודם: דרגת המונה גבוהה מדרגת המכנה.",
              r"לשכוח ערך מוחלט בלוגריתמים או להחליף סימן ב-$B$."],
    steps=[
        chx(r"מהי המנה בחילוק $x^3+2x+5$ ב-$x^2-1$?", x, [x + 2, x**2, 3*x + 5], lambda e: e == quo,
            r"$x^3+2x+5=x(x^2-1)+(3x+5)$, כלומר מנה $x$ ושארית $3x+5$ (אומת ב-sympy)."),
        num(r"מהו המקדם $A$ בפירוק $\frac{3x+5}{(x-1)(x+1)}=\frac{A}{x-1}+\frac{B}{x+1}$?", s2[A_],
            r"הצבת $x=1$ ב-$3x+5=A(x+1)+B(x-1)$ נותנת $8=2A$, כלומר $A=4$."),
        num(r"מהו המקדם $B$?", s2[B_], r"הצבת $x=-1$ נותנת $2=-2B$, כלומר $B=-1$."),
        chx(r"מהי הפונקציה הקדומה (בתחום $x>1$, בלי הקבוע)?", F2, F2w, lambda e: same(sp.diff(e, x), g2),
            r"$\int\left(x+\frac{4}{x-1}-\frac{1}{x+1}\right)dx=\frac{x^2}{2}+4\ln(x-1)-\ln(x+1)$; הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: continuity at 0 =====
L3 = sp.limit((sp.exp(x) - 1)/sp.sin(2*x), x, 0, '-')
R3 = sp.limit(x*sp.log(x) + sp.asin(x)/(2*x), x, 0, '+')
xl = sp.limit(x*sp.log(x), x, 0, '+')
al = sp.limit(sp.asin(x)/(2*x), x, 0, '+')
assert (L3, R3, xl, al) == (R(1, 2), R(1, 2), 0, R(1, 2))

add(3, "א",
    rubric=rub((r"הגבול השמאלי $\lim_{x\to0^-}\frac{e^x-1}{\sin2x}=\frac{1}{2}$", 3),
               (r"$\lim_{x\to0^+}x\ln x=0$ (לופיטל) ו-$\lim\frac{\arcsin x}{2x}=\frac{1}{2}$", 4),
               (r"השוואה ל-$f(0)=\frac{1}{2}$ ומסקנה שהפונקציה רציפה", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לחשב את הגבול הימני כ-$0\cdot\infty=0$ בלי הצדקה, ולשכוח את האיבר $\frac{\arcsin x}{2x}$.",
              r"לבדוק רק גבול אחד ולא את שני הצדדים ואת ערך הפונקציה."],
    steps=[
        num(r"מהו $\lim_{x\to0^-}\frac{e^x-1}{\sin2x}$?", L3, r"$\frac{e^x-1}{x}\to1$ ו-$\frac{2x}{\sin2x}\to1$, לכן הגבול $\frac{1}{2}$."),
        num(r"מהו $\lim_{x\to0^+}x\ln x$?", xl, r"$x\ln x=\frac{\ln x}{1/x}\to\frac{1/x}{-1/x^2}=-x\to0$."),
        num(r"מהו $\lim_{x\to0^+}\frac{\arcsin x}{2x}$?", al, r"$\frac{\arcsin x}{x}\to1$, לכן הגבול $\frac{1}{2}$."),
        ch("האם $f$ רציפה ב-$x=0$?", r"כן, כי שני הגבולות החד-צדדיים שווים ל-$f(0)=\frac{1}{2}$",
           [r"לא, כי הגבול הימני $0$ שונה מ-$f(0)$", r"לא, כי הגבול השמאלי אינו קיים", r"לא, כי $f(0)\neq1$"],
           r"שני הגבולות החד-צדדיים הם $\frac{1}{2}=f(0)$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: extrema of x sqrt(18-x^2) on [0,4] =====
f3 = x*sp.sqrt(18 - x**2)
f3p = sp.diff(f3, x)
assert same(f3p, (18 - 2*x**2)/sp.sqrt(18 - x**2))
assert [s for s in sp.solve(f3p, x) if 0 <= s <= 4] == [3]
assert (f3.subs(x, 0), f3.subs(x, 3), f3.subs(x, 4)) == (0, 9, 4*sp.sqrt(2))

add(3, "ב",
    rubric=rub(("נימוק שהפונקציה רציפה בקטע סגור ולכן מקבלת מקסימום ומינימום", 2),
               (r"נגזרת $f'(x)=\frac{18-2x^2}{\sqrt{18-x^2}}$ והנקודה החשודה $x=3$", 4),
               ("חישוב ערכי הפונקציה בנקודה החשודה ובקצוות", 2),
               (r"מסקנה: מקסימום $9$ ב-$x=3$ ומינימום $0$ ב-$x=0$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לשכוח לבדוק את קצות הקטע $x=0$ ו-$x=4$.",
              r"לכלול את הנקודה $x=-3$, שאינה בקטע $[0,4]$."],
    steps=[
        chx(r"מהי הנגזרת של $f(x)=x\sqrt{18-x^2}$?", (18 - 2*x**2)/sp.sqrt(18 - x**2),
            [(18 - x**2)/sp.sqrt(18 - x**2), (18 - 2*x)/sp.sqrt(18 - x**2), (18 + 2*x**2)/sp.sqrt(18 - x**2)],
            lambda e: same(e, f3p), r"כלל המכפלה: $f'=\sqrt{18-x^2}-\frac{x^2}{\sqrt{18-x^2}}=\frac{18-2x^2}{\sqrt{18-x^2}}$ (אומת ב-sympy)."),
        num(r"מהי הנקודה הקריטית בקטע $[0,4]$?", 3, r"$18-2x^2=0$ נותן $x=\pm3$, ובקטע רק $x=3$."),
        num(r"מהו $f(3)$?", f3.subs(x, 3), r"$f(3)=3\sqrt{9}=9$."),
        num(r"מהו $f(4)$? (עשרוני)", f3.subs(x, 4), r"$f(4)=4\sqrt{2}\approx5.657$."),
        ch("מהם הערך המקסימלי והמינימלי בקטע?", r"מקסימום $9$ ב-$x=3$, מינימום $0$ ב-$x=0$",
           [r"מקסימום $9$ ב-$x=3$, מינימום $4\sqrt{2}$ ב-$x=4$", r"מקסימום $4\sqrt{2}$ ב-$x=4$, מינימום $0$ ב-$x=0$",
            r"מקסימום $9$ ב-$x=3$, מינימום $-9$ ב-$x=-3$"],
           r"משווים $f(0)=0$, $f(3)=9$, $f(4)\approx5.66$; הגדול הוא $9$ והקטן הוא $0$."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: int ln^2 x =====
F4 = x*sp.log(x)**2 - 2*x*sp.log(x) + 2*x
assert same(sp.diff(F4, x), sp.log(x)**2)
F4w = [x*sp.log(x)**2 - 2*x*sp.log(x) - 2*x, x*sp.log(x)**2 + 2*x*sp.log(x) + 2*x, sp.log(x)**3/3]
i1 = sp.integrate(sp.log(x), (x, 1, sp.E))
i2 = sp.integrate(sp.log(x)**2, (x, 1, sp.E))
assert i1 == 1 and sp.simplify(i2 - (sp.E - 2)) == 0
assert same(sp.diff(x*sp.log(x) - x, x), sp.log(x))

add(4, "א",
    rubric=rub((r"אינטגרציה בחלקים ראשונה: $\int\ln^2x\,dx=x\ln^2x-2\int\ln x\,dx$", 4),
               (r"אינטגרציה בחלקים שנייה: $\int\ln x\,dx=x\ln x-x$", 4),
               (r"הרכבה לתשובה $x\ln^2x-2x\ln x+2x+C$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לשכוח את הגורם $2$ ב-$\int\ln^2x\,dx=x\ln^2x-2\int\ln x\,dx$ (נגזרת $\ln^2x$ היא $\frac{2\ln x}{x}$).",
              r"לטעות בסימן בשלב השני ולקבל $-2x$ במקום $+2x$."],
    steps=[
        num(r"מהו $\int_1^e\ln x\,dx$?", i1, r"הפונקציה הקדומה $x\ln x-x$ נותנת $(e-e)-(0-1)=1$."),
        num(r"מהו $\int_1^e\ln^2x\,dx$? (עשרוני)", i2, r"$\left[x\ln^2x-2x\ln x+2x\right]_1^e=(e-2e+2e)-2=e-2\approx0.7183$."),
        chx(r"מהי הפונקציה הקדומה של $\ln^2x$?", F4, F4w, lambda e: same(sp.diff(e, x), sp.log(x)**2),
            r"מציבים $\int\ln x\,dx=x\ln x-x$ בנוסחה הראשונה; הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: limit with square roots =====
g4 = (sp.sqrt(3*x - 2) - sp.sqrt(x + 2))/(x**2 - 4)
assert sp.limit(g4, x, 2) == R(1, 8)
red4 = 2/((x + 2)*(sp.sqrt(3*x - 2) + sp.sqrt(x + 2)))
assert same(g4, red4) and red4.subs(x, 2) == R(1, 8)
den4 = ((x + 2)*(sp.sqrt(3*x - 2) + sp.sqrt(x + 2))).subs(x, 2)
assert den4 == 16

add(4, "ב",
    rubric=rub((r"זיהוי צורה $\frac{0}{0}$ ובחירה בכפל בצמוד", 2),
               (r"המונה אחרי הכפל: $(3x-2)-(x+2)=2(x-2)$", 3),
               (r"צמצום הגורם $x-2$ והגעה לביטוי $\frac{2}{(x+2)(\sqrt{3x-2}+\sqrt{x+2})}$", 3),
               (r"הצבה וחישוב הגבול $\frac{1}{8}$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"להציב $x=2$ ישירות ולכתוב $\frac{0}{0}=0$ בלי לפתור את אי-הוודאות.",
              r"לכפול רק את המונה בצמוד ולא את המכנה, או לטעות ב-$(3x-2)-(x+2)$."],
    steps=[
        chx(r"מהו המונה אחרי הכפל בצמוד $\sqrt{3x-2}+\sqrt{x+2}$ (מעל אותו מכנה)?", 2*x - 4, [4*x, 2*x, 4*x - 4],
            lambda e: same(e, (3*x - 2) - (x + 2)), r"$(\sqrt{3x-2})^2-(\sqrt{x+2})^2=(3x-2)-(x+2)=2x-4=2(x-2)$."),
        num(r"אחרי צמצום $x-2$ המכנה הוא $(x+2)\left(\sqrt{3x-2}+\sqrt{x+2}\right)$. מה ערכו ב-$x=2$?", den4,
            r"$(2+2)\left(\sqrt4+\sqrt4\right)=4\cdot4=16$."),
        num(r"מהו הגבול?", sp.limit(g4, x, 2), r"$\frac{2}{16}=\frac{1}{8}=0.125$."),
    ],
    stepsSource="ai-verified")

# ===== Q5a: bounds of an integral =====
v5 = sp.integrate(1/(2*x**4 + 1), (x, -1, 1))
assert R(2, 3) <= sp.N(v5) <= 2
assert sp.N(sp.integrate(1/(2*x**4 + 1), (x, -1, 1))) > 0
L5 = [r"לכל $x\in[-1,1]$ מתקיים $0\le x^4\le1$, ולכן $1\le2x^4+1\le3$.",
      r"מכאן $\frac{1}{3}\le\frac{1}{2x^4+1}\le1$ לכל $x\in[-1,1]$.",
      r"לפי מונוטוניות האינטגרל על קטע באורך $2$: $\frac{1}{3}\cdot2\le\int_{-1}^{1}\frac{dx}{2x^4+1}\le1\cdot2$, כלומר $\frac{2}{3}\le\int_{-1}^{1}\frac{dx}{2x^4+1}\le2$."]
L5b = list(L5)
L5b[1] = r"מכאן $1\le\frac{1}{2x^4+1}\le3$ לכל $x\in[-1,1]$."
assert R(1, 3) == 1/R(3) and not (1/R(3) == 1)

add(5, "א",
    rubric=rub((r"חסימת המכנה: $1\le2x^4+1\le3$ בקטע $[-1,1]$", 3),
               (r"חסימת האינטגרנד: $\frac{1}{3}\le\frac{1}{2x^4+1}\le1$", 3),
               (r"שימוש במונוטוניות האינטגרל ובאורך הקטע $2$", 2),
               (r"מסקנה: $\frac{2}{3}\le\int\le2$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"להפוך את כיוון אי-השוויונות בעת מעבר להופכי ולכתוב $1\le\frac{1}{2x^4+1}\le3$.",
              r"לשכוח להכפיל באורך הקטע $2$ בקבלת הגבולות של האינטגרל."],
    steps=[
        num(r"מהו הערך המינימלי של $\frac{1}{2x^4+1}$ בקטע $[-1,1]$? (עשרוני)", R(1, 3), r"המכנה מקסימלי ב-$x=\pm1$ ושווה $3$, לכן המינימום הוא $\frac{1}{3}\approx0.3333$."),
        num(r"מהו אורך הקטע $[-1,1]$, שבו מכפילים את הגבולות?", 2, r"האורך הוא $1-(-1)=2$."),
        order("סדרו את שלבי ההוכחה.", L5,
              "קודם חוסמים את המכנה, אחר כך את האינטגרנד, ואז מפעילים מונוטוניות של האינטגרל. כל שלב נשען על קודמו."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L5b, 1,
                r"כאשר $1\le2x^4+1\le3$ ההופכי מקיים $\frac{1}{3}\le\frac{1}{2x^4+1}\le1$ (ההפכים מחליפים סדר), לא $1\le\cdots\le3$."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: limit with integral =====
ser5 = sp.integrate(sp.series(t**2/(1 + t**4), t, 0, 10).removeO(), (t, 0, x))
assert sp.limit(ser5/x**3, x, 0) == R(1, 3)
d5 = sp.diff(sp.integrate(t**2/(1 + t**4), (t, 0, x)), x) if False else x**2/(1 + x**4)

add(5, "ב",
    rubric=rub((r"זיהוי צורה $\frac{0}{0}$ והפעלת לופיטל", 3),
               (r"גזירת המונה לפי המשפט היסודי: $\frac{x^2}{1+x^4}$", 3),
               (r"צמצום וחישוב הגבול $\frac{1}{3}$", 4)),
    rubricSource="ai-verified",
    pitfalls=[r"לנסות לחשב את האינטגרל $\int\frac{t^2}{1+t^4}dt$ במפורש במקום להשתמש במשפט היסודי ובלופיטל.",
              r"לשכוח את המכנה $3x^2$ כשגוזרים את $x^3$."],
    steps=[
        chx(r"מהי נגזרת המונה $\int_0^x\frac{t^2}{1+t^4}dt$ לפי $x$?", x**2/(1 + x**4), [x**3/(1 + x**4), t**2/(1 + t**4), 2*x/(1 + x**4)],
            lambda e: same(e, d5) , r"לפי המשפט היסודי של החשבון האינטגרלי, גוזרים את האינטגרנד ומציבים את הגבול העליון: $\frac{x^2}{1+x^4}$."),
        num(r"מהו הגבול?", R(1, 3), r"$\frac{x^2/(1+x^4)}{3x^2}=\frac{1}{3(1+x^4)}\to\frac{1}{3}\approx0.3333$ (נבדק ב-sympy דרך טור)."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: differential approximation of tan 48 =====
dx6 = sp.pi/60
dy6 = (1/sp.cos(x)**2).subs(x, sp.pi/4)
ap6 = 1 + dy6*dx6
assert dy6 == 2 and abs(float(ap6) - 1.1047) < 1e-4 and abs(float(sp.tan(48*sp.pi/180)) - 1.1106) < 1e-4

add(6, "א",
    rubric=rub((r"הנוסחה $\tan(x_0+\Delta x)\approx\tan x_0+\frac{1}{\cos^2x_0}\Delta x$", 3),
               (r"המרת $3^\circ$ לרדיאנים: $\Delta x=\frac{\pi}{60}$", 3),
               (r"חישוב $\tan\frac{\pi}{4}=1$ ו-$\frac{1}{\cos^2\frac{\pi}{4}}=2$", 2),
               (r"הקירוב $1+\frac{\pi}{30}\approx1.1047$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"להציב $\Delta x=3$ במעלות במקום ברדיאנים ($\frac{\pi}{60}$).",
              r"לשכוח שהנגזרת של $\tan x$ היא $\frac{1}{\cos^2x}$ ולהשתמש ב-$\cos x$."],
    steps=[
        num(r"מהו $\Delta x$ ברדיאנים ($3^\circ$)? (עשרוני)", dx6, r"$3\cdot\frac{\pi}{180}=\frac{\pi}{60}\approx0.05236$."),
        num(r"מהו הערך $\frac{1}{\cos^2\frac{\pi}{4}}$ (הנגזרת של $\tan x$ ב-$\frac{\pi}{4}$)?", dy6, r"$\cos^2\frac{\pi}{4}=\frac{1}{2}$ ולכן הנגזרת $2$."),
        num(r"מהו הקירוב של $\tan48^\circ$? (עשרוני)", ap6, r"$1+2\cdot\frac{\pi}{60}=1+\frac{\pi}{30}\approx1.1047$."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: area between y=2x, y=x/2, y=1/x =====
x1 = 1/sp.sqrt(2)
x2 = sp.sqrt(2)
assert sp.solve(sp.Eq(2*x, 1/x), x) == [-x1, x1] or set(sp.solve(sp.Eq(2*x, 1/x), x)) == {x1, -x1}
assert sp.solve(sp.Eq(x/2, 1/x), x) and x2 in sp.solve(sp.Eq(x/2, 1/x), x)
P1 = sp.integrate(2*x - x/2, (x, 0, x1))
P2 = sp.integrate(1/x - x/2, (x, x1, x2))
assert sp.simplify(P1 - R(3, 8)) == 0 and sp.simplify(P1 + P2 - sp.log(2)) == 0
for xv in (R(9, 10), R(1), R(13, 10)):
    assert 1/xv < 2*xv and 1/xv > xv/2

add(6, "ב",
    rubric=rub((r"נקודות החיתוך: $x=\frac{1}{\sqrt2}$ (בין $y=2x$ ל-$y=\frac{1}{x}$) ו-$x=\sqrt2$ (בין $y=\frac{x}{2}$ ל-$y=\frac{1}{x}$)", 3),
               (r"זיהוי הגבולות: למטה $y=\frac{x}{2}$, למעלה $y=2x$ ואחר כך $y=\frac{1}{x}$", 2),
               (r"הצבת שני אינטגרלים מתאימים", 2),
               (r"חישוב השטח $\ln2$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לקחת אינטגרל יחיד בין $y=2x$ ל-$y=\frac{x}{2}$ ולהתעלם מכך שהגבול העליון מתחלף ל-$y=\frac{1}{x}$.",
              r"לטעות בנקודת החיתוך של $y=\frac{x}{2}$ עם $y=\frac{1}{x}$: היא ב-$x=\sqrt2$ ולא ב-$x=2$."],
    steps=[
        num(r"מהו ה-$x$ של נקודת החיתוך של $y=2x$ עם $y=\frac{1}{x}$ ברביע הראשון? (עשרוני)", x1, r"$2x=\frac{1}{x}$ נותן $x^2=\frac{1}{2}$, כלומר $x=\frac{1}{\sqrt2}\approx0.7071$."),
        ch(r"מהו הגבול העליון של התחום עבור $\frac{1}{\sqrt2}\le x\le\sqrt2$?", r"$y=\frac{1}{x}$", [r"$y=2x$", r"$y=\frac{x}{2}$", r"$y=\frac{1}{x}+2x$"],
           r"בנקודה $x=1$ מתקיים $\frac{x}{2}=0.5<\frac{1}{x}=1<2x=2$. התחום חסום על ידי הנמוך מבין $2x$ ו-$\frac{1}{x}$, כלומר $\frac{1}{x}$ (נבדק ב-sympy)."),
        num(r"מהו האינטגרל על $0\le x\le\frac{1}{\sqrt2}$ של $2x-\frac{x}{2}$?", P1, r"$\frac{3x^2}{4}\Big|_0^{1/\sqrt2}=\frac{3}{8}=0.375$."),
        num(r"מהו השטח הכולל? (עשרוני)", P1 + P2, r"$\frac{3}{8}+\left(\ln2-\frac{3}{8}\right)=\ln2\approx0.6931$."),
    ],
    stepsSource="ai-verified")

exam = {
    "examCode": "20B-C",
    "examLabel": "מבחן סוף סמסטר קיץ תש\"פ, מועד ב'",
    "year": 2020,
    "examDate": "27/10/2020",
    "sourceFile": "calculus-1/20B-C exam.pdf",
    "solutionFile": "",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

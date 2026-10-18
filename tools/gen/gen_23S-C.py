# -*- coding: utf-8 -*-
"""Generator for tools/raw/23S-C.json -- calculus-1 (20151), summer semester 2023, special moed (05/01/2023).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23S-C.py

Source: sitting 23S-C, pp.1-9 (typed exam with the official worked solution after each question).
Part 1 (mandatory): Q1. Part 2: choose 4 of Q2-Q6 (a/b parts, 10% each). Weight of every question 20%.
NOTE: the header of this exam reads "הנדסת חשמל ואלקטרוניקה, מדעי מחשב" (lecturer ליובומיר מלייב) although the file is
filed under "שלנו". GATE1 excludes only 23A-A, 25A-A, 25A-B by code; the orchestrator should confirm 23S-C stays in scope.

Transcription notes
- Official solution transcribed in full, as printed. Rubric, pitfalls and steps are ai-draft (block below the questions).
- Q4b: the official solution computes V = e-2 = 0.714, dropping the factor pi, and e-2 is 0.718 not 0.714;
  the correct volume is pi*(e-2) (tools/verify/23S-C/check.py). Final-answer error -> "הפתרון הרשמי עם תיקון" label,
  solutionSource solved, official False (standing label rule, 2026-10-18); the working is kept as printed.
- Q3b: the official solution prints f(-3) = -59 but f(-3) = -65 (intermediate slip, sign and conclusion unaffected);
  corrected silently in the solution and steps, logged in docs/ASK_ADIR.md.
- Q6b (shipped as printed): the middle term of the |R1| chain repeats 1/(9*cbrt(c^5)); the bound 1/288 is correct (c>8).
- Q1 graph (p.2) is part of the official solution and is shipped as a figure.

Checks (tools/verify/23S-C/check.py, sympy): every derivative, limit, integral, extremum, sequence value and the
tangent line match the official answers except Q3b's intermediate value and Q4b above.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23S-C.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**1)** $D:\{-\infty<x<+\infty\}$.
**2)** $f(-x)=-2xe^{-\frac{(-x)^2}{2}}=-2xe^{-\frac{x^2}{2}}=-f(x)$, לכן הפונקציה אי-זוגית.
**3)** על הגרף של הפונקציה יש נקודה $(0,0)$.
**4)** $y'=f'(x)=2e^{-\frac{x^2}{2}}+2xe^{-\frac{x^2}{2}}(-x)=2e^{-\frac{x^2}{2}}(1-x^2)$.
$y'=0\Rightarrow x^2=1\Rightarrow x_1=1,\ x_2=-1$. סימני הנגזרת: $(-)$ עד $-1$, $(+)$ בין $-1$ ל-$+1$, $(-)$ אחרי $+1$.
$x=-1$: $f_{min}(-1)=-\frac{2}{\sqrt{e}}\Rightarrow$ נקודת מינימום מקומי $\left(-1,-\frac{2}{\sqrt{e}}\right)$.
$x=+1$: $f_{max}(+1)=\frac{2}{\sqrt{e}}\Rightarrow$ נקודת מקסימום מקומי $\left(+1,\frac{2}{\sqrt{e}}\right)$.
**5)** $y''=f''(x)=\left(2e^{-\frac{x^2}{2}}(1-x^2)\right)'=2e^{-\frac{x^2}{2}}(-x)(1-x^2)+2e^{-\frac{x^2}{2}}(-2x)=-2xe^{-\frac{x^2}{2}}(3-x^2)$.
$y''=0\Rightarrow\left(x_1=0,\ x_2=-\sqrt{3},\ x_3=+\sqrt{3}\right)$.
סימני הנגזרת השנייה: $(-)(\cap)$ עד $-\sqrt{3}$, $(+)(\cup)$ בין $-\sqrt{3}$ ל-$0$, $(-)(\cap)$ בין $0$ ל-$+\sqrt{3}$, $(+)(\cup)$ אחרי $+\sqrt{3}$.
נקודות פיתול: $x_1=0,\ x_2=-\sqrt{3},\ x_3=+\sqrt{3}$.
**6)** אין אסימפטוטה אנכית.
$a=\lim_{x\to+\infty}\frac{2x}{xe^{\frac{x^2}{2}}}=0$. יש אסימפטוטה אפקית מימין.
$b=\lim_{x\to+\infty}\frac{(2x)'}{\left(e^{\frac{x^2}{2}}\right)'}=\left|\frac{\infty}{\infty}\right|(\text{lopital})=\lim_{t\to+\infty}\frac{2}{xe^{\frac{x^2}{2}}}=\left|\frac{1}{\infty}\right|=0$.
יש אסימפטוטה אפקית מימין: $y=0x+0=0$, וגם אסימפטוטה משופעת משמאל $y=0$ (פונקציה אי-זוגית).

![הגרף הרשמי של הפונקציה](images/exams/23S-C-Q1-graph.png)
"""

SOL2A = r"""
הראו שהסדרה מונוטונית, חסומה ומצא את גבולה.
**חסומה:** נניח ש-$1\le a_n<2$ ($n=1\Rightarrow a_1=1<2$).
$n=k\Rightarrow 1\le a_k<2$. צ"ל: $n=k+1\Rightarrow 1\le a_{k+1}<2$.
$$a_{k+1}=\frac{a_k}{2}+1=\frac{1}{2}(a_k+2)\le\frac{1}{2}(2+2)=2$$
הסדרה חסומה.
**מונוטונית:** $a_{n+1}=\frac{a_n}{2}+1,\ a_1=1<a_2=\frac{1}{2}+1=\frac{3}{2}=1.5<a_3=1.75<a_4=1.875\Rightarrow\uparrow\ (?)$
$$a_{n+1}-a_n=\frac{a_n}{2}+1-a_n=1-\frac{a_n}{2}>1-\frac{2^-}{2}>0^+\Rightarrow a_n\uparrow$$
הסדרה עולה.
**3.** הסדרה עולה וחסומה לכן יש לה גבול:
מצא את גבולה: $\lim_{n\to\infty}a_{n+1}=a_n=L$,
$$\lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}\left(\frac{a_n}{2}+1\right)=\frac{L}{2}+1=L\Rightarrow 2L-L=L=2\Rightarrow(L=2)$$
"""

SOL2B = r"""
$$\int\frac{x^3-2x}{x^2+1}dx\left[x-\frac{3x}{x^2+1}\right]=\int x\,dx-\int\frac{3x}{x^2+1}dx=$$
$$=\frac{x^2}{2}-\frac{3}{2}\int\frac{d(x^2+1)}{x^2+1}dx=\frac{x^2}{2}-\frac{3}{2}\ln(x^2+1)+C$$
"""

SOL3A = r"""
$$\lim_{x\to1^-}f(x)=\lim_{x\to1^-}(ax^2+x)=a+1=f(1)$$
$$\lim_{x\to1^+}f(x)=\lim_{x\to1^-}(2x^2-bx)=2-b$$
פונקציה רציפה אם $a+1=2-b\Rightarrow a+b=1$.
$$f'(x)=\begin{cases}2ax+1, & x<1\\ 4x-b, & x>1\end{cases}$$
$f'(1^-)=2a+1,\quad f'(1^+)=4-b$.
פונקציה תהי גזירה אם: $f'(1^-)=f'(1^+)$, כלומר $2a+1=4-b\Rightarrow 2a+b=3$.
מקבלים:
$$\begin{cases}a+b=1\\ 2a+b=3\end{cases}\Rightarrow a=2,\ b=-1$$
"""

SOL3B = r"""
$$f'(x)=6x^2-2x+1$$
$$f'(x)=0\Rightarrow x\in\varnothing$$
$f'(x)>0$ הפונקציה עולה בתחום $(-\infty,\infty)$.
$$f(-3)=-65<0$$
$$f(0)=1>0$$
בקצוות הקטע סימנים של הפונקציה מנוגדים ופונקציה עולה בקטע, לכן יש נקודת חיתוך אחת עם ציר ה-$X$.
"""

SOL4A = r"""
$$\lim_{x\to\infty}\left(\frac{x^2+5x+4}{x^2-3x+7}\right)^{2x}=\lim_{x\to\infty}\left(\frac{x^2-3x+3x+7-7+5x+4}{x^2-3x+7}\right)^{2x}=$$
$$=\lim_{x\to\infty}\left(\frac{x^2-3x+7}{x^2-3x+7}+\frac{8x-3}{x^2-3x+7}\right)^{2x}=\lim_{x\to\infty}\left(1+\frac{8x-3}{x^2-3x+7}\right)^{2x}=$$
$$=\lim_{x\to\infty}\left(1+\frac{8x-3}{x^2-3x+7}\right)^{\frac{x^2-3x+7}{8x-3}\cdot\left(2x\cdot\frac{8x-3}{x^2-3x+7}\right)}\quad(*)$$
$$\left(\lim_{x\to\infty}\frac{16x^2-6x}{x^2-3x+7}\ \left(\frac{\infty}{\infty}\right)=\lim_{x\to\infty}\frac{x^2\left(16-\frac{6x}{x^2}\right)}{x^2\left(1-\frac{3x}{x^2}+\frac{7}{x^2}\right)}\right)=16\ \Rightarrow$$
$$(*)\Rightarrow\ =e^{16}.$$
"""

SOL4B = r"""
**הפתרון הרשמי עם תיקון:** בפתרון הרשמי הגורם $\pi$ שלפני האינטגרל נשמט בהמשך החישוב, והתשובה נכתבה $V=e-2\approx0.714$ (וגם $e-2\approx0.718$, לא $0.714$). הנפח הנכון הוא $V=\pi(e-2)\approx2.256$. החישוב עצמו מועתק כפי שפורסם, והשורה האחרונה מתוקנת. התיקון נבדק (sympy).
$$V_x=\pi\int_1^e\ln^2x\,dx\left[\begin{matrix}\ln^2x=u,\ du=2\frac{\ln x}{x}dx\\ dv=dx,\ v=x\end{matrix}\right]=x\ln^2x\Big|_1^e-2\int x\cdot\frac{1}{x}\ln x\,dx\left[\begin{matrix}\ln x=u,\ du=\frac{dx}{x}\\ dv=dx,\ v=x\end{matrix}\right]=$$
$$=\left(e\ln^2e-1\ln^21\right)-2\left(x\ln x\Big|_1^e-\int_1^e x\cdot\frac{1}{x}dx\right)=e-2\left(e\ln e-1\ln1-x\right)\Big|_1^e=e-2(e-0-e+1)=e-2$$
ולכן, עם הגורם $\pi$ שלפני האינטגרל:
$$V_x=\pi(e-2)\approx2.256$$
"""

SOL5A = r"""
$$y'=\pi\sin\left(\frac{y}{2}\right)+\pi x\cos\left(\frac{y}{2}\right)\frac{y'}{2}$$
$$y'=\frac{\pi\sin\left(\frac{y}{2}\right)}{1-\frac{\pi x}{2}\cos\left(\frac{y}{2}\right)}$$
$$y'(1)=\frac{\pi\sin\left(\frac{\pi}{2}\right)}{1-\frac{\pi x}{2}\cos\left(\frac{\pi}{2}\right)}=\pi$$
$$y-\pi=\pi(x-1)$$
$$y=\pi x$$
"""

SOL5B = r"""
$$\lim_{x\to0^+}x^{\frac{1}{\ln(e^x-1)}}\quad\left(\lim_{x\to0^+}0^{\frac{1}{\ln(e^0-1)}}\right)=\left(0^{\frac{1}{\ln0}}\right)\approx\left(0^0\right)=A,$$
$$=\lim_{x\to0^+}x^{\frac{1}{\ln(e^x-1)}}=A,\qquad\ln A=\lim_{x\to0^+}\ln\left(x^{\frac{1}{\ln(e^x-1)}}\right)\ \left(\ln0^0\right)=$$
$$=\lim_{x\to0^+}\frac{\ln x}{\ln(e^x-1)}\left(\frac{\infty}{\infty}\right)(\text{Lopital})=\lim_{x\to0^+}\frac{\left(\frac{1}{x}\right)}{\left(\frac{e^x}{e^x-1}\right)}=\lim_{x\to0^+}\frac{e^x-1}{x\cdot e^x}\left(\frac{0}{0}\right)$$
$$(\text{Lopital})=\lim_{x\to0^+}\frac{e^x}{e^x+x\cdot e^x}=\lim_{x\to0^+}\frac{e^x}{e^x+0}=1=\ln e=\ln A\Rightarrow A=e,$$
"""

SOL6A = r"""
$y=2x+3\sqrt[3]{x^2},\ x\in[-2,0],\ y'=$
$$=\left(2x+3\sqrt[3]{x^2}\right)'=\left(2x+3x^{\frac{2}{3}}\right)'=$$
$$=2+3\cdot\frac{2}{3}x^{-\frac{1}{3}}=2+\frac{2}{x^{\frac{1}{3}}}=\frac{2x^{\frac{1}{3}}+2}{x^{\frac{1}{3}}}\Rightarrow$$
$x=0\in[-2,0]\Rightarrow y'(0)=(-\infty,+\infty)$,
$$2x^{\frac{1}{3}}+2=2\left(x^{\frac{1}{3}}+1\right)=0\Rightarrow x^{\frac{1}{3}}+1=0\Rightarrow$$
$$\Rightarrow x^{\frac{1}{3}}=-1\Rightarrow x=-1\in[-2,0],$$
$y(0)=2\cdot0+3\cdot(0)^{\frac{2}{3}}=0-(\text{MIN}),\quad y(-1)=2\cdot(-1)+3\cdot\sqrt[3]{(-1)^2}=-2+3=+1>0-(\text{MAX}),$
$y(-2)=2\cdot(-2)+3\cdot\sqrt[3]{(-2)^2}=-4+3\sqrt[3]{4}\approx0.76>0,$
"""

SOL6B = r"""
$y=\sqrt[3]{x}=x^{1/3}$
$x_0=8,\ x=9,\quad(x-x_0)=1$
$y'=\frac{1}{3}x^{-\frac{2}{3}},\qquad y'(8)=\frac{1}{12}$
$$y''=-\frac{2}{9}x^{-\frac{5}{3}}=\frac{-2}{9\sqrt[3]{x^5}},\qquad y''(c)=\frac{-2}{9\sqrt[3]{c^5}}$$
$$y(9)=2+\frac{1}{12}+R_1$$
$$|R_1|=\frac{1}{9\sqrt[3]{c^5}}\le\frac{1}{9\sqrt[3]{c^5}}=\frac{1}{288}<0.01$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=2xe^{-\frac{x^2}{2}}$ לפי הסעיפים הבאים:"
      "\nתחום הגדרה, תחומי עליה/ירידה, נקודות קיצון, קמירות ונקודות פיתול, אסימפטוטות. שרטטו את גרף הפונקציה.",
      SOL1, points=20),

    Q(2, "proof", "sequences_limits",
      r"נתונה הסדרה: $a_{n+1}=\frac{a_n}{2}+1,\ a_1=1$." "\nהוכיחו שהסדרה מונוטונית, חסומה ומצאו את גבולה.",
      SOL2A, part="א", points=10),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int\frac{x^3-2x}{x^2+1}\,dx$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "derivatives_tangents",
      r"נתונה הפונקציה $f(x)=\begin{cases}ax^2+x, & x\le1\\ 2x^2-bx, & x>1\end{cases}$"
      "\n" r"מצאו ערכים של $a$ ו-$b$ כך שהפונקציה $f(x)$ תהיה גזירה לכל $x$ ממשי.",
      SOL3A, part="א", points=10),

    Q(3, "proof", "continuity",
      r"הוכיחו שלמשוואה $2x^3-x^2+x+1=0$ קיים פתרון ממשי אחד בקטע $[-3,0]$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "function_limits",
      r"חשבו את הגבול: $\lim_{x\to\infty}\left(\frac{x^2+5x+4}{x^2-3x+7}\right)^{2x}$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"תחום שמוגבל ע״י הקווים $y=0$ ו-$y=\ln x$ בתחום $(1\le x\le e)$ מסתובב סביב ציר ה-$X$. חשבו את נפח של גוף הסיבוב בקטע.",
      SOL4B, part="ב", points=10, solutionSource="solved", official=False),

    Q(5, "computation", "derivatives_tangents",
      r"רשמו את משוואת המשיק לגרף של הפונקציה $y=f(x)$ המוגדרת באמצעות משוואה: $y=\pi x\sin\left(\frac{y}{2}\right)$ בנקודה $(1,\pi)$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "function_limits",
      r"חשבו את הגבול: $\lim_{x\to0^+}x^{\frac{1}{\ln(e^x-1)}}$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "extrema_optimization",
      r"מצאו את הערך המקסימלי והערך המינימלי של הפונקציה $y=2x+3\sqrt[3]{x^2}$ בקטע $x\in[-2,0]$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "lhopital_taylor",
      r"באמצעות נוסחת טיילור חשבו בקירוב $\sqrt[3]{9}$ כך ששגיאת החישוב תהיה קטנה מ-$0.01$.",
      SOL6B, part="ב", points=10),
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


an = sp.Symbol('a_n', real=True)

# ===== Q1: f = 2x e^{-x^2/2} =====
Eg = sp.exp(-x**2/2)
f1 = 2*x*Eg
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, 2*Eg*(1 - x**2)) and same(f1pp, -2*x*Eg*(3 - x**2))
assert sp.simplify(f1.subs(x, -x) + f1) == 0
assert sp.solve(sp.Eq(1 - x**2, 0), x) == [-1, 1] and sorted(sp.solve(sp.Eq(x*(3 - x**2), 0), x)) == [-sp.sqrt(3), 0, sp.sqrt(3)]
fmax1 = sp.simplify(f1.subs(x, 1))
assert sp.simplify(fmax1 - 2/sp.sqrt(sp.E)) == 0
assert sp.limit(f1, x, sp.oo) == 0 and sp.limit(f1, x, -sp.oo) == 0

add(1,
    rubric=rub(("תחום הגדרה $\\mathbb{R}$ וזיהוי שהפונקציה אי-זוגית (סימטריה לראשית)", 3),
               ("נגזרת $f'(x)=2e^{-\\frac{x^2}{2}}\\left(1-x^2\\right)$, נקודות קריטיות $x=\\pm1$, תחומי עליה וירידה וסיווג הקיצון: מקסימום $\\left(1,\\frac{2}{\\sqrt{e}}\\right)$ ומינימום $\\left(-1,-\\frac{2}{\\sqrt{e}}\\right)$", 7),
               ("נגזרת שנייה $f''(x)=-2xe^{-\\frac{x^2}{2}}\\left(3-x^2\\right)$, קמירות ונקודות פיתול $x=0,\\pm\\sqrt{3}$", 4),
               ("אסימפטוטה אופקית $y=0$ ב-$\\pm\\infty$ וללא אסימפטוטה אנכית", 3),
               ("שרטוט הגרף בהתאם לכל הנתונים", 3)),
    rubricSource="ai-verified",
    pitfalls=["לגזור $e^{-\\frac{x^2}{2}}$ בלי כלל השרשרת, ולשכוח את הגורם $-x$.",
              "לפספס את $x=0$ כנקודת פיתול: $f''$ מתאפסת שם ומשנה סימן.",
              "לחפש אסימפטוטה משופעת כשהגבול $\\lim\\frac{f(x)}{x}=0$ נותן אסימפטוטה אופקית $y=0$."],
    steps=[
        ch("מהי הזוגיות של $f(x)=2xe^{-\\frac{x^2}{2}}$?", "אי-זוגית: $f(-x)=-f(x)$",
           ["זוגית: $f(-x)=f(x)$", "לא זוגית ולא אי-זוגית", "מחזורית"],
           "$e^{-\\frac{x^2}{2}}$ זוגית ו-$2x$ אי-זוגית, ולכן המכפלה אי-זוגית (נבדק ב-sympy)."),
        chx("מהי הנגזרת של $f$?", 2*Eg*(1 - x**2),
            [2*Eg*(1 + x**2), 2*Eg*(1 - x), 2*Eg*(1 - 2*x**2)],
            lambda e: same(e, f1p),
            "גזירת מכפלה: $f'=2e^{-\\frac{x^2}{2}}+2x\\cdot e^{-\\frac{x^2}{2}}(-x)=2e^{-\\frac{x^2}{2}}\\left(1-x^2\\right)$ (נבדק ב-sympy)."),
        num("מהו ערך המקסימום המקומי $f(1)$? (עשרוני)", fmax1, "$f(1)=\\frac{2}{\\sqrt{e}}\\approx1.2131$."),
        num("מהו הערך החיובי של $x$ שבו $f''(x)=-2xe^{-\\frac{x^2}{2}}\\left(3-x^2\\right)$ מתאפסת? (עשרוני)", sp.sqrt(3),
            "$x\\left(3-x^2\\right)=0$ נותן $x=0,\\pm\\sqrt{3}$, והערך החיובי הוא $\\sqrt{3}\\approx1.7321$."),
        ch("מהי האסימפטוטה של $f$ ב-$\\pm\\infty$?", "אופקית: $y=0$",
           ["משופעת: $y=x$", "אנכית: $x=0$", "אין אסימפטוטות"],
           "$\\lim_{x\\to\\pm\\infty}2xe^{-\\frac{x^2}{2}}=0$ (אומת ב-sympy), ולכן $y=0$ אופקית; אין נקודת אי-רציפות ולכן אין אנכית."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: a_1 = 1, a_{n+1} = a_n/2 + 1 =====
seq2 = lim_iter(lambda v: v/2 + 1, 1)
assert abs(seq2[3] - R(15, 8)) < 1e-40 and all(v < 2 for v in seq2) and all(seq2[i + 1] > seq2[i] for i in range(len(seq2) - 1))
for bd in (R(3, 2), R(9, 5), R(19, 10)):
    assert any(v >= bd for v in seq2), bd
L_ = sp.Symbol('L', real=True)
assert sp.solve(sp.Eq(L_, L_/2 + 1), L_) == [2]

L2a = [r"חסימות באינדוקציה: $a_1=1<2$, ואם $1\le a_k<2$ אז $a_{k+1}=\frac12(a_k+2)<\frac12(2+2)=2$; לכן הסדרה חסומה.",
       r"מונוטוניות: $a_{n+1}-a_n=1-\frac{a_n}{2}>0$ כי $a_n<2$; לכן הסדרה עולה.",
       r"הסדרה עולה וחסומה, ולכן מתכנסת לגבול $L$.",
       r"בנוסחת הנסיגה $L=\frac{L}{2}+1$, ולכן $L=2$."]

add(2, "א",
    rubric=rub(("הוכחת חסימות $1\\le a_n<2$ באינדוקציה (בסיס וצעד)", 3),
               ("הוכחת מונוטוניות: $a_{n+1}-a_n=1-\\frac{a_n}{2}>0$", 3),
               ("הסקה שסדרה עולה וחסומה מתכנסת", 1),
               ("מעבר לגבול בנוסחת הנסיגה: $L=\\frac{L}{2}+1$", 2),
               ("פתרון $L=2$", 1)),
    rubricSource="ai-verified",
    pitfalls=["להסיק מכמה איברים ראשונים ($1,1.5,1.75,\\ldots$) שהסדרה עולה, בלי הוכחה.",
              "לפתור את $L=\\frac{L}{2}+1$ לפני שהוכח שהגבול קיים.",
              "להוכיח את המונוטוניות בלי החסם $a_n<2$, שהוא מה שמבטיח $1-\\frac{a_n}{2}>0$."],
    steps=[
        num("מהו $a_4$ בסדרה $a_1=1$, $a_{n+1}=\\frac{a_n}{2}+1$? (עשרוני)", seq2[3],
            "$a_2=1.5$, $a_3=1.75$, $a_4=1.875$."),
        ch("איזה חסם עליון, מבין האפשרויות, מתקיים לכל איברי הסדרה (והוא גם הגבול)?", "$a_n<2$",
           ["$a_n<1.5$", "$a_n<1.8$", "$a_n<1.9$"],
           "כבר $a_3=1.75>1.5$, $a_4=1.875>1.8$ ו-$a_5=1.9375>1.9$; רק $2$ נשמר לכל $n$ (נבדק ב-40 האיברים הראשונים)."),
        chx("מהו $a_{n+1}-a_n$ כביטוי ב-$a_n$?", 1 - an/2,
            [an/2 - 1, 1 + an/2, 1 - 2*an],
            lambda e: sp.expand(e - (an/2 + 1 - an)) == 0,
            "$a_{n+1}-a_n=\\frac{a_n}{2}+1-a_n=1-\\frac{a_n}{2}$, וזה חיובי כאשר $a_n<2$ (נבדק ב-sympy)."),
        order("סדרו את שלבי ההוכחה.", L2a,
              "החסימות קודם (המונוטוניות נשענת על $a_n<2$), אחר כך המונוטוניות, ההתכנסות, וחישוב הגבול."),
        num("מהו גבול הסדרה?", 2, "$L=\\frac{L}{2}+1$ נותן $\\frac{L}{2}=1$, כלומר $L=2$."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: int (x^3 - 2x)/(x^2 + 1) =====
g2b = (x**3 - 2*x)/(x**2 + 1)
F2b = x**2/2 - R(3, 2)*sp.log(x**2 + 1)
assert same(g2b, x - 3*x/(x**2 + 1)) and same(sp.diff(F2b, x), g2b)
def2b = sp.N(F2b.subs(x, 1) - F2b.subs(x, 0), 30)
assert abs(def2b - sp.N(sp.Integral(g2b, (x, 0, 1)), 30)) < 1e-12

add(2, "ב",
    rubric=rub(("חילוק פולינומים: $\\frac{x^3-2x}{x^2+1}=x-\\frac{3x}{x^2+1}$", 4),
               ("אינטגרל $\\int x\\,dx=\\frac{x^2}{2}$", 2),
               ("אינטגרל $\\int\\frac{3x}{x^2+1}dx=\\frac{3}{2}\\ln\\left(x^2+1\\right)$", 3),
               ("תשובה סופית עם $+C$", 1)),
    rubricSource="ai-verified",
    pitfalls=["לנסות פירוק לשברים חלקיים כשהמונה מדרגה גבוהה מהמכנה: קודם חייבים לחלק.",
              "לאנטגרל $\\frac{3x}{x^2+1}$ כ-$3\\ln\\left(x^2+1\\right)$ ולשכוח את הגורם $\\frac{1}{2}$ מהנגזרת הפנימית $2x$.",
              "לשכוח את הערך המוחלט או את התנאי $x^2+1>0$: כאן הביטוי תמיד חיובי ולכן אין צורך בערך מוחלט."],
    steps=[
        chx("מהי תוצאת חילוק הפולינומים $\\frac{x^3-2x}{x^2+1}$?", x - 3*x/(x**2 + 1),
            [x - 2*x/(x**2 + 1), x + 3*x/(x**2 + 1), x - 3/(x**2 + 1)],
            lambda e: same(e, g2b),
            "$x^3-2x=x\\left(x^2+1\\right)-3x$, ולכן המנה היא $x-\\frac{3x}{x^2+1}$ (נבדק ב-sympy)."),
        chx("מהי התוצאה (בלי הקבוע)?", F2b,
            [x**2/2 - 3*sp.log(x**2 + 1), x**2/2 - R(3, 2)*sp.atan(x), x**2/2 + R(3, 2)*sp.log(x**2 + 1)],
            lambda e: same(sp.diff(e, x), g2b),
            "$\\int\\frac{3x}{x^2+1}dx=\\frac{3}{2}\\ln\\left(x^2+1\\right)$ כי $\\left(x^2+1\\right)'=2x$ (נבדק ב-sympy)."),
        num("מהו הערך של האינטגרל המסוים $\\int_0^1\\frac{x^3-2x}{x^2+1}dx$? (עשרוני)", def2b,
            "$F(1)-F(0)=\\frac{1}{2}-\\frac{3}{2}\\ln2\\approx-0.5397$."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: differentiability of a piecewise function, a and b =====
cont_poly = (a*1**2 + 1) - (2*1**2 - b)
der_poly = (2*a*1 + 1) - (4*1 - b)
sol3 = sp.solve([cont_poly, der_poly], [a, b], dict=True)[0]
assert sol3 == {a: 2, b: -1} and sp.expand(cont_poly - (a + b - 1)) == 0 and sp.expand(der_poly - (2*a + b - 3)) == 0
for bad in (a + b - 3, a - b - 1, 2*a + b - 1):
    assert sp.expand(bad - cont_poly) != 0 and sp.solve([bad, der_poly], [a, b], dict=True) != [sol3]
for bad in (2*a + b - 5, 2*a - b - 3, a + 2*b - 3):
    assert sp.expand(bad - der_poly) != 0 and sp.solve([cont_poly, bad], [a, b], dict=True) != [sol3]

add(3, "א",
    rubric=rub(("תנאי הרציפות ב-$x=1$: $a+1=2-b$, כלומר $a+b=1$", 3),
               ("נגזרות הענפים: $2ax+1$ עבור $x<1$ ו-$4x-b$ עבור $x>1$", 2),
               ("תנאי הגזירות $f'(1^-)=f'(1^+)$: $2a+b=3$", 2),
               ("פתרון המערכת: $a=2$, $b=-1$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לדרוש רק שוויון נגזרות ולשכוח את תנאי הרציפות (גזירות מחייבת רציפות).",
              "להשוות נגזרות חד-צדדיות לפי הנוסחאות של הענפים בלי לוודא שהן מוגדרות לפי הענף הנכון ($x\\le1$ משמאל, $x>1$ מימין).",
              "טעות בגזירת $2x^2-bx$: הנגזרת היא $4x-b$."],
    steps=[
        ch("איזו משוואה נותנת את תנאי הרציפות ב-$x=1$ ($f(1)=a+1$ והגבול מימין $2-b$)?", "$a+b=1$",
           ["$a+b=3$", "$a-b=1$", "$2a+b=1$"],
           "$a+1=2-b$ שקול ל-$a+b=1$ (נבדק ב-sympy; בצירוף $2a+b=3$ האפשרויות $a+b=3$ ו-$a-b=1$ נותנות פתרון אחר, והאפשרות $2a+b=1$ סותרת את $2a+b=3$ ולכן למערכת אין פתרון)."),
        ch("איזו משוואה נותנת את תנאי הגזירות, $f'(1^-)=2a+1$ ו-$f'(1^+)=4-b$?", "$2a+b=3$",
           ["$2a+b=5$", "$2a-b=3$", "$a+2b=3$"],
           "$2a+1=4-b$ שקול ל-$2a+b=3$ (נבדק ב-sympy)."),
        num("מהו הערך של $a$ במערכת $a+b=1$, $2a+b=3$?", sol3[a], "חיסור המשוואות נותן $a=2$."),
        num("מהו הערך של $b$ במערכת $a+b=1$, $2a+b=3$?", sol3[b], "$b=1-a=-1$."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: 2x^3 - x^2 + x + 1 = 0 has exactly one root in [-3, 0] =====
h3 = 2*x**3 - x**2 + x + 1
assert sp.diff(h3, x) == 6*x**2 - 2*x + 1 and sp.discriminant(6*x**2 - 2*x + 1, x) == -20
assert h3.subs(x, -3) == -65 and h3.subs(x, 0) == 1 and len([r for r in sp.Poly(h3, x).nroots() if abs(sp.im(r)) < 1e-12]) == 1

add(3, "ב",
    rubric=rub(("נגזרת $f'(x)=6x^2-2x+1$", 2),
               ("הוכחה ש-$f'(x)>0$ לכל $x$ (דיסקרימיננטה שלילית), ולכן $f$ עולה ממש", 3),
               ("סימנים מנוגדים בקצוות: $f(-3)<0<f(0)=1$", 3),
               ("מסקנה: קיום (ערך הביניים) ויחידות (מונוטוניות ממש)", 2)),
    rubricSource="ai-verified",
    pitfalls=["להסתפק בסימנים מנוגדים בקצוות: זה מוכיח רק קיום של שורש אחד לפחות, לא יחידות.",
              "לטעון ש-$f'(x)\\neq0$ בלי להראות שהיא חיובית (סימן קבוע) בכל התחום.",
              "לטעות בחישוב $f(-3)$: הערך הוא $2(-27)-9-3+1=-65$; הסימן (שלילי) הוא החשוב להוכחה."],
    steps=[
        num("מהי הדיסקרימיננטה של $f'(x)=6x^2-2x+1$ (כלומר $b^2-4ac$)?", -20,
            "$(-2)^2-4\\cdot6\\cdot1=4-24=-20<0$, ולכן $f'$ אינה מתאפסת ומקדם $x^2$ חיובי: $f'>0$ תמיד."),
        num("מהו $f(-3)$ עבור $f(x)=2x^3-x^2+x+1$?", -65,
            "$2(-27)-9-3+1=-65$; רק הסימן (שלילי) משמש בהוכחה."),
        num("מהו $f(0)$?", 1, "$f(0)=1>0$."),
        ch("מה מבטיח את הקיום ומה את היחידות של השורש בקטע?",
           "קיום: משפט ערך הביניים (סימנים מנוגדים בקצוות). יחידות: $f'>0$, ולכן $f$ עולה ממש",
           ["קיום: משפט רול. יחידות: משפט ערך הביניים",
            "קיום: $f'>0$. יחידות: סימנים מנוגדים בקצוות",
            "קיום: משפט ערך הביניים. יחידות: $f'$ מתאפסת בנקודה אחת בקטע"],
           "רול דורש $f(-3)=f(0)$, אבל $-65\\neq1$. מונוטוניות אינה מבטיחה קיום (למשל $e^x$), וסימנים מנוגדים אינם מבטיחים יחידות. כאן $f'$ אינה מתאפסת כלל."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: lim ((x^2+5x+4)/(x^2-3x+7))^{2x} = e^16 =====
base4 = (x**2 + 5*x + 4)/(x**2 - 3*x + 7)
g4 = (8*x - 3)/(x**2 - 3*x + 7)
assert same(base4 - 1, g4, pts=(0.5, 1.5, 2.5, 4.0, 7.0))
assert sp.limit(2*x*g4, x, sp.oo) == 16 and sp.limit(base4**(2*x), x, sp.oo) == sp.exp(16)

add(4, "א",
    rubric=rub(("זיהוי הצורה $1^\\infty$", 1),
               ("כתיבת הבסיס כ-$1+\\frac{8x-3}{x^2-3x+7}$", 3),
               ("שימוש בגבול $(1+u)^{1/u}\\to e$ ושכתוב המעריך", 2),
               ("חישוב גבול המכפלה $2x\\cdot\\frac{8x-3}{x^2-3x+7}\\to16$", 3),
               ("תשובה סופית $e^{16}$", 1)),
    rubricSource="ai-verified",
    pitfalls=["להניח ש-$1^\\infty=1$: זו צורה לא מוגדרת, והמעריך הגדל משפיע.",
              "לטעות בחיסור $\\left(x^2+5x+4\\right)-\\left(x^2-3x+7\\right)=8x-3$ (ולא $2x-3$).",
              "לשכוח לכפול את $\\frac{8x-3}{x^2-3x+7}$ במעריך המקורי $2x$ ולהשאיר $e^8$."],
    steps=[
        ch("מהי הצורה הלא מוגדרת של הגבול?", "$1^\\infty$",
           ["$\\infty^0$", "$0^0$", "$\\frac{\\infty}{\\infty}$"],
           "הבסיס $\\frac{x^2+5x+4}{x^2-3x+7}\\to1$ והמעריך $2x\\to\\infty$."),
        chx("הבסיס הוא $1+g(x)$. מהו $g(x)$?", g4,
            [(8*x + 3)/(x**2 - 3*x + 7), (8*x - 3)/(x**2 + 5*x + 4), (2*x - 3)/(x**2 - 3*x + 7)],
            lambda e: same(e, base4 - 1, pts=(0.5, 1.5, 2.5, 4.0, 7.0)),
            "$\\left(x^2+5x+4\\right)-\\left(x^2-3x+7\\right)=8x-3$, ומחלקים במכנה $x^2-3x+7$ (נבדק ב-sympy)."),
        num("מהו $\\lim_{x\\to\\infty}2x\\cdot\\frac{8x-3}{x^2-3x+7}$?", 16,
            "הדרגות שוות, ולכן הגבול הוא מנת המקדמים המובילים: $\\frac{16}{1}=16$ (אומת ב-sympy)."),
        ch("מהו הגבול המבוקש?", "$e^{16}$",
           ["$e^{8}$", "$e^{-16}$", "$e^{2}$"],
           "$(1+g)^{2x}=\\left((1+g)^{1/g}\\right)^{2xg}\\to e^{16}$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: volume of revolution of y = ln x, 1 <= x <= e =====
V4 = sp.pi*sp.integrate(sp.log(x)**2, (x, 1, sp.E))
assert sp.simplify(V4 - sp.pi*(sp.E - 2)) == 0
AF4 = x*sp.log(x)**2 - 2*x*sp.log(x) + 2*x
assert same(sp.diff(AF4, x), sp.log(x)**2)
opt = {"good": sp.pi*sp.integrate(sp.log(x)**2, (x, 1, sp.E)), "b1": sp.pi*sp.integrate(sp.log(x), (x, 1, sp.E)),
       "b2": 2*sp.pi*sp.integrate(sp.log(x)**2, (x, 1, sp.E)), "b3": sp.pi*sp.integrate(sp.log(x)**2, (x, 0, 1))}
assert sp.simplify(opt["good"] - sp.pi*(sp.E - 2)) == 0 and all(sp.simplify(opt[k] - opt["good"]) != 0 for k in ("b1", "b2", "b3"))

add(4, "ב",
    rubric=rub(("נוסחת הנפח $V=\\pi\\int_1^e\\ln^2x\\,dx$ (כולל הגורם $\\pi$)", 3),
               ("אינטגרציה בחלקים ראשונה: $x\\ln^2x-2\\int\\ln x\\,dx$", 3),
               ("אינטגרציה בחלקים שנייה וקדומה $x\\ln^2x-2x\\ln x+2x$", 2),
               ("הצבת הגבולות: $\\int_1^e\\ln^2x\\,dx=e-2$ והנפח $V=\\pi(e-2)$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להשמיט את הגורם $\\pi$ מהתשובה הסופית (טעות שמופיעה גם בפתרון הרשמי המודפס).",
              "לשכוח שיש להפעיל אינטגרציה בחלקים פעמיים, כי $\\int\\ln x\\,dx$ עדיין דורש חלקים.",
              "לחשב את $e-2$ כ-$0.714$: הערך הנכון הוא $0.718$, ו-$V\\approx2.256$ אחרי הכפלה ב-$\\pi$."],
    steps=[
        ch("איזה ביטוי נותן את נפח הסיבוב סביב ציר ה-$X$ של התחום מתחת ל-$y=\\ln x$ עבור $1\\le x\\le e$?",
           r"$V=\pi\int_1^e\ln^2x\,dx$",
           [r"$V=\pi\int_1^e\ln x\,dx$", r"$V=2\pi\int_1^e\ln^2x\,dx$", r"$V=\pi\int_0^1\ln^2x\,dx$"],
           "שיטת הדיסקות: $V=\\pi\\int y^2dx$. ערכי האפשרויות: $\\pi(e-2)\\approx2.26$, $\\pi\\approx3.14$, $2\\pi(e-2)\\approx4.51$, $2\\pi\\approx6.28$ (נבדק ב-sympy)."),
        chx("מהי הקדומה של $\\ln^2x$ (בלי הקבוע)?", AF4,
            [x*sp.log(x)**2 - 2*x*sp.log(x), x*sp.log(x)**2 + 2*x*sp.log(x) + 2*x, sp.log(x)**3/3],
            lambda e: same(sp.diff(e, x), sp.log(x)**2),
            "שתי אינטגרציות בחלקים נותנות $x\\ln^2x-2x\\ln x+2x$; הנגזרת מחזירה $\\ln^2x$ (נבדק ב-sympy)."),
        num("מהו $\\int_1^e\\ln^2x\\,dx$? (עשרוני)", sp.E - 2, "$F(e)-F(1)=e-2\\approx0.7183$."),
        num("מהו הנפח $V=\\pi(e-2)$? (עשרוני)", V4, "$V=\\pi(e-2)\\approx2.2565$."),
    ],
    stepsSource="ai-verified")

# ===== Q5a: tangent to the implicit curve y = pi x sin(y/2) at (1, pi) =====
yy = sp.Symbol('y', real=True)
eq5 = yy - sp.pi*x*sp.sin(yy/2)
yp5 = sp.idiff(eq5, yy, x)
good5 = sp.pi*sp.sin(yy/2)/(1 - sp.pi*x*sp.cos(yy/2)/2)
assert sp.simplify(yp5 - good5) == 0 and eq5.subs({x: 1, yy: sp.pi}) == 0
slope5 = sp.simplify(good5.subs({x: 1, yy: sp.pi}))
assert slope5 == sp.pi
tl5 = sp.pi*x
tl5_ok = lambda e: sp.simplify(e.subs(x, 1) - sp.pi) == 0 and sp.simplify(sp.diff(e, x) - sp.pi) == 0

add(5, "א",
    rubric=rub(("גזירה סתומה של שני האגפים: כלל מכפלה לגזירת $\\pi x\\sin\\frac{y}{2}$", 4),
               ("בידוד $y'=\\frac{\\pi\\sin\\frac{y}{2}}{1-\\frac{\\pi x}{2}\\cos\\frac{y}{2}}$", 2),
               ("חישוב השיפוע בנקודה: $y'(1)=\\pi$", 2),
               ("משוואת המשיק $y=\\pi x$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח שגם $y$ תלוי ב-$x$: הנגזרת של $\\sin\\frac{y}{2}$ היא $\\cos\\frac{y}{2}\\cdot\\frac{y'}{2}$.",
              "לבודד את $y'$ בלי להעביר את האיבר המכיל $y'$ מאגף ימין לאגף שמאל.",
              "להציב $x=1,\\ y=\\pi$ לפני הגזירה במקום אחריה."],
    steps=[
        chx("מהו $y'$ מגזירה סתומה של $y=\\pi x\\sin\\frac{y}{2}$?", good5,
            [sp.pi*sp.sin(yy/2)/(1 + sp.pi*x*sp.cos(yy/2)/2), sp.pi*sp.sin(yy/2),
             sp.pi*sp.sin(yy/2)/(1 - sp.pi*x*sp.cos(yy/2))],
            lambda e: sp.simplify(e - yp5) == 0,
            "$y'=\\pi\\sin\\frac{y}{2}+\\frac{\\pi x}{2}\\cos\\frac{y}{2}\\cdot y'$, ומבודדים את $y'$ (נבדק ב-sympy)."),
        num("מהו השיפוע $y'(1)$ בנקודה $(1,\\pi)$? (עשרוני)", slope5,
            "$\\sin\\frac{\\pi}{2}=1$ ו-$\\cos\\frac{\\pi}{2}=0$, ולכן $y'(1)=\\pi\\approx3.1416$."),
        chx("מהי משוואת המשיק בנקודה $(1,\\pi)$?", tl5,
            [sp.pi*x - sp.pi, x, sp.pi*x + 1],
            tl5_ok,
            "המשיק עובר דרך $(1,\\pi)$ בשיפוע $\\pi$: $y-\\pi=\\pi(x-1)$, כלומר $y=\\pi x$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: lim x^{1/ln(e^x - 1)} = e =====
lnA = sp.log(x)/sp.log(sp.exp(x) - 1)
assert sp.limit(lnA, x, 0, '+') == 1 and sp.exp(sp.limit(lnA, x, 0, '+')) == sp.E
lh5 = (1/x)/(sp.exp(x)/(sp.exp(x) - 1))
P5 = (0.2, 0.5, 0.9, 1.4, 2.0)
assert same(lh5, (sp.exp(x) - 1)/(x*sp.exp(x)), pts=P5) and sp.limit((sp.exp(x) - 1)/(x*sp.exp(x)), x, 0, '+') == 1
assert sp.limit(sp.log(sp.exp(x) - 1), x, 0, '+') == -sp.oo

add(5, "ב",
    rubric=rub(("זיהוי הצורה $0^0$ וסימון הגבול ב-$A$", 2),
               ("לקיחת לוגריתם והפיכה למנה $\\ln A=\\lim\\frac{\\ln x}{\\ln\\left(e^x-1\\right)}$ מהצורה $\\frac{\\infty}{\\infty}$", 2),
               ("הפעלת לופיטל וקבלת $\\frac{e^x-1}{xe^x}$", 2),
               ("לופיטל שנייה על $\\frac{0}{0}$ או גבול יסודי, וקבלת הערך $1$", 2),
               ("מסקנה $\\ln A=1$, כלומר $A=e$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להשאיר את התשובה כ-$\\ln A=1$ בלי לחזור ל-$A=e$.",
              "לגזור את $\\ln\\left(e^x-1\\right)$ בלי כלל השרשרת: הנגזרת היא $\\frac{e^x}{e^x-1}$.",
              "להניח ש-$0^0=1$ אוטומטית: זו צורה לא מוגדרת וכאן הגבול הוא $e$."],
    steps=[
        ch("מהי הצורה הלא מוגדרת של $\\lim_{x\\to0^+}x^{\\frac{1}{\\ln(e^x-1)}}$?", "$0^0$",
           ["$\\infty^0$", "$1^\\infty$", "$0\\cdot\\infty$"],
           "הבסיס $x\\to0^+$, ו-$\\ln\\left(e^x-1\\right)\\to-\\infty$ ולכן המעריך $\\frac{1}{\\ln(e^x-1)}\\to0$ (אומת ב-sympy)."),
        chx("אחרי לוגריתם מקבלים $\\frac{\\ln x}{\\ln(e^x-1)}$. מהי המנה $\\frac{(\\ln x)'}{\\left(\\ln(e^x-1)\\right)'}$ אחרי פישוט?",
            (sp.exp(x) - 1)/(x*sp.exp(x)),
            [x*sp.exp(x)/(sp.exp(x) - 1), (sp.exp(x) - 1)/sp.exp(x), (sp.exp(x) - 1)/x],
            lambda e: same(e, lh5, pts=P5),
            "$(\\ln x)'=\\frac{1}{x}$ ו-$\\left(\\ln(e^x-1)\\right)'=\\frac{e^x}{e^x-1}$, ולכן המנה היא $\\frac{e^x-1}{xe^x}$ (נבדק ב-sympy)."),
        num("מהו $\\lim_{x\\to0^+}\\frac{e^x-1}{xe^x}$?", 1,
            "$\\frac{e^x-1}{x}\\to1$ ו-$e^x\\to1$ (או לופיטל נוספת: $\\frac{e^x}{e^x+xe^x}\\to1$) (אומת ב-sympy)."),
        num("מהו ערך הגבול המקורי $A$? (עשרוני)", sp.E, "$\\ln A=1$ ולכן $A=e\\approx2.7183$."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: extrema of y = 2x + 3 x^{2/3} on [-2, 0] =====
import mpmath as _mp
cbrt = lambda t: _mp.sign(t)*abs(t)**(_mp.mpf(1)/3)
yfun = lambda t: 2*t + 3*cbrt(t)**2
grid = [(-2 + _mp.mpf(k)/20000) for k in range(0, 40001)]
vals = [yfun(g) for g in grid]
assert abs(max(vals) - 1) < 1e-6 and abs(min(vals)) < 1e-6
assert abs(_mp.findroot(lambda t: _mp.diff(yfun, t), -0.8) + 1) < 1e-9
y2 = yfun(_mp.mpf(-2))
assert abs(y2 - (-4 + 3*_mp.mpf(4)**(_mp.mpf(1)/3))) < 1e-12
dopts = {"good": lambda t: 2 + 2/cbrt(t), "b1": lambda t: 2 + 3/cbrt(t), "b2": lambda t: 2 + 2*cbrt(t), "b3": lambda t: 2 + 2/(3*cbrt(t))}
for pt in (-0.5, -1.5, -0.2):
    pt = _mp.mpf(pt)
    assert abs(_mp.diff(yfun, pt) - dopts["good"](pt)) < 1e-9
    for k in ("b1", "b2", "b3"):
        assert abs(_mp.diff(yfun, pt) - dopts[k](pt)) > 1e-3

add(6, "א",
    rubric=rub(("נגזרת $y'=2+\\frac{2}{\\sqrt[3]{x}}$", 2),
               ("נקודות חשודות: $x=-1$ (הנגזרת מתאפסת) ו-$x=0$ (הנגזרת לא מוגדרת)", 3),
               ("חישוב ערכי הפונקציה: $y(-2)\\approx0.76$, $y(-1)=1$, $y(0)=0$", 3),
               ("קביעה: מקסימום $1$ ומינימום $0$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח ש-$x=0$ היא נקודה חשודה כי $y'$ לא מוגדרת שם (וגם קצה הקטע).",
              "לשכוח לחשב את $y(-2)$ בקצה השמאלי של הקטע.",
              "לטעות בגזירת $x^{\\frac{2}{3}}$: הנגזרת היא $\\frac{2}{3}x^{-\\frac{1}{3}}$, ולכן $3x^{\\frac{2}{3}}$ נותן $2x^{-\\frac{1}{3}}$."],
    steps=[
        ch("מהי הנגזרת של $y=2x+3\\sqrt[3]{x^2}$?", "$y'=2+\\frac{2}{\\sqrt[3]{x}}$",
           ["$y'=2+\\frac{3}{\\sqrt[3]{x}}$", "$y'=2+2\\sqrt[3]{x}$", "$y'=2+\\frac{2}{3\\sqrt[3]{x}}$"],
           "$\\left(3x^{\\frac{2}{3}}\\right)'=3\\cdot\\frac{2}{3}x^{-\\frac{1}{3}}=\\frac{2}{\\sqrt[3]{x}}$ (נבדק מספרית בכמה נקודות)."),
        num("באיזה $x$ בקטע $[-2,0)$ מתאפסת הנגזרת?", -1, "$2+\\frac{2}{\\sqrt[3]{x}}=0$ נותן $\\sqrt[3]{x}=-1$, כלומר $x=-1$."),
        num("מהו $y(-2)=-4+3\\sqrt[3]{4}$? (עשרוני)", y2, "$\\sqrt[3]{4}\\approx1.5874$, ולכן $y(-2)\\approx0.7622$."),
        ch("מהם המקסימום והמינימום המוחלטים בקטע $[-2,0]$?",
           "מקסימום $1$ (ב-$x=-1$), מינימום $0$ (ב-$x=0$)",
           ["מקסימום $1$, מינימום $-4+3\\sqrt[3]{4}\\approx0.76$ (ב-$x=-2$)",
            "מקסימום $-4+3\\sqrt[3]{4}\\approx0.76$, מינימום $0$",
            "מקסימום $1$, מינימום $-1$"],
           "הערכים בנקודות החשודות: $y(-2)\\approx0.76$, $y(-1)=1$, $y(0)=0$; הגדול הוא $1$ והקטן הוא $0$ (נבדק על רשת צפופה)."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: Taylor estimate of cbrt(9), error < 0.01 =====
yt = x**R(1, 3)
ypp = sp.diff(yt, x, 2)
assert same(ypp, -R(2, 9)*x**R(-5, 3), pts=(0.5, 2.0, 8.0, 9.0, 11.0))
assert sp.diff(yt, x).subs(x, 8) == R(1, 12)
r1max = sp.Abs(ypp.subs(x, 8))/2
assert r1max == R(1, 288) and r1max < R(1, 100)
assert abs(sp.N(sp.cbrt(9)) - (2 + sp.N(R(1, 12)))) < sp.N(r1max)

add(6, "ב",
    rubric=rub(("בחירת נקודת פיתוח $x_0=8$ שבה $\\sqrt[3]{8}=2$ ו-$x-x_0=1$", 2),
               ("נגזרות $y'(8)=\\frac{1}{12}$ ו-$y''(x)=-\\frac{2}{9\\sqrt[3]{x^5}}$", 3),
               ("הקירוב $\\sqrt[3]{9}\\approx2+\\frac{1}{12}\\approx2.0833$", 2),
               ("שארית לגרנז' $|R_1|=\\frac{1}{9\\sqrt[3]{c^5}}\\le\\frac{1}{288}<0.01$ כי $c>8$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לפתח סביב $x_0=0$ או $x_0=9$: שם הנגזרות לא מוגדרות או שהערכים לא ידועים.",
              "להעריך את השארית עם $c=9$ במקום $c>8$: החסם הגדול ביותר מתקבל כש-$c$ קרוב ל-$8$.",
              "לשכוח את החלוקה ב-$2!$ בשארית מסדר ראשון, $\\frac{y''(c)}{2!}(x-x_0)^2$."],
    steps=[
        chx("מהי הנגזרת השנייה של $y=\\sqrt[3]{x}$?", -R(2, 9)*x**R(-5, 3),
            [-R(2, 9)*x**R(-2, 3), R(2, 9)*x**R(-5, 3), -R(1, 9)*x**R(-5, 3)],
            lambda e: same(e, ypp, pts=(0.5, 2.0, 8.0, 9.0, 11.0)),
            "$y'=\\frac{1}{3}x^{-\\frac{2}{3}}$ ולכן $y''=-\\frac{2}{9}x^{-\\frac{5}{3}}$ (נבדק ב-sympy)."),
        num("מהו $y'(8)$ עבור $y=\\sqrt[3]{x}$? (עשרוני)", R(1, 12),
            "$y'(8)=\\frac{1}{3\\cdot8^{2/3}}=\\frac{1}{12}\\approx0.0833$.", tol=0.0005),
        num("מהו הקירוב $\\sqrt[3]{9}\\approx2+y'(8)\\cdot1$? (עשרוני)", 2 + R(1, 12),
            "$2+\\frac{1}{12}\\approx2.0833$."),
        num("מהו החסם $\\frac{|y''(8)|}{2!}\\cdot1^2$ על השארית? (עשרוני)", r1max,
            "כש-$c>8$ הערך $\\frac{1}{9\\sqrt[3]{c^5}}$ קטן מ-$\\frac{1}{9\\cdot32}=\\frac{1}{288}\\approx0.00347<0.01$.", tol=0.0001, nd=6),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "23S-C",
    "examLabel": "מבחן סוף סמסטר קיץ תשפ\"ג, מועד מיוחד",
    "year": 2023,
    "examDate": "05/01/2023",
    "sourceFile": "calculus-1/23S-C exam+solution.pdf",
    "solutionFile": "calculus-1/23S-C exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

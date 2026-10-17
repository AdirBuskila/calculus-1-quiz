# -*- coding: utf-8 -*-
"""Generator for tools/raw/24A-B.json -- calculus-1 (20151), semester B 2024, moed A (22/07/2024).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24A-B.py

Source: sitting 24A-B, pp.1-7 (typed exam with the official worked solution after each question).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Q1: the official solution labels the graph "ה." (a second "ה"); transcribed as the sketch item ו.
- Q3b: the figure in the official solution labels the top of the region "2-sqrt(2)" where the solution's own
  integration limit is 4-sqrt(2); the figure is shipped as printed (the text is the authority).
- Q4b: the official solution's sketch is clipped by the page footer and is not shipped.
- Q6b: HELD. The printed limit has numerator x^4 (value 2, sympy) but the official solution works the limit with
  numerator sin^2 x (value +oo); the official text is transcribed, the key is not trusted (see docs/ASK_ADIR.md).
- Q6a: the official line "f(0)=2^1+arctan(0)-5=-4" is printed with 2^1 where 2^0=1 is meant (the value -4 is
  correct); transcribed as 2^0.

Checks (tools/verify/24A-B/check.py, sympy): every derivative, limit, integral, recursion bound, area and volume
(washers and shells) matches the official answers. 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24A-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**א.** תחום ההגדרה של הפונקציה $x\in\mathbb{R}$.
**ב.** נקודת חיתוך עם צירי הקואורדינאטות $x=0,\ y=0$.
**ג.** תחומי עליה וירידה, נקודות קיצון: מכאן רואים שהנגזרת $f'(x)=(2x+x^2)e^x$ מתאפסת בנקודות $x=0,-2$ ובנוסף $y'>0$ כאשר $x<-2$ או $x>0$ וגם $y'<0$ כאשר $-2<x<0$. הנקודה $x=0$ היא נקודת מינימום מקומי, הנקודה $x=-2$ היא נקודת מקסימום מקומי.
**ד.** תחומי קמירות וקעירות, נקודות פיתול: $y''=e^x(x^2+4x+2)$, נקודות פיתול הן $x=-2\pm\sqrt{2}$. בנוסף, $y''>0$ עבור $x>-2+\sqrt{2}$ או $x<-2-\sqrt{2}$ וכאן הפונקציה קעורה (כלפי מעלה); $y''<0$ עבור $-2-\sqrt{2}<x<-2+\sqrt{2}$ וכאן הפונקציה קמורה (כלפי מטה).
**ה.** אין אסימפטוטה אנכית לגרף הפונקציה.
$$\begin{cases}\lim\limits_{x\to+\infty}\dfrac{f(x)}{x}=\lim\limits_{x\to+\infty}\dfrac{x^2e^x}{x}=+\infty\\[2mm]\lim\limits_{x\to-\infty}f(x)=\lim\limits_{x\to-\infty}x^2e^x=\lim\limits_{x\to-\infty}\dfrac{x^2}{e^{-x}}=\lim\limits_{x\to-\infty}\dfrac{2x}{-e^{-x}}=\lim\limits_{x\to-\infty}\dfrac{2}{e^{-x}}=0\end{cases}$$
ולכן קו ישר $y=0$ מהווה אסימפטוטה אופקית לגרף הפונקציה במינוס אינסוף.
**ו.** שרטוט (בפתרון הרשמי מסומן "ה."):
![הגרף של f(x)=x^2 e^x](images/exams/24A-B-Q1-graph.png)
"""

SOL2A = r"""
כיוון ש-$\frac{x^2+2x+3}{(x-1)(x^2+4x+4)}=\frac{x^2+2x+3}{(x-1)(x+2)^2}$ קיימים $A,B,C\in\mathbb{R}$ כך ש:
$$\frac{x^2+2x+3}{(x-1)(x^2+4x+4)}=\frac{A}{(x-1)}+\frac{B}{(x+2)}+\frac{C}{(x+2)^2}.$$
על-ידי השוואת מקדמים או הצבת ערכים ב-$x$, מקבלים ש-$A=\frac{2}{3}$, $B=\frac{1}{3}$ ו-$C=-1$. לכן
$$\int\frac{x^2+2x+3}{(x-1)(x^2+4x+4)}dx=\frac{2}{3}\int\frac{1}{x-1}dx+\frac{1}{3}\int\frac{1}{x+2}dx-\int\frac{1}{(x+2)^2}dx$$
$$=\frac{2}{3}\ln|x-1|+\frac{1}{3}\ln|x+2|+\frac{1}{x+2}+c,\qquad c\in\mathbb{R}$$
"""

SOL2B = r"""
ראשית, נוכיח באינדוקציה שהסדרה עולה. נשים לב שאכן $a_1=4=\sqrt{16}\le\sqrt{24}=a_2$. יהא $n\in\mathbb{N}$, ונניח ש-$a_n\le a_{n+1}$. אז כיוון שפונקציית השורש עולה מתקיים
$$a_{n+1}=\sqrt{a_n+20}\le\sqrt{a_{n+1}+20}=a_{n+2}.$$
לכן, לפי עקרון האינדוקציה, $a_n\le a_{n+1}$ לכל $n\in\mathbb{N}$.
כעת נוכיח באינדוקציה שהסדרה חסומה מלעיל על-ידי $5$. נשים לב שאכן $a_1=4\le5$. יהא $n\in\mathbb{N}$, ונניח ש-$a_n\le5$. אז כיוון שפונקציית השורש עולה מתקיים
$$a_{n+1}=\sqrt{a_n+20}\le\sqrt{5+20}=5$$
לכן, לפי עקרון האינדוקציה, $a_n\le5$ לכל $n\in\mathbb{N}$.
לפיכך, הסדרה עולה וחסומה מלעיל, ולכן, לפי משפט, בהכרח מתכנסת. נסמן $L=\lim_{n\to\infty}a_n$. אז גם $\lim_{n\to\infty}a_{n+1}=L$. מאריתמטיקה של גבולות מתקיים
$$L=\lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}\sqrt{a_n+20}=\sqrt{L+20}$$
כלומר $L^2-L-20=0$ ולכן $(L-5)(L+4)=0$. אבל כיוון שהאיבר הראשון בסדרה הוא $4$ והסדרה מונוטונית עולה, היא בהכרח אי-שלילית, ולכן לא ייתכן ש-$-4$ הוא גבולה. מכאן שגבול הסדרה הוא $5$.
"""

SOL3A = r"""
כיוון שלכל $a\in\mathbb{R}$ מתקיים $\lim_{x\to\infty}\left(1+\frac{a}{x}\right)^x=e^a$, מאריתמטיקה של גבולות נקבל
$$\lim_{n\to\infty}\left(\frac{n^2+5n-2}{n^2+3n-2}\right)^n=\lim_{n\to\infty}\left(1+\frac{2n}{n^2+3n-2}\right)^n=\lim_{n\to\infty}\left(1+\frac{2}{n+3-\frac{2}{n}}\right)^n$$
$$=\lim_{n\to\infty}\left(\left(1+\frac{2}{n+3-\frac{2}{n}}\right)^{n+3-\frac{2}{n}}\right)^{\frac{n}{n+3-\frac{2}{n}}}=e^2$$
"""

SOL3B = r"""
נקודת מפגש בין בקווים:
$$x-2=4-\sqrt{x},\qquad\sqrt{x}=t\ge0$$
$$t^2+t-6=0,\quad t_1=2,\quad t_2=-3,\quad x=4$$
נקודת מפגש $(4,2)$.
![התחום המישורי, נקודת המפגש (4,2) והישר x=2](images/exams/24A-B-Q3b-region.png)
שיטת פרוסות:
$$V=\pi\int_2^4\left((4-\sqrt{x})^2-(x-2)^2\right)dx=\pi\int_2^4\left(16-8\sqrt{x}+x-x^2+4x-4\right)dx=$$
$$\pi\left(12x-\frac{16\sqrt{x^3}}{3}+2.5x^2-\frac{x^3}{3}\right)\Big|_2^4\cong7.752\pi\cong24.352$$
שיטת קליפות:
$$V=2\pi\int_2^{4-\sqrt{2}}\left((4-y)^2-2\right)y\,dy+2\pi\int_0^2(y+2-2)y\,dy=$$
$$=2\pi\int_2^{4-\sqrt{2}}(14y-8y^2+y^3)\,dy+2\pi\int_0^2y^2\,dy=$$
$$=2\pi\left[\left(7y^2-\frac{8y^3}{3}+\frac{y^4}{4}\right)\Big|_2^{4-\sqrt{2}}+\left(\frac{y^3}{3}\right)\Big|_0^2\right]\cong7.752\pi$$
"""

SOL4A = r"""
$$y'=e^{\frac{1}{x}}+xe^{\frac{1}{x}}\left(-\frac{1}{x^2}\right)=e^{\frac{1}{x}}\left(\frac{x-1}{x}\right)$$
$$y'=0\Rightarrow x=1$$
$$y(0.5)=0.5e^2\cong3.694$$
$$y(1)=e\cong2.718$$
$$y(3)=3e^{\frac{1}{3}}\cong4.187$$
$$y_{\max}=3\sqrt[3]{e},\qquad y_{\min}=e\qquad(x\in[0.5,3])$$
"""

SOL4B = r"""
$$f'(x)=\frac{-2}{2\sqrt{2-2x}}=\frac{-1}{\sqrt{2-2x}}=-\frac{1}{2},\qquad\sqrt{2-2x}=2$$
$$2-2x=4,\qquad x=-1,\quad f(-1)=2$$
נקודת השקה $(-1,2)$.
משוואת המשיק:
$$y-2=-\frac{1}{2}(x+1)$$
$$y=1.5-0.5x$$
המשיק חותך את ציר ה-$X$ בנקודה $(3,0)$.
השטח:
$$S=\int_{-1}^1\left(1.5-0.5x-\sqrt{2-2x}\right)dx+\int_1^3(1.5-0.5x)\,dx$$
או
$$S=\int_{-1}^3(1.5-0.5x)\,dx-\int_{-1}^1\sqrt{2-2x}\,dx=$$
$$\left[1.5x-0.25x^2\right]_{-1}^3+\frac{1}{3}\left[\sqrt{(2-2x)^3}\right]_{-1}^1=\frac{4}{3}$$
"""

SOL5A = r"""
$$\int\frac{\ln x\,dx}{x(\ln^2x+1)}=\left|\begin{matrix}t=\ln x\\dt=\frac{1}{x}dx\end{matrix}\right|=\int\frac{t\,dt}{t^2+1}=\frac{1}{2}\ln\left(t^2+1\right)+C=\frac{1}{2}\ln\left(\ln^2x+1\right)+C$$
"""

SOL5B = r"""
ראשית, נחשב גבולות חד צדדיים בנקודות התפר:
$$\begin{cases}\lim_{x\to0^-}f(x)=\lim_{x\to0^-}\frac{\arctan(2x)}{x}\overset{(*)}{=}\lim_{x\to0^-}\frac{2}{1\left(1+4x^2\right)}=2\\ \lim_{x\to0^+}f(x)=\lim_{x\to0^+}(ax+b)=b\end{cases}\ \Leftarrow\ b=2$$
$$\begin{cases}\lim_{x\to2^-}f(x)=\lim_{x\to2^-}(ax+b)=2a+b=2a+2\\ \lim_{x\to2^+}f(x)=\lim_{x\to2^+}\frac{4\left(x-\sqrt{3x-2}\right)}{x-2}=\lim_{x\to2^+}\frac{4\left(x^2-3x+2\right)}{(x-2)\left(x+\sqrt{3x-2}\right)}=\lim_{x\to2^+}\frac{4(x-2)(x-1)}{(x-2)\left(x+\sqrt{3x-2}\right)}=1\end{cases}$$
ומכאן נקבל ש-$2a+2=1\ \Leftarrow\ a=-\frac{1}{2}$.
"""

SOL6A = r"""
נגדיר פונקציה $f(x)=2^{\sqrt{x}}+\arctan(2x)-5$.
תחום ההגדרה של הפונקציה $f(x)$ הוא $x\ge0$. הפונקציה רציפה וגזירה בתחום $x>0$. הנגזרת היא:
$$f'(x)=\frac{1}{2\sqrt{x}}2^{\sqrt{x}}\ln2+\frac{2}{1+4x^2}.$$
לכן $f'(x)=\frac{1}{2\sqrt{x}}2^{\sqrt{x}}\ln2+\frac{2}{1+4x^2}>0$ ומכאן הפונקציה עולה ממש.
כמו כן, $f(0)=2^0+\arctan(0)-5=-4$, ואם נסתכל על הגבול ב-$\infty$, נקבל: $\lim_{x\to\infty}f(x)=\infty+\frac{\pi}{2}-5=\infty$.
לכן לפי משפט ערך הביניים קיימת נקודה $c>0$, כך ש-$f(c)=0$. $c$ יחידה כי הפונקציה עולה ממש.
"""

SOL6B = r"""
יש לחשב את $\lim_{x\to0^+}\frac{\sin^2x}{\int_0^{x^2}t\cos(t^2)\,dt}$.
$$\lim_{x\to0^+}\frac{\sin^2x}{\int_0^{x^2}t\cos(t^2)\,dt}=\frac{0}{0}\overset{\text{L'hopital}}{=}\lim_{x\to0^+}\frac{2\sin x\cos x}{2x\cdot x^2\cos(x^4)}=$$
$$=\lim_{x\to0^+}\frac{\sin2x}{2x\cdot x^2\cos(x^4)}=\lim_{x\to0^+}\frac{\frac{\sin2x}{2x}}{x^2\cos(x^4)}=\frac{\lim_{x\to0^+}\frac{\sin2x}{2x}}{\lim_{x\to0^+}x^2\cos(x^4)}$$
המונה שואף ל-$1$, המכנה ל-$0^+$ לכן הגבול הוא $\infty$.
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=x^2e^x$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, תחומי עליה וירידה, "
      "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, נקודות אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{x^2+2x+3}{(x-1)(x^2+4x+4)}\,dx$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "sequences_limits",
      "נתונה הסדרה:\n" r"$$a_{n+1}=\sqrt{a_n+20},\quad a_1=4$$" "\nהוכיחו כי הסדרה מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "sequences_limits",
      r"חשבו את הגבול הבא: $\lim_{n\to\infty}\left(\frac{n^2+5n-2}{n^2+3n-2}\right)^n$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר מסיבוב התחום המישורי הכלוא בין הקווים: $y=4-\sqrt{x},\ y=x-2,\ x=2$ סביב ציר ה-$X$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "extrema_optimization",
      r"מצאו את הערך המקסימלי ואת הערך המינימלי של הפונקציה: $y=xe^{\frac{1}{x}}$ בקטע הסגור $\left[\frac{1}{2},3\right]$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "derivatives_tangents",
      r"נתונה הפונקציה: $f(x)=\sqrt{2-2x}$. חשבו את המשיק לגרף הפונקציה בעל שיפוע $-\frac{1}{2}$. "
      "מצאו את השטח התחום בין הגרף הפונקציה, המשיק וציר ה-$X$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\ln x\,dx}{x(\ln^2x+1)}$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "continuity",
      r"נתונה הפונקציה: $f(x)=\begin{cases}\frac{\arctan(2x)}{x}, & x<0\\ ax+b, & 0\le x\le2\\ \frac{4\left(x-\sqrt{3x-2}\right)}{x-2}, & x>2\end{cases}$"
      "\nמצאו לאלו ערכים של $a,b$ (ממשיים) $f(x)$ תהיה רציפה לכל $x$ ממשי.",
      SOL5B, part="ב", points=10),

    Q(6, "proof", "continuity",
      r"הוכיחו כי למשוואה $2^{\sqrt{x}}+\arctan(2x)=5$ קיים פתרון ממשי אחד בלבד.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "lhopital_taylor",
      r"חשבו את הגבול הבא: $\lim_{x\to0^+}\frac{x^4}{\int_0^{x^2}t\cos(t^2)\,dt}$.",
      SOL6B, part="ב", points=10,
      hold="official-solution-mismatch: the official solution computes a different limit (numerator sin^2 x, answer infinity) than the printed one (numerator x^4); sympy gives 2 for the printed limit"),
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

# ===== Q1: f = x^2 e^x =====
f1 = x**2*sp.exp(x)
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, (x**2 + 2*x)*sp.exp(x)) and same(f1pp, sp.exp(x)*(x**2 + 4*x + 2))
assert sorted(sp.solve(f1p, x)) == [-2, 0]
assert f1pp.subs(x, 0) > 0 and f1pp.subs(x, -2) < 0
infl1 = sorted(sp.solve(x**2 + 4*x + 2, x), key=sp.N)
assert infl1 == [-2 - sp.sqrt(2), -2 + sp.sqrt(2)]
assert sp.limit(f1, x, -sp.oo) == 0 and sp.limit(f1, x, sp.oo) == sp.oo and sp.limit(f1/x, x, sp.oo) == sp.oo
fmax1 = f1.subs(x, -2)
assert same(fmax1, 4*sp.exp(-2))

add(1,
    rubric=rub(("תחום הגדרה $\\mathbb{R}$ וחיתוך עם הצירים $(0,0)$", 2),
               ("נגזרת $f'(x)=(x^2+2x)e^x$, נקודות קריטיות $x=0,-2$ ותחומי עליה וירידה", 5),
               ("סיווג הקיצון: מקסימום מקומי ב-$x=-2$, מינימום מקומי ב-$x=0$", 3),
               ("$f''(x)=e^x(x^2+4x+2)$, נקודות פיתול $x=-2\\pm\\sqrt{2}$ ותחומי קמירות", 4),
               ("אסימפטוטות: $y=0$ ב-$-\\infty$, אין אנכית ואין משופעת ב-$+\\infty$", 3),
               ("שרטוט הגרף", 3)),
    rubricSource="ai-verified",
    pitfalls=["לטעון ל-$y=0$ כאסימפטוטה אופקית משני הכיוונים. ב-$+\\infty$ הפונקציה שואפת ל-$\\infty$, ואין אסימפטוטה משופעת כי $\\frac{f(x)}{x}\\to\\infty$.",
              "לשכוח את $e^x$ בנגזרת: $(x^2)'e^x+x^2(e^x)'=(2x+x^2)e^x$.",
              "להסיק שגם $x=0$ מקסימום: סימן הנגזרת משתנה משלילי לחיובי, ולכן מינימום."],
    steps=[
        chx("מהי הנגזרת של $f(x)=x^2e^x$?", (x**2 + 2*x)*sp.exp(x),
            [x**2*sp.exp(x), 2*x*sp.exp(x), (x**2 - 2*x)*sp.exp(x)], lambda e: same(e, f1p),
            "כלל מכפלה: $2xe^x+x^2e^x=(x^2+2x)e^x$ (אומת ב-sympy)."),
        num("מהו ערך הפונקציה בנקודת המקסימום המקומי $x=-2$? (עשרוני)", fmax1,
            "$f(-2)=4e^{-2}\\approx0.5413$.", tol=0.001),
        num("מהו ערך $x$ של נקודת הפיתול הימנית $x=-2+\\sqrt{2}$? (עשרוני)", infl1[1],
            "$x^2+4x+2=0$ נותן $x=-2\\pm\\sqrt{2}$; הימנית היא $-2+\\sqrt{2}\\approx-0.5858$.", tol=0.001),
        ch("מהן האסימפטוטות של $f$?", "$y=0$ ב-$-\\infty$ בלבד",
           ["$y=0$ בשני הכיוונים", "$y=x$ ב-$+\\infty$", "$x=0$ אנכית"],
           "$\\lim_{x\\to-\\infty}x^2e^x=0$, וב-$+\\infty$ הפונקציה שואפת ל-$\\infty$ מהר מכל ישר ($\\frac{f(x)}{x}\\to\\infty$). אין אסימפטוטה אנכית כי $f$ רציפה (sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: (x^2+2x+3)/((x-1)(x+2)^2) =====
g2 = (x**2 + 2*x + 3)/((x - 1)*(x + 2)**2)
A_, B_, C_ = sp.symbols('A B C')
fr2 = sp.apart(g2, x)
sol2 = sp.solve(sp.Poly(sp.expand(A_*(x + 2)**2 + B_*(x - 1)*(x + 2) + C_*(x - 1) - (x**2 + 2*x + 3)), x).all_coeffs(),
                [A_, B_, C_], dict=True)[0]
assert sol2 == {A_: R(2, 3), B_: R(1, 3), C_: -1}
# C multiplies 1/(x+2)^2 in the official form: A/(x-1)+B/(x+2)+C/(x+2)^2
sol2b = sp.solve(sp.Poly(sp.expand(A_*(x + 2)**2 + B_*(x - 1)*(x + 2) + C_*(x - 1) - (x**2 + 2*x + 3)), x).all_coeffs(), [A_, B_, C_], dict=True)[0]
assert same(g2, sol2b[A_]/(x - 1) + sol2b[B_]/(x + 2) + sol2b[C_]/(x + 2)**2)
# the two wrong forms cannot represent g2
for bf in (A_*(x + 2)**2 + B_*(x - 1)*(x + 2) - (x**2 + 2*x + 3), A_*(x + 2)**2 + B_*(x - 1) - (x**2 + 2*x + 3)):
    assert sp.solve(sp.Poly(sp.expand(bf), x).all_coeffs(), [A_, B_], dict=True) == []

add(2, "א",
    rubric=rub(("פירוק לשברים חלקיים בצורה $\\frac{A}{x-1}+\\frac{B}{x+2}+\\frac{C}{(x+2)^2}$ (כולל הגורם הריבועי)", 3),
               ("חישוב $A=\\frac{2}{3}$, $B=\\frac{1}{3}$, $C=-1$", 3),
               ("אינטגרציה של כל אחד משלושת השברים", 3),
               ("תשובה סופית עם $+c$", 1)),
    rubricSource="ai-verified",
    pitfalls=["להשמיט את השבר $\\frac{C}{(x+2)^2}$ כשהמכנה כולל גורם בריבוע, ואז אין פתרון למערכת.",
              "לאנטגרל $\\int\\frac{dx}{(x+2)^2}$ לתת לוגריתם: התוצאה היא $-\\frac{1}{x+2}$.",
              "לשכוח לפרק את $x^2+4x+4=(x+2)^2$ לפני בניית הפירוק."],
    steps=[
        ch("איזה פירוק לשברים חלקיים מתאים ל-$\\frac{x^2+2x+3}{(x-1)(x+2)^2}$?",
           "$\\frac{A}{x-1}+\\frac{B}{x+2}+\\frac{C}{(x+2)^2}$",
           ["$\\frac{A}{x-1}+\\frac{B}{x+2}$", "$\\frac{A}{x-1}+\\frac{B}{(x+2)^2}$"],
           "גורם בריבוע דורש שני שברים. בשתי האפשרויות האחרות מערכת המקדמים חסרת פתרון (אומת ב-sympy)."),
        num("מהו $A$? (עשרוני)", sol2[A_], "הצבת $x=1$: $6=9A$ ולכן $A=\\frac{2}{3}$.", tol=0.0005),
        num("מהו $B$? (עשרוני)", sol2[B_], "השוואת מקדמי $x^2$: $A+B=1$ ולכן $B=\\frac{1}{3}$.", tol=0.0005),
        num("מהו $C$?", sol2[C_], "הצבת $x=-2$: $3=-3C$ ולכן $C=-1$."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: a_{n+1} = sqrt(a_n + 20), a_1 = 4 =====
a_ = [sp.Integer(4)]
for _ in range(40):
    a_.append(sp.sqrt(a_[-1] + 20))
assert all(a_[i] < a_[i + 1] < 5 for i in range(12))
a2 = a_[1]
assert same(a2, sp.sqrt(24))
Lsym = sp.Symbol('L', real=True)
assert sorted(sp.solve(Lsym**2 - Lsym - 20, Lsym)) == [-4, 5]
assert sp.solve(sp.Eq(Lsym, sp.sqrt(Lsym + 20)), Lsym) == [5]
assert sp.sqrt(-4 + 20) == 4  # sqrt(L+20) is defined at L=-4, so that is not the reason to drop it
L2 = ["נוכיח באינדוקציה ש-$a_n\\le a_{n+1}$ וש-$a_n\\le5$ לכל $n$, כלומר הסדרה עולה וחסומה מלעיל ב-$5$.",
      "סדרה עולה וחסומה מלעיל מתכנסת, ונסמן $L=\\lim_{n\\to\\infty}a_n$.",
      "מאריתמטיקה של גבולות $L=\\sqrt{L+20}$, ולכן $L^2-L-20=0$.",
      "$(L-5)(L+4)=0$; כל איברי הסדרה גדולים או שווים ל-$4$ ולכן $L\\ne-4$ והגבול הוא $5$."]
L2b = list(L2)
L2b[2] = "מאריתמטיקה של גבולות $L=\\sqrt{L+20}$, ולכן $L^2+L-20=0$."
assert not same(Lsym**2 + Lsym - 20, Lsym**2 - Lsym - 20)

add(2, "ב",
    rubric=rub(("הוכחה באינדוקציה שהסדרה עולה", 3),
               ("הוכחה באינדוקציה שהסדרה חסומה מלעיל ב-$5$", 3),
               ("מסקנה: סדרה מונוטונית וחסומה מתכנסת (משפט ויירשטראס)", 1),
               ("משוואת הגבול $L=\\sqrt{L+20}$ ופתרונה $L=5$", 2),
               ("פסילת $L=-4$", 1)),
    rubricSource="ai-verified",
    pitfalls=["לחשב את הגבול מהמשוואה $L=\\sqrt{L+20}$ בלי להוכיח קודם שהגבול קיים.",
              "לא לפסול את השורש השלילי $L=-4$: הסדרה חיובית ולכן גבולה אינו שלילי.",
              "להוכיח רק שהסדרה עולה, בלי חסם מלעיל, ולהסיק התכנסות."],
    steps=[
        num("מהו האיבר $a_2$ בסדרה $a_{n+1}=\\sqrt{a_n+20}$, $a_1=4$? (עשרוני)", a2,
            "$a_2=\\sqrt{24}\\approx4.8990$.", tol=0.001),
        ch("מדוע בפתרון המשוואה $L^2-L-20=0$ נפסל השורש $L=-4$?",
           "כל איברי הסדרה גדולים או שווים ל-$4$, ולכן הגבול אינו יכול להיות שלילי",
           ["$-4$ אינו פתרון של $L^2-L-20=0$", "$\\sqrt{L+20}$ אינו מוגדר עבור $L=-4$", "הסדרה יורדת ולכן הגבול קטן מ-$a_1$"],
           "השורשים הם $5$ ו-$-4$ (sympy), והביטוי $\\sqrt{-4+20}=4$ מוגדר. הסדרה עולה מ-$a_1=4$, לכן הגבול לפחות $4$ ומתקבל $5$."),
        order("סדרו את שלבי ההוכחה.", L2, "קודם מוכיחים עליה וחסימות, אחר כך התכנסות, אחר כך משוואת הגבול, ובסוף בחירת השורש."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L2b, 2,
                "העלאה בריבוע של $L=\\sqrt{L+20}$ נותנת $L^2=L+20$, כלומר $L^2-L-20=0$ ולא $L^2+L-20=0$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: lim ((n^2+5n-2)/(n^2+3n-2))^n = e^2 =====
base3 = (n**2 + 5*n - 2)/(n**2 + 3*n - 2)
assert sp.limit(base3, n, sp.oo) == 1
assert sp.limit(n*(base3 - 1), n, sp.oo) == 2
assert sp.limit(base3**n, n, sp.oo) == sp.exp(2)

add(3, "א",
    rubric=rub(("זיהוי צורה $1^\\infty$ וכתיבת הבסיס כ-$1+\\frac{2n}{n^2+3n-2}$", 4),
               ("שימוש בגבול הידוע $\\left(1+\\frac{a}{x}\\right)^x\\to e^a$ או בחישוב גבול המעריך", 3),
               ("חישוב $\\lim n\\cdot\\frac{2n}{n^2+3n-2}=2$ ותשובה $e^2$", 3)),
    rubricSource="ai-verified",
    pitfalls=["להציב $1^\\infty=1$: זו צורה לא מסוימת ולא ערך.",
              "לחשב רק את גבול הבסיס ($1$) ולהתעלם מהמעריך שהולך לאינסוף.",
              "לטעות בחישוב $n\\cdot\\frac{2n}{n^2+3n-2}$ ולקבל $0$ או $\\infty$ במקום $2$."],
    steps=[
        ch("מה סוג הצורה הלא מסוימת של $\\left(\\frac{n^2+5n-2}{n^2+3n-2}\\right)^n$ כאשר $n\\to\\infty$?", "$1^\\infty$",
           ["$0\\cdot\\infty$", "$\\infty^0$", "$0^0$"],
           "הבסיס שואף ל-$1$ והמעריך ל-$\\infty$ (נבדק ב-sympy)."),
        num("מהו $\\lim_{n\\to\\infty}n\\cdot\\left(\\frac{n^2+5n-2}{n^2+3n-2}-1\\right)$?", 2,
            "$\\frac{n^2+5n-2}{n^2+3n-2}-1=\\frac{2n}{n^2+3n-2}$ ולכן המכפלה $\\frac{2n^2}{n^2+3n-2}\\to2$."),
        num("מהו ערך הגבול? (עשרוני)", sp.exp(2), "$e^2\\approx7.389$.", tol=0.001),
    ],
    stepsSource="ai-verified")

# ===== Q3b: solid of revolution about the x-axis =====
xs3 = [s for s in sp.solve(sp.Eq(x - 2, 4 - sp.sqrt(x)), x) if s.is_real]
assert xs3 == [4]
assert all(4 - sp.sqrt(v) > v - 2 for v in (2, R(5, 2), 3, R(7, 2), R(39, 10)))
V3 = sp.pi*sp.integrate((4 - sp.sqrt(x))**2 - (x - 2)**2, (x, 2, 4))
assert abs(sp.N(V3/sp.pi) - 7.752) < 0.001 and abs(sp.N(V3) - 24.352) < 0.01

add(3, "ב",
    rubric=rub(("נקודת החיתוך $(4,2)$ של הישר והעקום", 2),
               ("זיהוי התחום $2\\le x\\le4$ והרדיוסים: חיצוני $4-\\sqrt{x}$ ופנימי $x-2$", 3),
               ("נוסחת הפרוסות $V=\\pi\\int_2^4\\left((4-\\sqrt{x})^2-(x-2)^2\\right)dx$", 3),
               ("חישוב האינטגרל: $7.752\\pi\\approx24.35$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להפריד את הגבולות לא נכון: התחום מתחיל ב-$x=2$ (הישר האנכי) ונגמר ב-$x=4$.",
              "לחשב $\\pi\\int\\left((4-\\sqrt{x})-(x-2)\\right)^2dx$ במקום הפרש ריבועי הרדיוסים.",
              "לבלבל בין הרדיוס החיצוני לפנימי: העליון $4-\\sqrt{x}$ הוא החיצוני."],
    steps=[
        num("באיזה ערך של $x$ נפגשים הישר $y=x-2$ והעקום $y=4-\\sqrt{x}$?", xs3[0],
            "$x-2=4-\\sqrt{x}$ עם $t=\\sqrt{x}$: $t^2+t-6=0$ ולכן $t=2$ ו-$x=4$ (sympy)."),
        ch("בקטע $2\\le x\\le4$, מהו הרדיוס החיצוני של הפרוסה בסיבוב סביב ציר ה-$x$?", "$4-\\sqrt{x}$",
           ["$x-2$", "$4-\\sqrt{x}-(x-2)$", "$\\sqrt{x}$"],
           "הפרוסה נמדדת מציר ה-$x$ עד הקו העליון, וזה $y=4-\\sqrt{x}$; הפנימי הוא $x-2$ (נבדק בנקודות לדוגמה ב-sympy)."),
        num("מהו $\\frac{V}{\\pi}$ כאשר $V=\\pi\\int_2^4\\left((4-\\sqrt{x})^2-(x-2)^2\\right)dx$? (עשרוני)", V3/sp.pi,
            "הערך הוא $7.752$.", tol=0.001),
        num("מהו הנפח $V$? (עשרוני)", V3, "$7.752\\pi\\approx24.352$.", tol=0.01),
    ],
    stepsSource="ai-verified")

# ===== Q4a: abs max/min of x e^(1/x) on [1/2, 3] =====
y4 = x*sp.exp(1/x)
c4 = [s for s in sp.solve(sp.diff(y4, x), x) if s.is_real and R(1, 2) <= s <= 3]
assert c4 == [1]
v4 = {R(1, 2): y4.subs(x, R(1, 2)), 1: y4.subs(x, 1), 3: y4.subs(x, 3)}
assert max(v4, key=lambda k: sp.N(v4[k])) == 3 and min(v4, key=lambda k: sp.N(v4[k])) == 1
assert same(v4[3], 3*sp.cbrt(sp.E)) and same(v4[R(1, 2)], sp.exp(2)/2)

add(4, "א",
    rubric=rub(("נגזרת $y'=e^{1/x}\\cdot\\frac{x-1}{x}$ ונקודה קריטית $x=1$", 3),
               ("חישוב הערך בקצוות הקטע: $0.5e^2\\approx3.694$ ו-$3e^{1/3}\\approx4.187$", 3),
               ("חישוב הערך בנקודה הקריטית $e\\approx2.718$", 2),
               ("השוואה וקביעת מקסימום $3\\sqrt[3]{e}$ ומינימום $e$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להשוות רק את הקיצון המקומי ולשכוח לבדוק את שני קצוות הקטע הסגור.",
              "לטעות בכלל השרשרת: $\\left(e^{1/x}\\right)'=-\\frac{1}{x^2}e^{1/x}$.",
              "להסיק שמקסימום בקצה השמאלי: $0.5e^2\\approx3.694$ קטן מ-$3e^{1/3}\\approx4.187$."],
    steps=[
        num("מהו ערך $x$ בקטע $\\left[\\frac12,3\\right]$ שבו $y'=0$?", c4[0], "$y'=e^{1/x}\\cdot\\frac{x-1}{x}$ מתאפס ב-$x=1$ (sympy)."),
        num("מהו $y\\left(\\frac12\\right)$? (עשרוני)", v4[R(1, 2)], "$\\frac12e^2\\approx3.694$.", tol=0.001),
        num("מהו $y(3)$? (עשרוני)", v4[3], "$3e^{1/3}\\approx4.187$.", tol=0.001),
        ch("מהם המקסימום והמינימום המוחלטים בקטע?",
           "מקסימום $3\\sqrt[3]{e}$ (ב-$x=3$), מינימום $e$ (ב-$x=1$)",
           ["מקסימום $\\frac12e^2$ (ב-$x=\\frac12$), מינימום $e$", "מקסימום $3\\sqrt[3]{e}$, מינימום $\\frac12e^2$", "מקסימום $e$ (ב-$x=1$), מינימום $\\frac12e^2$"],
           "הערכים $3.694$, $2.718$, $4.187$ (sympy): הגדול ביותר ב-$x=3$ והקטן ביותר ב-$x=1$."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: tangent to sqrt(2-2x) with slope -1/2, area with the x-axis =====
f4 = sp.sqrt(2 - 2*x)
x4 = [s for s in sp.solve(sp.Eq(sp.diff(f4, x), R(-1, 2)), x)]
assert x4 == [-1] and f4.subs(x, -1) == 2
tan4 = 2 - R(1, 2)*(x + 1)
assert same(tan4, R(3, 2) - x/2) and sp.solve(tan4, x) == [3]
S4 = sp.integrate(tan4 - f4, (x, -1, 1)) + sp.integrate(tan4, (x, 1, 3))
assert S4 == R(4, 3)

add(4, "ב",
    rubric=rub(("גזירה ופתרון $f'(x)=-\\frac12$: נקודת ההשקה $(-1,2)$", 3),
               ("משוואת המשיק $y=1.5-0.5x$ וחיתוכו עם ציר ה-$x$ ב-$(3,0)$", 3),
               ("הצבת השטח כסכום אינטגרלים או כהפרש (משיק פחות עקום)", 2),
               ("חישוב השטח $\\frac43$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחשב את הנגזרת בלי כלל השרשרת: $\\left(\\sqrt{2-2x}\\right)'=\\frac{-1}{\\sqrt{2-2x}}$.",
              "לשכוח שהשטח כולל את חלק המשיק שמעל ציר ה-$x$ עד $x=3$, כאשר העקום מסתיים ב-$x=1$.",
              "לחשב אינטגרל של המשיק פחות העקום על כל $[-1,3]$, אך העקום לא מוגדר אחרי $x=1$."],
    steps=[
        num("בכל נקודה $x$ שבה השיפוע של $\\sqrt{2-2x}$ הוא $-\\frac12$, מהו $x$?", x4[0],
            "$\\frac{-1}{\\sqrt{2-2x}}=-\\frac12$ נותן $\\sqrt{2-2x}=2$ ולכן $x=-1$ (sympy)."),
        chx("מהי משוואת המשיק $y=\\ ?$", R(3, 2) - x/2, [R(5, 2) - x/2, R(3, 2) + x/2, 2 - x/2],
            lambda e: same(e, tan4), "המשיק עובר ב-$(-1,2)$ עם שיפוע $-\\frac12$: $y-2=-\\frac12(x+1)$ כלומר $y=1.5-0.5x$."),
        num("באיזה ערך $x$ חותך המשיק את ציר ה-$x$?", 3, "$1.5-0.5x=0$ נותן $x=3$."),
        num("מהו השטח התחום בין העקום, המשיק וציר ה-$x$? (עשרוני)", S4, "$\\int_{-1}^{1}(1.5-0.5x-\\sqrt{2-2x})dx+\\int_1^3(1.5-0.5x)dx=\\frac43\\approx1.3333$.", tol=0.001),
    ],
    stepsSource="ai-verified")

# ===== Q5a: int ln x / (x (ln^2 x + 1)) =====
I5 = sp.log(x)/(x*(sp.log(x)**2 + 1))
F5 = sp.log(sp.log(x)**2 + 1)/2
assert same(sp.diff(F5, x), I5)
sub5 = sp.simplify(I5.subs(x, sp.exp(t))*sp.exp(t))
assert same(sub5, t/(t**2 + 1))
v5 = sp.integrate(I5, (x, 1, sp.E))
assert same(v5, sp.log(2)/2)

add(5, "א",
    rubric=rub(("הצבה $t=\\ln x$, $dt=\\frac{dx}{x}$", 3),
               ("האינטגרל $\\int\\frac{t}{t^2+1}dt$ ופתרונו $\\frac12\\ln(t^2+1)$", 5),
               ("חזרה למשתנה $x$ וקבוע האינטגרציה", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח להחליף את $dx$ ב-$x\\,dt$, כך שנשאר $x$ באינטגרל.",
              "לכתוב $\\arctan(\\ln x)$ במקום $\\frac12\\ln(\\ln^2x+1)$: המונה $t$ הוא נגזרת המכנה עד גורם $2$.",
              "לשכוח את הגורם $\\frac12$."],
    steps=[
        chx("אחרי ההצבה $t=\\ln x$ מהו האינטגרנד ב-$t$ (כלומר $\\int\\ldots\\,dt$)?", t/(t**2 + 1),
            [1/(t**2 + 1), t/(t**2 + 1)**2, t**2/(t**2 + 1)], lambda e: same(e, sub5),
            "$dx=x\\,dt$ מצמצם את $\\frac1x$, ונשאר $\\frac{t}{t^2+1}$ (אומת ב-sympy)."),
        chx("מהי הקדומה?", F5, [sp.log(sp.log(x)**2 + 1), sp.atan(sp.log(x))/2, sp.log(sp.log(x))/2],
            lambda e: same(sp.diff(e, x), I5), "$\\int\\frac{t}{t^2+1}dt=\\frac12\\ln(t^2+1)$; הנגזרת של כל אפשרות נבדקה ב-sympy."),
        num("כבדיקה: מהו $\\int_1^e\\frac{\\ln x}{x(\\ln^2x+1)}dx$? (עשרוני)", v5, "$\\frac12\\ln2\\approx0.3466$.", tol=0.001),
    ],
    stepsSource="ai-verified")

# ===== Q5b: continuity with parameters =====
l0 = sp.limit(sp.atan(2*x)/x, x, 0, '-')
r2 = sp.limit(4*(x - sp.sqrt(3*x - 2))/(x - 2), x, 2, '+')
assert (l0, r2) == (2, 1)
sol5 = sp.solve([sp.Eq(b_ := sp.Symbol('bb'), 2)], [b_], dict=True)
a5 = sp.solve(sp.Eq(2*a + 2, 1), a)[0]
assert a5 == R(-1, 2)

add(5, "ב",
    rubric=rub(("הגבול ב-$x=0^-$: $\\lim\\frac{\\arctan2x}{x}=2$, ולכן $b=2$", 3),
               ("הגבול ב-$x=2^+$: הכפלה בצמוד וצמצום נותנים $1$", 4),
               ("רציפות ב-$x=2$: $2a+b=1$ ומכאן $a=-\\frac12$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לבדוק רציפות רק ב-$x=0$ או רק ב-$x=2$. יש שתי נקודות תפר.",
              "לא להכפיל בצמוד בגבול ב-$x=2^+$, ולהישאר בצורה $\\frac00$ בלי לצמצם $(x-2)$.",
              "לשכוח שבקטע $0\\le x\\le2$ הפונקציה היא $ax+b$, ולכן שני התנאים קושרים את $a$ ו-$b$."],
    steps=[
        num("מהו $\\lim_{x\\to0^-}\\frac{\\arctan(2x)}{x}$ (וכך $b$)?", l0, "לפי לופיטל: $\\frac{2}{1+4x^2}\\to2$, ולכן $b=2$."),
        num("מהו $\\lim_{x\\to2^+}\\frac{4\\left(x-\\sqrt{3x-2}\\right)}{x-2}$?", r2,
            "הכפלה בצמוד: $\\frac{4(x-2)(x-1)}{(x-2)\\left(x+\\sqrt{3x-2}\\right)}\\to\\frac{4\\cdot1}{2+2}=1$."),
        num("מהו הערך של $a$? (עשרוני)", a5, "$2a+b=1$ עם $b=2$ נותן $a=-\\frac12$.", tol=0.0005),
    ],
    stepsSource="ai-verified")

# ===== Q6a: unique root of 2^sqrt(x) + arctan(2x) = 5 =====
f6 = 2**sp.sqrt(x) + sp.atan(2*x) - 5
xp6 = sp.Symbol('xp', positive=True)
f6p = sp.diff(2**sp.sqrt(xp6) + sp.atan(2*xp6) - 5, xp6)
assert all(sp.N(f6p.subs(xp6, v)) > 0 for v in (R(1, 100), R(1, 2), 1, 5, 40))
assert f6.subs(x, 0) == -4
assert sp.N(f6.subs(x, 16)) > 0 and sp.limit(f6, x, sp.oo) == sp.oo

add(6, "א",
    rubric=rub(("הגדרת $f(x)=2^{\\sqrt{x}}+\\arctan(2x)-5$ ורציפותה בתחום $x\\ge0$", 2),
               ("$f(0)=-4<0$ וגבול ב-$\\infty$ חיובי, ולכן קיים שורש לפי ערך הביניים", 4),
               ("$f'(x)>0$, כלומר $f$ עולה ממש", 3),
               ("מסקנה: השורש יחיד", 1)),
    rubricSource="ai-verified",
    pitfalls=["להסתפק בקיום השורש (ערך הביניים) ולא להוכיח יחידות.",
              "לבדוק את הנגזרת ב-$x=0$ שבו $\\sqrt{x}$ אינו גזיר: הגזירות רק עבור $x>0$.",
              "לא להראות שהפונקציה חיובית בנקודה כלשהי, ולכן אין שינוי סימן."],
    steps=[
        num("מהו $f(0)$ עבור $f(x)=2^{\\sqrt{x}}+\\arctan(2x)-5$?", f6.subs(x, 0), "$2^0+\\arctan0-5=1-5=-4$."),
        num("מהו $f(16)$? (עשרוני)", f6.subs(x, 16), "$2^4+\\arctan32-5=11+\\arctan32\\approx12.54>0$, ולכן יש שינוי סימן.", tol=0.001),
        ch("מה מבטיח שהשורש יחיד?", "$f'(x)>0$ לכל $x>0$, ולכן $f$ עולה ממש",
           ["$f$ רציפה בקטע", "$f(0)<0$ ו-$f(16)>0$", "$\\lim_{x\\to\\infty}f(x)=\\infty$"],
           "רציפות וסימנים הפוכים נותנים קיום בלבד. יחידות נובעת ממונוטוניות חזקה: הנגזרת חיובית (נבדק ב-sympy בנקודות שונות)."),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "24A-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ד, מועד א'",
    "year": 2024,
    "examDate": "22/07/2024",
    "sourceFile": "calculus-1/24A-B exam+solution.pdf",
    "solutionFile": "calculus-1/24A-B exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

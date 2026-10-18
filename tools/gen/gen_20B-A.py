# -*- coding: utf-8 -*-
"""Generator for tools/raw/20B-A.json -- calculus-1 (20151), semester A 2020, moed B (01/05/2020).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_20B-A.py

Source: sitting 20B-A, pp.1-5 (typed "פתרון המבחן": every question is restated and followed by the official worked
solution). Part A (mandatory): Q1 (weight not printed). Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Q1 sketch (p.2) is shipped as a figure inside the solution.
- Q1 f'' line: the printed intermediate numerator reads (2e^{2x}(2x-1) - 2e^{2x})x^2 ...; the derivative of
  e^{2x}(2x-1) is 2e^{2x}(2x-1) + 2e^{2x}, so the sign is corrected to "+" (the simplified f'' printed next is right).
  Intermediate slip, no student-facing label; logged in docs/ASK_ADIR.md.
- Q2a keeps the official wording "מהמעבר לגבול ... נוסחת הנסיגה".

Checks (tools/verify/20B-A/check.py, sympy): every derivative, sign claim, limit, integral, tangent line, arc length,
parameter value and area matches the official answer. 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20B-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
נחקור את הפונקציה לפי הסעיפים הבאים:
**תחום ההגדרה:** $x\neq 0$, ונמצא את הגבולות החד-צדדיים ב-$0$:
$$\lim_{x\to0^-}\frac{e^{2x}}{x}=-\infty,\qquad \lim_{x\to0^+}\frac{e^{2x}}{x}=+\infty$$
לכן הנקודה $x=0$ היא נקודת אי-רציפות מסוג שני, ואז $x=0$ היא אסימפטוטה אנכית לגרף הפונקציה.
**אסימפטוטות:** נמצא אסימפטוטות משופעות/אופקיות עבור $x\to+\infty$ ו-$x\to-\infty$ כי התנהגות של $e^{2x}$ עבור השאיפות אלו שונה.
$$k_1=\lim_{x\to+\infty}\frac{f(x)}{x}=\lim_{x\to+\infty}\frac{e^{2x}}{x^2}=\left\{\frac{\infty}{\infty}\right\}=\lim_{x\to+\infty}\frac{2e^{2x}}{2x}=\lim_{x\to+\infty}\frac{e^{2x}}{x}=\left\{\frac{\infty}{\infty}\right\}=\lim_{x\to+\infty}\frac{2e^{2x}}{1}=\infty$$
$$k_2=\lim_{x\to-\infty}\frac{f(x)}{x}=\lim_{x\to-\infty}\frac{e^{2x}}{x^2}=0,\qquad b_2=\lim_{x\to-\infty}\left(f(x)-k_2x\right)=\lim_{x\to-\infty}\frac{e^{2x}}{x}=0$$
לגרף הפונקציה אין אסימפטוטות ימניות, אך יש אסימפטוטה אופקית שמאלית $y=0$.
**זוגיות:** הפונקציה אינה בעלת זוגיות מוגדרת כי $f(-x)=-\frac{e^{-2x}}{x}\neq f(x)$ ו-$f(-x)=-\frac{e^{-2x}}{x}\neq -f(x)$.
**מונוטוניות וקיצון מקומי:**
$$f'(x)=\frac{2e^{2x}x-e^{2x}}{x^2}=\frac{e^{2x}(2x-1)}{x^2},\qquad f'(x)=0\ \Rightarrow\ x=\frac{1}{2}$$
טבלת סימנים של $f'$: שלילית ב-$x<0$ (ויורדת), שלילית ב-$0<x<\frac12$ (ויורדת), חיובית ב-$x>\frac12$ (עולה).
הנקודה $x=\frac{1}{2}$ היא נקודת מינימום מקומי ו-$f\left(\frac12\right)=2e$.
**קמירות/קעירות ונקודות פיתול:**
$$f''(x)=\frac{\left(2e^{2x}(2x-1)+2e^{2x}\right)x^2-e^{2x}(2x-1)2x}{x^4}=\frac{2e^{2x}\left(2x^2-2x+1\right)}{x^3},\qquad f''(x)\neq0$$
טבלת סימנים של $f''$: שלילית ב-$x<0$ (הפונקציה קעורה, $\\cap$), חיובית ב-$x>0$ (הפונקציה קמורה, $\\cup$).
הנקודה $x=0$ אינה בתחום ההגדרה ולכן אין נקודות פיתול. נשרטט את הגרף:
![שרטוט הגרף של y = e^(2x)/x עם האסימפטוטה האנכית x=0, האסימפטוטה השמאלית y=0 והמינימום ב-x=1/2](images/exams/20B-A-Q1-graph.png)
"""

SOL2A = r"""
נתבונן ב-$a_{n+1}-a_n$ ונקבל
$$a_{n+1}-a_n=3-\frac{2}{a_n}-a_n=\frac{(2-a_n)(a_n-1)}{a_n}.$$
נוכיח באמצעות אינדוקציה מתמטית ש-$1<a_n<2$. אמנם, $2>a_1>1$. נניח כי $2>a_k>1$ ונוכיח כי $2>a_{k+1}>1$. אם $1<a_k<2$ אז $1<\frac{2}{a_k}<2$ ו-$-2<-\frac{2}{a_k}<-1$, לכן $1<3-\frac{2}{a_k}<2$.
מההוכחה $1<a_n<2$ נובע כי $a_{n+1}-a_n>0$ ואז הסדרה עולה. מונוטוניות וחסימות גוררות כי הסדרה מתכנסת ונסמן את גבולה ב-$L$. מהמעבר לגבול בנוסחת הנסיגה נובע כי $L=3-\frac{2}{L}$ או $\frac{L^2-3L+2}{L}=0$ ולכן $L=1$ או $L=2$. לפי המונוטוניות (עולה) נקבל שהגבול שווה ל-$2$.
"""

SOL2B = r"""
העקומות נחתכות בנקודה $(1,1)$ והשיפועים לכל גרף שונים ב-$x=1$ כי $g'(1)=2$ ו-$f'(1)=-1$, לכן אין נקודת ההשקה המשותפת. נסמן את נקודת ההשקה של $f$ ב-$x_1$ ושל $g$ ב-$x_2$. אז נקבל את המערכת עבור אותו קו משיק:
$$\begin{cases}y-\frac{1}{x_1}=-\frac{1}{x_1^2}(x-x_1)\\ y-x_2^2=2x_2(x-x_2)\end{cases}\Rightarrow\begin{cases}y=-\frac{1}{x_1^2}x+\frac{2}{x_1}\\ y=2x_2x-x_2^2\end{cases}\Rightarrow\begin{cases}-\frac{1}{x_1^2}=2x_2\\ \frac{2}{x_1}=-x_2^2\end{cases}\Rightarrow\begin{cases}x_2=-\frac{1}{2x_1^2}\\ \frac{2}{x_1}=-\frac{1}{4x_1^4}\end{cases}$$
אז $x_1=-\frac{1}{2},\ x_2=-2$ ומשוואת המשיק לשני הגרפים היא $y=-4x-4$.
"""

SOL3A = r"""
$$\lim_{x\to0}\left(\frac{\sin x}{x}\right)^{\frac{1}{x^2}}=\{1^{\infty}\}=A$$
$$\ln A=\lim_{x\to0}\frac{\ln\frac{\sin x}{x}}{x^2}=\left\{\frac{0}{0}\right\}=\lim_{x\to0}\frac{\ln\sin x-\ln x}{x^2}=\lim_{x\to0}\frac{\frac{\cos x}{\sin x}-\frac{1}{x}}{2x}=\lim_{x\to0}\frac{x\cos x-\sin x}{2x^2\sin x}=$$
$$=\left\{\frac{0}{0}\right\}=\lim_{x\to0}\frac{-x\sin x}{4x\sin x+2x^2\cos x}=\lim_{x\to0}\frac{-\sin x}{4\sin x+2x\cos x}=\left\{\frac{0}{0}\right\}=\lim_{x\to0}\frac{-\cos x}{6\cos x-2x\sin x}=-\frac{1}{6}$$
התשובה: $e^{-\frac{1}{6}}$.
"""

SOL3B = r"""
נפרק את השבר לשברים אלמנטריים:
$$\frac{2x^2+15}{x(x^2+2x+5)}=\frac{A}{x}+\frac{Bx+C}{x^2+2x+5}=\frac{A(x^2+2x+5)+x(Bx+C)}{x(x^2+2x+5)}$$
מהשוואת הפולינומים נקבל $\begin{cases}A+B=2\\2A+C=0\\5A=15\end{cases}$ או $\begin{cases}A=3\\B=-1\\C=-6\end{cases}$, לכן
$$\int\frac{2x^2+15}{x(x^2+2x+5)}dx=\int\left(\frac{3}{x}-\frac{x+6}{x^2+2x+5}\right)dx=3\ln|x|-\int\frac{x+6}{x^2+2x+5}dx$$
$$\int\frac{x+6}{x^2+2x+5}dx=\begin{vmatrix}t=x+1\\x=t-1\\dx=dt\end{vmatrix}=\int\frac{t+5}{t^2+4}dt=\int\frac{t\,dt}{t^2+4}+5\int\frac{dt}{t^2+4}=\frac{1}{2}\ln(t^2+4)+\frac{5}{2}\arctan\frac{t}{2}+C=\frac{1}{2}\ln(x^2+2x+5)+\frac{5}{2}\arctan\frac{x+1}{2}+C$$
$$\int\frac{2x^2+15}{x(x^2+2x+5)}dx=3\ln|x|-\frac{1}{2}\ln(x^2+2x+5)-\frac{5}{2}\arctan\frac{x+1}{2}+C$$
"""

SOL4A = r"""
$$\lim_{x\to+\infty}\left[x\left(\sqrt{x^2+x+a}-\sqrt{x^2-bx}\right)\right]=\lim_{x\to+\infty}x\,\frac{x^2+x+a-(x^2-bx)}{\sqrt{x^2+x+a}+\sqrt{x^2-bx}}=$$
$$=\lim_{x\to+\infty}\frac{(1+b)x^2+ax}{\sqrt{x^2+x+a}+\sqrt{x^2-bx}}$$
החזקה הגבוהה ביותר במונה היא $x^2$ אם $b\neq-1$ והחזקה של המכנה $x$. לכן הגבול קיים רק עבור $b=-1$ ואז
$$\lim_{x\to+\infty}\frac{ax}{\sqrt{x^2+x+a}+\sqrt{x^2+x}}=\lim_{x\to+\infty}\frac{a}{\sqrt{1+\frac{1}{x}+\frac{a}{x^2}}+\sqrt{1+\frac{1}{x}}}=\frac{a}{2}.$$
השוויון מתקיים רק כאשר $a=6,\ b=-1$.
"""

SOL4B = r"""
$$\int\frac{\sin x\cos x\,dx}{1+\sin^2x}=\begin{vmatrix}t=\sin x\\dt=\cos x\,dx\end{vmatrix}=\int\frac{t\,dt}{1+t^2}=\frac{1}{2}\ln(1+t^2)+C=\frac{1}{2}\ln\left(1+\sin^2x\right)+C$$
"""

SOL5A = r"""
הערך של הפונקציה בנקודה $x=1$ שווה ל-$0$. נבדוק את הגזירות לפי ההגדרה:
$$f'(1)=\lim_{h\to0}\frac{f(1+h)-f(1)}{h}=\lim_{h\to0}\frac{\sqrt[3]{h^2}\sin h}{h}=\lim_{h\to0}\sqrt[3]{h^2}=0$$
לכן הפונקציה גזירה ב-$1$ והנגזרת שלה שווה ל-$0$ בנקודה זאת.
"""

SOL5B = r"""
לפי הנוסחה: $L=\int_0^1\sqrt{1+(y')^2}\,dx$, אז נמצא את הנגזרת של הפונקציה:
$$y'=\frac{2}{5}\cdot\frac{5}{4}x^{\frac14}-\frac{2}{3}\cdot\frac{3}{4}x^{-\frac14}=\frac{1}{2}\left(x^{\frac14}-x^{-\frac14}\right),$$
$$1+(y')^2=1+\frac{x^{\frac12}-2+x^{-\frac12}}{4}=\frac{x^{\frac12}+2+x^{-\frac12}}{4}=\left(\frac{x^{\frac14}+x^{-\frac14}}{2}\right)^2,$$
$$L=\int_0^1\sqrt{1+(y')^2}\,dx=\frac{1}{2}\int_0^1\left(x^{\frac14}+x^{-\frac14}\right)dx=\frac{1}{2}\left(\frac{4}{5}x^{\frac54}+\frac{4}{3}x^{\frac34}\right)\Big|_0^1=\frac{2}{5}+\frac{2}{3}=\frac{16}{15}$$
"""

SOL6A = r"""
נמצא את הנגזרת של הפונקציה:
$$g'(x)=\frac{2x(x-b)-(x^2+a)}{(x-b)^2}=\frac{x^2-2bx-a}{(x-b)^2}.$$
מקיום הקיצון המקומי ב-$x=2$ נובע $g'(2)=0$ או $4-4b-a=0$. השיפוע של אסימפטוטה $y=kx+m$ הוא
$$k=\lim_{x\to\infty}\frac{g(x)}{x}=\lim_{x\to\infty}\frac{x^2+a}{x(x-b)}=1$$
והאיבר החופשי
$$m=\lim_{x\to\infty}\left(g(x)-x\right)=\lim_{x\to\infty}\left(\frac{x^2+a}{x-b}-x\right)=\lim_{x\to\infty}\frac{bx+a}{x-b}=b.$$
מהתנאי נקבל $b=7$ ו-$a=4-4b=-24$.
"""

SOL6B = r"""
נציין כי בקטע $[0,1]$ הפונקציה מקבלת ערכים לא שליליים כי $\ln(x+1)\ge0$ ו-$\sqrt{x+1}\ge1$, לכן
$$S=\int_0^1\frac{\ln(x+1)}{\sqrt{x+1}}\,dx.$$
לפי אינטגרציה בחלקים נקבל, עם $u=\ln(x+1),\ dv=\frac{dx}{\sqrt{x+1}},\ du=\frac{dx}{x+1},\ v=2\sqrt{x+1}$:
$$S=2\sqrt{x+1}\ln(x+1)\Big|_0^1-2\int_0^1\frac{\sqrt{x+1}}{x+1}\,dx=2\sqrt{2}\ln2-2\int_0^1\frac{dx}{\sqrt{x+1}}=2\sqrt{2}\ln2-4\sqrt{x+1}\Big|_0^1=2\sqrt{2}\ln2-4\sqrt{2}+4$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $y=\frac{e^{2x}}{x}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, נקודות קיצון, "
      "תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1),

    Q(2, "proof", "sequences_limits",
      "נתונה הסדרה " r"$a_{n+1}=3-\frac{2}{a_n},\quad a_1=\frac{3}{2}$" ". הראו כי היא מונוטונית, חסומה וחשבו את גבולה.",
      SOL2A, part="א", points=10),

    Q(2, "computation", "derivatives_tangents",
      r"מצאו את משוואת המשיק המשותף לגרפים של שתי הפונקציות $f(x)=\frac{1}{x}$ ו-$g(x)=x^2$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\left(\frac{\sin x}{x}\right)^{\frac{1}{x^2}}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{2x^2+15}{x\left(x^2+2x+5\right)}\,dx$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "function_limits",
      r"מצאו עבור אילו פרמטרים ממשיים $a,b$ מתקיים השוויון: $\lim_{x\to+\infty}\left[x\left(\sqrt{x^2+x+a}-\sqrt{x^2-bx}\right)\right]=3$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\sin x\cos x\,dx}{1+\sin^2x}$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "derivatives_tangents",
      r"בדקו האם הפונקציה $f(x)=\sqrt[3]{(x-1)^2}\,\sin(x-1)$ גזירה בנקודה $x=1$?",
      SOL5A, part="א", points=10),

    Q(5, "computation", "definite_integrals",
      r"חשבו את אורך הקשת של העקומה $y=\frac{2}{5}x\sqrt[4]{x}-\frac{2}{3}\sqrt[4]{x^3}$ בתחום $0\le x\le1$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "function_investigation",
      r"נתונה הפונקציה $g(x)=\frac{x^2+a}{x-b}$ וידוע כי היא מקבלת קיצון מקומי ב-$x=2$ והקו $y=x+7$ הוא אסימפטוטה משופעת "
      "של גרף הפונקציה באינסוף. מצאו את $a$ ו-$b$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "definite_integrals",
      r"חשבו את השטח של התחום הנמצא בין גרף הפונקציה $f(x)=\frac{\ln(x+1)}{\sqrt{x+1}}$ לבין ציר ה-$x$ בקטע $[0,1]$.",
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



# ===== Q1: f = e^(2x)/x =====
f1 = sp.exp(2*x)/x
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, sp.exp(2*x)*(2*x - 1)/x**2) and same(f1pp, 2*sp.exp(2*x)*(2*x**2 - 2*x + 1)/x**3)
assert sp.solve(f1p, x) == [R(1, 2)] and sp.simplify(f1.subs(x, R(1, 2)) - 2*sp.E) == 0
assert sp.limit(f1, x, -sp.oo) == 0 and sp.limit(f1, x, sp.oo) == sp.oo and sp.limit(f1/x, x, sp.oo) == sp.oo
assert sp.limit(f1, x, 0, '+') == sp.oo and sp.limit(f1, x, 0, '-') == -sp.oo
assert all(f1pp.subs(x, v) < 0 for v in (-3, R(-1, 2))) and all(f1pp.subs(x, v) > 0 for v in (R(1, 2), 3))
assert 2*x**2 - 2*x + 1 != 0 and sp.discriminant(2*x**2 - 2*x + 1, x) < 0

add(1,
    rubric=rub((r"תחום הגדרה $x\neq0$ וסיווג $x=0$ כאי-רציפות מסוג שני עם אסימפטוטה אנכית", 3),
               (r"אסימפטוטות באינסוף: אין ב-$+\infty$ ($k=\infty$), ואופקית $y=0$ ב-$-\infty$", 4),
               (r"נגזרת $f'(x)=\frac{e^{2x}(2x-1)}{x^2}$, טבלת סימנים ומינימום מקומי $f\left(\frac12\right)=2e$", 5),
               (r"$f''(x)=\frac{2e^{2x}(2x^2-2x+1)}{x^3}$, קמירות וקעירות ואין נקודות פיתול", 5),
               ("שרטוט הגרף בהתאם לכל הנתונים", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לטעון שיש אסימפטוטה אופקית $y=0$ גם ב-$+\infty$: שם $\frac{e^{2x}}{x}\to\infty$ ואין אסימפטוטה בכלל.",
              r"לראות בנקודה $x=0$ נקודת פיתול כי $f''$ מחליפה סימן, אף ש-$x=0$ אינה בתחום ההגדרה.",
              r"לשכוח שהמונה $2x^2-2x+1$ של $f''$ חיובי תמיד (דיסקרימיננטה שלילית), ולכן הסימן נקבע לפי $x^3$."],
    steps=[
        chx(r"מהי הנגזרת של $f(x)=\frac{e^{2x}}{x}$?", sp.exp(2*x)*(2*x - 1)/x**2,
            [sp.exp(2*x)*(2*x + 1)/x**2, sp.exp(2*x)*(2*x - 1)/x, 2*sp.exp(2*x)/x**2],
            lambda e: same(e, f1p), r"כלל המנה: $f'(x)=\frac{2e^{2x}x-e^{2x}}{x^2}=\frac{e^{2x}(2x-1)}{x^2}$ (אומת ב-sympy)."),
        num(r"מהו ה-$x$ של נקודת המינימום המקומי?", R(1, 2), r"$f'(x)=0$ נותן $2x-1=0$, כלומר $x=\frac{1}{2}$."),
        num(r"מהו $f\left(\frac{1}{2}\right)$? (עשרוני)", f1.subs(x, R(1, 2)), r"$f\left(\frac12\right)=\frac{e}{1/2}=2e\approx5.4366$."),
        chx(r"מהי הנגזרת השנייה של $f$?", 2*sp.exp(2*x)*(2*x**2 - 2*x + 1)/x**3,
            [2*sp.exp(2*x)*(2*x**2 + 2*x + 1)/x**3, 2*sp.exp(2*x)*(2*x**2 - 2*x + 1)/x**2, 4*sp.exp(2*x)/x**3],
            lambda e: same(e, f1pp), r"גוזרים את $f'$ בכלל המנה ומקבלים $f''(x)=\frac{2e^{2x}(2x^2-2x+1)}{x^3}$ (אומת ב-sympy)."),
        ch("מהן האסימפטוטות של הגרף?", r"אנכית $x=0$ ואופקית $y=0$ רק ב-$-\infty$; אין אסימפטוטה ב-$+\infty$",
           [r"אנכית $x=0$ ואופקית $y=0$ גם ב-$+\infty$ וגם ב-$-\infty$", r"אנכית $x=0$ ואסימפטוטה משופעת ב-$+\infty$ בלבד",
            r"אופקית $y=0$ בלבד"],
           r"$\lim_{x\to-\infty}f=0$, $\lim_{x\to+\infty}f=\infty$ ו-$\lim_{x\to+\infty}\frac{f}{x}=\infty$ (אין שיפוע סופי); בנוסף $\lim_{x\to0^\pm}f=\pm\infty$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: a_{n+1} = 3 - 2/a_n, a_1 = 3/2 =====
an = sp.Symbol('a_n', positive=True)
assert same((3 - 2/an) - an, (2 - an)*(an - 1)/an)
seq = [R(3, 2)]
for _ in range(60):
    seq.append(3 - 2/seq[-1])
assert all(1 < v < 2 for v in seq) and all(seq[i] < seq[i + 1] for i in range(60)) and abs(float(seq[-1]) - 2) < 1e-9
assert seq[1] == R(5, 3)
Ls = sp.symbols('L')
assert sp.solve(sp.Eq(Ls, 3 - 2/Ls), Ls) == [1, 2] or set(sp.solve(sp.Eq(Ls, 3 - 2/Ls), Ls)) == {1, 2}
L2 = [r"נוכיח באינדוקציה ש-$1<a_n<2$ לכל $n$: עבור $n=1$ מתקיים $a_1=\frac{3}{2}$.",
      r"אם $1<a_k<2$ אז $1<\frac{2}{a_k}<2$, ולכן $1<3-\frac{2}{a_k}<2$, כלומר $1<a_{k+1}<2$.",
      r"לכן $a_{n+1}-a_n=\frac{(2-a_n)(a_n-1)}{a_n}>0$, והסדרה עולה.",
      r"סדרה עולה וחסומה מתכנסת, ונסמן את גבולה ב-$L$.",
      r"מנוסחת הנסיגה $L=3-\frac{2}{L}$, כלומר $L^2-3L+2=0$ ו-$L=1$ או $L=2$. הסדרה עולה מ-$a_1=\frac{3}{2}$, ולכן $L=2$."]
L2b = list(L2)
L2b[4] = r"מנוסחת הנסיגה $L=3-\frac{2}{L}$, כלומר $L^2-3L+2=0$ ו-$L=1$ או $L=2$. הסדרה עולה מ-$a_1=\frac{3}{2}$, ולכן $L=1$."

add(2, "א",
    rubric=rub((r"הוכחה באינדוקציה ש-$1<a_n<2$ (בסיס וצעד)", 3),
               (r"חישוב $a_{n+1}-a_n=\frac{(2-a_n)(a_n-1)}{a_n}>0$ ומסקנה שהסדרה עולה", 3),
               (r"מסקנה מונוטוניות וחסימות: הסדרה מתכנסת", 1),
               (r"מעבר לגבול בנוסחת הנסיגה: $L^2-3L+2=0$ ובחירה נכונה $L=2$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לבחור $L=1$ בלי לשים לב שסדרה עולה המתחילה מ-$\frac{3}{2}$ לא יכולה להתכנס לערך קטן ממנה.",
              r"לעבור לגבול בנוסחת הנסיגה לפני שהוכחנו שהסדרה מתכנסת.",
              r"להניח $a_n>0$ במקום להוכיח את החסימה $1<a_n<2$, שממנה נובע סימן הפרש."],
    steps=[
        num(r"מהו $a_2$? (עשרוני)", seq[1], r"$a_2=3-\frac{2}{3/2}=3-\frac{4}{3}=\frac{5}{3}\approx1.6667$."),
        chx(r"מהו $a_{n+1}-a_n$ בצורה מפורקת?", (2 - an)*(an - 1)/an, [(2 - an)*(an + 1)/an, (an - 2)*(an - 1)/an, (2 - an)*(an - 1)],
            lambda e: same(e, (3 - 2/an) - an), r"$3-\frac{2}{a_n}-a_n=\frac{-a_n^2+3a_n-2}{a_n}=\frac{(2-a_n)(a_n-1)}{a_n}$ (אומת ב-sympy)."),
        order("סדרו את שלבי ההוכחה.", L2, "חסימה באינדוקציה, אחר כך מונוטוניות (שנשענת על החסימה), התכנסות, ולבסוף מציאת הגבול. כל שלב נשען על קודמו."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L2b, 4,
                r"הסדרה עולה ו-$a_1=\frac{3}{2}>1$, לכן $L\ge\frac{3}{2}$ ו-$L=1$ אינו אפשרי; נכון $L=2$ (הסדרה מתקרבת ל-$2$ בחישוב ישיר)."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: common tangent of 1/x and x^2 =====
x1s, x2s = sp.symbols('x1 x2')
tl_f = lambda p: (-1/p**2, 2/p)       # slope, intercept of the tangent to 1/x at p
tl_g = lambda p: (2*p, -p**2)         # slope, intercept of the tangent to x^2 at p
assert tl_f(R(-1, 2)) == tl_g(-2) == (-4, -4)


def tangent_to_both(m_, k_):
    # y = m x + k tangent to 1/x ( x*(m x + k) = 1 has a double root ) and to x^2 ( x^2 - m x - k = 0 has a double root )
    return sp.discriminant(m_*x**2 + k_*x - 1, x) == 0 and sp.discriminant(x**2 - m_*x - k_, x) == 0


assert tangent_to_both(-4, -4) and not tangent_to_both(4, 4) and not tangent_to_both(-4, 4) and not tangent_to_both(-4, -2)
good_sys = (-1/x1s**2, 2*x2s, 2/x1s, -x2s**2)
assert good_sys[0].subs(x1s, R(-1, 2)) == good_sys[1].subs(x2s, -2) and good_sys[2].subs(x1s, R(-1, 2)) == good_sys[3].subs(x2s, -2)
assert (2/x1s).subs(x1s, R(-1, 2)) != (x2s**2).subs(x2s, -2) and (1/x1s).subs(x1s, R(-1, 2)) != (x2s**2).subs(x2s, -2)

add(2, "ב",
    rubric=rub((r"נקודות ההשקה שונות: $x_1$ עבור $f$ ו-$x_2$ עבור $g$ (בגלל שהשיפועים ב-$(1,1)$ שונים)", 2),
               (r"משוואות המשיקים: $y=-\frac{1}{x_1^2}x+\frac{2}{x_1}$ ו-$y=2x_2x-x_2^2$", 3),
               (r"השוואת שיפועים ומשוואות חופשיים: $-\frac{1}{x_1^2}=2x_2$ ו-$\frac{2}{x_1}=-x_2^2$", 2),
               (r"פתרון $x_1=-\frac12$, $x_2=-2$ והמשיק $y=-4x-4$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"להניח שהמשיק עובר בנקודת החיתוך $(1,1)$ של הגרפים. שם השיפועים שונים ($-1$ ו-$2$), ולכן אין משיק משותף בה.",
              r"להשתמש באותו $x$ עבור שתי הפונקציות במקום $x_1$ ו-$x_2$ נפרדים.",
              r"לטעות בחותך של המשיק ל-$x^2$: הוא $-x_2^2$ ולא $+x_2^2$."],
    steps=[
        ch(r"אילו שתי משוואות מבטאות שישר הוא משיק גם ל-$f(x)=\frac{1}{x}$ בנקודה $x_1$ וגם ל-$g(x)=x^2$ בנקודה $x_2$?",
           r"$-\frac{1}{x_1^2}=2x_2$ ו-$\frac{2}{x_1}=-x_2^2$",
           [r"$-\frac{1}{x_1^2}=2x_2$ ו-$\frac{2}{x_1}=x_2^2$", r"$\frac{1}{x_1}=x_2^2$ ו-$-\frac{1}{x_1^2}=2x_2$", r"$x_1=x_2$ ו-$-\frac{1}{x_1^2}=2x_1$"],
           r"המשיקים הם $y=-\frac{x}{x_1^2}+\frac{2}{x_1}$ ו-$y=2x_2x-x_2^2$; ישר משותף דורש שיפוע שווה וחותך שווה. הפתרון $x_1=-\frac12$, $x_2=-2$ מקיים רק את הזוג הראשון."),
        num(r"מהו $x_1$?", R(-1, 2), r"מהמשוואות נקבל $\frac{2}{x_1}=-\frac{1}{4x_1^4}$, כלומר $x_1^3=-\frac{1}{8}$ ו-$x_1=-\frac{1}{2}$."),
        num(r"מהו $x_2$?", -2, r"$x_2=-\frac{1}{2x_1^2}=-\frac{1}{2\cdot\frac14}=-2$."),
        ch("מהי משוואת המשיק המשותף?", "$y=-4x-4$", ["$y=4x+4$", "$y=-4x+4$", "$y=-4x-2$"],
           r"השיפוע הוא $-\frac{1}{x_1^2}=-4$ והחותך $\frac{2}{x_1}=-4$. רק הישר $y=-4x-4$ משיק גם ל-$\frac1x$ וגם ל-$x^2$ (נבדק ב-sympy לפי דיסקרימיננטה אפס)."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: lim (sin x / x)^(1/x^2) =====
g3 = (sp.sin(x)/x)**(1/x**2)
lnA = sp.limit(sp.log(sp.sin(x)/x)/x**2, x, 0)
assert lnA == R(-1, 6)
assert sp.limit(sp.sin(x)/x, x, 0) == 1 and sp.limit(1/x**2, x, 0, '+') == sp.oo
assert abs(float(sp.N(g3.subs(x, R(1, 1000)))) - float(sp.exp(R(-1, 6)))) < 1e-5

add(3, "א",
    rubric=rub((r"זיהוי צורה $1^{\infty}$ והעברה ללוגריתם: $\ln A=\lim\frac{\ln\frac{\sin x}{x}}{x^2}$", 3),
               (r"הפעלת לופיטל מספר פעמים עד $\ln A=-\frac16$", 5),
               (r"חזרה מהלוגריתם: $A=e^{-\frac16}$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לכתוב $1^{\infty}=1$. זו אי-ודאות ולא ערך.",
              r"לשכוח לחזור מ-$\ln A$ ל-$A$ בסוף ולהשאיר $-\frac16$ כתשובה.",
              r"לעצור אחרי לופיטל אחד כשעדיין מתקבלת צורה $\frac{0}{0}$."],
    steps=[
        ch(r"מהי צורת אי-הוודאות של $\lim_{x\to0}\left(\frac{\sin x}{x}\right)^{\frac{1}{x^2}}$?", r"$1^{\infty}$", [r"$0^0$", r"$\infty^0$", r"$\frac{0}{0}$"],
           r"הבסיס $\frac{\sin x}{x}\to1$ והחזקה $\frac{1}{x^2}\to\infty$, כלומר $1^{\infty}$."),
        num(r"מהו $\ln A=\lim_{x\to0}\frac{\ln\frac{\sin x}{x}}{x^2}$? (עשרוני)", lnA, r"אחרי שלוש הפעלות של לופיטל מקבלים $\frac{-\cos x}{6\cos x-2x\sin x}\to-\frac{1}{6}\approx-0.1667$."),
        num(r"מהו הגבול $A=e^{\ln A}$? (עשרוני)", sp.exp(lnA), r"$A=e^{-1/6}\approx0.8465$."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: int (2x^2+15)/(x(x^2+2x+5)) =====
g3b = (2*x**2 + 15)/(x*(x**2 + 2*x + 5))
A3, B3, C3 = sp.symbols('A B C')
sol3 = sp.solve(sp.Poly(sp.expand(A3*(x**2 + 2*x + 5) + (B3*x + C3)*x - (2*x**2 + 15)), x).all_coeffs(), [A3, B3, C3], dict=True)[0]
assert sol3 == {A3: 3, B3: -1, C3: -6}
assert sp.discriminant(x**2 + 2*x + 5, x) < 0
for bf in [A3*(x**2 + 2*x + 5) + B3*x - (2*x**2 + 15), A3*(x**2 + 2*x + 5) + B3*x**2 - (2*x**2 + 15)]:
    assert sp.solve(sp.Poly(sp.expand(bf), x).all_coeffs(), [A3, B3], dict=True) == []
F3 = 3*sp.log(x) - sp.log(x**2 + 2*x + 5)/2 - 5*sp.atan((x + 1)/2)/2
assert same(sp.diff(F3, x), g3b)
F3w = [3*sp.log(x) + sp.log(x**2 + 2*x + 5)/2 - 5*sp.atan((x + 1)/2)/2, 3*sp.log(x) - sp.log(x**2 + 2*x + 5)/2 + 5*sp.atan((x + 1)/2)/2,
       3*sp.log(x) - sp.log(x**2 + 2*x + 5)/2 - 5*sp.atan(x + 1)/2]

add(3, "ב",
    rubric=rub((r"פירוק לשברים חלקיים בצורה $\frac{A}{x}+\frac{Bx+C}{x^2+2x+5}$", 2),
               (r"חישוב המקדמים $A=3$, $B=-1$, $C=-6$", 3),
               (r"השלמה לריבוע והצבה $t=x+1$ באינטגרל $\int\frac{x+6}{x^2+2x+5}dx$", 2),
               (r"אינטגרציה: לוגריתם ו-$\arctan\frac{x+1}{2}$ ותשובה סופית עם $+C$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לכתוב מונה קבוע $B$ מעל הגורם הריבועי $x^2+2x+5$. כך אין פתרון למערכת המקדמים.",
              r"לשכוח את הגורם $\frac{1}{2}$ באינטגרל $\int\frac{dt}{t^2+4}=\frac{1}{2}\arctan\frac{t}{2}$.",
              r"לשכוח סימן מינוס כשמוציאים את $-\int\frac{x+6}{x^2+2x+5}dx$."],
    steps=[
        ch(r"איזה פירוק מתאים ל-$\frac{2x^2+15}{x(x^2+2x+5)}$?", r"$\frac{A}{x}+\frac{Bx+C}{x^2+2x+5}$",
           [r"$\frac{A}{x}+\frac{B}{x^2+2x+5}$", r"$\frac{A}{x}+\frac{Bx}{x^2+2x+5}$"],
           r"הגורם $x^2+2x+5$ אי-פריק (דיסקרימיננטה שלילית) ולכן מעליו מונה לינארי. בשתי האפשרויות האחרות למערכת המקדמים אין פתרון (אומת ב-sympy)."),
        num(r"מהו $A$?", sol3[A3], r"הצבת $x=0$ ב-$2x^2+15=A(x^2+2x+5)+(Bx+C)x$ נותנת $15=5A$, כלומר $A=3$."),
        num(r"מהו $B$?", sol3[B3], r"מהשוואת מקדמי $x^2$: $A+B=2$, ולכן $B=-1$."),
        num(r"מהו $C$?", sol3[C3], r"מהשוואת מקדמי $x$: $2A+C=0$, ולכן $C=-6$."),
        chx(r"מהי הפונקציה הקדומה (בתחום $x>0$, בלי הקבוע)?", F3, F3w, lambda e: same(sp.diff(e, x), g3b),
            r"$3\ln x-\frac{1}{2}\ln(x^2+2x+5)-\frac{5}{2}\arctan\frac{x+1}{2}$; הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: parameters a, b =====
a4, b4 = sp.symbols('a b', real=True)
h4 = lambda av, bv: x*(sp.sqrt(x**2 + x + av) - sp.sqrt(x**2 - bv*x))
assert sp.limit(h4(6, -1), x, sp.oo) == 3
assert all(sp.limit(h4(6, bv), x, sp.oo) in (sp.oo, -sp.oo) for bv in (0, 1, -2))
assert sp.limit(h4(4, -1), x, sp.oo) == 2 and sp.limit(h4(R(7, 2), -1), x, sp.oo) == R(7, 4)

add(4, "א",
    rubric=rub((r"כפל בצמוד והבאה לצורה $\frac{(1+b)x^2+ax}{\sqrt{x^2+x+a}+\sqrt{x^2-bx}}$", 3),
               (r"נימוק שהגבול סופי רק כאשר $b=-1$ (אחרת המונה מסדר $x^2$ והמכנה מסדר $x$)", 3),
               (r"חישוב הגבול עבור $b=-1$: $\frac{a}{2}$", 2),
               (r"השוואה ל-$3$ ופתרון $a=6$, $b=-1$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לחשב את הגבול כאילו $b=-1$ מראש, בלי להסביר למה אין פתרון עבור $b\neq-1$.",
              r"לשכוח שבחילוק ב-$x$ מתחת לשורש מתקבל $|x|=x$ ב-$+\infty$ (בלי שינוי סימן)."],
    steps=[
        ch(r"לאיזה ערך של $b$ הגבול $\lim_{x\to+\infty}x\left(\sqrt{x^2+x+a}-\sqrt{x^2-bx}\right)$ יכול להיות סופי?", "$b=-1$", ["$b=0$", "$b=1$", r"לכל ערך של $b$"],
           r"אחרי הכפל בצמוד המונה הוא $(1+b)x^2+ax$ והמכנה מסדר $x$. אם $b\neq-1$ הגבול אינסופי (נבדק ב-sympy עבור $b=0,1,-2$), ולכן $b=-1$."),
        num(r"עבור $b=-1$ הגבול שווה ל-$\frac{a}{2}$. מהו הגבול כאשר $a=4$?", 2, r"$\frac{a}{2}=\frac{4}{2}=2$ (נבדק ב-sympy)."),
        num(r"מהו $a$ שעבורו הגבול שווה ל-$3$?", 6, r"$\frac{a}{2}=3$ נותן $a=6$; עבור $a=6$, $b=-1$ הגבול הוא $3$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: int sin x cos x/(1+sin^2 x) =====
g4b = sp.sin(x)*sp.cos(x)/(1 + sp.sin(x)**2)
F4b = sp.log(1 + sp.sin(x)**2)/2
assert same(sp.diff(F4b, x), g4b)
F4bw = [sp.log(1 + sp.sin(x)**2), sp.log(1 + sp.sin(x))/2, sp.atan(sp.sin(x))/2, -sp.log(1 + sp.sin(x)**2)/2]
i4 = sp.integrate(t/(1 + t**2), (t, 0, 1))
assert sp.simplify(i4 - sp.log(2)/2) == 0

add(4, "ב",
    rubric=rub((r"הצבה $t=\sin x$, $dt=\cos x\,dx$", 3),
               (r"אינטגרל $\int\frac{t}{1+t^2}dt=\frac12\ln(1+t^2)$", 4),
               (r"חזרה למשתנה המקורי ותשובה $\frac12\ln(1+\sin^2x)+C$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לשכוח את הגורם $\frac{1}{2}$ באינטגרל של $\frac{t}{1+t^2}$ (נגזרת המכנה היא $2t$).",
              r"לשכוח לחזור מ-$t$ ל-$\sin x$ בסוף."],
    steps=[
        ch("איזו הצבה משתמש הפתרון הרשמי?", r"$t=\sin x$", [r"$t=\cos x$", r"$t=\tan x$", r"$t=1+\cos x$"],
           r"הפתרון הרשמי מציב $t=\sin x$ ולכן $dt=\cos x\,dx$ והאינטגרל נהיה $\int\frac{t}{1+t^2}dt$."),
        num(r"מהו $\int_0^1\frac{t}{1+t^2}dt$? (עשרוני)", i4, r"$\frac{1}{2}\ln(1+t^2)\Big|_0^1=\frac{1}{2}\ln2\approx0.3466$."),
        chx(r"מהי הפונקציה הקדומה של $\frac{\sin x\cos x}{1+\sin^2x}$?", F4b, F4bw, lambda e: same(sp.diff(e, x), g4b),
            r"אחרי ההצבה $\frac12\ln(1+t^2)$, ובחזרה ל-$x$: $\frac12\ln(1+\sin^2x)$. הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-verified")

# ===== Q5a: differentiability at x=1 =====
hh = sp.Symbol('h', real=True)
dq = (hh**2)**R(1, 3)*sp.sin(hh)/hh
assert sp.limit(dq, hh, 0, '+') == 0 and sp.limit(dq, hh, 0, '-') == 0
assert sp.limit(sp.sin(hh)/hh, hh, 0) == 1

add(5, "א",
    rubric=rub((r"חישוב $f(1)=0$ ורישום הגבול המגדיר את $f'(1)$", 3),
               (r"הצבה ופישוט: $\frac{\sqrt[3]{h^2}\sin h}{h}$", 3),
               (r"חישוב הגבול $0$ משני הצדדים ומסקנה: גזירה עם $f'(1)=0$", 4)),
    rubricSource="ai-verified",
    pitfalls=[r"לטעון ש-$\sqrt[3]{(x-1)^2}$ אינה גזירה ב-$1$ ולכן גם המכפלה אינה גזירה. הגורם $\sin(x-1)$ מרסן את התנהגות הנגזרת.",
              r"לגזור בכלל המכפלה כרגיל ולקבל ביטוי לא מוגדר ב-$x=1$ במקום להשתמש בהגדרת הנגזרת."],
    steps=[
        num(r"מהו $f(1)$?", 0, r"$f(1)=\sqrt[3]{0}\cdot\sin0=0$."),
        num(r"מהו $\lim_{h\to0}\frac{\sin h}{h}$?", 1, r"גבול יסודי."),
        num(r"מהו $f'(1)$?", 0, r"$\frac{f(1+h)-f(1)}{h}=\sqrt[3]{h^2}\cdot\frac{\sin h}{h}\to0\cdot1=0$ משני הצדדים (נבדק ב-sympy)."),
        ch("האם $f$ גזירה ב-$x=1$?", r"כן, והנגזרת היא $0$", [r"לא, כי $\sqrt[3]{(x-1)^2}$ אינה גזירה ב-$1$", r"לא, כי הגבולות החד-צדדיים שונים", r"כן, והנגזרת היא $1$"],
           r"שני הגבולות החד-צדדיים של מנת ההפרשים שווים ל-$0$, ולכן $f$ גזירה ו-$f'(1)=0$."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: arc length =====
y5 = R(2, 5)*x**R(5, 4) - R(2, 3)*x**R(3, 4)
y5p = sp.diff(y5, x)
assert same(y5p, (x**R(1, 4) - x**R(-1, 4))/2)
assert same(1 + y5p**2, ((x**R(1, 4) + x**R(-1, 4))/2)**2)
L5 = sp.integrate((x**R(1, 4) + x**R(-1, 4))/2, (x, 0, 1))
assert L5 == R(16, 15)

add(5, "ב",
    rubric=rub((r"נוסחת אורך הקשת $L=\int_0^1\sqrt{1+(y')^2}\,dx$", 2),
               (r"נגזרת $y'=\frac12\left(x^{1/4}-x^{-1/4}\right)$", 3),
               (r"השלמה לריבוע מושלם: $1+(y')^2=\left(\frac{x^{1/4}+x^{-1/4}}{2}\right)^2$", 3),
               (r"אינטגרציה וחישוב $L=\frac{16}{15}$", 2)),
    rubricSource="ai-verified",
    pitfalls=[r"לא לזהות ש-$1+(y')^2$ הוא ריבוע מושלם ולהישאר עם שורש שאין לו פונקציה קדומה פשוטה.",
              r"טעות בחזקות בגזירה: $\left(x^{5/4}\right)'=\frac54x^{1/4}$."],
    steps=[
        chx(r"מהי הנגזרת $y'$?", (x**R(1, 4) - x**R(-1, 4))/2, [(x**R(1, 4) + x**R(-1, 4))/2, (x**R(1, 4) - x**R(-1, 4)), (x**R(5, 4) - x**R(3, 4))/2],
            lambda e: same(e, y5p), r"$y'=\frac25\cdot\frac54x^{1/4}-\frac23\cdot\frac34x^{-1/4}=\frac12\left(x^{1/4}-x^{-1/4}\right)$ (אומת ב-sympy)."),
        chx(r"מהו $1+(y')^2$?", ((x**R(1, 4) + x**R(-1, 4))/2)**2, [((x**R(1, 4) - x**R(-1, 4))/2)**2, (x**R(1, 4) + x**R(-1, 4))/2, 1 + (x**R(1, 4) - x**R(-1, 4))],
            lambda e: same(e, 1 + y5p**2), r"$1+\frac{x^{1/2}-2+x^{-1/2}}{4}=\frac{x^{1/2}+2+x^{-1/2}}{4}=\left(\frac{x^{1/4}+x^{-1/4}}{2}\right)^2$ (אומת ב-sympy)."),
        num(r"מהו אורך הקשת? (עשרוני)", L5, r"$\frac12\left(\frac45x^{5/4}+\frac43x^{3/4}\right)\Big|_0^1=\frac25+\frac23=\frac{16}{15}\approx1.0667$."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: parameters of g = (x^2+a)/(x-b) =====
g6 = (x**2 + a4)/(x - b4)
g6p = sp.diff(g6, x)
assert same(g6p, (x**2 - 2*b4*x - a4)/(x - b4)**2)
assert sp.limit(g6.subs({a4: -24, b4: 7})/x, x, sp.oo) == 1 and sp.limit(g6.subs({a4: -24, b4: 7}) - x, x, sp.oo) == 7
assert sp.simplify(g6p.subs({a4: -24, b4: 7, x: 2})) == 0
assert sp.solve([4 - 4*b4 - a4, b4 - 7], [a4, b4], dict=True)[0] == {a4: -24, b4: 7}
assert not same(4 + 4*b4 - a4, 4 - 4*b4 - a4) and not same(4 - 4*b4 + a4, 4 - 4*b4 - a4)

add(6, "א",
    rubric=rub((r"נגזרת $g'(x)=\frac{x^2-2bx-a}{(x-b)^2}$", 2),
               (r"תנאי הקיצון $g'(2)=0$: $4-4b-a=0$", 2),
               (r"שיפוע האסימפטוטה $k=1$ וחותך $m=b$", 3),
               (r"מהתנאי $y=x+7$: $b=7$, ומכאן $a=-24$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לשכוח את הגורם $(x-b)^2$ במכנה של הנגזרת ולטעות בכלל המנה.",
              r"לחשב את חותך האסימפטוטה כ-$\lim g(x)$ במקום $\lim(g(x)-x)$."],
    steps=[
        chx(r"מהי הנגזרת של $g(x)=\frac{x^2+a}{x-b}$?", (x**2 - 2*b4*x - a4)/(x - b4)**2,
            [(x**2 + 2*b4*x - a4)/(x - b4)**2, (x**2 - 2*b4*x + a4)/(x - b4)**2, (x**2 - 2*b4*x - a4)/(x - b4)],
            lambda e: same(e, g6p), r"כלל המנה: $\frac{2x(x-b)-(x^2+a)}{(x-b)^2}=\frac{x^2-2bx-a}{(x-b)^2}$ (אומת ב-sympy)."),
        ch(r"איזו משוואה נובעת מקיצון מקומי ב-$x=2$?", "$4-4b-a=0$", ["$4+4b-a=0$", "$4-4b+a=0$", "$2-2b-a=0$"],
           r"$g'(2)=0$ אומר שהמונה $x^2-2bx-a$ מתאפס ב-$x=2$: $4-4b-a=0$."),
        num(r"האסימפטוטה המשופעת היא $y=kx+m$ עם $m=\lim\left(g(x)-x\right)$. מהו $b$ כאשר האסימפטוטה היא $y=x+7$?", 7,
            r"$k=1$ ו-$m=\lim\left(g(x)-x\right)=\lim\frac{bx+a}{x-b}=b$, לכן $b=7$."),
        num(r"מהו $a$?", -24, r"$a=4-4b=4-28=-24$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: area under ln(x+1)/sqrt(x+1) on [0,1] =====
g6b = sp.log(x + 1)/sp.sqrt(x + 1)
F6 = 2*sp.sqrt(x + 1)*sp.log(x + 1) - 4*sp.sqrt(x + 1)
assert same(sp.diff(F6, x), g6b)
S6 = sp.integrate(g6b, (x, 0, 1))
assert sp.simplify(S6 - (2*sp.sqrt(2)*sp.log(2) - 4*sp.sqrt(2) + 4)) == 0
F6w = [2*sp.sqrt(x + 1)*sp.log(x + 1) + 4*sp.sqrt(x + 1), sp.sqrt(x + 1)*sp.log(x + 1) - 4*sp.sqrt(x + 1), 2*sp.sqrt(x + 1)*sp.log(x + 1) - 2*sp.sqrt(x + 1)]

add(6, "ב",
    rubric=rub((r"נימוק שהפונקציה אי-שלילית בקטע, ולכן השטח הוא $\int_0^1\frac{\ln(x+1)}{\sqrt{x+1}}dx$", 2),
               (r"אינטגרציה בחלקים עם $u=\ln(x+1)$, $v=2\sqrt{x+1}$", 3),
               (r"חישוב האינטגרל הנותר $\int\frac{dx}{\sqrt{x+1}}=2\sqrt{x+1}$", 2),
               (r"הצבת הגבולות: $S=2\sqrt2\ln2-4\sqrt2+4$", 3)),
    rubricSource="ai-verified",
    pitfalls=[r"לשכוח שהשטח הוא אינטגרל של פונקציה אי-שלילית. כאן $\ln(x+1)\ge0$ בקטע, ולכן אין צורך בערך מוחלט.",
              r"לטעות ב-$v$: הקדומה של $\frac{1}{\sqrt{x+1}}$ היא $2\sqrt{x+1}$ ולא $\sqrt{x+1}$."],
    steps=[
        chx(r"מהי הפונקציה הקדומה של $\frac{1}{\sqrt{x+1}}$ ($v$ באינטגרציה בחלקים)?", 2*sp.sqrt(x + 1), [sp.sqrt(x + 1), 1/(2*sp.sqrt(x + 1)), 2*sp.sqrt(x + 1) + x],
            lambda e: same(sp.diff(e, x), 1/sp.sqrt(x + 1)), r"$\int(x+1)^{-1/2}dx=2(x+1)^{1/2}$ (נבדק בגזירה ב-sympy)."),
        chx(r"מהי הפונקציה הקדומה של $\frac{\ln(x+1)}{\sqrt{x+1}}$?", F6, F6w, lambda e: same(sp.diff(e, x), g6b),
            r"$2\sqrt{x+1}\ln(x+1)-2\int\frac{dx}{\sqrt{x+1}}=2\sqrt{x+1}\ln(x+1)-4\sqrt{x+1}$; הנגזרת של כל אפשרות נבדקה ב-sympy."),
        num(r"מהו השטח? (עשרוני)", S6, r"$S=2\sqrt2\ln2-4\sqrt2+4\approx0.3037$."),
    ],
    stepsSource="ai-verified")

exam = {
    "examCode": "20B-A",
    "examLabel": "מבחן סוף סמסטר א' תש\"פ, מועד ב'",
    "year": 2020,
    "examDate": "01/05/2020",
    "sourceFile": "calculus-1/20B-A exam+solution.pdf",
    "solutionFile": "calculus-1/20B-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

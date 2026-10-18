# -*- coding: utf-8 -*-
"""Generator for tools/raw/22B-A.json -- calculus-1 (20151), semester A 2022, moed B (22/02/2022).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22B-A.py

Source: sitting 22B-A, pp.1-2 (printed exam only, NO solution or key anywhere). Six questions, 20% each (two parts of
10%), solve 5 of 6. Parameters A, B, C (last three digits of the student's ID) appear in some parts; the header rule is
shipped as context c0.

Solutions: written by the solver (2026-10-18), solutionSource "solved", official False, confidence high. No partial
evidence exists (no key, no tutor marks). Every answer is checked in tools/verify/22B-A/check.py (sympy, 0 mismatches).
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22B-A.json"
SOL = {}


def Q(num, kind, topic, question, part=None, points=10, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "points": points, "solution": SOL[(num, part)].strip("\n"),
         "solutionSource": "solved", "official": False, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


CTX0 = (r"בחלק מסעיפי המבחן מופיעים הפרמטרים $A$, $B$ ו-$C$. חובה להציב בתחילת הפתרון לכל שאלה את ערכי הפרמטרים, "
        r"בהתאם לשלוש הספרות האחרונות של מספר תעודת הזהות שלכם: למשל עבור ת.ז. 123456789 נקבל $A=7$, $B=8$, $C=9$. "
        r"שאלות בהן $A$, $B$ ו-$C$ יוצבו רק בשלב התשובה הסופית לא ייבדקו.")


PARAM = r"הפתרון כתוב באופן כללי עבור הפרמטרים $A,B,C\in\{0,1,\dots,9\}$; במבחן מציבים אותם כבר בתחילת הפתרון." + "\n"

SOL[(1, "א")] = r"""
תחום ההגדרה: כל $\mathbb{R}$. עבור $x\neq0$:
$$f'(x)=2+3\cdot\frac{2}{3}x^{-\frac{1}{3}}=2+\frac{2}{\sqrt[3]{x}}=\frac{2\left(\sqrt[3]{x}+1\right)}{\sqrt[3]{x}}$$
נקודות חשודות לקיצון: $f'(x)=0\iff\sqrt[3]{x}=-1\iff x=-1$, ו-$x=0$ שבה הנגזרת אינה קיימת (הפונקציה רציפה שם).
טבלת סימן של $f'$:
$x<-1$: $\sqrt[3]{x}<-1$, המונה שלילי והמכנה שלילי, $f'>0$ (עולה).
$-1<x<0$: המונה חיובי והמכנה שלילי, $f'<0$ (יורדת).
$x>0$: $f'>0$ (עולה).
לכן $x=-1$ היא נקודת מקסימום מקומי, $f(-1)=-2+3=1$, ו-$x=0$ היא נקודת מינימום מקומי, $f(0)=0$ (נקודת חוד, הנגזרת אינה קיימת בה).
"""

SOL[(1, "ב")] = PARAM + r"""
נפשט את השבר באמצעות $(n+2)!=(n+2)(n+1)!$ ו-$(n+1)!=(n+1)\cdot n!$:
$$\frac{(n+2)!+(A+1)\,n\,(n+1)!}{(n+1)!-n\cdot n!}=\frac{(n+1)!\left[(n+2)+(A+1)n\right]}{n!\left[(n+1)-n\right]}=(n+1)\left((A+2)n+2\right)$$
כאשר $n\to\infty$ מתקיים $\frac{C+1}{(n+1)^2}\to0$, ולכן $\sin\frac{C+1}{(n+1)^2}=\frac{C+1}{(n+1)^2}\cdot\frac{\sin u_n}{u_n}$ עם $u_n=\frac{C+1}{(n+1)^2}$ ו-$\frac{\sin u_n}{u_n}\to1$:
$$\lim_{n\to\infty}(n+1)\left((A+2)n+2\right)\cdot\frac{C+1}{(n+1)^2}\cdot\frac{\sin u_n}{u_n}=(C+1)\lim_{n\to\infty}\frac{(A+2)n+2}{n+1}\cdot1=(A+2)(C+1)$$
"""

SOL[(2, "א")] = r"""
יהי $x>0$. הפונקציה $g(t)=\arctan t$ רציפה ב-$[0,x]$ וגזירה ב-$(0,x)$, $g'(t)=\frac{1}{1+t^2}$. לפי משפט לגרנז' קיימת $c\in(0,x)$ כך ש-
$$\arctan x-\arctan0=\frac{1}{1+c^2}\cdot x\quad\Longrightarrow\quad\arctan x=\frac{x}{1+c^2}$$
מכיוון ש-$0<c<x$ מתקיים $1<1+c^2<1+x^2$, ולכן $\frac{1}{1+x^2}<\frac{1}{1+c^2}<1$. נכפיל ב-$x>0$:
$$\frac{x}{1+x^2}<\frac{x}{1+c^2}=\arctan x<x$$
"""

SOL[(2, "ב")] = PARAM + r"""
נסמן $k=B+2\ge2$. אז $a_{n+1}=\frac{(k+1)a_n}{ka_n+1}$ ו-$a_1=C+2\ge2$.
**חסימות מלמטה:** נוכיח באינדוקציה ש-$a_n>1$. בסיס: $a_1\ge2>1$. צעד: אם $a_n>1$ אז
$$a_{n+1}-1=\frac{(k+1)a_n-ka_n-1}{ka_n+1}=\frac{a_n-1}{ka_n+1}>0$$
**מונוטוניות:** לכל $n$
$$a_{n+1}-a_n=\frac{(k+1)a_n-ka_n^2-a_n}{ka_n+1}=\frac{ka_n\left(1-a_n\right)}{ka_n+1}<0$$
כי $a_n>1$. לכן הסדרה יורדת וחסומה מלמטה, ולכן מתכנסת.
**הגבול:** נסמן $L=\lim a_n$ ונעבור לגבול בנוסחת הנסיגה:
$$L=\frac{(k+1)L}{kL+1}\ \Rightarrow\ kL^2+L=(k+1)L\ \Rightarrow\ kL(L-1)=0$$
כלומר $L=0$ או $L=1$.
מכיוון ש-$a_n>1$ לכל $n$, מתקיים $L\ge1$, ולכן $\lim_{n\to\infty}a_n=1$ (לכל ערך של $B$ ו-$C$).
"""

SOL[(3, "א")] = PARAM + r"""
תחום ההגדרה: $x\neq-A$.
**אסימפטוטה אנכית:** כאשר $x\to-A$ הגורם $x+A\to0$, והסוגריים חסומים: $1\le2+\cos\frac{B+1}{x+A}\le3$. לכן $\lim_{x\to-A}f(x)=0$ (מכפלה של שואפת ל-$0$ בחסומה), ואין אסימפטוטה אנכית.
**אסימפטוטה משופעת** $y=ax+b$ ב-$\pm\infty$: כאשר $x\to\pm\infty$, $u=\frac{B+1}{x+A}\to0$.
$$a=\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim_{x\to\pm\infty}\frac{x+A}{x}\left(2+\cos u\right)=1\cdot(2+1)=3$$
$$b=\lim_{x\to\pm\infty}\left(f(x)-3x\right)=\lim_{x\to\pm\infty}\left[(x+A)\left(\cos u-1\right)+3(x+A)-3x\right]=\lim_{x\to\pm\infty}(x+A)\left(\cos u-1\right)+3A$$
ומכיוון ש-$1-\cos u=2\sin^2\frac{u}{2}$:
$$(x+A)\left(\cos u-1\right)=-(x+A)\cdot2\sin^2\frac{u}{2}=-(B+1)\cdot\frac{\sin\frac{u}{2}}{\frac{u}{2}}\cdot\sin\frac{u}{2}\ \xrightarrow[x\to\pm\infty]{}\ -(B+1)\cdot1\cdot0=0$$
לכן $b=3A$, והישר $y=3x+3A$ הוא אסימפטוטה משופעת ב-$\pm\infty$. אין אסימפטוטות נוספות.
"""

SOL[(3, "ב")] = r"""
הצבה אוניברסלית $t=\tan\frac{x}{2}$: $\sin x=\frac{2t}{1+t^2}$, $\cos x=\frac{1-t^2}{1+t^2}$, $dx=\frac{2\,dt}{1+t^2}$.
$$1+\sin x+3\cos x=\frac{1+t^2+2t+3-3t^2}{1+t^2}=\frac{2\left(2+t-t^2\right)}{1+t^2}=\frac{2(2-t)(1+t)}{1+t^2}$$
$$\int\frac{dx}{1+\sin x+3\cos x}=\int\frac{dt}{(2-t)(1+t)}=\frac{1}{3}\int\left(\frac{1}{2-t}+\frac{1}{1+t}\right)dt=\frac{1}{3}\left(\ln|1+t|-\ln|2-t|\right)+C=$$
$$=\frac{1}{3}\ln\left|\frac{1+\tan\frac{x}{2}}{2-\tan\frac{x}{2}}\right|+C$$
"""

SOL[(4, "א")] = PARAM + r"""
נגדיר $g(x)=x^3+(C+1)x+\cos\left((C+1)x\right)-(B+1)$, רציפה וגזירה בכל $\mathbb{R}$.
**קיום:** $\cos$ חסומה, ולכן $\lim_{x\to+\infty}g(x)=+\infty$ ו-$\lim_{x\to-\infty}g(x)=-\infty$. מכאן קיימים $x_1<x_2$ עם $g(x_1)<0<g(x_2)$, ולפי משפט ערך הביניים קיים $c\in(x_1,x_2)$ עם $g(c)=0$.
**יחידות:**
$$g'(x)=3x^2+(C+1)-(C+1)\sin\left((C+1)x\right)=3x^2+(C+1)\left(1-\sin\left((C+1)x\right)\right)\ge0$$
ושוויון $g'(x)=0$ דורש גם $x=0$ וגם $\sin\left((C+1)x\right)=1$, אבל $\sin0=0$. לכן $g'(x)>0$ לכל $x$, $g$ עולה ממש, ויש לה לכל היותר שורש אחד. בסך הכל למשוואה שורש ממשי אחד בלבד.
"""

SOL[(4, "ב")] = r"""
הצבה $t=\arctan\sqrt{x}$ (עבור $x>0$): $dt=\frac{1}{1+x}\cdot\frac{1}{2\sqrt{x}}\,dx$, כלומר $\frac{dx}{(x+1)\sqrt{x}}=2\,dt$.
$$\int\frac{\arctan^3\left(\sqrt{x}\right)}{(x+1)\sqrt{x}}\,dx=\int t^3\cdot2\,dt=\frac{t^4}{2}+C=\frac{1}{2}\arctan^4\left(\sqrt{x}\right)+C$$
"""

SOL[(5, "א")] = PARAM + r"""
נסמן $D=C+1>0$. נכפיל פעמיים בצמוד:
$$\sqrt{x^2+\sqrt{x^4+D}}-x\sqrt{2}=\frac{x^2+\sqrt{x^4+D}-2x^2}{\sqrt{x^2+\sqrt{x^4+D}}+x\sqrt{2}}=\frac{\sqrt{x^4+D}-x^2}{\sqrt{x^2+\sqrt{x^4+D}}+x\sqrt{2}}=$$
$$=\frac{D}{\left(\sqrt{x^4+D}+x^2\right)\left(\sqrt{x^2+\sqrt{x^4+D}}+x\sqrt{2}\right)}$$
נחלק מונה ומכנה ב-$x^3$:
$$\lim_{x\to+\infty}\frac{\left(x^3+A\right)D}{\left(\sqrt{x^4+D}+x^2\right)\left(\sqrt{x^2+\sqrt{x^4+D}}+x\sqrt{2}\right)}=\lim_{x\to+\infty}\frac{\left(1+\frac{A}{x^3}\right)D}{\left(\sqrt{1+\frac{D}{x^4}}+1\right)\left(\sqrt{1+\sqrt{1+\frac{D}{x^4}}}+\sqrt{2}\right)}=\frac{D}{2\cdot2\sqrt{2}}$$
$$\lim_{x\to+\infty}\left(x^3+A\right)\left(\sqrt{x^2+\sqrt{x^4+C+1}}-x\sqrt{2}\right)=\frac{C+1}{4\sqrt{2}}=\frac{\sqrt{2}\,(C+1)}{8}$$
(הגבול אינו תלוי ב-$A$.)
"""

SOL[(5, "ב")] = r"""
$y'=\frac{\cos x}{\sin x}=\cot x$, ולכן $1+(y')^2=1+\cot^2x=\frac{1}{\sin^2x}$, ובקטע $\left[\frac{\pi}{3},\frac{\pi}{2}\right]$ מתקיים $\sin x>0$:
$$L=\int_{\pi/3}^{\pi/2}\frac{dx}{\sin x}=\ln\left|\tan\frac{x}{2}\right|\Big|_{\pi/3}^{\pi/2}=\ln\tan\frac{\pi}{4}-\ln\tan\frac{\pi}{6}=0-\ln\frac{1}{\sqrt{3}}=\frac{1}{2}\ln3$$
"""

SOL[(6, "א")] = r"""
תנאי הכרחי לגזירות הוא רציפות ב-$0$. עבור $x\neq0$: $f(x)=\frac{1}{\sin x}-\frac{1}{x}=\frac{x-\sin x}{x\sin x}$.
$$\lim_{x\to0}\frac{x-\sin x}{x\sin x}\left[\frac{0}{0}\right]=\lim_{x\to0}\frac{1-\cos x}{\sin x+x\cos x}\left[\frac{0}{0}\right]=\lim_{x\to0}\frac{\sin x}{2\cos x-x\sin x}=\frac{0}{2}=0$$
לכן חייב להתקיים $p=0$. עם $p=0$:
$$f'(0)=\lim_{x\to0}\frac{f(x)-0}{x}=\lim_{x\to0}\frac{x-\sin x}{x^2\sin x}=\lim_{x\to0}\frac{x-\sin x}{x^3}\cdot\frac{x}{\sin x}$$
$$\lim_{x\to0}\frac{x-\sin x}{x^3}\left[\frac{0}{0}\right]=\lim_{x\to0}\frac{1-\cos x}{3x^2}=\lim_{x\to0}\frac{2\sin^2\frac{x}{2}}{3x^2}=\frac{2}{3}\cdot\frac{1}{4}=\frac{1}{6}$$
ולכן $f$ גזירה ב-$0$ עבור $p=0$, ו-$f'(0)=\frac{1}{6}$.
"""

SOL[(6, "ב")] = PARAM + r"""
נסמן $k=B+1$. התחום הוא $0\le x\le\frac{\pi}{k}$, $0\le y\le\sin^2(kx)$, והוא מסתובב סביב ציר ה-$y$. בשיטת הקליפות הגליליות:
$$V=2\pi\int_0^{\pi/k}x\sin^2(kx)\,dx=\left[u=kx,\ dx=\frac{du}{k}\right]=\frac{2\pi}{k^2}\int_0^{\pi}u\sin^2u\,du$$
$$\int_0^{\pi}u\sin^2u\,du=\int_0^{\pi}\frac{u}{2}\,du-\frac{1}{2}\int_0^{\pi}u\cos2u\,du=\frac{\pi^2}{4}-\frac{1}{2}\left(\frac{u\sin2u}{2}\Big|_0^{\pi}-\int_0^{\pi}\frac{\sin2u}{2}\,du\right)=\frac{\pi^2}{4}-\frac{1}{2}\left(0+\frac{\cos2u}{4}\Big|_0^{\pi}\right)=\frac{\pi^2}{4}$$
$$V=\frac{2\pi}{k^2}\cdot\frac{\pi^2}{4}=\frac{\pi^3}{2(B+1)^2}$$
"""


questions = [
    Q(1, "computation", "extrema_optimization",
      r"מצאו ומיינו את כל הנקודות החשודות לקיצון מקומי של הפונקציה $f(x)=2x+3\sqrt[3]{x^2}$.", part="א"),
    Q(1, "computation", "sequences_limits",
      r"חשבו את הגבול $\lim_{n\to\infty}\frac{(n+2)!+(A+1)\,n\,(n+1)!}{(n+1)!-n\cdot n!}\sin\frac{C+1}{(n+1)^2}$.",
      part="ב", contextId="c0"),

    Q(2, "proof", "mean_value_theorems",
      r"הראו כי לכל $x>0$ מתקיים האי-שוויון $\frac{x}{1+x^2}<\arctan x<x$.", part="א"),
    Q(2, "proof", "sequences_limits",
      r"הוכיחו כי הסדרה $a_{n+1}=\frac{(B+3)a_n}{(B+2)a_n+1},\ a_1=C+2$ מתכנסת וחשבו את גבולה.",
      part="ב", contextId="c0"),

    Q(3, "computation", "function_limits",
      r"מצאו את כל האסימפטוטות לגרף הפונקציה $f(x)=(x+A)\left(2+\cos\frac{B+1}{x+A}\right)$.",
      part="א", contextId="c0"),
    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{dx}{1+\sin x+3\cos x}$.", part="ב"),

    Q(4, "proof", "continuity",
      r"הוכיחו כי למשוואה $x^3+(C+1)x+\cos\left((C+1)x\right)=B+1$ קיים שורש ממשי אחד בלבד.",
      part="א", contextId="c0"),
    Q(4, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{\arctan^3\left(\sqrt{x}\right)}{(x+1)\sqrt{x}}\,dx$.", part="ב"),

    Q(5, "computation", "function_limits",
      r"חשבו את הגבול: $\lim_{x\to+\infty}\left(x^3+A\right)\left(\sqrt{x^2+\sqrt{x^4+C+1}}-x\sqrt{2}\right)$.",
      part="א", contextId="c0"),
    Q(5, "computation", "definite_integrals",
      r"חשבו את אורך הקשת של העקומה $y=\ln(\sin x)$ בקטע $\left[\frac{\pi}{3},\frac{\pi}{2}\right]$.", part="ב"),

    Q(6, "computation", "derivatives_tangents",
      r"תהיה $f(x)=\begin{cases}\frac{1}{\sin x}-\frac{1}{x}, & x\neq0\\ p, & x=0\end{cases}$. "
      r"מצאו ערך פרמטר ממשי $p$ כך שפונקציה $f$ תהיה גזירה ב-$x=0$. מהו $f'(0)$?", part="א"),
    Q(6, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום המישורי הכלוא בין הקווים: "
      r"$y=\sin^2\left((B+1)x\right),\ y=0,\ x=0,\ x=\frac{\pi}{B+1}$ סביב ציר ה-$y$.",
      part="ב", contextId="c0"),
]



# ---- steps / rubric / pitfalls (ai-draft); every value below is computed or asserted with sympy / mpmath ----
import sympy as sp
import mpmath as mp

IDS = "abcdef"
_rot = [0]
x, t, a, b = sp.symbols('x t a b', real=True)
R = sp.Rational
mp.mp.dps = 60


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
    """choice over expressions: ok(e) must hold for the good one and fail for every distractor."""
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


def dnum(F, g, pts):
    """numeric check that F' = g at each point (F, g sympy expressions in x)"""
    return all(abs(sp.N((sp.diff(F, x) - g).subs(x, p), 30)) < 1e-15 for p in pts)


# ===== Q1a: f = 2x + 3 x^(2/3) =====
def f1r(v):
    v = mp.mpf(v)
    return 2*v + 3*mp.cbrt(v*v)

assert abs(f1r(-1) - 1) < 1e-30 and f1r(0) == 0
assert f1r(0) < f1r(mp.mpf('0.01')) and f1r(0) < f1r(mp.mpf('-0.01'))       # local min at 0
assert f1r(-1) > f1r(mp.mpf('-1.01')) and f1r(-1) > f1r(mp.mpf('-0.99'))    # local max at -1
assert same(sp.diff(2*x + 3*x**R(2, 3), x), 2 + 2/x**R(1, 3))
fp_at = lambda v: 2 + 2/(mp.sign(mp.mpf(v))*mp.cbrt(abs(mp.mpf(v))))   # real cube root
assert abs(fp_at(-R(1, 8)) + 2) < 1e-30 and abs(fp_at(8) - 3) < 1e-30 and fp_at(-1) == 0

add(1, "א",
    rubric=rub(("תחום הגדרה ונגזרת $f'(x)=2+\\frac{2}{\\sqrt[3]{x}}$ לכל $x\\neq0$", 3),
               ("נקודות חשודות: $x=-1$ (הנגזרת מתאפסת) ו-$x=0$ (הנגזרת אינה קיימת)", 2),
               ("טבלת סימן של $f'$ (עולה, יורדת, עולה)", 3),
               ("סיווג: מקסימום מקומי ב-$x=-1$ עם $f=1$ ומינימום מקומי ב-$x=0$ עם $f=0$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את $x=0$ כנקודה חשודה: הנגזרת אינה קיימת שם, אבל הפונקציה רציפה ויש בה קיצון.",
              "לחשב את $\\sqrt[3]{x}$ לא נכון עבור $x<0$ (שורש שלישי של שלילי הוא שלילי).",
              "לקבוע שאין קיצון ב-$x=0$ רק כי $f'(0)$ לא מוגדרת."],
    steps=[
        num("מהו הערך של $f'(x)=2+\\frac{2}{\\sqrt[3]{x}}$ בנקודה $x=-\\frac{1}{8}$?", -2,
            "$\\sqrt[3]{-\\frac{1}{8}}=-\\frac{1}{2}$ ולכן $f'=2+\\frac{2}{-1/2}=-2$. הנגזרת שלילית ב-$(-1,0)$."),
        num("באיזה ערך שלילי של $x$ מתאפסת הנגזרת $f'(x)=2+\\frac{2}{\\sqrt[3]{x}}$?", -1,
            "$\\sqrt[3]{x}=-1$ ולכן $x=-1$."),
        num("מהו $f(-1)$ עבור $f(x)=2x+3\\sqrt[3]{x^2}$?", 1, "$f(-1)=-2+3=1$ (נבדק מספרית)."),
        ch("מהו סוג הנקודה $x=0$?", "מינימום מקומי (הנגזרת אינה קיימת שם)",
           ["מקסימום מקומי", "אינה נקודת קיצון כי $f'(0)$ אינה קיימת"],
           "$f(0)=0$ קטנה מ-$f(\\pm0.01)$ (נבדק מספרית), ו-$f'$ משנה סימן משלילית לחיובית ב-$0$."),
    ],
    stepsSource="ai-verified")

# ===== Q1b: factorial limit =====
nn = sp.Symbol('nn', positive=True, integer=True)
Aa = sp.Symbol('Aa')
frac1 = (sp.factorial(nn + 2) + (Aa + 1)*nn*sp.factorial(nn + 1))/(sp.factorial(nn + 1) - nn*sp.factorial(nn))
for nv in (2, 5, 9):
    for av in (0, 3, 9):
        assert sp.simplify(frac1.subs({nn: nv, Aa: av}) - (nv + 1)*((av + 2)*nv + 2)) == 0
assert frac1.subs({nn: 4, Aa: 3}) == 110
for av in (0, 3, 9):
    for cv in (0, 1, 7):
        N_ = mp.mpf(10)**6
        val = (N_ + 1)*((av + 2)*N_ + 2)*mp.sin(mp.mpf(cv + 1)/(N_ + 1)**2)
        assert abs(val - (av + 2)*(cv + 1)) < 1e-4, (av, cv, val)

add(1, "ב",
    rubric=rub(("פישוט עצרות: $(n+2)!=(n+2)(n+1)!$ ו-$(n+1)!=(n+1)\\cdot n!$", 3),
               ("קבלת הצורה $(n+1)\\left((A+2)n+2\\right)$ לאחר צמצום", 3),
               ("שימוש ב-$\\sin u_n\\sim u_n$ כאשר $u_n\\to0$", 2),
               ("חישוב הגבול $(A+2)(C+1)$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לצמצם עצרות בלי להוציא גורם משותף: $(n+2)!-(n+1)!$ אינו $1!$.",
              "להשאיר את הביטוי כ-$\\infty\\cdot0$ בלי להחליף את $\\sin u_n$ ב-$u_n$ (גבול מפורסם).",
              "לשכוח את הגורם $C+1$ שמגיע מהארגומנט של הסינוס."],
    steps=[
        num("עבור $A=3$ ו-$n=4$, מהו ערך השבר $\\frac{(n+2)!+(A+1)\\,n\\,(n+1)!}{(n+1)!-n\\cdot n!}$?", 110,
            "מתקבל $(n+1)\\left((A+2)n+2\\right)=5\\cdot22=110$ (נבדק ישירות עם עצרות)."),
        ch("לאיזו צורה מצטמצם השבר אחרי הוצאת $(n+1)!$ מהמונה ו-$n!$ מהמכנה?",
           "$(n+1)\\left((A+2)n+2\\right)$",
           ["$(n+1)\\left((A+1)n+2\\right)$", "$\\left((A+2)n+2\\right)$", "$(n+2)(A+2)n$"],
           "המונה $(n+1)!\\left[(n+2)+(A+1)n\\right]=(n+1)!\\left[(A+2)n+2\\right]$ והמכנה $n!$, ולכן השבר $(n+1)\\left((A+2)n+2\\right)$ (נבדק לכמה ערכי $A,n$)."),
        num("עבור $A=3$ ו-$C=1$, מהו הגבול? (עשרוני)", 10,
            "$(n+1)(5n+2)\\cdot\\frac{2}{(n+1)^2}\\to5\\cdot2=10$, בכלליות: $(A+2)(C+1)$ (נבדק מספרית עם $n=10^6$)."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: Lagrange for arctan =====
for cv in (R(1, 2), R(3, 4)):
    assert 1/(1 + 1**2) < 1/(1 + cv**2) < 1 and not (1 < 1/(1 + cv**2))
L2a = ["לפי משפט לגרנז' על $\\arctan t$ בקטע $[0,x]$ קיימת $c\\in(0,x)$ כך ש-$\\arctan x=\\frac{x}{1+c^2}$.",
       "מכיוון ש-$0<c<x$ מתקיים $1<1+c^2<1+x^2$.",
       "לכן $\\frac{1}{1+x^2}<\\frac{1}{1+c^2}<1$.",
       "נכפול ב-$x>0$ ונקבל $\\frac{x}{1+x^2}<\\arctan x<x$."]
L2a_b = list(L2a)
L2a_b[2] = "לכן $1<\\frac{1}{1+c^2}<\\frac{1}{1+x^2}$."

add(2, "א",
    rubric=rub(("הפעלת משפט לגרנז' על $\\arctan t$ בקטע $[0,x]$ ובדיקת התנאים", 3),
               ("קבלת $\\arctan x=\\frac{x}{1+c^2}$ עם $c\\in(0,x)$", 2),
               ("חסימת $1+c^2$ בין $1$ ל-$1+x^2$ והיפוך לשברים", 3),
               ("כפל ב-$x>0$ ומסקנת אי-השוויון", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח להפוך את כיוון האי-שוויון בעת מעבר להופכי $\\frac{1}{1+c^2}$.",
              "להפעיל את המשפט על $[0,1]$ במקום על $[0,x]$, ואז לא מתקבל אי-שוויון התלוי ב-$x$.",
              "לכפול ב-$x$ בלי לציין ש-$x>0$."],
    steps=[
        ch("לאיזו פונקציה ולאיזה קטע מפעיל הפתרון את משפט לגרנז'?",
           "$g(t)=\\arctan t$ בקטע $[0,x]$",
           ["$g(t)=\\frac{t}{1+t^2}$ בקטע $[0,x]$", "$g(t)=\\arctan t$ בקטע $[0,1]$", "$g(t)=\\arctan t-t$ בקטע $[0,x]$"],
           "הפתרון מציב $\\arctan x-\\arctan0=g'(c)\\cdot x$ כאשר $g=\\arctan$ והקטע $[0,x]$."),
        num("מהו $g'(1)$ עבור $g(t)=\\arctan t$?", R(1, 2), "$g'(t)=\\frac{1}{1+t^2}$ ולכן $g'(1)=\\frac{1}{2}$."),
        order("סדרו את שלבי ההוכחה.", L2a,
              "כל שלב נשען על קודמו: משפט לגרנז', חסימת $c$, הופכי, כפל ב-$x$."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L2a_b, 2,
                "ההופכי של $1<1+c^2<1+x^2$ הוא $\\frac{1}{1+x^2}<\\frac{1}{1+c^2}<1$, לא $1<\\frac{1}{1+c^2}$ (למשל $c=0.5$ נותן $0.8<1$)."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: recursive sequence a_{n+1}=(k+1)a_n/(k a_n+1) =====
kk, an = sp.symbols('kk an', positive=True)
step = (kk + 1)*an/(kk*an + 1)
assert same(step - 1, (an - 1)/(kk*an + 1)) and same(step - an, kk*an*(1 - an)/(kk*an + 1))
assert set(sp.solve(sp.Eq(a, (kk + 1)*a/(kk*a + 1)), a)) == {0, 1}
a2_k2 = step.subs({kk: 2, an: 2})
assert a2_k2 == R(6, 5)
seq = mp.mpf(3)
for _ in range(200):
    seq = 4*seq/(3*seq + 1)
assert abs(seq - 1) < 1e-20                        # k=3, a1=3 converges to 1
d2 = (step - 1).subs({kk: 2, an: 3})
assert d2 == R(2, 7)
L2b = ["נוכיח באינדוקציה ש-$a_n>1$: $a_1\\ge2>1$, ואם $a_n>1$ אז $a_{n+1}-1=\\frac{a_n-1}{ka_n+1}>0$.",
       "לכל $n$ מתקיים $a_{n+1}-a_n=\\frac{ka_n\\left(1-a_n\\right)}{ka_n+1}<0$, ולכן הסדרה יורדת.",
       "סדרה יורדת וחסומה מלמטה מתכנסת, נסמן את גבולה $L$.",
       "מנוסחת הנסיגה $kL(L-1)=0$, ומכיוון ש-$a_n>1$ מתקבל $L=1$."]

add(2, "ב",
    rubric=rub(("חסימה מלמטה $a_n>1$ באינדוקציה (בסיס וצעד)", 3),
               ("מונוטוניות: $a_{n+1}-a_n<0$", 3),
               ("מסקנת ההתכנסות (יורדת וחסומה)", 1),
               ("משוואת הגבול $kL(L-1)=0$ ובחירת $L=1$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לבחור $L=0$ מבלי לבדוק שהסדרה חסומה מלמטה על ידי $1$.",
              "להוכיח מונוטוניות לפני שהוכחה החסימה: הסימן של $a_{n+1}-a_n$ תלוי ב-$a_n>1$.",
              "להשתמש בגבול הסדרה בנוסחת הנסיגה לפני שהוכחה התכנסות."],
    steps=[
        num("עבור $B=0$ (כלומר $k=2$) ו-$a_1=2$, מהו $a_2$? (עשרוני)", a2_k2,
            "$a_2=\\frac{3\\cdot2}{2\\cdot2+1}=\\frac{6}{5}=1.2$."),
        num("עבור $k=2$ ו-$a_n=3$, מהו $a_{n+1}-1=\\frac{a_n-1}{ka_n+1}$? (עשרוני)", d2,
            "$\\frac{3-1}{2\\cdot3+1}=\\frac{2}{7}\\approx0.2857>0$, בהתאם לכך ש-$a_n>1$ נשמר."),
        ch("מהו גבול הסדרה?", "$1$",
           ["$0$", "$k$", "$a_1$"],
           "נקודות השבת הן $L=0$ ו-$L=1$; מכיוון ש-$a_n>1$ לכל $n$, $L\\ge1$ ולכן $L=1$ (נבדק מספרית עם $k=3$, $a_1=3$)."),
        order("סדרו את שלבי ההוכחה.", L2b,
              "חסימה קודמת למונוטוניות, שתיהן קודמות להתכנסות, וההתכנסות קודמת למעבר לגבול."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: asymptotes of (x+A)(2+cos((B+1)/(x+A))) =====
def f3(av, bv):
    return lambda v: (v + av)*(2 + mp.cos(mp.mpf(bv + 1)/(v + av)))

for av, bv in ((0, 0), (2, 1), (7, 9)):
    ff = f3(av, bv)
    assert abs(ff(-av + mp.mpf('1e-12'))) < 1e-9 and abs(ff(-av - mp.mpf('1e-12'))) < 1e-9     # limit 0 at -A
    for X in (mp.mpf(10)**9, -mp.mpf(10)**9):
        assert abs(ff(X)/X - 3) < 1e-6 and abs(ff(X) - 3*X - 3*av) < 1e-6                         # y=3x+3A

add(3, "א",
    rubric=rub(("תחום הגדרה $x\\neq-A$ ובדיקת $x\\to-A$: הגבול הוא $0$, ללא אסימפטוטה אנכית", 3),
               ("שיפוע האסימפטוטה המשופעת $a=3$", 2),
               ("חישוב $b=3A$ בעזרת $1-\\cos u=2\\sin^2\\frac{u}{2}$", 4),
               ("מסקנה: $y=3x+3A$ ב-$\\pm\\infty$, ואין אסימפטוטות נוספות", 1)),
    rubricSource="ai-verified",
    pitfalls=["להכריז על $x=-A$ כאסימפטוטה אנכית רק כי הפונקציה אינה מוגדרת שם. צריך לבדוק שהגבול אינו סופי.",
              "לטעות בגבול $\\cos u\\to1$ ולכתוב $a=2$ במקום $a=3$.",
              "לשכוח את $3A$ בחישוב $b$, אחרי הוצאת $(x+A)$ כגורם משותף."],
    steps=[
        ch("מה קורה ל-$f$ כאשר $x\\to-A$?", "$f\\to0$ ולכן אין אסימפטוטה אנכית",
           ["$f\\to\\infty$ ולכן $x=-A$ אסימפטוטה אנכית", "אין גבול כי הקוסינוס מתנדנד, ולכן $x=-A$ אסימפטוטה אנכית",
            "$f\\to3$ ולכן יש שם אסימפטוטה אופקית"],
           "הגורם $x+A\\to0$ והסוגריים בין $1$ ל-$3$, ולכן המכפלה שואפת ל-$0$ (נבדק מספרית)."),
        num("מהו השיפוע $a=\\lim\\frac{f(x)}{x}$ של האסימפטוטה המשופעת?", 3,
            "כאשר $x\\to\\pm\\infty$, $\\cos\\frac{B+1}{x+A}\\to1$ ולכן $a=2+1=3$."),
        num("עבור $A=2$, מהו $b$ באסימפטוטה $y=3x+b$?", 6,
            "$b=3A=6$ (נבדק מספרית עבור כמה ערכי $A,B$)."),
        ch("מהי האסימפטוטה המשופעת של $f$ ב-$\\pm\\infty$?", "$y=3x+3A$",
           ["$y=3x+A$", "$y=3x$", "$y=2x+3A$"],
           "$a=3$, $b=\\lim\\left[(x+A)(\\cos u-1)\\right]+3A=0+3A$ (נבדק מספרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: universal substitution =====
tt = sp.Symbol('tt')
den3 = 1 + 2*tt/(1 + tt**2) + 3*(1 - tt**2)/(1 + tt**2)
assert same(den3, 2*(2 - tt)*(1 + tt)/(1 + tt**2))
assert same(R(1, 3)*(1/(2 - tt) + 1/(1 + tt)), 1/((2 - tt)*(1 + tt)))
g3 = 1/(1 + sp.sin(x) + 3*sp.cos(x))
Fgood = R(1, 3)*sp.log((1 + sp.tan(x/2))/(2 - sp.tan(x/2)))
Fbads = [R(1, 3)*sp.log((2 - sp.tan(x/2))/(1 + sp.tan(x/2))),
         R(1, 2)*sp.log((1 + sp.tan(x/2))/(2 - sp.tan(x/2))),
         R(1, 3)*sp.log((1 + sp.tan(x/2))*(2 - sp.tan(x/2)))]
pts3 = [R(3, 10), 1, R(1, 2)]
assert dnum(Fgood, g3, pts3) and not any(dnum(e, g3, pts3) for e in Fbads)

add(3, "ב",
    rubric=rub(("הצבה $t=\\tan\\frac{x}{2}$ והצגת $\\sin x$, $\\cos x$, $dx$", 2),
               ("פישוט המכנה ל-$\\frac{2(2-t)(1+t)}{1+t^2}$ וצמצום ל-$\\int\\frac{dt}{(2-t)(1+t)}$", 3),
               ("פירוק לשברים חלקיים ואינטגרציה", 3),
               ("הצבה חזרה והתוצאה הסופית", 2)),
    rubricSource="ai-verified",
    pitfalls=["לטעות בנוסחאות ההצבה האוניברסלית, כגון $dx=\\frac{2\\,dt}{1+t^2}$.",
              "לשכוח את הגורם $\\frac{1}{3}$ בפירוק $\\frac{1}{(2-t)(1+t)}=\\frac{1}{3}\\left(\\frac{1}{2-t}+\\frac{1}{1+t}\\right)$.",
              "לשכוח לחזור למשתנה $x$ בסוף."],
    steps=[
        ch("איזו הצבה משתמש הפתרון כדי לחשב את האינטגרל?", "$t=\\tan\\frac{x}{2}$",
           ["$t=\\sin x$", "$t=\\cos x$", "$t=\\tan x$"],
           "האינטגרנד רציונלי ב-$\\sin x,\\cos x$ ולכן ההצבה האוניברסלית $t=\\tan\\frac{x}{2}$ מורידה אותו לשבר רציונלי."),
        num("מהו המקדם $c$ בפירוק $\\frac{1}{(2-t)(1+t)}=c\\left(\\frac{1}{2-t}+\\frac{1}{1+t}\\right)$? (עשרוני)", R(1, 3),
            "$\\frac{1}{2-t}+\\frac{1}{1+t}=\\frac{3}{(2-t)(1+t)}$ ולכן $c=\\frac{1}{3}$ (sympy)."),
        ch("איזו קדומה נכונה? (בתחום שבו הביטוי בתוך הלוגריתם חיובי)", T(Fgood),
           [T(e) for e in Fbads],
           "הנגזרת של $\\frac{1}{3}\\ln\\frac{1+\\tan\\frac{x}{2}}{2-\\tan\\frac{x}{2}}$ שווה לאינטגרנד; לשלוש האפשרויות האחרות הנגזרת שונה (נבדק מספרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: unique real root =====
def g4(cv, bv):
    return lambda v: v**3 + (cv + 1)*v + mp.cos((cv + 1)*v) - (bv + 1)

def g4p(cv):
    return lambda v: 3*v**2 + (cv + 1) - (cv + 1)*mp.sin((cv + 1)*v)

for cv in range(10):
    dd = g4p(cv)
    h = mp.diff(g4(cv, 0), mp.mpf('0.37'))
    assert abs(h - dd(mp.mpf('0.37'))) < 1e-20
    assert min(dd(mp.mpf(k)/20) for k in range(-400, 401)) > 0
assert abs(g4(0, 1)(1) - mp.cos(1)) < 1e-30 and g4(0, 1)(0) == -1
assert g4p(1)(0) == 2
L4a = ["נגדיר $g(x)=x^3+(C+1)x+\\cos\\left((C+1)x\\right)-(B+1)$; הפונקציה רציפה בכל $\\mathbb{R}$.",
       "$g'(x)=3x^2+(C+1)-(C+1)\\sin\\left((C+1)x\\right)$.",
       "$g'(x)=3x^2+(C+1)\\left(1-\\sin\\left((C+1)x\\right)\\right)>0$ לכל $x$, ולכן $g$ עולה ממש.",
       "$g\\to\\pm\\infty$ כאשר $x\\to\\pm\\infty$, ולפי ערך הביניים יש שורש, ועלייה ממש נותנת שורש יחיד."]
L4a_b = list(L4a)
L4a_b[1] = "$g'(x)=3x^2+(C+1)+(C+1)\\sin\\left((C+1)x\\right)$."
assert sp.simplify(sp.diff(sp.cos(a*x), x) + a*sp.sin(a*x)) == 0

add(4, "א",
    rubric=rub(("הגדרת $g$ ורציפותה", 1),
               ("קיום שורש: גבולות $\\pm\\infty$ ומשפט ערך הביניים", 3),
               ("נגזרת $g'(x)=3x^2+(C+1)\\left(1-\\sin((C+1)x)\\right)$", 2),
               ("הוכחת $g'>0$ (שוויון דורש $x=0$ ו-$\\sin=1$ בו-זמנית)", 2),
               ("מסקנה: עלייה ממש, ולכן שורש יחיד", 2)),
    rubricSource="ai-verified",
    pitfalls=["להסתפק בכך ש-$g'\\ge0$ בלי להראות שהשוויון אינו מתקיים אף פעם, כדי לקבל עלייה ממש.",
              "טעות סימן בנגזרת של $\\cos\\left((C+1)x\\right)$: היא $-(C+1)\\sin\\left((C+1)x\\right)$.",
              "לא להראות קיום: מונוטוניות לבדה לא מבטיחה שורש."],
    steps=[
        num("עבור $B=1$ ו-$C=0$ מתקבל $g(x)=x^3+x+\\cos x-2$. מהו $g(1)$? (עשרוני)", mp.cos(1),
            "$g(1)=1+1+\\cos1-2=\\cos1\\approx0.5403>0$ ו-$g(0)=-1<0$, ולכן יש שורש בקטע $(0,1)$ (נבדק מספרית)."),
        num("עבור $C=1$, מהו $g'(0)$?", 2, "$g'(0)=0+2\\left(1-\\sin0\\right)=2$ (נבדק מספרית)."),
        ch("מהו סימן $g'(x)$?", "חיובי ממש לכל $x$",
           ["אי-שלילי, ומתאפס בנקודה אחת לפחות", "משנה סימן, ולכן יש כמה שורשים", "שלילי לכל $x$"],
           "$g'=3x^2+(C+1)(1-\\sin(\\cdot))\\ge0$, והשוויון דורש $x=0$ וגם $\\sin0=1$, בלתי אפשרי. המינימום על רשת צפופה חיובי לכל $C=0..9$ (נבדק מספרית)."),
        findbug("בפתרון הבא שורה אחת שגויה. מצאו אותה.", L4a_b, 1,
                "הנגזרת של $\\cos\\left((C+1)x\\right)$ היא $-(C+1)\\sin\\left((C+1)x\\right)$, לא $+$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: int arctan^3(sqrt x)/((x+1) sqrt x) =====
g4b = sp.atan(sp.sqrt(x))**3/((x + 1)*sp.sqrt(x))
F4b = sp.atan(sp.sqrt(x))**4/2
pts4 = [R(1, 3), 2, 5]
assert dnum(F4b, g4b, pts4)
F4b_bads = [sp.atan(sp.sqrt(x))**4/4, sp.atan(sp.sqrt(x))**4, sp.atan(sp.sqrt(x))**3/3]
assert not any(dnum(e, g4b, pts4) for e in F4b_bads)
assert same(sp.diff(sp.atan(sp.sqrt(x)), x)*2, 1/((x + 1)*sp.sqrt(x)))
q4b = mp.quad(lambda v: mp.atan(mp.sqrt(v))**3/((v + 1)*mp.sqrt(v)), [0, 1])
assert abs(q4b - (mp.atan(1)**4)/2) < 1e-25

add(4, "ב",
    rubric=rub(("הצבה $t=\\arctan\\sqrt{x}$", 3),
               ("חישוב $dt$ והמעבר $\\frac{dx}{(x+1)\\sqrt{x}}=2\\,dt$", 3),
               ("אינטגרל $\\int2t^3dt=\\frac{t^4}{2}$", 2),
               ("הצבה חזרה בתוצאה", 2)),
    rubricSource="ai-verified",
    pitfalls=["לגזור את $\\arctan\\sqrt{x}$ בלי כלל השרשרת: $\\frac{1}{1+x}\\cdot\\frac{1}{2\\sqrt{x}}$.",
              "לשכוח את הגורם $2$ שמגיע מ-$dx=2(x+1)\\sqrt{x}\\,dt$.",
              "לכתוב $\\frac{t^4}{4}$ במקום $\\frac{t^4}{2}$."],
    steps=[
        ch("איזו הצבה משתמש הפתרון?", "$t=\\arctan\\sqrt{x}$",
           ["$t=\\sqrt{x}$", "$t=x+1$", "$t=\\arctan x$"],
           "הנגזרת של $\\arctan\\sqrt{x}$ היא $\\frac{1}{2(x+1)\\sqrt{x}}$, כלומר בדיוק הגורם שנשאר באינטגרנד."),
        num("אם $dt=\\frac{dx}{2(x+1)\\sqrt{x}}$, מהו המקדם $c$ ב-$\\frac{dx}{(x+1)\\sqrt{x}}=c\\,dt$?", 2,
            "$dx=2(x+1)\\sqrt{x}\\,dt$ ולכן $c=2$ (נבדק ב-sympy)."),
        chx("איזו קדומה נכונה?", F4b, F4b_bads, lambda e: dnum(e, g4b, pts4),
            "$\\int2t^3dt=\\frac{t^4}{2}$; הנגזרת של כל אחת מהאפשרויות האחרות שונה מהאינטגרנד (נבדק מספרית)."),
        num("מהו הערך של $\\int_0^1\\frac{\\arctan^3\\sqrt{x}}{(x+1)\\sqrt{x}}dx$? (עשרוני)", mp.atan(1)**4/2,
            "$\\frac{1}{2}\\left(\\frac{\\pi}{4}\\right)^4\\approx0.1903$ (נבדק באינטגרציה נומרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q5a: double conjugate limit =====
def lim5(av, cv, X):
    X = mp.mpf(X)
    return (X**3 + av)*(mp.sqrt(X**2 + mp.sqrt(X**4 + cv + 1)) - X*mp.sqrt(2))

for av in (0, 5, 9):
    for cv in (0, 3, 9):
        assert abs(lim5(av, cv, mp.mpf(10)**8) - (cv + 1)*mp.sqrt(2)/8) < 1e-6, (av, cv)
Xv = mp.mpf('3.7'); Dv = 4
assert abs((mp.sqrt(Xv**2 + mp.sqrt(Xv**4 + Dv)) - Xv*mp.sqrt(2)) -
           Dv/((mp.sqrt(Xv**4 + Dv) + Xv**2)*(mp.sqrt(Xv**2 + mp.sqrt(Xv**4 + Dv)) + Xv*mp.sqrt(2)))) < 1e-40
L5a = ["נכפול ונחלק בצמוד של $\\sqrt{x^2+\\sqrt{x^4+D}}-x\\sqrt{2}$ ונקבל מונה $\\sqrt{x^4+D}-x^2$.",
       "נכפול ונחלק בצמוד פעם שנייה: המונה הופך ל-$D$ והמכנה למכפלה $\\left(\\sqrt{x^4+D}+x^2\\right)\\left(\\sqrt{x^2+\\sqrt{x^4+D}}+x\\sqrt{2}\\right)$.",
       "נחלק מונה ומכנה ב-$x^3$ ונעבור לגבול: $\\frac{D}{2\\cdot2\\sqrt{2}}=\\frac{\\sqrt{2}\\,(C+1)}{8}$."]

add(5, "א",
    rubric=rub(("הכפלה בצמוד ראשונה והמונה $\\sqrt{x^4+D}-x^2$", 2),
               ("הכפלה בצמוד שנייה והמונה $D=C+1$", 3),
               ("חלוקה ב-$x^3$ ושליפת גבולות הגורמים", 2),
               ("ערך הגבול $\\frac{C+1}{4\\sqrt{2}}=\\frac{\\sqrt{2}(C+1)}{8}$ ואי-התלות ב-$A$", 3)),
    rubricSource="ai-verified",
    pitfalls=["להשאיר צורה לא מוגדרת $\\infty\\cdot0$ בלי להכפיל בצמוד.",
              "להכפיל בצמוד פעם אחת בלבד: נשאר הפרש $\\sqrt{x^4+D}-x^2$ מסוג $\\infty-\\infty$.",
              "לחשוב שהגבול תלוי ב-$A$; $A$ משפיע רק על סדר גודל נמוך ושואף לאפס אחרי החלוקה."],
    steps=[
        ch("איזו שיטה משתמש הפתרון לחישוב הגבול?", "הכפלה בצמוד פעמיים ואז חלוקה ב-$x^3$",
           ["לופיטל על $x^3$", "הצבת $x=\\frac{1}{u}$ ופיתוח טיילור מסדר ראשון בלבד", "קריטריון השוואה (סנדוויץ')"],
           "הביטוי הוא $\\infty\\cdot0$ עם שני שורשים מקוננים, והפתרון מכפיל בצמוד פעמיים (השוויון נבדק מספרית)."),
        num("עבור $C=3$ (כלומר $D=4$), מהו המונה שמתקבל אחרי שתי ההכפלות בצמוד?", 4, "המונה הוא $D=C+1=4$."),
        num("מהו הגבול של גורם המכנה $\\left(\\sqrt{1+\\frac{D}{x^4}}+1\\right)\\left(\\sqrt{1+\\sqrt{1+\\frac{D}{x^4}}}+\\sqrt{2}\\right)$ כאשר $x\\to\\infty$? (עשרוני)",
            4*sp.sqrt(2), "$2\\cdot2\\sqrt{2}=4\\sqrt{2}\\approx5.657$."),
        num("עבור $C=3$, מהו ערך הגבול? (עשרוני)", 4*sp.sqrt(2)/8,
            "$\\frac{\\sqrt{2}(C+1)}{8}=\\frac{4\\sqrt{2}}{8}\\approx0.7071$ (נבדק מספרית ב-$x=10^8$, לכמה ערכי $A$)."),
        order("סדרו את שלבי החישוב.", L5a, "כל שלב משתמש בביטוי שהתקבל בקודם."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: arc length of ln(sin x) =====
yy = sp.log(sp.sin(x))
assert same(1 + sp.diff(yy, x)**2, 1/sp.sin(x)**2)
Larc = mp.quad(lambda v: mp.sqrt(1 + mp.cot(v)**2), [mp.pi/3, mp.pi/2])
assert abs(Larc - mp.log(3)/2) < 1e-25
assert abs(mp.log(mp.tan(mp.pi/6)) + mp.log(3)/2) < 1e-30

add(5, "ב",
    rubric=rub(("נוסחת אורך קשת $\\int\\sqrt{1+(y')^2}dx$ והנגזרת $y'=\\cot x$", 2),
               ("פישוט $1+\\cot^2x=\\frac{1}{\\sin^2x}$ והוצאת שורש", 3),
               ("האינטגרל $\\int\\frac{dx}{\\sin x}=\\ln\\left|\\tan\\frac{x}{2}\\right|$", 3),
               ("הצבת הגבולות והתוצאה $\\frac{1}{2}\\ln3$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח שהשורש של $\\frac{1}{\\sin^2x}$ הוא $\\frac{1}{|\\sin x|}$ (כאן $\\sin x>0$).",
              "לטעות בקדומה של $\\frac{1}{\\sin x}$: היא $\\ln\\left|\\tan\\frac{x}{2}\\right|$ ולא $-\\ln|\\cos x|$.",
              "להציב $\\tan\\frac{\\pi}{3}$ במקום $\\tan\\frac{\\pi}{6}$ בגבול התחתון."],
    steps=[
        num("מהו $y'\\left(\\frac{\\pi}{3}\\right)$ עבור $y=\\ln(\\sin x)$? (עשרוני)", 1/sp.sqrt(3), "$y'=\\cot x$ ו-$\\cot\\frac{\\pi}{3}=\\frac{1}{\\sqrt{3}}\\approx0.5774$."),
        ch("מהו $1+(y')^2$?", "$\\frac{1}{\\sin^2x}$", ["$\\frac{1}{\\cos^2x}$", "$1+\\sin^2x$", "$\\cot^2x$"],
           "$1+\\cot^2x=\\frac{1}{\\sin^2x}$ (נבדק ב-sympy)."),
        num("מהו $\\ln\\tan\\frac{\\pi}{6}$? (עשרוני)", -sp.log(3)/2, "$\\tan\\frac{\\pi}{6}=\\frac{1}{\\sqrt{3}}$ ולכן $\\ln\\tan\\frac{\\pi}{6}=-\\frac{1}{2}\\ln3\\approx-0.5493$."),
        num("מהו אורך הקשת? (עשרוני)", sp.log(3)/2, "$0-\\left(-\\frac{1}{2}\\ln3\\right)=\\frac{1}{2}\\ln3\\approx0.5493$ (נבדק באינטגרציה נומרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: differentiability at 0 =====
f6 = lambda v: 1/mp.sin(v) - 1/v
assert abs(f6(mp.mpf('1e-15'))) < 1e-14
assert abs((mp.mpf('1e-6') - mp.sin(mp.mpf('1e-6')))/mp.mpf('1e-6')**3 - mp.mpf(1)/6) < 1e-10
assert abs(f6(mp.mpf('1e-4'))/mp.mpf('1e-4') - mp.mpf(1)/6) < 1e-6
assert sp.limit(1/sp.sin(x) - 1/x, x, 0) == 0 and sp.limit((x - sp.sin(x))/x**3, x, 0) == R(1, 6)

add(6, "א",
    rubric=rub(("תנאי הכרחי: רציפות ב-$0$", 2),
               ("חישוב $\\lim_{x\\to0}\\left(\\frac{1}{\\sin x}-\\frac{1}{x}\\right)=0$ ולכן $p=0$", 3),
               ("הצבה בהגדרת הנגזרת $\\lim\\frac{f(x)-f(0)}{x}$", 2),
               ("חישוב $\\lim\\frac{x-\\sin x}{x^3}=\\frac{1}{6}$ ו-$f'(0)=\\frac{1}{6}$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לדלג על בדיקת הרציפות ולהניח ש-$p$ חופשי.",
              "להפעיל לופיטל על הפרש $\\frac{1}{\\sin x}-\\frac{1}{x}$ לפני שהופכים אותו למנה.",
              "לשכוח את הגורם $\\frac{x}{\\sin x}\\to1$ בעת הצבה בהגדרת הנגזרת."],
    steps=[
        num("מהו $\\lim_{x\\to0}\\left(\\frac{1}{\\sin x}-\\frac{1}{x}\\right)$?", 0,
            "$\\frac{x-\\sin x}{x\\sin x}\\to\\frac{0}{0}$ ועם לופיטל פעמיים מתקבל $0$ (sympy)."),
        ch("מדוע חייב להתקיים $p=0$?", "גזירות ב-$0$ מחייבת רציפות, והגבול של $f$ כש-$x\\to0$ הוא $0$",
           ["כי $f'(0)=p$", "כי הגבול של $f$ כש-$x\\to0$ הוא $\\frac{1}{6}$", "כי $f$ זוגית"],
           "הגבול הוא $0$ (לא $\\frac{1}{6}$), ורציפות מחייבת $p=f(0)=0$."),
        num("מהו $\\lim_{x\\to0}\\frac{x-\\sin x}{x^3}$? (עשרוני)", R(1, 6), "לופיטל פעמיים או פיתוח טיילור: $\\frac{1}{6}\\approx0.1667$ (sympy)."),
        num("מהו $f'(0)$? (עשרוני)", R(1, 6), "$f'(0)=\\lim\\frac{x-\\sin x}{x^3}\\cdot\\frac{x}{\\sin x}=\\frac{1}{6}\\cdot1$ (נבדק מספרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: shells volume =====
def vol6(k):
    return 2*mp.pi*mp.quad(lambda v: v*mp.sin(k*v)**2, [0, mp.pi/k])

for B_ in range(10):
    assert abs(vol6(B_ + 1) - mp.pi**3/(2*(B_ + 1)**2)) < 1e-25
assert abs(mp.quad(lambda u: u*mp.sin(u)**2, [0, mp.pi]) - mp.pi**2/4) < 1e-25

add(6, "ב",
    rubric=rub(("זיהוי שיטת הקליפות הגליליות: $V=2\\pi\\int x\\,y\\,dx$", 2),
               ("קביעת גבולות האינטגרציה $\\left[0,\\frac{\\pi}{B+1}\\right]$ ואינטגרנד $x\\sin^2\\left((B+1)x\\right)$", 2),
               ("הצבה $u=(B+1)x$ ואינטגרציה בחלקים: $\\int_0^\\pi u\\sin^2u\\,du=\\frac{\\pi^2}{4}$", 4),
               ("נפח סופי $V=\\frac{\\pi^3}{2(B+1)^2}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להשתמש בשיטת הטבעות סביב ציר $y$: התחום אינו מתואר בנוחות כפונקציה של $y$.",
              "לשכוח את הגורם $\\frac{1}{k^2}$ מההצבה $u=kx$ (גם $x=\\frac{u}{k}$ וגם $dx=\\frac{du}{k}$).",
              "לשכוח את $2\\pi$ בנוסחת הקליפות."],
    steps=[
        ch("באיזו שיטה משתמש הפתרון לחישוב הנפח?", "שיטת הקליפות הגליליות",
           ["שיטת הטבעות (חתכים) סביב ציר $y$", "משפט פפוס בלבד, בלי אינטגרל"],
           "הסיבוב סביב ציר $y$ של תחום מתחת לגרף של $y(x)$ נותן קליפות: $V=2\\pi\\int_0^{\\pi/k}x\\sin^2(kx)\\,dx$."),
        num("מהו $\\int_0^{\\pi}u\\sin^2u\\,du$? (עשרוני)", mp.pi**2/4, "$\\frac{\\pi^2}{4}\\approx2.4674$ (נבדק באינטגרציה נומרית)."),
        num("עבור $B=1$ (כלומר $k=2$), מהו הנפח $V=\\frac{2\\pi}{k^2}\\cdot\\frac{\\pi^2}{4}$? (עשרוני)", mp.pi**3/8,
            "$V=\\frac{\\pi^3}{2(B+1)^2}=\\frac{\\pi^3}{8}\\approx3.8758$ (נבדק באינטגרציה נומרית של הקליפות לכל $B=0..9$)."),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "22B-A",
    "examLabel": "מבחן סוף סמסטר א' תשפ\"ב, מועד ב'",
    "year": 2022,
    "examDate": "22/02/2022",
    "sourceFile": "calculus-1/22B-A exam.pdf",
    "solutionFile": "",
    "contexts": {"c0": {"kind": "text", "title": "הפרמטרים A, B, C", "text": CTX0}},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

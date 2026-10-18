# -*- coding: utf-8 -*-
"""Generator for tools/raw/22B-B.json -- calculus-1 (20151), semester B 2022, moed B (12/07/2022).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22B-B.py

Source: sitting 22B-B, pp.1-9 (HIT-headed typeset document "solution of the final exam of 12.07.2022": the lecturers'
official solution, with each question restated before its solution). Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6
(each question 20%, two parts of 10%). Question wording below is the restatement in that file.

Transcription notes
- Q1 is one item (single instruction list); the typeset graph on p.3 is shipped as images/exams/22B-B-Q1-graph.png. The two
  hand-drawn sign tables are described in words (f' : -,+,- ; f'' : -,+,-,+).
- Q1e: the file prints the second form of b as lim x/(e^(2x^2)-1) and the L'Hopital form as 1/(4x e^(2x)); the correct
  expressions x/e^(2x^2-1) and 1/(4x e^(2x^2-1)) are written (both tend to 0 as the file concludes).
- Q2a: the file's induction chain prints '1+1/a' in two places where '1+3/a' is meant; written with the 3.
- Q3a: the printed task has <= while the proof gives the strict inequality (which implies it); transcribed as is.
- Q4b: the file prints the upper limit of the antiderivative as 2 instead of 1; the value is computed with 1.
- Q3b, Q5b: the sketches in the solution are shipped as images.
- Q6b: the official remainder estimate uses (0.01)^3 where |x|<=0.1 gives |x|^3<=0.001; the official 4.57e-7 should be
  4.57e-4 (sympy). Final-answer error -> "הפתרון הרשמי עם תיקון" label, solutionSource solved, official False.

Checks (tools/verify/22B-B/check.py, sympy): every derivative, sign table, limit, antiderivative, volume, arc length,
area and Taylor coefficient matches the official answers except the Q6b remainder bound.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22B-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**א. תחום ההגדרה של הפונקציה:** $x\in\mathbb{R}$.
**ב. נקודות החיתוך עם הצירים:** $x\cdot e^{1-2x^2}=0$, נקבל את הנקודה $x=0,\ y=0$.
**ג. תחומי עליה וירידה, נקודות קיצון:**
$$f'(x)=e^{1-2x^2}\left(1-4x^2\right)=0$$
קיימות שתי נקודות חשודות לקיצון: $x_1=\frac{1}{2},\ x_2=-\frac{1}{2}$.
טבלת סימן של $f'(x)$: שלילית כאשר $x<-\frac{1}{2}$, חיובית כאשר $-\frac{1}{2}<x<\frac{1}{2}$, ושלילית כאשר $x>\frac{1}{2}$.
קיימות שתי נקודות קיצון: נקודת מקסימום $\left(\frac{1}{2},\frac{\sqrt{e}}{2}\right)$, נקודת מינימום $\left(-\frac{1}{2},-\frac{\sqrt{e}}{2}\right)$.
**ד. תחומי קמירות וקעירות, נקודות פיתול:**
$$f''(x)=4xe^{1-2x^2}\left(4x^2-3\right)=0$$
טבלת סימן של $f''(x)$: שלילית כאשר $x<-\frac{\sqrt{3}}{2}$, חיובית כאשר $-\frac{\sqrt{3}}{2}<x<0$, שלילית כאשר $0<x<\frac{\sqrt{3}}{2}$, וחיובית כאשר $x>\frac{\sqrt{3}}{2}$.
נקודות פיתול הן: $x_1=0,\ x_2=\frac{\sqrt{3}}{2},\ x_3=-\frac{\sqrt{3}}{2}$.
**ה. אסימפטוטות:**
1. אין אסימפטוטה אנכית (פונקציה מוגדרת ורציפה בכל תחום הגדרתה).
2. אסימפטוטה משופעת:
$$a=\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim_{x\to\pm\infty}\frac{xe^{1-2x^2}}{x}=0$$
$$b=\lim_{x\to\pm\infty}xe^{1-2x^2}\,[\infty\cdot0]=\lim_{x\to\pm\infty}\frac{x}{e^{2x^2-1}}\left[\frac{\infty}{\infty}\right]=\lim_{x\to\pm\infty}\frac{1}{4xe^{2x^2-1}}\left[\frac{1}{\infty}\right]=0$$
$y=0$ - אסימפטוטה אופקית של הפונקציה.
**ו. שרטוט:**
![גרף הפונקציה f(x)=x e^(1-2x^2): מקסימום ב-x=1/2, מינימום ב-x=-1/2, אסימפטוטה y=0](images/exams/22B-B-Q1-graph.png)
"""

SOL2A = r"""
מתוך ההגדרה של הסדרה מקבלים ש-$a_n>0$. לכן $0$ הוא חסם תחתון של הסדרה.
נוכיח לפי אינדוקציה שהסדרה הנתונה יורדת. צריך להוכיח ש-$a_{n+1}<a_n$.
בדיקה $n=1$: $a_2=\frac{2}{1+3}=\frac{1}{2}<a_1=1$.
ההנחה עבור $n=k$: $a_{k+1}<a_k$. צריך להוכיח עבור $n=k+1$: $a_{k+2}<a_{k+1}$.
$$a_{k+1}<a_k\ \Rightarrow\ \frac{1}{a_{k+1}}>\frac{1}{a_k}\ \Rightarrow\ \frac{3}{a_{k+1}}>\frac{3}{a_k}\ \Rightarrow$$
$$1+\frac{3}{a_{k+1}}>1+\frac{3}{a_k}\ \Rightarrow$$
$$\frac{1}{1+\frac{3}{a_{k+1}}}<\frac{1}{1+\frac{3}{a_k}}\ \Rightarrow\ \frac{2}{1+\frac{3}{a_{k+1}}}<\frac{2}{1+\frac{3}{a_k}}\ \Rightarrow\ a_{k+2}<a_{k+1}$$
מ.ש.ל.
לכן הסדרה הנתונה מתכנסת כסדרה יורדת וחסומה מלמטה. נסמן
$$\lim_{n\to\infty}a_n=L\ \Rightarrow\ \lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}\frac{2}{1+\frac{3}{a_n}}\ \Rightarrow$$
$$L=\frac{2}{1+\frac{3}{L}},\qquad L=\frac{2L}{L+3}\ \Rightarrow\ L^2+3L=2L,\ L^2+L=0$$
$$L_1=0,\ L_2=-1$$
$$a_n>0\ \Rightarrow\ L\neq-1\ \Rightarrow\ L=0$$
$$\lim_{n\to\infty}a_n=0$$
"""

SOL2B = r"""
אם נשתמש בהצבה טריגונומטרית אוניברסלית, $t=\tan\frac{x}{2}$, אז $\sin x=\frac{2t}{1+t^2},\ \cos x=\frac{1-t^2}{1+t^2},\ dx=\frac{2dt}{1+t^2}$, וכתוצאה מכך נוכל להציג את האינטגרל המקורי בצורה:
$$\int\frac{dx}{5-4\sin x+3\cos x}=\int\frac{2\,dt}{(1+t^2)\left(5-4\frac{2t}{1+t^2}+3\frac{1-t^2}{1+t^2}\right)}=\int\frac{dt}{4-4t+t^2}=\int\frac{dt}{(t-2)^2}=$$
$$=-\frac{1}{t-2}+C=-\frac{1}{\tan\frac{x}{2}-2}+C=\frac{1}{2-\tan\frac{x}{2}}+C$$
"""

SOL3A = r"""
הבה נבחן את הפונקציה $f(x)=\arcsin x$ שנגזרת שלה היא: $f'(x)=(\arcsin x)'=\frac{1}{\sqrt{1-x^2}}$.
לפי משפט לגרנז' קיימת נקודה $c\in(a,b)$ כך ש-
$$f'(c)=\frac{f(b)-f(a)}{b-a}$$
כלומר:
$$\frac{1}{\sqrt{1-c^2}}=\frac{\arcsin b-\arcsin a}{b-a}\iff\frac{b-a}{\sqrt{1-c^2}}=\arcsin b-\arcsin a$$
מאז $0<a<c<b$ יש לנו כי
$$a^2<c^2<b^2\ \Longrightarrow\ -b^2<-c^2<-a^2\ \Longrightarrow\ 1-b^2<1-c^2<1-a^2\ \Longrightarrow\ \sqrt{1-b^2}<\sqrt{1-c^2}<\sqrt{1-a^2}\ \Longrightarrow$$
$$\frac{1}{\sqrt{1-a^2}}<\frac{1}{\sqrt{1-c^2}}<\frac{1}{\sqrt{1-b^2}}\ \Longrightarrow\ \frac{b-a}{\sqrt{1-a^2}}<\frac{b-a}{\sqrt{1-c^2}}<\frac{b-a}{\sqrt{1-b^2}}\iff$$
$$\frac{b-a}{\sqrt{1-a^2}}<\arcsin(b)-\arcsin(a)<\frac{b-a}{\sqrt{1-b^2}}$$
"""

SOL3B = r"""
![התחום הכלוא בין y=sqrt(x ln x) לציר ה-x עבור 1<=x<=e](images/exams/22B-B-Q3b-sketch.png)
$$V=\pi\int_1^ef^2(x)\,dx=\pi\int_1^ex\ln x\,dx=\left|\begin{array}{ll}u=\ln x & du=\frac{dx}{x}\\ dv=x\,dx & v=\frac{x^2}{2}\end{array}\right|=$$
$$=\pi\left(\frac{x^2}{2}\ln x\Big|_1^e-\frac{1}{2}\int_1^ex^2\frac{dx}{x}\right)=\pi\left(\frac{e^2}{2}-\frac{1}{2}\int_1^ex\,dx\right)=$$
$$=\pi\left(\frac{e^2}{2}-\frac{1}{2}\cdot\frac{x^2}{2}\Big|_1^e\right)=\pi\left(\frac{e^2}{2}-\frac{1}{2}\left(\frac{e^2}{2}-\frac{1}{2}\right)\right)=$$
$$=\pi\left(\frac{e^2}{2}-\frac{e^2}{4}+\frac{1}{4}\right)=\frac{\pi}{4}\left(e^2+1\right)$$
"""

SOL4A = r"""
$$\lim_{x\to0}\frac{x-\int_0^{x^2}\cos\left(t^2\right)dt}{x^3-6x}=\left\{\tfrac{0}{0}\right\}=\lim_{x\to0}\frac{1-\cos\left(x^4\right)(2x)}{3x^2-6}=-\frac{1}{6}$$
"""

SOL4B = r"""
$$L=\int_0^1\sqrt{1+\left(f'(x)\right)^2}\,dx$$
$$f(x)=x\sqrt{x}=x^{3/2}\ \Longrightarrow\ f'(x)=\frac{3}{2}x^{1/2}\ \Longrightarrow\ \left(f'(x)\right)^2=\frac{9}{4}x\ \Longrightarrow$$
$$L=\int_0^1\sqrt{1+\frac{9}{4}x}\,dx=\frac{4}{9}\int_0^1\frac{9}{4}\left(1+\frac{9}{4}x\right)^{1/2}dx=$$
$$=\frac{4}{9}\cdot\frac{2}{3}\left(1+\frac{9}{4}x\right)^{3/2}\Big|_0^1=\frac{8}{27}\left(\left(\frac{13}{4}\right)^{3/2}-1\right)$$
"""

SOL5A = r"""
נסמן $f(x)=2x^3+3\arctan x+e^x+1$. המשוואה הנתונה שקולה ל-$f(x)=0$.
$$f(0)=2>0,\qquad f(-1)=-2-\frac{3\pi}{4}+\frac{1}{e}+1<0$$
$f(x)$ רציפה על $[-1,0]$, אז לפי משפט על ערך הביניים $f(0)\cdot f(-1)<0$, קיימת נקודה $x=c\in(-1,0)$ כך ש-$f(c)=0$. ז"א למשוואה קיים פתרון $x=c$.
נוכיח שפתרון יחיד: $f'(x)=6x^2+\frac{3}{1+x^2}+e^x>0$ ב-$(-\infty,\infty)$. ז"א $f(x)$ מונוטונית עולה ממש ב-$(-\infty,\infty)$. לכן $x=c$ הוא פתרון יחיד למשוואה.
"""

SOL5B = r"""
נסמן נקודת השקה: $A\left(a,\sqrt{a-1}\right)$.
![גרף y=sqrt(x-1), המשיק דרך הראשית והתחום הכלוא בין הגרף, המשיק וציר ה-x](images/exams/22B-B-Q5b-sketch.png)
שיפוע של משיק דרך 2 נקודות: $m_{OA}=\frac{\sqrt{a-1}}{a}$.
שיפוע של משיק דרך נקודת השקה: $m=y'(a)=\frac{1}{2\sqrt{a-1}}$.
$$\frac{1}{2\sqrt{a-1}}=\frac{\sqrt{a-1}}{a}\ \to\ 2(a-1)=a\ \to\ a=2\ \to\ A(2,1)$$
משוואת משיק: $y-1=\frac{1}{2}(x-2)\ \to\ y=\frac{1}{2}x$.
$$S_{\triangle OAB}=\frac{2\cdot1}{2}=1,\qquad S_2=\int_1^2\sqrt{x-1}\,dx=\frac{2}{3}\left((x-1)^{3/2}\right)\Big|_1^2=\frac{2}{3}\ \to\ S=S_{\triangle OAB}-S_2=\frac{1}{3}$$
"""

SOL6A = r"""
נמצא את הפירוק מן הצורה:
$$\frac{1}{(x+1)\left(x^2+4x+5\right)}=\frac{A}{x+1}+\frac{Bx+C}{x^2+4x+5}$$
$$1=A\left(x^2+4x+5\right)+(Bx+C)(x+1)$$
נמצא את המקדמים:
$$x=-1:\ 1=2A\Rightarrow A=\frac{1}{2}$$
$$x^2:\ A+B=0\Rightarrow B=-\frac{1}{2}$$
$$x:\ 4A+B+C=0\Rightarrow C=-\frac{3}{2}$$
$$\int\frac{dx}{(x+1)\left(x^2+4x+5\right)}=\frac{1}{2}\int\frac{dx}{x+1}-\frac{1}{2}\int\frac{x\,dx}{x^2+4x+5}-\frac{3}{2}\int\frac{dx}{x^2+4x+5}=$$
$$=\frac{1}{2}\ln|x+1|-\frac{1}{4}\int\frac{(2x+4-4)\,dx}{x^2+4x+5}-\frac{3}{2}\int\frac{dx}{x^2+4x+5}=$$
$$=\frac{1}{2}\ln|x+1|-\frac{1}{4}\int\frac{(2x+4)\,dx}{x^2+4x+5}-\frac{1}{2}\int\frac{dx}{(x+2)^2+1}$$
$$=\frac{1}{2}\ln|x+1|-\frac{1}{4}\ln\left(x^2+4x+5\right)-\frac{1}{2}\arctan(x+2)+C$$
"""

SOL6B = r"""
**הפתרון הרשמי עם תיקון:** בהערכת השארית בפתרון הרשמי הוצב $(0.01)^3$ והתקבל $4.57\cdot10^{-7}$. בקטע $[-0.1,0.1]$ מתקיים $|x|\le0.1$, כלומר $|x|^3\le(0.1)^3$, והחסם הנכון הוא $\frac{1}{3\cdot0.9^3}(0.1)^3\approx4.57\cdot10^{-4}$. הפולינום $T_2(x)=x-\frac{x^2}{2}$ נכון. השורה האחרונה מתוקנת. התיקון נבדק (sympy).
הפולינום הנדרש הוא $T_2(x)=y(0)+\frac{y'(0)}{1!}x+\frac{y''(0)}{2!}x^2$, ואם נחשב
$$y'=\frac{1}{1+x}\Big|_{x=0}=1,\qquad y''=-\frac{1}{(1+x)^2}\Big|_{x=0}=-1$$
אז נקבל אותו בצורה $T_2(x)=x-\frac{1}{2}x^2$. לפי משפט טיילור עם שארית, שגיאת הקירוב $y=\ln(1+x)\approx T_2(x)=x-\frac{1}{2}x^2$ ניתן להעריך בהתאם ל-
$$\left|y-T_2(x)\right|=\left|R_2(x)\right|=\left|\frac{y'''(z)}{3!}x^3\right|=\left|\frac{2}{3!(1+z)^3}x^3\right|$$
כאשר $-0.1<z<0.1$. מכאן נובע ש-
$$\left|R_2(x)\right|=\left|\frac{1}{3(1+z)^3}x^3\right|\le\frac{1}{3\cdot0.9^3}(0.1)^3\approx4.57\cdot10^{-4}$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=x\cdot e^{1-2x^2}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, "
      "תחומי עליה וירידה, נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "proof", "sequences_limits",
      r"נתונה הסדרה: $a_1=1,\ a_{n+1}=\frac{2a_n}{a_n+3}$. הוכיחו כי הסדרה מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2A, part="א", points=10),
    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{dx}{5-4\sin(x)+3\cos(x)}$.",
      SOL2B, part="ב", points=10),

    Q(3, "proof", "mean_value_theorems",
      r"הוכיחו את האי-שוויון $\frac{b-a}{\sqrt{1-a^2}}\le\arcsin(b)-\arcsin(a)\le\frac{b-a}{\sqrt{1-b^2}}$, כאשר $0<a<b<1$.",
      SOL3A, part="א", points=10),
    Q(3, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום המישורי הכלוא בין הקווים: "
      r"$y=\sqrt{x\ln(x)},\ y=0,\ x=1,\ x=e$ סביב ציר ה-$X$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "lhopital_taylor",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\frac{x-\int_0^{x^2}\cos\left(t^2\right)dt}{x^3-6x}$.",
      SOL4A, part="א", points=10),
    Q(4, "computation", "definite_integrals",
      r"חשבו את אורך הקשת של העקומה $y=x\sqrt{x}$ בקטע $0\le x\le1$.",
      SOL4B, part="ב", points=10),

    Q(5, "proof", "continuity",
      r"הוכיחו כי למשוואה $2x^3+3\arctan x+e^x+1=0$ קיים פתרון אחד בלבד.",
      SOL5A, part="א"),
    Q(5, "computation", "definite_integrals",
      r"חשבו את השטח הכלוא בין הגרף של הפונקציה $y=\sqrt{x-1}$, משיק לאותה הפונקציה העובר דרך ראשית הצירים $(0,0)$ וציר ה-$X$.",
      SOL5B, part="ב"),

    Q(6, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{dx}{(x+1)\left(x^2+4x+5\right)}$.",
      SOL6A, part="א", points=10),
    Q(6, "computation", "lhopital_taylor",
      r"פתחו את הפונקציה $y=\ln(1+x)$ לפולינום מקלורן מסדר שני והעריכו את השארית עבור הקטע $[-0.1,0.1]$.",
      SOL6B, part="ב", points=10, solutionSource="solved", official=False),
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


import mpmath as _mp
import numpy as _np
an = sp.Symbol('a_n', real=True)
tt = sp.Symbol('t', real=True)

# ===== Q1: f = x e^{1-2x^2} =====
Eg = sp.exp(1 - 2*x**2)
f1 = x*Eg
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, Eg*(1 - 4*x**2)) and same(f1pp, 4*x*Eg*(4*x**2 - 3))
assert sorted(sp.solve(sp.Eq(1 - 4*x**2, 0), x)) == [-R(1, 2), R(1, 2)]
assert sorted(sp.solve(sp.Eq(x*(4*x**2 - 3), 0), x)) == [-sp.sqrt(3)/2, 0, sp.sqrt(3)/2]
fmax1 = sp.simplify(f1.subs(x, R(1, 2)))
assert sp.simplify(fmax1 - sp.sqrt(sp.E)/2) == 0
assert sp.limit(f1, x, sp.oo) == 0 and sp.limit(f1, x, -sp.oo) == 0

add(1,
    rubric=rub(("תחום הגדרה $\\mathbb{R}$ ונקודת החיתוך היחידה $(0,0)$", 3),
               ("נגזרת $f'(x)=e^{1-2x^2}\\left(1-4x^2\\right)$, נקודות קריטיות $x=\\pm\\frac{1}{2}$, טבלת סימנים וסיווג הקיצון: מקסימום $\\left(\\frac{1}{2},\\frac{\\sqrt{e}}{2}\\right)$ ומינימום $\\left(-\\frac{1}{2},-\\frac{\\sqrt{e}}{2}\\right)$", 7),
               ("נגזרת שנייה $f''(x)=4xe^{1-2x^2}\\left(4x^2-3\\right)$, קמירות ונקודות פיתול $x=0,\\pm\\frac{\\sqrt{3}}{2}$", 5),
               ("אסימפטוטה אופקית $y=0$ ב-$\\pm\\infty$ וללא אסימפטוטה אנכית", 3),
               ("שרטוט הגרף בהתאם לכל הנתונים", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את כלל השרשרת באקספוננט: $\\left(e^{1-2x^2}\\right)'=-4x\\cdot e^{1-2x^2}$.",
              "לפספס את $x=0$ כנקודת פיתול: $f''$ מתאפסת שם ומשנה סימן.",
              "להשאיר את $\\lim x\\,e^{1-2x^2}$ כ-$\\infty\\cdot0$ בלי להפוך למנה $\\frac{x}{e^{2x^2-1}}$ ולהפעיל לופיטל."],
    steps=[
        chx("מהי הנגזרת של $f(x)=x\\cdot e^{1-2x^2}$?", Eg*(1 - 4*x**2),
            [Eg*(1 + 4*x**2), Eg*(1 - 2*x**2), Eg*(1 - 4*x)],
            lambda e: same(e, f1p),
            "גזירת מכפלה: $f'=e^{1-2x^2}+x\\cdot e^{1-2x^2}(-4x)=e^{1-2x^2}\\left(1-4x^2\\right)$ (נבדק ב-sympy)."),
        num("באיזה $x$ נמצא המקסימום המקומי? (עשרוני)", R(1, 2), "$1-4x^2=0$ נותן $x=\\pm\\frac{1}{2}$; ה-$f'$ חיובית משמאל ל-$\\frac{1}{2}$ ושלילית מימין לו, ולכן שם המקסימום."),
        num("מהו ערך המקסימום המקומי $f\\left(\\frac{1}{2}\\right)$? (עשרוני)", fmax1,
            "$f\\left(\\frac{1}{2}\\right)=\\frac{1}{2}e^{\\frac{1}{2}}=\\frac{\\sqrt{e}}{2}\\approx0.8244$."),
        num("מהו הערך החיובי של $x$ שבו $f''(x)=4xe^{1-2x^2}\\left(4x^2-3\\right)$ מתאפסת? (עשרוני)", sp.sqrt(3)/2,
            "$x\\left(4x^2-3\\right)=0$ נותן $x=0,\\pm\\frac{\\sqrt{3}}{2}$, והערך החיובי הוא $\\frac{\\sqrt{3}}{2}\\approx0.8660$."),
        ch("מהי האסימפטוטה של $f$ ב-$\\pm\\infty$?", "אופקית: $y=0$",
           ["משופעת: $y=x$", "אנכית: $x=0$", "אין אסימפטוטות"],
           "$\\lim_{x\\to\\pm\\infty}\\frac{x}{e^{2x^2-1}}=0$ (אומת ב-sympy), ולכן $y=0$ אופקית; אין נקודת אי-רציפות ולכן אין אנכית."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: a_1 = 1, a_{n+1} = 2a_n/(a_n+3) =====
seq2 = lim_iter(lambda v: 2*v/(v + 3), 1, n=60)
assert abs(seq2[1] - R(1, 2)) < 1e-40 and all(seq2[i + 1] < seq2[i] for i in range(len(seq2) - 1)) and seq2[-1] < 1e-8
Ls = sp.Symbol('L', real=True)
assert sorted(sp.solve(sp.Eq(Ls, 2*Ls/(Ls + 3)), Ls)) == [-1, 0]
assert sp.simplify(2*an/(an + 3) - 2/(1 + 3/an)) == 0
for bd in (1, 3):
    assert bd**2 + bd != 0

L2a = [r"מההנחה $a_{k+1}<a_k$ ומכיוון שהאיברים חיוביים נובע $\frac{3}{a_{k+1}}>\frac{3}{a_k}$, ולכן $1+\frac{3}{a_{k+1}}>1+\frac{3}{a_k}$.",
       r"בהיפוך: $\frac{2}{1+\frac{3}{a_{k+1}}}<\frac{2}{1+\frac{3}{a_k}}$.",
       r"ומכיוון ש-$a_{k+2}=\frac{2}{1+\frac{3}{a_{k+1}}}$ ו-$a_{k+1}=\frac{2}{1+\frac{3}{a_k}}$ מתקבל $a_{k+2}<a_{k+1}$."]

add(2, "א",
    rubric=rub(("חסם תחתון: $a_n>0$ לכל $n$ מהגדרת הסדרה", 2),
               ("אינדוקציה לירידה: בסיס $a_2=\\frac{1}{2}<a_1=1$ וצעד מ-$a_{k+1}<a_k$ ל-$a_{k+2}<a_{k+1}$", 4),
               ("הסקה שסדרה יורדת וחסומה מלמטה מתכנסת", 1),
               ("מעבר לגבול $L=\\frac{2L}{L+3}$, כלומר $L^2+L=0$, ופסילת $L=-1$ ומסקנה $L=0$", 3)),
    rubricSource="ai-verified",
    pitfalls=["להסיק מ-$a_2<a_1$ בלבד שהסדרה יורדת, בלי צעד אינדוקציה.",
              "לשכוח לפסול את $L=-1$ אף שכל איברי הסדרה חיוביים.",
              "בצעד האינדוקציה להפוך אי-שוויון בלי לוודא שהאיברים חיוביים; ההיפוך $\\frac{1}{u}$ הופך את כיוון האי-שוויון רק עבור $u>0$."],
    steps=[
        num("מהו $a_2=\\frac{2a_1}{a_1+3}$? (עשרוני)", R(1, 2), "$a_2=\\frac{2}{4}=\\frac{1}{2}<1=a_1$."),
        order("סדרו את צעד האינדוקציה (מההנחה $a_{k+1}<a_k$ למסקנה).", L2a,
              "כל שורה נובעת מקודמתה: היפוך והכפלה ב-$3$, אחר כך היפוך נוסף והכפלה ב-$2$, ולבסוף הצבת הנוסחה הרקורסיבית."),
        ch("אילו ערכים אפשריים לגבול $L$ לפי המשוואה $L=\\frac{2L}{L+3}$?", "$L=0$ או $L=-1$",
           ["$L=0$ או $L=1$", "$L=0$ או $L=3$", "$L=1$ או $L=-1$"],
           "$L(L+3)=2L$ נותן $L^2+L=0$, כלומר $L(L+1)=0$ (נבדק ב-sympy)."),
        num("מהו גבול הסדרה?", 0, "האיברים חיוביים, ולכן $L\\ge0$ ו-$L=0$ (נבדק גם מספרית: $a_{60}<10^{-8}$)."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: int dx/(5 - 4 sin x + 3 cos x), universal substitution =====
g2b = 1/(5 - 4*sp.sin(x) + 3*sp.cos(x))
integrand_t = sp.simplify(1/(5 - 4*(2*tt/(1 + tt**2)) + 3*((1 - tt**2)/(1 + tt**2)))*2/(1 + tt**2))
assert sp.simplify(integrand_t - 1/(tt - 2)**2) == 0
F2b = 1/(2 - sp.tan(x/2))
P2b = (0.3, 0.7, 1.1, 2.0, 2.5)
assert same(sp.diff(F2b, x), g2b, pts=P2b)

add(2, "ב",
    rubric=rub(("הצבה אוניברסלית $t=\\tan\\frac{x}{2}$ והנוסחאות ל-$\\sin x$, $\\cos x$, $dx$", 3),
               ("הצבה באינטגרל ופישוט למכנה $4-4t+t^2$", 3),
               ("אינטגרל $\\int\\frac{dt}{(t-2)^2}=-\\frac{1}{t-2}$", 2),
               ("הצבה חוזרת ותשובה $\\frac{1}{2-\\tan\\frac{x}{2}}+C$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את הגורם $\\frac{2}{1+t^2}$ מ-$dx$, ולהישאר עם אינטגרל שאינו מצטמצם.",
              "לטעות בסימן בפישוט המכנה: $5(1+t^2)-8t+3(1-t^2)=2t^2-8t+8=2(t-2)^2$.",
              "לשכוח את הסימן ב-$\\int\\frac{dt}{(t-2)^2}=-\\frac{1}{t-2}$."],
    steps=[
        ch("איזו הצבה מתאימה לאינטגרל רציונלי ב-$\\sin x$ וב-$\\cos x$ בפתרון הרשמי?", "$t=\\tan\\frac{x}{2}$",
           ["$t=\\sin x$", "$t=\\cos x$", "$t=\\tan x$"],
           "ההצבה האוניברסלית נותנת $\\sin x=\\frac{2t}{1+t^2}$, $\\cos x=\\frac{1-t^2}{1+t^2}$ ו-$dx=\\frac{2\\,dt}{1+t^2}$, ולכן כל האינטגרנד הופך לרציונלי ב-$t$."),
        chx("מהו האינטגרנד אחרי ההצבה והפישוט (הביטוי ב-$t$ שמוכפל ב-$dt$)?", 1/(tt - 2)**2,
            [1/(tt + 2)**2, 1/(tt**2 - 4), 2/(tt - 2)**2],
            lambda e: sp.simplify(e - integrand_t) == 0,
            "המכנה הוא $\\frac{5(1+t^2)-8t+3(1-t^2)}{1+t^2}=\\frac{2(t-2)^2}{1+t^2}$, וכפל ב-$\\frac{2}{1+t^2}$ נותן $\\frac{1}{(t-2)^2}$ (נבדק ב-sympy)."),
        chx("מהי התוצאה (בלי הקבוע)?", F2b,
            [-1/(2 - sp.tan(x/2)), 1/(2 + sp.tan(x/2)), 1/(sp.tan(x/2) - 2)**2],
            lambda e: same(sp.diff(e, x), g2b, pts=P2b),
            "$\\int\\frac{dt}{(t-2)^2}=-\\frac{1}{t-2}=\\frac{1}{2-t}$ ואז $t=\\tan\\frac{x}{2}$ (הנגזרת נבדקה ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: Lagrange for arcsin =====
fa = sp.asin(x)
P3a = (0.1, 0.3, 0.5, 0.7, 0.9)
assert same(sp.diff(fa, x), 1/sp.sqrt(1 - x**2), pts=P3a)
_a, _c, _b = 0.2, 0.5, 0.8
assert not (1 - _b**2 > 1 - _c**2 > 1 - _a**2) and (1 - _b**2 < 1 - _c**2 < 1 - _a**2)

L3a = [r"$f(x)=\arcsin x$ רציפה ב-$[a,b]$ וגזירה ב-$(a,b)$; לפי לגרנז' קיימת $c\in(a,b)$ כך ש-$\frac{1}{\sqrt{1-c^2}}=\frac{\arcsin b-\arcsin a}{b-a}$.",
       r"מ-$0<a<c<b$ נובע $a^2<c^2<b^2$, ולכן $1-b^2<1-c^2<1-a^2$.",
       r"לכן $\sqrt{1-b^2}<\sqrt{1-c^2}<\sqrt{1-a^2}$, ובהיפוך $\frac{1}{\sqrt{1-a^2}}<\frac{1}{\sqrt{1-c^2}}<\frac{1}{\sqrt{1-b^2}}$.",
       r"נכפיל ב-$b-a>0$ ונציב את שוויון לגרנז': $\frac{b-a}{\sqrt{1-a^2}}<\arcsin b-\arcsin a<\frac{b-a}{\sqrt{1-b^2}}$."]
L3a_bug = list(L3a)
L3a_bug[1] = r"מ-$0<a<c<b$ נובע $a^2<c^2<b^2$, ולכן $1-b^2>1-c^2>1-a^2$."

add(3, "א",
    rubric=rub(("בחירת $f(x)=\\arcsin x$ ובדיקת תנאי משפט לגרנז' על $[a,b]$", 3),
               ("שוויון לגרנז': $\\frac{b-a}{\\sqrt{1-c^2}}=\\arcsin b-\\arcsin a$", 1),
               ("שרשרת אי-השוויונות על $c$ עד $\\frac{1}{\\sqrt{1-a^2}}<\\frac{1}{\\sqrt{1-c^2}}<\\frac{1}{\\sqrt{1-b^2}}$", 4),
               ("כפל ב-$b-a>0$ והצבה, והמסקנה הסופית", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח להפוך את כיוון האי-שוויון בשלב ההיפוך $\\frac{1}{u}$: אצל מספרים חיוביים ההיפוך הופך את הכיוון.",
              "לשכוח שהאי-שוויון הוא אי-שוויון חזק בגלל $a<c<b$, אף שהמשימה מבקשת $\\le$.",
              "לכפול ב-$b-a$ בלי לציין שהוא חיובי, ולכן הכיוון נשמר."],
    steps=[
        ch("איזו פונקציה מגדיר הפתרון הרשמי כדי להפעיל את משפט לגרנז'?", "$f(x)=\\arcsin x$",
           ["$f(x)=\\arccos x$", "$f(x)=\\arctan x$", "$f(x)=\\frac{1}{\\sqrt{1-x^2}}$"],
           "הפרש $\\arcsin b-\\arcsin a$ הוא $f(b)-f(a)$ עבור $f=\\arcsin$."),
        chx("מהי הנגזרת של $f(x)=\\arcsin x$?", 1/sp.sqrt(1 - x**2),
            [1/(1 - x**2), -1/sp.sqrt(1 - x**2), 1/sp.sqrt(1 + x**2)],
            lambda e: same(e, sp.diff(fa, x), pts=P3a),
            "זו הנגזרת הידועה של $\\arcsin$ (נבדק ב-sympy)."),
        order("סדרו את שלבי ההוכחה.", L3a,
              "קודם לגרנז' (שמגדיר את $c$), אחר כך אי-שוויון על $c^2$, אחר כך שורש והיפוך, ולבסוף כפל ב-$b-a$."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L3a_bug, 1,
                "מ-$a^2<c^2<b^2$ נובע (אחרי הכפלה ב-$-1$ והוספת $1$) $1-b^2<1-c^2<1-a^2$; הכיוון בשורה השגויה הפוך."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: volume of y = sqrt(x ln x), 1 <= x <= e =====
_mp.mp.dps = 25
e_ = _mp.e
vals3b = {
    "good": _mp.pi*_mp.quad(lambda u: u*_mp.log(u), [1, e_]),
    "b1": _mp.pi*_mp.quad(lambda u: _mp.sqrt(u*_mp.log(u)), [1, e_]),
    "b2": 2*_mp.pi*_mp.quad(lambda u: u*_mp.log(u), [1, e_]),
    "b3": _mp.pi*_mp.quad(lambda u: (u*_mp.log(u))**2, [1, e_]),
}
assert abs(vals3b["good"] - _mp.pi*(e_**2 + 1)/4) < 1e-15
assert all(abs(vals3b[k] - vals3b["good"]) > 1e-3 for k in ("b1", "b2", "b3"))
AF3b = x**2*sp.log(x)/2 - x**2/4
assert same(sp.diff(AF3b, x), x*sp.log(x))
I3b = sp.integrate(x*sp.log(x), (x, 1, sp.E))
assert sp.simplify(I3b - (sp.E**2 + 1)/4) == 0

add(3, "ב",
    rubric=rub(("נוסחת הדיסקות $V=\\pi\\int_1^ef^2(x)\\,dx=\\pi\\int_1^ex\\ln x\\,dx$", 3),
               ("אינטגרציה בחלקים עם $u=\\ln x$, $dv=x\\,dx$", 2),
               ("קדומה $\\frac{x^2}{2}\\ln x-\\frac{x^2}{4}$ והצבת הגבולות", 3),
               ("תשובה סופית $V=\\frac{\\pi}{4}\\left(e^2+1\\right)$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח לרבע את הפונקציה: $\\left(\\sqrt{x\\ln x}\\right)^2=x\\ln x$, בלי שורש.",
              "לבחור $u=x$ ו-$dv=\\ln x\\,dx$: זה מסבך את החישוב ללא צורך.",
              "לטעות בהצבת הגבול התחתון: ב-$x=1$ מתקבל $\\frac{1}{2}\\ln1-\\frac{1}{4}=-\\frac{1}{4}$ ולא $0$."],
    steps=[
        ch("איזה ביטוי נותן את נפח הסיבוב סביב ציר ה-$X$?", r"$V=\pi\int_1^ex\ln x\,dx$",
           [r"$V=\pi\int_1^e\sqrt{x\ln x}\,dx$", r"$V=2\pi\int_1^ex\ln x\,dx$", r"$V=\pi\int_1^e\left(x\ln x\right)^2dx$"],
           "שיטת הדיסקות: $V=\\pi\\int y^2dx$ ו-$y^2=x\\ln x$. ערכי האפשרויות שונים זה מזה (נבדק מספרית)."),
        chx("מהי הקדומה של $x\\ln x$ (בלי הקבוע)?", AF3b,
            [x**2*sp.log(x)/2 - x**2/2, x**2*sp.log(x)/2, x*sp.log(x) - x],
            lambda e: same(sp.diff(e, x), x*sp.log(x)),
            "בחלקים: $\\frac{x^2}{2}\\ln x-\\int\\frac{x}{2}dx=\\frac{x^2}{2}\\ln x-\\frac{x^2}{4}$ (נבדק ב-sympy)."),
        num("מהו $\\int_1^ex\\ln x\\,dx$? (עשרוני)", I3b, "$\\frac{e^2+1}{4}\\approx2.0973$."),
        num("מהו הנפח $V=\\frac{\\pi}{4}\\left(e^2+1\\right)$? (עשרוני)", sp.pi*I3b, "$V\\approx6.589$.", nd=3),
    ],
    stepsSource="ai-verified")

# ===== Q4a: lim (x - int_0^{x^2} cos(t^2) dt)/(x^3 - 6x) = -1/6 =====
_mp.mp.dps = 25
_N = lambda s: s - _mp.quad(lambda u: _mp.cos(u**2), [0, s**2])
_pt = _mp.mpf('0.6')
assert abs(_mp.diff(_N, _pt) - (1 - 2*_pt*_mp.cos(_pt**4))) < 1e-8
numd = 1 - 2*x*sp.cos(x**4)
assert sp.limit(numd/(3*x**2 - 6), x, 0) == -R(1, 6)
_h = _mp.mpf('1e-4')
assert abs(_N(_h)/(_h**3 - 6*_h) + _mp.mpf(1)/6) < 1e-3
P4a = (0.3, 0.6, 0.9, 1.2, 1.5)

add(4, "א",
    rubric=rub(("זיהוי הצורה $\\frac{0}{0}$ והפעלת לופיטל", 2),
               ("גזירת המונה לפי המשפט היסודי וכלל השרשרת: $1-2x\\cos\\left(x^4\\right)$", 4),
               ("גזירת המכנה $3x^2-6$", 1),
               ("הצבת $x=0$ ותשובה $-\\frac{1}{6}$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את כלל השרשרת: הגבול העליון $x^2$ מוסיף גורם $2x$, ובאינטגרנד $t=x^2$ נותן $\\cos\\left(x^4\\right)$.",
              "להציב $t=x^2$ באינטגרנד $\\cos\\left(t^2\\right)$ ולכתוב $\\cos\\left(x^2\\right)$ במקום $\\cos\\left(x^4\\right)$.",
              "לטעות בסימן הנגזרת של המונה: האינטגרל מופיע עם מינוס, ולכן המונה נגזר ל-$1-2x\\cos\\left(x^4\\right)$ ולא ל-$1+2x\\cos\\left(x^4\\right)$."],
    steps=[
        ch("מהי הצורה הלא מוגדרת של הגבול ב-$x\\to0$?", "$\\frac{0}{0}$",
           ["$\\frac{\\infty}{\\infty}$", "$1^\\infty$", "$\\infty-\\infty$"],
           "המונה $0-\\int_0^0\\ldots=0$ והמכנה $0^3-0=0$."),
        chx("מהי הנגזרת של המונה $x-\\int_0^{x^2}\\cos\\left(t^2\\right)dt$?", numd,
            [1 - sp.cos(x**4), 1 - 2*x*sp.cos(x**2), 1 - 2*x*sp.cos(x**4)*x**2],
            lambda e: same(e, numd, pts=P4a),
            "משפט יסודי וכלל שרשרת: $\\cos\\left((x^2)^2\\right)\\cdot2x=2x\\cos\\left(x^4\\right)$ (נבדק מספרית)."),
        num("מהו הגבול? (עשרוני)", -R(1, 6),
            "$\\frac{1-2x\\cos(x^4)}{3x^2-6}\\to\\frac{1}{-6}=-\\frac{1}{6}\\approx-0.1667$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: arc length of y = x^{3/2} on [0, 1] =====
fs = x**R(3, 2)
fp2 = sp.diff(fs, x)**2
P4b = (0.2, 0.5, 0.8, 1.0, 1.4)
assert same(1 + fp2, 1 + R(9, 4)*x, pts=P4b)
AF4b = R(8, 27)*(1 + R(9, 4)*x)**R(3, 2)
assert same(sp.diff(AF4b, x), sp.sqrt(1 + R(9, 4)*x), pts=P4b)
L4b = AF4b.subs(x, 1) - AF4b.subs(x, 0)
assert sp.simplify(L4b - (13*sp.sqrt(13) - 8)/27) == 0
_mp.mp.dps = 25
lv = {
    "good": _mp.quad(lambda u: _mp.sqrt(1 + (_mp.mpf(3)/2*_mp.sqrt(u))**2), [0, 1]),
    "b1": _mp.quad(lambda u: _mp.sqrt(1 + (u**_mp.mpf(1.5))**2), [0, 1]),
    "b2": _mp.quad(lambda u: 1 + (_mp.mpf(3)/2*_mp.sqrt(u))**2, [0, 1]),
    "b3": _mp.quad(lambda u: _mp.sqrt(1 + _mp.mpf(3)/2*_mp.sqrt(u)), [0, 1]),
}
assert abs(lv["good"] - sp.N(L4b, 20)) < 1e-15 and all(abs(lv[k] - lv["good"]) > 1e-3 for k in ("b1", "b2", "b3"))

add(4, "ב",
    rubric=rub(("נוסחת אורך קשת $L=\\int_0^1\\sqrt{1+\\left(f'(x)\\right)^2}\\,dx$", 2),
               ("נגזרת $f'(x)=\\frac{3}{2}\\sqrt{x}$ ו-$1+\\left(f'\\right)^2=1+\\frac{9}{4}x$", 3),
               ("קדומה $\\frac{8}{27}\\left(1+\\frac{9}{4}x\\right)^{\\frac{3}{2}}$", 3),
               ("הצבת הגבולות ותשובה $\\frac{8}{27}\\left(\\left(\\frac{13}{4}\\right)^{\\frac{3}{2}}-1\\right)$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח לרבע את הנגזרת: $\\left(f'\\right)^2=\\frac{9}{4}x$ ולא $\\frac{3}{2}\\sqrt{x}$.",
              "לשכוח את הגורם $\\frac{4}{9}$ בהצבה $u=1+\\frac{9}{4}x$ (מהנגזרת הפנימית $\\frac{9}{4}$).",
              "להשתמש בנוסחת האורך $\\int\\sqrt{1+f^2}$ במקום $\\int\\sqrt{1+\\left(f'\\right)^2}$."],
    steps=[
        ch("איזה ביטוי נותן את אורך העקום $y=x\\sqrt{x}$ בקטע $[0,1]$?", r"$L=\int_0^1\sqrt{1+\left(f'(x)\right)^2}\,dx$",
           [r"$L=\int_0^1\sqrt{1+f^2(x)}\,dx$", r"$L=\int_0^1\left(1+\left(f'(x)\right)^2\right)dx$", r"$L=\int_0^1\sqrt{1+f'(x)}\,dx$"],
           "זו נוסחת אורך הקשת. ערכי האפשרויות שונים זה מזה (נבדק מספרית): רק הראשונה נותנת $\\approx1.4397$."),
        chx("מהו $1+\\left(f'(x)\\right)^2$ עבור $f(x)=x^{\\frac{3}{2}}$?", 1 + R(9, 4)*x,
            [1 + R(3, 2)*x, 1 + R(9, 4)*x**2, 1 + R(3, 2)*sp.sqrt(x)],
            lambda e: same(e, 1 + fp2, pts=P4b),
            "$f'=\\frac{3}{2}x^{\\frac{1}{2}}$ ולכן $\\left(f'\\right)^2=\\frac{9}{4}x$ (נבדק ב-sympy)."),
        chx("מהי הקדומה של $\\sqrt{1+\\frac{9}{4}x}$ (בלי הקבוע)?", AF4b,
            [R(2, 3)*(1 + R(9, 4)*x)**R(3, 2), R(8, 27)*(1 + R(9, 4)*x)**R(1, 2), R(4, 9)*(1 + R(9, 4)*x)**R(3, 2)],
            lambda e: same(sp.diff(e, x), sp.sqrt(1 + R(9, 4)*x), pts=P4b),
            "$\\int u^{\\frac{1}{2}}du=\\frac{2}{3}u^{\\frac{3}{2}}$ והגורם $\\frac{4}{9}$ מהנגזרת הפנימית נותן $\\frac{8}{27}$ (נבדק ב-sympy)."),
        num("מהו אורך העקום? (עשרוני)", L4b, "$\\frac{8}{27}\\left(\\left(\\frac{13}{4}\\right)^{\\frac{3}{2}}-1\\right)=\\frac{13\\sqrt{13}-8}{27}\\approx1.4397$."),
    ],
    stepsSource="ai-verified")

# ===== Q5a: 2x^3 + 3 arctan x + e^x + 1 = 0 has exactly one solution =====
f5 = 2*x**3 + 3*sp.atan(x) + sp.exp(x) + 1
f5p = 6*x**2 + 3/(1 + x**2) + sp.exp(x)
P5 = (-2.0, -0.7, 0.4, 1.3, 2.4)
assert same(sp.diff(f5, x), f5p, pts=P5)
assert f5.subs(x, 0) == 2 and sp.N(f5.subs(x, -1)) < 0 and sp.N(f5p.subs(x, 0)) > 0
assert abs(sp.N(f5.subs(x, -1) - (-2 - 3*sp.pi/4 + 1/sp.E + 1))) < 1e-12
_gx = _np.linspace(-20, 20, 400001)
assert (6*_gx**2 + 3/(1 + _gx**2) + _np.exp(_gx)).min() > 0

add(5, "א",
    rubric=rub(("הגדרת $f(x)=2x^3+3\\arctan x+e^x+1$ והמעבר למשוואה $f(x)=0$", 2),
               ("חישוב $f(0)=2>0$ ו-$f(-1)<0$ ורציפות $f$ על $[-1,0]$", 3),
               ("משפט ערך הביניים: קיים פתרון $c\\in(-1,0)$", 2),
               ("נגזרת $f'(x)=6x^2+\\frac{3}{1+x^2}+e^x>0$ לכל $x$", 2),
               ("מונוטוניות עולה ממש, ולכן הפתרון יחיד", 1)),
    rubricSource="ai-verified",
    pitfalls=["להסתפק בקיום פתרון (ערך הביניים) ולא להוכיח יחידות.",
              "לטעון ש-$f'>0$ בלי להצדיק: כל שלושת המחוברים $6x^2$, $\\frac{3}{1+x^2}$, $e^x$ אי-שליליים והשני והשלישי חיוביים ממש.",
              "לבדוק סימנים בקצוות קטע שבו $f$ אינה רציפה, או לבחור קטע ששני קצותיו נותנים אותו סימן."],
    steps=[
        chx("מהי הנגזרת של $f(x)=2x^3+3\\arctan x+e^x+1$?", f5p,
            [6*x**2 + 3/(1 + x**2) - sp.exp(x), 6*x**2 + 3*sp.atan(x) + sp.exp(x), 2*x**2 + 3/(1 + x**2) + sp.exp(x)],
            lambda e: same(e, sp.diff(f5, x), pts=P5),
            "$\\left(2x^3\\right)'=6x^2$, $(3\\arctan x)'=\\frac{3}{1+x^2}$, $\\left(e^x\\right)'=e^x$ (נבדק ב-sympy)."),
        num("מהו $f(0)$?", 2, "$f(0)=0+3\\cdot0+e^0+1=2>0$."),
        num("מהו $f(-1)=-2-\\frac{3\\pi}{4}+\\frac{1}{e}+1$? (עשרוני)", f5.subs(x, -1),
            "$-2-2.3562+0.3679+1\\approx-2.9883<0$."),
        ch("מה מבטיח את הקיום ומה את היחידות של הפתרון?",
           "קיום: משפט ערך הביניים על $[-1,0]$ (סימנים מנוגדים). יחידות: $f'>0$, ולכן $f$ עולה ממש",
           ["קיום: משפט רול. יחידות: משפט ערך הביניים",
            "קיום: $f'>0$. יחידות: סימנים מנוגדים בקצוות",
            "קיום: משפט ערך הביניים. יחידות: $f'$ מתאפסת בנקודה אחת"],
           "רול דורש $f(-1)=f(0)$, אבל $f(-1)<0<2=f(0)$. מונוטוניות אינה מבטיחה קיום, וסימנים מנוגדים אינם מבטיחים יחידות. כאן $f'$ חיובית תמיד."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: area between y = sqrt(x-1), the tangent through the origin and the x-axis =====
aa = sp.Symbol('a', positive=True)
sol_a = sp.solve(sp.Eq(1/(2*sp.sqrt(aa - 1)), sp.sqrt(aa - 1)/aa), aa)
assert sol_a == [2]
tl5 = x/2
tl5_ok = lambda e: sp.simplify(e.subs(x, 0)) == 0 and sp.simplify(e.subs(x, 2) - 1) == 0 and sp.simplify(sp.diff(e, x) - R(1, 2)) == 0
tri = R(1, 2)*2*1
S2 = sp.integrate(sp.sqrt(x - 1), (x, 1, 2))
S5 = tri - S2
assert tri == 1 and S2 == R(2, 3) and S5 == R(1, 3)

add(5, "ב",
    rubric=rub(("נקודת ההשקה $A\\left(a,\\sqrt{a-1}\\right)$ ותנאי השוויון בין שיפוע המיתר $\\frac{\\sqrt{a-1}}{a}$ לשיפוע המשיק $\\frac{1}{2\\sqrt{a-1}}$", 3),
               ("פתרון $a=2$ ומשוואת המשיק $y=\\frac{1}{2}x$", 2),
               ("שטח המשולש $OAB$: $1$", 2),
               ("שטח מתחת לגרף $\\int_1^2\\sqrt{x-1}\\,dx=\\frac{2}{3}$ וההפרש $S=\\frac{1}{3}$", 3)),
    rubricSource="ai-verified",
    pitfalls=["להניח שהמשיק נוגע ב-$x=1$ (שם הנגזרת לא מוגדרת) במקום לפתור את תנאי ההשקה.",
              "לחבר את שטח המשולש ושטח מתחת לגרף במקום לחסר.",
              "לשכוח שהגרף מתחיל ב-$x=1$ ולכן השטח מתחת לגרף נמדד מ-$1$ עד $2$ ולא מ-$0$."],
    steps=[
        num("מהו שיעור ה-$x$ של נקודת ההשקה? (פתרון $\\frac{1}{2\\sqrt{a-1}}=\\frac{\\sqrt{a-1}}{a}$)", sol_a[0],
            "$a=2(a-1)$ נותן $a=2$, ולכן $A(2,1)$."),
        chx("מהי משוואת המשיק לגרף $y=\\sqrt{x-1}$ העובר דרך הראשית?", tl5,
            [x - 1, x/2 + 1/2, x],
            tl5_ok,
            "השיפוע ב-$a=2$ הוא $\\frac{1}{2\\sqrt{1}}=\\frac{1}{2}$ והמשיק עובר דרך $(0,0)$ ו-$(2,1)$: $y=\\frac{1}{2}x$ (נבדק ב-sympy)."),
        num("מהו שטח המשולש שקודקודיו $(0,0)$, $(2,1)$ ו-$(2,0)$?", tri, "$\\frac{2\\cdot1}{2}=1$."),
        num("מהו $\\int_1^2\\sqrt{x-1}\\,dx$? (עשרוני)", S2, "$\\frac{2}{3}(x-1)^{\\frac{3}{2}}\\Big|_1^2=\\frac{2}{3}\\approx0.6667$."),
        num("מהו השטח המבוקש? (עשרוני)", S5, "$1-\\frac{2}{3}=\\frac{1}{3}\\approx0.3333$."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: int dx/((x+1)(x^2+4x+5)) =====
g6 = 1/((x + 1)*(x**2 + 4*x + 5))
A_, B_, C_ = sp.symbols('A B C')
s6 = sp.solve(sp.Poly(sp.expand(A_*(x**2 + 4*x + 5) + (B_*x + C_)*(x + 1) - 1), x).all_coeffs(), [A_, B_, C_], dict=True)[0]
assert s6 == {A_: R(1, 2), B_: -R(1, 2), C_: -R(3, 2)}
F6 = sp.log(x + 1)/2 - sp.log(x**2 + 4*x + 5)/4 - sp.atan(x + 2)/2
P6 = (0.2, 0.7, 1.5, 2.4, 3.3)
assert same(sp.diff(F6, x), g6, pts=P6)

add(6, "א",
    rubric=rub(("פירוק לשברים חלקיים בצורה $\\frac{A}{x+1}+\\frac{Bx+C}{x^2+4x+5}$", 2),
               ("חישוב המקדמים $A=\\frac{1}{2}$, $B=-\\frac{1}{2}$, $C=-\\frac{3}{2}$", 3),
               ("אינטגרציה של $\\frac{1}{x+1}$ ושל $\\frac{2x+4}{x^2+4x+5}$ כלוגריתמים", 2),
               ("השלמה לריבוע $(x+2)^2+1$ ואינטגרל $\\arctan(x+2)$", 2),
               ("תשובה סופית עם $+C$", 1)),
    rubricSource="ai-verified",
    pitfalls=["לכתוב $\\frac{B}{x^2+4x+5}$ במקום מונה לינארי $Bx+C$.",
              "לפצל את המונה $x$ ל-$\\frac{1}{2}(2x+4)-2$ ולשכוח את החלק $-2$, שנותן את ה-$\\arctan$.",
              "לשכוח שהמכנה $x^2+4x+5=(x+2)^2+1$ אי-פריק, ולכן החלק הלינארי נשאר מעל הריבועי."],
    steps=[
        num("מהו המקדם $A$? (עשרוני)", s6[A_], "הצבת $x=-1$ ב-$1=A\\left(x^2+4x+5\\right)+(Bx+C)(x+1)$ נותנת $1=2A$, כלומר $A=\\frac{1}{2}$.", tol=0.0005),
        num("מהו המקדם $B$? (עשרוני)", s6[B_], "משווים מקדמי $x^2$: $A+B=0$, ולכן $B=-\\frac{1}{2}$.", tol=0.0005),
        num("מהו המקדם $C$? (עשרוני)", s6[C_], "משווים מקדמי $x$: $4A+B+C=0$, ולכן $C=-2+\\frac{1}{2}=-\\frac{3}{2}$.", tol=0.0005),
        chx("מהי התוצאה (בלי הקבוע, בתחום $x>-1$)?", F6,
            [sp.log(x + 1)/2 - sp.log(x**2 + 4*x + 5)/4 + sp.atan(x + 2)/2,
             sp.log(x + 1)/2 - sp.log(x**2 + 4*x + 5)/2 - sp.atan(x + 2)/2,
             sp.log(x + 1)/2 - sp.log(x**2 + 4*x + 5)/4 - sp.atan(x + 2)],
            lambda e: same(sp.diff(e, x), g6, pts=P6),
            "החלק הלוגריתמי הוא $\\frac{1}{2}\\ln|x+1|-\\frac{1}{4}\\ln\\left(x^2+4x+5\\right)$ והחלק הנוסף הוא $-\\frac{1}{2}\\arctan(x+2)$ (הנגזרת של כל אפשרות נבדקה ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: Maclaurin of ln(1+x) of order 2 on [-0.1, 0.1] =====
y6 = sp.log(1 + x)
assert sp.diff(y6, x, 2).subs(x, 0) == -1
coef6 = sp.diff(y6, x, 3)/6
assert same(coef6, 1/(3*(1 + x)**3), pts=(0.2, 0.5, 1.0, 2.0, 3.0))
bound6 = R(1, 10)**3/(3*R(9, 10)**3)
_xs = _np.linspace(-0.1, 0.1, 20001)
assert (_np.abs(_np.log(1 + _xs) - (_xs - _xs**2/2))).max() < float(bound6)
T2 = x - x**2/2
assert T2.subs(x, R(1, 10)) == R(19, 200)

add(6, "ב",
    rubric=rub(("חישוב הנגזרות $y'(0)=1$ ו-$y''(0)=-1$", 2),
               ("פולינום מקלורן $T_2(x)=x-\\frac{x^2}{2}$", 2),
               ("שארית לגרנז' $R_2(x)=\\frac{1}{3(1+z)^3}x^3$", 2),
               ("חסם $|x|\\le0.1$ ו-$1+z\\ge0.9$ על הקטע", 2),
               ("הערכה $|R_2|\\le\\frac{(0.1)^3}{3\\cdot0.9^3}\\approx4.57\\cdot10^{-4}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להציב $(0.01)^3$ בחסם במקום $(0.1)^3$ (טעות בפתרון הרשמי המודפס): $|x|\\le0.1$ ולכן $|x|^3\\le0.001$.",
              "לחסום את המכנה $(1+z)^3$ בעזרת $z=0.1$ במקום $z=-0.1$: החסם הגרוע ביותר מתקבל ב-$1+z=0.9$.",
              "לשכוח את החלוקה ב-$3!$ בשארית, או את הגורם $2$ בנגזרת $y'''=\\frac{2}{(1+x)^3}$."],
    steps=[
        num("מהו $y''(0)$ עבור $y=\\ln(1+x)$?", -1, "$y'=\\frac{1}{1+x}$ ו-$y''=-\\frac{1}{(1+x)^2}$, ולכן $y''(0)=-1$."),
        num("מהו $T_2(0.1)=0.1-\\frac{(0.1)^2}{2}$? (עשרוני)", R(19, 200), "$0.1-0.005=0.095$.", tol=0.0005),
        chx("מהו מקדם השארית $\\frac{y'''(z)}{3!}$ עבור $y=\\ln(1+x)$?", 1/(3*(1 + x)**3),
            [1/(6*(1 + x)**3), 2/(1 + x)**3, 1/(3*(1 + x)**2)],
            lambda e: same(e, coef6, pts=(0.2, 0.5, 1.0, 2.0, 3.0)),
            "$y'''=\\frac{2}{(1+x)^3}$ ולכן $\\frac{y'''}{3!}=\\frac{1}{3(1+x)^3}$ (נבדק ב-sympy)."),
        num("מהו החסם $\\frac{(0.1)^3}{3\\cdot0.9^3}$ על השארית בקטע? (עשרוני)", bound6,
            "$\\frac{0.001}{3\\cdot0.729}\\approx4.57\\cdot10^{-4}$ (לא $4.57\\cdot10^{-7}$ כפי שמודפס בפתרון הרשמי; נבדק גם על רשת צפופה).",
            tol=0.00001, nd=6),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "22B-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ב, מועד ב'",
    "year": 2022,
    "examDate": "12/07/2022",
    "sourceFile": "calculus-1/22B-B exam+solution.pdf",
    "solutionFile": "calculus-1/22B-B exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

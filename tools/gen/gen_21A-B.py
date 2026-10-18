# -*- coding: utf-8 -*-
"""Generator for tools/raw/21A-B.json -- calculus-1 (20151), semester B 2021 (תשפ"א), moed A.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_21A-B.py

Source: sitting 21A-B, pp.1-11 (image-only PDF "פתרון המבחן": question stem plus worked solution for every question;
there is no separate printed exam). Part A (mandatory): Q1 (20%). Part B: Q2-Q6, a/b parts.
Pages 1-6 and 8-11 are typed/printed solutions; Q4b (pp.7-8) is a HANDWRITTEN page (stem + solution) of unknown
author, inserted in place of a printed solution. Both source trees hold the identical file.

Transcription notes
- Q1 plot (p.2), Q4b sketches (p.7) and the Q6b region sketch (p.10) are shipped as figures inside the solutions.
- Q3b: the stem on the page is only the words "חשב את האינטגרל"; the integrand is taken from the first line of the
  solution (the integral of (x+1)arctan x).
- Q4a: the official proof divides by a2, i.e. assumes a2 != 0; transcribed as printed.
- Q4b (handwritten): the set-up (washers about x=4, radii, the two integrals) is correct and transcribed, but the
  handwritten arithmetic is wrong: it reaches pi(1184 - 224*sqrt(2)/3) = 3387.9, while sympy (washers AND shells)
  gives 128*pi = 402.1. Final-answer error -> "הפתרון ... עם תיקון" label, solutionSource solved, official False,
  and an ASK_ADIR entry. The antiderivative of 8*sqrt(y) - y is printed with "+ y^2/2"; written here with the
  correct "-" (intermediate slip, logged).
- Q6b: the printed first line lists x=+-1/sqrt2 and x=+-sqrt18 and restricts to x>=0; transcribed as printed.

Q4b blind re-check (solver, 2026-10-18): tools/verify/21A-B/blind_recheck_q4b.py gets 128*pi by shells and by washers.
Checks (tools/verify/21A-B/check.py, sympy): every derivative, limit, extremum, parameter, integral and area matches
the official answer, except the Q4b final value described above. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "21A-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**I.** $x^3-1=(x-1)(x^2+x+1)$, $D(f)=\{x\in\mathbb{R}:x\neq1\}$,
$$\lim_{x\to1^+}f(x)=\lim_{x\to1^+}\frac{x^4}{x^3-1}=+\infty,\qquad \lim_{x\to1^-}f(x)=\lim_{x\to1^-}\frac{x^4}{x^3-1}=-\infty$$
לכן $x=1$ נקודת אי-רציפות מסוג שני. $x=1$ הוא אסימפטוטה אנכית,
$$a=\lim_{x\to\infty}\frac{f(x)}{x}=\lim_{x\to\infty}\frac{x^3}{x^3-1}=1,\qquad b=\lim_{x\to\infty}\left(f(x)-ax\right)=\lim_{x\to\infty}\left(\frac{x^4}{x^3-1}-x\right)=\lim_{x\to\infty}\frac{x}{x^3-1}=0$$
$y=x$ הוא אסימפטוטה משופעת.
תחום ההגדרה אינו סימטרי ביחס ל-$0$ לכן הפונקציה אינה זוגית ואינה אי-זוגית.
**II.**
$$f'(x)=\frac{4x^3(x^3-1)-x^4\cdot3x^2}{(x^3-1)^2}=\frac{x^6-4x^3}{(x^3-1)^2}=\frac{x^3(x^3-4)}{(x^3-1)^2}$$
$f'(x)=0$ כאשר $x=0$ או $x=\sqrt[3]{4}$.
טבלת סימנים של $f'$: חיובית ב-$x<0$ (עולה), שלילית ב-$0<x<1$ (יורדת), שלילית ב-$1<x<\sqrt[3]{4}$ (יורדת), חיובית ב-$x>\sqrt[3]{4}$ (עולה).
הנקודה $x=\sqrt[3]{4}$ היא נקודת מינימום מקומי ו-$f\left(\sqrt[3]{4}\right)=\frac{4\sqrt[3]{4}}{3}$.
הנקודה $x=0$ היא נקודת מקסימום מקומי ו-$f(0)=0$.
**III.**
$$f''(x)=\left(\frac{x^6-4x^3}{(x^3-1)^2}\right)'=\frac{(6x^5-12x^2)(x^3-1)^2-(x^6-4x^3)\cdot2(x^3-1)\cdot3x^2}{(x^3-1)^4}=$$
$$=\frac{(6x^5-12x^2)(x^3-1)-(x^6-4x^3)6x^2}{(x^3-1)^3}=\frac{6x^5+12x^2}{(x^3-1)^3}=\frac{6x^2(x^3+2)}{(x^3-1)^3}$$
$6x^2(x^3+2)=0$ כאשר $x=-\sqrt[3]{2}$ או $x=0$.
טבלת סימנים של $f''$: חיובית ב-$x<-\sqrt[3]{2}$ (קמורה (∪)), שלילית ב-$-\sqrt[3]{2}<x<0$ וב-$0<x<1$ (קעורה (∩)), חיובית ב-$x>1$ (קמורה (∪)).
הנקודה $\left(-\sqrt[3]{2},-\frac{2\sqrt[3]{2}}{3}\right)$ היא נקודת הפיתול של הפונקציה, $f\left(-\sqrt[3]{2}\right)=-\frac{2\sqrt[3]{2}}{3}$.
![גרף הפונקציה f(x)=x^4/(x^3-1) עם האסימפטוטה האנכית x=1 והאסימפטוטה המשופעת y=x (מקווקוות)](images/exams/21A-B-Q1-graph.png)
"""

SOL2A = r"""
$$\lim_{x\to+\infty}\left(\frac{x^3}{x^2-x+2}+ax+b\right)=\lim_{x\to+\infty}\left(\frac{x^3+ax^3-ax^2+2ax+bx^2-bx+2b}{x^2-x+2}\right)=$$
$$\lim_{x\to+\infty}\left(\frac{(a+1)x^3+(b-a)x^2+(2a-b)x+2b}{x^2-x+2}\right)\ \{a=-1\}\ \left[\frac{\infty}{\infty}\right]=$$
$$=\lim_{x\to+\infty}\left(\frac{(b-a)+\frac{2a-b}{x}+\frac{2b}{x^2}}{1-\frac{1}{x}+\frac{2}{x^2}}\right)=0$$
לכן $a=b=-1$
"""

SOL2B = r"""
$$\lim_{x\to3^{\pm}}\frac{x|x-3|}{(x^2-4x+3)\arcsin\left(\frac{x}{5}\right)}=\lim_{x\to3^{\pm}}\frac{\pm x(x-3)}{(x-3)(x-1)\arcsin\left(\frac{x}{5}\right)}=$$
$$\lim_{x\to3^{\pm}}\frac{\pm x}{(x-1)\arcsin\left(\frac{x}{5}\right)}=\pm\frac{3}{2\arcsin\frac{3}{5}}$$
**נקודה $x=3$ הינה נקודת אי-רציפות מסוג הראשון.**
$$\lim_{x\to1^{\pm}}\frac{x|x-3|}{(x^2-4x+3)\arcsin\left(\frac{x}{5}\right)}=\lim_{x\to1^{\pm}}\frac{x|x-3|}{(x-3)(x-1)\arcsin\left(\frac{x}{5}\right)}=\mp\infty$$
**נקודה $x=1$ הינה נקודת אי-רציפות מסוג השני.**
$$\lim_{x\to0^{\pm}}\frac{x|x-3|}{(x^2-4x+3)\arcsin\left(\frac{x}{5}\right)}=\lim_{x\to0^{\pm}}\frac{5x|x-3|}{(x-3)(x-1)\arcsin\left(\frac{x}{5}\right)5}=$$
$$\lim_{x\to0^{\pm}}\frac{|x-3|}{(x-3)(x-1)}\lim_{x\to0^{\pm}}\frac{5x}{\arcsin\left(\frac{x}{5}\right)5}=5$$
**נקודה $x=0$ הינה נקודת אי רציפות סליקה.**
"""

SOL3A = r"""
$$\lim_{x\to0}\frac{\sqrt{1+\sin\frac{x}{2}}-\sqrt{1-\sin\frac{x}{2}}}{x}=\lim_{x\to0}\frac{\left(\sqrt{1+\sin\frac{x}{2}}-\sqrt{1-\sin\frac{x}{2}}\right)\left(\sqrt{1+\sin\frac{x}{2}}+\sqrt{1-\sin\frac{x}{2}}\right)}{x\left(\sqrt{1+\sin\frac{x}{2}}+\sqrt{1-\sin\frac{x}{2}}\right)}=$$
$$=\lim_{x\to0}\frac{2\sin\frac{x}{2}}{x\left(\sqrt{1+\sin\frac{x}{2}}+\sqrt{1-\sin\frac{x}{2}}\right)}=\lim_{x\to0}\frac{\sin\frac{x}{2}}{\frac{x}{2}}\cdot\frac{1}{\sqrt{1+\sin\frac{x}{2}}+\sqrt{1-\sin\frac{x}{2}}}=\frac{1}{2}$$
"""

SOL3B = r"""
$$\int(x+1)\arctan x\,dx=\begin{bmatrix}u=\arctan x& u'=\frac{1}{1+x^2}\\ v'=x+1& v=\int(x+1)dx=\frac{x^2}{2}+x\end{bmatrix}=\left(\frac{x^2}{2}+x\right)\arctan x-\int\frac{1}{1+x^2}\left(\frac{x^2}{2}+x\right)dx=$$
$$=\left(\frac{x^2}{2}+x\right)\arctan x-\frac{1}{2}\int\frac{x^2+2x}{x^2+1}dx=\left(\frac{x^2}{2}+x\right)\arctan x-\frac{1}{2}\int\left(1+\frac{2x-1}{x^2+1}\right)dx=$$
$$=\left(\frac{x^2}{2}+x\right)\arctan x-\frac{1}{2}\left(x+\int\frac{2x}{x^2+1}dx-\int\frac{1}{x^2+1}dx\right)=$$
$$=\left(\frac{x^2}{2}+x\right)\arctan x-\frac{1}{2}\left(x+\ln\left(x^2+1\right)-\arctan x\right)=$$
$$=\left(\frac{x^2}{2}+x+\frac{1}{2}\right)\arctan x-\frac{x}{2}-\frac{\ln\left(x^2+1\right)}{2}+c$$
"""

SOL4A = r"""
על פי משפט הערך הממוצע של לגרנז' קיימת נקודה $c\in(a,b)$ בה מתקיים
$$\frac{f(b)-f(a)}{b-a}=f'(c)\ \Rightarrow\ \frac{\left(a_2b^2+a_1b+a_0\right)-\left(a_2a^2+a_1a+a_0\right)}{b-a}=2a_2c+a_1$$
$$\Rightarrow\ \frac{a_2\left(b^2-a^2\right)+a_1(b-a)}{b-a}=2a_2c+a_1\ \Rightarrow\ a_2(a+b)+a_1=2a_2c+a_1\ \Rightarrow\ c=\frac{a+b}{2}\quad\left(a_2\neq0\right)$$
"""

SOL4B = r"""
**הפתרון בכתב היד במקור, עם תיקון:** ההצבה (שיטת הטבעות סביב $x=4$, הרדיוסים ושני האינטגרלים) נכונה ומועתקת כאן כפי שהיא, אך החישוב הסופי בכתב היד שגוי: בכתב היד התקבל $\pi\left(1184-\frac{224}{3}\sqrt{2}\right)\approx3387.9$. הערך הנכון הוא $V=128\pi\approx402.1$ (נבדק בשתי שיטות: טבעות וקליפות). להלן הפתרון עם החישוב המתוקן.
ראשית, נמצא את נקודות החיתוך של הקווים.
$$x^2=2x+8\iff x^2-2x-8=0\iff(x-4)(x+2)=0$$
ולכן נקבל $x=-2$ ו-$x=4$.
![שרטוט התחום הכלוא בין y=x^2, y=2x+8 ו-x=0 (משמאל) והגוף המתקבל מסיבוב סביב x=4 (מימין)](images/exams/21A-B-Q4b-sketch.png)
ברור לנו שכל חתך של הגוף יתקבל בצורת טבעת.
הרדיוס הפנימי הוא: $r=4-\sqrt{y}$.
כאשר $y\in[0,8]$, הרדיוס החיצוני הוא $R=4$.
כאשר $y\in[8,16]$, הרדיוס החיצוני הוא $R=4-\left(\frac{1}{2}y-4\right)$, כלומר $R=8-\frac{1}{2}y$.
מכאן נבחין שהנפח המבוקש ניתן לחישוב בתור:
$$V=\pi\int_0^8\left[4^2-\left(4-\sqrt{y}\right)^2\right]dy+\pi\int_8^{16}\left[\left(8-\frac{1}{2}y\right)^2-\left(4-\sqrt{y}\right)^2\right]dy$$
$$=\pi\left(\int_0^8\left[16-\left(16-8y^{\frac12}+y\right)\right]dy+\int_8^{16}\left[64-8y+\frac{1}{4}y^2-\left(16-8\sqrt{y}+y\right)\right]dy\right)$$
$$=\pi\left(\int_0^8\left[8y^{\frac12}-y\right]dy+\int_8^{16}\left[48-9y+\frac{1}{4}y^2+8y^{\frac12}\right]dy\right)$$
$$=\pi\left(\left(\frac{16}{3}y^{\frac32}-\frac{y^2}{2}\right)\Big|_0^8+\left(48y-\frac{9}{2}y^2+\frac{1}{12}y^3+\frac{16}{3}y^{\frac32}\right)\Big|_8^{16}\right)$$
**החישוב המתוקן:**
$$\int_0^8\left[8y^{\frac12}-y\right]dy=\frac{256\sqrt{2}}{3}-32,\qquad \int_8^{16}\left[48-9y+\frac{1}{4}y^2+8y^{\frac12}\right]dy=160-\frac{256\sqrt{2}}{3}$$
$$V=\pi\left(\frac{256\sqrt{2}}{3}-32+160-\frac{256\sqrt{2}}{3}\right)=128\pi\approx402.1$$
"""

SOL5A = r"""
ראשית נשים לב לכך ש
$$f(x)=x^6-2x^2+x\ \Rightarrow\ f'(x)=6x^5-4x+1$$
בנוסף, מתקיים $f(0)=f(1)=0$. על-פי משפט רול קיימת נקודה $x_0\in(0,1)$ בה מתקיים
$$6x_0^5-4x_0+1=f'(x_0)=0$$
"""

SOL5B = r"""
$$\lim_{x\to0}\left(2\cdot\frac{1-\cos x}{x^4}-\frac{1}{x^2}\right)=\lim_{x\to0}\frac{2-2\cos x-x^2}{x^4}=\lim_{x\to0}\frac{-2x+2\sin x}{4x^3}=$$
$$=\frac{1}{2}\lim_{x\to0}\frac{-x+\sin x}{x^3}=\frac{1}{2}\lim_{x\to0}\frac{-1+\cos x}{3x^2}=-\frac{1}{6}\lim_{x\to0}\frac{1-\cos x}{x^2}=-\frac{1}{6}\lim_{x\to0}\frac{2\sin^2(x/2)}{x^2}=$$
$$=-\frac{1}{12}\lim_{x\to0}\frac{\sin^2(x/2)}{(x/2)^2}=-\frac{1}{12}$$
"""

SOL6A = r"""
ראשית נציין שהפונקציה מוגדרת לכל $x$ ממשי. נמצא נקודות קריטיות בתוך הקטע:
$$f'(x)=\frac{2x-2}{3\sqrt[3]{(x^2-2x)^2}}$$
ומכאן ברור שהנגזרת מתאפסת בנק' $x=1$ ולא קיימת בנק' $x=0$ ו-$x=2$ בתוך הקטע. בנוסף לזאת, יש להוסיף לנקודות האלו נקודות הקצה וכתוצאה מכך כל הנקודות החשודות כאן יהיו: $x=1,\ x=0,\ x=2,\ x=-1$ ו-$x=3$.
$$f(0)=\sqrt[3]{x^2-2x}=0,\quad f(1)=\sqrt[3]{x^2-2x}=-1,\quad f(2)=\sqrt[3]{x^2-2x}=0,\quad f(-1)=\sqrt[3]{x^2-2x}=\sqrt[3]{3},\quad f(3)=\sqrt[3]{x^2-2x}=\sqrt[3]{3}$$
$$\Rightarrow\ \begin{cases}f_{\min}=f(1)=-1\\ f_{\max}=f(-1)=f(3)=\sqrt[3]{3}\end{cases}$$
"""

SOL6B = r"""
![הרביע הראשון: הגרפים y=4x^2, y=x^2/9 והישר y=2, עם נקודות החיתוך x=1/sqrt(2) ו-x=sqrt(18)](images/exams/21A-B-Q6b-region.png)
$$y=4x^2,\ y=\frac{x^2}{9},\ y=2$$
$$4x^2=\frac{x^2}{9},\quad x=0,\qquad 4x^2=2,\quad x=\pm\frac{1}{\sqrt{2}},\qquad \frac{x^2}{9}=2,\quad x=\pm\sqrt{18},\qquad x\ge0$$
$$S=\int_0^{\frac{1}{\sqrt{2}}}\left(4x^2-\frac{x^2}{9}\right)dx+\int_{\frac{1}{\sqrt{2}}}^{\sqrt{18}}\left(2-\frac{x^2}{9}\right)dx=$$
$$=\left(4\frac{x^3}{3}-\frac{x^3}{27}\right)\Big|_0^{\frac{1}{\sqrt{2}}}+\left(2x-\frac{x^3}{27}\right)\Big|_{\frac{1}{\sqrt{2}}}^{\sqrt{18}}=$$
$$=\left(4\frac{\left(\frac{1}{\sqrt{2}}\right)^3}{3}-\frac{\left(\frac{1}{\sqrt{2}}\right)^3}{27}\right)+\left(2\sqrt{18}-\frac{\sqrt{18}^3}{27}\right)-\left(2\left(\frac{1}{\sqrt{2}}\right)-\frac{\left(\frac{1}{\sqrt{2}}\right)^3}{27}\right)=$$
$$=10\sqrt{2}/3\approx4.714$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=\frac{x^4}{x^3-1}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, נקודות קיצון, "
      "תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "computation", "function_limits",
      r"עבור אילו ערכים של $a$ ו-$b$ מתקיים: $\lim_{x\to+\infty}\left(\frac{x^3}{x^2-x+2}+ax+b\right)=0$.",
      SOL2A, part="א"),

    Q(2, "computation", "continuity",
      r"מצאו את כל נקודות האי-רציפות של הפונקציה $f(x)=\frac{x|x-3|}{\left(x^2-4x+3\right)\arcsin\left(\frac{x}{5}\right)}$ ומיינו אותן.",
      SOL2B, part="ב"),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\frac{\sqrt{1+\sin\frac{x}{2}}-\sqrt{1-\sin\frac{x}{2}}}{x}$.",
      SOL3A, part="א"),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int(x+1)\arctan x\,dx$.",
      SOL3B, part="ב"),

    Q(4, "proof", "mean_value_theorems",
      r"הוכיחו שאם $f(x)=a_0+a_1x+a_2x^2$, אז הנקודה $x=c$ שאת קיומה מבטיח משפט הערך הממוצע של לגרנז' נמצאת בדיוק באמצע הקטע $[a,b]$.",
      SOL4A, part="א"),

    Q(4, "computation", "definite_integrals",
      r"מצאו את נפח הגוף המתקבל מסיבוב של התחום הכלוא בין הקווים $y=2x+8,\ y=x^2$ ו-$x=0$ כאשר $x\ge0$ סביב הציר $x=4$. "
      "צייר את התחום המסובב והסבר את פעולותיך!",
      SOL4B, part="ב", points=10, solutionSource="solved", official=False),

    Q(5, "proof", "mean_value_theorems",
      r"הוכיחו כי למשוואה $6x^5-4x+1=0$ יש שורש ממשי אחד לפחות בקטע $(0,1)$.",
      SOL5A, part="א"),

    Q(5, "computation", "lhopital_taylor",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\left(2\cdot\frac{1-\cos x}{x^4}-\frac{1}{x^2}\right)$.",
      SOL5B, part="ב"),

    Q(6, "computation", "extrema_optimization",
      r"מצאו אקסטרמומים מוחלטים של $f(x)=\sqrt[3]{x^2-2x}$ בקטע $[-1,3]$.",
      SOL6A, part="א"),

    Q(6, "computation", "definite_integrals",
      r'חשבו את שטח התחום הנמצא ברביע הראשון החסום ע"י הקווים $y=4x^2,\ y=\frac{x^2}{9},\ y=2$.',
      SOL6B, part="ב"),
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


# ===== Q1: f = x^4/(x^3-1) =====
f1 = x**4/(x**3 - 1)
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
c2 = sp.cbrt(2)
c4 = sp.cbrt(4)
assert same(f1p, x**3*(x**3 - 4)/(x**3 - 1)**2) and same(f1pp, 6*x**2*(x**3 + 2)/(x**3 - 1)**3)
assert same(f1.subs(x, c4), 4*c4/3) and f1.subs(x, 0) == 0 and same(f1.subs(x, -c2), -2*c2/3)
assert f1p.subs(x, R(1, 2)) < 0 and f1p.subs(x, -1) > 0 and f1p.subs(x, R(6, 5)) < 0 and f1p.subs(x, 2) > 0
assert f1pp.subs(x, -2) > 0 and f1pp.subs(x, -1) < 0 and f1pp.subs(x, R(1, 2)) < 0 and f1pp.subs(x, 2) > 0   # only -2^(1/3) changes sign
assert sp.limit(f1/x, x, sp.oo) == 1 and sp.limit(f1 - x, x, sp.oo) == 0
assert sp.limit(f1, x, 1, '+') == sp.oo and sp.limit(f1, x, 1, '-') == -sp.oo
f1p_bads = [x**3*(x**3 - 4)/(x**3 + 1)**2, x**3*(x**3 + 4)/(x**3 - 1)**2, x**2*(x**3 - 4)/(x**3 - 1)**2]

add(1,
    rubric=rub(("תחום הגדרה $x\\neq1$, ושהפונקציה אינה זוגית ואינה אי-זוגית", 2),
               ("נגזרת $f'(x)=\\frac{x^3\\left(x^3-4\\right)}{\\left(x^3-1\\right)^2}$ וטבלת סימן", 4),
               ("קיצון: מקסימום ב-$x=0$ ומינימום ב-$x=\\sqrt[3]{4}$ וערכיהם", 4),
               ("נגזרת שנייה $f''(x)=\\frac{6x^2\\left(x^3+2\\right)}{\\left(x^3-1\\right)^3}$, קמירות ונקודת הפיתול $x=-\\sqrt[3]{2}$", 4),
               ("אסימפטוטות: $x=1$ אנכית ו-$y=x$ משופעת", 4),
               ("שרטוט הגרף בהתאם לנתונים", 2)),
    rubricSource="ai-verified",
    pitfalls=["לסווג את $x=0$ כנקודת פיתול רק כי $f''(0)=0$. $f''$ אינה משנה סימן שם (גורם $x^2$).",
              "לשכוח שבסביבת $x=1$ הפונקציה לא מוגדרת, ולחבר את הענפים בטבלת הסימן.",
              "לטעות באסימפטוטה המשופעת: $b=\\lim\\frac{x}{x^3-1}=0$ ולא $1$."],
    steps=[
        chx("מהי הנגזרת של $f(x)=\\frac{x^4}{x^3-1}$?", x**3*(x**3 - 4)/(x**3 - 1)**2, f1p_bads, lambda e: same(e, f1p),
            "כלל המנה: $\\frac{4x^3\\left(x^3-1\\right)-3x^6}{\\left(x^3-1\\right)^2}=\\frac{x^6-4x^3}{\\left(x^3-1\\right)^2}$ (נבדק ב-sympy)."),
        num("באיזה ערך חיובי של $x$ מתאפסת הנגזרת? (עשרוני)", c4, "$x^3=4$ ולכן $x=\\sqrt[3]{4}\\approx1.5874$ (וגם $x=0$)."),
        num("מהו $f\\left(\\sqrt[3]{4}\\right)$ בנקודת המינימום המקומי? (עשרוני)", 4*c4/3, "$f\\left(\\sqrt[3]{4}\\right)=\\frac{4\\sqrt[3]{4}}{3}\\approx2.1165$ (sympy)."),
        ch("מהן נקודות הפיתול של $f$?", "רק $x=-\\sqrt[3]{2}$",
           ["$x=-\\sqrt[3]{2}$ ו-$x=0$", "רק $x=0$", "אין נקודות פיתול"],
           "$f''=\\frac{6x^2\\left(x^3+2\\right)}{\\left(x^3-1\\right)^3}$ משנה סימן רק ב-$-\\sqrt[3]{2}$; ב-$x=0$ הגורם $x^2$ אינו משנה סימן (נבדק ב-sympy)."),
        ch("מהן האסימפטוטות של $f$?", "$x=1$ אנכית ו-$y=x$ משופעת",
           ["$x=1$ אנכית בלבד", "$y=x$ משופעת בלבד", "$x=1$ אנכית ו-$y=x+1$ משופעת"],
           "$\\frac{f}{x}\\to1$ ו-$f-x=\\frac{x}{x^3-1}\\to0$; ב-$x=1$ הגבולות אינסופיים (sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: x^3/(x^2-x+2) + a x + b -> 0 =====
assert same(x**3 - ((x + 1)*(x**2 - x + 2) + (-x - 2)), 0)
tail = x**3/(x**2 - x + 2) - x - 1
assert sp.limit(tail, x, sp.oo) == 0 and sp.limit(tail, x, -sp.oo) == 0
for av, bv in ((-1, 0), (0, -1), (-1, -2), (-2, -1)):
    assert sp.limit(x**3/(x**2 - x + 2) + av*x + bv, x, sp.oo) != 0

add(2, "א",
    rubric=rub(("חיבור למכנה משותף וקבלת המונה $(a+1)x^3+(b-a)x^2+(2a-b)x+2b$", 3),
               ("דרישת מעלת המונה: $a+1=0$ ולכן $a=-1$", 3),
               ("דרישה שהגבול יתאפס: $b-a=0$ ולכן $b=-1$", 3),
               ("אימות שהגבול אכן $0$", 1)),
    rubricSource="ai-verified",
    pitfalls=["לדרוש רק $a+1=0$ ולשכוח את התנאי השני, $b-a=0$.",
              "לבלבל בין דרישת גבול $0$ לדרישת גבול סופי כלשהו.",
              "טעות בכפל $ax\\cdot\\left(x^2-x+2\\right)$ בחיבור למכנה משותף."],
    steps=[
        ch("איזה תנאי על המקדמים מבטיח שהגבול של המנה בין המונה $(a+1)x^3+(b-a)x^2+\\dots$ למכנה $x^2-x+2$ יהיה $0$?",
           "מקדמי $x^3$ ו-$x^2$ במונה מתאפסים, כלומר $a+1=0$ ו-$b-a=0$",
           ["רק מקדם $x^3$ מתאפס", "רק מקדם $x^2$ מתאפס", "מקדם $x^3$ שווה למקדם $x^2$"],
           "מונה מדרגה $\\ge2$ מול מכנה מדרגה $2$ נותן גבול שאינו $0$; רק כשהמונה מדרגה $\\le1$ הגבול $0$ (נבדק ב-sympy למקרים הדוגמה)."),
        num("מהו $a$?", -1, "$a+1=0$ ולכן $a=-1$."),
        num("מהו $b$?", -1, "$b-a=0$ ולכן $b=a=-1$; גם $\\frac{x^3}{x^2-x+2}-x-1\\to0$ (sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: discontinuities of x|x-3| / ((x^2-4x+3) arcsin(x/5)) =====
def f2(v):
    v = mp.mpf(v)
    return v*abs(v - 3)/((v**2 - 4*v + 3)*mp.asin(v/5))

e_ = mp.mpf('1e-9')
assert abs(f2(e_) - 5) < 1e-6 and abs(f2(-e_) - 5) < 1e-6
k3 = 3/(2*mp.asin(mp.mpf(3)/5))
assert abs(f2(3 + e_) - k3) < 1e-5 and abs(f2(3 - e_) + k3) < 1e-5
assert abs(f2(1 + e_)) > 1e8 and abs(f2(1 - e_)) > 1e8 and f2(1 + e_)*f2(1 - e_) < 0

add(2, "ב",
    rubric=rub(("פירוק המכנה $x^2-4x+3=(x-1)(x-3)$ וזיהוי הנקודות החשודות $0,1,3$", 2),
               ("$x=3$: גבולות חד-צדדיים $\\pm\\frac{3}{2\\arcsin\\frac35}$, סופיים ושונים, ממין ראשון", 3),
               ("$x=1$: גבולות אינסופיים, ממין שני", 2),
               ("$x=0$: הגבול $5$, אי-רציפות סליקה", 3)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את $x=0$, שבה $\\arcsin\\frac{x}{5}=0$ במכנה.",
              "לא לפצל את $|x-3|$ לשני צדדים כשבודקים את $x=3$.",
              "לסווג את $x=1$ כסליקה בלי לבדוק שהמונה אינו מתאפס שם."],
    steps=[
        num("מהו $\\lim_{x\\to0}f(x)$?", 5, "$\\frac{|x-3|}{(x-3)(x-1)}\\to1$ ו-$\\frac{x}{\\arcsin\\frac{x}{5}}\\to5$ (נבדק מספרית משני הצדדים)."),
        num("מהו הגבול הימני $\\lim_{x\\to3^+}f(x)=\\frac{3}{2\\arcsin\\frac35}$? (עשרוני)", k3,
            "$\\arcsin0.6\\approx0.6435$ ולכן הגבול $\\approx2.331$, והגבול השמאלי $-2.331$ (נבדק מספרית)."),
        ch("מהו סוג אי-הרציפות ב-$x=3$?", "ממין ראשון (גבולות חד-צדדיים סופיים ושונים)",
           ["ממין שני", "סליקה", "אין שם אי-רציפות"],
           "הגבולות $\\pm2.331$ סופיים ושונים."),
        ch("מהו סוג אי-הרציפות ב-$x=1$?", "ממין שני (גבולות חד-צדדיים אינסופיים)",
           ["ממין ראשון", "סליקה", "אין שם אי-רציפות"],
           "המכנה מתאפס והמונה אינו, ולכן $|f|\\to\\infty$ משני הצדדים (נבדק מספרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: lim (sqrt(1+sin(x/2)) - sqrt(1-sin(x/2)))/x =====
def f3(v):
    v = mp.mpf(v)
    s_ = mp.sin(v/2)
    return (mp.sqrt(1 + s_) - mp.sqrt(1 - s_))/v

assert abs(f3('1e-8') - mp.mpf(1)/2) < 1e-6 and abs(f3('-1e-8') - mp.mpf(1)/2) < 1e-6
vv = mp.mpf('0.7'); s_ = mp.sin(vv/2)
assert abs((mp.sqrt(1 + s_) - mp.sqrt(1 - s_))*(mp.sqrt(1 + s_) + mp.sqrt(1 - s_)) - 2*s_) < 1e-40
assert sp.limit((sp.sqrt(1 + sp.sin(x/2)) + sp.sqrt(1 - sp.sin(x/2))), x, 0) == 2

add(3, "א",
    rubric=rub(("כפל בצמוד: $\\sqrt{1+\\sin\\frac x2}+\\sqrt{1-\\sin\\frac x2}$", 3),
               ("פישוט המונה ל-$2\\sin\\frac x2$", 3),
               ("הגבול המפורסם $\\frac{\\sin\\frac x2}{x/2}\\to1$ וגבול המכנה $2$", 2),
               ("ערך הגבול $\\frac12$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להפעיל לופיטל ישירות על שורשים מקוננים ולסבך את החישוב.",
              "לשכוח שהמכנה אחרי הצמוד גם מכיל את $x$.",
              "לכתוב $\\frac{\\sin(x/2)}{x}\\to1$ במקום $\\frac12$."],
    steps=[
        ch("איזו שיטה משתמש הפתרון הרשמי?", "כפל בצמוד ואז הגבול המפורסם של $\\frac{\\sin u}{u}$",
           ["הצבת $x=\\frac1u$", "קריטריון השוואה (סנדוויץ')", "פיתוח טיילור מסדר $3$ בלבד"],
           "ההפרש של שורשים מתפשט בעזרת הצמוד לביטוי $2\\sin\\frac{x}{2}$."),
        num("מהו הגבול של גורם המכנה $\\sqrt{1+\\sin\\frac x2}+\\sqrt{1-\\sin\\frac x2}$ כאשר $x\\to0$?", 2, "$\\sqrt1+\\sqrt1=2$ (sympy)."),
        num("מהו $\\lim_{x\\to0}\\frac{2\\sin\\frac x2}{x}$?", 1, "$\\frac{2\\sin(x/2)}{x}=\\frac{\\sin(x/2)}{x/2}\\to1$."),
        num("מהו ערך הגבול? (עשרוני)", R(1, 2), "$\\frac{1}{2}$ (נבדק מספרית משני הצדדים)."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: int (x+1) arctan x =====
g3b = (x + 1)*sp.atan(x)
F3b = (x**2/2 + x + R(1, 2))*sp.atan(x) - x/2 - sp.log(x**2 + 1)/2
F3b_bads = [(x**2/2 + x + R(1, 2))*sp.atan(x) - x/2 + sp.log(x**2 + 1)/2, (x**2/2 + x)*sp.atan(x) - x/2 - sp.log(x**2 + 1)/2,
            (x**2/2 + x + R(1, 2))*sp.atan(x) - x - sp.log(x**2 + 1)/2]
pts3 = [R(1, 3), 1, 2]
assert dnum(F3b, g3b, pts3) and not any(dnum(e, g3b, pts3) for e in F3b_bads)
assert same((x**2 + 2*x)/(x**2 + 1), 1 + (2*x - 1)/(x**2 + 1)) and ((x**2 + 2*x)/(x**2 + 1)).subs(x, 1) == R(3, 2)

add(3, "ב",
    rubric=rub(("בחירה באינטגרציה בחלקים: $u=\\arctan x$, $dv=(x+1)dx$", 2),
               ("חישוב $u'=\\frac{1}{1+x^2}$ ו-$v=\\frac{x^2}{2}+x$", 2),
               ("חילוק פולינומים $\\frac{x^2+2x}{x^2+1}=1+\\frac{2x-1}{x^2+1}$", 3),
               ("אינטגרציה של הרכיבים ואיחוד $\\arctan x$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לבחור $u=x+1$ ו-$dv=\\arctan x\\,dx$ ולהסתבך באינטגרל של $\\arctan$.",
              "לשכוח לחלק פולינומים לפני שמפרקים את $\\frac{x^2+2x}{x^2+1}$.",
              "לשכוח שהאיבר $-\\frac12\\left(-\\arctan x\\right)$ מצטרף ל-$\\arctan x$ עם מקדם $\\frac12$."],
    steps=[
        ch("איזו בחירה באינטגרציה בחלקים משתמש הפתרון הרשמי?", "$u=\\arctan x,\\ dv=(x+1)\\,dx$",
           ["$u=x+1,\\ dv=\\arctan x\\,dx$", "$u=(x+1)\\arctan x$ בלי $dv$", "$u=\\frac{1}{1+x^2},\\ dv=(x+1)\\,dx$"],
           "גוזרים את $\\arctan$ (נהפך לשבר רציונלי) ומאנטגרלים את הפולינום."),
        num("מהו הערך של $v(2)$ כאשר $v=\\int(x+1)\\,dx=\\frac{x^2}{2}+x$?", 4, "$\\frac{4}{2}+2=4$."),
        num("מהו הערך של $\\frac{x^2+2x}{x^2+1}$ בנקודה $x=1$, והאם הוא שווה ל-$1+\\frac{2x-1}{x^2+1}$? (עשרוני)", R(3, 2),
            "$\\frac{3}{2}=1+\\frac{1}{2}$; הזהות נבדקה סימבולית."),
        chx("איזו קדומה נכונה?", F3b, F3b_bads, lambda e: dnum(e, g3b, pts3),
            "$\\left(\\frac{x^2}{2}+x+\\frac12\\right)\\arctan x-\\frac{x}{2}-\\frac{\\ln\\left(x^2+1\\right)}{2}$; הנגזרת של כל אחת מהאחרות שונה (נבדק מספרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: Lagrange point of a quadratic is the midpoint =====
a0, a1, a2, aa, bb, cc = sp.symbols('a0 a1 a2 aa bb cc')
fq = a0 + a1*x + a2*x**2
slope = sp.simplify((fq.subs(x, bb) - fq.subs(x, aa))/(bb - aa))
assert same(slope, a2*(aa + bb) + a1)
assert sp.solve(sp.Eq(a2*(aa + bb) + a1, 2*a2*cc + a1), cc) == [(aa + bb)/(2)]
fe = 3*x**2 + 2*x + 1
assert (fe.subs(x, 5) - fe.subs(x, 1))/4 == 20 and sp.solve(sp.Eq(sp.diff(fe, x), 20), x) == [3]
L4a = ["לפי משפט לגרנז' קיימת $c\\in(a,b)$ כך ש-$\\frac{f(b)-f(a)}{b-a}=f'(c)$.",
       "הצד השמאלי שווה $a_2(a+b)+a_1$, והצד הימני שווה $2a_2c+a_1$.",
       "משוואת שני הצדדים נותנת $a_2(a+b)=2a_2c$, ולכן $c=\\frac{a+b}{2}$ (כאשר $a_2\\neq0$)."]
L4a_b = list(L4a)
L4a_b[1] = "הצד השמאלי שווה $a_2(a-b)+a_1$, והצד הימני שווה $2a_2c+a_1$."

add(4, "א",
    rubric=rub(("ניסוח משפט לגרנז' והצבת $f(x)=a_0+a_1x+a_2x^2$", 2),
               ("חישוב הצד השמאלי $a_2(a+b)+a_1$ (הוצאת $b-a$ כגורם משותף)", 3),
               ("חישוב $f'(c)=2a_2c+a_1$", 2),
               ("השוואה ופתרון $c=\\frac{a+b}{2}$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לצמצם בלי לציין ש-$a_2\\neq0$ (אם $a_2=0$ כל נקודה מקיימת את המשפט).",
              "טעות בפירוק $b^2-a^2=(b-a)(b+a)$.",
              "לשכוח שהנגזרת $f'(c)$ מחושבת ב-$c$ ולא ב-$b$."],
    steps=[
        num("עבור $f(x)=3x^2+2x+1$ בקטע $[1,5]$, מהו $\\frac{f(5)-f(1)}{5-1}$?", 20, "$\\frac{86-6}{4}=20$ (נבדק ב-sympy)."),
        num("עבור אותה פונקציה, באיזו נקודה $c$ מתקיים $f'(c)=20$?", 3, "$6c+2=20$ ולכן $c=3$, וזהו אמצע הקטע $[1,5]$."),
        order("סדרו את שלבי ההוכחה.", L4a, "לגרנז', חישוב שני הצדדים, ובסוף השוואה ופתרון."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L4a_b, 1,
                "$\\frac{a_2\\left(b^2-a^2\\right)}{b-a}=a_2(a+b)$ ולא $a_2(a-b)$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: washers/shells about x = 4 =====
V4 = 2*mp.pi*mp.quad(lambda v: (4 - v)*(2*v + 8 - v**2), [0, 4])
V4w = mp.pi*(mp.quad(lambda y: 16 - (4 - mp.sqrt(y))**2, [0, 8]) +
             mp.quad(lambda y: (8 - y/2)**2 - (4 - mp.sqrt(y))**2, [8, 16]))
assert abs(V4 - 128*mp.pi) < 1e-20 and abs(V4w - 128*mp.pi) < 1e-20
assert sp.solve(x**2 - 2*x - 8, x) in ([-2, 4], [4, -2])
assert 4 - mp.sqrt(9) == 1 and 8 - mp.mpf(10)/2 == 3
bad_vals = [mp.pi*(1184 - mp.mpf(224)/3*mp.sqrt(2)), 64*mp.pi, 256*mp.pi]
assert all(abs(v - 128*mp.pi) > 1 for v in bad_vals)

add(4, "ב",
    rubric=rub(("נקודות החיתוך $x=-2$ ו-$x=4$ והתחום ($x\\ge0$)", 2),
               ("רדיוסים: פנימי $4-\\sqrt y$, חיצוני $4$ ב-$[0,8]$ ו-$8-\\frac y2$ ב-$[8,16]$", 3),
               ("הצבה בשני האינטגרלים של שיטת הטבעות", 3),
               ("חישוב הערך $V=128\\pi\\approx402.1$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח לפצל את האינטגרל ב-$y=8$, שבו הרדיוס החיצוני משתנה.",
              "להשתמש ב-$y$ כרדיוס במקום המרחק מהציר $x=4$.",
              "טעות חשבונית באינטגרל הסופי. הערך הנכון הוא $128\\pi$ ולא $3387.9$."],
    steps=[
        num("מהו הפתרון החיובי של $x^2=2x+8$?", 4, "$(x-4)(x+2)=0$ ולכן $x=4$ (ו-$x=-2$ מחוץ לתחום $x\\ge0$)."),
        num("מהו הרדיוס הפנימי $r=4-\\sqrt y$ בגובה $y=9$?", 1, "$4-3=1$."),
        num("מהו הרדיוס החיצוני $R=8-\\frac y2$ בגובה $y=10$?", 3, "$8-5=3$."),
        ch("מהו נפח הגוף?", "$128\\pi\\approx402.1$",
           ["$\\pi\\left(1184-\\frac{224\\sqrt2}{3}\\right)\\approx3387.9$", "$64\\pi\\approx201.1$", "$256\\pi\\approx804.2$"],
           "הטבעות נותנות $128\\pi$ וכך גם הקליפות $2\\pi\\int_0^4(4-x)(2x+8-x^2)\\,dx$ (נבדק נומרית בשתי השיטות)."),
    ],
    stepsSource="ai-verified")

# ===== Q5a: Rolle for 6x^5 - 4x + 1 =====
F5 = x**6 - 2*x**2 + x
assert F5.subs(x, 0) == 0 and F5.subs(x, 1) == 0 and same(sp.diff(F5, x), 6*x**5 - 4*x + 1)
assert F5.subs(x, -1) == -2                                                    # [-1,1] does not satisfy f(a)=f(b)
G5 = 6*x**5 - 4*x + 1
assert G5.subs(x, 0) != G5.subs(x, 1)                                           # Rolle cannot be applied to f' itself
L5a = ["נגדיר $f(x)=x^6-2x^2+x$, פונקציה רציפה וגזירה בכל $\\mathbb{R}$, ו-$f'(x)=6x^5-4x+1$.",
       "מתקיים $f(0)=0$ ו-$f(1)=1-2+1=0$.",
       "לפי משפט רול קיימת $x_0\\in(0,1)$ כך ש-$f'(x_0)=6x_0^5-4x_0+1=0$."]
L5a_b = list(L5a)
L5a_b[1] = "מתקיים $f(0)=0$ ו-$f(1)=1-2+1=2$."

add(5, "א",
    rubric=rub(("בחירת פונקציית עזר: הקדומה $f(x)=x^6-2x^2+x$", 3),
               ("בדיקת תנאי רול: רציפות, גזירות ו-$f(0)=f(1)=0$", 3),
               ("חישוב $f'(x)=6x^5-4x+1$", 2),
               ("מסקנה: קיום $x_0\\in(0,1)$ עם $f'(x_0)=0$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להפעיל את משפט רול ישירות על $6x^5-4x+1$: ערכיה בקצוות הם $1$ ו-$3$, לא שווים.",
              "לשכוח לבדוק ש-$f(1)=0$ ולא רק $f(0)=0$.",
              "לבחור קטע שאינו מקיים $f(a)=f(b)$, כמו $[-1,1]$."],
    steps=[
        ch("לאיזו פונקציה ולאיזה קטע מפעיל הפתרון הרשמי את משפט רול?", "$f(x)=x^6-2x^2+x$ בקטע $[0,1]$",
           ["$f(x)=6x^5-4x+1$ בקטע $[0,1]$", "$f(x)=x^6-2x^2+x$ בקטע $[-1,1]$", "$f(x)=x^6-2x^2$ בקטע $[0,1]$"],
           "ל-$f=x^6-2x^2+x$ מתקיים $f(0)=f(1)=0$ ו-$f'=6x^5-4x+1$; לאפשרויות האחרות ערכי הקצוות שונים ($1\\ne3$; $-2\\ne0$; $0\\ne-1$) (נבדק ב-sympy)."),
        num("מהו $f(1)$ עבור $f(x)=x^6-2x^2+x$?", 0, "$1-2+1=0$."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L5a_b, 1, "$f(1)=1-2+1=0$ ולא $2$; בלי $f(1)=f(0)$ אי אפשר להפעיל את משפט רול."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: lim (2(1-cos x)/x^4 - 1/x^2) = -1/12 =====
assert sp.limit(2*(1 - sp.cos(x))/x**4 - 1/x**2, x, 0) == -R(1, 12)
assert sp.limit((x - sp.sin(x))/x**3, x, 0) == R(1, 6) and sp.limit((1 - sp.cos(x))/x**2, x, 0) == R(1, 2)
assert abs((2*(1 - mp.cos(mp.mpf('0.01')))/mp.mpf('0.01')**4 - 1/mp.mpf('0.01')**2) + mp.mpf(1)/12) < 1e-3

add(5, "ב",
    rubric=rub(("מכנה משותף: $\\frac{2-2\\cos x-x^2}{x^4}$ וזיהוי $\\frac00$", 2),
               ("לופיטל ראשון: $\\frac{-2x+2\\sin x}{4x^3}$", 3),
               ("לופיטל נוסף וגבול מפורסם $\\frac{1-\\cos x}{x^2}\\to\\frac12$", 3),
               ("ערך הגבול $-\\frac{1}{12}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להפריד ל-$\\lim\\frac{2(1-\\cos x)}{x^4}-\\lim\\frac{1}{x^2}$: שני הגבולות אינסופיים.",
              "לעצור אחרי לופיטל אחד: הביטוי $\\frac{-x+\\sin x}{x^3}$ עדיין מסוג $\\frac00$.",
              "טעות בסימן הגבול הסופי ($-\\frac1{12}$ ולא $+\\frac1{12}$)."],
    steps=[
        ch("מהי צורת הביטוי $\\frac{2-2\\cos x-x^2}{x^4}$ כאשר $x\\to0$?", "$\\frac00$",
           ["$\\frac{\\infty}{\\infty}$", "$\\infty-\\infty$", "$1^\\infty$"],
           "המונה $2-2\\cos x-x^2\\to0$ והמכנה $x^4\\to0$."),
        num("מהו $\\lim_{x\\to0}\\frac{x-\\sin x}{x^3}$? (עשרוני)", R(1, 6), "לופיטל פעמיים נותן $\\frac{1}{6}$ (sympy)."),
        num("מהו ערך הגבול? (עשרוני)", -R(1, 12), "$\\frac{-2x+2\\sin x}{4x^3}=-\\frac12\\cdot\\frac{x-\\sin x}{x^3}\\to-\\frac{1}{12}\\approx-0.0833$ (נבדק מספרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: abs extrema of cbrt(x^2-2x) on [-1,3] =====
def f6(v):
    v = mp.mpf(v)
    w = v*v - 2*v
    return mp.sign(w)*abs(w)**(mp.mpf(1)/3)

grid6 = [f6(mp.mpf(-1) + mp.mpf(k)/1500) for k in range(0, 6001)]
assert abs(max(grid6) - mp.cbrt(3)) < 1e-9 and abs(min(grid6) + 1) < 1e-9
assert abs(f6(1) + 1) < 1e-30 and f6(0) == 0 and f6(2) == 0 and abs(f6(-1) - mp.cbrt(3)) < 1e-30 and abs(f6(3) - mp.cbrt(3)) < 1e-30

add(6, "א",
    rubric=rub(("נגזרת $f'(x)=\\frac{2x-2}{3\\sqrt[3]{(x^2-2x)^2}}$", 2),
               ("נקודה קריטית $x=1$ ונקודות שבהן הנגזרת אינה קיימת: $x=0,2$", 3),
               ("הוספת קצות הקטע $-1,3$ ורשימת כל הנקודות החשודות", 1),
               ("ערכי $f$ בנקודות: $0,-1,0,\\sqrt[3]{3},\\sqrt[3]{3}$", 2),
               ("מינימום $-1$ ומקסימום $\\sqrt[3]{3}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את $x=0$ ו-$x=2$, שבהן הנגזרת אינה קיימת (המכנה מתאפס).",
              "לשכוח את קצות הקטע ולהסתפק בקיצון מקומי.",
              "לחשב שורש שלישי של מספר שלילי כאילו אינו מוגדר: $\\sqrt[3]{-1}=-1$."],
    steps=[
        num("באיזה ערך $x$ מתאפס המונה של $f'(x)=\\frac{2x-2}{3\\sqrt[3]{(x^2-2x)^2}}$?", 1, "$2x-2=0$ ולכן $x=1$."),
        num("מהו $f(-1)=\\sqrt[3]{x^2-2x}$ בקצה $x=-1$? (עשרוני)", mp.cbrt(3), "$\\sqrt[3]{1+2}=\\sqrt[3]{3}\\approx1.4422$."),
        num("מהו $f(1)$?", -1, "$\\sqrt[3]{1-2}=\\sqrt[3]{-1}=-1$."),
        ch("מהם הערך הגדול ביותר והקטן ביותר של $f$ בקטע $[-1,3]$?",
           "הגדול $\\sqrt[3]{3}$ (ב-$x=-1$ וב-$x=3$) והקטן $-1$ (ב-$x=1$)",
           ["הגדול $0$ והקטן $-1$", "הגדול $\\sqrt[3]{3}$ והקטן $0$", "הגדול $\\sqrt[3]{3}$ רק ב-$x=3$ והקטן $-1$"],
           "הערכים הם $f(-1)=f(3)=\\sqrt[3]{3}$, $f(0)=f(2)=0$, $f(1)=-1$ (נבדק על רשת צפופה)."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: area in the first quadrant =====
S6 = mp.quad(lambda v: 4*v**2 - v**2/9, [0, 1/mp.sqrt(2)]) + mp.quad(lambda v: 2 - v**2/9, [1/mp.sqrt(2), mp.sqrt(18)])
assert abs(S6 - 10*mp.sqrt(2)/3) < 1e-25
S6a = mp.quad(lambda v: 4*v**2 - v**2/9, [0, 1/mp.sqrt(2)])
assert abs(S6a - 35/(54*mp.sqrt(2))) < 1e-25
assert sp.solve(4*x**2 - 2, x) == [-sp.sqrt(2)/2, sp.sqrt(2)/2] and sp.solve(x**2/9 - 2, x) == [-3*sp.sqrt(2), 3*sp.sqrt(2)]

add(6, "ב",
    rubric=rub(("נקודות החיתוך עם $y=2$: $x=\\frac{1}{\\sqrt2}$ ו-$x=\\sqrt{18}$", 3),
               ("פיצול השטח ל-$\\left[0,\\frac{1}{\\sqrt2}\\right]$ ול-$\\left[\\frac{1}{\\sqrt2},\\sqrt{18}\\right]$ עם אינטגרנדים נכונים", 3),
               ("חישוב שני האינטגרלים", 2),
               ("השטח $\\frac{10\\sqrt2}{3}\\approx4.714$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לאנטגרל $4x^2-\\frac{x^2}{9}$ על כל הקטע $\\left[0,\\sqrt{18}\\right]$ בלי להתחשב בקו $y=2$.",
              "לכלול נקודות חיתוך בשלילי ($x<0$) אף שהתחום ברביע הראשון.",
              "טעות בחישוב $\\sqrt{18}^3=54\\sqrt2$."],
    steps=[
        num("מהו $x>0$ שבו $4x^2=2$? (עשרוני)", 1/sp.sqrt(2), "$x=\\frac{1}{\\sqrt2}\\approx0.7071$."),
        num("מהו $x>0$ שבו $\\frac{x^2}{9}=2$? (עשרוני)", sp.sqrt(18), "$x=\\sqrt{18}=3\\sqrt2\\approx4.2426$."),
        num("מהו $\\int_0^{1/\\sqrt2}\\left(4x^2-\\frac{x^2}{9}\\right)dx$? (עשרוני)", 35/(54*mp.sqrt(2)),
            "$\\frac{35}{27}\\cdot\\frac{1}{2\\sqrt2}=\\frac{35}{54\\sqrt2}\\approx0.4583$ (נבדק נומרית)."),
        num("מהו השטח הכולל? (עשרוני)", 10*mp.sqrt(2)/3, "$\\frac{10\\sqrt2}{3}\\approx4.714$ (נבדק נומרית)."),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "21A-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"א, מועד א'",
    "year": 2021,
    "examDate": "",
    "sourceFile": "calculus-1/21A-B solution (image PDF).pdf",
    "solutionFile": "calculus-1/21A-B solution (image PDF).pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

# -*- coding: utf-8 -*-
"""Generator for tools/raw/22A-B.json -- calculus-1 (20151), semester B 2022, moed A (14/06/2022).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22A-B.py

Source: sitting 22A-B, pp.1-10. The file is a worked-solution document titled "solution of moed A 14.06.2022": it carries NO
printed exam header; each question is restated by its author, followed by the solution (typeset, with some hand-drawn sign
tables and a few black handwritten additions in Q6a). The question texts below are the restatements from that file, so
the wording is the file's, not the printed exam's. The author is not identified and the file has no institute header,
so it is shipped as solutionSource student-solution with official False (the triage note listing this sitting as having
no solution was wrong: a full worked solution exists).

Transcription notes
- Q1: restated only as "function investigation f(x)=x^3/(x^2-1)"; the standard task list is written out in the question.
  Points are not printed. The two hand-drawn sign tables (f' and f'') are described in words; the plotted graph on p.3
  is shipped as images/exams/22A-B-Q1-graph.png.
- Q1d: the file prints 'x f''(x)=' before the formula (stray x) and a red cross next to it; the formula itself is correct
  (sympy), transcribed as f''(x).
- Q1e: the slope limit is printed as lim (x^2-1)/x^2 = 1; f(x)/x is x^2/(x^2-1) (also tends to 1); written with the
  correct fraction.
- Q4b: the part label is printed 'a' (copy of Q4a's label); it is the second part of Q4, stored as part ב. The hand-drawn
  region sketch is shipped as images/exams/22A-B-Q4b-sketch.png.
- Q5b: the file's value 1.98 does not match the exact value of the arc-length integral (2.0035, sympy); the
  closed form is right, the decimal evaluation at the end is off. Final-answer error -> labeled fix (the source is not
  official, so the label reads "הפתרון שבמקור (לא רשמי) עם תיקון"), solutionSource solved, official False.
- Blind re-check 2026-10-18 (tools/verify/22A-B/blind_recheck.py): every final answer re-derived independently; all agree
  except Q5b above.
- Q6a: black handwriting added x=1/3 (where f' does not exist) and f(1/3)=0 to the typeset solution; transcribed.

Checks (tools/verify/22A-B/check.py, sympy plus numeric): every derivative, sign table, limit, antiderivative, extremum,
volume and parameter value matches the file's answers; the only disagreement is the Q5b decimal.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22A-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "student-solution", "official": False, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**א. תחום הגדרה:** $D=\{x\in\mathbb{R},\ x\neq\pm1\}$.
**ב. נקודת חיתוך עם צירי הקואורדינטות:** $(0,0)$.
**ג.** $$f'(x)=\frac{3x^2\left(x^2-1\right)-2x^4}{\left(x^2-1\right)^2}=\frac{x^4-3x^2}{\left(x^2-1\right)^2}=\frac{x^2\left(x^2-3\right)}{\left(x^2-1\right)^2}$$ והנקודות הקריטיות של הפונקציה הן $x=0,\ x=\pm\sqrt{3}$.
טבלת סימן של $f'$: חיובית כאשר $x<-\sqrt{3}$, שלילית כאשר $-\sqrt{3}<x<0$ וגם כאשר $0<x<\sqrt{3}$, וחיובית כאשר $x>\sqrt{3}$ (בתחום ההגדרה).
**סיכום:** $f(x)$ עולה כאשר $x<-\sqrt{3}$ וגם $x>\sqrt{3}$, ו-$f(x)$ יורדת כאשר $-\sqrt{3}<x<\sqrt{3}$. הנקודה $x=-\sqrt{3}$ היא נקודת מקסימום מקומי כך ש-$f(-\sqrt{3})=-\frac{3\sqrt{3}}{2}$, והנקודה $x=\sqrt{3}$ היא נקודת מינימום מקומי כך ש-$f(\sqrt{3})=\frac{3\sqrt{3}}{2}$.
**ד.** $$f''(x)=\frac{\left(4x^3-6x\right)\left(x^2-1\right)^2-2\left(x^4-3x^2\right)\left(x^2-1\right)2x}{\left(x^2-1\right)^4}=\frac{\left(4x^3-6x\right)\left(x^2-1\right)-2\left(x^4-3x^2\right)2x}{\left(x^2-1\right)^3}=\frac{2x^3+6x}{\left(x^2-1\right)^3}$$
טבלת סימן של $f''$: שלילית כאשר $x<-1$, חיובית כאשר $-1<x<0$, שלילית כאשר $0<x<1$, וחיובית כאשר $x>1$.
**סיכום:** $f(x)$ קמורה (∩) כאשר $x<-1$ וגם $0<x<1$. $f(x)$ קעורה (∪) כאשר $x>1$ וגם $-1<x<0$. הנקודה $x=0$ היא נקודת פיתול.
**ה.** הישרים $x=\pm1$ מהווים אסימפטוטות אנכיות לגרף הפונקציה, כך ש-$\lim_{x\to-1^-}f(x)=-\infty$ ו-$\lim_{x\to-1^+}f(x)=\infty$, וכן $\lim_{x\to1^-}f(x)=-\infty$ ו-$\lim_{x\to1^+}f(x)=\infty$.
בנוסף לזאת,
$$k=\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim_{x\to\pm\infty}\frac{x^2}{x^2-1}=1,\qquad m=\lim_{x\to\pm\infty}\left(f(x)-x\right)=0$$
והתוצאה מכך היא ש-$y=x$ היא אסימפטוטה משופעת לגרף הפונקציה ב-$\pm\infty$.
**ו. שרטוט:**
![גרף הפונקציה עם האסימפטוטות x=1, x=-1 ו-y=x](images/exams/22A-B-Q1-graph.png)
"""

SOL2A = r"""
השערה: $a_1=5,\ a_2=3,\ a_3=2.3\ldots$ הסדרה יורדת וחסומה מלרע. אם זה נכון, אז הסדרה מתכנסת וגבולה מקיים את המשוואה (על פניו הסדרה חיובית):
$$L=\frac{1}{2}\left(L+\frac{5}{L}\right),\qquad L=\sqrt{5},\ L^2=5$$
במקרה זה $L=\sqrt{5}$ הוא החסם התחתון של הסדרה.
נוכיח באינדוקציה שהסדרה באמת חסומה מלרע על ידי $\sqrt{5}$.
בסיס האינדוקציה: $a_1=5>\sqrt{5}$.
שלב האינדוקציה: נניח ש-$a_n>\sqrt{5}$, בפרט $a_n$ חיובי וניתן להשתמש באי-שוויון הממוצעים:
$$a_{n+1}=\frac{1}{2}\left(a_n+\frac{5}{a_n}\right)\ge\sqrt{a_n\cdot\frac{5}{a_n}}=\sqrt{5}$$
נותר להראות שהסדרה מונוטונית יורדת. נקבל:
$$\frac{a_{n+1}}{a_n}=\frac{1}{2}\left(1+\frac{5}{a_n^2}\right)<\frac{1}{2}\left(1+\frac{5}{5}\right)=1$$
כלומר הסדרה יורדת. לפי חישוב העזר שעשינו מקודם, $L=\sqrt{5}$.
"""

SOL2B = r"""
$$\int x\arctan\frac{2}{x}\,dx=\left\{u=\arctan\frac{2}{x},\ du=\frac{-\frac{2}{x^2}}{1+\frac{4}{x^2}}dx,\ dv=x\,dx,\ v=\frac{x^2}{2}\right\}=$$
$$=\frac{x^2}{2}\arctan\frac{2}{x}+\int\frac{\frac{2}{x^2}\cdot\frac{x^2}{2}}{1+\frac{4}{x^2}}dx=\frac{x^2}{2}\arctan\frac{2}{x}+\int\frac{x^2+4-4}{x^2+4}dx=$$
$$=\frac{x^2}{2}\arctan\frac{2}{x}+x-2\arctan\frac{x}{2}+c$$
"""

SOL3A = r"""
נגדיר את הפונקציה החדשה $f(x)=\ln(x+1)-\frac{3x+2}{x+2}$. הפונקציה רציפה וגזירה לכל $x>-1$, כפונקציה אלמנטרית ומוגדרת בתחום.
$$f(0)=-1<0,\qquad \lim_{x\to+\infty}f(x)=+\infty>0$$
לפי משפט ערך הביניים של קושי קיימת נקודה $c\in(0,+\infty)$ כך ש-$f(c)=0$.
נבדוק את הסימן של נגזרת:
$$f'(x)=\frac{1}{x+1}-\frac{4}{(x+2)^2}=\frac{(x+2)^2-4x-4}{(x+1)(x+2)^2}=\frac{x^2}{(x+1)(x+2)^2}>0$$
הפונקציה מונוטונית עולה, לכן הפתרון הוא יחיד.
"""

SOL3B = r"""
$$\int\frac{\cos x\,dx}{\left(3-\cos^2x\right)(3-\sin x)}=\int\frac{\cos x\,dx}{\left(2+\sin^2x\right)(3-\sin x)}\ \left\{\begin{array}{l}t=\sin x\\ dt=\cos x\,dx\end{array}\right\}=\int\frac{dt}{\left(2+t^2\right)(3-t)}$$
נחפש את הפירוק מן הצורה:
$$\frac{1}{\left(2+t^2\right)(3-t)}=\frac{At+B}{t^2+2}+\frac{C}{3-t}$$
נמצא את המקדמים של השברים: $1=(At+B)(3-t)+C\left(t^2+2\right)$.
$$t=3:\ 1=11C\Rightarrow C=\frac{1}{11}$$
$$t^2:\ 0=-A+C\Rightarrow A=C=\frac{1}{11}$$
$$t:\ 0=3A-B\Rightarrow B=3A=\frac{3}{11}$$
$$\int\frac{dt}{\left(2+t^2\right)(3-t)}=\frac{1}{11}\int\frac{t+3}{t^2+2}dt+\frac{1}{11}\int\frac{dt}{3-t}=\frac{1}{22}\int\frac{2t\,dt}{t^2+2}+\frac{3}{11}\int\frac{dt}{t^2+2}+\frac{1}{11}\int\frac{dt}{3-t}=$$
$$=\frac{1}{22}\ln\left(t^2+2\right)+\frac{3}{11\sqrt{2}}\arctan\frac{t}{\sqrt{2}}-\frac{1}{11}\ln|3-t|+C=$$
$$=\frac{1}{22}\ln\left(\sin^2x+2\right)+\frac{3}{11\sqrt{2}}\arctan\frac{\sin x}{\sqrt{2}}-\frac{1}{11}\ln|3-\sin x|+C$$
"""

SOL4A = r"""
תחום ההגדרה: $x\neq0,1$. נקודות האי-רציפות הן $0,1$.
$x=0$:
$$\lim_{x\to0^-}y=\lim_{x\to0^-}\frac{e^{\frac{x}{1-x}}}{1-e^{\frac{x}{1-x}}}=\frac{e^{\frac{0}{1-0}}}{1-e^{\frac{0}{1-0}}}=\frac{1}{0(+)}=\infty$$
$$\lim_{x\to0^+}y=\lim_{x\to0^+}\frac{e^{\frac{x}{1-x}}}{1-e^{\frac{x}{1-x}}}=\frac{e^{\frac{0}{1-0}}}{1-e^{\frac{0}{1-0}}}=\frac{1}{0(-)}=-\infty$$
$0$ היא אי-רציפות מהסוג השני.
$x=1$:
$$\lim_{x\to1^-}y=\lim_{x\to1^-}\frac{e^{\frac{x}{1-x}}}{1-e^{\frac{x}{1-x}}}=\frac{e^{\frac{1}{0(+)}}}{1-e^{\frac{1}{0(+)}}}=\frac{e^{\infty}}{1-e^{\infty}}=\frac{\infty}{-\infty}=\left[t=e^{\frac{x}{1-x}}\to\infty\right]=\lim_{t\to\infty}\frac{t}{1-t}=-1$$
$$\lim_{x\to1^+}y=\lim_{x\to1^+}\frac{e^{\frac{x}{1-x}}}{1-e^{\frac{x}{1-x}}}=\frac{e^{\frac{1}{0(-)}}}{1-e^{\frac{1}{0(-)}}}=\frac{e^{-\infty}}{1-e^{-\infty}}=\frac{0}{1-0}=0$$
$\lim_{x\to1^-}y\neq\lim_{x\to1^+}y$, לכן $1$ היא אי-רציפות מהסוג הראשון.
"""

SOL4B = r"""
![התחום הכלוא בין הגרף לציר ה-x](images/exams/22A-B-Q4b-sketch.png)
נשתמש בשיטת הקליפה:
$$V=2\pi\int_{\frac{\pi}{2}}^{\pi}x\cos^2x\,dx=\pi\int_{\frac{\pi}{2}}^{\pi}x\left(\cos(2x)+1\right)dx=\pi\left(\int_{\frac{\pi}{2}}^{\pi}x\cos(2x)\,dx+\int_{\frac{\pi}{2}}^{\pi}x\,dx\right)=$$
$$=\left|\begin{array}{ll}u=x & du=dx\\ dv=\cos(2x)\,dx & v=\frac{1}{2}\sin(2x)\end{array}\right|=$$
$$=\pi\left(\frac{1}{2}x\sin(2x)\Big|_{\frac{\pi}{2}}^{\pi}-\frac{1}{2}\int_{\frac{\pi}{2}}^{\pi}\sin(2x)\,dx+\frac{x^2}{2}\Big|_{\frac{\pi}{2}}^{\pi}\right)$$
$$=\pi\left(\frac{1}{2}\pi\sin(2\pi)-\frac{1}{2}\cdot\frac{\pi}{2}\sin(\pi)+\frac{1}{4}\cos(2x)\Big|_{\frac{\pi}{2}}^{\pi}+\frac{1}{2}\left(\pi^2-\frac{\pi^2}{4}\right)\right)$$
$$=\pi\left(\frac{1}{4}\left(\cos(2\pi)-\cos(\pi)\right)+\frac{3}{8}\pi^2\right)=\pi\left(\frac{1}{2}+\frac{3}{8}\pi^2\right)=\frac{\pi}{2}\left(1+\frac{3}{4}\pi^2\right)$$
"""

SOL5A = r"""
ניקח $x>0$. לפי משפט לגרנז', קיימת $c\in(0,x)$ כך שלפונקציה $f(x)=\ln(1+x)$ מקבלים:
$$\frac{f(x)-f(0)}{x-0}=\frac{\ln(1+x)}{x}=f'(c)=\frac{1}{1+c}$$
מכיוון ש-$0<c<x$, נובע מכך ש-
$$1<1+c<1+x\ \Longrightarrow\ \frac{1}{1+x}<\frac{1}{1+c}<1$$
זה אומר ש-
$$\frac{1}{1+x}<\frac{\ln(1+x)}{x}=\frac{1}{1+c}<1$$
ומכיוון ש-$x>0$ נקבל ש-
$$\frac{x}{1+x}<\ln(1+x)<x$$
"""

SOL5B = r"""
**הפתרון שבמקור (לא רשמי) עם תיקון:** הביטוי הסגור בפתרון נכון, אבל בהצבה המספרית בסוף עוגל $\sqrt{1+e^2}$ ל-$2.9$ והתקבל $1.98$. הערך הנכון של האינטגרל הוא $L\approx2.0035\approx2.00$. השורה המספרית האחרונה מתוקנת. התיקון נבדק (sympy).
$$L=\int_0^1\sqrt{1+\left(\left(e^x\right)'\right)^2}\cdot dx=\int_0^1\sqrt{1+e^{2x}}\cdot dx=$$
$$=\left[t=\sqrt{1+e^{2x}},\ dt=\frac{2e^{2x}}{2\sqrt{1+e^{2x}}}dx=\frac{t^2-1}{t}dx,\ dx=\frac{t}{t^2-1}dt;\quad x=0\Rightarrow t=\sqrt{2},\ x=1\Rightarrow t=\sqrt{1+e^2}\right]=$$
$$=\int_{\sqrt{2}}^{\sqrt{1+e^2}}t\cdot\frac{t}{t^2-1}dt=\int_{\sqrt{2}}^{\sqrt{1+e^2}}\frac{t^2}{t^2-1}dt=\int_{\sqrt{2}}^{\sqrt{1+e^2}}\left(1+\frac{1}{t^2-1}\right)dt=$$
$$=\left(t+\frac{1}{2}\ln\left|\frac{t-1}{t+1}\right|\right)\Bigg|_{\sqrt{2}}^{\sqrt{1+e^2}}=\left(\sqrt{1+e^2}+\frac{1}{2}\ln\left|\frac{\sqrt{1+e^2}-1}{\sqrt{1+e^2}+1}\right|\right)-\left(\sqrt{2}+\frac{1}{2}\ln\left|\frac{\sqrt{2}-1}{\sqrt{2}+1}\right|\right)=$$
$$\approx\left(2.8964-0.3600\right)-\left(1.4142-0.8814\right)=2.5363-0.5328\approx2.00$$
"""

SOL6A = r"""
$$f'(x)=\sqrt[3]{3x-1}+x\cdot\frac{1}{3}(3x-1)^{-2/3}\cdot3=(3x-1)^{1/3}+\frac{x}{(3x-1)^{2/3}}=\frac{4x-1}{(3x-1)^{2/3}}$$
$$f'(x)=0\iff x=\frac{1}{4}\in\left(-1,\frac{2}{3}\right)$$
וגם $x=\frac{1}{3}\in\left[-1,\frac{2}{3}\right]$ (שם הנגזרת אינה קיימת).
$$f\left(\frac{1}{4}\right)=\frac{1}{4}\sqrt[3]{\frac{3}{4}-1}=-\left(\frac{1}{4}\right)^{4/3},\qquad f\left(\frac{1}{3}\right)=0$$
$$f(-1)=-\sqrt[3]{-3-1}=\sqrt[3]{4},\qquad f\left(\frac{2}{3}\right)=\frac{2}{3}$$
הערך הגדול ביותר הוא: $\sqrt[3]{4}$.
הערך הקטן ביותר הוא: $-\left(\frac{1}{4}\right)^{4/3}$.
"""

SOL6B = r"""
$$\lim_{x\to2^+}f(x)=\lim_{x\to2^+}\left(x^2+b\right)=4+b$$
$$\lim_{x\to2^-}f(x)=\lim_{x\to2^-}ax^3=8a$$
$$f(2)=8a=4+b$$
$$f_+'(2)=\lim_{\Delta x\to0^+}\frac{f(2+\Delta x)-f(2)}{\Delta x}=\lim_{\Delta x\to0^+}\frac{(2+\Delta x)^2+b-8a}{\Delta x}$$
$$\lim_{\Delta x\to0^+}\frac{(2+\Delta x)^2-4}{\Delta x}=\lim_{\Delta x\to0^+}\frac{4\Delta x+\Delta x^2}{\Delta x}=\lim_{\Delta x\to0^+}(4+\Delta x)=4$$
$$f_-'(2)=\lim_{\Delta x\to0^-}\frac{f(2+\Delta x)-f(2)}{\Delta x}=\lim_{\Delta x\to0^-}\frac{a(2+\Delta x)^3-8a}{\Delta x}=$$
$$\lim_{\Delta x\to0^-}\frac{12a\Delta x+6a\Delta x^2+a\Delta x^3}{\Delta x}=\lim_{\Delta x\to0^-}\left(12a+6a\Delta x+a\Delta x^2\right)=12a$$
נקבל $8a=4+b$ ו-$12a=4\Rightarrow a=\frac{1}{3}$, ולכן $b=-\frac{4}{3}$.
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=\frac{x^3}{x^2-1}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, "
      "תחומי עליה וירידה ונקודות קיצון, תחומי קמירות וקעירות ונקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1),

    Q(2, "proof", "sequences_limits",
      r"הוכיחו כי הסדרה הבאה מתכנסת ומצאו את גבולה: $a_1=5,\ a_{n+1}=\frac{1}{2}\left(a_n+\frac{5}{a_n}\right)$.",
      SOL2A, part="א"),
    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int x\arctan\frac{2}{x}\,dx$.",
      SOL2B, part="ב"),

    Q(3, "proof", "continuity",
      r"הוכיחו כי למשוואה $\ln(x+1)-\frac{3x+2}{x+2}=0$ יש פתרון יחיד.",
      SOL3A, part="א", points=10),
    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\cos x\,dx}{\left(3-\cos^2x\right)(3-\sin x)}$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "continuity",
      r"מצאו את הנקודות האי-רציפות של הפונקציה הבאה וסווגו אותן: $y=\frac{e^{\frac{x}{1-x}}}{1-e^{\frac{x}{1-x}}}$.",
      SOL4A, part="א", points=10),
    Q(4, "computation", "definite_integrals",
      r"חשבו את נפח הגוף, הנוצר על ידי סיבוב סביב ציר ה-$y$ של התחום הכלוא בין הקווים הבאים: "
      r"$y=\cos^2x,\ y=0$ כאשר $\frac{\pi}{2}\le x\le\pi$.",
      SOL4B, part="ב"),

    Q(5, "proof", "mean_value_theorems",
      r"הוכיחו את האי-שוויון $\frac{x}{x+1}<\ln(1+x)<x$, כאשר $x>0$.",
      SOL5A, part="א", points=10),
    Q(5, "computation", "definite_integrals",
      r"חשבו את אורך הקשת של העקומה $y=e^x$ בקטע $0\le x\le1$.",
      SOL5B, part="ב", solutionSource="solved", official=False),

    Q(6, "computation", "extrema_optimization",
      r"מצאו את הערך הגדול ביותר ואת הערך הקטן ביותר של הפונקציה $f(x)=x\cdot\sqrt[3]{3x-1}$ בקטע $-1\le x\le\frac{2}{3}$.",
      SOL6A, part="א", points=10),
    Q(6, "computation", "derivatives_tangents",
      r"נתונה הפונקציה $f(x)=\begin{cases}ax^3, & x\le2\\ x^2+b, & x>2\end{cases}$ כאשר $a$ ו-$b$ פרמטרים ממשיים. "
      r"מצאו את כל הערכים של $a$ ו-$b$ כך ש-$f(x)$ תהיה גזירה בנקודה $x=2$.",
      SOL6B, part="ב", points=10),
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


# ===== Q1: f = x^3/(x^2-1) =====
f1 = x**3/(x**2 - 1)
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
assert same(f1p, x**2*(x**2 - 3)/(x**2 - 1)**2) and same(f1pp, (2*x**3 + 6*x)/(x**2 - 1)**3)
assert sorted(s for s in sp.solve(sp.numer(sp.together(f1p)), x) if s.is_real) == sorted([-sp.sqrt(3), 0, sp.sqrt(3)])
assert same(f1.subs(x, sp.sqrt(3)), 3*sp.sqrt(3)/2) and same(f1.subs(x, -sp.sqrt(3)), -3*sp.sqrt(3)/2)
assert f1p.subs(x, 2) == R(4, 9) and f1pp.subs(x, 2) == R(28, 27)
assert f1p.subs(x, R(-1, 2)) < 0 and f1p.subs(x, R(1, 2)) < 0                      # f' does not change sign at 0
assert f1pp.subs(x, R(-1, 2)) > 0 and f1pp.subs(x, R(1, 2)) < 0                    # f'' does: inflection at 0
assert sp.limit(f1/x, x, sp.oo) == 1 and sp.limit(f1 - x, x, sp.oo) == 0 and sp.limit(f1 - x, x, -sp.oo) == 0
assert sp.limit(f1, x, 1, '+') == sp.oo and sp.limit(f1, x, 1, '-') == -sp.oo
f1p_bads = [x**2*(x**2 - 3)/(x**2 + 1)**2, x**2*(x**2 + 3)/(x**2 - 1)**2, x**2*(x**2 - 3)/(x**2 - 1)]

add(1,
    rubric=rub(("תחום הגדרה $x\\neq\\pm1$ ונקודת חיתוך $(0,0)$", 2),
               ("נגזרת $f'(x)=\\frac{x^2\\left(x^2-3\\right)}{\\left(x^2-1\\right)^2}$ וטבלת סימן", 5),
               ("סיווג הקיצון: מקסימום ב-$x=-\\sqrt3$ ומינימום ב-$x=\\sqrt3$ וערכיהם", 3),
               ("נגזרת שנייה $f''(x)=\\frac{2x^3+6x}{\\left(x^2-1\\right)^3}$, קמירות ונקודת פיתול ב-$x=0$", 4),
               ("אסימפטוטות: $x=\\pm1$ ו-$y=x$", 4),
               ("שרטוט הגרף בהתאם לנתונים", 2)),
    rubricSource="ai-verified",
    pitfalls=["לסווג את $x=0$ כנקודת קיצון רק כי $f'(0)=0$. ב-$x=0$ הנגזרת $f'$ אינה משנה סימן, ולכן אין שם קיצון. נקודת פיתול נקבעת לפי שינוי הסימן של $f''$, ו-$f''$ אכן משנה סימן ב-$x=0$.",
              "לשכוח שגם $x=1$ וגם $x=-1$ מחוץ לתחום ההגדרה ולכן הם נקודות אסימפטוטה אנכית ואי אפשר לחבר דרכן.",
              "לחשב את האסימפטוטה המשופעת רק ב-$+\\infty$ ולא לבדוק ב-$-\\infty$."],
    steps=[
        chx("מהי הנגזרת של $f(x)=\\frac{x^3}{x^2-1}$?", x**2*(x**2 - 3)/(x**2 - 1)**2, f1p_bads,
            lambda e: same(e, f1p),
            "כלל המנה: $\\frac{3x^2\\left(x^2-1\\right)-2x^4}{\\left(x^2-1\\right)^2}=\\frac{x^4-3x^2}{\\left(x^2-1\\right)^2}$ (נבדק ב-sympy)."),
        num("באיזה ערך חיובי של $x$ מתאפסת הנגזרת? (עשרוני)", sp.sqrt(3), "$x^2\\left(x^2-3\\right)=0$ נותן $x=\\sqrt3\\approx1.7321$ (וגם $x=0$, $x=-\\sqrt3$)."),
        num("מהו $f\\left(\\sqrt3\\right)$ בנקודת המינימום המקומי? (עשרוני)", 3*sp.sqrt(3)/2, "$f\\left(\\sqrt3\\right)=\\frac{3\\sqrt3}{2}\\approx2.598$ (sympy)."),
        ch("מהו סוג הנקודה $x=0$?", "נקודת פיתול, לא נקודת קיצון",
           ["מקסימום מקומי", "מינימום מקומי", "אסימפטוטה אנכית"],
           "$f'<0$ משני צדי $0$ (אין שינוי סימן, לכן אין קיצון), ו-$f''$ משנה סימן מחיובית לשלילית (נבדק ב-sympy)."),
        ch("מהן כל האסימפטוטות של $f$?", "$x=1$, $x=-1$ ו-$y=x$",
           ["$x=1$ ו-$x=-1$ בלבד", "$y=x$ בלבד", "$x=0$ ו-$y=x$"],
           "$x=\\pm1$ אנכיות (גבולות אינסופיים), ו-$y=x$ משופעת ב-$\\pm\\infty$ כי $\\frac{f}{x}\\to1$ ו-$f-x\\to0$ (sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: a_{n+1} = (a_n + 5/a_n)/2, a_1 = 5 =====
seq = mp.mpf(5)
for _ in range(80):
    assert seq >= mp.sqrt(5) - mp.mpf(10)**-40
    nxt = (seq + 5/seq)/2
    assert nxt <= seq
    seq = nxt
assert abs(seq - mp.sqrt(5)) < 1e-30
assert (5 + R(5, 5))/2 == 3 and R(1, 2)*(1 + R(5, 25)) == R(3, 5)
L2a = ["נוכיח באינדוקציה ש-$a_n\\ge\\sqrt5$: $a_1=5$, ומאי-שוויון הממוצעים $a_{n+1}=\\frac{1}{2}\\left(a_n+\\frac{5}{a_n}\\right)\\ge\\sqrt5$.",
       "$\\frac{a_{n+1}}{a_n}=\\frac{1}{2}\\left(1+\\frac{5}{a_n^2}\\right)\\le1$ כי $a_n^2\\ge5$, ולכן הסדרה יורדת.",
       "סדרה יורדת וחסומה מלמטה מתכנסת; מנוסחת הנסיגה $L=\\frac{1}{2}\\left(L+\\frac{5}{L}\\right)$, כלומר $L^2=5$ ו-$L=\\sqrt5$ (חיובי)."]
L2a_b = list(L2a)
L2a_b[1] = "$\\frac{a_{n+1}}{a_n}=\\frac{1}{2}\\left(1+\\frac{5}{a_n^2}\\right)\\ge1$ כי $a_n^2\\ge5$, ולכן הסדרה עולה."

add(2, "א",
    rubric=rub(("השערת הגבול מהמשוואה $L=\\frac{1}{2}\\left(L+\\frac{5}{L}\\right)$, כלומר $L=\\sqrt5$", 1),
               ("חסימה מלמטה על ידי $\\sqrt5$ באינדוקציה ובאי-שוויון הממוצעים", 3),
               ("מונוטוניות: $\\frac{a_{n+1}}{a_n}<1$ (או $\\le1$)", 3),
               ("מסקנה: התכנסות וגבול $\\sqrt5$", 3)),
    rubricSource="ai-verified",
    pitfalls=["להניח שהגבול קיים ולפתור את משוואת הגבול בלי להוכיח מונוטוניות וחסימה.",
              "לשכוח את $L=-\\sqrt5$ ולפסול אותו כי כל האיברים חיוביים.",
              "להוכיח מונוטוניות לפני החסימה: האי-שוויון $\\frac{a_{n+1}}{a_n}\\le1$ נשען על $a_n^2\\ge5$."],
    steps=[
        num("מהו $a_2$ כאשר $a_1=5$?", 3, "$a_2=\\frac{1}{2}\\left(5+\\frac{5}{5}\\right)=3$."),
        num("מהו היחס $\\frac{a_2}{a_1}=\\frac{1}{2}\\left(1+\\frac{5}{a_1^2}\\right)$? (עשרוני)", R(3, 5),
            "$\\frac{1}{2}\\left(1+\\frac{5}{25}\\right)=0.6<1$, כלומר הסדרה יורדת בשלב זה."),
        order("סדרו את שלבי ההוכחה.", L2a, "חסימה קודמת למונוטוניות (היא תלויה בה), והמעבר לגבול דורש את שתיהן."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L2a_b, 1,
                "מ-$a_n^2\\ge5$ נובע $\\frac{5}{a_n^2}\\le1$ ולכן היחס $\\le1$ והסדרה יורדת, לא עולה (למשל $0.6$ עבור $a_1=5$)."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: int x arctan(2/x) dx =====
g2b = x*sp.atan(2/x)
F2b = x**2/2*sp.atan(2/x) + x - 2*sp.atan(x/2)
pts2 = [R(1, 2), 1, 3]
F2b_bads = [x**2/2*sp.atan(2/x) + x + 2*sp.atan(x/2), x**2/2*sp.atan(2/x) - x + 2*sp.atan(x/2),
            x**2/2*sp.atan(2/x) + x - sp.atan(x/2)]
assert dnum(F2b, g2b, pts2) and not any(dnum(e, g2b, pts2) for e in F2b_bads)
assert same(sp.diff(sp.atan(2/x), x), -2/(x**2 + 4)) and sp.diff(sp.atan(2/x), x).subs(x, 2) == -R(1, 4)

add(2, "ב",
    rubric=rub(("בחירה באינטגרציה בחלקים: $u=\\arctan\\frac{2}{x}$, $dv=x\\,dx$", 2),
               ("חישוב $du=-\\frac{2}{x^2+4}dx$", 2),
               ("פישוט האינטגרל הנותר ל-$\\int\\frac{x^2}{x^2+4}dx=\\int\\left(1-\\frac{4}{x^2+4}\\right)dx$", 3),
               ("התוצאה $\\frac{x^2}{2}\\arctan\\frac{2}{x}+x-2\\arctan\\frac{x}{2}+c$", 3)),
    rubricSource="ai-verified",
    pitfalls=["טעות בנגזרת של $\\arctan\\frac{2}{x}$: כלל השרשרת נותן $-\\frac{2}{x^2+4}$.",
              "לשכוח את הסימן ההפוך: $-\\int u'v$ עם $u'<0$ נותן סימן פלוס.",
              "לשכוח שהאינטגרל $\\int\\frac{4}{x^2+4}dx$ שווה $2\\arctan\\frac{x}{2}$ ולא $4\\arctan\\frac{x}{2}$."],
    steps=[
        ch("איזו בחירה באינטגרציה בחלקים משתמש הפתרון?", "$u=\\arctan\\frac{2}{x},\\ dv=x\\,dx$",
           ["$u=x,\\ dv=\\arctan\\frac{2}{x}\\,dx$", "$u=\\frac{2}{x},\\ dv=x\\,dx$", "$u=x\\arctan\\frac{2}{x}$ בלי $dv$"],
           "גוזרים את $\\arctan$ (נעלם בצורה רציונלית) ומאנטגרלים את $x$."),
        num("מהי הנגזרת של $\\arctan\\frac{2}{x}$ בנקודה $x=2$? (עשרוני)", -R(1, 4),
            "$\\frac{d}{dx}\\arctan\\frac{2}{x}=-\\frac{2}{x^2+4}$ ולכן $-\\frac{2}{8}=-0.25$ (sympy)."),
        num("מהו המקדם $c$ ב-$\\int\\frac{4}{x^2+4}dx=c\\arctan\\frac{x}{2}$?", 2, "$\\int\\frac{dx}{x^2+4}=\\frac{1}{2}\\arctan\\frac{x}{2}$ ולכן $c=4\\cdot\\frac12=2$."),
        chx("איזו קדומה נכונה? (בתחום $x>0$)", F2b, F2b_bads, lambda e: dnum(e, g2b, pts2),
            "$\\frac{x^2}{2}\\arctan\\frac{2}{x}+x-2\\arctan\\frac{x}{2}$; הנגזרת של כל אחת מהאחרות שונה מהאינטגרנד (נבדק מספרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: unique root of ln(x+1) - (3x+2)/(x+2) =====
g3 = sp.log(x + 1) - (3*x + 2)/(x + 2)
g3p = sp.diff(g3, x)
assert same(g3p, x**2/((x + 1)*(x + 2)**2)) and g3.subs(x, 0) == -1 and g3p.subs(x, 1) == R(1, 18)
v100 = sp.N(g3.subs(x, 100))
assert v100 > 0 and sp.limit(g3, x, sp.oo) == sp.oo
assert min(sp.N(g3p.subs(x, R(k, 4))) for k in range(-3, 400) if k != 0) > 0

add(3, "א",
    rubric=rub(("הגדרת $f(x)=\\ln(x+1)-\\frac{3x+2}{x+2}$ ורציפותה ב-$x>-1$", 1),
               ("קיום: $f(0)=-1<0$ וגם $f\\to+\\infty$, ולפי משפט ערך הביניים יש שורש", 4),
               ("נגזרת $f'(x)=\\frac{x^2}{(x+1)(x+2)^2}$", 3),
               ("$f'>0$ ולכן $f$ עולה ממש והשורש יחיד", 2)),
    rubricSource="ai-verified",
    pitfalls=["להסתפק במשפט ערך הביניים: הוא נותן קיום בלבד ולא יחידות.",
              "לשכוח שהנגזרת מתאפסת ב-$x=0$ אך עדיין חיובית משני צדדיה, ולכן $f$ עולה ממש.",
              "טעות בכלל המנה בנגזרת של $\\frac{3x+2}{x+2}$, שהיא $\\frac{4}{(x+2)^2}$."],
    steps=[
        num("מהו $f(0)$ עבור $f(x)=\\ln(x+1)-\\frac{3x+2}{x+2}$?", -1, "$f(0)=\\ln1-\\frac{2}{2}=-1<0$."),
        num("מהו $f(100)$? (עשרוני)", g3.subs(x, 100), "$\\ln101-\\frac{302}{102}\\approx1.65>0$, ולכן יש שורש בין $0$ ל-$100$ (ערך הביניים)."),
        chx("מהי הנגזרת $f'(x)$?", x**2/((x + 1)*(x + 2)**2),
            [x/((x + 1)*(x + 2)**2), x**2/((x + 1)*(x + 2)), (x**2 + 4)/((x + 1)*(x + 2)**2)], lambda e: same(e, g3p),
            "$\\frac{1}{x+1}-\\frac{4}{(x+2)^2}=\\frac{(x+2)^2-4(x+1)}{(x+1)(x+2)^2}=\\frac{x^2}{(x+1)(x+2)^2}$ (sympy)."),
        num("מהו $f'(1)$? (עשרוני)", R(1, 18), "$\\frac{1}{2\\cdot9}=\\frac{1}{18}\\approx0.0556>0$."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: int cos x / ((3-cos^2 x)(3 - sin x)) =====
g3b = sp.cos(x)/((3 - sp.cos(x)**2)*(3 - sp.sin(x)))
F3b = sp.log(sp.sin(x)**2 + 2)/22 + 3/(11*sp.sqrt(2))*sp.atan(sp.sin(x)/sp.sqrt(2)) - sp.log(3 - sp.sin(x))/11
F3b_bads = [sp.log(sp.sin(x)**2 + 2)/22 + 3/(11*sp.sqrt(2))*sp.atan(sp.sin(x)/sp.sqrt(2)) + sp.log(3 - sp.sin(x))/11,
            sp.log(sp.sin(x)**2 + 2)/11 + 3/(11*sp.sqrt(2))*sp.atan(sp.sin(x)/sp.sqrt(2)) - sp.log(3 - sp.sin(x))/11,
            sp.log(sp.sin(x)**2 + 2)/22 + 3/11*sp.atan(sp.sin(x)/sp.sqrt(2)) - sp.log(3 - sp.sin(x))/11]
pts3 = [R(1, 3), 1, 2]
assert dnum(F3b, g3b, pts3) and not any(dnum(e, g3b, pts3) for e in F3b_bads)
At, Bt, Ct = sp.symbols('At Bt Ct')
sol3 = sp.solve(sp.Poly(sp.expand((At*t + Bt)*(3 - t) + Ct*(t**2 + 2) - 1), t).all_coeffs(), [At, Bt, Ct], dict=True)[0]
assert sol3 == {At: R(1, 11), Bt: R(3, 11), Ct: R(1, 11)}

add(3, "ב",
    rubric=rub(("הצבה $t=\\sin x$, $dt=\\cos x\\,dx$ ושימוש ב-$3-\\cos^2x=2+\\sin^2x$", 2),
               ("צורת הפירוק $\\frac{At+B}{t^2+2}+\\frac{C}{3-t}$", 2),
               ("מקדמים $A=C=\\frac{1}{11}$, $B=\\frac{3}{11}$", 3),
               ("אינטגרציה (לוגריתמים ו-$\\arctan$) והחזרה ל-$x$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח ש-$3-\\cos^2x=2+\\sin^2x$ ולהישאר עם שני משתנים.",
              "לבחור פירוק עם מונה קבוע מעל $t^2+2$ במקום מונה לינארי.",
              "לחשב $\\int\\frac{dt}{t^2+2}=\\frac{1}{\\sqrt2}\\arctan\\frac{t}{\\sqrt2}$ בלי הגורם $\\frac{1}{\\sqrt2}$."],
    steps=[
        ch("איזו הצבה משתמש הפתרון?", "$t=\\sin x$", ["$t=\\cos x$", "$t=\\tan\\frac{x}{2}$", "$t=3-\\cos^2x$"],
           "$\\cos x\\,dx=dt$, ו-$3-\\cos^2x=2+\\sin^2x=2+t^2$; כך מתקבל שבר רציונלי ב-$t$."),
        num("מהו המקדם $C$ בפירוק $\\frac{1}{(2+t^2)(3-t)}=\\frac{At+B}{t^2+2}+\\frac{C}{3-t}$? (עשרוני)", sol3[Ct],
            "הצבת $t=3$ ב-$1=(At+B)(3-t)+C\\left(t^2+2\\right)$ נותנת $1=11C$, כלומר $C=\\frac{1}{11}\\approx0.0909$."),
        num("מהו המקדם $B$? (עשרוני)", sol3[Bt], "השוואת מקדם $t$: $0=3A-B$ עם $A=\\frac{1}{11}$ נותנת $B=\\frac{3}{11}\\approx0.2727$."),
        ch("איזו קדומה נכונה?", T(F3b), [T(e) for e in F3b_bads],
           "$\\frac{1}{22}\\ln\\left(\\sin^2x+2\\right)+\\frac{3}{11\\sqrt2}\\arctan\\frac{\\sin x}{\\sqrt2}-\\frac{1}{11}\\ln(3-\\sin x)$; הנגזרת של כל אחת מהאחרות שונה (נבדק מספרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: discontinuities of e^(x/(1-x))/(1-e^(x/(1-x))) =====
def y4(v):
    v = mp.mpf(v)
    E = mp.exp(v/(1 - v))
    return E/(1 - E)

e_ = mp.mpf('1e-9')
assert y4(-e_) > 1e8 and y4(e_) < -1e8                                   # second kind at 0
assert abs(y4(1 - mp.mpf('1e-3')) + 1) < 1e-6 and abs(y4(1 + mp.mpf('1e-3'))) < 1e-6   # -1 and 0 at x=1 (one-sided)

add(4, "א",
    rubric=rub(("תחום הגדרה $x\\neq0,1$ וקביעת נקודות האי-רציפות", 2),
               ("$x=0$: גבולות חד-צדדיים $+\\infty$ ו-$-\\infty$, ולכן ממין שני", 3),
               ("$x=1$: הגבול השמאלי $-1$", 2),
               ("$x=1$: הגבול הימני $0$, גבולות סופיים ושונים ולכן ממין ראשון", 3)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח ש-$x=1$ אינה בתחום (המעריך $\\frac{x}{1-x}$ לא מוגדר) ולבדוק רק את $x=0$.",
              "בבדיקת $x\\to1^-$ לשכוח ש-$\\frac{x}{1-x}\\to+\\infty$, ולבדוק במקום זאת גבול של $e^{-\\infty}$.",
              "לסווג את $x=1$ כמין שני רק כי המעריך שואף ל-$\\pm\\infty$."],
    steps=[
        num("מהו $\\lim_{x\\to1^-}y$? (כאשר $t=e^{x/(1-x)}\\to\\infty$ מקבלים $\\frac{t}{1-t}$)", -1, "$\\lim_{t\\to\\infty}\\frac{t}{1-t}=-1$ (נבדק מספרית)."),
        num("מהו $\\lim_{x\\to1^+}y$? (כאן $t=e^{x/(1-x)}\\to0$)", 0, "$\\frac{t}{1-t}\\to\\frac{0}{1}=0$ (נבדק מספרית)."),
        ch("מהו סוג אי-הרציפות ב-$x=0$?", "ממין שני (הגבולות החד-צדדיים אינסופיים)",
           ["ממין ראשון", "סליקה", "אין שם אי-רציפות"],
           "המכנה $1-e^{x/(1-x)}\\to0$ והמונה $\\to1$, והגבול הוא $+\\infty$ משמאל ו-$-\\infty$ מימין (נבדק מספרית)."),
        ch("מהו סוג אי-הרציפות ב-$x=1$?", "ממין ראשון (גבולות חד-צדדיים סופיים ושונים: $-1$ ו-$0$)",
           ["ממין שני", "סליקה (גבולות חד-צדדיים שווים)", "אין שם אי-רציפות"],
           "הגבולות $-1$ ו-$0$ סופיים ושונים."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: shells, y = cos^2 x on [pi/2, pi] =====
V4 = 2*mp.pi*mp.quad(lambda v: v*mp.cos(v)**2, [mp.pi/2, mp.pi])
assert abs(V4 - mp.pi*(mp.mpf(1)/2 + 3*mp.pi**2/8)) < 1e-25
assert abs(mp.quad(lambda v: v*mp.cos(2*v), [mp.pi/2, mp.pi]) - mp.mpf(1)/2) < 1e-25
assert abs(mp.quad(lambda v: v, [mp.pi/2, mp.pi]) - 3*mp.pi**2/8) < 1e-25
assert same(sp.cos(x)**2, (1 + sp.cos(2*x))/2)

add(4, "ב",
    rubric=rub(("שיטת הקליפות: $V=2\\pi\\int_{\\pi/2}^{\\pi}x\\cos^2x\\,dx$", 3),
               ("זהות $\\cos^2x=\\frac{1+\\cos2x}{2}$", 2),
               ("אינטגרציה בחלקים: $\\int_{\\pi/2}^{\\pi}x\\cos2x\\,dx=\\frac12$", 3),
               ("סכום $\\pi\\left(\\frac12+\\frac{3\\pi^2}{8}\\right)$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להשתמש בשיטת הטבעות סביב ציר $y$ במקום קליפות ולסבך את החישוב.",
              "לשכוח את $2\\pi$ או את הגורם $x$ (רדיוס הקליפה) באינטגרנד.",
              "טעות בגבולות האינטגרציה: התחום הוא $\\frac{\\pi}{2}\\le x\\le\\pi$."],
    steps=[
        ch("באיזו שיטה משתמש הפתרון לחישוב הנפח?", "שיטת הקליפות הגליליות",
           ["שיטת הטבעות (חתכים) סביב ציר $y$", "משפט פפוס בלבד, בלי אינטגרל"],
           "סיבוב סביב ציר $y$ של תחום מתחת לגרף של $y(x)$: $V=2\\pi\\int x\\cos^2x\\,dx$."),
        num("מהו $\\int_{\\pi/2}^{\\pi}x\\,dx$? (עשרוני)", 3*mp.pi**2/8, "$\\frac{\\pi^2-\\frac{\\pi^2}{4}}{2}=\\frac{3\\pi^2}{8}\\approx3.7011$."),
        num("מהו $\\int_{\\pi/2}^{\\pi}x\\cos2x\\,dx$? (עשרוני)", R(1, 2),
            "אינטגרציה בחלקים נותנת $\\frac{x\\sin2x}{2}\\Big|+\\frac{\\cos2x}{4}\\Big|=0+\\frac{1-(-1)}{4}=\\frac12$ (נבדק נומרית)."),
        num("מהו הנפח $V=\\pi\\left(\\frac12+\\frac{3\\pi^2}{8}\\right)$? (עשרוני)", mp.pi*(mp.mpf(1)/2 + 3*mp.pi**2/8),
            "$V\\approx13.20$ (נבדק באינטגרציה נומרית של הקליפות).", tol=0.01),
    ],
    stepsSource="ai-verified")

# ===== Q5a: x/(x+1) < ln(1+x) < x =====
for cv in (R(1, 2), R(3, 4)):
    assert 1/(1 + 1) < 1/(1 + cv) < 1 and not (1 < 1/(1 + cv))
L5a = ["לפי משפט לגרנז' על $f(t)=\\ln(1+t)$ בקטע $[0,x]$ קיימת $c\\in(0,x)$ כך ש-$\\frac{\\ln(1+x)}{x}=\\frac{1}{1+c}$.",
       "מכיוון ש-$0<c<x$ מתקיים $1<1+c<1+x$.",
       "לכן $\\frac{1}{1+x}<\\frac{1}{1+c}<1$.",
       "נכפול ב-$x>0$ ונקבל $\\frac{x}{1+x}<\\ln(1+x)<x$."]
L5a_b = list(L5a)
L5a_b[2] = "לכן $1<\\frac{1}{1+c}<\\frac{1}{1+x}$."

add(5, "א",
    rubric=rub(("הפעלת משפט לגרנז' על $\\ln(1+t)$ בקטע $[0,x]$", 3),
               ("קבלת $\\frac{\\ln(1+x)}{x}=\\frac{1}{1+c}$", 2),
               ("חסימת $1+c$ והיפוך: $\\frac{1}{1+x}<\\frac{1}{1+c}<1$", 3),
               ("כפל ב-$x>0$ והמסקנה", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח להפוך את כיוון האי-שוויון במעבר להופכי.",
              "להפעיל את המשפט על $\\ln x$ במקום על $\\ln(1+t)$ ולקבל גבולות שגויים.",
              "לכפול ב-$x$ בלי לציין $x>0$."],
    steps=[
        ch("לאיזו פונקציה ולאיזה קטע מפעיל הפתרון את משפט לגרנז'?",
           "$f(t)=\\ln(1+t)$ בקטע $[0,x]$",
           ["$f(t)=\\ln t$ בקטע $[1,x]$", "$f(t)=\\ln(1+t)$ בקטע $[0,1]$", "$f(t)=\\frac{t}{1+t}$ בקטע $[0,x]$"],
           "הפתרון מציב $f(x)-f(0)=f'(c)\\,x$ עם $f(t)=\\ln(1+t)$ והקטע $[0,x]$."),
        num("מהו $f'(1)$ עבור $f(t)=\\ln(1+t)$? (עשרוני)", R(1, 2), "$f'(t)=\\frac{1}{1+t}$ ולכן $f'(1)=0.5$."),
        order("סדרו את שלבי ההוכחה.", L5a, "כל שלב נשען על קודמו: לגרנז', חסימת $c$, הופכי, כפל ב-$x$."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L5a_b, 2,
                "ההופכי של $1<1+c<1+x$ הוא $\\frac{1}{1+x}<\\frac{1}{1+c}<1$, לא $1<\\frac{1}{1+c}$ (למשל $c=0.5$ נותן $0.67<1$)."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: arc length of e^x on [0,1] =====
L5 = mp.quad(lambda v: mp.sqrt(1 + mp.exp(2*v)), [0, 1])
t1 = mp.sqrt(1 + mp.e**2)
Fclosed = lambda tv: tv + mp.log(abs((tv - 1)/(tv + 1)))/2
assert abs(L5 - (Fclosed(t1) - Fclosed(mp.sqrt(2)))) < 1e-25
assert abs(L5 - mp.mpf('2.0035')) < 1e-3
vv = mp.mpf('0.7'); tv_ = mp.sqrt(1 + mp.exp(2*vv))
assert abs(mp.diff(lambda s: mp.sqrt(1 + mp.exp(2*s)), vv) - (tv_**2 - 1)/tv_) < 1e-20   # dt/dx = (t^2-1)/t
assert abs(mp.quad(lambda tv: tv**2/(tv**2 - 1), [mp.sqrt(2), t1]) - L5) < 1e-25

add(5, "ב",
    rubric=rub(("נוסחת אורך קשת והנגזרת $y'=e^x$: $L=\\int_0^1\\sqrt{1+e^{2x}}\\,dx$", 2),
               ("הצבה $t=\\sqrt{1+e^{2x}}$, $dx=\\frac{t}{t^2-1}dt$ וגבולות $\\sqrt2$, $\\sqrt{1+e^2}$", 3),
               ("פירוק $\\frac{t^2}{t^2-1}=1+\\frac{1}{t^2-1}$ ואינטגרציה", 3),
               ("הצבת הגבולות והערך המספרי $\\approx2.0035$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את הריבוע בנגזרת: $1+(y')^2=1+e^{2x}$.",
              "לא להמיר את גבולות האינטגרציה בעת ההצבה.",
              "טעות בחישוב הערך המספרי הסופי. הערך הנכון הוא $2.0035$ ולא $1.98$."],
    steps=[
        ch("מהו האינטגרנד אחרי ההצבה $t=\\sqrt{1+e^{2x}}$ (עם $dx=\\frac{t}{t^2-1}dt$)?", "$\\frac{t^2}{t^2-1}$",
           ["$\\frac{t}{t^2-1}$", "$\\frac{t^2}{t^2+1}$", "$\\frac{1}{t^2-1}$"],
           "$\\sqrt{1+e^{2x}}\\,dx=t\\cdot\\frac{t}{t^2-1}dt$ (נבדק מספרית)."),
        num("מהו הגבול העליון החדש $t=\\sqrt{1+e^{2}}$? (עשרוני)", t1, "$\\sqrt{1+e^2}\\approx2.8964$."),
        num("מהו $\\int_{\\sqrt2}^{\\sqrt{1+e^2}}\\frac{dt}{t^2-1}$? (עשרוני)", L5 - (t1 - mp.sqrt(2)),
            "הערך הוא $L-\\left(t_1-\\sqrt2\\right)\\approx0.5213$ (נבדק נומרית).", tol=0.005),
        num("מהו אורך הקשת? (עשרוני)", L5, "$L\\approx2.0035$ (נבדק באינטגרציה נומרית ובביטוי הסגור).", tol=0.01),
    ],
    stepsSource="ai-verified")

# ===== Q6a: abs extrema of x * cbrt(3x-1) on [-1, 2/3] =====
def f6(v):
    v = mp.mpf(v)
    w = 3*v - 1
    return v*mp.sign(w)*abs(w)**(mp.mpf(1)/3)

grid6 = [f6(mp.mpf(-1) + mp.mpf(k)/6000*(mp.mpf(5)/3)) for k in range(0, 6001)]
assert abs(max(grid6) - mp.cbrt(4)) < 1e-9 and abs(min(grid6) + (mp.mpf(1)/4)**(mp.mpf(4)/3)) < 1e-6
assert abs(f6(mp.mpf(1)/4) + (mp.mpf(1)/4)**(mp.mpf(4)/3)) < 1e-25 and abs(f6(mp.mpf(1)/3)) < 1e-25 and abs(f6(-1) - mp.cbrt(4)) < 1e-25
assert abs(f6(mp.mpf(2)/3) - mp.mpf(2)/3) < 1e-25
fp6 = lambda v: (4*v - 1)/(mp.sign(3*v - 1)*abs(3*v - 1)**(mp.mpf(1)/3))**2
assert abs(mp.diff(f6, mp.mpf('0.6')) - fp6(mp.mpf('0.6'))) < 1e-15 and abs(fp6(mp.mpf(1)/4)) < 1e-30

add(6, "א",
    rubric=rub(("נגזרת $f'(x)=\\frac{4x-1}{(3x-1)^{2/3}}$", 3),
               ("נקודות חשודות: $x=\\frac14$ (מאפסת), $x=\\frac13$ (לא קיימת) וקצות הקטע", 2),
               ("חישוב ערכי $f$: $-\\left(\\frac14\\right)^{4/3},\\ 0,\\ \\sqrt[3]{4},\\ \\frac23$", 3),
               ("מקסימום $\\sqrt[3]{4}$ ומינימום $-\\left(\\frac14\\right)^{4/3}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את $x=\\frac13$, שבה הנגזרת אינה קיימת (המכנה מתאפס).",
              "לחשב $\\sqrt[3]{3x-1}$ לא נכון בקצה $x=-1$ (שורש שלישי של $-4$ הוא שלילי).",
              "לשכוח את קצות הקטע."],
    steps=[
        num("באיזה ערך $x$ מתאפס המונה של $f'(x)=\\frac{4x-1}{(3x-1)^{2/3}}$? (עשרוני)", R(1, 4), "$4x-1=0$ ולכן $x=\\frac14$."),
        num("מהו $f\\left(\\frac14\\right)=-\\left(\\frac14\\right)^{4/3}$? (עשרוני)", -(R(1, 4))**R(4, 3),
            "$\\frac14\\sqrt[3]{-\\frac14}=-\\left(\\frac14\\right)^{4/3}\\approx-0.1575$ (נבדק מספרית)."),
        num("מהו $f(-1)=-1\\cdot\\sqrt[3]{-4}$? (עשרוני)", mp.cbrt(4), "$\\sqrt[3]{4}\\approx1.5874$."),
        ch("מהם הערך הגדול ביותר והקטן ביותר של $f$ בקטע?",
           "הגדול $\\sqrt[3]{4}$ (ב-$x=-1$) והקטן $-\\left(\\frac14\\right)^{4/3}$ (ב-$x=\\frac14$)",
           ["הגדול $\\frac23$ והקטן $0$", "הגדול $\\sqrt[3]{4}$ והקטן $0$ (ב-$x=\\frac13$)", "הגדול $\\sqrt[3]{4}$ והקטן $-1$"],
           "$f\\left(\\frac13\\right)=0$ אינו המינימום כי $f\\left(\\frac14\\right)<0$ (נבדק על רשת צפופה)."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: differentiable at 2 =====
sol6 = sp.solve([sp.Eq(8*a, 4 + b), sp.Eq(12*a, 4)], [a, b], dict=True)[0]
assert sol6 == {a: R(1, 3), b: -R(4, 3)}
fq = lambda v: (mp.mpf(1)/3)*v**3 if v <= 2 else v**2 - mp.mpf(4)/3
d_ = mp.mpf('1e-8')
assert abs((fq(2 + d_) - fq(2))/d_ - 4) < 1e-6 and abs((fq(2 - d_) - fq(2))/(-d_) - 4) < 1e-6

add(6, "ב",
    rubric=rub(("רציפות ב-$x=2$: $8a=4+b$", 3),
               ("הנגזרת הימנית $f'_+(2)=4$", 2),
               ("הנגזרת השמאלית $f'_-(2)=12a$", 2),
               ("השוואת נגזרות ופתרון $a=\\frac13$, $b=-\\frac43$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לדרוש רק שוויון נגזרות בלי רציפות (או להפך). גזירות דורשת את שניהם.",
              "לשכוח את התנאי השני: גם כשהנגזרות החד-צדדיות שוות, בלי רציפות הפונקציה אינה גזירה.",
              "טעות בנגזרת של $ax^3$: היא $3ax^2$ ולכן $12a$ ב-$x=2$."],
    steps=[
        ch("אילו שני תנאים נדרשים לגזירות ב-$x=2$?", "רציפות ב-$2$ ושוויון הנגזרות החד-צדדיות",
           ["שוויון הנגזרות החד-צדדיות בלבד", "רציפות ב-$2$ בלבד", "שוויון $a=b$"],
           "גזירות מחייבת רציפות וגם ששתי הנגזרות החד-צדדיות יהיו שוות."),
        num("מהי הנגזרת הימנית $f'_+(2)$ של $x^2+b$?", 4, "$2x=4$ ב-$x=2$ (נבדק במנת הפרשים נומרית)."),
        num("מהו $a$? (עשרוני)", sol6[a], "$12a=4$ ולכן $a=\\frac13\\approx0.3333$ (sympy)."),
        num("מהו $b$? (עשרוני)", sol6[b], "$8a=4+b$ נותן $b=\\frac83-4=-\\frac43\\approx-1.3333$ (sympy)."),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "22A-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ב, מועד א'",
    "year": 2022,
    "examDate": "14/06/2022",
    "sourceFile": "calculus-1/22A-B solution.pdf",
    "solutionFile": "calculus-1/22A-B solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

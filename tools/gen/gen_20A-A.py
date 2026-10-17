# -*- coding: utf-8 -*-
"""Generator for tools/raw/20A-A.json -- calculus-1 (20151), semester A 2020, moed A (20/02/2020).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_20A-A.py

Source: sitting 20A-A, pp.1-6 (typed exam with the official worked solution after every question).
Part A (mandatory): Q1 (20%). Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Q1 sketch (p.3 top) is shipped as a figure inside the solution.
- Q6a/Q6b share the function of Q6; the stem is repeated in both parts.
- Q6a: the official solution treats only x=3 (the endpoint x=2 is not discussed); transcribed as printed.

Checks (tools/verify/20A-A/check.py, sympy): derivatives, limits, asymptotes, partial fractions, antiderivatives,
arc length, the continuity parameter and the solid of revolution all match the official answers. 0 mismatches.
No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20A-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**תחום ההגדרה:** $x\neq 0$. מיון אי-רציפות ב-$x=0$:
$$\lim_{x\to0^+}xe^{\frac1x}=\lim_{x\to0^+}\frac{e^{\frac1x}}{\frac1x}=\left[\frac{\infty}{\infty}\right]=\lim_{x\to0^+}\frac{\left(e^{\frac1x}\right)'}{\left(\frac1x\right)'}=\lim_{x\to0^+}\frac{-\frac{1}{x^2}e^{\frac1x}}{-\frac{1}{x^2}}=\lim_{x\to0^+}e^{\frac1x}=+\infty$$
$$\lim_{x\to0^-}xe^{\frac1x}=\lim_{x\to0^-}\frac{e^{\frac1x}}{\frac1x}=\left[\frac{0}{\infty}\right]=0$$
אז $x=0$ היא נקודת אי-רציפות מסוג שני. לכן $x=0$ היא אסימפטוטה אנכית.
**אסימפטוטות משופעות/אופקיות** $y=ax+b$:
$$a=\lim_{x\to\pm\infty}\frac{xe^{\frac1x}}{x}=\lim_{x\to\pm\infty}e^{\frac1x}=1,$$
$$b=\lim_{x\to\pm\infty}\left(xe^{\frac1x}-x\right)=\{\infty-\infty\}=\lim_{t\to0}\left(\frac1te^t-\frac1t\right)=\lim_{t\to0}\frac{e^t-1}{t}=\lim_{t\to0}\frac{e^t}{1}=1$$
לכן $y=x+1$ היא אסימפטוטה משופעת.
**חקירה עם הנגזרת הראשונה:** תחומי עלייה וירידה, נקודות קיצון.
$$f'(x)=\left(xe^{\frac1x}\right)'=e^{\frac1x}-\frac{x}{x^2}e^{\frac1x}=e^{\frac1x}\frac{x-1}{x}$$
טבלת סימנים של $f'$: חיובית ב-$x<0$ (עולה), שלילית ב-$0<x<1$ (יורדת), חיובית ב-$x>1$ (עולה).
נקודת מינימום מקומי: $x=1$, $f(1)=e$.
**תחומי קמירות, נקודות פיתול:**
$$f''(x)=\left(e^{\frac1x}\left(1-\frac1x\right)\right)'=-\frac{1}{x^2}e^{\frac1x}\left(1-\frac1x\right)+e^{\frac1x}\frac{1}{x^2}=e^{\frac1x}\frac{1}{x^2}\left(-1+\frac1x+1\right)=e^{\frac1x}\frac{1}{x^3}$$
טבלת סימנים של $f''$: שלילית ב-$x<0$ (קעורה), חיובית ב-$x>0$ (קמורה). אין נקודות פיתול כי $x=0$ אינה בתחום ההגדרה.
סקיצה של הגרף:
![סקיצה של הגרף y = x·e^(1/x) עם האסימפטוטה האנכית x=0, האסימפטוטה המשופעת y=x+1 והמינימום ב-x=1](images/exams/20A-A-Q1-graph.png)
"""

SOL2A = r"""
נציין כי $-1\le\cos 2n\le 1$ והביטוי
$$\lim_{n\to\infty}\frac{n+\sqrt[3]{1-n^6}}{1+n^3}=\lim_{n\to\infty}\frac{\frac{1}{n^2}+\sqrt[3]{\frac{1}{n^9}-\frac{1}{n^3}}}{\frac{1}{n^3}+1}=0$$
לכן
$$\lim_{n\to\infty}\frac{n+\sqrt[3]{1-n^6}}{1+n^3}\cos 2n=0$$
"""

SOL2B = r"""
התנאי שלפונקציה (פולינום) יש משיק אופקי הוא $y'=0$. התנאי שבאותה נקודה לגרף הפונקציה יש פיתול אומר ש-$y''=0$. אז באותה נקודה $x$ מתקיים $3ax^2+2bx+c=0$ ו-$6ax+2b=0$. לכן $x=-\frac{b}{3a}$ ומהצבה נקבל
$$3a\left(-\frac{b}{3a}\right)^2+2b\left(-\frac{b}{3a}\right)+c=0\ \Rightarrow\ -\frac{b^2}{3a}+c=0$$
או $b^2=3ac$.
"""

SOL3A = r"""
$$\lim_{x\to0}(\cos x)^{\frac{1}{\sin^2(2x)}}=\{1^{\infty}\}=\lim_{x\to0}\left(1+\cos x-1\right)^{\frac{1}{\sin^2(2x)}}=$$
$$=\lim_{x\to0}\left(1+\cos x-1\right)^{\frac{1}{\cos x-1}\cdot\frac{\cos x-1}{\sin^2(2x)}}=\lim_{x\to0}\left(1+\cos x-1\right)^{\frac{1}{\cos x-1}\cdot\frac{-2\sin^2\frac{x}{2}}{\sin^2(2x)}}=e^{\frac{-2\cdot\frac14}{4}}=e^{-\frac18}$$
"""

SOL3B = r"""
$$\int\frac{dx}{x\left(\ln^2x-5\ln x+6\right)}=\begin{vmatrix}t=\ln x\\dt=\frac{dx}{x}\end{vmatrix}=\int\frac{dt}{t^2-5t+6}=\int\frac{dt}{(t-2)(t-3)}$$
$$\frac{1}{(t-2)(t-3)}=\frac{A}{t-2}+\frac{B}{t-3}=\frac{A(t-3)+B(t-2)}{(t-2)(t-3)}\ \Rightarrow\ A=-1,\ B=1$$
$$\int\frac{dt}{(t-2)(t-3)}=\int\left(-\frac{1}{t-2}+\frac{1}{t-3}\right)dt=-\ln|t-2|+\ln|t-3|+C=\ln\left|\frac{t-3}{t-2}\right|+C$$
$$\int\frac{dx}{x\left(\ln^2x-5\ln x+6\right)}=\ln\left|\frac{\ln x-3}{\ln x-2}\right|+C$$
"""

SOL4A = r"""
נמצא את הגבולות החד-צדדיים:
$$\lim_{x\to0^-}f(x)=\lim_{x\to0^-}\left(\frac{1}{\sqrt{2-x}-1}-\sqrt{2-x}\right)=\frac{1}{\sqrt2-1}-\sqrt2=\frac{1-\sqrt2\left(\sqrt2-1\right)}{\sqrt2-1}=1$$
$$\lim_{x\to0^+}f(x)=\lim_{x\to0^+}\frac{\sqrt{1+ax}-1+1-\cos x}{x}=\lim_{x\to0^+}\left(\frac{\sqrt{1+ax}-1}{x}+\frac{2\sin^2\frac{x}{2}}{x}\right)=\frac12a+0=\frac{a}{2}$$
הפונקציה תהיה רציפה ב-$x=0$ אם $\frac{a}{2}=1$ ולכן $a=2$.
"""

SOL4B = r"""
נמצא את אורך הקשת לפי הנוסחה: $l=\int_{-2}^{2}\sqrt{1+(y')^2}\,dx$.
$$y'=\frac{e^x-e^{-x}}{2},$$
$$1+(y')^2=1+\left(\frac{e^x-e^{-x}}{2}\right)^2=1+\frac{e^{2x}-2+e^{-2x}}{4}=\frac{e^{2x}+2+e^{-2x}}{4}=\left(\frac{e^x+e^{-x}}{2}\right)^2,$$
$$l=\int_{-2}^{2}\sqrt{1+(y')^2}\,dx=\int_{-2}^{2}\frac{e^x+e^{-x}}{2}\,dx=2\int_{0}^{2}\frac{e^x+e^{-x}}{2}\,dx=\left(e^x-e^{-x}\right)\Big|_0^2=e^2-e^{-2}$$
"""

SOL5A = r"""
נבדוק את הגזירות של $f$ לפי ההגדרה:
$$f'(a)=\lim_{\Delta x\to0}\frac{f(a+\Delta x)-f(a)}{\Delta x}=\lim_{\Delta x\to0}\frac{|a+\Delta x-a|\,g(a+\Delta x)-|a-a|\,g(a)}{\Delta x}=$$
$$=\lim_{\Delta x\to0}\frac{|\Delta x|\,g(a+\Delta x)}{\Delta x}=\lim_{\Delta x\to0}\frac{|\Delta x|}{\Delta x}\,g(a+\Delta x)=0,$$
כי הביטוי $\frac{|\Delta x|}{\Delta x}$ חסום $-1\le\frac{|\Delta x|}{\Delta x}\le1$ ו-$g(a+\Delta x)$ שואף ל-$0$, כי $g(x)$ רציפה.
"""

SOL5B = r"""
$$\int\frac{dx}{\sqrt[4]{x^3}\left(\sqrt{x}+2\sqrt[4]{x}\right)}=\begin{vmatrix}x=t^4\\dx=4t^3dt\end{vmatrix}=\int\frac{4t^3dt}{t^3\left(t^2+2t\right)}=4\int\frac{dt}{t(t+2)},$$
$$\frac{1}{t(t+2)}=\frac{A}{t}+\frac{B}{t+2}=\frac{A(t+2)+Bt}{t(t+2)},\quad A=\frac12,\ B=-\frac12,$$
$$\int\frac{dx}{\sqrt[4]{x^3}\left(\sqrt{x}+2\sqrt[4]{x}\right)}=2\int\left(\frac1t-\frac{1}{t+2}\right)dt=2\left(\ln|t|-\ln|t+2|\right)+C=2\left(\ln\left|\sqrt[4]{x}\right|-\ln\left|\sqrt[4]{x}+2\right|\right)+C=$$
$$=\frac12\ln x-2\ln\left(\sqrt[4]{x}+2\right)+C$$
"""

SOL6A = r"""
תחום ההגדרה של הפונקציה הוא $x\in[2,\infty)$. נחקור את הפונקציה לקיצון מקומי.
$$f'(x)=\frac{1}{2\sqrt{x-2}}e^{-\frac x2}-\frac12\sqrt{x-2}\,e^{-\frac x2}=\frac{1}{2\sqrt{x-2}}e^{-\frac x2}\left(1-x+2\right)=\frac{3-x}{2\sqrt{x-2}}e^{-\frac x2},$$
הנקודה $x=3$ היא נקודת המקסימום המקומי כי $f'(3)=0$ והנגזרת משנה את הסימן במעבר דרך $x=3$ ממינוס לפלוס.
"""

SOL6B = r"""
נמצא את נפח הגוף לפי שיטת הפרוסות כאשר $2\le x\le3$. לכן
$$V=\pi\int_2^3(x-2)e^{-x}dx=\begin{vmatrix}u=x-2&du=dx\\dv=e^{-x}dx&v=-e^{-x}\end{vmatrix}=\pi\left(-(x-2)e^{-x}\Big|_2^3+\int_2^3e^{-x}dx\right)=$$
$$=\pi\left(-e^{-3}-e^{-x}\Big|_2^3\right)=\pi\left(e^{-2}-2e^{-3}\right)$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $y=x\cdot e^{\frac{1}{x}}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, נקודות קיצון, "
      "תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1),

    Q(2, "computation", "sequences_limits",
      r"חשבו את הגבול $\lim_{n\to\infty}\frac{n+\sqrt[3]{1-n^6}}{1+n^3}\cos(2n)$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "function_investigation",
      r"נתון כי לפונקציה (פולינום) $y=ax^3+bx^2+cx+d$ כאשר $a\neq0$ יש משיק אופקי ונקודת פיתול עבור אותו ערך של $x$. "
      r"הוכיחו כי מתקיים השוויון $b^2=3ac$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0}(\cos x)^{\frac{1}{\sin^2(2x)}}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{dx}{x\left(\ln^2x-5\ln x+6\right)}$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "continuity",
      r"עבור איזה ערך של הפרמטר $a>0$ הפונקציה "
      r"$f(x)=\begin{cases}\dfrac{1}{\sqrt{2-x}-1}-\sqrt{2-x}, & x\le0\\[2mm] \dfrac{\sqrt{1+ax}-\cos x}{x}, & x>0\end{cases}$"
      " רציפה ב-$x=0$?",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"חשבו את אורך הקשת של העקומה $y=\cosh x$ בתחום $-2\le x\le2$. ניזכר: $\cosh x=\frac{e^x+e^{-x}}{2}$.",
      SOL4B, part="ב", points=10),

    Q(5, "proof", "derivatives_tangents",
      r"נתון כי פונקציה $g(x)$ רציפה ב-$x=a$ ו-$g(a)=0$. הוכיחו כי פונקציה $f(x)=|x-a|\,g(x)$ גזירה ב-$x=a$ ומצאו את $f'(a)$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{dx}{\sqrt[4]{x^3}\left(\sqrt{x}+2\sqrt[4]{x}\right)}$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "extrema_optimization",
      r"נתונה הפונקציה $f(x)=\sqrt{x-2}\,e^{-\frac{x}{2}}$. חקרו את הפונקציה לקיצון מקומי (לוקלי).",
      SOL6A, part="א", points=10),

    Q(6, "computation", "definite_integrals",
      r"נתונה הפונקציה $f(x)=\sqrt{x-2}\,e^{-\frac{x}{2}}$. מצאו את נפח הגוף הנוצר כסיבוב של התחום החסום על ידי גרף הפונקציה, "
      r"ציר ה-$x$ והישר $x=b$ כאשר $x=b$ היא נקודת המקסימום המקומי שמצאתם בסעיף א' סביב ציר ה-$x$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "20A-A",
    "examLabel": "מבחן סוף סמסטר א' תש\"פ, מועד א'",
    "year": 2020,
    "examDate": "20/02/2020",
    "sourceFile": "calculus-1/20A-A exam+solution.pdf",
    "solutionFile": "calculus-1/20A-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

# -*- coding: utf-8 -*-
"""Generator for tools/raw/17A-A.json -- calculus-1 (20151), semester A 2017, moed A (printed date 25.06.17).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_17A-A.py

Source: sitting 17A-A, pp.1-7 (typed exam; the official worked solution follows every question).
Part A (mandatory): Q1 (20%). Part B: choose 4 of Q2-Q6 (each split into parts a/b, 10% each).

Transcription notes
- Q1: the sketch printed in the official solution is cropped as a figure; sign diagrams are transcribed as sentences.
- Q4a: the printed text carries the function definition and, separately, "for which a is f continuous at x=a?"
  (each followed by "(10%)"); merged into one part a whose solution holds both the limit and the value of a.
- Q4b: the printed stem has a stray "Q" after dx ("dxQ"); the solution names the integral Q. Stem written with dx.
- Q6a: the official solution computes P2(1.05) as 1.02466875 and concludes 1.02467 +- 1e-5. The correct value is
  1.0246875 and the interval must be 1.02469 +- 1e-5 (the true sqrt(1.05)=1.024695 lies outside the printed one).
  Final-answer error: shipped with the "הפתרון הרשמי עם תיקון" label, solutionSource solved, official:false.

Checks: tools/verify/17A-A/check.py (sympy), 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "17A-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**תחום הגדרה:** $x\in(-\infty,1)\cup(1,\infty)$.
**אסימפטוטה אנכית:** $x=1$:
$$\lim_{x\to1^+}\frac{4x^2-2x-1}{x-1}=\frac1{0^+}=+\infty$$
$$\lim_{x\to1^-}\frac{4x^2-2x-1}{x-1}=\frac1{0^-}=-\infty$$
**אסימפטוטה משופעת:**
$$a_\pm=\lim_{x\to\pm\infty}\frac{4x^2-2x-1}{x(x-1)}=4$$
$$b_\pm=\lim_{x\to\pm\infty}\left(\frac{4x^2-2x-1}{x-1}-4x\right)=\lim_{x\to\pm\infty}\frac{2x-1}{x-1}=2$$
$$y=4x+2$$
**תחומי עלייה וירידה, נקודות קיצון:**
$$y'=\frac{(8x-2)(x-1)-\left(4x^2-2x-1\right)}{(x-1)^2}=\frac{4x^2-8x+3}{(x-1)^2}=0$$
$$x_1=\frac12,\quad x_2=\frac32$$
סימני נגזרת: חיובית ב-$x<\frac12$ (עולה), שלילית ב-$\frac12<x<1$ וב-$1<x<\frac32$ (יורדת), חיובית ב-$x>\frac32$ (עולה).
$$y_{max}=y(0.5)=2,\quad y_{min}=y(1.5)=10$$
**תחומי קמירות וקעירות, נקודות פיתול:**
$$y''=\frac{2}{(x-1)^3}$$
סימני נגזרת שנייה: שלילית ב-$x<1$ (קעורה), חיובית ב-$x>1$ (קמורה). אין נקודת פיתול.
נקודות חיתוך עם צירים: $(0,1)$, $\left(\frac{1+\sqrt5}{4},0\right)$, $\left(\frac{1-\sqrt5}{4},0\right)$.
![שרטוט הגרף של y = (4x² − 2x − 1)/(x − 1) עם האסימפטוטה האנכית x = 1 והאסימפטוטה המשופעת y = 4x + 2](images/exams/17A-A-Q1-graph.png)
"""

SOL2A = r"""
נוכיח שהסדרה חסומה: $a_n\le4.5$.
בסיס האינדוקציה: $a_1=1\le4.5$.
הנחת האינדוקציה: $a_n\le4.5$. מכאן:
$$\frac{a_n}{3}\le1.5\ \Rightarrow\ \frac{a_n}{3}+3\le4.5\ \Rightarrow\ a_{n+1}\le4.5$$
לפי עיקרון האינדוקציה הוכחנו שלכל $n$ מתקיים $a_n\le4.5$.
נוכיח שהסדרה עולה מונוטונית:
בסיס האינדוקציה: $a_2=\frac{10}{3}\ge1=a_1$.
הנחת האינדוקציה: $a_{n+1}\ge a_n$. מכאן:
$$\frac{a_{n+1}}{3}\ge\frac{a_n}{3}\ \Rightarrow\ \frac{a_{n+1}}{3}+3\ge\frac{a_n}{3}+3\ \Rightarrow\ a_{n+2}\ge a_{n+1}$$
לפי עיקרון האינדוקציה הוכחנו שלכל $n$ מתקיים $a_{n+1}\ge a_n$.
הוכחנו שהסדרה חסומה מלמעלה ועולה מונוטונית, לכן לפי משפט ווירשטרס היא מתכנסת. נחשב גבול:
$$\lim_{n\to\infty}a_{n+1}=\frac13\lim_{n\to\infty}a_n+3,\quad L=\frac13L+3,\quad\frac23L=3,\quad L=4.5$$
"""

SOL2B = r"""
$$\int\frac{dx}{\cos^2x+4\cos^4x}=\left\{\begin{matrix}\tan x=t,\quad x=\arctan t,\quad dx=\frac{dt}{1+t^2}\\\cos^2x=\frac1{1+t^2}\end{matrix}\right\}=$$
$$=\int\frac{\frac{dt}{1+t^2}}{\frac1{1+t^2}+\frac4{\left(1+t^2\right)^2}}=\int\frac{\left(1+t^2\right)dt}{5+t^2}=\int\left(1-\frac4{5+t^2}\right)dt=$$
$$=t-\frac4{\sqrt5}\arctan\frac t{\sqrt5}=\tan x-\frac4{\sqrt5}\arctan\frac{\tan x}{\sqrt5}+C$$
"""

SOL3A = r"""
$$p=(\cos x)^{\frac1{x\sin x}},\qquad\ln p=\frac1{x\sin x}\ln\cos x$$
$$\ln p=\frac{\ln\cos x}{x\sin x},\qquad\lim_{x\to0}\ln p=\lim_{x\to0}\frac{\ln\cos x}{x\sin x}=\left[\frac00\right]=\lim_{x\to0}\frac{\frac{-\sin x}{\cos x}}{\sin x+x\cos x}=$$
$$=\lim_{x\to0}\frac{-\sin x}{\cos x\left(\sin x+x\cos x\right)}=\lim_{x\to0}\frac{-1}{\cos x\left(1+\frac x{\sin x}\cos x\right)}=-\frac12$$
$$p=e^{-0.5}$$
"""

SOL3B = r"""
$$y=\cos\left(\frac{\pi e^x}{6}\right)$$
$$\Delta x=0.1,\quad x_0=0$$
$$y(0)=\frac{\sqrt3}{2},\qquad y'(x)=-\frac\pi6e^x\sin\frac{\pi e^x}{6},\qquad y'(0)=-\frac\pi6\sin\frac\pi6=-\frac\pi{12}$$
$$y(0.1)-y(0)\approx y'(0)\Delta x$$
$$y(0.1)\approx y(0)+y'(0)\Delta x=\frac{\sqrt3}{2}-\frac\pi{12}\cdot0.1\approx0.8398\approx0.84$$
"""

SOL4A = r"""
$$\lim_{x\to a}\frac{\sqrt{2x-a}-\sqrt x}{x^2-a^2}=\lim_{x\to a}\frac{2x-a-x}{(x-a)(x+a)\left(\sqrt{2x-a}+\sqrt x\right)}=$$
$$=\lim_{x\to a}\frac{x-a}{(x-a)(x+a)\left(\sqrt{2x-a}+\sqrt x\right)}=\lim_{x\to a}\frac1{(x+a)\left(\sqrt{2x-a}+\sqrt x\right)}=$$
$$=\frac1{4a\sqrt a}$$
הפונקציה רציפה בנקודה $x=a$ כאשר הגבול שווה לערך הפונקציה בנקודה:
$$\frac1{4a\sqrt a}=\sqrt a,\quad4a^2=1,\quad a=0.5$$
"""

SOL4B = r"""
$$Q=\int_0^1e^x\sin(\pi x)\,dx=\left\{\begin{matrix}u=\sin(\pi x),&dv=e^x\,dx\\du=\pi\cos\pi x\,dx,&v=e^x\end{matrix}\right\}=$$
$$=\left(e^x\sin(\pi x)\right)\Big|_0^1-\pi\int_0^1e^x\cos\pi x\,dx=\left\{\begin{matrix}u=\cos(\pi x),&dv=e^x\,dx\\du=-\pi\sin\pi x\,dx,&v=e^x\end{matrix}\right\}=$$
$$=e^1\sin(\pi)-e^0\sin0-\pi\left\{\left(e^x\cos(\pi x)\right)\Big|_0^1+\pi\int_0^1e^x\sin\pi x\,dx\right\}=$$
$$=\pi(e+1)-\pi^2Q$$
$$Q=\frac{\pi(e+1)}{1+\pi^2}$$
"""

SOL5A = r"""
$$y'=\sqrt[3]{(3x-12)^2}+\frac23x\frac{3}{\sqrt[3]{3x-12}}$$
$$y'=\frac{3x-12+2x}{\sqrt[3]{3x-12}}=\frac{5x-12}{\sqrt[3]{3x-12}}$$
תחום הגדרה של הנגזרת: $x\ne4$. בנקודה $x=4$ הפונקציה מוגדרת, לכן $x=4$ היא נקודה חשודה.
$$y'=0\ \Rightarrow\ x=2.4$$
$$y(0)=0,\qquad y(2.4)\cong6.829,\quad y(4)=0,\quad y(6)\cong19.81$$
$$y_{max}=y(6)=6\cdot\sqrt[3]{36}\cong19.81$$
$$y_{min}=y(0)=y(4)=0$$
"""

SOL5B = r"""
$$\frac{x^3+3x^2+5}{x\left(x^2+2x+5\right)}=1+\frac{x^2-5x+5}{x\left(x^2+2x+5\right)}$$
$$\frac{x^2-5x+5}{x\left(x^2+2x+5\right)}=\frac Ax+\frac{Bx+C}{x^2+2x+5}$$
$$x^2-5x+5=A\left(x^2+2x+5\right)+x(Bx+C)$$
$$x=0\ \Rightarrow\ 5=5A,\quad A=1$$
$$x^2:\quad1=A+B,\quad B=0$$
$$x:\quad-5=2A+C,\quad C=-7$$
$$\int\frac{\left(x^3+3x^2+5\right)dx}{x\left(x^2+2x+5\right)}=\int\left(1+\frac1x-\frac7{(x+1)^2+4}\right)dx=x+\ln|x|-\frac72\arctan\frac{x+1}{2}+C$$
"""

SOL6A = r"""
הפתרון הרשמי עם תיקון: בפתרון הרשמי חושב $P_2(1.05)=1.02466875$ והתשובה נכתבה כ-$1.02467\pm10^{-5}$. הערך הנכון הוא $P_2(1.05)=1.0246875$, והתשובה היא $1.02469\pm10^{-5}$ (הערך המדויק $\sqrt{1.05}=1.024695\ldots$ אינו נמצא בקטע שנכתב בפתרון הרשמי). התיקון נבדק (sympy).
$$f(x)=\sqrt x,\quad f(1)=1$$
$$f'(x)=\frac1{2\sqrt x},\quad f'(1)=\frac12$$
$$f''(x)=-\frac1{4\sqrt{x^3}},\quad f''(1)=-\frac14$$
$$f'''(x)=\frac3{8\sqrt{x^5}},\quad f'''(c)=\frac3{8\sqrt{c^5}}$$
$$P_2(x)=1+0.5(x-1)-\frac18(x-1)^2$$
$$\sqrt{1.05}\approx P_2(1.05)=1+0.5(0.05)-\frac18(0.05)^2=1.0246875$$
$$|R_2|=\frac{(0.05)^3}{16\sqrt{c^5}}\le\frac{(0.05)^3}{16}=7.81\cdot10^{-6}<10^{-5}$$
$$\sqrt{1.05}\approx1.02469\pm10^{-5}$$
"""

SOL6B = r"""
נקודות חיתוך בין הקווים: $x=0$, $x=2$:
$$S=\int_0^2\left(\sqrt{32x}-x^3\right)dx=\left(\sqrt{32}\cdot\frac{2\sqrt{x^3}}{3}-\frac{x^4}{4}\right)\Bigg|_0^2=\frac{32}{3}-4\approx6.67$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה הבאה $y=\frac{4x^2-2x-1}{x-1}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, "
      "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.", SOL1),

    Q(2, "proof", "sequences_limits",
      r"נתונה הסדרה $a_1=1,\ a_{n+1}=\frac{a_n}{3}+3$. הוכח שהסדרה מתכנסת וחשב את גבולה.",
      SOL2A, part="א", points=10),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{dx}{\cos^2x+4\cos^4x}$.", SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to0}(\cos x)^{\frac1{x\sin x}}$.", SOL3A, part="א", points=10),

    Q(3, "computation", "derivatives_tangents",
      r"חשבו בקירוב באמצעות דיפרנציאל $\cos\left(\frac{\pi e^{0.1}}{6}\right)$. "
      r"(ידוע כי $\sin(\pi/6)=0.5$, $\cos(\pi/6)=\sqrt3/2$).", SOL3B, part="ב", points=10),

    Q(4, "computation", "continuity",
      r"נתונה הפונקציה $f(x)$ עם פרמטר $a>0$: "
      r"$f(x)=\begin{cases}\dfrac{\sqrt{2x-a}-\sqrt x}{x^2-a^2},&x\ne a\\[2mm]\sqrt a,&x=a\end{cases}$. "
      r"עבור איזה ערך של פרמטר $a$ הפונקציה רציפה בנקודה $x=a$?", SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"חשבו: $\int_0^1e^x\sin(\pi x)\,dx$.", SOL4B, part="ב", points=10),

    Q(5, "computation", "extrema_optimization",
      r"מצאו מינימום ומקסימום מוחלטים של הפונקציה $y=x\cdot\sqrt[3]{(3x-12)^2}$ בקטע $[0,6]$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int\frac{\left(x^3+3x^2+5\right)dx}{x\left(x^2+2x+5\right)}$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "lhopital_taylor",
      r"מצאו פולינום טיילור מסדר שני לפונקציה $f(x)=\sqrt x$ סביב נקודה $x_0=1$, חשב בעזרת הפולינום בקירוב "
      r"$\sqrt{1.05}$ והערך את שגיאת החישוב.", SOL6A, part="א", points=10,
      solutionSource="solved", official=False),

    Q(6, "computation", "definite_integrals",
      r"חשבו שטח הכלוא בין גרפים של פונקציות $y=x^3$ ו-$y=\sqrt{32x}$.", SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "17A-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ז, מועד א'",
    "year": 2017,
    "examDate": "25/06/2017",
    "sourceFile": "calculus-1/17A-A exam+solution.pdf",
    "solutionFile": "calculus-1/17A-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

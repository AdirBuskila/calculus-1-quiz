# -*- coding: utf-8 -*-
"""Generator for tools/raw/17B-A.json -- calculus-1 (20151), semester A 2017, moed B (06/03/2017).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_17B-A.py

Source: sitting 17B-A. Exam: 2 typed pages. Solution: 5 handwritten pages, author not stated (labelled
"student-solution", official:false, confidence med; it needs the refuter pass). The Hebrew connecting words of the
handwritten pages are only partly legible, so the prose is a reconstruction of the written mathematics, and every
formula is checked (tools/verify/17B-A/check.py, sympy + numeric).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (Q2 one part; Q3-Q6 a/b parts, 10% each).

Transcription notes
- Q1/Q3b/Q4b: the handwritten sketches are cropped as figures inside the solutions (no names on them).
- Q2: the handwritten difference a(n+1)-a(n) has the denominator written "2-a_n"; it must be 2+a_n (the numerator
  3-a_n^2 is right, and the sign conclusion is unchanged). Silent, intermediate; logged in docs/ASK_ADIR.md.
- Q3b: the handwritten V2 line reads "9pi * integral" where it must be "2pi * integral" (the value 77pi/5 is right).
  Silent, intermediate; logged.
- Q4a: the handwritten range "1<x<X" for the Lagrange point is c, written as c.
- Q5a: FINAL-ANSWER error in the handwritten solution: f(1/4) is written 17/2 (it is 1/2+16 = 33/2), f(100) is
  written 52/5 = "52/2" and the maximum is declared at x=100. Correct values f(1/4)=33/2, f(4)=3, f(100)=251/25, so
  the maximum is 33/2 at x=1/4 and the minimum 3 at x=4. Shipped corrected with the
  "הפתרון שבמקור (לא רשמי) עם תיקון" label (the key is not official), solutionSource solved, official:false (sympy + grid check).

Checks: tools/verify/17B-A/check.py. No code in this sitting.
Blind re-check (solver, 2026-10-18): tools/verify/17B-A/blind_recheck.py re-derives every final answer
independently (sympy); all agree with the shipped answers (the labeled fix included), so confidence is high.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "17B-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "student-solution", "official": False, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**תחום ההגדרה:** $D(f)=\{x\in\mathbb R,\ x\neq1\}$. חיתוך עם הצירים: $(2,0)$ ו-$(0,4)$.
**אסימפטוטה אנכית** $x=1$: $\lim_{x\to1^+}f(x)=\lim_{x\to1^-}f(x)=+\infty$.
**אסימפטוטה משופעת / אופקית:**
$$a=\lim_{x\to\infty}\frac{f(x)}{x}=\lim_{x\to\infty}\frac{(x-2)^2}{x(x-1)^2}=0,\qquad b=\lim_{x\to\infty}f(x)=\lim_{x\to\infty}\frac{(x-2)^2}{(x-1)^2}=1$$
לכן $y=1$ היא אסימפטוטה אופקית (משני הצדדים, $\pm\infty$).
**עלייה וירידה:**
$$f'(x)=2\cdot\frac{x-2}{x-1}\cdot\frac{x-1-(x-2)}{(x-1)^2}=2\cdot\frac{x-2}{(x-1)^3}$$
טבלת סימנים של $f'$: חיובית ב-$x<1$ (עולה), שלילית ב-$1<x<2$ (יורדת), חיובית ב-$x>2$ (עולה). מינימום ב-$x=2$, $f(2)=0$.
**קמירות ונקודות פיתול:**
$$f''(x)=2\cdot\frac{(x-1)^3-(x-2)\cdot3(x-1)^2}{(x-1)^6}=2\cdot\frac{x-1-3(x-2)}{(x-1)^4}=2\cdot\frac{-2x+5}{(x-1)^4}$$
טבלת סימנים של $f''$: חיובית ב-$x<1$ (קמורה), חיובית ב-$1<x<\frac52$ (קמורה), שלילית ב-$x>\frac52$ (קעורה). נקודת פיתול ב-$x=\frac52$, $f\left(\frac52\right)=\frac19$.
**שרטוט:**
![סקיצה של הגרף של y = ((x−2)/(x−1))² עם האסימפטוטה האנכית x=1, האסימפטוטה האופקית y=1 והמינימום ב-x=2](images/exams/17B-A-Q1-sketch.png)
"""

SOL2 = r"""
$a_1=5,\quad a_{n+1}=2-\frac{1}{2+a_n}$. נחשב: $a_2=2-\frac17=\frac{13}{7}$, $a_3=2-\frac{1}{2+\frac{13}{7}}=2-\frac{7}{27}=\frac{47}{27}$.
**חסימות:** נראה באינדוקציה שמתקיים $\sqrt3\le a_n\le2$ לכל $n\ge2$. עבור $n=2$: $\sqrt3\le a_2\le2$. אם $\sqrt3\le a_k\le2$ אז
$$2+\sqrt3\le2+a_k\le4\ \Rightarrow\ \frac14\le\frac{1}{2+a_k}\le\frac{1}{2+\sqrt3}=2-\sqrt3$$
$$2-(2-\sqrt3)\le2-\frac{1}{2+a_k}\le2-\frac14\ \Rightarrow\ \sqrt3\le a_{k+1}\le2$$
**מונוטוניות:** נראה שהסדרה יורדת.
$$a_{n+1}-a_n=2-a_n-\frac{1}{2+a_n}=\frac{(2-a_n)(2+a_n)-1}{2+a_n}=\frac{3-a_n^2}{2+a_n}$$
מכיוון ש-$\sqrt3\le a_n\le2$ מתקיים $a_{n+1}-a_n\le0$.
לכן הסדרה יורדת וחסומה מלרע, ולכן מתכנסת (מ-$n=2$ ואילך, ובהכרח גם כולה). נסמן $\lim_{n\to\infty}a_n=L$:
$$L=2-\frac{1}{2+L}\ \Leftrightarrow\ L=\frac{4+2L-1}{2+L}\ \Leftrightarrow\ L^2=3\ \Leftrightarrow\ L_1=\sqrt3,\quad L_2=-\sqrt3$$
מכיוון ש-$\sqrt3\le a_n$ לא מתקבל $L_2$, ולכן $\lim_{n\to\infty}a_n=\sqrt3$.
"""

SOL3A = r"""
$$\lim_{x\to+\infty}\left(x-\ln\left(1+2e^x\right)\right)=\{\infty-\infty\}=\lim_{x\to+\infty}\left[\ln e^x-\ln\left(1+2e^x\right)\right]=\lim_{x\to+\infty}\ln\frac{e^x}{1+2e^x}=\ln\lim_{x\to+\infty}\frac{e^x}{1+2e^x}=\ln\frac12=-\ln2$$
"""

SOL3B = r"""
$y=1+x^3$, $x=1$, $y=9$: $9=1+x^3\Rightarrow x^3=8\Rightarrow x=2$.
![סקיצה של התחום בין y = 1 + x³, x = 1 ו-y = 9 וסיבובו סביב ציר ה-y](images/exams/17B-A-Q3b-sketch.png)
$V=V_1-V_2$:
$$V_1=2\pi\int_1^2x\cdot9\,dx=9\pi x^2\Big|_1^2=27\pi$$
$$V_2=2\pi\int_1^2x\left(1+x^3\right)dx=2\pi\int_1^2\left(x+x^4\right)dx=2\pi\left(\frac{x^2}{2}+\frac{x^5}{5}\right)\Big|_1^2=2\pi\left(2+\frac{32}{5}-\frac12-\frac15\right)=2\pi\cdot\frac{20+64-5-2}{10}=\frac{77\pi}{5}$$
$$V=27\pi-\frac{77\pi}{5}=\frac{58\pi}{5}$$
"""

SOL4A = r"""
נגדיר $f(x)=\ln x$ על $[1,x]$. הפונקציה $f$ רציפה ב-$[1,x]$ וגזירה ב-$(1,x)$, $f'(x)=\frac1x$, ולכן לפי משפט לגרנז' $f(x)-f(1)=f'(c)(x-1)$ עבור $1<c<x$, כלומר
$$\ln x-\ln1=\frac1c(x-1),\qquad1<c<x$$
$$\ln x=\frac1c(x-1)\ \Rightarrow\ \frac{x-1}{x}<\ln x<x-1$$
(כי $\frac1x<\frac1c<1$.)
"""

SOL4B = r"""
$y=\sqrt x$, נקודה $(4,2)$. משוואת המשיק: $y-2=y'(4)(x-4)$, ומכאן $y-2=\frac{1}{2\sqrt4}(x-4)=\frac{x-4}{4}$, כלומר $x=4y-4$.
![סקיצה: הגרף של y = √x, המשיק בנקודה (4,2) והתחום הכלוא עם ציר ה-x](images/exams/17B-A-Q4b-sketch.png)
$$S=\int_0^2\left(y^2-(4y-4)\right)dy=\left(\frac{y^3}{3}-2y^2+4y\right)\Big|_0^2=\frac83-8+8=\frac83$$
"""

SOL5A = r"""
**הפתרון שבמקור (לא רשמי) עם תיקון:** בפתרון הכתוב ערכי הפונקציה בשני קצות הקטע מחושבים בטעות ($f\left(\frac14\right)$ נכתב $\frac{17}{2}$, $f(100)$ נכתב $\frac{52}{2}$) והמקסימום נקבע ב-$x=100$. הערכים הנכונים הם $f\left(\frac14\right)=\frac12+16=\frac{33}{2}$ ו-$f(100)=10+\frac{1}{25}=\frac{251}{25}$, ולכן המקסימום המוחלט הוא $\frac{33}{2}$ ב-$x=\frac14$. הערך $f(4)=3$ והמינימום המוחלט נכונים. התיקון נבדק (sympy).
$$f'(x)=\frac{1}{2\sqrt x}-\frac{4}{x^2}=\frac{x^{\frac32}-8}{2x^2}=0\ \Rightarrow\ x^{\frac32}=8\ \Rightarrow\ x=4$$
$$f\left(\tfrac14\right)=\frac12+16=\frac{33}{2},\qquad f(4)=2+1=3,\qquad f(100)=10+\frac{1}{25}=\frac{251}{25}$$
$$\max_{\left[\frac14,100\right]}f(x)=\frac{33}{2}=f\left(\tfrac14\right),\qquad\min_{\left[\frac14,100\right]}f(x)=3=f(4)$$
"""

SOL5B = r"""
$$\int\sin^5x\,dx=\left|\begin{matrix}t=\cos x\\dt=-\sin x\,dx\\\sin^4x=\left(1-\cos^2x\right)^2\end{matrix}\right|=-\int\left(1-t^2\right)^2dt=-\int\left(1-2t^2+t^4\right)dt=-t+\frac{2t^3}{3}-\frac{t^5}{5}+C=-\cos x+\frac23\cos^3x-\frac15\cos^5x+C$$
"""

SOL6A = r"""
$$\lim_{x\to0^-}f(x)=\lim_{x\to0^-}\left(\frac{e^{ax}-1}{x}\right)^2=\lim_{x\to0^-}\left(a\cdot\frac{e^{ax}-1}{ax}\right)^2=a^2$$
$$\lim_{x\to0^+}f(x)=\lim_{x\to0^+}\left(4+e^{-\frac{a^2}{x}}\right)=4$$
לכן $a^2=b=4$, כלומר הפונקציה רציפה אם ורק אם $b=4$ ו-$a=\pm2$.
"""

SOL6B = r"""
$$\int\frac{\ln(x+1)}{\sqrt{x+1}}\,dx=\left|\begin{matrix}u=\ln(x+1)&du=\frac{dx}{x+1}\\dv=\frac{dx}{\sqrt{x+1}}&v=2\sqrt{x+1}\end{matrix}\right|=2\sqrt{x+1}\ln(x+1)-2\int\frac{dx}{\sqrt{x+1}}=2\sqrt{x+1}\ln(x+1)-4\sqrt{x+1}+C$$
"""

HEAD1 = (r"חקרו את הפונקציה הבאה $y=\left(\frac{x-2}{x-1}\right)^2$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, "
         "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.")

questions = [
    Q(1, "computation", "function_investigation", HEAD1, SOL1),

    Q(2, "proof", "sequences_limits",
      r"הוכיחו כי הסדרה $a_1=5,\ a_{n+1}=2-\frac{1}{2+a_n}$ מתכנסת וחשבו את הגבול שלה.",
      SOL2, points=20),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to+\infty}\left(x-\ln\left(1+2e^x\right)\right)$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום המישורי הכלוא בין הקווים $y=1+x^3,\ x=1,\ y=9$ סביב ציר ה-$y$.",
      SOL3B, part="ב", points=10),

    Q(4, "proof", "mean_value_theorems",
      r"הוכיחו כי $\frac{x-1}{x}<\ln x<x-1$ לכל $x>1$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"מצאו את השטח הכלוא בין: ציר ה-$x$, הגרף של $y=\sqrt x$ והמשיק שלו בנקודה $(4,2)$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "extrema_optimization",
      r"מצאו מינימום ומקסימום מוחלטים של הפונקציה $f(x)=\sqrt x+\frac4x$ בקטע $[0.25,100]$.",
      SOL5A, part="א", points=10,
      solutionSource="solved", official=False),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int\sin^5x\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "continuity",
      r"עבור אילו ערכים של $a,b$ תהיה הפונקציה "
      r"$f(x)=\begin{cases}x^{-2}\left(e^{ax}-1\right)^2,&x<0\\[1mm]b,&x=0\\[1mm]4+e^{-a^2/x},&x>0\end{cases}$ "
      r"רציפה בנקודה $x=0$?",
      SOL6A, part="א", points=10),

    Q(6, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int\frac{\ln(x+1)}{\sqrt{x+1}}\,dx$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "17B-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ז, מועד ב'",
    "year": 2017,
    "examDate": "06/03/2017",
    "sourceFile": "calculus-1/17B-A exam.pdf",
    "solutionFile": "calculus-1/17B-A handwritten-solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

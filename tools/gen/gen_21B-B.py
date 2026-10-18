# -*- coding: utf-8 -*-
"""Generator for tools/raw/21B-B.json -- calculus-1 (20151), semester B 2021 (תשפ"א), moed B.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_21B-B.py

Source: sitting 21B-B, pp.1-7 ("פתרונות מלאים למועד ב'": the question text, where printed, followed by the worked
solution; no separate exam file exists). Both source trees hold the identical file.

What the file does and does not contain
- Q1 (20%), Q3, Q4, Q5: stem and official solution are printed.
- Q2 is NOT in the file at all (p.1 ends with Q1 and p.3 starts with Q3). Held, reason "not-in-source".
- Q6a / Q6b: only the worked solution is printed, the question stems are not. The solutions are kept in raw next to
  the hold so the orchestrator can ship them once a stem is approved. Held, reason "stem-not-printed".
- Arbiter re-search 2026-10-18: the BSC and C24-BSC copies differ in file hash but render identically page by page
  (7 pages, same text); a text search of every other calculus-1 PDF in both trees (exams, practice sheets, summaries)
  finds no copy of the Q2 or Q6 stems (scanned files are not text-searchable). Holds kept; Adir must supply the stems.

Transcription notes
- Q1 sketch (p.2) and Q4b sketch (p.5) are shipped as figures inside the solutions.
- Q3a: the official solution is written in English and is kept as printed. Its conclusion "c in (-1,0)" is wrong
  (f(0)=5>0 and f(1)<0, f(-1)>0, so the sign change is on (0,1)); the printed f(1) = -3.99 is also off (-3.96).
  Final-line error -> "הפתרון הרשמי עם תיקון" label, solutionSource solved, official False.
- Q3b: the printed middle line drops a "ln" in "0.5 ln|t-3| - 0.5|t-1|"; restored silently (logged in ASK_ADIR).
- Q6a (held): the printed implicit derivative starts with 8x^4; d/dx(2x^4)=8x^3. The final slope 4 is unchanged;
  corrected silently (logged).

Checks (tools/verify/21B-B/check.py, sympy): every derivative, limit, extremum, parameter, integral, volume and area
matches the official answer, except the two slips named above. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "21B-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**I.**
1. $D(y)=(-\infty,-1)\cup(-1,\infty)$.
2. $\lim_{x\to-1^-}y=\lim_{x\to-1^+}y=+\infty$, לכן $x=-1$ נקודת אי-רציפות מסוג שני.
3. $k=\lim_{x\to\pm\infty}\frac{y}{x}=\lim_{x\to\pm\infty}\frac{(x+2)^2}{x(x+1)^2}=0,\quad b=\lim_{x\to\pm\infty}(y-kx)=\lim_{x\to\pm\infty}\frac{(x+2)^2}{(x+1)^2}=1$. הישרים $x=-1$ ו-$y=1$ הם אסימפטוטות.
4. $y\ge0$.
**II.**
1. $y'=2\frac{x+2}{x+1}\left(-\frac{1}{(x+1)^2}\right)=\frac{-2(x+2)}{(x+1)^3}$.
2. $x=-2$ נקודה קריטית.
3. $y$ עולה ב-$(-2,-1)$ ויורדת ב-$(-\infty,-2)$ וב-$(-1,\infty)$; $x=-2$ נקודת מינימום, $y(-2)=0$.
**III.**
1. $y''=\frac{-2(x+1)^3+2(x+2)3(x+1)^2}{(x+1)^6}=\frac{4x+10}{(x+1)^4}$.
2. $x=-\frac{5}{2}$.
3. $y''>0$ עבור $x>-\frac{5}{2}$, $y''<0$ עבור $x<-\frac{5}{2}$. נקודת פיתול: $\left(-\frac{5}{2},\frac{1}{9}\right)$.
![שרטוט הגרף של y = ((x+2)/(x+1))^2 עם האסימפטוטות x=-1 ו-y=1 והמינימום ב-x=-2](images/exams/21B-B-Q1-graph.png)
"""

SOL3A = r"""
**הפתרון הרשמי עם תיקון:** בפתרון הרשמי נכתב שהשורש נמצא בקטע $(-1,0)$ ושהערך $f(1)\approx-3.99$. אך $f(0)=5>0$, ו-$f(-1)\approx4.04>0$ (אין שינוי סימן בקטע $[-1,0]$), ואילו $f(1)\approx-3.96<0$. לכן שינוי הסימן הוא בקטע $(0,1)$ והשורש $c$ נמצא ב-$(0,1)$. להלן הפתרון הרשמי עם התיקון הזה.
$f(x)=2\sin^2(3x)+5\sqrt[3]{1-x^2}-4x^5$
Continues function for all $x$.
$f(0)=5,\quad f(1)=2\sin^2(3)-4\approx-3.96<0$
Therefore there exist $c\in(0,1)$ such that $f(c)=0$
$c$ is a root of $f(x)$.
"""

SOL3B = r"""
$$\int\frac{dx}{x(\ln x-1)(\ln x-3)}=\left[t=\ln x,\quad dt=\frac{dx}{x}\right]=\int\frac{dt}{(t-1)(t-3)}$$
$$\frac{1}{(t-1)(t-3)}=\frac{0.5}{t-3}-\frac{0.5}{t-1}$$
$$\int\frac{dt}{(t-3)(t-1)}=\int\left(\frac{0.5}{t-3}-\frac{0.5}{t-1}\right)dt=0.5\ln|t-3|-0.5\ln|t-1|=0.5\ln\left|\frac{t-3}{t-1}\right|$$
$$\int\frac{dx}{x(\ln x-1)(\ln x-3)}=0.5\ln\left|\frac{\ln x-3}{\ln x-1}\right|+c$$
"""

SOL4A = r"""
$$\lim_{x\to0}\frac{\ln\cos x}{\ln\cos4x}=\left(\frac{0}{0}\right)=\lim_{x\to0}\frac{\frac{-\sin x}{\cos x}}{\frac{-4\sin4x}{\cos4x}}=\frac{1}{4}\lim_{x\to0}\frac{\tan x}{\tan4x}=\left(\frac{0}{0}\right)=$$
$$=\frac{1}{4}\lim_{x\to0}\frac{\frac{1}{\cos^2x}}{\frac{4}{\cos^24x}}=\frac{1}{4}\lim_{x\to0}\frac{\cos^24x}{4\cos^2x}=\frac{1}{16}$$
"""

SOL4B = r"""
![שרטוט התחום הכלוא בין y=x^2, y=-2x+8 וציר ה-x, והישר X=4 שסביבו מסובבים](images/exams/21B-B-Q4b-region.png)
$$V=V_1+V_2=2\pi\int_0^2(4-x)x^2dx+2\pi\int_2^4(4-x)(-2x+8)dx=$$
$$2\pi\int_0^2\left(4x^2-x^3\right)dx+4\pi\int_2^4(4-x)^2dx=$$
$$=2\pi\left(\frac{4x^3}{3}-\frac{x^4}{4}\right)\Big|_0^2+4\pi\frac{(4-x)^3}{-3}\Big|_2^4=$$
$$=2\pi\left(\frac{32}{3}-\frac{16}{4}\right)-\frac{4\pi}{3}(0-8)=\frac{40\pi}{3}+\frac{32\pi}{3}=\frac{72\pi}{3}=24\pi$$
"""

SOL5A = r"""
נמצא את הנקודות הקריטיות:
$$f(x)=\ln(1+x^2)\ \Rightarrow\ f'(x)=\frac{2x}{1+x^2}=0\ \Rightarrow\ x=0$$
נמצא את הערכים של הפונקציה בנקודה $x=0$ ובקצוות של הקטע:
$f(0)=0$ (min), $f(-1)=\ln2$, $f(\sqrt{e-1})=\ln(e)=1$ (max).
"""

SOL5B = r"""
בודקים את הרציפות של הפונקציה בנקודה $x=0$:
$$\lim_{x\to0^+}\left(x^2+b\sin2x+c\right)=c,\qquad \lim_{x\to0^-}\left(ae^x\right)=a$$
לכן $a=c$.
נמצא את הנגזרות החד-צדדיות בנקודה $x=0$:
$$f'_+(0)=\lim_{\Delta x\to0^+}\frac{(\Delta x)^2+b\sin2\Delta x+c-a}{\Delta x}=\lim_{\Delta x\to0^+}\frac{(\Delta x)^2+b\sin2\Delta x}{\Delta x}=$$
$$=\lim_{\Delta x\to0^+}\left(\Delta x+\frac{b\sin2\Delta x}{\Delta x}\right)=\lim_{\Delta x\to0^+}\left(\Delta x+\frac{2b\sin2\Delta x}{2\Delta x}\right)=2b$$
$$f'_-(0)=\lim_{\Delta x\to0^-}\frac{ae^{\Delta x}-a}{\Delta x}=a\cdot\lim_{\Delta x\to0^-}\frac{e^{\Delta x}-1}{\Delta x}=a\cdot1=a$$
לכן $a=2b=c$.
"""

# Held items: the file prints only the worked solution of Q6; the stem is not printed (Q2 is absent altogether).
SOL6A_HELD = r"""
ראשית, יש לבדוק שהנקודה אכן נמצאת על הגרף של הפונקציה ומקיימת את המשוואה הנתונה: $2x^4+3x^2y^3-2\sin y=2$.
לאחר מכן, נגזור את המשוואה ונקבל
$$8x^3+6xy^3+9x^2y^2\frac{dy}{dx}-2\cos y\,\frac{dy}{dx}=0$$
$$8x^3+6xy^3=\frac{dy}{dx}\left(2\cos y-9x^2y^2\right)$$
$$\frac{dy}{dx}=\frac{8x^3+6xy^3}{2\cos y-9x^2y^2}\ \Rightarrow\ \frac{dy}{dx}(1,0)=4$$
$$y-0=4(x-1)\ \Rightarrow\ y=4x-4$$
"""

SOL6B_HELD = r"""
נמצא קודם נקודות חיתוך בין הפרבולה לבין הקווים הישרים ואחר כך את השטח המבוקש.
$$\frac{3}{10}x+\frac{3}{2}=\sqrt{3x-6}\ \Rightarrow\ 3x+15=10\sqrt{3x-6}$$
$$9x^2-210x+825=0\ \Rightarrow\ x_1=5$$
$$-\frac{1}{5}x-2=-\sqrt{3x-6}\ \Rightarrow\ x+10=5\sqrt{3x-6}$$
$$x^2-55x+250=0\ \Rightarrow\ x_1=5$$
$$S_1=\int_0^5\left(\frac{3}{10}x+\frac{3}{2}-\left(-\frac{1}{5}x-2\right)\right)dx=\int_0^5\left(\frac{1}{2}x+\frac{7}{2}\right)dx=\left(\frac{x^2}{4}+\frac{7}{2}x\right)\Big|_0^5=23.75$$
$$S_2=2\int_2^5\sqrt{3x-6}\,dx=2\left(\frac{1}{3}\frac{(3x-6)^{\frac32}}{\frac32}\right)\Big|_2^5=\frac{4}{9}\left((3x-6)^{\frac32}\right)\Big|_2^5=12$$
$$S=S_1-S_2=11.75$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $y=\left(\frac{x+2}{x+1}\right)^2$ לפי הסעיפים הבאים: תחום הגדרה, תחומי עליה/ירידה, נקודות קיצון, "
      "קמירות ונקודות פיתול, אסימפטוטות, שרטטו את גרף הפונקציה.",
      SOL1, points=20),

    {"num": 2, "kind": "computation", "hold": "not-in-source"},

    Q(3, "proof", "continuity",
      r"הוכיחו שלמשוואה $2\sin^2(3x)+5\sqrt[3]{1-x^2}-4x^5=0$ קיים שורש ממשי.",
      SOL3A, part="א", solutionSource="solved", official=False),

    Q(3, "computation", "indefinite_integrals",
      r"מצאו את האינטגרל $\int\frac{dx}{x(\ln x-1)(\ln x-3)}$.",
      SOL3B, part="ב"),

    Q(4, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to0}\frac{\ln\cos x}{\ln\cos4x}$.",
      SOL4A, part="א"),

    Q(4, "computation", "definite_integrals",
      r"מצאו את נפח הגוף המתקבל כסיבוב התחום הכלוא בין הקווים $y=x^2,\ y=-2x+8$ ו-$y=0$ כאשר $x\ge0$ סביב הציר $X=4$. "
      "צייר את התחום המסובב והסבר את פעולותיך.",
      SOL4B, part="ב"),

    Q(5, "computation", "extrema_optimization",
      r"נתונה הפונקציה $f(x)=\ln\left(1+x^2\right)$. מצאו את הערך הגדול ביותר ואת הערך הקטן ביותר שלה בקטע $\left[-1,\sqrt{e-1}\right]$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "derivatives_tangents",
      r"נתונה הפונקציה $f(x)=\begin{cases}ae^x, & x\le0\\ x^2+b\sin2x+c, & x>0\end{cases}$, כאשר $a,b,c\in\mathbb{R}$ פרמטרים. "
      r"עבור אילו ערכים של $a,b,c\in\mathbb{R}$ הפונקציה $f(x)$ תהיה גזירה ב-$x=0$.",
      SOL5B, part="ב", points=10),

    {"num": 6, "part": "א", "kind": "computation", "topic": "derivatives_tangents",
     "hold": "stem-not-printed", "solution": SOL6A_HELD.strip("\n"), "solutionSource": "official-pdf"},

    {"num": 6, "part": "ב", "kind": "computation", "topic": "definite_integrals",
     "hold": "stem-not-printed", "solution": SOL6B_HELD.strip("\n"), "solutionSource": "official-pdf"},
]

exam = {
    "examCode": "21B-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"א, מועד ב'",
    "year": 2021,
    "examDate": "",
    "sourceFile": "calculus-1/21B-B full solutions.pdf",
    "solutionFile": "calculus-1/21B-B full solutions.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

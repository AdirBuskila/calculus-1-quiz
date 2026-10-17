# -*- coding: utf-8 -*-
"""Generator for tools/raw/24A-A.json -- calculus-1 (20151), semester B 2024, moed A (19/03/2024).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24A-A.py

Source: sitting 24A-A, pp.1-7 (typed exam with the official worked solution after each "פתרון" label).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each). Weight of every question 20%.

Transcription notes
- Official solution transcribed in full, as printed. Rubric and steps are intentionally not written.
- Q1 is HELD: the official solution claims y''<0 for x<0 (concave down there), but y''=e^x(x^2-4x+6)/x^4 has a
  quadratic with negative discriminant, so y''>0 for every x!=0 (tools/verify/24A-A/check.py). Text kept as printed.
- Figures: Q1 official graph (p.2), Q4b official sketch (p.5), Q6b official figure (p.7).

Checks (tools/verify/24A-A/check.py, sympy): every derivative, limit, integral, extremum table, volume, tangent and
area matches the official answers except the Q1 convexity claim above.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24A-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**א. תחום הגדרה:** $D=\{x\neq 0\}$. אין נקודות חיתוך עם צירי הקואורדינטות.
**ב.** $f'(x)=\frac{e^x(x^2-2x)}{x^4}=\frac{e^x\cdot x(x-2)}{x^4}=\frac{e^x\cdot(x-2)}{x^3}$. מכאן רואים שהנגזרת מתאפסת רק ב-$x=2$ ובנוסף $y'>0$ כאשר $x<0\ \cup\ x>2$ וגם $y'<0$ כאשר $0<x<2$. הנקודה $x=2$ היא נקודת מינימום מקומי.
**ג.** $y''=\frac{e^x(x^2-4x+6)}{x^4}$. אין נקודות פיתול. בנוסף, $y''>0$ עבור $x>0$ וכאן הפונקציה קעורה (כלפי מעלה) ו-$y''<0$ עבור $x<0$ וכאן הפונקציה קמורה (כלפי מטה).
**ד.** $\begin{cases}\lim_{x\to0^-}\frac{e^x}{x^2}=+\infty\\ \lim_{x\to0^+}\frac{e^x}{x^2}=+\infty\end{cases}$ ולכן קו ישר $x=0$ (ציר ה-$y$) מהווה אסימפטוטה אנכית לגרף הפונקציה.
$\begin{cases}\lim_{x\to+\infty}f(x)=\lim_{x\to+\infty}\frac{e^x}{x^2}=+\infty\\ \lim_{x\to-\infty}f(x)=\lim_{x\to-\infty}\frac{e^x}{x^2}=0\end{cases}$ ולכן קו ישר $y=0$ מהווה אסימפטוטה אופקית לגרף הפונקציה במינוס אינסוף.

![הגרף הרשמי של הפונקציה](images/exams/24A-A-Q1-graph.png)
"""

SOL2A = r"""
$$\frac{x^2}{(x+2)(x^2+1)}=\frac{A}{x+2}+\frac{Bx+C}{x^2+1}$$
$$x^2=A(x^2+1)+(Bx+C)(x+2)$$
הצבת $x=-2$ נותנת $4=5A$; מקדמי $x^2$ נותנים $A+B=1$; מקדמי $x$ נותנים $2B+C=0$.
$$A=\frac{4}{5},\quad B=\frac{1}{5},\quad C=-\frac{2}{5}$$
$$\int\frac{x^2\,dx}{(x+2)(x^2+1)}=\frac{1}{5}\int\left(\frac{4}{x+2}+\frac{x-2}{x^2+1}\right)dx=\frac{1}{5}\left(4\ln|x+2|+\frac{1}{2}\ln(x^2+1)-2\arctan x\right)+C$$
"""

SOL2B = r"""
נוכיח באמצעות שיטת האינדוקציה ש-$a_n\le 2$ לכל $n$ טבעי, כלומר נוכיח שסדרה חסומה מלמעלה:
בסיס האינדוקציה: $n=1,\ a_1=1\le 2$.
שלב האינדוקציה: נניח ש-$a_n\le 2$ ומכאן נוכיח שגם $a_{n+1}\le 2$.
$$a_n\le 2\iff -a_n\ge -2\iff 5-a_n\ge 3\iff\{5-a_n>0\}\Rightarrow\frac{1}{5-a_n}\le\frac{1}{3}$$
$$\frac{6}{5-a_n}\le\frac{6}{3}\Rightarrow\frac{6}{5-a_n}\le 2\Rightarrow a_{n+1}\le 2$$
קיבלנו: $\forall n\in\mathbb{N}\ \ a_n\le 2$.
נוכיח שסדרה עולה מונוטונית: צריך לבדוק שאי-השוויון $a_{n+1}\ge a_n$ אמת לכל $n$ טבעי. לפי הגדרה רקורסיבית $a_{n+1}=\frac{6}{5-a_n}$, לכן יש לבדוק אי-השוויון:
$$\frac{6}{5-a_n}\ge a_n$$
אי-השוויון זה שקול לאי-השוויון הבא:
$$a_n^2-5a_n+6\ge 0\quad(*)$$
פתרון של אי-השוויון $x^2-5x+6\ge 0,\ x\in\mathbb{R}$ (פרבולה מחייכת, וחותכת ציר ה-$X$ בנקודות $x_1=2,\ x_2=3$): $x\in(-\infty,2]\cup[3,\infty)$.
קודם הוכחנו ש-$a_n\le 2$ לכן אי-השוויון $(*)$ אמת.
הוכחנו שסדרה חסומה מלמעלה ועולה מונוטונית לכן לפי משפט ויירשטראס קיים גבול $\lim_{n\to\infty}a_n=L$. לפי תכונות גבולות:
$$\lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}\frac{6}{5-a_n},\qquad L=\frac{6}{5-L}$$
$$L^2-5L+6=0,\quad L_1=2,\quad L_2=3$$
ברור ש-$L_2=3$ לא מתאים, לכן:
$$\lim_{n\to\infty}a_n=2$$
"""

SOL3A = r"""
$$\lim_{x\to0}(1-\tan x)^{\frac{1}{\sin 2x}}=\lim_{x\to0}(1-\tan x)^{-\frac{1}{\tan x}\cdot\frac{(-\tan x)}{\sin 2x}}=e^{\lim_{x\to0}\frac{-\sin x}{2\sin x\cos x\cos x}}=e^{-\frac{1}{2}}=\frac{1}{\sqrt{e}}$$
"""

SOL3B = r"""
$$\int\frac{\sin 2x}{3+\cos^2 2x}dx=\{t=\cos 2x,\ dt=-2\sin 2x\,dx\}=-\frac{1}{2}\int\frac{dt}{3+t^2}=$$
$$=-\frac{1}{2\sqrt{3}}\arctan\frac{t}{\sqrt{3}}+c=-\frac{1}{2\sqrt{3}}\arctan\frac{\cos 2x}{\sqrt{3}}+c$$
"""

SOL4A = r"""
$$y=x^{2/3}e^{-x}\ \Rightarrow\ y'=\frac{2}{3}\cdot\frac{e^{-x}}{\sqrt[3]{x}}-x^{2/3}e^{-x}=e^{-x}\cdot\frac{2-3x}{3\sqrt[3]{x}},\qquad y'=0\ \Rightarrow\ x=\frac{2}{3}$$
הנגזרת לא מוגדרת בנקודה $x=0$. לכן הנקודות החשודות הפנימיות הן $x=0$, $x=\frac{2}{3}$.

| $x$ | $-3$ | $0$ | $2/3$ | $1$ |
|---|---|---|---|---|
| $y$ | $41.8$ | $0$ | $0.39$ | $0.37$ |

$$y_{min}=y(0)=0$$
$$y_{max}=y(-3)=41.8$$
"""

SOL4B = r"""
![שרטוט רשמי של התחום](images/exams/24A-A-Q4b-sketch.png)
$$V=\pi\int_0^1 y^2\,dx=\pi\int_0^1\arctan x\,dx=\left|\begin{matrix}u=\arctan x & du=\frac{dx}{1+x^2}\\ dv=dx & v=x\end{matrix}\right|=$$
$$=\pi x\arctan x\Big|_0^1-\pi\int_0^1\frac{x\,dx}{1+x^2}=\frac{\pi^2}{4}-\frac{\pi}{2}\int_0^1\frac{2x\,dx}{1+x^2}=\frac{\pi^2}{4}-\frac{\pi}{2}\int_0^1\frac{d(1+x^2)}{1+x^2}=$$
$$=\frac{\pi^2}{4}-\frac{\pi}{2}\ln(1+x^2)\Big|_0^1=\frac{\pi^2}{4}-\frac{\pi}{2}\ln 2$$
"""

SOL5A = r"""
$$\lim_{x\to0^+}\frac{\int_0^{\sqrt{x}}\sin(t^2)\,dt}{x^{\frac{3}{2}}}=\left\{\frac{0}{0}\right\}=\lim_{x\to0^+}\frac{\sin x\cdot\frac{1}{2\sqrt{x}}}{\frac{3}{2}x^{\frac{1}{2}}}=\lim_{x\to0^+}\frac{\sin x}{3x}=\frac{1}{3}$$
"""

SOL5B = r"""
$$\lim_{x\to0^-}x^{-2}(e^{ax}-1)^2=\lim_{x\to0^-}\frac{(e^{ax}-1)^2}{x^2}=\lim_{x\to0^-}\left(\frac{e^{ax}-1}{x}\right)^2=\left(\lim_{x\to0^-}\frac{e^{ax}-1}{x}\right)^2=\left(\lim_{x\to0^-}\frac{ae^{ax}}{1}\right)^2=a^2$$
$$\lim_{x\to0^+}\left(4+e^{-\frac{a^2}{x}}\right)=\begin{cases}5, & a=0\\ 4, & a\neq0\end{cases}$$
$$a^2=b=4$$
תשובה: $b=4,\quad a=\pm2$
"""

SOL6A = r"""
הפונקציה $f(x)=\tan x$ מקיימת את כל התנאים של משפט לגרנז' בתחום $0<x<\frac{\pi}{2}$.
לכן קיימת נקודה $c$ בקטע $(0,x)$, שבה מתקיים:
$$f'(c)=\frac{\tan x-\tan 0}{x-0}\ \Rightarrow\ \frac{1}{\cos^2 c}=\frac{\tan x}{x}.$$
לכן $\cos^2 c<1$ ואז $\frac{1}{\cos^2 c}>1$. מכאן נובע $\frac{\tan x}{x}>1$, כלומר $\tan x>x$.
"""

SOL6B = r"""
נמצא את משוואת הישר המשיק העובר דרך הנקודה $x=3$: $y(3)=1,\ y'=\frac{1}{\sqrt{2x-5}},\ y'(3)=1$, נקבל ישר המשיק: $y-1=1(x-3)\Rightarrow y=x-2$.
חישוב השטח:
$$s=s_1+s_2=\int_2^{5/2}(x-2)\,dx+\int_{5/2}^{3}\left(x-2-\sqrt{2x-5}\right)dx=$$
$$=\frac{(x-2)^2}{2}\Big|_2^3-\frac{(2x-5)^{3/2}}{3}\Big|_{5/2}^3=\frac{1}{6}$$

![הציור הרשמי](images/exams/24A-A-Q6b-fig.png)
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=\frac{e^x}{x^2}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, תחומי עליה וירידה, "
      "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20, confidence="low",
      hold="official-solution-disagrees: part ג claims y''<0 for x<0 but y''=e^x(x^2-4x+6)/x^4>0 for all x!=0 (sympy)"),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{x^2\,dx}{(x+2)(x^2+1)}$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "sequences_limits",
      "נתונה הסדרה: " r"$a_1=1,\ a_{n+1}=\frac{6}{5-a_n}$." "\nהוכיחו כי הסדרה מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0}(1-\tan x)^{\frac{1}{\sin 2x}}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\sin 2x\,dx}{3+\cos^2 2x}$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "extrema_optimization",
      r"מצאו את ערך מקסימלי ואת הערך מינימלי של הפונקציה $y=x^{2/3}e^{-x}$ בקטע סגור $[-3,1]$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר מסיבוב של התחום המישורי הכלוא בין הקווים: $y=\sqrt{\arctan(x)},\ y=0,\ x=0,\ x=1$ סביב ציר ה-$X$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "lhopital_taylor",
      r"חשבו את הגבול הבא: $\lim_{x\to0^+}\frac{\int_0^{\sqrt{x}}\sin(t^2)\,dt}{x^{\frac{3}{2}}}$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "continuity",
      r"נתונה הפונקציה: $f(x)=\begin{cases}x^{-2}\left(e^{ax}-1\right)^2 & x<0\\ b & x=0\\ 4+e^{-a^2/x} & x>0\end{cases}$"
      "\n" r"מצאו לאלו ערכים של פרמטרים $a$ ו-$b$, פונקציה $f(x)$ תהיה רציפה בנקודה $x=0$?",
      SOL5B, part="ב", points=10),

    Q(6, "proof", "mean_value_theorems",
      r"הוכיחו שמתקיים $\tan x>x$ עבור $0<x<\frac{\pi}{2}$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "definite_integrals",
      r"מצאו את השטח הכלוא בין ציר ה-$X$, גרף של הפונקציה $y=\sqrt{2x-5}$ והמשיק שלו בנקודה $x=3$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "24A-A",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ד, מועד א'",
    "year": 2024,
    "examDate": "19/03/2024",
    "sourceFile": "calculus-1/24A-A exam+solution.pdf",
    "solutionFile": "calculus-1/24A-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

# -*- coding: utf-8 -*-
"""Generator for tools/raw/24B-A.json -- calculus-1 (20151), semester A 2024, moed B (03/04/2024).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24B-A.py

Source: sitting 24B-A, pp.1-7 (exam with the official solution after each question; Q1, Q3, Q4a, Q5a are
handwritten, the rest typed). Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Q1 is one item (single instruction list); the handwritten sketch is shipped as images/exams/24B-A-Q1-sketch.png.
- Q1: the handwritten convexity table only shows the sign of f'' (negative on both sides, no inflection); the words
  'convex (downward)' and the endpoint-free summary are the transcriber's reading of that table.
- Q1 solution: the official page writes f''' = -6/x^4 where f'' is meant; transcribed as f''.
- Q3 is split into four items (printed roman numerals i-iv, stored as parts א-ד); the official solution computes both one-sided limits once, so the
  shared computation is repeated in each part.
- Q3: the middle limit of the left-sided computation is printed with x->0+ in the official page; written as 0^- here.
- Q5b: the official page prints "x_2=-1, x_2=3" (second index is a typo for x_1,x_2); transcribed as x_1,x_2.
- Q6b: the official page writes f'(x) where y'(x) is meant; transcribed as y'.

Checks (tools/verify/24B-A/check.py, sympy): every derivative, limit, integral, area and extremum value matches
the official answers. 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24B-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**תחום הגדרה:** $x\neq 0$.
**נקודות חיתוך עם הצירים:** חיתוך עם ציר ה-$x$: $x=1$, כי $\frac{x^3-1}{x^2}=0$, כלומר הנקודה $(1,0)$. אין חיתוך עם ציר ה-$y$.
**נגזרת:** $f(x)=\frac{x^3-1}{x^2}=\frac{x^3}{x^2}-\frac{1}{x^2}=x-\frac{1}{x^2}$, ו-$f'(x)=1+\frac{2}{x^3}=0\Rightarrow x=-\sqrt[3]{2}$. $f''(x)=-\frac{6}{x^4}=0\Rightarrow\emptyset$.
**תחומי עליה וירידה:** $f'>0$ כאשר $x<-\sqrt[3]{2}$ או $x>0$ (הפונקציה עולה); $f'<0$ כאשר $-\sqrt[3]{2}<x<0$ (הפונקציה יורדת).
**קיצון:** $\left(-\sqrt[3]{2},\,\frac{-3}{\sqrt[3]{4}}\right)$ (נקודת מקסימום מקומי).
**תחומי קמירות וקעירות, נקודות פיתול:** $f''<0$ משני צדי $x=0$ (אין שינוי סימן ב-$f''$), לכן הפונקציה קמורה (כלפי מטה) בכל תחום ההגדרה ואין נקודות פיתול.
**אסימפטוטות אנכיות:** $x=0$. מתקיים $\lim_{x\to0^+}\frac{x^3-1}{x^2}=-\infty$ וגם $\lim_{x\to0^-}\frac{x^3-1}{x^2}=-\infty$, ולכן $x=0$ היא אסימפטוטה אנכית.
**אסימפטוטות משופעות, ב-$\infty$:**
$$a=\lim_{x\to\infty}\frac{f(x)}{x}=\lim_{x\to\infty}\frac{x^3-1}{x^2}\cdot\frac{1}{x}=\lim_{x\to\infty}\frac{x^3-1}{x^3}=1$$
$$b=\lim_{x\to\infty}\left(f(x)-ax\right)=\lim_{x\to\infty}\left(\frac{x^3-1}{x^2}-1\cdot x\right)=\lim_{x\to\infty}\frac{-1}{x^2}=0$$
אסימפטוטה משופעת ב-$\infty$: $y=1x+0$. באופן דומה ב-$-\infty$: $y=x$.
**שרטוט:**
![שרטוט הגרף של הפונקציה עם האסימפטוטות x=0 ו-y=x](images/exams/24B-A-Q1-sketch.png)
"""

SOL2A = r"""
$$\int\frac{x}{(x+1)(x^2+1)}dx\overset{(*)}{=}\frac{1}{2}\int\left(\frac{-1}{x+1}+\frac{x+1}{x^2+1}\right)dx=-\frac{1}{2}\ln|x+1|+\frac{1}{4}\int\frac{2x+2}{x^2+1}dx$$
$$=-\frac{1}{2}\ln|x+1|+\frac{1}{4}\ln|x^2+1|+\frac{1}{4}\cdot 2\cdot\arctan x+c$$
"""

SOL2B = r"""
נרצה להוכיח ש-$\ln(1+x)<x$. כעת נגדיר את פונקציית העזר $f(x)=x-\ln(1+x)$ ונוכיח כי $f(x)>0$ לכל $x>0$.
אכן, $f(0)=0$, $f$ גזירה לכל $x>0$ והנגזרת היא $f'(x)=1-\frac{1}{1+x}=\frac{x}{1+x}>0$.
אזי $f'(x)>0$ לכל $x>0$, ולכן $f$ עולה בקטע $[0,\infty)$, כלומר, $f(x)>f(0)=0$ לכל $x>0$.
"""

CTX3 = r"""נתונה פונקציה:
$$f(x)=\begin{cases}\frac{\sin bx}{x+\sin 2x}, & x<0\\ 2a-7, & x=0\\ x\ln x, & x>0\end{cases}$$
מצאו (אם קיימים) את כל הערכים של הפרמטרים $a,b$ ממשיים עבורם:
אם לא קיימים ערכים כנדרש, רשום "לא קיימים" והסבר מדוע."""

SOL3_COMMON = r"""נחשב את הגבולות החד-צדדיים בנקודה $x=0$:
$$\lim_{x\to0^-}f(x)=\lim_{x\to0^-}\frac{\sin bx}{x+\sin 2x}=\lim_{x\to0^-}\frac{\frac{\sin bx}{x}}{1+\frac{\sin 2x}{x}}=\frac{b}{3}$$
(כאשר $\frac{\sin bx}{x}\to b$ ו-$\frac{\sin 2x}{x}\to 2$.)
$$f(0)=2a-7$$
$$\lim_{x\to0^+}x\ln x\ \text{``}0\cdot\infty\text{''}=\lim_{x\to0^+}\frac{\ln x}{\frac{1}{x}}\ \overset{\text{L'H}}{=}\ \lim_{x\to0^+}\frac{\frac{1}{x}}{-\frac{1}{x^2}}=\lim_{x\to0^+}(-x)=0$$
"""

SOL3I = SOL3_COMMON + r"""
$f$ רציפה ב-$0$ אם הגבול בנקודה קיים ושווה לערך הפונקציה בנקודה:
$$2a-7=\frac{b}{3}=0\ \longrightarrow\ b=0,\ a=\frac{7}{2}=3.5$$
"""

SOL3II = SOL3_COMMON + r"""
אי רציפות סליקה: הגבול קיים אך שונה מערך הפונקציה בנקודה:
$$\lim_{x\to0^+}f(x)=\lim_{x\to0^-}f(x)\neq f(0)$$
$$0=\frac{b}{3}\neq 2a-7$$
$$b=0,\quad a\neq\frac{7}{2}$$
"""

SOL3III = SOL3_COMMON + r"""
אי רציפות ממין 1: הגבולות החד-צדדיים קיימים אך שונים:
$$\lim_{x\to0^+}f(x)\neq\lim_{x\to0^-}f(x)$$
$$0\neq\frac{b}{3}\ \to\ b\neq0,\quad a\in\mathbb{R}$$
"""

SOL3IV = SOL3_COMMON + r"""
עבור כל ערך של $a$ ו-$b$ הגבולות החד-צדדיים קיימים. לכן אין ערכים של $a$ ו-$b$ עבורם נקבל אי רציפות ממין II.
"""

SOL4A = r"""
$$\lim_{x\to1}\left(\frac{1}{\ln x}-\frac{1}{x-1}\right)=\lim_{x\to1}\frac{x-1-\ln x}{\ln x\cdot(x-1)}\quad\left\{\text{``}\tfrac{0}{0}\text{''}\right\}\ \overset{\text{L'H}}{=}$$
$$=\lim_{x\to1}\frac{1-\frac{1}{x}}{\frac{1}{x}(x-1)+\ln x}=\lim_{x\to1}\frac{x-1}{x-1+x\ln x}\quad\left\{\text{``}\tfrac{0}{0}\text{''}\right\}\ \overset{\text{L'H}}{=}$$
$$=\lim_{x\to1}\frac{1}{1+\ln x+x\cdot\frac{1}{x}}=\frac{1}{2}.$$
"""

SOL4B = r"""
$$\lim_{x\to0}\frac{\int_0^x\tan t\,dt}{x\sin x}\overset{(*)}{=}\lim_{x\to0}\frac{\tan x}{\sin x+x\cos x}\overset{(**)}{=}\lim_{x\to0}\frac{\frac{\tan x}{x}}{\frac{\sin x}{x}+\cos x}=\frac{1}{2}$$
"""

SOL5A = r"""
אינטגרציה בחלקים עם $u=x^2+2x,\ v'=\cos 2x,\ u'=2x+2,\ v=\frac{\sin 2x}{2}$:
$$\int(x^2+2x)\cos 2x\,dx=(x^2+2x)\cdot\frac{\sin 2x}{2}-\int\frac{(2x+2)\sin 2x}{2}\,dx$$
באינטגרל הנותר, אינטגרציה בחלקים נוספת עם $u=x+1,\ v'=\sin 2x,\ u'=1,\ v=-\frac{\cos 2x}{2}$:
$$=\frac{x^2+2x}{2}\sin 2x+\frac{(x+1)\cos 2x}{2}-\int\frac{\cos 2x}{2}\,dx=\frac{x^2+2x-0.5}{2}\sin 2x+\frac{(x+1)\cos 2x}{2}+c$$
"""

SOL5B = r"""
$$x^2+2=2x+5,\quad x^2-2x-3=0,\quad x_1=-1,\ x_2=3$$
$$S=\int_0^3\left(2x+5-(x^2+2)\right)dx+\int_3^6\left(x^2+2-(2x+5)\right)dx=$$
$$=\left(3x+x^2-\frac{x^3}{3}\right)\Big|_0^3+\left(-3x-x^2+\frac{x^3}{3}\right)\Big|_3^6=36$$
"""

SOL6A = r"""
נגדיר פונקציה $g(x)=e^x-\frac{1}{x}-3$ ו-$x\in(1,1.5)$: $g$ גזירה לכל $x\in(1,1.5)$ ו-$g'(x)=e^x+\frac{1}{x^2}>0$.
הנגזרת תמיד חיובית ולכן הפונקציה מונוטונית עולה.
$$g(1)=e-4<0,\qquad g(1.5)=e^{1.5}-\frac{2}{3}-3>0$$
לכן: למשוואה $e^x-\frac{1}{x}-3=0$ יש פתרון יחיד $c$ בקטע $(1,1.5)$.
"""

SOL6B = r"""
$$x^2+4x-5=0,\ x=-5,\ x=1,\qquad y'(x)=\frac{x^2+4x-5}{(x+2)^2},\qquad D(y)=(-\infty,-2)\cup(-2,+\infty)$$
$$y(10)=\frac{105}{12},\quad y(0)=\frac{5}{2},\quad y(1)=2$$
$$y_{max}=y(10)=\frac{105}{12},\qquad y_{min}=y(1)=2$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה: $f(x)=\frac{x^3-1}{x^2}$ על פי הסעיפים הבאים: תחום הגדרה, חיתוך עם הצירים, תחומי עליה וירידה, "
      "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{x}{(x+1)(x^2+1)}\,dx$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "mean_value_theorems",
      r"הוכיחו $\ln(1+x)<x$ לכל $x>0$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "continuity", r"$f(x)$ תהיה רציפה ב-$x=0$.",
      SOL3I, part="א", points=5, contextId="c3"),
    Q(3, "computation", "continuity", r"$x=0$ תהיה נק' אי-רציפות סליקה.",
      SOL3II, part="ב", points=5, contextId="c3"),
    Q(3, "computation", "continuity", r"$x=0$ תהיה נק' אי-רציפות מסוג ראשון של $f(x)$.",
      SOL3III, part="ג", points=5, contextId="c3"),
    Q(3, "computation", "continuity", r"$x=0$ תהיה נק' אי-רציפות מסוג שני של $f(x)$.",
      SOL3IV, part="ד", points=5, contextId="c3"),

    Q(4, "computation", "lhopital_taylor",
      r"חשבו את הגבול: $\lim_{x\to1}\left(\frac{1}{\ln x}-\frac{1}{x-1}\right)$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "lhopital_taylor",
      r"חשבו את הגבול: $\lim_{x\to0}\frac{\int_0^x\tan t\,dt}{x\sin x}$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int(x^2+2x)\cos 2x\,dx$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "definite_integrals",
      r"מצאו את השטח החסום בין הקווים: $y=x^2+2,\ y=2x+5,\ x=0,\ x=6$.",
      SOL5B, part="ב", points=10),

    Q(6, "proof", "continuity",
      r"הוכיחו כי למשוואה $e^x-\frac{1}{x}-3=0$ יש פתרון יחיד בקטע $(1,1.5)$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "extrema_optimization",
      r"מצאו את המינימום והמקסימום המוחלטים של $y=\frac{x^2+5}{x+2}$ בקטע $[0,10]$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "24B-A",
    "examLabel": "מבחן סוף סמסטר א' תשפ\"ד, מועד ב'",
    "year": 2024,
    "examDate": "03/04/2024",
    "sourceFile": "calculus-1/24B-A exam+solution.pdf",
    "solutionFile": "calculus-1/24B-A exam+solution.pdf",
    "contexts": {"c3": {"kind": "text", "title": "שאלה 3", "text": CTX3}},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

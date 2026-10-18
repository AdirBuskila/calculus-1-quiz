# -*- coding: utf-8 -*-
"""Generator for tools/raw/17A1-A.json -- calculus-1 (20151), semester A 2017, moed A version 1 (06/02/2017).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_17A1-A.py

Source: sitting 17A1-A, pp.1-9 (typed exam with the official worked solution after every question).
Part A (mandatory): Q1 (20%). Part B: choose 4 of Q2-Q6 (each Q2-Q6 split into parts a/b, 10% each).

Transcription notes
- Q1/Q3b/Q4b/Q5a: plots printed in the official solution are cropped as figures inside the solutions.
  The sketched sign diagrams (arrows / arcs) in Q1 are transcribed as sentences.
- Q3a (p.5): the middle line of the official solution reads (cos x - 1)/(1+sin x); the correct expression is
  (1/cos x - 1)/(1+sin x) (the limit 0 and the answer 1 are unchanged). Corrected silently, logged in ASK_ADIR.
- Q5a (p.7): the official text gives f(-2) = cbrt(36); it is cbrt(4) (the printed plot shows ~1.59). The
  max/min conclusion is unchanged. Corrected silently, logged in ASK_ADIR.

Checks: tools/verify/17A1-A/check.py (sympy), 0 mismatches with the official answers. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "17A1-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**1. תחום ההגדרה:** $x>0$. נקודות חיתוך עם הצירים: $(1,0)$.
**2. תחומי עלייה וירידה, נקודות קיצון:**
$$y'=2x\ln x+x=x(2\ln x+1)=0\ \Rightarrow\ x=\frac{1}{\sqrt e}$$
טבלת סימנים של $y'$: שלילית ב-$0<x<\frac1{\sqrt e}$ (יורדת), חיובית ב-$x>\frac1{\sqrt e}$ (עולה). $x=\frac1{\sqrt e}$ נקודת מינימום, מתקיים $y\left(\frac1{\sqrt e}\right)=-\frac1{2e}$.
**3. תחומי קמירות וקעירות, נקודות פיתול:**
$$y''=2\ln x+3=0\ \Rightarrow\ x=\frac{1}{\sqrt{e^3}}$$
טבלת סימנים של $y''$: שלילית ב-$0<x<\frac1{\sqrt{e^3}}$ (קעורה), חיובית ב-$x>\frac1{\sqrt{e^3}}$ (קמורה). $x=\frac1{\sqrt{e^3}}$ נקודת פיתול, מתקיים $y\left(\frac1{\sqrt{e^3}}\right)=-\frac{3}{2e^3}$.
**4. אסימפטוטות אנכיות:** ישנה נקודה אחת בלבד החשודה לאסימפטוטה, קצה תחום ההגדרה $x=0$. נחשב את הגבול של הפונקציה בנקודה זו:
$$\lim_{x\to0^+}x^2\ln x=\lim_{x\to0^+}\frac{\ln x}{\frac1{x^2}}=\lim_{x\to0^+}\frac{\frac1x}{-\frac2{x^3}}=\lim_{x\to0^+}\frac{x^2}{-2}=0$$
$x=0$ אינה אסימפטוטה אנכית.
**אסימפטוטות משופעות:** ניתן לחפש ב-$+\infty$ בלבד. נזכיר כי אם לפונקציה $f(x)$ קיימת אסימפטוטה משופעת $y=ax+b$ אז בהכרח $a=\lim_{x\to\infty}\frac{f(x)}{x}$. נקבל עבור הפונקציה הנתונה: $a=\lim_{x\to+\infty}\frac{x^2\ln x}{x}=\lim_{x\to+\infty}x\ln x=+\infty$. כלומר אין לה אסימפטוטה משופעת.
**5. שרטוט:**
![שרטוט הגרף של y = x² ln x בקטע מ-0 עד 3, עם מינימום קטן ליד x = 0.6](images/exams/17A1-A-Q1-graph.png)
"""

SOL2A = r"""
מצד אחד
$$2=\sqrt[n]{2^n}\le\sqrt[n]{n^2+2^n}$$
מצד שני, עבור $n$ מספיק גדול
$$\sqrt[n]{n^2+2^n}\le\sqrt[n]{2^n+2^n}=\sqrt[n]{2\cdot2^n}=2\sqrt[n]2$$
כלומר $2\le\sqrt[n]{n^2+2^n}\le2\sqrt[n]2$. לכן לפי משפט הסנדוויץ' $\lim_{n\to\infty}\sqrt[n]{n^2+2^n}=2$.
"""

SOL2B = r"""
נשתמש באינטגרציה בחלקים:
$$\int(x^2-4x)\ln(x)\,dx=\left[\begin{matrix}u=\ln x&dv=\left(x^2-4x\right)dx\\du=\frac1x\,dx&v=\frac{x^3}{3}-2x^2\end{matrix}\right]=$$
$$=\left(\frac{x^3}{3}-2x^2\right)\ln x-\int\left(\frac{x^3}{3}-2x^2\right)\frac1x\,dx=\left(\frac{x^3}{3}-2x^2\right)\ln x-\int\left(\frac{x^2}{3}-2x\right)dx=$$
$$=\left(\frac{x^3}{3}-2x^2\right)\ln x-\frac{x^3}{9}+x^2+c$$
"""

SOL3A = r"""
$$\lim_{x\to0}\left(\frac{1+\tan x}{1+\sin x}\right)^{\frac1{\sin x}}=\lim_{x\to0}\left(1+\frac{1+\tan x}{1+\sin x}-1\right)^{\frac1{\sin x}}=\lim_{x\to0}\left(1+\frac{\tan x-\sin x}{1+\sin x}\right)^{\frac1{\sin x}}=$$
$$=\lim_{x\to0}\left(1+\frac{\tan x-\sin x}{1+\sin x}\right)^{\frac{1+\sin x}{\tan x-\sin x}\cdot\frac{\tan x-\sin x}{1+\sin x}\cdot\frac1{\sin x}}=e^{\lim_{x\to0}\frac{\tan x-\sin x}{1+\sin x}\cdot\frac1{\sin x}}=e^{\lim_{x\to0}\frac{\frac1{\cos x}-1}{1+\sin x}}=e^0=1$$
"""

SOL3B = r"""
התחום הינו:
![התחום הכלוא בין y = 1/x², y = x ו-y = 4, מסומן בכחול](images/exams/17A1-A-Q3b-fig.png)
הפונקציה התחתונה היא $y=\frac1{x^2}$ מ-$x=0.5$ עד $x=1$, ומ-$x=1$ עד $x=4$ היא $y=x$. לכן השטח מחושב כדלקמן:
$$S=\int_{0.5}^{1}\left(4-\frac1{x^2}\right)dx+\int_1^4(4-x)\,dx=\left(4x+\frac1x\right)\Big|_{0.5}^{1}+\left(4x-\frac{x^2}{2}\right)\Big|_1^4=5.5$$
"""

SOL4A = r"""
נגדיר את הפונקציה $f(x)=x+\sin x-1$. הפונקציה אלמנטרית ומוגדרת ב-$\mathbb R$, לכן היא רציפה ב-$\mathbb R$.
מתקיים $f(0)=-1<0$ ו-$f(3)=2+\sin3>0$. לפי משפט ערך הביניים (בולצאנו-קושי) קיימת נקודה $0<c<3$ כך ש-$f(c)=0$. כלומר למשוואה $x+\sin x=1$ קיים פתרון.
על מנת להוכיח את יחידותו של הפתרון, נסתכל בנגזרת של הפונקציה: $f'(x)=1+\cos x$. נשים לב כי $f'(x)$ אי-שלילית ב-$\mathbb R$, לכן הפונקציה $f(x)$ לא יורדת ב-$\mathbb R$ וזה מוכיח את יחידות הפתרון.
"""

SOL4B = r"""
התחום המסתובב הינו התחום הצבוע:
![התחום הצבוע בין חצי המעגל y = √(25 − x²) לבין הישר y = 3](images/exams/17A1-A-Q4b-fig.png)
נחשב את הנפח לפי שיטת הפרוסות:
$$V=\pi\int_{-4}^{4}\left(\left(\sqrt{25-x^2}\right)^2-3^2\right)dx=\pi\int_{-4}^{4}\left(16-x^2\right)dx=\pi\left(16x-\frac{x^3}{3}\right)\Big|_{-4}^{4}=\frac{256}{3}\pi$$
"""

SOL5A = r"""
בקטע הנתון הפונקציה נראית כך:
![גרף הפונקציה f(x) = (x² + x)^(2/3) בקטע מ-−2 עד 3, עם שתי נקודות חוד ב-x = −1 וב-x = 0](images/exams/17A1-A-Q5a-graph.png)
הפונקציה רציפה על הישר הממשי. נגזור אותה. הנגזרת אינה קיימת ב-$x=0$ וב-$x=-1$. לכן הנקודות הקריטיות הן: $x=-0.5$, $x=0$ ו-$x=-1$.
הערך הגדול ביותר והערך הקטן ביותר של הפונקציה בקטע סגור $[-2,3]$ מתקבלים בנקודות קריטיות או בקצוות הקטע:
$$f(-2)=\sqrt[3]{4},\quad f(3)=\sqrt[3]{144},\quad f(0)=f(-1)=0$$
הערך הגדול ביותר הוא $\sqrt[3]{144}$ והערך הקטן ביותר הוא $0$.
"""

SOL5B = r"""
$$\int\frac{\sqrt{3+\sqrt x}}{\sqrt x}\,dx=\left[\begin{matrix}t=\sqrt x\\dt=\frac1{2\sqrt x}\,dx\end{matrix}\right]=2\int\sqrt{3+t}\,dt=2\frac{(3+t)^{1.5}}{1.5}=\frac43\left(3+\sqrt x\right)^{1.5}+c$$
"""

SOL6A = r"""
בקטע הנתון ישנן 2 נקודות החשודות לאי-רציפות: $x=0$ ו-$x=0.5$. נחקור את שתי הנקודות:
**ב-$x=0$:**
$$\lim_{x\to0}f(x)=\lim_{x\to0}\left(\frac{\tan x}{x}+\frac{2x^2-5x+2}{|2x-1|}\right)=1+2=3$$
לכן $x=0$ היא נקודת אי-רציפות סליקה.
**נעבור ל-$x=0.5$:**
$$\lim_{x\to0.5^+}f(x)=\lim_{x\to0.5^+}\left(\frac{\tan x}{x}+\frac{2x^2-5x+2}{|2x-1|}\right)=\lim_{x\to0.5^+}\left(\frac{\tan x}{x}+\frac{(2x-1)(x-2)}{|2x-1|}\right)=\lim_{x\to0.5^+}\left(\frac{\tan x}{x}+\frac{(2x-1)(x-2)}{2x-1}\right)=2\tan0.5-1.5$$
מצד שני:
$$\lim_{x\to0.5^-}f(x)=\lim_{x\to0.5^-}\left(\frac{\tan x}{x}+\frac{(2x-1)(x-2)}{|2x-1|}\right)=\lim_{x\to0.5^-}\left(\frac{\tan x}{x}+\frac{(2x-1)(x-2)}{-(2x-1)}\right)=2\tan0.5+1.5$$
מכאן רואים ש-$x=0.5$ היא נקודת אי-רציפות מסוג ראשון (קפיצה).
"""

SOL6B = r"""
נחשב את הגבול בעזרת הכפלה בצמוד:
$$\lim_{x\to-\infty}\left(\sqrt{x^2+ax}-\sqrt{x^2+2x}\right)=\lim_{x\to-\infty}\frac{x^2+ax-x^2-2x}{\sqrt{x^2+ax}+\sqrt{x^2+2x}}=\lim_{x\to-\infty}\frac{(a-2)x}{\sqrt{x^2+ax}+\sqrt{x^2+2x}}=$$
$$=\lim_{x\to-\infty}\frac{(a-2)x}{\sqrt{x^2\left(1+\frac ax\right)}+\sqrt{x^2\left(1+\frac2x\right)}}=\lim_{x\to-\infty}\frac{(a-2)x}{|x|\sqrt{1+\frac ax}+|x|\sqrt{1+\frac2x}}$$
עבור $x<0$:
$$\lim_{x\to-\infty}\frac{(a-2)x}{-x\left(\sqrt{1+\frac ax}+\sqrt{1+\frac2x}\right)}=\frac{2-a}{2}$$
נדרוש $\frac{2-a}{2}=2$ ונקבל $a=-2$.
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה הבאה $y=x^2\cdot\ln x$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, "
      "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.", SOL1),

    Q(2, "computation", "sequences_limits",
      r"חשבו את הגבול: $\lim_{n\to\infty}\sqrt[n]{n^2+2^n}$.", SOL2A, part="א", points=10),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int(x^2-4x)\ln(x)\,dx$.", SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to0}\left(\frac{1+\tan x}{1+\sin x}\right)^{\frac1{\sin x}}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "definite_integrals",
      r"חשבו את שטח התחום הכלוא בין הקווים: $y=\frac1{x^2},\ y=x,\ y=4$.", SOL3B, part="ב", points=10),

    Q(4, "proof", "continuity",
      r"הראו כי למשוואה $x+\sin x=1$ קיים שורש ממשי אחד בלבד.", SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום הכלוא בין חצי המעגל $y=\sqrt{25-x^2}$ לבין הישר "
      r"$y=3$ סביב ציר ה-$x$.", SOL4B, part="ב", points=10),

    Q(5, "computation", "extrema_optimization",
      r"מצאו מינימום ומקסימום מוחלטים של הפונקציה $f(x)=\left(x^2+x\right)^{\frac23}$ בקטע $[-2,3]$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int\frac{\sqrt{3+\sqrt x}}{\sqrt x}\,dx$.", SOL5B, part="ב", points=10),

    Q(6, "computation", "continuity",
      r"מיינו את כל נקודות אי-הרציפות של הפונקציה $f(x)=\frac{\tan x}{x}+\frac{2x^2-5x+2}{|2x-1|}$ "
      r"בתחום $[-1,1]$.", SOL6A, part="א", points=10),

    Q(6, "computation", "function_limits",
      r"עבור איזה ערך של $a$ מתקיים: $\lim_{x\to-\infty}\left(\sqrt{x^2+ax}-\sqrt{x^2+2x}\right)=2$?",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "17A1-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ז, מועד א', גרסה 1",
    "year": 2017,
    "examDate": "06/02/2017",
    "sourceFile": "calculus-1/17A1-A exam+solution.pdf",
    "solutionFile": "calculus-1/17A1-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

# -*- coding: utf-8 -*-
"""Generator for tools/raw/18A2-A.json -- calculus-1 (20151), semester A 2018, moed A version 2 (30/01/2018).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_18A2-A.py

Source: sitting 18A2-A, pp.1-9 (typed exam with the official worked solution after every question).
Part A (mandatory): Q1 (20%). Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Q1: the official text calls x=e^2 a minimum, but y' changes from + to - there, so it is a MAXIMUM; it also prints the
  inflection point as x=e^(2/3) where 3 ln x - 8 = 0 gives x=e^(8/3) (the printed sign diagram says e^(8/3)).
  Final-answer errors: shipped corrected with the "הפתרון הרשמי עם תיקון" label, solutionSource solved, official:false.
- Q1/Q3b/Q4b/Q6a: the plots printed in the official solution are cropped as figures inside the solutions.
- Q4b: both printed plots (x-axis view and the rotated view) are shipped.
- Q4a "another way" paragraph transcribed in full.

Checks: tools/verify/18A2-A/check.py (sympy), 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "18A2-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
הפתרון הרשמי עם תיקון: בפתרון הרשמי נכתב ש-$x=e^2$ היא נקודת מינימום, אבל $y'$ חיובית משמאלה ושלילית מימינה, ולכן זו נקודת מקסימום. כמו כן נכתב שנקודת הפיתול היא $x=e^{\frac23}$, אך $3\ln x-8=0$ נותן $x=e^{\frac83}$ (וכך גם בטבלת הסימנים הרשמית). התיקונים נבדקו (sympy).
**1. תחום ההגדרה:** $x>0$.
**2. תחומי עלייה וירידה, נקודות קיצון:**
$$y'=\frac{2-\ln x}{2x^{1.5}}=0\ \Rightarrow\ x=e^2$$
טבלת סימנים של $y'$: חיובית ב-$0<x<e^2$ (עולה), שלילית ב-$x>e^2$ (יורדת). נקודת מקסימום מקומי: $x=e^2$, $y\left(e^2\right)=\frac2e$.
**3. תחומי קמירות וקעירות, נקודות פיתול:**
$$y''=\frac{3\ln x-8}{4x^{2.5}}=0\ \Rightarrow\ x=e^{\frac83}$$
טבלת סימנים של $y''$: שלילית ב-$0<x<e^{\frac83}$ (קעורה, $\\cap$), חיובית ב-$x>e^{\frac83}$ (קמורה, $\\cup$). $x=e^{\frac83}$ היא נקודת פיתול.
**4. אסימפטוטות:**
**אסימפטוטה אנכית:** $x=0$ חשודה לאסימפטוטה אנכית. מתקיים $\lim_{x\to0^+}\frac{\ln x}{\sqrt x}=-\infty$, לכן $x=0$ באמת אסימפטוטה אנכית.
**אסימפטוטה משופעת (יש לבדוק רק ב-$+\infty$):**
$$a=\lim_{x\to+\infty}\frac{\frac{\ln x}{\sqrt x}}{x}=\lim_{x\to+\infty}\frac{\ln x}{x^{1.5}}=0,\qquad b=\lim_{x\to+\infty}\left(\frac{\ln x}{\sqrt x}-0\cdot x\right)=\lim_{x\to+\infty}\frac{\ln x}{\sqrt x}=0$$
כלומר $y=0$.
**5. שרטוט:**
![שרטוט הגרף של y = ln x / √x עם האסימפטוטה האנכית x=0 והאסימפטוטה האופקית y=0](images/exams/18A2-A-Q1-graph.png)
"""

SOL2A = r"""
נשתמש במשפט הסנדוויץ':
$$\sqrt[2n]{10^n}\ \le\ \sqrt[2n]{10^n+\arctan n}\ \le\ \sqrt[2n]{10^n+10^n}$$
$$\sqrt{10}\ \le\ \sqrt[2n]{10^n+\arctan n}\ \le\ 2^{\frac{1}{2n}}\sqrt{10}$$
האגף השמאלי שווה ל-$\sqrt{10}$, והאגף הימני שואף ל-$1\cdot\sqrt{10}$ (כי $2^{\frac1{2n}}\to1$). לכן
$$\lim_{n\to\infty}\sqrt[2n]{10^n+\arctan n}=\sqrt{10}$$
"""

SOL2B = r"""
$$\int_{-1}^{1}(2x+1)\sin(\pi x)\,dx=\left[\begin{matrix}u=2x+1&dv=\sin(\pi x)\,dx\\du=2\,dx&v=-\frac{\cos(\pi x)}{\pi}\end{matrix}\right]=$$
$$=-\frac{\cos(\pi x)}{\pi}(2x+1)\Big|_{-1}^{1}+\frac2\pi\int_{-1}^{1}\cos(\pi x)\,dx=\frac4\pi+\frac2\pi\cdot\frac{\sin(\pi x)}{\pi}\Big|_{-1}^{1}=\frac4\pi$$
"""

SOL3A = r"""
מתקיים:
$$\lim_{x\to2}(3-x)^{\tan\frac{\pi x}{4}}=\{1^\infty\}=\lim_{x\to2}\left(1+(2-x)\right)^{\frac{1}{2-x}\cdot(2-x)\cdot\tan\frac{\pi x}{4}}=\lim_{x\to2}\left(\left(1+(2-x)\right)^{\frac{1}{2-x}}\right)^{(2-x)\tan\frac{\pi x}{4}}$$
הביטוי בסוגריים הפנימיים שואף ל-$e$, והחזקה:
$$\lim_{x\to2}(2-x)\tan\frac{\pi x}{4}=\lim_{x\to2}\frac{2-x}{\cot\frac{\pi x}{4}}=\lim_{x\to2}\frac{-1}{-\frac{1}{\sin^2\frac{\pi x}{4}}\cdot\frac\pi4}=\frac4\pi$$
לכן הגבול הוא $e^{\frac4\pi}$.
"""

SOL3B = r"""
$$L=\int_a^b\sqrt{1+\left(f'(x)\right)^2}\,dx=\int_1^2\sqrt{1+\left(\frac{x^2}{2}-\frac{1}{2x^2}\right)^2}\,dx=\int_1^2\sqrt{\frac{x^4}{4}+\frac12+\frac{1}{4x^4}}\,dx=$$
$$=\int_1^2\sqrt{\left(\frac{x^2}{2}+\frac{1}{2x^2}\right)^2}\,dx=\int_1^2\left(\frac{x^2}{2}+\frac{1}{2x^2}\right)dx=\left(\frac{x^3}{6}-\frac{1}{2x}\right)\Big|_1^2=\left(\frac86-\frac14\right)-\left(\frac16-\frac12\right)=\frac{17}{12}$$
![גרף הפונקציה f(x) = x³/6 + 1/(2x) בקטע מ-1 עד 2](images/exams/18A2-A-Q3b-graph.png)
"""

SOL4A = r"""
קודם כל נדרש שהפונקציה תהיה רציפה:
$$\lim_{x\to0^+}\left(ax^2+bx+1\right)=1,\qquad\lim_{x\to0^-}(x+a)e^{-bx}=a$$
כלומר $a=1$, ו-
$$f(x)=\begin{cases}x^2+bx+1,&x\ge0\\(x+1)e^{-bx},&x<0\end{cases}$$
על מנת שתהיה גזירה, יש לדרוש את שוויון הנגזרות החד-צדדיות:
$$f'_+(0)=\lim_{h\to0^+}\frac{f(h)-f(0)}{h}=\lim_{h\to0^+}\frac{\left(h^2+bh+1\right)-1}{h}=b$$
$$f'_-(0)=\lim_{h\to0^-}\frac{f(h)-f(0)}{h}=\lim_{h\to0^-}\frac{(h+1)e^{-bh}-1}{h}=\lim_{h\to0^-}\frac{he^{-bh}+e^{-bh}-1}{h}=\lim_{h\to0^-}\left(e^{-bh}+\frac{e^{-bh}-1}{h}\right)=1-b$$
מכאן $b=1-b$, כלומר $b=\frac12$. תשובה סופית: $a=1,\ b=\frac12$.
**דרך נוספת** (דורשת הסבר נוסף, כי אחרת אינה מדויקת, אך עדיין מקובלת במסגרת הקורס):
מדרישת הרציפות מקבלים ש-$a=1$. מתקיים:
$$f'(x)=\begin{cases}2x^2+b,&x>0\\e^{-bx}-b(1+x)e^{-bx},&x<0\end{cases}$$
(כעקרון אנו לא יודעים האם הפונקציה גזירה ב-$0$). נחשב את הגבולות החד-צדדיים של הנגזרת:
$$\lim_{x\to0^+}f'(x)=\lim_{x\to0^+}\left(2x^2+b\right)=b,\qquad\lim_{x\to0^-}f'(x)=\lim_{x\to0^-}\left(e^{-bx}-b(1+x)e^{-bx}\right)=1-b$$
נשווה את $b=1-b$ ונסיק כי $b=\frac12$.
"""

SOL4B = r"""
![הפרבולה y² = 2x+1 והישר y = x−1, ציר ה-x אופקי](images/exams/18A2-A-Q4b-fig1.png)
במקרה זה כדאי לעבור לפונקציות ההפוכות, $x=y+1$, $x=\frac12\left(y^2-1\right)$, ואז החישוב מידי.
קודם כל נמצא את נקודות החיתוך של שני הגרפים: $y+1=\frac12\left(y^2-1\right)$, $y=-1$, $y=3$. כעת ניתן לחשב את השטח:
![אותם גרפים, כשציר ה-y אופקי](images/exams/18A2-A-Q4b-fig2.png)
$$S=\int_{-1}^{3}\left(y+1-\frac12\left(y^2-1\right)\right)dy=\int_{-1}^{3}\left(y+\frac32-\frac12y^2\right)dy=\left(\frac{y^2}{2}+\frac32y-\frac{y^3}{6}\right)\Big|_{-1}^{3}=$$
$$=\left(\frac92+\frac92-\frac92\right)-\left(\frac12-\frac32+\frac16\right)=\frac{16}{3}$$
"""

SOL5A = r"""
נחלק את שלושת האגפים של אי-השוויון ב-$x$ אשר חיובי ונקבל את אי-השוויון השקול:
$$\frac{1}{1+x}<\frac{\ln(1+x)}{x}<1$$
נסתכל בפונקציה $f(x)=\ln(1+x)$ בקטע $[0,x]$. בקטע זה הפונקציה רציפה כפונקציה אלמנטרית בתחום הגדרתה וגזירה בקטע פתוח $(0,x)$. לכן היא מקיימת בקטע הנ"ל את כל התנאים של משפט לגרנז', לפיו קיימת נקודה $0<c<x$ כך ש:
$$\frac{f(x)-f(0)}{x-0}=f'(c)$$
כלומר
$$\frac{\ln(1+x)-\ln1}{x-0}=\frac{1}{1+c}$$
ז"א $\frac{\ln(1+x)}{x}=\frac{1}{1+c}$. כיוון ש-$0<c<x$ אנו מסיקים כי $\frac{1}{1+x}<\frac{1}{1+c}<1$ ומקבלים את התוצאה הרצויה:
$$\frac{1}{1+x}<\frac{\ln(1+x)}{x}<1$$
"""

SOL5B = r"""
נפרק את השבר האמיתי $\frac{2x^2-3x+3}{x^3-2x^2+x}$ לסכום של שברים אלמנטריים:
$$\frac{2x^2-3x+3}{x^3-2x^2+x}=\frac{2x^2-3x+3}{x\left(x^2-2x+1\right)}=\frac{2x^2-3x+3}{x(x-1)^2}=\frac Ax+\frac B{x-1}+\frac C{(x-1)^2}$$
$$A=3,\quad B=-1,\quad C=2$$
מכאן
$$\int\frac{2x^2-3x+3}{x^3-2x^2+x}dx=3\int\frac{dx}{x}-\int\frac{dx}{x-1}+2\int\frac{dx}{(x-1)^2}=3\ln|x|-\ln|x-1|-\frac{2}{x-1}+c$$
"""

SOL6A = r"""
משוואת המשיק העובר דרך $(0,8)$ ייראה כך: $y=ax+8$. עלינו למצוא את $a$.
נקודת ההשקה היא נקודה משותפת של שני הגרפים $y=ax+8$ ו-$y=4-x^2$. בנוסף שיפוע המשיק $a$ חייב להיות שווה לנגזרת של $y=4-x^2$.
נקבל:
$$\begin{cases}a=-2x\\4-x^2=ax+8\end{cases}\ \Leftarrow\ 4-x^2=-2x^2+8\ \Leftarrow\ x^2=4,\quad x=-2,\ x=2$$
לכן $a=4$ או $a=-4$. סופית: ישנם שני המשיקים $y=4x+8$ ו-$y=-4x+8$.
![הפרבולה y = 4 − x² ושני המשיקים העוברים דרך הנקודה (0,8)](images/exams/18A2-A-Q6a-fig.png)
"""

SOL6B = r"""
מתקיים:
$$\int\frac{dx}{\tan x+\cot x}=\int\frac{dx}{\frac{\sin x}{\cos x}+\frac{\cos x}{\sin x}}=\int\frac{dx}{\frac{\sin^2x+\cos^2x}{\cos x\cdot\sin x}}=\int\cos x\cdot\sin x\,dx=\frac{\sin^2x}{2}+c$$
"""

HEAD1 = (r"חקרו את הפונקציה הבאה $y=\frac{\ln x}{\sqrt x}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, "
         "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.")

questions = [
    Q(1, "computation", "function_investigation", HEAD1, SOL1,
      solutionSource="solved", official=False, confidence="med"),

    Q(2, "computation", "sequences_limits",
      r"חשבו את הגבול $\lim_{n\to\infty}\sqrt[2n]{10^n+\arctan n}$.",
      SOL2A, part="א", points=10),

    Q(2, "computation", "definite_integrals",
      r"חשבו את האינטגרל $\int_{-1}^{1}(2x+1)\sin(\pi x)\,dx$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to2}(3-x)^{\tan\frac{\pi x}{4}}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "definite_integrals",
      r"חשבו את אורך הקשת של גרף הפונקציה $f(x)=\frac{x^3}{6}+\frac{1}{2x}$, כאשר $1\le x\le2$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "derivatives_tangents",
      r"נתונה הפונקציה $f(x)=\begin{cases}ax^2+bx+1,&x\ge0,\\(x+a)e^{-bx},&x<0.\end{cases}$ "
      r"מצאו את ערכי הפרמטרים $a,b\in\mathbb R$ כך ש-$f(x)$ תהיה גזירה ב-$x=0$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"מצאו את השטח הכלוא בין הקווים $y^2=2x+1,\ y=x-1$.",
      SOL4B, part="ב", points=10),

    Q(5, "proof", "mean_value_theorems",
      r"הוכיחו את אי-השוויון $\frac{x}{1+x}<\ln(1+x)<x$ לכל $x>0$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{2x^2-3x+3}{x^3-2x^2+x}\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "derivatives_tangents",
      r"מצאו את המשוואות של כל המשיקים לגרף של $y=4-x^2$ אשר עוברים דרך נקודה $(0,8)$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{dx}{\tan x+\cot x}$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "18A2-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ח, מועד א', גרסה 2",
    "year": 2018,
    "examDate": "30/01/2018",
    "sourceFile": "calculus-1/18A2-A exam+solution.pdf",
    "solutionFile": "calculus-1/18A2-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

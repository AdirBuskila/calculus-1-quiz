# -*- coding: utf-8 -*-
"""Generator for tools/raw/18B-A.json -- calculus-1 (20151), semester A 2018, moed B (05/02/2018).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_18B-A.py

Source: sitting 18B-A. Exam: 2 typed pages. Solution: 4 handwritten pages, author not stated (labelled
"student-solution", official:false, confidence med; it needs the refuter pass). The Hebrew connecting words of the
handwritten pages are only partly legible, so the prose is a reconstruction of the written mathematics and every
formula is checked (tools/verify/18B-A/check.py, sympy + numeric).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (10% per part; Q2 is one part).

Transcription notes
- Q1 sketch (handwritten p.1) is shipped as a figure inside the solution (a stray label was whited out).
- Q1: the handwritten one-sided limits at x=-sqrt(3) have the signs swapped (+oo / -oo); corrected (y is odd). Silent,
  intermediate; logged in docs/ASK_ADIR.md.
- Q3b: the handwritten words are barely legible; the solution is existence by IVT on [-pi/2, 0] (as written) plus the
  reasoning that there are infinitely many roots (written: sin x takes all values in [-1,1] while 0<e^x<1 for x<0).
  The "not unique" reading is checked numerically (>= 8 roots in [-30, 0.5]). Logged in ASK_ADIR.
- Q4b: FINAL-ANSWER ERROR in the handwritten solution (-pi/3 instead of -pi/6); shipped corrected with the
  "הפתרון הרשמי עם תיקון" label, solutionSource solved, official:false (sympy: pi^2/12 - pi/6 + (pi/6) ln 2).
- Q6b: the handwritten L'Hopital line drops the factor x (x -> 1, so harmless); the factor is restored. Silent, logged.

Checks: tools/verify/18B-A/check.py (sympy), 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "18B-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "student-solution", "official": False, "confidence": "med"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**תחום ההגדרה:** $D=(-\infty,-\sqrt3)\cup(-\sqrt3,\sqrt3)\cup(\sqrt3,\infty)$.
**חיתוך עם הצירים:** $y=0\Leftrightarrow x=0$, ולכן החיתוך היחיד הוא $(0,0)$. הפונקציה אי-זוגית: $y(-x)=-y(x)$.
**אסימפטוטות אנכיות** $x=\pm\sqrt3$:
$$\lim_{x\to\sqrt3^+}y=+\infty,\quad\lim_{x\to\sqrt3^-}y=-\infty,\qquad\lim_{x\to-\sqrt3^+}y=+\infty,\quad\lim_{x\to-\sqrt3^-}y=-\infty$$
**אסימפטוטה משופעת** $y=kx+b$ ב-$\pm\infty$:
$$k=\lim_{x\to\pm\infty}\frac{y}{x}=\lim_{x\to\pm\infty}\frac{x^2}{x^2-3}=1,\qquad b=\lim_{x\to\pm\infty}(y-kx)=\lim_{x\to\pm\infty}\left(\frac{x^3}{x^2-3}-x\right)=\lim_{x\to\pm\infty}\frac{3x}{x^2-3}=0$$
לכן $y=x$ היא אסימפטוטה משופעת (משני הצדדים).
**מונוטוניות וקיצון:**
$$y'=\frac{3x^2\left(x^2-3\right)-x^3\cdot2x}{\left(x^2-3\right)^2}=\frac{x^4-9x^2}{\left(x^2-3\right)^2}=\frac{x^2(x-3)(x+3)}{\left(x^2-3\right)^2}$$
טבלת סימנים של $y'$: חיובית ב-$x<-3$ (עולה), שלילית ב-$-3<x<-\sqrt3$, ב-$-\sqrt3<x<\sqrt3$ (גם סביב $x=0$) וב-$\sqrt3<x<3$ (יורדת), חיובית ב-$x>3$ (עולה).
מקסימום מקומי ב-$x=-3$: $y(-3)=-\frac92$. מינימום מקומי ב-$x=3$: $y(3)=\frac92$.
**קמירות ונקודות פיתול:**
$$y''=\frac{\left(4x^3-18x\right)\left(x^2-3\right)^2-\left(x^4-9x^2\right)\cdot2\left(x^2-3\right)\cdot2x}{\left(x^2-3\right)^4}=\frac{\left(4x^3-18x\right)\left(x^2-3\right)-4x\left(x^4-9x^2\right)}{\left(x^2-3\right)^3}=$$
$$=\frac{4x^5-30x^3+54x-4x^5+36x^3}{\left(x^2-3\right)^3}=\frac{6x^3+54x}{\left(x^2-3\right)^3}=\frac{6x\left(x^2+9\right)}{\left(x-\sqrt3\right)^3\left(x+\sqrt3\right)^3}$$
טבלת סימנים של $y''$: שלילית ב-$x<-\sqrt3$ (קעורה), חיובית ב-$-\sqrt3<x<0$ (קמורה), שלילית ב-$0<x<\sqrt3$ (קעורה), חיובית ב-$x>\sqrt3$ (קמורה). נקודת הפיתול היחידה: $(0,0)$.
![שרטוט הגרף של y = x³/(x²−3) עם האסימפטוטות x=±√3 ו-y=x, המקסימום ב-x=−3 והמינימום ב-x=3](images/exams/18B-A-Q1-graph.png)
"""

SOL2 = r"""
נחשב: $a_1=2,\ a_2=\frac65,\ a_3=\frac{18}{17},\dots$ ונרשום $a_{n+1}=\frac{3}{2+\frac{1}{a_n}}$.
**חסימות:** נוכיח באינדוקציה ש-$1<a_n<2$ לכל $n\ge1$. עבור $n=1$ זה נכון. אם $1<a_n<2$ אז
$$\frac12<\frac{1}{a_n}<1\ \Rightarrow\ \frac52<2+\frac{1}{a_n}<3\ \Rightarrow\ \frac13<\frac{1}{2+\frac{1}{a_n}}<\frac25\ \Rightarrow\ 1<\frac{3}{2+\frac{1}{a_n}}<\frac65<2$$
ז"א $1<a_{n+1}<2$.
**מונוטוניות:** נראה שהסדרה יורדת:
$$\frac{a_{n+1}}{a_n}=\frac{3}{2a_n+1}$$
מ-$1<a_n<2$ נקבל $3<2a_n+1<5$, ולכן $\frac15<\frac{1}{2a_n+1}<\frac13$ ו-$\frac{a_{n+1}}{a_n}<1$.
הסדרה יורדת וחסומה מלמטה, ולכן מתכנסת. נסמן $\lim_{n\to\infty}a_n=L$ ונעבור לגבול בנוסחת הנסיגה $a_{n+1}=\frac{3a_n}{2a_n+1}$:
$$L=\frac{3L}{2L+1}\ \Rightarrow\ 2L^2+L=3L\ \Rightarrow\ L^2-L=0$$
מכיוון ש-$a_n>1$, לא ייתכן $L=0$, ולכן הגבול הוא $L=1$.
"""

SOL3A = r"""
$$f(x)=\int_{-3}^{x^3+1}t(t-1)^5\,dt$$
תחום ההגדרה: $(-\infty,\infty)$. לפי משפט היסוד של החשבון האינטגרלי וכלל השרשרת:
$$f'(x)=t(t-1)^5\Big|_{t=x^3+1}\cdot3x^2=\left(x^3+1\right)\left(x^3\right)^5\cdot3x^2=3x^{17}\left(x^3+1\right)$$
$$3x^{17}\left(x^3+1\right)=0\ \Rightarrow\ x_1=0,\quad x_2=-1$$
טבלת סימנים של $f'$: חיובית ב-$x<-1$ (עולה), שלילית ב-$-1<x<0$ (יורדת), חיובית ב-$x>0$ (עולה).
לכן ל-$f$ יש קיצון מקומי ב-$x=-1$ (מקסימום) וב-$x=0$ (מינימום).
"""

SOL3B = r"""
הפונקציה $f(x)=e^x+\sin x$ רציפה על כל הממשיים.
$f(0)=1>0$ ו-$f\left(-\frac\pi2\right)<0$ כי $\sin\left(-\frac\pi2\right)=-1$ ו-$e^{-\frac\pi2}<1$. לכן לפי משפט ערך הביניים יש פתרון בקטע $\left[-\frac\pi2,0\right]$, כלומר למשוואה $e^x+\sin x=0$ יש לפחות פתרון אחד.
**הפתרון אינו יחיד:** עבור $x\ge0$ מתקיים $e^x\ge1\ge-\sin x$, ושוויון בשני האי-שוויונות בו-זמנית אינו אפשרי (ב-$x=0$ מתקיים $\sin0=0$), ולכן $f(x)>0$ ואין שם פתרונות. עבור $x<0$ מתקיים $0<e^x<1$, ו-$\sin x$ מקבלת את כל הערכים בין $-1$ ל-$1$ שוב ושוב. בכל קטע $\left[-\frac\pi2-2\pi k,\,-2\pi k\right]$ (עבור $k=0,1,2,\dots$) מתקיים $f\left(-\frac\pi2-2\pi k\right)=e^{-\frac\pi2-2\pi k}-1<0$ ו-$f(-2\pi k)=e^{-2\pi k}>0$, ולכן לפי משפט ערך הביניים יש בכל קטע פתרון. למשוואה יש אם כן אינסוף פתרונות, והפתרון אינו יחיד.
"""

SOL4A = r"""
נמצא את הגבולות החד-צדדיים של $f$ ב-$x=\frac\pi2$.
$$\lim_{x\to\frac\pi2^-}f(x)=\lim_{x\to\frac\pi2^-}(\sin x)^{\tan x}=\{1^\infty\}=A$$
$$\ln A=\lim_{x\to\frac\pi2^-}\tan x\cdot\ln(\sin x)=\lim_{x\to\frac\pi2^-}\frac{\ln\sin x}{\cot x}=\lim_{x\to\frac\pi2^-}\frac{\frac{\cos x}{\sin x}}{-\frac{1}{\sin^2x}}=-\lim_{x\to\frac\pi2^-}\cos x\sin x=0\ \Rightarrow\ A=1$$
$$\lim_{x\to\frac\pi2^+}f(x)=\lim_{x\to\frac\pi2^+}e=e$$
הגבולות החד-צדדיים קיימים וסופיים אך שונים ($1\ne e$), ולכן $f$ אינה רציפה ב-$x=\frac\pi2$ (אי-רציפות מסוג ראשון, קפיצה).
"""

SOL4B = r"""
הפתרון הרשמי עם תיקון: בפתרון הכתוב התוצאה הסופית היא $\frac{\pi^2}{12}-\frac\pi3+\frac\pi6\ln2$. בהצבת הגבולות בשורה האחרונה מתקבל $\frac12-\frac12\ln2$ ולא $1-\frac12\ln2$, ולכן המקדם של $\pi$ הוא $-\frac16$ ולא $-\frac13$. הפתרון המתוקן נבדק (sympy).
$$V=\pi\int_0^1\left(x\sqrt{\arctan x}\right)^2dx=\pi\int_0^1x^2\arctan x\,dx=\left|\begin{matrix}u=\arctan x&du=\frac{dx}{1+x^2}\\dv=x^2dx&v=\frac{x^3}{3}\end{matrix}\right|=\pi\left(\frac{x^3}{3}\arctan x\Big|_0^1-\frac13\int_0^1\frac{x^3dx}{1+x^2}\right)=$$
$$=\pi\left(\frac13\cdot\frac\pi4-\frac13\int_0^1\left(x-\frac{x}{1+x^2}\right)dx\right)=\pi\left(\frac{\pi}{12}-\frac13\left(\frac{x^2}{2}-\frac12\ln\left(1+x^2\right)\right)\Big|_0^1\right)=\pi\left(\frac\pi{12}-\frac13\left(\frac12-\frac12\ln2\right)\right)=$$
$$=\frac{\pi^2}{12}-\frac\pi6+\frac\pi6\ln2$$
"""

SOL5A = r"""
נגדיר $f(x)=xe^{x^2}$. הפונקציה רציפה על $[a,b]$ וגזירה על $(a,b)$, ולכן לפי משפט לגרנז' קיימת $c\in(a,b)$ כך ש-$\frac{f(b)-f(a)}{b-a}=f'(c)$.
$$f'(x)=e^{x^2}+x\cdot e^{x^2}\cdot2x=e^{x^2}\left(1+2x^2\right)$$
$$\frac{be^{b^2}-ae^{a^2}}{b-a}=e^{c^2}\left(1+2c^2\right),\qquad1<a<c<b<2$$
$f'(x)=e^{x^2}\left(1+2x^2\right)$ עולה ממש עבור $x>0$ (מכפלה של שתי פונקציות חיוביות עולות), ולכן מ-$1<c<2$ נקבל
$$3e=f'(1)<e^{c^2}\left(1+2c^2\right)<f'(2)=9e^4$$
כלומר $3e<\frac{be^{b^2}-ae^{a^2}}{b-a}<9e^4$.
"""

SOL5B = r"""
$$\int\frac{\sin^3x}{\cos^4x}dx=\left|\begin{matrix}t=\cos x\\dt=-\sin x\,dx\end{matrix}\right|=\int\frac{\sin^2x\cdot\sin x\,dx}{\cos^4x}=-\int\frac{1-t^2}{t^4}dt=\frac{1}{3t^3}-\frac1t+C=\frac{1}{3\cos^3x}-\frac{1}{\cos x}+C$$
"""

SOL6A = r"""
$$y=\sqrt{1-x^2}\ \Rightarrow\ y'=\frac{-x}{\sqrt{1-x^2}}\ \Rightarrow\ 1+(y')^2=\frac{x^2}{1-x^2}+1=\frac{1}{1-x^2}$$
$$L=\int_0^{0.5}\sqrt{1+(y')^2}\,dx=\int_0^{0.5}\frac{1}{\sqrt{1-x^2}}\,dx=\arcsin x\Big|_0^{0.5}=\arcsin0.5=\frac\pi6$$
"""

SOL6B = r"""
$$\lim_{x\to1^-}\ln x\cdot\ln(1-x)=\{0\cdot\infty\}=\lim_{x\to1^-}\frac{\ln(1-x)}{\frac{1}{\ln x}}=\lim_{x\to1^-}\frac{-\frac{1}{1-x}}{-\frac{1}{\ln^2x}\cdot\frac1x}=\lim_{x\to1^-}\frac{x\ln^2x}{1-x}=\left\{\frac00\right\}=\lim_{x\to1^-}\frac{\ln^2x+2\ln x}{-1}=0$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה הבאה $y=\frac{x^3}{x^2-3}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, תחומי עליה וירידה, "
      "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1),

    Q(2, "proof", "sequences_limits",
      r"נתונה הסדרה: $a_1=2,\quad a_{n+1}=\frac{3a_n}{2a_n+1}$. הוכיחו כי הסדרה מונוטונית וחסומה וחשבו את גבולה.",
      SOL2, points=10),

    Q(3, "computation", "extrema_optimization",
      r"מצאו את כל ערכי $x$ שבהם לפונקציה $f(x)=\int_{-3}^{x^3+1}t\cdot(t-1)^5\,dt$ יש קיצון מקומי.",
      SOL3A, part="א", points=10),

    Q(3, "proof", "continuity",
      r"הראו שלמשוואה $e^x+\sin x=0$ קיים פתרון. האם הוא יחיד?",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "continuity",
      r"בדקו האם הפונקציה $f(x)=\begin{cases}(\sin x)^{\tan x}, & 0<x<0.5\pi\\[1mm] e, & x\ge0.5\pi\end{cases}$ רציפה ב-$x=0.5\pi$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      "מצאו את נפח הגוף הנוצר על ידי הסיבוב סביב ציר ה-$X$ של הצורה המישורית הכלואה בין הקווים הבאים: "
      r"$y=x\sqrt{\arctan x},\ y=0,\ x=1$.",
      SOL4B, part="ב", points=10,
      solutionSource="solved", confidence="med"),

    Q(5, "proof", "mean_value_theorems",
      r"הוכיחו את אי-השוויון $3e<\frac{be^{b^2}-ae^{a^2}}{b-a}<9e^4$ כאשר $1<a<b<2$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int\frac{\sin^3x}{\cos^4x}\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "definite_integrals",
      r"מצאו את אורך הקשת של $y=\sqrt{1-x^2}$ כאשר $0\le x\le0.5$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to1^-}\ln x\cdot\ln(1-x)$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "18B-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ח, מועד ב'",
    "year": 2018,
    "examDate": "05/02/2018",
    "sourceFile": "calculus-1/18B-A exam.pdf",
    "solutionFile": "calculus-1/18B-A handwritten-solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

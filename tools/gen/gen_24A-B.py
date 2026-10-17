# -*- coding: utf-8 -*-
"""Generator for tools/raw/24A-B.json -- calculus-1 (20151), semester B 2024, moed A (22/07/2024).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24A-B.py

Source: sitting 24A-B, pp.1-7 (typed exam with the official worked solution after each question).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Q1: the official solution labels the graph "ה." (a second "ה"); transcribed as the sketch item ו.
- Q3b: the figure in the official solution labels the top of the region "2-sqrt(2)" where the solution's own
  integration limit is 4-sqrt(2); the figure is shipped as printed (the text is the authority).
- Q4b: the official solution's sketch is clipped by the page footer and is not shipped.
- Q6b: HELD. The printed limit has numerator x^4 (value 2, sympy) but the official solution works the limit with
  numerator sin^2 x (value +oo); the official text is transcribed, the key is not trusted (see docs/ASK_ADIR.md).
- Q6a: the official line "f(0)=2^1+arctan(0)-5=-4" is printed with 2^1 where 2^0=1 is meant (the value -4 is
  correct); transcribed as 2^0.

Checks (tools/verify/24A-B/check.py, sympy): every derivative, limit, integral, recursion bound, area and volume
(washers and shells) matches the official answers. 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24A-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**א.** תחום ההגדרה של הפונקציה $x\in\mathbb{R}$.
**ב.** נקודת חיתוך עם צירי הקואורדינאטות $x=0,\ y=0$.
**ג.** תחומי עליה וירידה, נקודות קיצון: מכאן רואים שהנגזרת $f'(x)=(2x+x^2)e^x$ מתאפסת בנקודות $x=0,-2$ ובנוסף $y'>0$ כאשר $x<-2$ או $x>0$ וגם $y'<0$ כאשר $-2<x<0$. הנקודה $x=0$ היא נקודת מינימום מקומי, הנקודה $x=-2$ היא נקודת מקסימום מקומי.
**ד.** תחומי קמירות וקעירות, נקודות פיתול: $y''=e^x(x^2+4x+2)$, נקודות פיתול הן $x=-2\pm\sqrt{2}$. בנוסף, $y''>0$ עבור $x>-2+\sqrt{2}$ או $x<-2-\sqrt{2}$ וכאן הפונקציה קעורה (כלפי מעלה); $y''<0$ עבור $-2-\sqrt{2}<x<-2+\sqrt{2}$ וכאן הפונקציה קמורה (כלפי מטה).
**ה.** אין אסימפטוטה אנכית לגרף הפונקציה.
$$\begin{cases}\lim\limits_{x\to+\infty}\dfrac{f(x)}{x}=\lim\limits_{x\to+\infty}\dfrac{x^2e^x}{x}=+\infty\\[2mm]\lim\limits_{x\to-\infty}f(x)=\lim\limits_{x\to-\infty}x^2e^x=\lim\limits_{x\to-\infty}\dfrac{x^2}{e^{-x}}=\lim\limits_{x\to-\infty}\dfrac{2x}{-e^{-x}}=\lim\limits_{x\to-\infty}\dfrac{2}{e^{-x}}=0\end{cases}$$
ולכן קו ישר $y=0$ מהווה אסימפטוטה אופקית לגרף הפונקציה במינוס אינסוף.
**ו.** שרטוט (בפתרון הרשמי מסומן "ה."):
![הגרף של f(x)=x^2 e^x](images/exams/24A-B-Q1-graph.png)
"""

SOL2A = r"""
כיוון ש-$\frac{x^2+2x+3}{(x-1)(x^2+4x+4)}=\frac{x^2+2x+3}{(x-1)(x+2)^2}$ קיימים $A,B,C\in\mathbb{R}$ כך ש:
$$\frac{x^2+2x+3}{(x-1)(x^2+4x+4)}=\frac{A}{(x-1)}+\frac{B}{(x+2)}+\frac{C}{(x+2)^2}.$$
על-ידי השוואת מקדמים או הצבת ערכים ב-$x$, מקבלים ש-$A=\frac{2}{3}$, $B=\frac{1}{3}$ ו-$C=-1$. לכן
$$\int\frac{x^2+2x+3}{(x-1)(x^2+4x+4)}dx=\frac{2}{3}\int\frac{1}{x-1}dx+\frac{1}{3}\int\frac{1}{x+2}dx-\int\frac{1}{(x+2)^2}dx$$
$$=\frac{2}{3}\ln|x-1|+\frac{1}{3}\ln|x+2|+\frac{1}{x+2}+c,\qquad c\in\mathbb{R}$$
"""

SOL2B = r"""
ראשית, נוכיח באינדוקציה שהסדרה עולה. נשים לב שאכן $a_1=4=\sqrt{16}\le\sqrt{24}=a_2$. יהא $n\in\mathbb{N}$, ונניח ש-$a_n\le a_{n+1}$. אז כיוון שפונקציית השורש עולה מתקיים
$$a_{n+1}=\sqrt{a_n+20}\le\sqrt{a_{n+1}+20}=a_{n+2}.$$
לכן, לפי עקרון האינדוקציה, $a_n\le a_{n+1}$ לכל $n\in\mathbb{N}$.
כעת נוכיח באינדוקציה שהסדרה חסומה מלעיל על-ידי $5$. נשים לב שאכן $a_1=4\le5$. יהא $n\in\mathbb{N}$, ונניח ש-$a_n\le5$. אז כיוון שפונקציית השורש עולה מתקיים
$$a_{n+1}=\sqrt{a_n+20}\le\sqrt{5+20}=5$$
לכן, לפי עקרון האינדוקציה, $a_n\le5$ לכל $n\in\mathbb{N}$.
לפיכך, הסדרה עולה וחסומה מלעיל, ולכן, לפי משפט, בהכרח מתכנסת. נסמן $L=\lim_{n\to\infty}a_n$. אז גם $\lim_{n\to\infty}a_{n+1}=L$. מאריתמטיקה של גבולות מתקיים
$$L=\lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}\sqrt{a_n+20}=\sqrt{L+20}$$
כלומר $L^2-L-20=0$ ולכן $(L-5)(L+4)=0$. אבל כיוון שהאיבר הראשון בסדרה הוא $4$ והסדרה מונוטונית עולה, היא בהכרח אי-שלילית, ולכן לא ייתכן ש-$-4$ הוא גבולה. מכאן שגבול הסדרה הוא $5$.
"""

SOL3A = r"""
כיוון שלכל $a\in\mathbb{R}$ מתקיים $\lim_{x\to\infty}\left(1+\frac{a}{x}\right)^x=e^a$, מאריתמטיקה של גבולות נקבל
$$\lim_{n\to\infty}\left(\frac{n^2+5n-2}{n^2+3n-2}\right)^n=\lim_{n\to\infty}\left(1+\frac{2n}{n^2+3n-2}\right)^n=\lim_{n\to\infty}\left(1+\frac{2}{n+3-\frac{2}{n}}\right)^n$$
$$=\lim_{n\to\infty}\left(\left(1+\frac{2}{n+3-\frac{2}{n}}\right)^{n+3-\frac{2}{n}}\right)^{\frac{n}{n+3-\frac{2}{n}}}=e^2$$
"""

SOL3B = r"""
נקודת מפגש בין בקווים:
$$x-2=4-\sqrt{x},\qquad\sqrt{x}=t\ge0$$
$$t^2+t-6=0,\quad t_1=2,\quad t_2=-3,\quad x=4$$
נקודת מפגש $(4,2)$.
![התחום המישורי, נקודת המפגש (4,2) והישר x=2](images/exams/24A-B-Q3b-region.png)
שיטת פרוסות:
$$V=\pi\int_2^4\left((4-\sqrt{x})^2-(x-2)^2\right)dx=\pi\int_2^4\left(16-8\sqrt{x}+x-x^2+4x-4\right)dx=$$
$$\pi\left(12x-\frac{16\sqrt{x^3}}{3}+2.5x^2-\frac{x^3}{3}\right)\Big|_2^4\cong7.752\pi\cong24.352$$
שיטת קליפות:
$$V=2\pi\int_2^{4-\sqrt{2}}\left((4-y)^2-2\right)y\,dy+2\pi\int_0^2(y+2-2)y\,dy=$$
$$=2\pi\int_2^{4-\sqrt{2}}(14y-8y^2+y^3)\,dy+2\pi\int_0^2y^2\,dy=$$
$$=2\pi\left[\left(7y^2-\frac{8y^3}{3}+\frac{y^4}{4}\right)\Big|_2^{4-\sqrt{2}}+\left(\frac{y^3}{3}\right)\Big|_0^2\right]\cong7.752\pi$$
"""

SOL4A = r"""
$$y'=e^{\frac{1}{x}}+xe^{\frac{1}{x}}\left(-\frac{1}{x^2}\right)=e^{\frac{1}{x}}\left(\frac{x-1}{x}\right)$$
$$y'=0\Rightarrow x=1$$
$$y(0.5)=0.5e^2\cong3.694$$
$$y(1)=e\cong2.718$$
$$y(3)=3e^{\frac{1}{3}}\cong4.187$$
$$y_{\max}=3\sqrt[3]{e},\qquad y_{\min}=e\qquad(x\in[0.5,3])$$
"""

SOL4B = r"""
$$f'(x)=\frac{-2}{2\sqrt{2-2x}}=\frac{-1}{\sqrt{2-2x}}=-\frac{1}{2},\qquad\sqrt{2-2x}=2$$
$$2-2x=4,\qquad x=-1,\quad f(-1)=2$$
נקודת השקה $(-1,2)$.
משוואת המשיק:
$$y-2=-\frac{1}{2}(x+1)$$
$$y=1.5-0.5x$$
המשיק חותך את ציר ה-$X$ בנקודה $(3,0)$.
השטח:
$$S=\int_{-1}^1\left(1.5-0.5x-\sqrt{2-2x}\right)dx+\int_1^3(1.5-0.5x)\,dx$$
או
$$S=\int_{-1}^3(1.5-0.5x)\,dx-\int_{-1}^1\sqrt{2-2x}\,dx=$$
$$\left[1.5x-0.25x^2\right]_{-1}^3+\frac{1}{3}\left[\sqrt{(2-2x)^3}\right]_{-1}^1=\frac{4}{3}$$
"""

SOL5A = r"""
$$\int\frac{\ln x\,dx}{x(\ln^2x+1)}=\left|\begin{matrix}t=\ln x\\dt=\frac{1}{x}dx\end{matrix}\right|=\int\frac{t\,dt}{t^2+1}=\frac{1}{2}\ln\left(t^2+1\right)+C=\frac{1}{2}\ln\left(\ln^2x+1\right)+C$$
"""

SOL5B = r"""
ראשית, נחשב גבולות חד צדדיים בנקודות התפר:
$$\begin{cases}\lim_{x\to0^-}f(x)=\lim_{x\to0^-}\frac{\arctan(2x)}{x}\overset{(*)}{=}\lim_{x\to0^-}\frac{2}{1\left(1+4x^2\right)}=2\\ \lim_{x\to0^+}f(x)=\lim_{x\to0^+}(ax+b)=b\end{cases}\ \Leftarrow\ b=2$$
$$\begin{cases}\lim_{x\to2^-}f(x)=\lim_{x\to2^-}(ax+b)=2a+b=2a+2\\ \lim_{x\to2^+}f(x)=\lim_{x\to2^+}\frac{4\left(x-\sqrt{3x-2}\right)}{x-2}=\lim_{x\to2^+}\frac{4\left(x^2-3x+2\right)}{(x-2)\left(x+\sqrt{3x-2}\right)}=\lim_{x\to2^+}\frac{4(x-2)(x-1)}{(x-2)\left(x+\sqrt{3x-2}\right)}=1\end{cases}$$
ומכאן נקבל ש-$2a+2=1\ \Leftarrow\ a=-\frac{1}{2}$.
"""

SOL6A = r"""
נגדיר פונקציה $f(x)=2^{\sqrt{x}}+\arctan(2x)-5$.
תחום ההגדרה של הפונקציה $f(x)$ הוא $x\ge0$. הפונקציה רציפה וגזירה בתחום $x>0$. הנגזרת היא:
$$f'(x)=\frac{1}{2\sqrt{x}}2^{\sqrt{x}}\ln2+\frac{2}{1+4x^2}.$$
לכן $f'(x)=\frac{1}{2\sqrt{x}}2^{\sqrt{x}}\ln2+\frac{2}{1+4x^2}>0$ ומכאן הפונקציה עולה ממש.
כמו כן, $f(0)=2^0+\arctan(0)-5=-4$, ואם נסתכל על הגבול ב-$\infty$, נקבל: $\lim_{x\to\infty}f(x)=\infty+\frac{\pi}{2}-5=\infty$.
לכן לפי משפט ערך הביניים קיימת נקודה $c>0$, כך ש-$f(c)=0$. $c$ יחידה כי הפונקציה עולה ממש.
"""

SOL6B = r"""
יש לחשב את $\lim_{x\to0^+}\frac{\sin^2x}{\int_0^{x^2}t\cos(t^2)\,dt}$.
$$\lim_{x\to0^+}\frac{\sin^2x}{\int_0^{x^2}t\cos(t^2)\,dt}=\frac{0}{0}\overset{\text{L'hopital}}{=}\lim_{x\to0^+}\frac{2\sin x\cos x}{2x\cdot x^2\cos(x^4)}=$$
$$=\lim_{x\to0^+}\frac{\sin2x}{2x\cdot x^2\cos(x^4)}=\lim_{x\to0^+}\frac{\frac{\sin2x}{2x}}{x^2\cos(x^4)}=\frac{\lim_{x\to0^+}\frac{\sin2x}{2x}}{\lim_{x\to0^+}x^2\cos(x^4)}$$
המונה שואף ל-$1$, המכנה ל-$0^+$ לכן הגבול הוא $\infty$.
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=x^2e^x$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, תחומי עליה וירידה, "
      "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, נקודות אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{x^2+2x+3}{(x-1)(x^2+4x+4)}\,dx$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "sequences_limits",
      "נתונה הסדרה:\n" r"$$a_{n+1}=\sqrt{a_n+20},\quad a_1=4$$" "\nהוכיחו כי הסדרה מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "sequences_limits",
      r"חשבו את הגבול הבא: $\lim_{n\to\infty}\left(\frac{n^2+5n-2}{n^2+3n-2}\right)^n$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר מסיבוב התחום המישורי הכלוא בין הקווים: $y=4-\sqrt{x},\ y=x-2,\ x=2$ סביב ציר ה-$X$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "extrema_optimization",
      r"מצאו את הערך המקסימלי ואת הערך המינימלי של הפונקציה: $y=xe^{\frac{1}{x}}$ בקטע הסגור $\left[\frac{1}{2},3\right]$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "derivatives_tangents",
      r"נתונה הפונקציה: $f(x)=\sqrt{2-2x}$. חשבו את המשיק לגרף הפונקציה בעל שיפוע $-\frac{1}{2}$. "
      "מצאו את השטח התחום בין הגרף הפונקציה, המשיק וציר ה-$X$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\ln x\,dx}{x(\ln^2x+1)}$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "continuity",
      r"נתונה הפונקציה: $f(x)=\begin{cases}\frac{\arctan(2x)}{x}, & x<0\\ ax+b, & 0\le x\le2\\ \frac{4\left(x-\sqrt{3x-2}\right)}{x-2}, & x>2\end{cases}$"
      "\nמצאו לאלו ערכים של $a,b$ (ממשיים) $f(x)$ תהיה רציפה לכל $x$ ממשי.",
      SOL5B, part="ב", points=10),

    Q(6, "proof", "continuity",
      r"הוכיחו כי למשוואה $2^{\sqrt{x}}+\arctan(2x)=5$ קיים פתרון ממשי אחד בלבד.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "lhopital_taylor",
      r"חשבו את הגבול הבא: $\lim_{x\to0^+}\frac{x^4}{\int_0^{x^2}t\cos(t^2)\,dt}$.",
      SOL6B, part="ב", points=10,
      hold="official-solution-mismatch: the official solution computes a different limit (numerator sin^2 x, answer infinity) than the printed one (numerator x^4); sympy gives 2 for the printed limit"),
]

exam = {
    "examCode": "24A-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ד, מועד א'",
    "year": 2024,
    "examDate": "22/07/2024",
    "sourceFile": "calculus-1/24A-B exam+solution.pdf",
    "solutionFile": "calculus-1/24A-B exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

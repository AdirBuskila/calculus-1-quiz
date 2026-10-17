# -*- coding: utf-8 -*-
"""Generator for tools/raw/18A1-A.json -- calculus-1 (20151), semester A 2018, moed A version 1 (30/01/2018).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_18A1-A.py

Source: sitting 18A1-A, pp.1-7 (typed official solution document; the question is printed before each solution).
Part A (mandatory): Q1 (20%). Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Q1: FINAL-ANSWER errors in the official y'': numerator printed -4x^2-3x-2 (must be +2), roots printed
  (-3 +- sqrt41)/16 (must be /8), and the sign diagram labels read (3 -+ sqrt41)/16. Shipped corrected with the
  "הפתרון הרשמי עם תיקון" label, solutionSource solved, official:false (sympy).
- Q3a: the question asks for the two-sided limit x->0, the official solution computes only x->0+ (answer 1/3).
  The left limit is -1/3, so the two-sided limit does not exist. Also the L'Hopital denominator lacks the square of
  cos. Shipped with the label, solved, official:false (sympy).
- Q5a: the official substitution line lists f(0)=0 instead of f(2)=4 (x=0 is outside [1,4]); the final answers
  (max 16, min 0) are right. Corrected silently, logged in docs/ASK_ADIR.md.
- Q1/Q4a/Q4b/Q5a/Q6a: plots printed in the official solution are cropped as figures inside the solutions.
- The printed sign diagrams (arrows / arcs) are transcribed as sentences.

Checks: tools/verify/18A1-A/check.py (sympy). No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "18A1-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
הפתרון הרשמי עם תיקון: בפתרון הרשמי המונה של $y''$ מודפס $-4x^2-3x-2$ ושורשיו $\frac{-3\pm\sqrt{41}}{16}$ (ובטבלת הסימנים $\frac{3\mp\sqrt{41}}{16}$). הנכון הוא $y''=\frac{-4x^2-3x+2}{\left(x^2+1\right)^{2.5}}$ ושורשי המונה הם $\frac{-3\pm\sqrt{41}}{8}$. התיקון נבדק (sympy).
**1. תחום ההגדרה:** כל $x$.
**2. תחומי עלייה וירידה, נקודות קיצון:**
$$y'=\frac{2x+1}{\left(x^2+1\right)^{1.5}}=0\ \Rightarrow\ x=-0.5$$
טבלת סימנים של $y'$: שלילית ב-$x<-0.5$ (יורדת), חיובית ב-$x>-0.5$ (עולה). נקודת מינימום: $x=-0.5$, $y(-0.5)=-\frac{2.5}{\sqrt{1.25}}$.
**3. תחומי קמירות וקעירות, נקודות פיתול:**
$$y''=\frac{-4x^2-3x+2}{\left(x^2+1\right)^{2.5}}=0\ \Rightarrow\ x=\frac{-3\pm\sqrt{41}}{8}$$
שתי נקודות פיתול. טבלת סימנים של $y''$: שלילית ב-$x<\frac{-3-\sqrt{41}}{8}$ (קעורה), חיובית בין שתי הנקודות (קמורה), שלילית ב-$x>\frac{-3+\sqrt{41}}{8}$ (קעורה).
**4. אסימפטוטות אנכיות:** אין.
**אסימפטוטה משופעת ב-$+\infty$:** $a=\lim_{x\to+\infty}\frac{\frac{x-2}{\sqrt{x^2+1}}}{x}=0$, $b=\lim_{x\to+\infty}\frac{x-2}{\sqrt{x^2+1}}=1$, כלומר $y=1$.
**אסימפטוטה משופעת ב-$-\infty$:** $a=\lim_{x\to-\infty}\frac{\frac{x-2}{\sqrt{x^2+1}}}{x}=0$, $b=\lim_{x\to-\infty}\frac{x-2}{\sqrt{x^2+1}}=-1$, כלומר $y=-1$.
**5. שרטוט:**
![שרטוט הגרף של y = (x−2)/√(x²+1) עם האסימפטוטות האופקיות y=1 ו-y=−1](images/exams/18A1-A-Q1-graph.png)
"""

SOL2A = r"""
$$\lim_{n\to\infty}\frac{n!\sin(n!)}{(n+1)!-n!}=\lim_{n\to\infty}\frac{n!\sin(n!)}{n\cdot n!}=\lim_{n\to\infty}\frac{\sin(n!)}{n}=0$$
כיוון ש-$\sin(n!)$ סדרה חסומה.
"""

SOL2B = r"""
$$\int\frac{dx}{\sqrt[3]x+\sqrt x}=\left[\begin{matrix}t=\sqrt[6]x\\x=t^6\\dx=6t^5dt\end{matrix}\right]=\int\frac{6t^5dt}{t^2+t^3}=\int\frac{6t^3dt}{1+t}=6\int\left(t^2-t+1-\frac{1}{1+t}\right)dt=$$
$$=6\left(\frac{t^3}{3}-\frac{t^2}{2}+t-\ln|1+t|\right)+c=2\sqrt x-3\sqrt[3]x+6\sqrt[6]x-6\ln\left|1+\sqrt[6]x\right|+c$$
"""

SOL3A = r"""
הפתרון הרשמי עם תיקון: הפתרון הרשמי מחשב רק את הגבול החד-צדדי $x\to0^+$ (ומקבל $\frac13$), אבל השאלה מבקשת את הגבול הדו-צדדי $x\to0$. עבור $x\to0^-$ מתקבל $-\frac13$ (המונה חיובי והמכנה שלילי), ולכן הגבול הדו-צדדי אינו קיים. בנוסף, נגזרת המכנה היא $\frac{6x^2}{\cos^2\left(2x^3\right)}$ (בפתרון הרשמי חסר הריבוע; אין לכך השפעה על הערך). התיקון נבדק (sympy).
$$\lim_{x\to0^+}\frac{\int_0^{x^2}\sin\sqrt t\,dt}{\tan\left(2x^3\right)}=\left[\begin{matrix}\int_0^{x^2}\sin\sqrt t\,dt\xrightarrow[x\to0]{}0\\\tan\left(2x^3\right)\xrightarrow[x\to0]{}0\\\text{apply L'Hospital's rule}\end{matrix}\right]=\lim_{x\to0^+}\frac{\sin x\cdot2x}{\frac{6x^2}{\cos^2\left(2x^3\right)}}=\frac13$$
באותו אופן, עבור $x\to0^-$ הנגזרת של האינטגרל היא $\sin|x|\cdot2x$ ולכן
$$\lim_{x\to0^-}\frac{\sin|x|\cdot2x\cos^2\left(2x^3\right)}{6x^2}=\lim_{x\to0^-}\frac{-\sin x}{3x}=-\frac13$$
הגבולות החד-צדדיים שונים, והגבול הדו-צדדי אינו קיים.
"""

SOL3B = r"""
משיק משותף: פירוש הדבר, לשני הגרפים ישנה נקודה משותפת $(x,y)$ בה מתקיים שוויון הנגזרות. כלומר:
$$\begin{cases}ax^2=\ln x\\2ax=\frac1x\end{cases}\ \Leftarrow\ \begin{cases}ax^2=\ln x\\a=\frac{1}{2x^2}\end{cases}\ \Leftarrow\ \ln x=\frac12\ \Leftarrow\ x=\sqrt e\ \Leftarrow\ a=\frac{1}{2e}$$
"""

SOL4A = r"""
נגדיר את הפונקציה $y=x\arctan x-1$. נשים לב כי $y(0)<0$ ו-$y(2)>0$. יתרה מזאת, הפונקציה $y$ רציפה, בפרט מקיימת את כל התנאים של משפט ערך הביניים (משפט בולצנו-קושי) בקטע $[0,2]$. לכן קיימת נקודה $0<c<2$ כך ש-$y(c)=0$. בזה הוכחנו את קיום הפתרון בתחום הנתון. נותר להוכיח את היחידות. לשם כך נחשב את הנגזרת של הפונקציה:
$$y'=\arctan x+\frac{x}{1+x^2}$$
אשר חיובית לכל $x>0$. לכן הפונקציה מונוטונית עולה ממש בתחום הנ"ל. זה מוכיח את היחידות של הפתרון $c$.
![גרף הפונקציה y = x·arctan x − 1 בקטע מ-0 עד 2, החותך את ציר ה-x פעם אחת](images/exams/18A1-A-Q4a-graph.png)
"""

SOL4B = r"""
![הגרפים y = x ו-y = x + sin²x בקטע מ-0 עד π](images/exams/18A1-A-Q4b-fig.png)
$$S=\int_0^\pi\left(x+\sin^2x-x\right)dx=\int_0^\pi\sin^2x\,dx=\int_0^\pi\frac{1-\cos2x}{2}\,dx=\left(\frac x2-\frac{\sin2x}{4}\right)\Big|_0^\pi=\frac\pi2$$
"""

SOL5A = r"""
![גרף הפונקציה f(x) = |x³ − 3x²| בקטע מ-1 עד 4](images/exams/18A1-A-Q5a-graph.png)
מתקיים $f(x)=\left|x^2(x-3)\right|=\begin{cases}x^3-3x^2,&x\ge3\\-x^3+3x^2,&x<3\end{cases}$.
כאשר $x\ge3$: $\left(x^3-3x^2\right)'=3x^2-6x=0$ גורר $x=0$, $x=2$. כאשר $x=0$, $x=2$ אינם בתחום. באותו אופן כאשר $x<3$: $\left(-x^3+3x^2\right)'=-3x^2+6x=0$ גורר $x=0$, $x=2$, כאשר $x=0$ אינו בתחום. בנקודה $x=3$ הפונקציה אינה גזירה. לכן הנקודות החשודות לערך הגדול ביותר ולערך הקטן ביותר הן $x=1$, $x=2$, $x=3$, $x=4$. נציב בפונקציה: $f(1)=2$, $f(2)=4$, $f(3)=0$, $f(4)=16$. הערך הגדול ביותר והערך הקטן ביותר של הפונקציה בקטע $[1,4]$ הם $16$ ו-$0$ בהתאמה.
"""

SOL5B = r"""
ניעזר בהצבה טריגו' אוניברסלית:
$$\int\frac{dx}{5-3\cos x}=\int\frac{1}{5-3\frac{1-t^2}{1+t^2}}\cdot\frac{2}{1+t^2}\,dt=\int\frac{dt}{4t^2+1}=\frac14\int\frac{dt}{t^2+\frac14}=\frac12\arctan(2t)+c=\frac12\arctan\left(2\tan\frac x2\right)+c$$
"""

SOL6A = r"""
$$V=2\pi\int_1^2xe^x\,dx=\left[\begin{matrix}u=x&dv=e^xdx\\du=dx&v=e^x\end{matrix}\right]=2\pi\left(xe^x\Big|_1^2-\int_1^2e^xdx\right)=2\pi\left(xe^x\Big|_1^2-e^x\Big|_1^2\right)=2\pi\left(2e^2-e-e^2+e\right)=2\pi e^2$$
![גוף הסיבוב סביב ציר ה-y: כלי גלילי שדופנו מוגבלת על ידי העקומה y = e^x](images/exams/18A1-A-Q6a-fig.png)
"""

SOL6B = r"""
$$\lim_{x\to0}\frac{\left(e^{3x}-e^{2x}\right)^2}{\cos5x-\cos x}=\lim_{x\to0}\frac{2\left(e^{3x}-e^{2x}\right)\left(3e^{3x}-2e^{2x}\right)}{-5\sin5x+\sin x}=\lim_{x\to0}\frac{2\left(e^{3x}-e^{2x}\right)}{-5\sin5x+\sin x}$$
(הגורם $3e^{3x}-2e^{2x}$ שואף ל-$1$.)
$$=\lim_{x\to0}\frac{2\left(3e^{3x}-2e^{2x}\right)}{-25\cos5x+\cos x}=\frac{2}{-24}=-\frac{1}{12}$$
"""

HEAD1 = (r"חקרו את הפונקציה הבאה $y=\frac{x-2}{\sqrt{x^2+1}}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, "
         "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.")

questions = [
    Q(1, "computation", "function_investigation", HEAD1, SOL1,
      solutionSource="solved", official=False, confidence="med"),

    Q(2, "computation", "sequences_limits",
      r"חשבו את הגבול $\lim_{n\to\infty}\frac{n!\sin(n!)}{(n+1)!-n!}$.",
      SOL2A, part="א", points=10),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{dx}{\sqrt[3]x+\sqrt x}$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to0}\frac{\int_0^{x^2}\sin\sqrt t\,dt}{\tan\left(2x^3\right)}$.",
      SOL3A, part="א", points=10,
      solutionSource="solved", official=False, confidence="med"),

    Q(3, "computation", "derivatives_tangents",
      r"עבור איזה ערך של הפרמטר $a\in\mathbb R$ הפרבולה $y=ax^2$ משיקה לעקומה $y=\ln x$ "
      r"(כלומר לשני הגרפים קיים משיק משותף)?",
      SOL3B, part="ב", points=10),

    Q(4, "proof", "continuity",
      r"הראו כי למשוואה $x\arctan x=1$ קיים פתרון יחיד בתחום $x\ge0$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"מצאו את שטח התחום הכלוא בין $y=x,\ y=x+\sin^2x$, כאשר $0\le x\le\pi$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "extrema_optimization",
      r"מצאו מינימום ומקסימום מוחלטים של הפונקציה $f(x)=\left|x^3-3x^2\right|$ בקטע $[1,4]$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int\frac{dx}{5-3\cos x}$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "definite_integrals",
      r"חשבו את הנפח של גוף הסיבוב של התחום הכלוא בין הקווים $y=e^x,\ y=0,\ x=1,\ x=2$ סביב ציר ה-$y$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to0}\frac{\left(e^{3x}-e^{2x}\right)^2}{\cos5x-\cos x}$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "18A1-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ח, מועד א', גרסה 1",
    "year": 2018,
    "examDate": "30/01/2018",
    "sourceFile": "calculus-1/18A1-A exam+solution.pdf",
    "solutionFile": "calculus-1/18A1-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

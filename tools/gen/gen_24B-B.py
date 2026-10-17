# -*- coding: utf-8 -*-
"""Generator for tools/raw/24B-B.json -- calculus-1 (20151), semester B 2024, moed B (12/08/2024), flagship sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24B-B.py

Source: sitting 24B-B, pp.1-6 (typed exam with the official worked solution after each "פתרון" label).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each). Weight of every question 20%.

Transcription notes
- Q1 is kept as ONE item: the printed question is a single instruction list; the official solution is the
  sequence of sections a-f. Its two figures (graph of f on p.2, the plot in Q6b on p.6) belong to the official
  solution and the raw schema has no solution-image field, so they are described in words, not shipped.
- Q3a: the solution sits on p.4 (the p.3 "פתרון" label is followed by a page break).
- Q2b: the official text solves L(L-1)=0 after clearing denominators; transcribed as printed.

Checks (tools/verify/24B-B/check.py, sympy): every derivative, limit, integral, extremum value, the area and the
volume match the official answers. 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24B-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**א. תחום הגדרה:** $D=\{x\in\mathbb{R}: x\neq \pm 1\}$.
**ב. נקודות חיתוך עם צירי הקואורדינטות:** $(0,0)$.
**ג. נגזרת:** $y'=\frac{x^2(x^2-3)}{(x^2-1)^2}$, ומכאן רואים שהנגזרת מתאפסת ב-$x=0,\pm\sqrt{3}$ ובנוסף $y'>0$ כאשר $x<-\sqrt{3}$ או $x>\sqrt{3}$, וגם $y'<0$ כאשר $-\sqrt{3}<x<-1$ או $-1<x<1$ או $1<x<\sqrt{3}$.
**ד. קיצון:** $x_{min}=\sqrt{3}$ הנקודה היא נקודת מינימום מקומי, $y(x_{min})=\frac{\sqrt{27}}{2}$; $x_{max}=-\sqrt{3}$ הנקודה היא נקודת מקסימום מקומי, $y(x_{max})=\frac{-\sqrt{27}}{2}$.
**ה. נגזרת שנייה:** $y''=\frac{2x(x^2+3)}{(x^2-1)^3}$. הנקודה $(0,0)$ היא נקודת פיתול. בנוסף, $y''>0$ עבור $x>1$ או $-1<x<0$, הפונקציה קמורה (כלפי מעלה); $y''<0$ עבור $x<-1$ או $0<x<1$, הפונקציה קעורה (כלפי מטה).
**ו. אסימפטוטות:** קווים ישרים $x=\pm 1$ מהווים אסימפטוטות אנכיות לגרף הפונקציה, כי
$$\lim_{x\to -1^-}\frac{x^3}{x^2-1}=-\infty,\quad \lim_{x\to -1^+}\frac{x^3}{x^2-1}=+\infty,\quad \lim_{x\to 1^-}\frac{x^3}{x^2-1}=-\infty,\quad \lim_{x\to 1^+}\frac{x^3}{x^2-1}=+\infty$$
$$a=\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim_{x\to\pm\infty}\frac{x^3}{x(x^2-1)}=1$$
$$b=\lim_{x\to\pm\infty}(f(x)-x)=\lim_{x\to\pm\infty}\left(\frac{x^3}{x^2-1}-x\right)=\lim_{x\to\pm\infty}\left(\frac{x}{x^2-1}\right)=0$$
לכן הישר $y=x$ הוא האסימפטוטה המשופעת של הפונקציה. השרטוט הרשמי מציג את הגרף יחד עם האסימפטוטות $x=\pm1$ ו-$y=x$.
"""

SOL2A = r"""
כיוון ש-$\frac{x^2+8}{x^4+4x^2}=\frac{x^2+8}{x^2(x^2+4)}$ קיימים $A,B,C,D\in\mathbb{R}$ כך ש:
$$\frac{x^2+8}{x^2(x^2+4)}=\frac{A}{x}+\frac{B}{x^2}+\frac{Cx+D}{x^2+4}.$$
על-ידי השוואת מקדמים או הצבת ערכים ב-$x$, מקבלים ש-$A=C=0$, $B=2$ ו-$D=-1$. לכן
$$\int\frac{x^2+8}{x^2(x^2+4)}dx=\int\frac{2}{x^2}dx-\int\frac{1}{x^2+4}dx=-\frac{2}{x}-\frac{1}{2}\arctan\frac{x}{2}+c,\qquad c\in\mathbb{R}$$
"""

SOL2B = r"""
ראשית, נוכיח באינדוקציה שהסדרה יורדת. נשים לב שאכן $a_2=\frac{6}{5}\le 2=a_1$. יהא $n\in\mathbb{N}$, ונניח ש-$a_{n+1}\le a_n$ מתקיים. אז
$$a_{n+2}=\frac{3}{2+\frac{1}{a_{n+1}}}\le\frac{3}{2+\frac{1}{a_n}}=a_{n+1}.$$
לכן, לפי עקרון האינדוקציה, $a_{n+1}\le a_n$ לכל $n\in\mathbb{N}$.
כעת נוכיח באינדוקציה שהסדרה חסומה מלרע (מלמטה) על-ידי $1$. נשים לב שאכן $a_1=2\ge 1$. יהא $n\in\mathbb{N}$, ונניח ש-$a_n\ge 1$ מתקיים. אז כיוון שפונקציית השורש עולה מתקיים
$$a_{n+1}=\frac{3}{2+\frac{1}{a_n}}\ge\frac{3}{2+\frac{1}{1}}=1.$$
לכן, לפי עקרון האינדוקציה, $a_n\ge 1$ לכל $n\in\mathbb{N}$.
לפיכך, הסדרה יורדת וחסומה מלרע, ולכן, לפי משפט, מתכנסת. נסמן $L=\lim_{n\to\infty}a_n$. אז גם $\lim_{n\to\infty}a_{n+1}=L$. מאריתמטיקה של גבולות מתקיים
$$L=\lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}\frac{3}{2+\frac{1}{a_n}}=\frac{3}{2+\frac{1}{L}},$$
כלומר $L^2-L=0$ ולכן $L(L-1)=0$. אבל כיוון שהסדרה חסומה מלרע על-ידי $1$, גם גבולה חסום מלרע על-ידי $1$, ולכן לא ייתכן שגבולה הוא $0$. מכאן שגבול הסדרה הוא $1$.
"""

SOL3A = r"""
$$\lim_{n\to\infty}\left(\sqrt{1+n+n^2}-\sqrt{1-2n+n^2}\right)=\lim_{n\to\infty}\frac{\left(\sqrt{1+n+n^2}-\sqrt{1-2n+n^2}\right)\left(\sqrt{1+n+n^2}+\sqrt{1-2n+n^2}\right)}{\sqrt{1+n+n^2}+\sqrt{1-2n+n^2}}$$
$$=\lim_{n\to\infty}\frac{1+n+n^2-(1-2n+n^2)}{\sqrt{1+n+n^2}+\sqrt{1-2n+n^2}}=\lim_{n\to\infty}\frac{3n}{\sqrt{1+n+n^2}+\sqrt{1-2n+n^2}}$$
$$=\lim_{n\to\infty}\frac{3}{\sqrt{\frac{1}{n^2}+\frac{1}{n}+1}+\sqrt{\frac{1}{n^2}-\frac{2}{n}+1}}=\frac{3}{2}.$$
"""

SOL3B = r"""
שיטת קליפות:
$$V=2\pi\int_0^1 x\left(e+1-(e^x+1)\right)dx=2\pi\int_0^1 x\left(e-e^x\right)dx=2\pi\left(e\int_0^1 x\,dx-\int_0^1 xe^x\,dx\right)$$
באינטגרציה בחלקים, עם $u=x,\ v'=e^x,\ du=dx,\ v=e^x$:
$$=2\pi\left(e\frac{x^2}{2}\Big|_0^1-\left(xe^x\Big|_0^1-\int_0^1 e^x\,dx\right)\right)=2\pi\left(\frac{1}{2}e-e+e^x\Big|_0^1\right)=2\pi\left(\frac{e}{2}-1\right)$$
"""

SOL4A = r"""
$$y'=2(\ln x)\cdot\frac{1}{x}-\frac{2}{x}=0$$
$$\frac{2}{x}(\ln x-1)=0,\quad x=e$$
$$y(\sqrt{e})=-0.75,\quad y(e)=-1,\quad y(e^2)=0$$
$$y_{max}=y(e^2)=0,\quad y_{min}=y(e)=-1$$
"""

SOL4B = r"""
$$\lim_{x\to+\infty}\left(\frac{3x^4}{x^3+2x+9}-ax-b\right)=\lim_{x\to+\infty}\frac{3x^4-ax^4-2ax^2-9ax}{x^3+2x+9}-b=0$$
לקיום גבול נדרש $a=3$, אז מקבלים:
$$\lim_{x\to+\infty}\frac{-6x^2-27x}{x^3+2x+9}=b\ \Longrightarrow\ b=0$$
אז התשובה היא $a=3,\ b=0$.
"""

SOL5A = r"""
ראשית, נחשב גבולות חד צדדיים בנקודות התפר:
$$\lim_{x\to-2^-}f(x)=\lim_{x\to-2^-}e^{\frac{-x|x+2|}{(x+2)^2}}\to e^{+\infty}=+\infty$$
$$\lim_{x\to-2^+}f(x)=\lim_{x\to-2^+}(x+3)=1$$
**סיכום:** $x=-2$ היא נקודת אי רציפות מסוג שני.
$$\lim_{x\to0^-}f(x)=\lim_{x\to0^-}(x+3)=3$$
$$\lim_{x\to0^+}f(x)=\lim_{x\to0^+}\arctan\left(\frac{1}{x}\right)\to\arctan(+\infty)=\frac{\pi}{2}$$
**סיכום:** $x=0$ היא נקודת אי רציפות מסוג ראשון (קפיצה סופית).
"""

SOL5B = r"""
$$\int x\cos(x^2)\,dx=\left|\begin{matrix}t=x^2\\dt=2x\,dx\end{matrix}\right|=\frac{1}{2}\int\cos(t)\,dt=\frac{1}{2}\sin(t)+C=\frac{1}{2}\sin(x^2)+C$$
"""

SOL6A = r"""
נגדיר פונקציית עזר: $f(x)=e^x-x-1$. הפונקציה גזירה. נגזור ונקבל: $f'(x)=e^x-1$. מתקיים: $f'(0)=0$. כמו כן $f''(x)=e^x$ ולכן $f''(0)=e^0=1>0$. לכן $x=0$ היא נקודת מינימום מקומי. $f(0)=0$ ולכן הפונקציה מקיימת לכל $x$ כי $f(x)=e^x-x-1\ge f(0)=0$. מכאן: $e^x-x-1\ge 0\Rightarrow e^x\ge x+1$.
"""

SOL6B = r"""
הפונקציות $y=x,\ y=\frac{1}{x}$ נחתכות ב-$x=\pm1$. אבל ברביע הראשון זה ב-$x=1$.
השטח המבוקש מורכב ממשולש ישר זוית שנסמן ב-$S_1$, שקדקדיו: $(1,1),(4,4),(1,4)$. שטחו הוא $\frac{9}{2}$.
שטח נוסף שצריך לחשב הוא השטח בין $y=4$, הפונקציה $y=\frac{1}{x}$ ו-$x=1$. נסמן אותו ב-$S_2$. נסמן ב-$S_4$ את המלבן שקדקודיו הם: $(0,1),(1,1),(1,4),(0,4)$. מקבלים:
$$S_2=S_4-S_3=3-\int_1^4\frac{1}{y}\,dy=3-\ln 4.$$
בסה"כ: $S=S_1+S_2=\frac{15}{2}-\ln 4$.
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=\frac{x^3}{x^2-1}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, "
      "תחומי עליה וירידה, נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int \frac{x^2+8}{x^4+4x^2}\,dx$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "sequences_limits",
      "נתונה הסדרה:\n" r"$$a_{n+1}=\frac{3}{2+\frac{1}{a_n}},\quad a_1=2$$" "\nהוכיחו כי הסדרה מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "sequences_limits",
      r"חשבו את הגבול הבא: $\lim_{n\to\infty}\left(\sqrt{1+n+n^2}-\sqrt{1-2n+n^2}\right)$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר מסיבוב התחום המישורי הכלוא בין הקווים: $y=e^x+1,\ y=e+1,\ x=0$ סביב ציר ה-$Y$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "extrema_optimization",
      r"מצאו את הערך המקסימלי ואת הערך המינימלי של הפונקציה: $y=\ln^2 x-2\ln x$, בקטע הסגור $[\sqrt{e},e^2]$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "function_limits",
      r"מצאו לאלו ערכים של $a,b$ (ממשיים) מתקיים: $\lim_{x\to+\infty}\left(\frac{3x^4}{x^3+2x+9}-ax-b\right)=0$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "continuity",
      r"נתונה הפונקציה: $f(x)=\begin{cases} e^{\frac{-x|x+2|}{(x+2)^2}} & x<-2\\ x+3 & -2\le x\le 0\\ \arctan\left(\frac{1}{x}\right) & x>0\end{cases}$"
      "\nמצאו את נקודות אי הרציפות שלה, וציינו את סוג אי הרציפות בנקודה.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int x\cdot\cos(x^2)\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "proof", "extrema_optimization",
      r"הוכיחו כי לכל $x$ ממשי מתקיים אי השוויון $e^x\ge x+1$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "definite_integrals",
      r"מצאו את השטח התחום החסום בין הגרפים של הפונקציות: $y=\frac{1}{x},\ y=x,\ y=4$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "24B-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ד, מועד ב'",
    "year": 2024,
    "examDate": "12/08/2024",
    "sourceFile": "calculus-1/24B-B exam+solution.pdf",
    "solutionFile": "calculus-1/24B-B exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

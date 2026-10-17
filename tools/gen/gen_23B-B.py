# -*- coding: utf-8 -*-
"""Generator for tools/raw/23B-B.json -- calculus-1 (20151), semester B 2023, moed B (10/07/2023).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23B-B.py

Source: sitting 23B-B, pp.1-7 (typed exam with the official worked solution after each question).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each). Weight of every question 20%.

Transcription notes
- Official solution transcribed in full, as printed. Rubric and steps are intentionally not written.
- Q1: the official graph (p.2) is shipped as a figure.
- Q2b (as printed): the text says the sequence is bounded above "by 6" and then proves a_n<5; transcribed as printed.
- Q5b (as printed): the middle expression "x - ln(1+x^2)" uses x where the substitution variable t belongs; the final
  answer x - ln(1+e^(2x)) + C is correct (tools/verify/23B-B/check.py).

Checks (tools/verify/23B-B/check.py, sympy): every derivative, limit, integral, volume and arc length matches the
official answers; the final answers have 0 mismatches.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23B-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
$y=xe^{\frac{1}{x}}$
**א. תחום הגדרה** $D=\{x\neq0\}$. אין נקודות חיתוך עם צירי הקואורדינטות.
**ב.** $y'=e^{\frac{1}{x}}-\frac{1}{x}e^{\frac{1}{x}}=e^{\frac{1}{x}}\left(1-\frac{1}{x}\right)$. מכאן רואים שהנגזרת מתאפסת רק ב-$x=1$ ובנוסף $y'>0$ כאשר $x<0\cup x>1$ וגם $y'<0$ כאשר $0<x<1$. הנקודה היא נקודת מינימום מקומי.
**ג.** $y''=e^{\frac{1}{x}}\left(-\frac{1}{x^2}+\frac{1}{x^3}+\frac{1}{x^2}\right)=e^{\frac{1}{x}}\cdot\frac{1}{x^3}$. אין נקודות פיתול. בנוסף, $y''>0$ עבור $x>0$ וכאן הפונקציה קעורה (כלפי מעלה) ו-$y''<0$ עבור $x<0$ וכאן הפונקציה קמורה (כלפי מטה).
**ד.** $\begin{cases}\lim_{x\to0^-}xe^{1/x}=0\\ \lim_{x\to0^+}xe^{1/x}=+\infty\end{cases}$ ולכן קו ישר $x=0$ (ציר ה-$y$) מהווה אסימפטוטה אנכית לגרף הפונקציה.
$\begin{cases}\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim_{x\to\pm\infty}e^{1/x}=1\\ \lim_{x\to\pm\infty}(f(x)-1x)=\lim_{x\to\pm\infty}x\left(e^{1/x}-1\right)=1\end{cases}$ ולכן קו ישר $y=x+1$ מהווה אסימפטוטה משופעת לגרף הפונקציה גם בפלוס וגם במינוס אינסוף.

![הגרף הרשמי של הפונקציה](images/exams/23B-B-Q1-graph.png)
"""

SOL2A = r"""
$$\int\frac{1}{2+\cos x}dx=\left[t=\tan\frac{x}{2},\quad\cos x=\frac{1-t^2}{1+t^2},\ dx=\frac{2}{1+t^2}dt\right]=\int\frac{1}{2+\frac{1-t^2}{1+t^2}}\cdot\frac{2}{1+t^2}dt=$$
$$=2\int\frac{1}{2+2t^2+1-t^2}dt=2\int\frac{1}{t^2+3}dt=\frac{2}{\sqrt{3}}\arctan\frac{t}{\sqrt{3}}=\frac{2}{\sqrt{3}}\arctan\frac{\tan\frac{x}{2}}{\sqrt{3}}+c$$
"""

SOL2B = r"""
נתונה הסדרה $a_1=0,\ a_{n+1}=\sqrt{20+a_n}$. הוכיחו כי הסדרה מתכנסת וחישבו את הגבול של הסדרה.
נוכיח באינדוקציה שהסדרה עולה $a_{n+1}>a_n\ge0$.
בדיקה עבור $n=1$: $a_2=\sqrt{20}>a_1=0\ge0$.
הנחת האינדוקציה: $a_{n+1}>a_n\ge0$.
צריך להוכיח: $a_{n+2}>a_{n+1}\ge0$.
$$a_{n+1}>a_n\ge0\Rightarrow a_{n+1}+20>a_n+20\ge20\Rightarrow\sqrt{a_{n+1}+20}>\sqrt{a_n+20}\ge\sqrt{20}\Rightarrow a_{n+2}>a_{n+1}\ge0$$
נוכיח באינדוקציה הסדרה חסומה מלמעלה על ידי 6: $a_n<5$.
בדיקה עבור $n=1$: $a_2=\sqrt{20}<5$.
הנחת האינדוקציה: $a_n<5$.
צריך להוכיח: $a_{n+1}<5$.
$$a_n<5\Rightarrow a_n+20<25\Rightarrow\sqrt{a_n+20}<\sqrt{25}\Rightarrow a_{n+1}<5$$
הסדרה עולה וחסומה מלמעלה לכן היא מתכנסת. נסמן $\lim_{n\to\infty}a_n=L$.
$$a_{n+1}=\sqrt{20+a_n}\Rightarrow\lim_{n\to\infty}a_n=\lim_{n\to\infty}\sqrt{20+a_n}\Rightarrow L=\sqrt{20+L}\Rightarrow L^2-L-20=0$$
$L_1=5$, $L_2=-4$ ($\varnothing$).
תשובה: $\lim_{n\to\infty}a_n=5$
"""

SOL3A = r"""
$$\lim_{x\to0}\frac{x^4}{\int_0^{x^2}\ln(1+3t)\,dt}=\left\{\frac{0}{0}\right\}=\lim_{x\to0}\frac{4x^3}{\ln(1+3x^2)\cdot2x}=\lim_{x\to0}\frac{2x^2}{\ln(1+3x^2)}\left\{\frac{0}{0}\right\}$$
$$=\lim_{x\to0}\frac{4}{\frac{1}{1+3x^2}\cdot6}=\frac{2}{3}$$
"""

SOL3B = r"""
$$\lim_{x\to0^+}f(x)=\lim_{x\to0^+}\ln\left(a+e^{-\frac{1}{x}}\right)=\ln a,\qquad f(0)=\ln^2a$$
על מנת שפונקציה תהיה רציפה יש לקיים:
$$\lim_{x\to0^+}f(x)=f(0)\Rightarrow\ln a=\ln^2a\Rightarrow\ln a(\ln a-1)=0$$
$$\ln a=0\Rightarrow a=1;\quad\ln a=1\Rightarrow a=e$$
"""

SOL4A = r"""
**דרך א'**
נגדיר פונקציה $f(x)=\arcsin x$. הפונקציה מקיימת את משפט לגרנז', כלומר רציפה בקטע $x\in[0,a]$, גזירה בקטע $x\in(0,a)$, כלומר קיימת נקודה $c\in(0,a)$, כך שמתקיים $f'(c)=\frac{f(a)-f(0)}{a-0}$. גזור את הפונקציה. נקבל: $f'(c)=\frac{1}{\sqrt{1-c^2}}$, כלומר $\frac{1}{\sqrt{1-c^2}}=\frac{\arcsin a-\arcsin0}{a-0}$, לכן מתקיים $1<\frac{\arcsin a-\arcsin0}{a-0}<\frac{1}{\sqrt{1-a^2}}$, מ.ש.ל.

**דרך ב'**
נגדיר פונקציה $f(x)=\arcsin x-x$ נגזור את הפונקציה. נקבל: $f'(x)=\frac{1}{\sqrt{1-x^2}}-1$.
נראה ש: $f'(x)>0,\ \forall0<x<1$:
$$0<x<1\Rightarrow0<x^2<1\Rightarrow0<1-x^2<1\Rightarrow\frac{1}{1-x^2}>1\Rightarrow\frac{1}{1-x^2}-1>0$$
לכן $f'(x)>0$ בקטע $(0,1)$, לכן הפונקציה עולה. אבל $f(0)=\arcsin0-0=0$ ומכאן $f(x)=\arcsin x-x>0\Rightarrow\arcsin x>x\Rightarrow\arcsin a>a$.
אם נגדיר עכשיו $g(x)=\frac{x}{\sqrt{1-x^2}}-\arcsin x$, אז
$$g'(x)=\frac{1}{(1-x^2)^{\frac{3}{2}}}-\frac{1}{(1-x^2)^{\frac{1}{2}}}=\frac{x^2}{(1-x^2)^{\frac{3}{2}}}>0.$$
לכן $g(x)$ עולה בקטע $(0,1)$ אבל $g(0)=0$ ולכן $g(x)=\frac{x}{\sqrt{1-x^2}}-\arcsin x>0\Rightarrow\frac{a}{\sqrt{1-a^2}}-\arcsin a>0$ ולכן בסה"כ מתקיים:
$$a<\arcsin a<\frac{a}{\sqrt{1-a^2}}.$$
"""

SOL4B = r"""
נפח גוף סיבוב סביב ציר $Y$ הוא לפי הנוסחה: $V=2\pi\int_a^bxf(x)\,dx$.
נבדוק את הנק' החיתוך $x^2=2x$. נקבל ב-$x=0,\ x=2$ ובקטע $[0,2]$ מתקיים $2x\ge x^2$.
$$V=2\pi\int_0^2x\left[2x-x^2\right]dx=2\pi\int_0^2\left[2x^2-x^3\right]dx=2\pi\left[\frac{2}{3}x^3-\frac{x^4}{4}\right]\Big|_0^2=\frac{8}{3}\pi$$
לכן $\frac{8}{3}\pi$.
"""

SOL5A = r"""
$$\lim_{x\to+\infty}\frac{\ln\left(1+\frac{1}{x}\right)}{\sin\left(\frac{3}{x}\right)}=\left\{\frac{0}{0}\right\}=\lim_{x\to+\infty}\frac{\frac{1}{1+\frac{1}{x}}\left(-\frac{1}{x^2}\right)}{\cos\left(\frac{3}{x}\right)\left(-\frac{3}{x^2}\right)}=\frac{1}{3}$$
"""

SOL5B = r"""
$$\int\frac{e^{-x}-e^x}{e^{-x}+e^x}dx=\int\frac{e^{-x}+e^x-e^x-e^x}{e^{-x}+e^x}dx$$
$$=\int dx-2\int\frac{e^x}{e^{-x}+e^x}dx=\left|\begin{matrix}t=e^x\\ dt=e^xdx\end{matrix}\right|$$
$$=x-2\int\frac{1}{\frac{1}{t}+t}dt=x-2\int\frac{1}{\frac{1+t^2}{t}}dt=x-2\int\frac{t}{1+t^2}dt$$
$$=x-\ln(1+x^2)+C=x-\ln\left(1+e^{2x}\right)+C$$
"""

SOL6A = r"""
$$L=\int_a^b\sqrt{1+\left(f'(x)\right)^2}\,dx=\int_{\frac{\pi}{3}}^{\frac{\pi}{2}}\sqrt{1+\frac{\cos^2x}{\sin^2x}}\,dx=\int_{\frac{\pi}{3}}^{\frac{\pi}{2}}\frac{1}{\sin x}\,dx=\ln\left|\tan\frac{x}{2}\right|\Big|_{\frac{\pi}{3}}^{\frac{\pi}{2}}$$
$$=\ln1-\ln\frac{1}{\sqrt{3}}=0.5493$$
"""

SOL6B = r"""
נסמן: $f(x)=\arctan x+x^3+x^5-2$.
פונקציה רציפה בקטע $[0,1]$ מקבלת סימנים שונים בקצוות הקטע: $f(0)=-2<0$, $f(1)=\frac{\pi}{4}>0$, לכן קיימת לפחות נקודה אחת $x=c,\ (0<c<1)$ כך ש-$f(c)=0$.
נוכיח כי הפתרון הוא יחיד. נגזרת של הפונקציה חיובית $\left(f'(x)=\frac{1}{1+x^2}+3x^2+5x^4>0\right)$, לכן הפונקציה מונוטונית עולה וחותכת ציר ה-$X$ פעם אחד בלבד.
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=xe^{\frac{1}{x}}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, "
      "תחומי עליה וירידה, נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{1}{2+\cos x}\,dx$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "sequences_limits",
      r"נתונה הסדרה: $a_1=0,\ a_{n+1}=\sqrt{20+a_n}$." "\nהוכיחו כי הסדרה מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "lhopital_taylor",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\frac{x^4}{\int_0^{x^2}\ln(1+3t)\,dt}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "continuity",
      r"נתונה הפונקציה $f(x)=\begin{cases}\ln\left(a+e^{-\frac{1}{x}}\right), & x>0\\ \ln^2\left(a+x^2\right), & x\le0\end{cases}$, כאשר $a>0$."
      "\n" r"עבור אילו ערכי $a$ הפונקציה רציפה ב-$x=0$?",
      SOL3B, part="ב", points=10),

    Q(4, "proof", "mean_value_theorems",
      r"הוכיחו את אי השוויון הבא עבור $0<a<1$: $a<\arcsin(a)<\frac{a}{\sqrt{1-a^2}}$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר מסיבוב של התחום המישורי הכלוא בין הקווים: $y=2x,\ y=x^2$ סביב ציר ה-$Y$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to+\infty}\frac{\ln\left(1+\frac{1}{x}\right)}{\sin\left(\frac{3}{x}\right)}$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{e^{-x}-e^x}{e^{-x}+e^x}\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "definite_integrals",
      r"חשבו את אורך הקשת המוגדרת ע״י $f(x)=\ln(\sin x)$ בתחום $\frac{\pi}{3}\le x\le\frac{\pi}{2}$.",
      SOL6A, part="א", points=10),

    Q(6, "proof", "continuity",
      r"הוכיחו כי למשוואה $\arctan x+x^3+x^5-2=0$ קיים שורש ממשי והוא יחיד.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "23B-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ג, מועד ב'",
    "year": 2023,
    "examDate": "10/07/2023",
    "sourceFile": "calculus-1/23B-B exam+solution.pdf",
    "solutionFile": "calculus-1/23B-B exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

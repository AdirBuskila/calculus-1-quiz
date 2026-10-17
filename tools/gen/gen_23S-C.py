# -*- coding: utf-8 -*-
"""Generator for tools/raw/23S-C.json -- calculus-1 (20151), summer semester 2023, special moed (05/01/2023).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23S-C.py

Source: sitting 23S-C, pp.1-9 (typed exam with the official worked solution after each question).
Part 1 (mandatory): Q1. Part 2: choose 4 of Q2-Q6 (a/b parts, 10% each). Weight of every question 20%.
NOTE: the header of this exam reads "הנדסת חשמל ואלקטרוניקה, מדעי מחשב" (lecturer ליובומיר מלייב) although the file is
filed under "שלנו". GATE1 excludes only 23A-A, 25A-A, 25A-B by code; the orchestrator should confirm 23S-C stays in scope.

Transcription notes
- Official solution transcribed in full, as printed. Rubric and steps are intentionally not written.
- Q4b is HELD: the official solution computes V = e-2 = 0.714, dropping the factor pi, and e-2 is 0.718 not 0.714;
  the correct volume is pi*(e-2) (tools/verify/23S-C/check.py). Text kept as printed.
- Q3b (shipped as printed): the official solution prints f(-3) = -59 but f(-3) = -65; only the sign is used, so the
  conclusion is unaffected.
- Q6b (shipped as printed): the middle term of the |R1| chain repeats 1/(9*cbrt(c^5)); the bound 1/288 is correct (c>8).
- Q1 graph (p.2) is part of the official solution and is shipped as a figure.

Checks (tools/verify/23S-C/check.py, sympy): every derivative, limit, integral, extremum, sequence value and the
tangent line match the official answers except Q3b's intermediate value and Q4b above.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23S-C.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**1)** $D:\{-\infty<x<+\infty\}$.
**2)** $f(-x)=-2xe^{-\frac{(-x)^2}{2}}=-2xe^{-\frac{x^2}{2}}=-f(x)$, לכן הפונקציה אי-זוגית.
**3)** על הגרף של הפונקציה יש נקודה $(0,0)$.
**4)** $y'=f'(x)=2e^{-\frac{x^2}{2}}+2xe^{-\frac{x^2}{2}}(-x)=2e^{-\frac{x^2}{2}}(1-x^2)$.
$y'=0\Rightarrow x^2=1\Rightarrow x_1=1,\ x_2=-1$. סימני הנגזרת: $(-)$ עד $-1$, $(+)$ בין $-1$ ל-$+1$, $(-)$ אחרי $+1$.
$x=-1$: $f_{min}(-1)=-\frac{2}{\sqrt{e}}\Rightarrow$ נקודת מינימום מקומי $\left(-1,-\frac{2}{\sqrt{e}}\right)$.
$x=+1$: $f_{max}(+1)=\frac{2}{\sqrt{e}}\Rightarrow$ נקודת מקסימום מקומי $\left(+1,\frac{2}{\sqrt{e}}\right)$.
**5)** $y''=f''(x)=\left(2e^{-\frac{x^2}{2}}(1-x^2)\right)'=2e^{-\frac{x^2}{2}}(-x)(1-x^2)+2e^{-\frac{x^2}{2}}(-2x)=-2xe^{-\frac{x^2}{2}}(3-x^2)$.
$y''=0\Rightarrow\left(x_1=0,\ x_2=-\sqrt{3},\ x_3=+\sqrt{3}\right)$.
סימני הנגזרת השנייה: $(-)(\cap)$ עד $-\sqrt{3}$, $(+)(\cup)$ בין $-\sqrt{3}$ ל-$0$, $(-)(\cap)$ בין $0$ ל-$+\sqrt{3}$, $(+)(\cup)$ אחרי $+\sqrt{3}$.
נקודות פיתול: $x_1=0,\ x_2=-\sqrt{3},\ x_3=+\sqrt{3}$.
**6)** אין אסימפטוטה אנכית.
$a=\lim_{x\to+\infty}\frac{2x}{xe^{\frac{x^2}{2}}}=0$. יש אסימפטוטה אפקית מימין.
$b=\lim_{x\to+\infty}\frac{(2x)'}{\left(e^{\frac{x^2}{2}}\right)'}=\left|\frac{\infty}{\infty}\right|(\text{lopital})=\lim_{t\to+\infty}\frac{2}{xe^{\frac{x^2}{2}}}=\left|\frac{1}{\infty}\right|=0$.
יש אסימפטוטה אפקית מימין: $y=0x+0=0$, וגם אסימפטוטה משופעת משמאל $y=0$ (פונקציה אי-זוגית).

![הגרף הרשמי של הפונקציה](images/exams/23S-C-Q1-graph.png)
"""

SOL2A = r"""
הראו שהסדרה מונוטונית, חסומה ומצא את גבולה.
**חסומה:** נניח ש-$1\le a_n<2$ ($n=1\Rightarrow a_1=1<2$).
$n=k\Rightarrow 1\le a_k<2$. צ"ל: $n=k+1\Rightarrow 1\le a_{k+1}<2$.
$$a_{k+1}=\frac{a_k}{2}+1=\frac{1}{2}(a_k+2)\le\frac{1}{2}(2+2)=2$$
הסדרה חסומה.
**מונוטונית:** $a_{n+1}=\frac{a_n}{2}+1,\ a_1=1<a_2=\frac{1}{2}+1=\frac{3}{2}=1.5<a_3=1.75<a_4=1.875\Rightarrow\uparrow\ (?)$
$$a_{n+1}-a_n=\frac{a_n}{2}+1-a_n=1-\frac{a_n}{2}>1-\frac{2^-}{2}>0^+\Rightarrow a_n\uparrow$$
הסדרה עולה.
**3.** הסדרה עולה וחסומה לכן יש לה גבול:
מצא את גבולה: $\lim_{n\to\infty}a_{n+1}=a_n=L$,
$$\lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}\left(\frac{a_n}{2}+1\right)=\frac{L}{2}+1=L\Rightarrow 2L-L=L=2\Rightarrow(L=2)$$
"""

SOL2B = r"""
$$\int\frac{x^3-2x}{x^2+1}dx\left[x-\frac{3x}{x^2+1}\right]=\int x\,dx-\int\frac{3x}{x^2+1}dx=$$
$$=\frac{x^2}{2}-\frac{3}{2}\int\frac{d(x^2+1)}{x^2+1}dx=\frac{x^2}{2}-\frac{3}{2}\ln(x^2+1)+C$$
"""

SOL3A = r"""
$$\lim_{x\to1^-}f(x)=\lim_{x\to1^-}(ax^2+x)=a+1=f(1)$$
$$\lim_{x\to1^+}f(x)=\lim_{x\to1^-}(2x^2-bx)=2-b$$
פונקציה רציפה אם $a+1=2-b\Rightarrow a+b=1$.
$$f'(x)=\begin{cases}2ax+1, & x<1\\ 4x-b, & x>1\end{cases}$$
$f'(1^-)=2a+1,\quad f'(1^+)=4-b$.
פונקציה תהי גזירה אם: $f'(1^-)=f'(1^+)$, כלומר $2a+1=4-b\Rightarrow 2a+b=3$.
מקבלים:
$$\begin{cases}a+b=1\\ 2a+b=3\end{cases}\Rightarrow a=2,\ b=-1$$
"""

SOL3B = r"""
$$f'(x)=6x^2-2x+1$$
$$f'(x)=0\Rightarrow x\in\varnothing$$
$f'(x)>0$ הפונקציה עולה בתחום $(-\infty,\infty)$.
$$f(-3)=-59<0$$
$$f(0)=1>0$$
בקצוות הקטע סימנים של הפונקציה מנוגדים ופונקציה עולה בקטע, לכן יש נקודת חיתוך אחת עם ציר ה-$X$.
"""

SOL4A = r"""
$$\lim_{x\to\infty}\left(\frac{x^2+5x+4}{x^2-3x+7}\right)^{2x}=\lim_{x\to\infty}\left(\frac{x^2-3x+3x+7-7+5x+4}{x^2-3x+7}\right)^{2x}=$$
$$=\lim_{x\to\infty}\left(\frac{x^2-3x+7}{x^2-3x+7}+\frac{8x-3}{x^2-3x+7}\right)^{2x}=\lim_{x\to\infty}\left(1+\frac{8x-3}{x^2-3x+7}\right)^{2x}=$$
$$=\lim_{x\to\infty}\left(1+\frac{8x-3}{x^2-3x+7}\right)^{\frac{x^2-3x+7}{8x-3}\cdot\left(2x\cdot\frac{8x-3}{x^2-3x+7}\right)}\quad(*)$$
$$\left(\lim_{x\to\infty}\frac{16x^2-6x}{x^2-3x+7}\ \left(\frac{\infty}{\infty}\right)=\lim_{x\to\infty}\frac{x^2\left(16-\frac{6x}{x^2}\right)}{x^2\left(1-\frac{3x}{x^2}+\frac{7}{x^2}\right)}\right)=16\ \Rightarrow$$
$$(*)\Rightarrow\ =e^{16}.$$
"""

SOL4B = r"""
$$V_x=\pi\int_1^e\ln^2x\,dx\left[\begin{matrix}\ln^2x=u,\ du=2\frac{\ln x}{x}dx\\ dv=dx,\ v=x\end{matrix}\right]=x\ln^2x\Big|_1^e-2\int x\cdot\frac{1}{x}\ln x\,dx\left[\begin{matrix}\ln x=u,\ du=\frac{dx}{x}\\ dv=dx,\ v=x\end{matrix}\right]=$$
$$=\left(e\ln^2e-1\ln^21\right)-2\left(x\ln x\Big|_1^e-\int_1^e x\cdot\frac{1}{x}dx\right)=e-2\left(e\ln e-1\ln1-x\right)\Big|_1^e=e-2(e-0-e+1)=e-2\approx0.714$$
"""

SOL5A = r"""
$$y'=\pi\sin\left(\frac{y}{2}\right)+\pi x\cos\left(\frac{y}{2}\right)\frac{y'}{2}$$
$$y'=\frac{\pi\sin\left(\frac{y}{2}\right)}{1-\frac{\pi x}{2}\cos\left(\frac{y}{2}\right)}$$
$$y'(1)=\frac{\pi\sin\left(\frac{\pi}{2}\right)}{1-\frac{\pi x}{2}\cos\left(\frac{\pi}{2}\right)}=\pi$$
$$y-\pi=\pi(x-1)$$
$$y=\pi x$$
"""

SOL5B = r"""
$$\lim_{x\to0^+}x^{\frac{1}{\ln(e^x-1)}}\quad\left(\lim_{x\to0^+}0^{\frac{1}{\ln(e^0-1)}}\right)=\left(0^{\frac{1}{\ln0}}\right)\approx\left(0^0\right)=A,$$
$$=\lim_{x\to0^+}x^{\frac{1}{\ln(e^x-1)}}=A,\qquad\ln A=\lim_{x\to0^+}\ln\left(x^{\frac{1}{\ln(e^x-1)}}\right)\ \left(\ln0^0\right)=$$
$$=\lim_{x\to0^+}\frac{\ln x}{\ln(e^x-1)}\left(\frac{\infty}{\infty}\right)(\text{Lopital})=\lim_{x\to0^+}\frac{\left(\frac{1}{x}\right)}{\left(\frac{e^x}{e^x-1}\right)}=\lim_{x\to0^+}\frac{e^x-1}{x\cdot e^x}\left(\frac{0}{0}\right)$$
$$(\text{Lopital})=\lim_{x\to0^+}\frac{e^x}{e^x+x\cdot e^x}=\lim_{x\to0^+}\frac{e^x}{e^x+0}=1=\ln e=\ln A\Rightarrow A=e,$$
"""

SOL6A = r"""
$y=2x+3\sqrt[3]{x^2},\ x\in[-2,0],\ y'=$
$$=\left(2x+3\sqrt[3]{x^2}\right)'=\left(2x+3x^{\frac{2}{3}}\right)'=$$
$$=2+3\cdot\frac{2}{3}x^{-\frac{1}{3}}=2+\frac{2}{x^{\frac{1}{3}}}=\frac{2x^{\frac{1}{3}}+2}{x^{\frac{1}{3}}}\Rightarrow$$
$x=0\in[-2,0]\Rightarrow y'(0)=(-\infty,+\infty)$,
$$2x^{\frac{1}{3}}+2=2\left(x^{\frac{1}{3}}+1\right)=0\Rightarrow x^{\frac{1}{3}}+1=0\Rightarrow$$
$$\Rightarrow x^{\frac{1}{3}}=-1\Rightarrow x=-1\in[-2,0],$$
$y(0)=2\cdot0+3\cdot(0)^{\frac{2}{3}}=0-(\text{MIN}),\quad y(-1)=2\cdot(-1)+3\cdot\sqrt[3]{(-1)^2}=-2+3=+1>0-(\text{MAX}),$
$y(-2)=2\cdot(-2)+3\cdot\sqrt[3]{(-2)^2}=-4+3\sqrt[3]{4}\approx0.76>0,$
"""

SOL6B = r"""
$y=\sqrt[3]{x}=x^{1/3}$
$x_0=8,\ x=9,\quad(x-x_0)=1$
$y'=\frac{1}{3}x^{-\frac{2}{3}},\qquad y'(8)=\frac{1}{12}$
$$y''=-\frac{2}{9}x^{-\frac{5}{3}}=\frac{-2}{9\sqrt[3]{x^5}},\qquad y''(c)=\frac{-2}{9\sqrt[3]{c^5}}$$
$$y(9)=2+\frac{1}{12}+R_1$$
$$|R_1|=\frac{1}{9\sqrt[3]{c^5}}\le\frac{1}{9\sqrt[3]{c^5}}=\frac{1}{288}<0.01$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=2xe^{-\frac{x^2}{2}}$ לפי הסעיפים הבאים:"
      "\nתחום הגדרה, תחומי עליה/ירידה, נקודות קיצון, קמירות ונקודות פיתול, אסימפטוטות. שרטטו את גרף הפונקציה.",
      SOL1, points=20),

    Q(2, "proof", "sequences_limits",
      r"נתונה הסדרה: $a_{n+1}=\frac{a_n}{2}+1,\ a_1=1$." "\nהוכיחו שהסדרה מונוטונית, חסומה ומצאו את גבולה.",
      SOL2A, part="א", points=10),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int\frac{x^3-2x}{x^2+1}\,dx$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "derivatives_tangents",
      r"נתונה הפונקציה $f(x)=\begin{cases}ax^2+x, & x\le1\\ 2x^2-bx, & x>1\end{cases}$"
      "\n" r"מצאו ערכים של $a$ ו-$b$ כך שהפונקציה $f(x)$ תהיה גזירה לכל $x$ ממשי.",
      SOL3A, part="א", points=10),

    Q(3, "proof", "continuity",
      r"הוכיחו שלמשוואה $2x^3-x^2+x+1=0$ קיים פתרון ממשי אחד בקטע $[-3,0]$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "function_limits",
      r"חשבו את הגבול: $\lim_{x\to\infty}\left(\frac{x^2+5x+4}{x^2-3x+7}\right)^{2x}$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"תחום שמוגבל ע״י הקווים $y=0$ ו-$y=\ln x$ בתחום $(1\le x\le e)$ מסתובב סביב ציר ה-$X$. חשבו את נפח של גוף הסיבוב בקטע.",
      SOL4B, part="ב", points=10, confidence="low",
      hold="official-solution-disagrees: V printed as e-2 ~ 0.714, missing the factor pi (and e-2 = 0.718); correct V = pi*(e-2) (sympy)"),

    Q(5, "computation", "derivatives_tangents",
      r"רשמו את משוואת המשיק לגרף של הפונקציה $y=f(x)$ המוגדרת באמצעות משוואה: $y=\pi x\sin\left(\frac{y}{2}\right)$ בנקודה $(1,\pi)$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "function_limits",
      r"חשבו את הגבול: $\lim_{x\to0^+}x^{\frac{1}{\ln(e^x-1)}}$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "extrema_optimization",
      r"מצאו את הערך המקסימלי והערך המינימלי של הפונקציה $y=2x+3\sqrt[3]{x^2}$ בקטע $x\in[-2,0]$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "lhopital_taylor",
      r"באמצעות נוסחת טיילור חשבו בקירוב $\sqrt[3]{9}$ כך ששגיאת החישוב תהיה קטנה מ-$0.01$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "23S-C",
    "examLabel": "מבחן סוף סמסטר קיץ תשפ\"ג, מועד מיוחד",
    "year": 2023,
    "examDate": "05/01/2023",
    "sourceFile": "calculus-1/23S-C exam+solution.pdf",
    "solutionFile": "calculus-1/23S-C exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

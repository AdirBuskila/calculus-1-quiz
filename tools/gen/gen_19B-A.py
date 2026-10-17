# -*- coding: utf-8 -*-
"""Generator for tools/raw/19B-A.json -- calculus-1 (20151), semester A 2019, moed B (27/03/2019).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_19B-A.py

Source: sitting 19B-A, pp.1-7 (typed exam with the official worked solution after every question).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Figures inside solutions: Q1 graph (p.2), Q6a region (p.7), Q6b region (p.7).
- The Q1 solution is the printed text; its sign tables are given in words.

Checks (tools/verify/19B-A/check.py, sympy): every derivative, limit, asymptote, partial-fraction coefficient,
antiderivative, tangent line, volume and area matches the official answer. 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "19B-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
$$f(x)=\frac{2x^2}{x^2-1}=2+\frac{2}{x^2-1}$$
**תחום ההגדרה:** $(-\infty,-1)\cup(-1,1)\cup(1,+\infty)$.
**אסימפטוטה אנכית** $x=1$:
$$\lim_{x\to1^+}\frac{2x^2}{x^2-1}=\left[\frac{2}{0^+}\right]=+\infty,\qquad\lim_{x\to1^-}\frac{2x^2}{x^2-1}=\left[\frac{2}{0^-}\right]=-\infty$$
**אסימפטוטה אנכית** $x=-1$:
$$\lim_{x\to-1^+}\frac{2x^2}{x^2-1}=\left[\frac{2}{0^-}\right]=-\infty,\qquad\lim_{x\to-1^-}\frac{2x^2}{x^2-1}=\left[\frac{2}{0^+}\right]=+\infty$$
**אסימפטוטה אופקית** ב-$+\infty$ וב-$-\infty$: $y=2$:
$$\lim_{x\to\pm\infty}\frac{2x^2}{x^2-1}=\lim_{x\to\pm\infty}\left(2+\frac{2}{x^2-1}\right)=\left[2+\frac{2}{+\infty}\right]=2$$
$$f'(x)=\left(2+\frac{2}{x^2-1}\right)'=\frac{-4x}{\left(x^2-1\right)^2}$$
תחומי עלייה: $(-\infty,-1),(-1,0)$. תחומי ירידה: $(0,1),(1,+\infty)$. נקודת מקסימום מקומי: $x=0$, $f(0)=0$.
$$f''(x)=\left(\frac{-4x}{\left(x^2-1\right)^2}\right)'=\frac{-4\left(x^2-1\right)^2+4x\cdot2\left(x^2-1\right)2x}{\left(x^2-1\right)^4}=\frac{4\left(-x^2+1+4x^2\right)}{\left(x^2-1\right)^3}=\frac{4\left(3x^2+1\right)}{\left(x^2-1\right)^3}$$
קמורה ב: $(-\infty,-1),(1,+\infty)$. קעורה ב: $(-1,1)$. אין נקודת פיתול.
![גרף הפונקציה y = 2x²/(x²−1) עם האסימפטוטות x=1, x=−1, y=2 והמקסימום ב-(0,0)](images/exams/19B-A-Q1-graph.png)
"""

SOL2A = r"""
סדרה $\{a_n\}_{n=1}^\infty$ חסומה מלמטה כי $a_n>3$ לכל $n\in\mathbb{N}$.
הוכחה על ידי אינדוקציה מתמטית: $n=1$: $a_1=4>3$. נניח ש-$a_k>3$. יש להוכיח ש-$a_{k+1}>3$.
$$a_{k+1}=\sqrt{5a_k-6}>\sqrt{5\cdot3-6}=3$$
סדרה $\{a_n\}_{n=1}^\infty$ מונוטונית יורדת:
$$a_{n+1}-a_n=\sqrt{5a_n-6}-a_n=\frac{5a_n-6-a_n^2}{\sqrt{5a_n-6}+a_n}=-\frac{(a_n-2)(a_n-3)}{\sqrt{5a_n-6}+a_n}<0$$
כי $a_n>3$. אז סדרה $\{a_n\}_{n=1}^\infty$ מונוטונית יורדת.
סדרה $\{a_n\}_{n=1}^\infty$ מונוטונית יורדת וחסומה מלמטה, אז $\{a_n\}_{n=1}^\infty$ מתכנסת. ז"א קיים $L\ge3$ כך ש-$L=\lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}a_n$.
$$L=\lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}\sqrt{5a_n-6}=\sqrt{5L-6}\ \Rightarrow\ L=\sqrt{5L-6}$$
$$L^2-5L+6=0,\ L\ge3\ \Rightarrow\ L=3$$
"""

SOL2B = r"""
נניח ש-$f(x)=x^3+x+e^x$, המשוואה $f(x)=0$ היא שקולה למשוואה הנתונה.
$$f(-1)=(-1)^3+(-1)+e^{(-1)}=-2+\frac1e<-2+1=-1<0$$
$$f(0)=0^3+0+e^0=1>0$$
$f(x)$ רציפה ב-$[-1,0]$ ו-$f(-1)\cdot f(0)<0$, אז לפי משפט על ערך הביניים קיים $c\in(-1,0)$ כך ש-$f(c)=0$. ז"א למשוואה הנתונה קיים פתרון $x=c$.
$f'(x)=\left(x^3+x+e^x\right)'=3x^2+1+e^x$. אז $f'(x)>0$ ב-$(-\infty,+\infty)$, ז"א $f(x)$ מונוטונית עולה ממש ב-$(-\infty,+\infty)$. קיבלנו ש-$f(x)$ חח"ע ב-$(-\infty,+\infty)$. אז $f(x)=0$ רק כאשר $x=c$.
ז"א למשוואה הנתונה קיים פתרון אחד בלבד $x=c$.
"""

SOL3A = r"""
$$\lim_{x\to+\infty}\left(1+e^x\right)^{\frac1x}=\left[\infty^0\right]=\lim_{x\to+\infty}e^{\frac1x\ln\left(1+e^x\right)}$$
$$\lim_{x\to+\infty}\frac1x\ln\left(1+e^x\right)=\lim_{x\to+\infty}\frac{\ln\left(1+e^x\right)}{x}=\left[\frac{\infty}{\infty}\right]=\lim_{x\to+\infty}\frac{\left(\ln\left(1+e^x\right)\right)'}{(x)'}=$$
$$=\lim_{x\to+\infty}\frac{\frac{e^x}{1+e^x}}{1}=\lim_{x\to+\infty}\frac{e^x}{1+e^x}=\lim_{x\to+\infty}\frac{1}{e^{-x}+1}=\frac{1}{0+1}=1$$
$$\lim_{x\to+\infty}\left(1+e^x\right)^{\frac1x}=e^1=e$$
"""

SOL3B = r"""
$$\int\arcsin x\,dx=\left[u=\arcsin x,\ v'=1\Rightarrow u'=\frac{1}{\sqrt{1-x^2}},\ v=x\right]=$$
$$=x\arcsin x-\int\frac{x}{\sqrt{1-x^2}}\,dx=x\arcsin x+\frac12\int\frac{\left(1-x^2\right)'}{\sqrt{1-x^2}}\,dx=x\arcsin x+\sqrt{1-x^2}+C$$
"""

SOL4A = r"""
הפונקציה רציפה ב-$x=0$, אם $\lim_{x\to0^-}g(x)=\lim_{x\to0^+}g(x)=g(0)$.
$$\lim_{x\to0^-}g(x)=\lim_{x\to0^-}\left(\ln\left(a+x^2\right)\right)^2=(\ln a)^2,\qquad g(0)=(\ln a)^2$$
$$\lim_{x\to0^+}g(x)=\lim_{x\to0^+}\ln\left(a+e^{-\frac1x}\right)=\ln a$$
$$(\ln a)^2=\ln a\ \Rightarrow\ (\ln a)^2-\ln a=0\ \Rightarrow\ \ln a(\ln a-1)=0$$
ז"א $\ln a=0$ או $\ln a=1$ ז"א $a=1$ או $a=e$.
אם $x\in(-\infty,0)$, $g(x)=\ln^2\left(a+x^2\right)$ רציפה כפונקציה אלמנטרית.
אם $x\in(0,+\infty)$, $g(x)=\ln\left(a+e^{-\frac1x}\right)$ רציפה כפונקציה אלמנטרית.
אז הפונקציה $g(x)$ רציפה ב-$\mathbb{R}$ עבור $a=1$ או $a=e$.
"""

SOL4B = r"""
$$y=1\cdot x-7\ \Rightarrow\ f'(x_0)=1\ \Rightarrow\ \frac{2x_0}{1+x_0^2}=1\ \Rightarrow\ x_0=1,\quad f(1)=\ln2$$
$$y=f(1)+f'(1)(x-1)\ \Rightarrow\ y=\ln2+(x-1)\ \Rightarrow\ y=x+(\ln2-1)$$
משוואת המשיק לגרף של הפונקציה היא $y=x+(\ln2-1)$.
"""

SOL5A = r"""
$$\lim_{x\to-\infty}\left(\sqrt{2+2x+x^2}-\sqrt{2-2x+x^2}\right)=\lim_{x\to-\infty}\frac{2+2x+x^2-2+2x-x^2}{\sqrt{2+2x+x^2}+\sqrt{2-2x+x^2}}=$$
$$=\lim_{x\to-\infty}\frac{4x}{\sqrt{2+2x+x^2}+\sqrt{2-2x+x^2}}=\lim_{x\to-\infty}\frac{4x}{|x|\left(\sqrt{\frac{2}{x^2}+\frac2x+1}+\sqrt{\frac{2}{x^2}-\frac2x+1}\right)}=$$
$$=\lim_{x\to-\infty}\frac{4}{-\left(\sqrt{\frac{2}{x^2}+\frac2x+1}+\sqrt{\frac{2}{x^2}-\frac2x+1}\right)}=\frac{4}{-\left(\sqrt1+\sqrt1\right)}=-2$$
"""

SOL5B = r"""
$$\frac{x}{\left(x^2+1\right)(x+1)}=\frac{A}{x+1}+\frac{Bx+C}{x^2+1}=\frac{A\left(x^2+1\right)+(Bx+C)(x+1)}{\left(x^2+1\right)(x+1)}$$
$$x=A\left(x^2+1\right)+(Bx+C)(x+1)=(A+B)x^2+(B+C)x+(A+C)$$
$$(A+B)=0,\ (B+C)=1,\ (A+C)=0\ \Rightarrow\ A=-\frac12,\ B=\frac12,\ C=\frac12$$
$$\int\frac{x}{\left(x^2+1\right)(x+1)}dx=\int\left(\frac{-\frac12}{x+1}+\frac{\frac12x+\frac12}{x^2+1}\right)dx=$$
$$=-\frac12\int\frac{1}{x+1}dx+\frac14\int\frac{2x}{x^2+1}dx+\frac12\int\frac{1}{x^2+1}dx=-\frac12\ln|x+1|+\frac14\ln\left(x^2+1\right)+\frac12\arctan x+C$$
"""

SOL6A = r"""
$$V=\pi\int_0^{\frac\pi2}\left(\left(\frac\pi2-x\right)^2-(\cos x)^2\right)dx=\pi\int_0^{\frac\pi2}\left(\left(x-\frac\pi2\right)^2-\frac12-\frac12\cos2x\right)dx=$$
$$=\pi\left(-\frac13\left(\frac\pi2-x\right)^3-\frac12x-\frac14\sin2x\right)\Bigg|_0^{\frac\pi2}=\pi\left(-\frac12\cdot\frac\pi2+\frac13\left(\frac\pi2\right)^3\right)=\frac{\pi^2}{4}\left(-1+\frac16\pi^2\right)$$
![התחום הכלוא בין y = cos x לבין הישר y = π/2 − x וציר ה-y, שמסתובב סביב ציר ה-x](images/exams/19B-A-Q6a-fig.png)
"""

SOL6B = r"""
$$S=\int_{-2}^{2}\sqrt{x+2}\,dx-\int_0^2\sqrt{2x}\,dx=\left(\frac23(x+2)^{\frac32}\right)\Bigg|_{-2}^{2}-\sqrt2\left(\frac23(x)^{\frac32}\right)\Bigg|_0^2=$$
$$=\frac23(4)^{\frac32}-\sqrt2\,\frac23(2)^{\frac32}=\frac23(8-4)=\frac83$$
![התחום הכלוא בין y = √(x+2), y = √(2x) וציר ה-x](images/exams/19B-A-Q6b-fig.png)
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $y=\frac{2x^2}{x^2-1}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, נקודות קיצון, "
      "תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1),

    Q(2, "proof", "sequences_limits",
      r"הוכיחו כי הסדרה $a_{n+1}=\sqrt{5a_n-6},\quad a_1=4$ מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "continuity",
      r"הוכח כי למשוואה $x^3+e^x=-x$ קיים פתרון אחד בלבד.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to+\infty}\left(1+e^x\right)^{\frac{1}{x}}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\arcsin x\,dx$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "continuity",
      r"נתונה הפונקציה $g(x)=\begin{cases}\ln\left(a+e^{-\frac1x}\right), & x>0\\[2mm] \ln^2\left(a+x^2\right), & x\le0\end{cases}$"
      r", כאשר $a>0$. עבור אילו ערכי $a$ הפונקציה $g$ רציפה ב-$\mathbb{R}$?",
      SOL4A, part="א", points=10),

    Q(4, "computation", "derivatives_tangents",
      r"מצאו את משוואת המשיק לגרף של הפונקציה $f(x)=\ln\left(1+x^2\right)$ המקביל לישר $x-y=7$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to-\infty}\left(\sqrt{2+2x+x^2}-\sqrt{2-2x+x^2}\right)$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{x}{\left(x^2+1\right)(x+1)}\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "definite_integrals",
      r"מצאו את נפח הגוף, הנוצר על-ידי סיבוב סביב ציר ה-$X$ של התחום הכלוא בין הקווים הבאים: "
      r"$y=\cos x,\ y=\frac\pi2-x$ כאשר $0\le x\le\frac\pi2$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "definite_integrals",
      r"חשבו את השטח הכלוא בין הקווים הבאים: $y=\sqrt{x+2},\ y=\sqrt{2x}$ ו-$y=0$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "19B-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ט, מועד ב'",
    "year": 2019,
    "examDate": "27/03/2019",
    "sourceFile": "calculus-1/19B-A exam+solution.pdf",
    "solutionFile": "calculus-1/19B-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

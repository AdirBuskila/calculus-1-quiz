# -*- coding: utf-8 -*-
"""Generator for tools/raw/19A-A.json -- calculus-1 (20151), semester A 2019, moed A, version 1 (26/02/2019).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_19A-A.py

Source: sitting 19A-A, pp.1-8 (typed exam with the official worked solution after every question; p.1 is the cover).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Figures inside solutions: Q1 graph (p.3), Q6b region (p.8).
- Q4a: the official min value is -(1/5)*540^(1/6); transcribed as printed (checked numerically).
- Q6a: the official cylinder-minus-shells set-up is transcribed as printed (equivalent to 2*pi*int x(2-e^x)).

Checks (tools/verify/19A-A/check.py, sympy + a numeric grid for Q4a): every derivative, limit, asymptote,
extremum, partial-fraction coefficient, antiderivative, tangent line, volume and area matches the official
answer. 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "19A-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
$$f(x)=\frac{e^{-x}}{1-x}=-\frac{1}{e^x(x-1)}$$
**תחום ההגדרה:** $(-\infty,1)\cup(1,+\infty)$.
**אסימפטוטה אנכית** $x=1$:
$$\lim_{x\to1^+}\frac{-1}{e^x(x-1)}=\left[\frac{-1}{0^+}\right]=-\infty,\qquad\lim_{x\to1^-}\frac{-1}{e^x(x-1)}=\left[\frac{-1}{0^-}\right]=+\infty$$
**אסימפטוטה אופקית** ב-$+\infty$: $y=0$:
$$\lim_{x\to+\infty}\frac{-1}{e^x(x-1)}=\left[\frac{-1}{+\infty}\right]=0$$
**אין אסימפטוטה משופעת ב-$-\infty$:**
$$\lim_{x\to-\infty}\frac{f(x)}{x}=\lim_{x\to-\infty}\frac{e^{-x}}{1-x}\cdot\frac1x=\lim_{x\to-\infty}\frac{-e^{-x}}{x(x-1)}=\left[\frac{\infty}{\infty}\right]=\lim_{x\to-\infty}\frac{\left(-e^{-x}\right)'}{\left(x^2-x\right)'}=$$
$$=\lim_{x\to-\infty}\frac{e^{-x}}{2x-1}=\left[\frac{\infty}{\infty}\right]=\lim_{x\to-\infty}\frac{\left(e^{-x}\right)'}{(2x-1)'}=\lim_{x\to-\infty}\frac{-e^{-x}}{2}=-\infty$$
$$f'(x)=\left(-\frac{1}{e^x(x-1)}\right)'=\frac{e^xx}{e^{2x}(x-1)^2}$$
תחומי עלייה: $(0,1),(1,+\infty)$. תחומי ירידה: $(-\infty,0)$. נקודת מינימום מקומי: $x=0$, $f(0)=1$.
$$f''(x)=\left(-\frac{1}{e^x(x-1)}\right)''=\left(\frac{x}{e^x(x-1)^2}\right)'=\frac{e^x(x-1)^2-xe^x(x-1)^2-xe^x2(x-1)}{e^{2x}(x-1)^4}=$$
$$=\frac{(x-1)-x(x-1)-2x}{e^x(x-1)^3}=-\frac{x^2+1}{e^x(x-1)^3}$$
קמורה ב: $(-\infty,1)$. קעורה ב: $(1,+\infty)$. אין נקודת פיתול.
![גרף הפונקציה y = e^(−x)/(1−x) עם האסימפטוטה האנכית x=1, האסימפטוטה y=0 מימין והמינימום ב-(0,1)](images/exams/19A-A-Q1-graph.png)
"""

SOL2A = r"""
$$\sqrt[2n]{7^{2n}}\le\sqrt[2n]{3^n+7^{2n}+\frac{n}{n+1}}\le\sqrt[2n]{7^{2n}+7^{2n}+7^{2n}}$$
$$7\le\sqrt[2n]{3^n+7^{2n}+\frac{n}{n+1}}\le7\cdot\sqrt[2n]{3}$$
$$\lim_{n\to\infty}\sqrt[2n]{3}=1$$
לכן לפי משפט הסנדוויץ'
$$\lim_{n\to\infty}\sqrt[2n]{3^n+7^{2n}+\frac{n}{n+1}}=7$$
"""

SOL2B = r"""
$f(x)=x\ln x$ רציפה ב-$[a,b]$ וגזירה ב-$(a,b)$ כאשר $1\le a<b\le e$. לפי משפט לגרנז' קיים $c\in(a,b)$ כך ש-$f'(c)=\frac{f(b)-f(a)}{b-a}$.
$f'(x)=(x\ln x)'=\ln x+1$, אז מתקיים $\ln c+1=\frac{b\ln b-a\ln a}{b-a}$.
פונקציה $\ln x+1$ מונוטונית עולה ממש ב-$[1,e]$, אז
$$1=\ln1+1\le\ln a+1<\ln c+1<\ln b+1\le\ln e+1=2,$$
ז"א $1\le\frac{b\ln b-a\ln a}{b-a}\le2$.
"""

SOL3A = r"""
$$L=\lim_{x\to0}\left(\frac{4}{1+\sqrt{9+x}}\right)^{\frac{1}{\sin x}}=\left[1^{\infty}\right]=\lim_{x\to0}\left(1+\frac{3-\sqrt{9+x}}{1+\sqrt{9+x}}\right)^{\frac{1+\sqrt{9+x}}{3-\sqrt{9+x}}\cdot\frac{3-\sqrt{9+x}}{1+\sqrt{9+x}}\cdot\frac{1}{\sin x}}$$
$$\lim_{x\to0}\left(1+\frac{3-\sqrt{9+x}}{1+\sqrt{9+x}}\right)^{\frac{1+\sqrt{9+x}}{3-\sqrt{9+x}}}=e,$$
$$\lim_{x\to0}\left(\frac{3-\sqrt{9+x}}{1+\sqrt{9+x}}\right)\frac{1}{\sin x}=\lim_{x\to0}\frac{1}{\left(1+\sqrt{9+x}\right)\left(3+\sqrt{9+x}\right)}\cdot\frac{(-x)}{\sin x}=\frac{1}{4\cdot6}\cdot(-1)=-\frac{1}{24}$$
$$L=e^{\left(-\frac{1}{24}\right)}$$
"""

SOL3B = r"""
$$\int\frac{\tan x}{\cos^2x\cdot e^{2\tan x}}dx=\left|t=\tan x,\ dt=\frac{1}{\cos^2x}dx\right|=\int te^{-2t}dt=\left|u=t,\ v'=e^{-2t}\Rightarrow u'=1,\ v=-\frac12e^{-2t}\right|=$$
$$=-\frac12te^{-2t}+\frac12\int e^{-2t}dt=-\frac12te^{-2t}-\frac14e^{-2t}+C=-\frac12\tan x\,e^{-2\tan x}-\frac14e^{-2\tan x}+C=-\frac{2\tan x+1}{4e^{2\tan x}}+C$$
"""

SOL4A = r"""
$$f'(x)=\left(x\left(x^2-1\right)^{\frac13}\right)'=\left(x^2-1\right)^{\frac13}+x\frac13\left(x^2-1\right)^{-\frac23}2x=\frac{3x^2-3+2x^2}{3\left(x^2-1\right)^{\frac23}}=$$
$$=\frac{5x^2-3}{3\left(x^2-1\right)^{\frac23}}=\frac{5\left(x-\sqrt{\frac35}\right)\left(x+\sqrt{\frac35}\right)}{3(x-1)^{\frac23}(x+1)^{\frac23}}$$
נקודות חשודות לקיצון ב-$(0,3)$ הן $x=1,\ x=\sqrt{\frac35}$.
$$f(1)=1\sqrt[3]{1^2-1}=0,\quad f(3)=3\sqrt[3]{3^2-1}=6,\quad f(0)=0\sqrt[3]{0^2-1}=0,$$
$$f\left(\sqrt{\frac35}\right)=\sqrt{\frac35}\sqrt[3]{\frac35-1}=-\sqrt{\frac35}\sqrt[3]{\frac25}=-\sqrt[6]{\frac{3^3}{5^3}\cdot\frac{2^2}{5^2}}=-\frac15\sqrt[6]{540}$$
אז הערך הגדול ביותר הוא $6$ והערך הקטן ביותר הוא $-\frac15\sqrt[6]{540}$.
"""

SOL4B = r"""
$$f'(x)=\left((x-3)^{\sqrt x}\right)'=\left(e^{\sqrt x\ln(x-3)}\right)'=(x-3)^{\sqrt x}\left(\frac{1}{2\sqrt x}\ln(x-3)+\frac{\sqrt x}{x-3}\right)$$
$$f'(4)=(4-3)^{\sqrt4}\left(\frac{1}{2\sqrt4}\ln(4-3)+\frac{\sqrt4}{4-3}\right)=2$$
$$f(4)=(4-3)^{\sqrt4}=1$$
משוואת המשיק לגרף של הפונקציה היא $y=1+2(x-4)$.
"""

SOL5A = r"""
$$\lim_{x\to+\infty}\frac{1}{\left(\sqrt{2x-1}-\sqrt{2x-3}\right)\sqrt{x+1}}=\lim_{x\to+\infty}\frac{\sqrt{2x-1}+\sqrt{2x-3}}{\left(\sqrt{2x-1}-\sqrt{2x-3}\right)\left(\sqrt{2x-1}+\sqrt{2x-3}\right)\sqrt{x+1}}=$$
$$=\lim_{x\to+\infty}\frac{\sqrt{2x-1}+\sqrt{2x-3}}{(2x-1-2x+3)\sqrt{x+1}}=\lim_{x\to+\infty}\frac{\sqrt{2x-1}+\sqrt{2x-3}}{2\sqrt{x+1}}=$$
$$=\lim_{x\to+\infty}\frac{\sqrt x\left(\sqrt{2-\frac1x}+\sqrt{2-\frac3x}\right)}{\sqrt x\,2\sqrt{1+\frac1x}}=\lim_{x\to+\infty}\frac{\sqrt{2-\frac1x}+\sqrt{2-\frac3x}}{2\sqrt{1+\frac1x}}=\frac{2\sqrt2}{2}=\sqrt2$$
"""

SOL5B = r"""
$$\frac{2x^2-x+1}{(x-1)\left(x^2+1\right)}=\frac{A}{x-1}+\frac{Bx+C}{x^2+1}=\frac{A\left(x^2+1\right)+(Bx+C)(x-1)}{(x-1)\left(x^2+1\right)}$$
$$2x^2-x+1=(A+B)x^2+(-B+C)x+(A-C)$$
$$A=1,\ B=1,\ C=0$$
$$\int\frac{2x^2-x+1}{(x-1)\left(x^2+1\right)}dx=\int\left(\frac{1}{x-1}+\frac{x}{x^2+1}\right)dx=\ln|x-1|+\frac12\ln\left(x^2+1\right)+C$$
"""

SOL6A = r"""
$$V=\pi(\ln2)^2-2\pi\int_0^{\ln2}x\left(e^x-1\right)dx=\pi(\ln2)^2+\pi x^2\Big|_0^{\ln2}-2\pi\int_0^{\ln2}xe^x\,dx=$$
$$=\left|u=x,\ v'=e^x\Rightarrow u'=1,\ v=e^x\right|=2\pi(\ln2)^2-2\pi xe^x\Big|_0^{\ln2}+2\pi\int_0^{\ln2}e^x\,dx=$$
$$=2\pi(\ln2)^2-4\pi\ln2+2\pi e^x\Big|_0^{\ln2}=2\pi(\ln2)^2-4\pi\ln2+4\pi-2\pi=2\pi\left((\ln2)^2-2\ln2+1\right)=2\pi(1-\ln2)^2$$
"""

SOL6B = r"""
![התחום הכלוא בין הישרים y = x, y = x/2 וההיפרבולה y = 1/x](images/exams/19A-A-Q6b-fig.png)
$$S=\int_0^1\left(x-\frac12x\right)dx+\int_1^{\sqrt2}\left(\frac1x-\frac12x\right)dx=\int_0^1\frac12x\,dx+\int_1^{\sqrt2}\frac1x\,dx-\int_1^{\sqrt2}\frac12x\,dx=$$
$$=\frac14x^2\Big|_0^1+\ln|x|\Big|_1^{\sqrt2}-\frac14x^2\Big|_1^{\sqrt2}=\frac14+\ln\sqrt2-\frac12+\frac14=\frac12\ln2$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $y=\frac{e^{-x}}{1-x}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, נקודות קיצון, "
      "תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1),

    Q(2, "computation", "sequences_limits",
      r"חשבו את הגבול $\lim_{n\to\infty}\sqrt[2n]{3^n+7^{2n}+\frac{n}{n+1}}$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "mean_value_theorems",
      r"הוכיחו את אי-השוויון הבא: $1\le\frac{b\ln b-a\ln a}{b-a}\le2$ כאשר $1\le a<b\le e$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\left(\frac{4}{1+\sqrt{9+x}}\right)^{\frac{1}{\sin x}}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\tan x}{\cos^2x\cdot e^{2\tan x}}\,dx$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "extrema_optimization",
      r"חשבו את הערך הגדול ביותר ואת הערך הקטן ביותר של הפונקציה $f(x)=x\sqrt[3]{x^2-1}$ בקטע $[0,3]$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "derivatives_tangents",
      r"מצאו את משוואת המשיק לגרף של הפונקציה $f(x)=(x-3)^{\sqrt{x}}$ בנקודה $x=4$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to+\infty}\frac{1}{\sqrt{2x-1}-\sqrt{2x-3}}\cdot\frac{1}{\sqrt{x+1}}$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{2x^2-x+1}{(x-1)\left(x^2+1\right)}\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "definite_integrals",
      r"מצאו את נפח הגוף, הנוצר על-ידי סיבוב סביב ציר ה-$Y$ של התחום הכלוא בין הקווים הבאים: "
      r"$y=e^x-1,\ y=1,\ x=0$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "definite_integrals",
      r"חשבו את השטח הכלוא בין הקווים הבאים: $y=x,\ y=\frac{x}{2},\ y=\frac1x\ (x>0)$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "19A-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ט, מועד א' (גרסה 1)",
    "year": 2019,
    "examDate": "26/02/2019",
    "sourceFile": "calculus-1/19A-A exam+solution.pdf",
    "solutionFile": "calculus-1/19A-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

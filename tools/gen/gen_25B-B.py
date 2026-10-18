# -*- coding: utf-8 -*-
"""Generator for tools/raw/25B-B.json -- calculus-1 (20151), semester B 2025, moed B (11/08/2025).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_25B-B.py

Source: sitting 25B-B, pp.1-2 (scanned exam only, NO solution or key anywhere). Six questions, 25% each,
solve 4 (Q1 is a single 25% investigation; Q2-Q6 have a 13% and a 12% part).

Solutions: written by the solver (2026-10-18), solutionSource "solved", official False, confidence high. No partial
evidence exists (no key, no tutor marks). Every answer is checked in tools/verify/25B-B/check.py (sympy, 0 mismatches);
the Q1 graph is rendered by tools/verify/25B-B/plot_q1.py (images/exams/25B-B-Q1-graph.png).
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25B-B.json"
SOL = {}


def Q(num, kind, topic, question, part=None, points=None):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": SOL[(num, part)].strip("\n"),
         "solutionSource": "solved", "official": False, "confidence": "high"}
    if part:
        q["part"] = part
    if points:
        q["points"] = points
    return q



SOL[(1, None)] = r"""
**א. תחום הגדרה:** $x\neq2$.
**ב. נקודות חיתוך עם הצירים:** $f(x)=0\iff x=0$ (כי $e^{\frac{1}{x-2}}>0$), ולכן נקודת החיתוך היחידה היא $(0,0)$.
**ג. תחומי עליה וירידה, נקודות קיצון:**
$$f'(x)=e^{\frac{1}{x-2}}+x\cdot e^{\frac{1}{x-2}}\cdot\left(-\frac{1}{(x-2)^2}\right)=e^{\frac{1}{x-2}}\cdot\frac{(x-2)^2-x}{(x-2)^2}=e^{\frac{1}{x-2}}\cdot\frac{(x-1)(x-4)}{(x-2)^2}$$
$f'(x)=0$ עבור $x=1$ ו-$x=4$. טבלת סימן של $f'$: חיובית כאשר $x<1$, שלילית כאשר $1<x<2$ וגם $2<x<4$, וחיובית כאשר $x>4$.
$f$ עולה ב-$(-\infty,1)$ וב-$(4,\infty)$, ויורדת ב-$(1,2)$ וב-$(2,4)$.
נקודת מקסימום מקומי: $\left(1,\frac{1}{e}\right)$. נקודת מינימום מקומי: $\left(4,4\sqrt{e}\right)$.
**ד. תחומי קמירות וקעירות, נקודות פיתול:**
$$f''(x)=e^{\frac{1}{x-2}}\left(-\frac{1}{(x-2)^2}\cdot\frac{x^2-5x+4}{(x-2)^2}+\frac{x+2}{(x-2)^3}\right)=e^{\frac{1}{x-2}}\cdot\frac{(x+2)(x-2)-\left(x^2-5x+4\right)}{(x-2)^4}=e^{\frac{1}{x-2}}\cdot\frac{5x-8}{(x-2)^4}$$
טבלת סימן של $f''$: שלילית כאשר $x<\frac{8}{5}$ (הגרף קעור, $\cap$), חיובית כאשר $\frac{8}{5}<x<2$ וגם $x>2$ (הגרף קמור, $\cup$).
נקודת פיתול: $\left(\frac{8}{5},\frac{8}{5}e^{-\frac{5}{2}}\right)\approx(1.6,\ 0.13)$.
**ה. אסימפטוטות:**
1. אנכית: כאשר $x\to2^+$ מתקיים $\frac{1}{x-2}\to+\infty$ ולכן $\lim_{x\to2^+}f(x)=+\infty$: הישר $x=2$ הוא אסימפטוטה אנכית (מימין). כאשר $x\to2^-$ מתקיים $\frac{1}{x-2}\to-\infty$ ולכן $\lim_{x\to2^-}f(x)=2\cdot0=0$ (הגרף מתקרב לנקודה $(2,0)$ שאינה שייכת לגרף).
2. משופעת $y=ax+b$ ב-$\pm\infty$:
$$a=\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim_{x\to\pm\infty}e^{\frac{1}{x-2}}=e^0=1$$
$$b=\lim_{x\to\pm\infty}\left(f(x)-x\right)=\lim_{x\to\pm\infty}x\left(e^{\frac{1}{x-2}}-1\right)=\lim_{x\to\pm\infty}\frac{e^{\frac{1}{x-2}}-1}{\frac{1}{x-2}}\cdot\frac{x}{x-2}=1\cdot1=1$$
(השתמשנו בגבול $\lim_{u\to0}\frac{e^u-1}{u}=1$ עם $u=\frac{1}{x-2}\to0$.) לכן $y=x+1$ היא אסימפטוטה משופעת ב-$\pm\infty$.
**ו. שרטוט:**
![גרף הפונקציה f(x)=x e^(1/(x-2)): מקסימום ב-(1,1/e), מינימום ב-(4,4√e), פיתול ב-x=8/5, אסימפטוטות x=2 (מימין) ו-y=x+1](images/exams/25B-B-Q1-graph.png)
"""

SOL[(2, "א")] = r"""
**חסימות מלמעלה:** נוכיח באינדוקציה ש-$0<a_n<5$.
בסיס: $a_1=\sqrt{20}<\sqrt{25}=5$.
צעד: אם $0<a_n<5$ אז $a_{n+1}=\sqrt{20+a_n}<\sqrt{20+5}=5$, וכמובן $a_{n+1}>0$.
**מונוטוניות:** הסדרה עולה, כי
$$a_{n+1}>a_n\iff20+a_n>a_n^2\iff a_n^2-a_n-20<0\iff(a_n-5)(a_n+4)<0$$
והאי-שוויון האחרון מתקיים כי $0<a_n<5$.
**הגבול:** הסדרה עולה וחסומה מלמעלה ולכן מתכנסת. נסמן $\lim_{n\to\infty}a_n=L$ ונעבור לגבול בנוסחת הנסיגה:
$$L=\sqrt{20+L}\ \Rightarrow\ L^2-L-20=0\ \Rightarrow\ (L-5)(L+4)=0$$
מכיוון ש-$a_n>0$ מתקיים $L\ge0$, ולכן $L=5$:
$$\lim_{n\to\infty}a_n=5$$
"""

SOL[(2, "ב")] = r"""
אינטגרציה בחלקים עם $u=\arctan x$, $dv=(4x+6)\,dx$. נבחר את הפונקציה הקדומה $v=2x^2+6x+2=2\left(x^2+1\right)+6x$ (מותר להוסיף קבוע ל-$v$, והבחירה הזו מקצרת את החישוב):
$$\int(4x+6)\arctan x\,dx=\left(2x^2+6x+2\right)\arctan x-\int\frac{2\left(x^2+1\right)+6x}{1+x^2}\,dx=$$
$$=\left(2x^2+6x+2\right)\arctan x-\int\left(2+\frac{6x}{1+x^2}\right)dx=\left(2x^2+6x+2\right)\arctan x-2x-3\ln\left(1+x^2\right)+C$$
"""

SOL[(3, "א")] = r"""
זהו גבול מהצורה $\infty^0$. נכתוב
$$\left(\frac{1}{x}\right)^{\tan2x}=e^{\tan2x\cdot\ln\frac{1}{x}}=e^{-\tan2x\cdot\ln x}$$
ונחשב את הגבול של המעריך (צורה $0\cdot\infty$, ואחר כך כלל לופיטל):
$$\lim_{x\to0^+}\tan2x\cdot\ln x=\lim_{x\to0^+}\frac{\ln x}{\cot2x}\left[\frac{\infty}{\infty}\right]=\lim_{x\to0^+}\frac{\frac{1}{x}}{-\frac{2}{\sin^22x}}=\lim_{x\to0^+}\left(-\frac{\sin^22x}{2x}\right)=\lim_{x\to0^+}\left(-\frac{\sin2x}{2x}\cdot\sin2x\right)=-1\cdot0=0$$
לכן
$$\lim_{x\to0^+}\left(\frac{1}{x}\right)^{\tan2x}=e^{0}=1$$
"""

SOL[(3, "ב")] = r"""
בנקודה $x=\frac{\pi}{4}$: $y\left(\frac{\pi}{4}\right)=1^{\frac{\sqrt{2}}{2}}=1$.
גזירה לוגריתמית: $\ln y=\cos x\cdot\ln(\tan x)$, ולכן
$$\frac{y'}{y}=-\sin x\cdot\ln(\tan x)+\cos x\cdot\frac{1}{\tan x}\cdot\frac{1}{\cos^2x}=-\sin x\cdot\ln(\tan x)+\frac{1}{\sin x}$$
$$y'=(\tan x)^{\cos x}\left(\frac{1}{\sin x}-\sin x\cdot\ln(\tan x)\right)$$
$$y'\left(\frac{\pi}{4}\right)=1\cdot\left(\frac{1}{\frac{\sqrt{2}}{2}}-\frac{\sqrt{2}}{2}\cdot\ln1\right)=\sqrt{2}$$
משוואת המשיק:
$$y-1=\sqrt{2}\left(x-\frac{\pi}{4}\right)\quad\Longleftrightarrow\quad y=\sqrt{2}\,x+1-\frac{\sqrt{2}\,\pi}{4}$$
"""

SOL[(4, "א")] = r"""
צורה $\frac{0}{0}$. נכפיל את המונה ואת המכנה בצמודים:
$$\sqrt{x+2}-\sqrt{3x-2}=\frac{(x+2)-(3x-2)}{\sqrt{x+2}+\sqrt{3x-2}}=\frac{2(2-x)}{\sqrt{x+2}+\sqrt{3x-2}}$$
$$\sqrt{4x+1}-\sqrt{5x-1}=\frac{(4x+1)-(5x-1)}{\sqrt{4x+1}+\sqrt{5x-1}}=\frac{2-x}{\sqrt{4x+1}+\sqrt{5x-1}}$$
לכן, אחרי צמצום $2-x\neq0$:
$$\lim_{x\to2}\frac{\sqrt{x+2}-\sqrt{3x-2}}{\sqrt{4x+1}-\sqrt{5x-1}}=\lim_{x\to2}\frac{2\left(\sqrt{4x+1}+\sqrt{5x-1}\right)}{\sqrt{x+2}+\sqrt{3x-2}}=\frac{2(3+3)}{2+2}=3$$
"""

SOL[(4, "ב")] = r"""
משוואת המשיק בנקודה $(2,4)$: $f'(x)=2x$, $f'(2)=4$, ולכן $y-4=4(x-2)$, כלומר $y=4x-4$. המשיק חותך את ציר ה-$X$ ב-$x=1$.
התחום חסום מלמעלה על ידי הפרבולה, ומלמטה על ידי ציר ה-$X$ (עבור $0\le x\le1$) ועל ידי המשיק (עבור $1\le x\le2$). לכן
$$S=\int_0^2x^2\,dx-\int_1^2(4x-4)\,dx=\frac{x^3}{3}\Big|_0^2-\left(2x^2-4x\right)\Big|_1^2=\frac{8}{3}-\left(0-(-2)\right)=\frac{8}{3}-2=\frac{2}{3}$$
(האינטגרל השני הוא שטח המשולש שקודקודיו $(1,0)$, $(2,0)$, $(2,4)$, כלומר $\frac{1\cdot4}{2}=2$.)
"""

SOL[(5, "א")] = r"""
נגדיר $f(x)=e^{\sin^2x}$. הפונקציה רציפה וגזירה בכל $\mathbb{R}$, ו-
$$f'(x)=e^{\sin^2x}\cdot2\sin x\cos x=e^{\sin^2x}\sin2x$$
לפי משפט לגרנז' על הקטע $[a,b]$ קיימת $c\in(a,b)$ כך ש-
$$e^{\sin^2b}-e^{\sin^2a}=f'(c)(b-a)=e^{\sin^2c}\sin2c\cdot(b-a)$$
מכיוון ש-$\sin^2c\le1$ ו-$\sin2c\le1$, מתקיים $e^{\sin^2c}\sin2c\le e^{\sin^2c}\le e$ (אם $\sin2c<0$ המכפלה שלילית וודאי קטנה מ-$e$). מכיוון ש-$b-a>0$:
$$e^{\sin^2b}-e^{\sin^2a}\le e(b-a)$$
"""

SOL[(5, "ב")] = r"""
הצבה $t=\cos x$, $dt=-\sin x\,dx$:
$$\int\frac{\sin x\,dx}{5+2\cos x+\cos^2x}=-\int\frac{dt}{t^2+2t+5}=-\int\frac{dt}{(t+1)^2+4}=-\frac{1}{2}\arctan\frac{t+1}{2}+C=-\frac{1}{2}\arctan\frac{\cos x+1}{2}+C$$
"""

SOL[(6, "א")] = r"""
נקודות החיתוך של חצי המעגל עם הישר: $\sqrt{25-x^2}=3\iff x^2=16\iff x=\pm4$. בקטע $-4\le x\le4$ חצי המעגל נמצא מעל הישר $y=3$.
שיטת הטבעות (דיסקה עם חור):
$$V=\pi\int_{-4}^{4}\left(\left(\sqrt{25-x^2}\right)^2-3^2\right)dx=\pi\int_{-4}^{4}\left(16-x^2\right)dx=2\pi\left(16x-\frac{x^3}{3}\right)\Big|_0^4=2\pi\left(64-\frac{64}{3}\right)=\frac{256\pi}{3}$$
"""

SOL[(6, "ב")] = r"""
**רציפות ב-$x=0$:** $f(0)=\sin0=0$, $\lim_{x\to0^-}\sin(ax)=0$, ו-$\lim_{x\to0^+}x^2\ln x=0$ (לפי לופיטל: $\lim_{x\to0^+}\frac{\ln x}{x^{-2}}=\lim_{x\to0^+}\frac{x^{-1}}{-2x^{-3}}=\lim_{x\to0^+}\left(-\frac{x^2}{2}\right)=0$). לכן $f$ רציפה ב-$0$ לכל $a$.
**נגזרות חד-צדדיות:**
$$f'_-(0)=\lim_{x\to0^-}\frac{\sin(ax)-0}{x}=a$$
(עבור $a\neq0$: $a\cdot\frac{\sin(ax)}{ax}\to a$; עבור $a=0$ המונה זהותית $0$ והגבול $0=a$.)
$$f'_+(0)=\lim_{x\to0^+}\frac{x^2\ln x-0}{x}=\lim_{x\to0^+}x\ln x=0$$
$f$ גזירה ב-$0$ אם ורק אם $f'_-(0)=f'_+(0)$, כלומר $a=0$ (ואז $f'(0)=0$).
"""


questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=x\cdot e^{\frac{1}{x-2}}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, "
      "תחומי עליה וירידה, נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.", points=25),

    Q(2, "proof", "sequences_limits",
      "נתונה הסדרה: " r"$a_1=\sqrt{20}$ ו-$a_{n+1}=\sqrt{20+a_n}$." "\nהוכיחו כי הסדרה מתכנסת וחשבו את גבולה.",
      part="א", points=13),
    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int(4x+6)\arctan x\,dx$.", part="ב", points=12),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0^+}\left(\frac{1}{x}\right)^{\tan 2x}$.", part="א", points=13),
    Q(3, "computation", "derivatives_tangents",
      r"מצאו את משוואת המשיק של גרף הפונקציה: $y=(\tan x)^{\cos x}$ בנקודה $x=\frac{\pi}{4}$.", part="ב", points=12),

    Q(4, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to2}\frac{\sqrt{x+2}-\sqrt{3x-2}}{\sqrt{4x+1}-\sqrt{5x-1}}$.", part="א", points=13),
    Q(4, "computation", "definite_integrals",
      r'חשבו את שטח התחום שחסום ע"י גרף הפונקציה $f(x)=x^2$, הישר המשיק לגרף הפונקציה $f(x)$ בנקודה $(2,4)$ וציר ה-$X$.',
      part="ב", points=12),

    Q(5, "proof", "mean_value_theorems",
      r"הוכיחו כי מתקיים האי שוויון: $e^{\sin^2 b}-e^{\sin^2 a}\le e(b-a)$, עבור $-\infty<a<b<\infty$.",
      part="א", points=13),
    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\sin(x)\,dx}{5+2\cos(x)+\cos^2(x)}$.", part="ב", points=12),

    Q(6, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום הכלוא בין חצי המעגל $y=\sqrt{25-x^2}$ לבין הישר $y=3$ סביב ציר ה-$X$.",
      part="א", points=13),
    Q(6, "computation", "derivatives_tangents",
      r"נתונה הפונקציה $f(x)=\begin{cases}\sin(ax), & x\le0\\ x^2\ln(x), & x>0\end{cases}$ כאשר $a$ הוא פרמטר ממשי. "
      r"עבור אילו ערכי $a$ הפונקציה תהיה גזירה בנקי $x=0$?",
      part="ב", points=12),
]

exam = {
    "examCode": "25B-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ה, מועד ב'",
    "year": 2025,
    "examDate": "11/08/2025",
    "sourceFile": "calculus-1/25B-B exam (scan).pdf",
    "solutionFile": "",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

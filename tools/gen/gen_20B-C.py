# -*- coding: utf-8 -*-
"""Generator for tools/raw/20B-C.json -- calculus-1 (20151), semester C (summer) 2020, moed B (27/10/2020).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_20B-C.py

Source: sitting 20B-C, pp.1-2 (typed exam only, NO solution or key anywhere). The header lists the course as a joint
exam for electrical/electronics engineering AND computer science, so it is in scope. Six questions, 20% each,
Q1 mandatory, choose 4 of Q2-Q6 (a/b parts 10% each).

Transcription fix (2026-10-18, arbiter): the Q3a cases environment had a backslash-space where the double-backslash row break is meant
(the three cases rendered on one row); the printed exam (p.1) shows three rows.

Solutions: written by the solver (2026-10-18), solutionSource "solved", official False, confidence high. No partial
evidence exists (no key, no tutor marks). Every answer is checked in tools/verify/20B-C/check.py (sympy, 0 mismatches).
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20B-C.json"
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
**תחום הגדרה:** $x\neq-1$. נקודת חיתוך עם הצירים: $(0,0)$.
**עליה וירידה, נקודות קיצון:**
$$f'(x)=\frac{3x^2\cdot2(x+1)^2-x^3\cdot4(x+1)}{4(x+1)^4}=\frac{3x^2(x+1)-2x^3}{2(x+1)^3}=\frac{x^2(x+3)}{2(x+1)^3}$$
$f'(x)=0$ עבור $x=-3$ ו-$x=0$. טבלת סימן של $f'$: חיובית כאשר $x<-3$, שלילית כאשר $-3<x<-1$, חיובית כאשר $-1<x<0$ וגם $x>0$ (ב-$x=0$ הנגזרת מתאפסת בלי להחליף סימן).
$f$ עולה ב-$(-\infty,-3)$ וב-$(-1,\infty)$, ויורדת ב-$(-3,-1)$.
נקודת מקסימום מקומי: $\left(-3,-\frac{27}{8}\right)$. ב-$x=0$ אין קיצון.
**קמירות ונקודות פיתול:** נכתוב $x^3=(x+1)^3-3(x+1)^2+3(x+1)-1$, ולכן
$$f(x)=\frac{1}{2}\left((x+1)-3+\frac{3}{x+1}-\frac{1}{(x+1)^2}\right)\ \Rightarrow\ f''(x)=\frac{1}{2}\left(\frac{6}{(x+1)^3}-\frac{6}{(x+1)^4}\right)=\frac{3x}{(x+1)^4}$$
טבלת סימן של $f''$: שלילית כאשר $x<-1$ וגם $-1<x<0$ (הגרף קעור, $\cap$), חיובית כאשר $x>0$ (הגרף קמור, $\cup$).
נקודת פיתול: $(0,0)$ (שם גם $f'(0)=0$: משיק אופקי בנקודת הפיתול).
**אסימפטוטות:**
1. אנכית $x=-1$: המונה שואף ל-$-1$ והמכנה ל-$0^+$, ולכן $\lim_{x\to-1^\pm}f(x)=-\infty$.
2. משופעת: מהפירוק שלמעלה, $f(x)=\frac{x}{2}-1+\frac{3x+2}{2(x+1)^2}$, והשבר האחרון שואף ל-$0$ כאשר $x\to\pm\infty$. כלומר
$$a=\lim_{x\to\pm\infty}\frac{f(x)}{x}=\frac{1}{2},\qquad b=\lim_{x\to\pm\infty}\left(f(x)-\frac{x}{2}\right)=-1$$
והישר $y=\frac{x}{2}-1$ הוא אסימפטוטה משופעת ב-$\pm\infty$.
**שרטוט:**
![גרף הפונקציה f(x)=x^3/(2(x+1)^2): מקסימום ב-(-3,-27/8), פיתול ב-(0,0), אסימפטוטות x=-1 ו-y=x/2-1](images/exams/20B-C-Q1-graph.png)
"""

SOL[(2, "א")] = r"""
נבחין בשלושה מקרים:
**$0<b<3$:** נחלק ב-$3^n$: $\frac{3^n}{3^n+b^n}=\frac{1}{1+\left(\frac{b}{3}\right)^n}\to\frac{1}{1+0}=1$, כי $0<\frac{b}{3}<1$.
**$b=3$:** $\frac{3^n}{3^n+3^n}=\frac{1}{2}$ לכל $n$, והגבול $\frac{1}{2}$.
**$b>3$:** נחלק ב-$b^n$: $\frac{3^n}{3^n+b^n}=\frac{\left(\frac{3}{b}\right)^n}{\left(\frac{3}{b}\right)^n+1}\to\frac{0}{0+1}=0$, כי $0<\frac{3}{b}<1$.
$$\lim_{n\to\infty}\frac{3^n}{3^n+b^n}=\begin{cases}1, & 0<b<3\\ \frac{1}{2}, & b=3\\ 0, & b>3\end{cases}$$
"""

SOL[(2, "ב")] = r"""
חילוק פולינומים: $x^3+2x+5=x\left(x^2-1\right)+3x+5$, ולכן $\frac{x^3+2x+5}{x^2-1}=x+\frac{3x+5}{(x-1)(x+1)}$.
פירוק לשברים חלקיים: $\frac{3x+5}{(x-1)(x+1)}=\frac{A}{x-1}+\frac{B}{x+1}$, כלומר $3x+5=A(x+1)+B(x-1)$.
$x=1$: $8=2A\Rightarrow A=4$. $x=-1$: $2=-2B\Rightarrow B=-1$.
$$\int\frac{x^3+2x+5}{x^2-1}\,dx=\int\left(x+\frac{4}{x-1}-\frac{1}{x+1}\right)dx=\frac{x^2}{2}+4\ln|x-1|-\ln|x+1|+C$$
"""

SOL[(3, "א")] = r"""
נחשב את הגבולות החד-צדדיים ב-$x=0$ ונשווה ל-$f(0)=\frac{1}{2}$.
$$\lim_{x\to0^-}\frac{e^x-1}{\sin2x}=\lim_{x\to0^-}\frac{e^x-1}{x}\cdot\frac{2x}{\sin2x}\cdot\frac{1}{2}=1\cdot1\cdot\frac{1}{2}=\frac{1}{2}$$
$$\lim_{x\to0^+}\left(x\ln x+\frac{\arcsin x}{2x}\right)=0+\frac{1}{2}\cdot1=\frac{1}{2}$$
כאן $\lim_{x\to0^+}x\ln x=\lim_{x\to0^+}\frac{\ln x}{\frac{1}{x}}=\lim_{x\to0^+}\frac{\frac{1}{x}}{-\frac{1}{x^2}}=\lim_{x\to0^+}(-x)=0$ (לופיטל), ו-$\lim_{x\to0}\frac{\arcsin x}{x}=\lim_{x\to0}\frac{\frac{1}{\sqrt{1-x^2}}}{1}=1$.
שני הגבולות החד-צדדיים שווים ל-$\frac{1}{2}=f(0)$, ולכן **הפונקציה רציפה ב-$x=0$**.
"""

SOL[(3, "ב")] = r"""
$f$ רציפה בקטע הסגור $[0,4]$ (שם $18-x^2>0$), ולכן מקבלת בו מקסימום ומינימום.
$$f'(x)=\sqrt{18-x^2}+x\cdot\frac{-2x}{2\sqrt{18-x^2}}=\frac{18-2x^2}{\sqrt{18-x^2}}$$
$f'(x)=0\iff x^2=9$, ובקטע: $x=3$.
ערכי הפונקציה בנקודה החשודה ובקצוות:
$$f(0)=0,\qquad f(3)=3\sqrt{9}=9,\qquad f(4)=4\sqrt{2}\approx5.66$$
הערך המקסימלי הוא $9$ (ב-$x=3$) והערך המינימלי הוא $0$ (ב-$x=0$).
"""

SOL[(4, "א")] = r"""
אינטגרציה בחלקים עם $u=\ln^2x$, $dv=dx$: $du=\frac{2\ln x}{x}dx$, $v=x$.
$$\int\ln^2x\,dx=x\ln^2x-2\int\ln x\,dx$$
ושוב בחלקים ($u=\ln x$, $dv=dx$): $\int\ln x\,dx=x\ln x-\int x\cdot\frac{1}{x}dx=x\ln x-x$. לכן
$$\int\ln^2x\,dx=x\ln^2x-2x\ln x+2x+C$$
"""

SOL[(4, "ב")] = r"""
צורה $\frac{0}{0}$. נכפיל בצמוד:
$$\frac{\sqrt{3x-2}-\sqrt{x+2}}{x^2-4}=\frac{(3x-2)-(x+2)}{(x-2)(x+2)\left(\sqrt{3x-2}+\sqrt{x+2}\right)}=\frac{2(x-2)}{(x-2)(x+2)\left(\sqrt{3x-2}+\sqrt{x+2}\right)}$$
$$\lim_{x\to2}\frac{\sqrt{3x-2}-\sqrt{x+2}}{x^2-4}=\lim_{x\to2}\frac{2}{(x+2)\left(\sqrt{3x-2}+\sqrt{x+2}\right)}=\frac{2}{4\cdot(2+2)}=\frac{1}{8}$$
"""

SOL[(5, "א")] = r"""
עבור $x\in[-1,1]$ מתקיים $0\le x^4\le1$, ולכן $1\le2x^4+1\le3$ ו-
$$\frac{1}{3}\le\frac{1}{2x^4+1}\le1$$
לפי תכונת המונוטוניות של האינטגרל המסוים (אורך הקטע $2$):
$$\frac{1}{3}\cdot2\le\int_{-1}^{1}\frac{dx}{2x^4+1}\le1\cdot2\quad\Longrightarrow\quad\frac{2}{3}\le\int_{-1}^{1}\frac{dx}{2x^4+1}\le2$$
"""

SOL[(5, "ב")] = r"""
המונה $\int_0^x\frac{t^2}{1+t^4}dt$ והמכנה $x^3$ שואפים ל-$0$, והמונה גזיר לפי המשפט היסודי. לפי כלל לופיטל:
$$\lim_{x\to0}\frac{\int_0^x\frac{t^2}{1+t^4}\,dt}{x^3}=\lim_{x\to0}\frac{\frac{x^2}{1+x^4}}{3x^2}=\lim_{x\to0}\frac{1}{3\left(1+x^4\right)}=\frac{1}{3}$$
"""

SOL[(6, "א")] = r"""
קירוב לינארי: $\tan(x_0+\Delta x)\approx\tan x_0+dy$, כאשר $dy=\frac{1}{\cos^2x_0}\,\Delta x$.
$x_0=\frac{\pi}{4}=45^\circ$, $\Delta x=3^\circ=\frac{3\pi}{180}=\frac{\pi}{60}$ (ברדיאנים!), $\tan\frac{\pi}{4}=1$, $\frac{1}{\cos^2\frac{\pi}{4}}=2$.
$$\tan48^\circ\approx1+2\cdot\frac{\pi}{60}=1+\frac{\pi}{30}\approx1.1047$$
(לשם השוואה, $\tan48^\circ=1.1106\ldots$)
"""

SOL[(6, "ב")] = r"""
נקודות החיתוך ברביע הראשון: $2x=\frac{1}{x}\Rightarrow x=\frac{1}{\sqrt{2}}$ (הנקודה $\left(\frac{1}{\sqrt{2}},\sqrt{2}\right)$), ו-$\frac{x}{2}=\frac{1}{x}\Rightarrow x=\sqrt{2}$ (הנקודה $\left(\sqrt{2},\frac{1}{\sqrt{2}}\right)$). שני הישרים נחתכים בראשית.
התחום חסום מלמטה על ידי $y=\frac{x}{2}$, ומלמעלה על ידי $y=2x$ (עבור $0\le x\le\frac{1}{\sqrt{2}}$) ועל ידי $y=\frac{1}{x}$ (עבור $\frac{1}{\sqrt{2}}\le x\le\sqrt{2}$):
$$S=\int_0^{1/\sqrt{2}}\left(2x-\frac{x}{2}\right)dx+\int_{1/\sqrt{2}}^{\sqrt{2}}\left(\frac{1}{x}-\frac{x}{2}\right)dx=\frac{3x^2}{4}\Big|_0^{1/\sqrt{2}}+\left(\ln x-\frac{x^2}{4}\right)\Big|_{1/\sqrt{2}}^{\sqrt{2}}=$$
$$=\frac{3}{8}+\left(\ln\sqrt{2}-\ln\frac{1}{\sqrt{2}}\right)-\left(\frac{2}{4}-\frac{1}{8}\right)=\frac{3}{8}+\ln2-\frac{3}{8}=\ln2$$
הערה: ברביע השלישי יש תחום סימטרי (סימטריה ביחס לראשית) עם אותו שטח $\ln2$; התשובה המקובלת לשאלה היא שטח התחום האחד, $\ln2$.
"""


questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=\frac{x^3}{2(x+1)^2}$ לפי הסעיפים הבאים: תחום הגדרה, תחומי עליה/ירידה, נקודות קיצון, "
      "קמירות ונקודות פיתול, אסימפטוטות. שרטטו את גרף הפונקציה.", points=20),

    Q(2, "computation", "sequences_limits",
      r"חשבו את גבול הסדרה $\lim_{n\to\infty}\frac{3^n}{3^n+b^n}$, כאשר $b>0$ הוא פרמטר ממשי.",
      part="א", points=10),
    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{x^3+2x+5}{x^2-1}\,dx$.", part="ב", points=10),

    Q(3, "computation", "continuity",
      "האם הפונקציה\n"
      r"$$f(x)=\begin{cases}\frac{e^x-1}{\sin 2x}, & x<0\\ \frac{1}{2}, & x=0\\ x\cdot\ln x+\frac{\arcsin x}{2x}, & x>0\end{cases}$$"
      "\n" r"רציפה ב-$x=0$?", part="א", points=10),
    Q(3, "computation", "extrema_optimization",
      r"מצאו את הערך המקסימלי ואת הערך המינימלי של הפונקציה $f(x)=x\sqrt{18-x^2}$ בקטע $[0,4]$.",
      part="ב", points=10),

    Q(4, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\ln^2 x\,dx$.", part="א", points=10),
    Q(4, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to2}\frac{\sqrt{3x-2}-\sqrt{x+2}}{x^2-4}$.", part="ב", points=10),

    Q(5, "proof", "definite_integrals",
      r"הוכיחו את אי-השוויון הבא: $\frac{2}{3}\le\int_{-1}^{1}\frac{1}{2x^4+1}\,dx\le2$.", part="א", points=10),
    Q(5, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to0}\frac{1}{x^3}\int_0^x\frac{t^2}{1+t^4}\,dt$.", part="ב", points=10),

    Q(6, "computation", "derivatives_tangents",
      r"בעזרת דיפרנציאל של הפונקציה $y=\tan x$ בנקודה $x=\frac{\pi}{4}$ חשבו בקירוב את $\tan 48^\circ$.",
      part="א", points=10),
    Q(6, "computation", "definite_integrals",
      r"חשבו את השטח הכלוא בין הקווים $y=2x,\quad y=\frac{x}{2},\quad y=\frac{1}{x}$.", part="ב", points=10),
]

exam = {
    "examCode": "20B-C",
    "examLabel": "מבחן סוף סמסטר קיץ תש\"פ, מועד ב'",
    "year": 2020,
    "examDate": "27/10/2020",
    "sourceFile": "calculus-1/20B-C exam.pdf",
    "solutionFile": "",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

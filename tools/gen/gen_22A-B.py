# -*- coding: utf-8 -*-
"""Generator for tools/raw/22A-B.json -- calculus-1 (20151), semester B 2022, moed A (14/06/2022).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22A-B.py

Source: sitting 22A-B, pp.1-10. The file is a worked-solution document titled "solution of moed A 14.06.2022": it carries NO
printed exam header; each question is restated by its author, followed by the solution (typeset, with some hand-drawn sign
tables and a few black handwritten additions in Q6a). The question texts below are the restatements from that file, so
the wording is the file's, not the printed exam's. The author is not identified and the file has no institute header,
so it is shipped as solutionSource student-solution with official False (the triage note listing this sitting as having
no solution was wrong: a full worked solution exists).

Transcription notes
- Q1: restated only as "function investigation f(x)=x^3/(x^2-1)"; the standard task list is written out in the question.
  Points are not printed. The two hand-drawn sign tables (f' and f'') are described in words; the plotted graph on p.3
  is shipped as images/exams/22A-B-Q1-graph.png.
- Q1d: the file prints 'x f''(x)=' before the formula (stray x) and a red cross next to it; the formula itself is correct
  (sympy), transcribed as f''(x).
- Q1e: the slope limit is printed as lim (x^2-1)/x^2 = 1; f(x)/x is x^2/(x^2-1) (also tends to 1); written with the
  correct fraction.
- Q4b: the part label is printed 'a' (copy of Q4a's label); it is the second part of Q4, stored as part ב. The hand-drawn
  region sketch is shipped as images/exams/22A-B-Q4b-sketch.png.
- Q5b: the file's value 1.98 does not match the exact value of the arc-length integral (2.0035, sympy); the
  closed form is right, the decimal evaluation at the end is off. Final-answer error -> labeled fix (the source is not
  official, so the label reads "הפתרון שבמקור (לא רשמי) עם תיקון"), solutionSource solved, official False.
- Blind re-check 2026-10-18 (tools/verify/22A-B/blind_recheck.py): every final answer re-derived independently; all agree
  except Q5b above.
- Q6a: black handwriting added x=1/3 (where f' does not exist) and f(1/3)=0 to the typeset solution; transcribed.

Checks (tools/verify/22A-B/check.py, sympy plus numeric): every derivative, sign table, limit, antiderivative, extremum,
volume and parameter value matches the file's answers; the only disagreement is the Q5b decimal.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22A-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "student-solution", "official": False, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**א. תחום הגדרה:** $D=\{x\in\mathbb{R},\ x\neq\pm1\}$.
**ב. נקודת חיתוך עם צירי הקואורדינטות:** $(0,0)$.
**ג.** $$f'(x)=\frac{3x^2\left(x^2-1\right)-2x^4}{\left(x^2-1\right)^2}=\frac{x^4-3x^2}{\left(x^2-1\right)^2}=\frac{x^2\left(x^2-3\right)}{\left(x^2-1\right)^2}$$ והנקודות הקריטיות של הפונקציה הן $x=0,\ x=\pm\sqrt{3}$.
טבלת סימן של $f'$: חיובית כאשר $x<-\sqrt{3}$, שלילית כאשר $-\sqrt{3}<x<0$ וגם כאשר $0<x<\sqrt{3}$, וחיובית כאשר $x>\sqrt{3}$ (בתחום ההגדרה).
**סיכום:** $f(x)$ עולה כאשר $x<-\sqrt{3}$ וגם $x>\sqrt{3}$, ו-$f(x)$ יורדת כאשר $-\sqrt{3}<x<\sqrt{3}$. הנקודה $x=-\sqrt{3}$ היא נקודת מקסימום מקומי כך ש-$f(-\sqrt{3})=-\frac{3\sqrt{3}}{2}$, והנקודה $x=\sqrt{3}$ היא נקודת מינימום מקומי כך ש-$f(\sqrt{3})=\frac{3\sqrt{3}}{2}$.
**ד.** $$f''(x)=\frac{\left(4x^3-6x\right)\left(x^2-1\right)^2-2\left(x^4-3x^2\right)\left(x^2-1\right)2x}{\left(x^2-1\right)^4}=\frac{\left(4x^3-6x\right)\left(x^2-1\right)-2\left(x^4-3x^2\right)2x}{\left(x^2-1\right)^3}=\frac{2x^3+6x}{\left(x^2-1\right)^3}$$
טבלת סימן של $f''$: שלילית כאשר $x<-1$, חיובית כאשר $-1<x<0$, שלילית כאשר $0<x<1$, וחיובית כאשר $x>1$.
**סיכום:** $f(x)$ קמורה כאשר $x<-1$ וגם $0<x<1$. $f(x)$ קעורה כאשר $x>1$ וגם $-1<x<0$. הנקודה $x=0$ היא נקודת פיתול.
**ה.** הישרים $x=\pm1$ מהווים אסימפטוטות אנכיות לגרף הפונקציה, כך ש-$\lim_{x\to-1^-}f(x)=-\infty$ ו-$\lim_{x\to-1^+}f(x)=\infty$, וכן $\lim_{x\to1^-}f(x)=-\infty$ ו-$\lim_{x\to1^+}f(x)=\infty$.
בנוסף לזאת,
$$k=\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim_{x\to\pm\infty}\frac{x^2}{x^2-1}=1,\qquad m=\lim_{x\to\pm\infty}\left(f(x)-x\right)=0$$
והתוצאה מכך היא ש-$y=x$ היא אסימפטוטה משופעת לגרף הפונקציה ב-$\pm\infty$.
**ו. שרטוט:**
![גרף הפונקציה עם האסימפטוטות x=1, x=-1 ו-y=x](images/exams/22A-B-Q1-graph.png)
"""

SOL2A = r"""
השערה: $a_1=5,\ a_2=3,\ a_3=2.3\ldots$ הסדרה יורדת וחסומה מלרע. אם זה נכון, אז הסדרה מתכנסת וגבולה מקיים את המשוואה (על פניו הסדרה חיובית):
$$L=\frac{1}{2}\left(L+\frac{5}{L}\right),\qquad L=\sqrt{5},\ L^2=5$$
במקרה זה $L=\sqrt{5}$ הוא החסם התחתון של הסדרה.
נוכיח באינדוקציה שהסדרה באמת חסומה מלרע על ידי $\sqrt{5}$.
בסיס האינדוקציה: $a_1=5>\sqrt{5}$.
שלב האינדוקציה: נניח ש-$a_n>\sqrt{5}$, בפרט $a_n$ חיובי וניתן להשתמש באי-שוויון הממוצעים:
$$a_{n+1}=\frac{1}{2}\left(a_n+\frac{5}{a_n}\right)\ge\sqrt{a_n\cdot\frac{5}{a_n}}=\sqrt{5}$$
נותר להראות שהסדרה מונוטונית יורדת. נקבל:
$$\frac{a_{n+1}}{a_n}=\frac{1}{2}\left(1+\frac{5}{a_n^2}\right)<\frac{1}{2}\left(1+\frac{5}{5}\right)=1$$
כלומר הסדרה יורדת. לפי חישוב העזר שעשינו מקודם, $L=\sqrt{5}$.
"""

SOL2B = r"""
$$\int x\arctan\frac{2}{x}\,dx=\left\{u=\arctan\frac{2}{x},\ du=\frac{-\frac{2}{x^2}}{1+\frac{4}{x^2}}dx,\ dv=x\,dx,\ v=\frac{x^2}{2}\right\}=$$
$$=\frac{x^2}{2}\arctan\frac{2}{x}+\int\frac{\frac{2}{x^2}\cdot\frac{x^2}{2}}{1+\frac{4}{x^2}}dx=\frac{x^2}{2}\arctan\frac{2}{x}+\int\frac{x^2+4-4}{x^2+4}dx=$$
$$=\frac{x^2}{2}\arctan\frac{2}{x}+x-2\arctan\frac{x}{2}+c$$
"""

SOL3A = r"""
נגדיר את הפונקציה החדשה $f(x)=\ln(x+1)-\frac{3x+2}{x+2}$. הפונקציה רציפה וגזירה לכל $x>-1$, כפונקציה אלמנטרית ומוגדרת בתחום.
$$f(0)=-1<0,\qquad \lim_{x\to+\infty}f(x)=+\infty>0$$
לפי משפט ערך הביניים של קושי קיימת נקודה $c\in(0,+\infty)$ כך ש-$f(c)=0$.
נבדוק את הסימן של נגזרת:
$$f'(x)=\frac{1}{x+1}-\frac{4}{(x+2)^2}=\frac{(x+2)^2-4x-4}{(x+1)(x+2)^2}=\frac{x^2}{(x+1)(x+2)^2}>0$$
הפונקציה מונוטונית עולה, לכן הפתרון הוא יחיד.
"""

SOL3B = r"""
$$\int\frac{\cos x\,dx}{\left(3-\cos^2x\right)(3-\sin x)}=\int\frac{\cos x\,dx}{\left(2+\sin^2x\right)(3-\sin x)}\ \left\{\begin{array}{l}t=\sin x\\ dt=\cos x\,dx\end{array}\right\}=\int\frac{dt}{\left(2+t^2\right)(3-t)}$$
נחפש את הפירוק מן הצורה:
$$\frac{1}{\left(2+t^2\right)(3-t)}=\frac{At+B}{t^2+2}+\frac{C}{3-t}$$
נמצא את המקדמים של השברים: $1=(At+B)(3-t)+C\left(t^2+2\right)$.
$$t=3:\ 1=11C\Rightarrow C=\frac{1}{11}$$
$$t^2:\ 0=-A+C\Rightarrow A=C=\frac{1}{11}$$
$$t:\ 0=3A-B\Rightarrow B=3A=\frac{3}{11}$$
$$\int\frac{dt}{\left(2+t^2\right)(3-t)}=\frac{1}{11}\int\frac{t+3}{t^2+2}dt+\frac{1}{11}\int\frac{dt}{3-t}=\frac{1}{22}\int\frac{2t\,dt}{t^2+2}+\frac{3}{11}\int\frac{dt}{t^2+2}+\frac{1}{11}\int\frac{dt}{3-t}=$$
$$=\frac{1}{22}\ln\left(t^2+2\right)+\frac{3}{11\sqrt{2}}\arctan\frac{t}{\sqrt{2}}-\frac{1}{11}\ln|3-t|+C=$$
$$=\frac{1}{22}\ln\left(\sin^2x+2\right)+\frac{3}{11\sqrt{2}}\arctan\frac{\sin x}{\sqrt{2}}-\frac{1}{11}\ln|3-\sin x|+C$$
"""

SOL4A = r"""
תחום ההגדרה: $x\neq0,1$. נקודות האי-רציפות הן $0,1$.
$x=0$:
$$\lim_{x\to0^-}y=\lim_{x\to0^-}\frac{e^{\frac{x}{1-x}}}{1-e^{\frac{x}{1-x}}}=\frac{e^{\frac{0}{1-0}}}{1-e^{\frac{0}{1-0}}}=\frac{1}{0(+)}=\infty$$
$$\lim_{x\to0^+}y=\lim_{x\to0^+}\frac{e^{\frac{x}{1-x}}}{1-e^{\frac{x}{1-x}}}=\frac{e^{\frac{0}{1-0}}}{1-e^{\frac{0}{1-0}}}=\frac{1}{0(-)}=-\infty$$
$0$ היא אי-רציפות מהסוג השני.
$x=1$:
$$\lim_{x\to1^-}y=\lim_{x\to1^-}\frac{e^{\frac{x}{1-x}}}{1-e^{\frac{x}{1-x}}}=\frac{e^{\frac{1}{0(+)}}}{1-e^{\frac{1}{0(+)}}}=\frac{e^{\infty}}{1-e^{\infty}}=\frac{\infty}{-\infty}=\left[t=e^{\frac{x}{1-x}}\to\infty\right]=\lim_{t\to\infty}\frac{t}{1-t}=-1$$
$$\lim_{x\to1^+}y=\lim_{x\to1^+}\frac{e^{\frac{x}{1-x}}}{1-e^{\frac{x}{1-x}}}=\frac{e^{\frac{1}{0(-)}}}{1-e^{\frac{1}{0(-)}}}=\frac{e^{-\infty}}{1-e^{-\infty}}=\frac{0}{1-0}=0$$
$\lim_{x\to1^-}y\neq\lim_{x\to1^+}y$, לכן $1$ היא אי-רציפות מהסוג הראשון.
"""

SOL4B = r"""
![התחום הכלוא בין הגרף לציר ה-x](images/exams/22A-B-Q4b-sketch.png)
נשתמש בשיטת הקליפה:
$$V=2\pi\int_{\frac{\pi}{2}}^{\pi}x\cos^2x\,dx=\pi\int_{\frac{\pi}{2}}^{\pi}x\left(\cos(2x)+1\right)dx=\pi\left(\int_{\frac{\pi}{2}}^{\pi}x\cos(2x)\,dx+\int_{\frac{\pi}{2}}^{\pi}x\,dx\right)=$$
$$=\left|\begin{array}{ll}u=x & du=dx\\ dv=\cos(2x)\,dx & v=\frac{1}{2}\sin(2x)\end{array}\right|=$$
$$=\pi\left(\frac{1}{2}x\sin(2x)\Big|_{\frac{\pi}{2}}^{\pi}-\frac{1}{2}\int_{\frac{\pi}{2}}^{\pi}\sin(2x)\,dx+\frac{x^2}{2}\Big|_{\frac{\pi}{2}}^{\pi}\right)$$
$$=\pi\left(\frac{1}{2}\pi\sin(2\pi)-\frac{1}{2}\cdot\frac{\pi}{2}\sin(\pi)+\frac{1}{4}\cos(2x)\Big|_{\frac{\pi}{2}}^{\pi}+\frac{1}{2}\left(\pi^2-\frac{\pi^2}{4}\right)\right)$$
$$=\pi\left(\frac{1}{4}\left(\cos(2\pi)-\cos(\pi)\right)+\frac{3}{8}\pi^2\right)=\pi\left(\frac{1}{2}+\frac{3}{8}\pi^2\right)=\frac{\pi}{2}\left(1+\frac{3}{4}\pi^2\right)$$
"""

SOL5A = r"""
ניקח $x>0$. לפי משפט לגרנז', קיימת $c\in(0,x)$ כך שלפונקציה $f(x)=\ln(1+x)$ מקבלים:
$$\frac{f(x)-f(0)}{x-0}=\frac{\ln(1+x)}{x}=f'(c)=\frac{1}{1+c}$$
מכיוון ש-$0<c<x$, נובע מכך ש-
$$1<1+c<1+x\ \Longrightarrow\ \frac{1}{1+x}<\frac{1}{1+c}<1$$
זה אומר ש-
$$\frac{1}{1+x}<\frac{\ln(1+x)}{x}<\frac{1}{1+c}<1$$
ומכיוון ש-$x>0$ נקבל ש-
$$\frac{x}{1+x}<\ln(1+x)<x$$
"""

SOL5B = r"""
**הפתרון שבמקור (לא רשמי) עם תיקון:** הביטוי הסגור בפתרון נכון, אבל בהצבה המספרית בסוף עוגל $\sqrt{1+e^2}$ ל-$2.9$ והתקבל $1.98$. הערך הנכון של האינטגרל הוא $L\approx2.0035\approx2.00$. השורה המספרית האחרונה מתוקנת. התיקון נבדק (sympy).
$$L=\int_0^1\sqrt{1+\left(\left(e^x\right)'\right)^2}\cdot dx=\int_0^1\sqrt{1+e^{2x}}\cdot dx=$$
$$=\left[t=\sqrt{1+e^{2x}},\ dt=\frac{2e^{2x}}{2\sqrt{1+e^{2x}}}dx=\frac{t^2-1}{t}dx,\ dx=\frac{t}{t^2-1}dt;\quad x=0\Rightarrow t=\sqrt{2},\ x=1\Rightarrow t=\sqrt{1+e^2}\right]=$$
$$=\int_{\sqrt{2}}^{\sqrt{1+e^2}}t\cdot\frac{t}{t^2-1}dt=\int_{\sqrt{2}}^{\sqrt{1+e^2}}\frac{t^2}{t^2-1}dt=\int_{\sqrt{2}}^{\sqrt{1+e^2}}\left(1+\frac{1}{t^2-1}\right)dt=$$
$$=\left(t+\frac{1}{2}\ln\left|\frac{t-1}{t+1}\right|\right)\Bigg|_{\sqrt{2}}^{\sqrt{1+e^2}}=\left(\sqrt{1+e^2}+\frac{1}{2}\ln\left|\frac{\sqrt{1+e^2}-1}{\sqrt{1+e^2}+1}\right|\right)-\left(\sqrt{2}+\frac{1}{2}\ln\left|\frac{\sqrt{2}-1}{\sqrt{2}+1}\right|\right)=$$
$$\approx\left(2.8964-0.3600\right)-\left(1.4142-0.8814\right)=2.5363-0.5328\approx2.00$$
"""

SOL6A = r"""
$$f'(x)=\sqrt[3]{3x-1}+x\cdot\frac{1}{3}(3x-1)^{-2/3}\cdot3=(3x-1)^{1/3}+\frac{x}{(3x-1)^{2/3}}=\frac{4x-1}{(3x-1)^{2/3}}$$
$$f'(x)=0\iff x=\frac{1}{4}\in\left(-1,\frac{2}{3}\right)$$
וגם $x=\frac{1}{3}\in\left[-1,\frac{2}{3}\right]$ (שם הנגזרת אינה קיימת).
$$f\left(\frac{1}{4}\right)=\frac{1}{4}\sqrt[3]{\frac{3}{4}-1}=-\left(\frac{1}{4}\right)^{4/3},\qquad f\left(\frac{1}{3}\right)=0$$
$$f(-1)=-\sqrt[3]{-3-1}=\sqrt[3]{4},\qquad f\left(\frac{2}{3}\right)=\frac{2}{3}$$
הערך הגדול ביותר הוא: $\sqrt[3]{4}$.
הערך הקטן ביותר הוא: $-\left(\frac{1}{4}\right)^{4/3}$.
"""

SOL6B = r"""
$$\lim_{x\to2^+}f(x)=\lim_{x\to2^+}\left(x^2+b\right)=4+b$$
$$\lim_{x\to2^-}f(x)=\lim_{x\to2^-}ax^3=8a$$
$$f(2)=8a=4+b$$
$$f_+'(2)=\lim_{\Delta x\to0^+}\frac{f(2+\Delta x)-f(2)}{\Delta x}=\lim_{\Delta x\to0^+}\frac{(2+\Delta x)^2+b-8a}{\Delta x}$$
$$\lim_{\Delta x\to0^+}\frac{(2+\Delta x)^2-4}{\Delta x}=\lim_{\Delta x\to0^+}\frac{4\Delta x+\Delta x^2}{\Delta x}=\lim_{\Delta x\to0^+}(4+\Delta x)=4$$
$$f_-'(2)=\lim_{\Delta x\to0^-}\frac{f(2+\Delta x)-f(2)}{\Delta x}=\lim_{\Delta x\to0^-}\frac{a(2+\Delta x)^3-8a}{\Delta x}=$$
$$\lim_{\Delta x\to0^-}\frac{12a\Delta x+6a\Delta x^2+a\Delta x^3}{\Delta x}=\lim_{\Delta x\to0^-}\left(12a+6a\Delta x+a\Delta x^2\right)=12a$$
נקבל $8a=4+b$ ו-$12a=4\Rightarrow a=\frac{1}{3}$, ולכן $b=-\frac{4}{3}$.
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=\frac{x^3}{x^2-1}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, "
      "תחומי עליה וירידה ונקודות קיצון, תחומי קמירות וקעירות ונקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1),

    Q(2, "proof", "sequences_limits",
      r"הוכיחו כי הסדרה הבאה מתכנסת ומצאו את גבולה: $a_1=5,\ a_{n+1}=\frac{1}{2}\left(a_n+\frac{5}{a_n}\right)$.",
      SOL2A, part="א"),
    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int x\arctan\frac{2}{x}\,dx$.",
      SOL2B, part="ב"),

    Q(3, "proof", "continuity",
      r"הוכיחו כי למשוואה $\ln(x+1)-\frac{3x+2}{x+2}=0$ יש פתרון יחיד.",
      SOL3A, part="א", points=10),
    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\cos x\,dx}{\left(3-\cos^2x\right)(3-\sin x)}$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "continuity",
      r"מצאו את הנקודות האי-רציפות של הפונקציה הבאה וסווגו אותן: $y=\frac{e^{\frac{x}{1-x}}}{1-e^{\frac{x}{1-x}}}$.",
      SOL4A, part="א", points=10),
    Q(4, "computation", "definite_integrals",
      r"חשבו את נפח הגוף, הנוצר על ידי סיבוב סביב ציר ה-$y$ של התחום הכלוא בין הקווים הבאים: "
      r"$y=\cos^2x,\ y=0$ כאשר $\frac{\pi}{2}\le x\le\pi$.",
      SOL4B, part="ב"),

    Q(5, "proof", "mean_value_theorems",
      r"הוכיחו את האי-שוויון $\frac{x}{x+1}<\ln(1+x)<x$, כאשר $x>0$.",
      SOL5A, part="א", points=10),
    Q(5, "computation", "definite_integrals",
      r"חשבו את אורך הקשת של העקומה $y=e^x$ בקטע $0\le x\le1$.",
      SOL5B, part="ב", solutionSource="solved", official=False),

    Q(6, "computation", "extrema_optimization",
      r"מצאו את הערך הגדול ביותר ואת הערך הקטן ביותר של הפונקציה $f(x)=x\cdot\sqrt[3]{3x-1}$ בקטע $-1\le x\le\frac{2}{3}$.",
      SOL6A, part="א", points=10),
    Q(6, "computation", "derivatives_tangents",
      r"נתונה הפונקציה $f(x)=\begin{cases}ax^3, & x\le2\\ x^2+b, & x>2\end{cases}$ כאשר $a$ ו-$b$ פרמטרים ממשיים. "
      r"מצאו את כל הערכים של $a$ ו-$b$ כך ש-$f(x)$ תהיה גזירה בנקודה $x=2$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "22A-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ב, מועד א'",
    "year": 2022,
    "examDate": "14/06/2022",
    "sourceFile": "calculus-1/22A-B solution.pdf",
    "solutionFile": "calculus-1/22A-B solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

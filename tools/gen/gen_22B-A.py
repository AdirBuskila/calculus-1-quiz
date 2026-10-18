# -*- coding: utf-8 -*-
"""Generator for tools/raw/22B-A.json -- calculus-1 (20151), semester A 2022, moed B (22/02/2022).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22B-A.py

Source: sitting 22B-A, pp.1-2 (printed exam only, NO solution or key anywhere). Six questions, 20% each (two parts of
10%), solve 5 of 6. Parameters A, B, C (last three digits of the student's ID) appear in some parts; the header rule is
shipped as context c0.

Solutions: written by the solver (2026-10-18), solutionSource "solved", official False, confidence high. No partial
evidence exists (no key, no tutor marks). Every answer is checked in tools/verify/22B-A/check.py (sympy, 0 mismatches).
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22B-A.json"
SOL = {}


def Q(num, kind, topic, question, part=None, points=10, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "points": points, "solution": SOL[(num, part)].strip("\n"),
         "solutionSource": "solved", "official": False, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


CTX0 = (r"בחלק מסעיפי המבחן מופיעים הפרמטרים $A$, $B$ ו-$C$. חובה להציב בתחילת הפתרון לכל שאלה את ערכי הפרמטרים, "
        r"בהתאם לשלוש הספרות האחרונות של מספר תעודת הזהות שלכם: למשל עבור ת.ז. 123456789 נקבל $A=7$, $B=8$, $C=9$. "
        r"שאלות בהן $A$, $B$ ו-$C$ יוצבו רק בשלב התשובה הסופית לא ייבדקו.")


PARAM = r"הפתרון כתוב באופן כללי עבור הפרמטרים $A,B,C\in\{0,1,\dots,9\}$; במבחן מציבים אותם כבר בתחילת הפתרון." + "\n"

SOL[(1, "א")] = r"""
תחום ההגדרה: כל $\mathbb{R}$. עבור $x\neq0$:
$$f'(x)=2+3\cdot\frac{2}{3}x^{-\frac{1}{3}}=2+\frac{2}{\sqrt[3]{x}}=\frac{2\left(\sqrt[3]{x}+1\right)}{\sqrt[3]{x}}$$
נקודות חשודות לקיצון: $f'(x)=0\iff\sqrt[3]{x}=-1\iff x=-1$, ו-$x=0$ שבה הנגזרת אינה קיימת (הפונקציה רציפה שם).
טבלת סימן של $f'$:
$x<-1$: $\sqrt[3]{x}<-1$, המונה שלילי והמכנה שלילי, $f'>0$ (עולה).
$-1<x<0$: המונה חיובי והמכנה שלילי, $f'<0$ (יורדת).
$x>0$: $f'>0$ (עולה).
לכן $x=-1$ היא נקודת מקסימום מקומי, $f(-1)=-2+3=1$, ו-$x=0$ היא נקודת מינימום מקומי, $f(0)=0$ (נקודת חוד, הנגזרת אינה קיימת בה).
"""

SOL[(1, "ב")] = PARAM + r"""
נפשט את השבר באמצעות $(n+2)!=(n+2)(n+1)!$ ו-$(n+1)!=(n+1)\cdot n!$:
$$\frac{(n+2)!+(A+1)\,n\,(n+1)!}{(n+1)!-n\cdot n!}=\frac{(n+1)!\left[(n+2)+(A+1)n\right]}{n!\left[(n+1)-n\right]}=(n+1)\left((A+2)n+2\right)$$
כאשר $n\to\infty$ מתקיים $\frac{C+1}{(n+1)^2}\to0$, ולכן $\sin\frac{C+1}{(n+1)^2}=\frac{C+1}{(n+1)^2}\cdot\frac{\sin u_n}{u_n}$ עם $u_n=\frac{C+1}{(n+1)^2}$ ו-$\frac{\sin u_n}{u_n}\to1$:
$$\lim_{n\to\infty}(n+1)\left((A+2)n+2\right)\cdot\frac{C+1}{(n+1)^2}\cdot\frac{\sin u_n}{u_n}=(C+1)\lim_{n\to\infty}\frac{(A+2)n+2}{n+1}\cdot1=(A+2)(C+1)$$
"""

SOL[(2, "א")] = r"""
יהי $x>0$. הפונקציה $g(t)=\arctan t$ רציפה ב-$[0,x]$ וגזירה ב-$(0,x)$, $g'(t)=\frac{1}{1+t^2}$. לפי משפט לגרנז' קיימת $c\in(0,x)$ כך ש-
$$\arctan x-\arctan0=\frac{1}{1+c^2}\cdot x\quad\Longrightarrow\quad\arctan x=\frac{x}{1+c^2}$$
מכיוון ש-$0<c<x$ מתקיים $1<1+c^2<1+x^2$, ולכן $\frac{1}{1+x^2}<\frac{1}{1+c^2}<1$. נכפיל ב-$x>0$:
$$\frac{x}{1+x^2}<\frac{x}{1+c^2}=\arctan x<x$$
"""

SOL[(2, "ב")] = PARAM + r"""
נסמן $k=B+2\ge2$. אז $a_{n+1}=\frac{(k+1)a_n}{ka_n+1}$ ו-$a_1=C+2\ge2$.
**חסימות מלמטה:** נוכיח באינדוקציה ש-$a_n>1$. בסיס: $a_1\ge2>1$. צעד: אם $a_n>1$ אז
$$a_{n+1}-1=\frac{(k+1)a_n-ka_n-1}{ka_n+1}=\frac{a_n-1}{ka_n+1}>0$$
**מונוטוניות:** לכל $n$
$$a_{n+1}-a_n=\frac{(k+1)a_n-ka_n^2-a_n}{ka_n+1}=\frac{ka_n\left(1-a_n\right)}{ka_n+1}<0$$
כי $a_n>1$. לכן הסדרה יורדת וחסומה מלמטה, ולכן מתכנסת.
**הגבול:** נסמן $L=\lim a_n$ ונעבור לגבול בנוסחת הנסיגה:
$$L=\frac{(k+1)L}{kL+1}\ \Rightarrow\ kL^2+L=(k+1)L\ \Rightarrow\ kL(L-1)=0$$
כלומר $L=0$ או $L=1$.
מכיוון ש-$a_n>1$ לכל $n$, מתקיים $L\ge1$, ולכן $\lim_{n\to\infty}a_n=1$ (לכל ערך של $B$ ו-$C$).
"""

SOL[(3, "א")] = PARAM + r"""
תחום ההגדרה: $x\neq-A$.
**אסימפטוטה אנכית:** כאשר $x\to-A$ הגורם $x+A\to0$, והסוגריים חסומים: $1\le2+\cos\frac{B+1}{x+A}\le3$. לכן $\lim_{x\to-A}f(x)=0$ (מכפלה של שואפת ל-$0$ בחסומה), ואין אסימפטוטה אנכית.
**אסימפטוטה משופעת** $y=ax+b$ ב-$\pm\infty$: כאשר $x\to\pm\infty$, $u=\frac{B+1}{x+A}\to0$.
$$a=\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim_{x\to\pm\infty}\frac{x+A}{x}\left(2+\cos u\right)=1\cdot(2+1)=3$$
$$b=\lim_{x\to\pm\infty}\left(f(x)-3x\right)=\lim_{x\to\pm\infty}\left[(x+A)\left(\cos u-1\right)+3(x+A)-3x\right]=\lim_{x\to\pm\infty}(x+A)\left(\cos u-1\right)+3A$$
ומכיוון ש-$1-\cos u=2\sin^2\frac{u}{2}$:
$$(x+A)\left(\cos u-1\right)=-(x+A)\cdot2\sin^2\frac{u}{2}=-(B+1)\cdot\frac{\sin\frac{u}{2}}{\frac{u}{2}}\cdot\sin\frac{u}{2}\ \xrightarrow[x\to\pm\infty]{}\ -(B+1)\cdot1\cdot0=0$$
לכן $b=3A$, והישר $y=3x+3A$ הוא אסימפטוטה משופעת ב-$\pm\infty$. אין אסימפטוטות נוספות.
"""

SOL[(3, "ב")] = r"""
הצבה אוניברסלית $t=\tan\frac{x}{2}$: $\sin x=\frac{2t}{1+t^2}$, $\cos x=\frac{1-t^2}{1+t^2}$, $dx=\frac{2\,dt}{1+t^2}$.
$$1+\sin x+3\cos x=\frac{1+t^2+2t+3-3t^2}{1+t^2}=\frac{2\left(2+t-t^2\right)}{1+t^2}=\frac{2(2-t)(1+t)}{1+t^2}$$
$$\int\frac{dx}{1+\sin x+3\cos x}=\int\frac{dt}{(2-t)(1+t)}=\frac{1}{3}\int\left(\frac{1}{2-t}+\frac{1}{1+t}\right)dt=\frac{1}{3}\left(\ln|1+t|-\ln|2-t|\right)+C=$$
$$=\frac{1}{3}\ln\left|\frac{1+\tan\frac{x}{2}}{2-\tan\frac{x}{2}}\right|+C$$
"""

SOL[(4, "א")] = PARAM + r"""
נגדיר $g(x)=x^3+(C+1)x+\cos\left((C+1)x\right)-(B+1)$, רציפה וגזירה בכל $\mathbb{R}$.
**קיום:** $\cos$ חסומה, ולכן $\lim_{x\to+\infty}g(x)=+\infty$ ו-$\lim_{x\to-\infty}g(x)=-\infty$. מכאן קיימים $x_1<x_2$ עם $g(x_1)<0<g(x_2)$, ולפי משפט ערך הביניים קיים $c\in(x_1,x_2)$ עם $g(c)=0$.
**יחידות:**
$$g'(x)=3x^2+(C+1)-(C+1)\sin\left((C+1)x\right)=3x^2+(C+1)\left(1-\sin\left((C+1)x\right)\right)\ge0$$
ושוויון $g'(x)=0$ דורש גם $x=0$ וגם $\sin\left((C+1)x\right)=1$, אבל $\sin0=0$. לכן $g'(x)>0$ לכל $x$, $g$ עולה ממש, ויש לה לכל היותר שורש אחד. בסך הכל למשוואה שורש ממשי אחד בלבד.
"""

SOL[(4, "ב")] = r"""
הצבה $t=\arctan\sqrt{x}$ (עבור $x>0$): $dt=\frac{1}{1+x}\cdot\frac{1}{2\sqrt{x}}\,dx$, כלומר $\frac{dx}{(x+1)\sqrt{x}}=2\,dt$.
$$\int\frac{\arctan^3\left(\sqrt{x}\right)}{(x+1)\sqrt{x}}\,dx=\int t^3\cdot2\,dt=\frac{t^4}{2}+C=\frac{1}{2}\arctan^4\left(\sqrt{x}\right)+C$$
"""

SOL[(5, "א")] = PARAM + r"""
נסמן $D=C+1>0$. נכפיל פעמיים בצמוד:
$$\sqrt{x^2+\sqrt{x^4+D}}-x\sqrt{2}=\frac{x^2+\sqrt{x^4+D}-2x^2}{\sqrt{x^2+\sqrt{x^4+D}}+x\sqrt{2}}=\frac{\sqrt{x^4+D}-x^2}{\sqrt{x^2+\sqrt{x^4+D}}+x\sqrt{2}}=$$
$$=\frac{D}{\left(\sqrt{x^4+D}+x^2\right)\left(\sqrt{x^2+\sqrt{x^4+D}}+x\sqrt{2}\right)}$$
נחלק מונה ומכנה ב-$x^3$:
$$\lim_{x\to+\infty}\frac{\left(x^3+A\right)D}{\left(\sqrt{x^4+D}+x^2\right)\left(\sqrt{x^2+\sqrt{x^4+D}}+x\sqrt{2}\right)}=\lim_{x\to+\infty}\frac{\left(1+\frac{A}{x^3}\right)D}{\left(\sqrt{1+\frac{D}{x^4}}+1\right)\left(\sqrt{1+\sqrt{1+\frac{D}{x^4}}}+\sqrt{2}\right)}=\frac{D}{2\cdot2\sqrt{2}}$$
$$\lim_{x\to+\infty}\left(x^3+A\right)\left(\sqrt{x^2+\sqrt{x^4+C+1}}-x\sqrt{2}\right)=\frac{C+1}{4\sqrt{2}}=\frac{\sqrt{2}\,(C+1)}{8}$$
(הגבול אינו תלוי ב-$A$.)
"""

SOL[(5, "ב")] = r"""
$y'=\frac{\cos x}{\sin x}=\cot x$, ולכן $1+(y')^2=1+\cot^2x=\frac{1}{\sin^2x}$, ובקטע $\left[\frac{\pi}{3},\frac{\pi}{2}\right]$ מתקיים $\sin x>0$:
$$L=\int_{\pi/3}^{\pi/2}\frac{dx}{\sin x}=\ln\left|\tan\frac{x}{2}\right|\Big|_{\pi/3}^{\pi/2}=\ln\tan\frac{\pi}{4}-\ln\tan\frac{\pi}{6}=0-\ln\frac{1}{\sqrt{3}}=\frac{1}{2}\ln3$$
"""

SOL[(6, "א")] = r"""
תנאי הכרחי לגזירות הוא רציפות ב-$0$. עבור $x\neq0$: $f(x)=\frac{1}{\sin x}-\frac{1}{x}=\frac{x-\sin x}{x\sin x}$.
$$\lim_{x\to0}\frac{x-\sin x}{x\sin x}\left[\frac{0}{0}\right]=\lim_{x\to0}\frac{1-\cos x}{\sin x+x\cos x}\left[\frac{0}{0}\right]=\lim_{x\to0}\frac{\sin x}{2\cos x-x\sin x}=\frac{0}{2}=0$$
לכן חייב להתקיים $p=0$. עם $p=0$:
$$f'(0)=\lim_{x\to0}\frac{f(x)-0}{x}=\lim_{x\to0}\frac{x-\sin x}{x^2\sin x}=\lim_{x\to0}\frac{x-\sin x}{x^3}\cdot\frac{x}{\sin x}$$
$$\lim_{x\to0}\frac{x-\sin x}{x^3}\left[\frac{0}{0}\right]=\lim_{x\to0}\frac{1-\cos x}{3x^2}=\lim_{x\to0}\frac{2\sin^2\frac{x}{2}}{3x^2}=\frac{2}{3}\cdot\frac{1}{4}=\frac{1}{6}$$
ולכן $f$ גזירה ב-$0$ עבור $p=0$, ו-$f'(0)=\frac{1}{6}$.
"""

SOL[(6, "ב")] = PARAM + r"""
נסמן $k=B+1$. התחום הוא $0\le x\le\frac{\pi}{k}$, $0\le y\le\sin^2(kx)$, והוא מסתובב סביב ציר ה-$y$. בשיטת הקליפות הגליליות:
$$V=2\pi\int_0^{\pi/k}x\sin^2(kx)\,dx=\left[u=kx,\ dx=\frac{du}{k}\right]=\frac{2\pi}{k^2}\int_0^{\pi}u\sin^2u\,du$$
$$\int_0^{\pi}u\sin^2u\,du=\int_0^{\pi}\frac{u}{2}\,du-\frac{1}{2}\int_0^{\pi}u\cos2u\,du=\frac{\pi^2}{4}-\frac{1}{2}\left(\frac{u\sin2u}{2}\Big|_0^{\pi}-\int_0^{\pi}\frac{\sin2u}{2}\,du\right)=\frac{\pi^2}{4}-\frac{1}{2}\left(0+\frac{\cos2u}{4}\Big|_0^{\pi}\right)=\frac{\pi^2}{4}$$
$$V=\frac{2\pi}{k^2}\cdot\frac{\pi^2}{4}=\frac{\pi^3}{2(B+1)^2}$$
"""


questions = [
    Q(1, "computation", "extrema_optimization",
      r"מצאו ומיינו את כל הנקודות החשודות לקיצון מקומי של הפונקציה $f(x)=2x+3\sqrt[3]{x^2}$.", part="א"),
    Q(1, "computation", "sequences_limits",
      r"חשבו את הגבול $\lim_{n\to\infty}\frac{(n+2)!+(A+1)\,n\,(n+1)!}{(n+1)!-n\cdot n!}\sin\frac{C+1}{(n+1)^2}$.",
      part="ב", contextId="c0"),

    Q(2, "proof", "mean_value_theorems",
      r"הראו כי לכל $x>0$ מתקיים האי-שוויון $\frac{x}{1+x^2}<\arctan x<x$.", part="א"),
    Q(2, "proof", "sequences_limits",
      r"הוכיחו כי הסדרה $a_{n+1}=\frac{(B+3)a_n}{(B+2)a_n+1},\ a_1=C+2$ מתכנסת וחשבו את גבולה.",
      part="ב", contextId="c0"),

    Q(3, "computation", "function_limits",
      r"מצאו את כל האסימפטוטות לגרף הפונקציה $f(x)=(x+A)\left(2+\cos\frac{B+1}{x+A}\right)$.",
      part="א", contextId="c0"),
    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{dx}{1+\sin x+3\cos x}$.", part="ב"),

    Q(4, "proof", "continuity",
      r"הוכיחו כי למשוואה $x^3+(C+1)x+\cos\left((C+1)x\right)=B+1$ קיים שורש ממשי אחד בלבד.",
      part="א", contextId="c0"),
    Q(4, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{\arctan^3\left(\sqrt{x}\right)}{(x+1)\sqrt{x}}\,dx$.", part="ב"),

    Q(5, "computation", "function_limits",
      r"חשבו את הגבול: $\lim_{x\to+\infty}\left(x^3+A\right)\left(\sqrt{x^2+\sqrt{x^4+C+1}}-x\sqrt{2}\right)$.",
      part="א", contextId="c0"),
    Q(5, "computation", "definite_integrals",
      r"חשבו את אורך הקשת של העקומה $y=\ln(\sin x)$ בקטע $\left[\frac{\pi}{3},\frac{\pi}{2}\right]$.", part="ב"),

    Q(6, "computation", "derivatives_tangents",
      r"תהיה $f(x)=\begin{cases}\frac{1}{\sin x}-\frac{1}{x}, & x\neq0\\ p, & x=0\end{cases}$. "
      r"מצאו ערך פרמטר ממשי $p$ כך שפונקציה $f$ תהיה גזירה ב-$x=0$. מהו $f'(0)$?", part="א"),
    Q(6, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום המישורי הכלוא בין הקווים: "
      r"$y=\sin^2\left((B+1)x\right),\ y=0,\ x=0,\ x=\frac{\pi}{B+1}$ סביב ציר ה-$y$.",
      part="ב", contextId="c0"),
]

exam = {
    "examCode": "22B-A",
    "examLabel": "מבחן סוף סמסטר א' תשפ\"ב, מועד ב'",
    "year": 2022,
    "examDate": "22/02/2022",
    "sourceFile": "calculus-1/22B-A exam.pdf",
    "solutionFile": "",
    "contexts": {"c0": {"kind": "text", "title": "הפרמטרים A, B, C", "text": CTX0}},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

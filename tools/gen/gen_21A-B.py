# -*- coding: utf-8 -*-
"""Generator for tools/raw/21A-B.json -- calculus-1 (20151), semester B 2021 (תשפ"א), moed A.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_21A-B.py

Source: sitting 21A-B, pp.1-11 (image-only PDF "פתרון המבחן": question stem plus worked solution for every question;
there is no separate printed exam). Part A (mandatory): Q1 (20%). Part B: Q2-Q6, a/b parts.
Pages 1-6 and 8-11 are typed/printed solutions; Q4b (pp.7-8) is a HANDWRITTEN page (stem + solution) of unknown
author, inserted in place of a printed solution. Both source trees hold the identical file.

Transcription notes
- Q1 plot (p.2), Q4b sketches (p.7) and the Q6b region sketch (p.10) are shipped as figures inside the solutions.
- Q3b: the stem on the page is only the words "חשב את האינטגרל"; the integrand is taken from the first line of the
  solution (the integral of (x+1)arctan x).
- Q4a: the official proof divides by a2, i.e. assumes a2 != 0; transcribed as printed.
- Q4b (handwritten): the set-up (washers about x=4, radii, the two integrals) is correct and transcribed, but the
  handwritten arithmetic is wrong: it reaches pi(1184 - 224*sqrt(2)/3) = 3387.9, while sympy (washers AND shells)
  gives 128*pi = 402.1. Final-answer error -> "הפתרון ... עם תיקון" label, solutionSource solved, official False,
  and an ASK_ADIR entry. The antiderivative of 8*sqrt(y) - y is printed with "+ y^2/2"; written here with the
  correct "-" (intermediate slip, logged).
- Q6b: the printed first line lists x=+-1/sqrt2 and x=+-sqrt18 and restricts to x>=0; transcribed as printed.

Checks (tools/verify/21A-B/check.py, sympy): every derivative, limit, extremum, parameter, integral and area matches
the official answer, except the Q4b final value described above. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "21A-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**I.** $x^3-1=(x-1)(x^2+x+1)$, $D(f)=\{x\in\mathbb{R}:x\neq1\}$,
$$\lim_{x\to1^+}f(x)=\lim_{x\to1^+}\frac{x^4}{x^3-1}=+\infty,\qquad \lim_{x\to1^-}f(x)=\lim_{x\to1^-}\frac{x^4}{x^3-1}=-\infty$$
לכן $x=1$ נקודת אי-רציפות מסוג שני. $x=1$ הוא אסימפטוטה אנכית,
$$a=\lim_{x\to\infty}\frac{f(x)}{x}=\lim_{x\to\infty}\frac{x^3}{x^3-1}=1,\qquad b=\lim_{x\to\infty}\left(f(x)-ax\right)=\lim_{x\to\infty}\left(\frac{x^4}{x^3-1}-x\right)=\lim_{x\to\infty}\frac{x}{x^3-1}=0$$
$y=x$ הוא אסימפטוטה משופעת.
תחום ההגדרה אינו סימטרי ביחס ל-$0$ לכן הפונקציה אינה זוגית ואינה אי-זוגית.
**II.**
$$f'(x)=\frac{4x^3(x^3-1)-x^4\cdot3x^2}{(x^3-1)^2}=\frac{x^6-4x^3}{(x^3-1)^2}=\frac{x^3(x^3-4)}{(x^3-1)^2}$$
$f'(x)=0$ כאשר $x=0$ או $x=\sqrt[3]{4}$.
טבלת סימנים של $f'$: חיובית ב-$x<0$ (עולה), שלילית ב-$0<x<1$ (יורדת), שלילית ב-$1<x<\sqrt[3]{4}$ (יורדת), חיובית ב-$x>\sqrt[3]{4}$ (עולה).
הנקודה $x=\sqrt[3]{4}$ היא נקודת מינימום מקומי ו-$f\left(\sqrt[3]{4}\right)=\frac{4\sqrt[3]{4}}{3}$.
הנקודה $x=0$ היא נקודת מקסימום מקומי ו-$f(0)=0$.
**III.**
$$f''(x)=\left(\frac{x^6-4x^3}{(x^3-1)^2}\right)'=\frac{(6x^5-12x^2)(x^3-1)^2-(x^6-4x^3)\cdot2(x^3-1)\cdot3x^2}{(x^3-1)^4}=$$
$$=\frac{(6x^5-12x^2)(x^3-1)-(x^6-4x^3)6x^2}{(x^3-1)^3}=\frac{6x^5+12x^2}{(x^3-1)^3}=\frac{6x^2(x^3+2)}{(x^3-1)^3}$$
$6x^2(x^3+2)=0$ כאשר $x=-\sqrt[3]{2}$ או $x=0$.
טבלת סימנים של $f''$: חיובית ב-$x<-\sqrt[3]{2}$ (קמורה), שלילית ב-$-\sqrt[3]{2}<x<0$ וב-$0<x<1$ (קעורה), חיובית ב-$x>1$ (קמורה).
הנקודה $\left(-\sqrt[3]{2},-\frac{2\sqrt[3]{2}}{3}\right)$ היא נקודת הפיתול של הפונקציה, $f\left(-\sqrt[3]{2}\right)=-\frac{2\sqrt[3]{2}}{3}$.
![גרף הפונקציה f(x)=x^4/(x^3-1) עם האסימפטוטה האנכית x=1 והאסימפטוטה המשופעת y=x (מקווקוות)](images/exams/21A-B-Q1-graph.png)
"""

SOL2A = r"""
$$\lim_{x\to+\infty}\left(\frac{x^3}{x^2-x+2}+ax+b\right)=\lim_{x\to+\infty}\left(\frac{x^3+ax^3-ax^2+2ax+bx^2-bx+2b}{x^2-x+2}\right)=$$
$$\lim_{x\to+\infty}\left(\frac{(a+1)x^3+(b-a)x^2+(2a-b)x+2b}{x^2-x+2}\right)\ \{a=-1\}\ \left[\frac{\infty}{\infty}\right]=$$
$$=\lim_{x\to+\infty}\left(\frac{(b-a)+\frac{2a-b}{x}+\frac{2b}{x^2}}{1-\frac{1}{x}+\frac{2}{x^2}}\right)=0$$
לכן $a=b=-1$
"""

SOL2B = r"""
$$\lim_{x\to3^{\pm}}\frac{x|x-3|}{(x^2-4x+3)\arcsin\left(\frac{x}{5}\right)}=\lim_{x\to3^{\pm}}\frac{\pm x(x-3)}{(x-3)(x-1)\arcsin\left(\frac{x}{5}\right)}=$$
$$\lim_{x\to3^{\pm}}\frac{\pm x}{(x-1)\arcsin\left(\frac{x}{5}\right)}=\pm\frac{3}{2\arcsin\frac{3}{5}}$$
**נקודה $x=3$ הינה נקודת אי-רציפות מסוג הראשון.**
$$\lim_{x\to1^{\pm}}\frac{x|x-3|}{(x^2-4x+3)\arcsin\left(\frac{x}{5}\right)}=\lim_{x\to1^{\pm}}\frac{x|x-3|}{(x-3)(x-1)\arcsin\left(\frac{x}{5}\right)}=\mp\infty$$
**נקודה $x=1$ הינה נקודת אי-רציפות מסוג השני.**
$$\lim_{x\to0^{\pm}}\frac{x|x-3|}{(x^2-4x+3)\arcsin\left(\frac{x}{5}\right)}=\lim_{x\to0^{\pm}}\frac{5x|x-3|}{(x-3)(x-1)\arcsin\left(\frac{x}{5}\right)5}=$$
$$\lim_{x\to0^{\pm}}\frac{|x-3|}{(x-3)(x-1)}\lim_{x\to0^{\pm}}\frac{5x}{\arcsin\left(\frac{x}{5}\right)5}=5$$
**נקודה $x=0$ הינה נקודת אי רציפות סליקה.**
"""

SOL3A = r"""
$$\lim_{x\to0}\frac{\sqrt{1+\sin\frac{x}{2}}-\sqrt{1-\sin\frac{x}{2}}}{x}=\lim_{x\to0}\frac{\left(\sqrt{1+\sin\frac{x}{2}}-\sqrt{1-\sin\frac{x}{2}}\right)\left(\sqrt{1+\sin\frac{x}{2}}+\sqrt{1-\sin\frac{x}{2}}\right)}{x\left(\sqrt{1+\sin\frac{x}{2}}+\sqrt{1-\sin\frac{x}{2}}\right)}=$$
$$=\lim_{x\to0}\frac{2\sin\frac{x}{2}}{x\left(\sqrt{1+\sin\frac{x}{2}}+\sqrt{1-\sin\frac{x}{2}}\right)}=\lim_{x\to0}\frac{\sin\frac{x}{2}}{\frac{x}{2}}\cdot\frac{1}{\sqrt{1+\sin\frac{x}{2}}+\sqrt{1-\sin\frac{x}{2}}}=\frac{1}{2}$$
"""

SOL3B = r"""
$$\int(x+1)\arctan x\,dx=\begin{bmatrix}u=\arctan x& u'=\frac{1}{1+x^2}\\ v'=x+1& v=\int(x+1)dx=\frac{x^2}{2}+x\end{bmatrix}=\left(\frac{x^2}{2}+x\right)\arctan x-\int\frac{1}{1+x^2}\left(\frac{x^2}{2}+x\right)dx=$$
$$=\left(\frac{x^2}{2}+x\right)\arctan x-\frac{1}{2}\int\frac{x^2+2x}{x^2+1}dx=\left(\frac{x^2}{2}+x\right)\arctan x-\frac{1}{2}\int\left(1+\frac{2x-1}{x^2+1}\right)dx=$$
$$=\left(\frac{x^2}{2}+x\right)\arctan x-\frac{1}{2}\left(x+\int\frac{2x}{x^2+1}dx-\int\frac{1}{x^2+1}dx\right)=$$
$$=\left(\frac{x^2}{2}+x\right)\arctan x-\frac{1}{2}\left(x+\ln\left(x^2+1\right)-\arctan x\right)=$$
$$=\left(\frac{x^2}{2}+x+\frac{1}{2}\right)\arctan x-\frac{x}{2}-\frac{\ln\left(x^2+1\right)}{2}+c$$
"""

SOL4A = r"""
על פי משפט הערך הממוצע של לגרנז' קיימת נקודה $c\in(a,b)$ בה מתקיים
$$\frac{f(b)-f(a)}{b-a}=f'(c)\ \Rightarrow\ \frac{\left(a_2b^2+a_1b+a_0\right)-\left(a_2a^2+a_1a+a_0\right)}{b-a}=2a_2c+a_1$$
$$\Rightarrow\ \frac{a_2\left(b^2-a^2\right)+a_1(b-a)}{b-a}=2a_2c+a_1\ \Rightarrow\ a_2(a+b)+a_1=2a_2c+a_1\ \Rightarrow\ c=\frac{a+b}{2}$$
"""

SOL4B = r"""
**הפתרון בכתב היד במקור, עם תיקון:** ההצבה (שיטת הטבעות סביב $x=4$, הרדיוסים ושני האינטגרלים) נכונה ומועתקת כאן כפי שהיא, אך החישוב הסופי בכתב היד שגוי: בכתב היד התקבל $\pi\left(1184-\frac{224}{3}\sqrt{2}\right)\approx3387.9$. הערך הנכון הוא $V=128\pi\approx402.1$ (נבדק בשתי שיטות: טבעות וקליפות). להלן הפתרון עם החישוב המתוקן.
ראשית, נמצא את נקודות החיתוך של הקווים.
$$x^2=2x+8\iff x^2-2x-8=0\iff(x-4)(x+2)=0$$
ולכן נקבל $x=-2$ ו-$x=4$.
![שרטוט התחום הכלוא בין y=x^2, y=2x+8 ו-x=0 (משמאל) והגוף המתקבל מסיבוב סביב x=4 (מימין)](images/exams/21A-B-Q4b-sketch.png)
ברור לנו שכל חתך של הגוף יתקבל בצורת טבעת.
הרדיוס הפנימי הוא: $r=4-\sqrt{y}$.
כאשר $y\in[0,8]$, הרדיוס החיצוני הוא $R=4$.
כאשר $y\in[8,16]$, הרדיוס החיצוני הוא $R=4-\left(\frac{1}{2}y-4\right)$, כלומר $R=8-\frac{1}{2}y$.
מכאן נבחין שהנפח המבוקש ניתן לחישוב בתור:
$$V=\pi\int_0^8\left[4^2-\left(4-\sqrt{y}\right)^2\right]dy+\pi\int_8^{16}\left[\left(8-\frac{1}{2}y\right)^2-\left(4-\sqrt{y}\right)^2\right]dy$$
$$=\pi\left(\int_0^8\left[16-\left(16-8y^{\frac12}+y\right)\right]dy+\int_8^{16}\left[64-8y+\frac{1}{4}y^2-\left(16-8\sqrt{y}+y\right)\right]dy\right)$$
$$=\pi\left(\int_0^8\left[8y^{\frac12}-y\right]dy+\int_8^{16}\left[48-9y+\frac{1}{4}y^2+8y^{\frac12}\right]dy\right)$$
$$=\pi\left(\left(\frac{16}{3}y^{\frac32}-\frac{y^2}{2}\right)\Big|_0^8+\left(48y-\frac{9}{2}y^2+\frac{1}{12}y^3+\frac{16}{3}y^{\frac32}\right)\Big|_8^{16}\right)$$
**החישוב המתוקן:**
$$\int_0^8\left[8y^{\frac12}-y\right]dy=\frac{256\sqrt{2}}{3}-32,\qquad \int_8^{16}\left[48-9y+\frac{1}{4}y^2+8y^{\frac12}\right]dy=160-\frac{256\sqrt{2}}{3}$$
$$V=\pi\left(\frac{256\sqrt{2}}{3}-32+160-\frac{256\sqrt{2}}{3}\right)=128\pi\approx402.1$$
"""

SOL5A = r"""
ראשית נשים לב לכך ש
$$f(x)=x^6-2x^2+x\ \Rightarrow\ f'(x)=6x^5-4x+1$$
בנוסף, מתקיים $f(0)=f(1)=0$. על-פי משפט רול קיימת נקודה $x_0\in(0,1)$ בה מתקיים
$$6x_0^5-4x_0+1=f'(x_0)=0$$
"""

SOL5B = r"""
$$\lim_{x\to0}\left(2\cdot\frac{1-\cos x}{x^4}-\frac{1}{x^2}\right)=\lim_{x\to0}\frac{2-2\cos x-x^2}{x^4}=\lim_{x\to0}\frac{-2x+2\sin x}{4x^3}=$$
$$=\frac{1}{2}\lim_{x\to0}\frac{-x+\sin x}{x^3}=\frac{1}{2}\lim_{x\to0}\frac{-1+\cos x}{3x^2}=-\frac{1}{6}\lim_{x\to0}\frac{1-\cos x}{x^2}=-\frac{1}{6}\lim_{x\to0}\frac{2\sin^2(x/2)}{x^2}=$$
$$=-\frac{1}{12}\lim_{x\to0}\frac{\sin^2(x/2)}{(x/2)^2}=-\frac{1}{12}$$
"""

SOL6A = r"""
ראשית נציין שהפונקציה מוגדרת לכל $x$ ממשי. נמצא נקודות קריטיות בתוך הקטע:
$$f'(x)=\frac{2x-2}{3\sqrt[3]{(x^2-2x)^2}}$$
ומכאן ברור שהנגזרת מתאפסת בנק' $x=1$ ולא קיימת בנק' $x=0$ ו-$x=2$ בתוך הקטע. בנוסף לזאת, יש להוסיף לנקודות האלו נקודות הקצה וכתוצאה מכך כל הנקודות החשודות כאן יהיו: $x=1,\ x=0,\ x=2,\ x=-1$ ו-$x=3$.
$$f(0)=\sqrt[3]{x^2-2x}=0,\quad f(1)=\sqrt[3]{x^2-2x}=-1,\quad f(2)=\sqrt[3]{x^2-2x}=0,\quad f(-1)=\sqrt[3]{x^2-2x}=\sqrt[3]{3},\quad f(3)=\sqrt[3]{x^2-2x}=\sqrt[3]{3}$$
$$\Rightarrow\ \begin{cases}f_{\min}=f(1)=-1\\ f_{\max}=f(-1)=f(3)=\sqrt[3]{3}\end{cases}$$
"""

SOL6B = r"""
![הרביע הראשון: הגרפים y=4x^2, y=x^2/9 והישר y=2, עם נקודות החיתוך x=1/sqrt(2) ו-x=sqrt(18)](images/exams/21A-B-Q6b-region.png)
$$y=4x^2,\ y=\frac{x^2}{9},\ y=2$$
$$4x^2=\frac{x^2}{9},\quad x=0,\qquad 4x^2=2,\quad x=\pm\frac{1}{\sqrt{2}},\qquad \frac{x^2}{9}=2,\quad x=\pm\sqrt{18},\qquad x\ge0$$
$$S=\int_0^{\frac{1}{\sqrt{2}}}\left(4x^2-\frac{x^2}{9}\right)dx+\int_{\frac{1}{\sqrt{2}}}^{\sqrt{18}}\left(2-\frac{x^2}{9}\right)dx=$$
$$=\left(4\frac{x^3}{3}-\frac{x^3}{27}\right)\Big|_0^{\frac{1}{\sqrt{2}}}+\left(2x-\frac{x^3}{27}\right)\Big|_{\frac{1}{\sqrt{2}}}^{\sqrt{18}}=$$
$$=\left(4\frac{\left(\frac{1}{\sqrt{2}}\right)^3}{3}-\frac{\left(\frac{1}{\sqrt{2}}\right)^3}{27}\right)+\left(2\sqrt{18}-\frac{\sqrt{18}^3}{27}\right)-\left(2\left(\frac{1}{\sqrt{2}}\right)-\frac{\left(\frac{1}{\sqrt{2}}\right)^3}{27}\right)=$$
$$=10\sqrt{2}/3\approx4.714$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=\frac{x^4}{x^3-1}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, נקודות קיצון, "
      "תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "computation", "function_limits",
      r"עבור אילו ערכים של $a$ ו-$b$ מתקיים: $\lim_{x\to+\infty}\left(\frac{x^3}{x^2-x+2}+ax+b\right)=0$.",
      SOL2A, part="א"),

    Q(2, "computation", "continuity",
      r"מצאו את כל נקודות האי-רציפות של הפונקציה $f(x)=\frac{x|x-3|}{\left(x^2-4x+3\right)\arcsin\left(\frac{x}{5}\right)}$ ומיינו אותן.",
      SOL2B, part="ב"),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\frac{\sqrt{1+\sin\frac{x}{2}}-\sqrt{1-\sin\frac{x}{2}}}{x}$.",
      SOL3A, part="א"),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int(x+1)\arctan x\,dx$.",
      SOL3B, part="ב"),

    Q(4, "proof", "mean_value_theorems",
      r"הוכיחו שאם $f(x)=a_0+a_1x+a_2x^2$, אז הנקודה $x=c$ שאת קיומה מבטיח משפט הערך הממוצע של לגרנז' נמצאת בדיוק באמצע הקטע $[a,b]$.",
      SOL4A, part="א"),

    Q(4, "computation", "definite_integrals",
      r"מצאו את נפח הגוף המתקבל מסיבוב של התחום הכלוא בין הקווים $y=2x+8,\ y=x^2$ ו-$x=0$ כאשר $x\ge0$ סביב הציר $x=4$. "
      "צייר את התחום המסובב והסבר את פעולותיך!",
      SOL4B, part="ב", points=10, solutionSource="solved", official=False, confidence="med"),

    Q(5, "proof", "mean_value_theorems",
      r"הוכיחו כי למשוואה $6x^5-4x+1=0$ יש שורש ממשי אחד לפחות בקטע $(0,1)$.",
      SOL5A, part="א"),

    Q(5, "computation", "lhopital_taylor",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\left(2\cdot\frac{1-\cos x}{x^4}-\frac{1}{x^2}\right)$.",
      SOL5B, part="ב"),

    Q(6, "computation", "extrema_optimization",
      r"מצאו אקסטרמומים מוחלטים של $f(x)=\sqrt[3]{x^2-2x}$ בקטע $[-1,3]$.",
      SOL6A, part="א"),

    Q(6, "computation", "definite_integrals",
      r'חשבו את שטח התחום הנמצא ברביע הראשון החסום ע"י הקווים $y=4x^2,\ y=\frac{x^2}{9},\ y=2$.',
      SOL6B, part="ב"),
]

exam = {
    "examCode": "21A-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"א, מועד א'",
    "year": 2021,
    "examDate": "",
    "sourceFile": "calculus-1/21A-B solution (image PDF).pdf",
    "solutionFile": "calculus-1/21A-B solution (image PDF).pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

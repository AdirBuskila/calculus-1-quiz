# -*- coding: utf-8 -*-
"""Generator for tools/raw/22B-B.json -- calculus-1 (20151), semester B 2022, moed B (12/07/2022).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22B-B.py

Source: sitting 22B-B, pp.1-9 (HIT-headed typeset document "solution of the final exam of 12.07.2022": the lecturers'
official solution, with each question restated before its solution). Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6
(each question 20%, two parts of 10%). Question wording below is the restatement in that file.

Transcription notes
- Q1 is one item (single instruction list); the typeset graph on p.3 is shipped as images/exams/22B-B-Q1-graph.png. The two
  hand-drawn sign tables are described in words (f' : -,+,- ; f'' : -,+,-,+).
- Q1e: the file prints the second form of b as lim x/(e^(2x^2)-1) and the L'Hopital form as 1/(4x e^(2x)); the correct
  expressions x/e^(2x^2-1) and 1/(4x e^(2x^2-1)) are written (both tend to 0 as the file concludes).
- Q2a: the file's induction chain prints '1+1/a' in two places where '1+3/a' is meant; written with the 3.
- Q3a: the printed task has <= while the proof gives the strict inequality (which implies it); transcribed as is.
- Q4b: the file prints the upper limit of the antiderivative as 2 instead of 1; the value is computed with 1.
- Q3b, Q5b: the sketches in the solution are shipped as images.
- Q6b: HELD. The official remainder estimate uses (0.01)^3 where |x|<=0.1 gives |x|^3<=0.001; the official 4.57e-7 should be
  4.57e-4 (sympy). Solution transcribed as printed, see ASK_ADIR.

Checks (tools/verify/22B-B/check.py, sympy): every derivative, sign table, limit, antiderivative, volume, arc length,
area and Taylor coefficient matches the official answers except the Q6b remainder bound.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22B-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**א. תחום ההגדרה של הפונקציה:** $x\in\mathbb{R}$.
**ב. נקודות החיתוך עם הצירים:** $x\cdot e^{1-2x^2}=0$, נקבל את הנקודה $x=0,\ y=0$.
**ג. תחומי עליה וירידה, נקודות קיצון:**
$$f'(x)=e^{1-2x^2}\left(1-4x^2\right)=0$$
קיימות שתי נקודות חשודות לקיצון: $x_1=\frac{1}{2},\ x_2=-\frac{1}{2}$.
טבלת סימן של $f'(x)$: שלילית כאשר $x<-\frac{1}{2}$, חיובית כאשר $-\frac{1}{2}<x<\frac{1}{2}$, ושלילית כאשר $x>\frac{1}{2}$.
קיימות שתי נקודות קיצון: נקודת מקסימום $\left(\frac{1}{2},\frac{\sqrt{e}}{2}\right)$, נקודת מינימום $\left(-\frac{1}{2},-\frac{\sqrt{e}}{2}\right)$.
**ד. תחומי קמירות וקעירות, נקודות פיתול:**
$$f''(x)=4xe^{1-2x^2}\left(4x^2-3\right)=0$$
טבלת סימן של $f''(x)$: שלילית כאשר $x<-\frac{\sqrt{3}}{2}$, חיובית כאשר $-\frac{\sqrt{3}}{2}<x<0$, שלילית כאשר $0<x<\frac{\sqrt{3}}{2}$, וחיובית כאשר $x>\frac{\sqrt{3}}{2}$.
נקודות פיתול הן: $x_1=0,\ x_2=\frac{\sqrt{3}}{2},\ x_3=-\frac{\sqrt{3}}{2}$.
**ה. אסימפטוטות:**
1. אין אסימפטוטה אנכית (פונקציה מוגדרת ורציפה בכל תחום הגדרתה).
2. אסימפטוטה משופעת:
$$a=\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim_{x\to\pm\infty}\frac{xe^{1-2x^2}}{x}=0$$
$$b=\lim_{x\to\pm\infty}xe^{1-2x^2}\,[\infty\cdot0]=\lim_{x\to\pm\infty}\frac{x}{e^{2x^2-1}}\left[\frac{\infty}{\infty}\right]=\lim_{x\to\pm\infty}\frac{1}{4xe^{2x^2-1}}\left[\frac{1}{\infty}\right]=0$$
$y=0$ - אסימפטוטה אופקית של הפונקציה.
**ו. שרטוט:**
![גרף הפונקציה f(x)=x e^(1-2x^2): מקסימום ב-x=1/2, מינימום ב-x=-1/2, אסימפטוטה y=0](images/exams/22B-B-Q1-graph.png)
"""

SOL2A = r"""
מתוך ההגדרה של הסדרה מקבלים ש-$a_n>0$. לכן $0$ הוא חסם תחתון של הסדרה.
נוכיח לפי אינדוקציה שהסדרה הנתונה יורדת. צריך להוכיח ש-$a_{n+1}<a_n$.
בדיקה $n=1$: $a_2=\frac{2}{1+3}=\frac{1}{2}<a_1=1$.
ההנחה עבור $n=k$: $a_{k+1}<a_k$. צריך להוכיח עבור $n=k+1$: $a_{k+2}<a_{k+1}$.
$$a_{k+1}<a_k\ \Rightarrow\ \frac{1}{a_{k+1}}>\frac{1}{a_k}\ \Rightarrow\ \frac{3}{a_{k+1}}>\frac{3}{a_k}\ \Rightarrow$$
$$1+\frac{3}{a_{k+1}}>1+\frac{3}{a_k}\ \Rightarrow$$
$$\frac{1}{1+\frac{3}{a_{k+1}}}<\frac{1}{1+\frac{3}{a_k}}\ \Rightarrow\ \frac{2}{1+\frac{3}{a_{k+1}}}<\frac{2}{1+\frac{3}{a_k}}\ \Rightarrow\ a_{k+2}<a_{k+1}$$
מ.ש.ל.
לכן הסדרה הנתונה מתכנסת כסדרה יורדת וחסומה מלמטה. נסמן
$$\lim_{n\to\infty}a_n=L\ \Rightarrow\ \lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}\frac{2}{1+\frac{3}{a_n}}\ \Rightarrow$$
$$L=\frac{2}{1+\frac{3}{L}},\qquad L=\frac{2L}{L+3}\ \Rightarrow\ L^2+3L=2L,\ L^2+L=0$$
$$L_1=0,\ L_2=-1$$
$$a_n>0\ \Rightarrow\ L\neq-1\ \Rightarrow\ L=0$$
$$\lim_{n\to\infty}a_n=0$$
"""

SOL2B = r"""
אם נשתמש בהצבה טריגונומטרית אוניברסלית, $t=\tan\frac{x}{2}$, אז $\sin x=\frac{2t}{1+t^2},\ \cos x=\frac{1-t^2}{1+t^2},\ dx=\frac{2dt}{1+t^2}$, וכתוצאה מכך נוכל להציג את האינטגרל המקורי בצורה:
$$\int\frac{dx}{5-4\sin x+3\cos x}=\int\frac{2\,dt}{(1+t^2)\left(5-4\frac{2t}{1+t^2}+3\frac{1-t^2}{1+t^2}\right)}=\int\frac{dt}{4-4t+t^2}=\int\frac{dt}{(t-2)^2}=$$
$$=-\frac{1}{t-2}+C=-\frac{1}{\tan\frac{x}{2}-2}+C=\frac{1}{2-\tan\frac{x}{2}}+C$$
"""

SOL3A = r"""
הבה נבחן את הפונקציה $f(x)=\arcsin x$ שנגזרת שלה היא: $f'(x)=(\arcsin x)'=\frac{1}{\sqrt{1-x^2}}$.
לפי משפט לגרנז' קיימת נקודה $c\in(a,b)$ כך ש-
$$f'(c)=\frac{f(b)-f(a)}{b-a}$$
כלומר:
$$\frac{1}{\sqrt{1-c^2}}=\frac{\arcsin b-\arcsin a}{b-a}\iff\frac{b-a}{\sqrt{1-c^2}}=\arcsin b-\arcsin a$$
מאז $0<a<c<b$ יש לנו כי
$$a^2<c^2<b^2\ \Longrightarrow\ -b^2<-c^2<-a^2\ \Longrightarrow\ 1-b^2<1-c^2<1-a^2\ \Longrightarrow\ \sqrt{1-b^2}<\sqrt{1-c^2}<\sqrt{1-a^2}\ \Longrightarrow$$
$$\frac{1}{\sqrt{1-a^2}}<\frac{1}{\sqrt{1-c^2}}<\frac{1}{\sqrt{1-b^2}}\ \Longrightarrow\ \frac{b-a}{\sqrt{1-a^2}}<\frac{b-a}{\sqrt{1-c^2}}<\frac{b-a}{\sqrt{1-b^2}}\iff$$
$$\frac{b-a}{\sqrt{1-a^2}}<\arcsin(b)-\arcsin(a)<\frac{b-a}{\sqrt{1-b^2}}$$
"""

SOL3B = r"""
![התחום הכלוא בין y=sqrt(x ln x) לציר ה-x עבור 1<=x<=e](images/exams/22B-B-Q3b-sketch.png)
$$V=\pi\int_1^ef^2(x)\,dx=\pi\int_1^ex\ln x\,dx=\left|\begin{array}{ll}u=\ln x & du=\frac{dx}{x}\\ dv=x\,dx & v=\frac{x^2}{2}\end{array}\right|=$$
$$=\pi\left(\frac{x^2}{2}\ln x\Big|_1^e-\frac{1}{2}\int_1^ex^2\frac{dx}{x}\right)=\pi\left(\frac{e^2}{2}-\frac{1}{2}\int_1^ex\,dx\right)=$$
$$=\pi\left(\frac{e^2}{2}-\frac{1}{2}\cdot\frac{x^2}{2}\Big|_1^e\right)=\pi\left(\frac{e^2}{2}-\frac{1}{2}\left(\frac{e^2}{2}-\frac{1}{2}\right)\right)=$$
$$=\pi\left(\frac{e^2}{2}-\frac{e^2}{4}+\frac{1}{4}\right)=\frac{\pi}{4}\left(e^2+1\right)$$
"""

SOL4A = r"""
$$\lim_{x\to0}\frac{x-\int_0^{x^2}\cos\left(t^2\right)dt}{x^3-6x}=\left\{\tfrac{0}{0}\right\}=\lim_{x\to0}\frac{1-\cos\left(x^4\right)(2x)}{3x^2-6}=-\frac{1}{6}$$
"""

SOL4B = r"""
$$L=\int_0^1\sqrt{1+\left(f'(x)\right)^2}\,dx$$
$$f(x)=x\sqrt{x}=x^{3/2}\ \Longrightarrow\ f'(x)=\frac{3}{2}x^{1/2}\ \Longrightarrow\ \left(f'(x)\right)^2=\frac{9}{4}x\ \Longrightarrow$$
$$L=\int_0^1\sqrt{1+\frac{9}{4}x}\,dx=\frac{4}{9}\int_0^1\frac{9}{4}\left(1+\frac{9}{4}x\right)^{1/2}dx=$$
$$=\frac{4}{9}\cdot\frac{2}{3}\left(1+\frac{9}{4}x\right)^{3/2}\Big|_0^1=\frac{8}{27}\left(\left(\frac{13}{4}\right)^{3/2}-1\right)$$
"""

SOL5A = r"""
נסמן $f(x)=2x^3+3\arctan x+e^x+1$. המשוואה הנתונה שקולה ל-$f(x)=0$.
$$f(0)=2>0,\qquad f(-1)=-2-\frac{3\pi}{4}+\frac{1}{e}+1<0$$
$f(x)$ רציפה על $[-1,0]$, אז לפי משפט על ערך הביניים $f(0)\cdot f(-1)<0$, קיימת נקודה $x=c\in(-1,0)$ כך ש-$f(c)=0$. ז"א למשוואה קיים פתרון $x=c$.
נוכיח שפתרון יחיד: $f'(x)=6x^2+\frac{3}{1+x^2}+e^x>0$ ב-$(-\infty,\infty)$. ז"א $f(x)$ מונוטונית עולה ממש ב-$(-\infty,\infty)$. לכן $x=c$ הוא פתרון יחיד למשוואה.
"""

SOL5B = r"""
נסמן נקודת השקה: $A\left(a,\sqrt{a-1}\right)$.
![גרף y=sqrt(x-1), המשיק דרך הראשית והתחום הכלוא בין הגרף, המשיק וציר ה-x](images/exams/22B-B-Q5b-sketch.png)
שיפוע של משיק דרך 2 נקודות: $m_{OA}=\frac{\sqrt{a-1}}{a}$.
שיפוע של משיק דרך נקודת השקה: $m=y'(a)=\frac{1}{2\sqrt{a-1}}$.
$$\frac{1}{2\sqrt{a-1}}=\frac{\sqrt{a-1}}{a}\ \to\ 2(a-1)=a\ \to\ a=2\ \to\ A(2,1)$$
משוואת משיק: $y-1=\frac{1}{2}(x-2)\ \to\ y=\frac{1}{2}x$.
$$S_{\triangle OAB}=\frac{2\cdot1}{2}=1,\qquad S_2=\int_1^2\sqrt{x-1}\,dx=\frac{2}{3}\left((x-1)^{3/2}\right)\Big|_1^2=\frac{2}{3}\ \to\ S=S_{\triangle OAB}-S_2=\frac{1}{3}$$
"""

SOL6A = r"""
נמצא את הפירוק מן הצורה:
$$\frac{1}{(x+1)\left(x^2+4x+5\right)}=\frac{A}{x+1}+\frac{Bx+C}{x^2+4x+5}$$
$$1=A\left(x^2+4x+5\right)+(Bx+C)(x+1)$$
נמצא את המקדמים:
$$x=-1:\ 1=2A\Rightarrow A=\frac{1}{2}$$
$$x^2:\ A+B=0\Rightarrow B=-\frac{1}{2}$$
$$x:\ 4A+B+C=0\Rightarrow C=-\frac{3}{2}$$
$$\int\frac{dx}{(x+1)\left(x^2+4x+5\right)}=\frac{1}{2}\int\frac{dx}{x+1}-\frac{1}{2}\int\frac{x\,dx}{x^2+4x+5}-\frac{3}{2}\int\frac{dx}{x^2+4x+5}=$$
$$=\frac{1}{2}\ln|x+1|-\frac{1}{4}\int\frac{(2x+4-4)\,dx}{x^2+4x+5}-\frac{3}{2}\int\frac{dx}{x^2+4x+5}=$$
$$=\frac{1}{2}\ln|x+1|-\frac{1}{4}\int\frac{(2x+4)\,dx}{x^2+4x+5}-\frac{1}{2}\int\frac{dx}{(x+2)^2+1}$$
$$=\frac{1}{2}\ln|x+1|-\frac{1}{4}\ln\left(x^2+4x+5\right)-\frac{1}{2}\arctan(x+2)+C$$
"""

SOL6B = r"""
הפולינום הנדרש הוא $T_2(x)=y(0)+\frac{y'(0)}{1!}x+\frac{y''(0)}{2!}x^2$, ואם נחשב
$$y'=\frac{1}{1+x}\Big|_{x=0}=1,\qquad y''=-\frac{1}{(1+x)^2}\Big|_{x=0}=-1$$
אז נקבל אותו בצורה $T_2(x)=x-\frac{1}{2}x^2$. לפי משפט טיילור עם שארית, שגיאת הקירוב $y=\ln(1+x)\approx T_2(x)=x-\frac{1}{2}x^2$ ניתן להעריך בהתאם ל-
$$\left|y-T_2(x)\right|=\left|R_2(x)\right|=\left|\frac{y'''(z)}{3!}x^3\right|=\left|\frac{2}{3!(1+z)^3}x^3\right|$$
כאשר $-0.1<z<0.1$. מכאן נובע ש-
$$\left|R_2(x)\right|=\left|\frac{1}{3(1+z)^3}x^3\right|\le\frac{1}{3\cdot0.9^3}(0.01)^3=4.57\cdot10^{-7}$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=x\cdot e^{1-2x^2}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, "
      "תחומי עליה וירידה, נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "proof", "sequences_limits",
      r"נתונה הסדרה: $a_1=1,\ a_{n+1}=\frac{2a_n}{a_n+3}$. הוכיחו כי הסדרה מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2A, part="א", points=10),
    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{dx}{5-4\sin(x)+3\cos(x)}$.",
      SOL2B, part="ב", points=10),

    Q(3, "proof", "mean_value_theorems",
      r"הוכיחו את האי-שוויון $\frac{b-a}{\sqrt{1-a^2}}\le\arcsin(b)-\arcsin(a)\le\frac{b-a}{\sqrt{1-b^2}}$, כאשר $0<a<b<1$.",
      SOL3A, part="א", points=10),
    Q(3, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום המישורי הכלוא בין הקווים: "
      r"$y=\sqrt{x\ln(x)},\ y=0,\ x=1,\ x=e$ סביב ציר ה-$X$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "lhopital_taylor",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\frac{x-\int_0^{x^2}\cos\left(t^2\right)dt}{x^3-6x}$.",
      SOL4A, part="א", points=10),
    Q(4, "computation", "definite_integrals",
      r"חשבו את אורך הקשת של העקומה $y=x\sqrt{x}$ בקטע $0\le x\le1$.",
      SOL4B, part="ב", points=10),

    Q(5, "proof", "continuity",
      r"הוכיחו כי למשוואה $2x^3+3\arctan x+e^x+1=0$ קיים פתרון אחד בלבד.",
      SOL5A, part="א"),
    Q(5, "computation", "definite_integrals",
      r"חשבו את השטח הכלוא בין הגרף של הפונקציה $y=\sqrt{x-1}$, משיק לאותה הפונקציה העובר דרך ראשית הצירים $(0,0)$ וציר ה-$X$.",
      SOL5B, part="ב"),

    Q(6, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{dx}{(x+1)\left(x^2+4x+5\right)}$.",
      SOL6A, part="א", points=10),
    Q(6, "computation", "lhopital_taylor",
      r"פתחו את הפונקציה $y=\ln(1+x)$ לפולינום מקלורן מסדר שני והעריכו את השארית עבור הקטע $[-0.1,0.1]$.",
      SOL6B, part="ב", points=10,
      hold="official remainder bound uses (0.01)^3 although |x|<=0.1 gives 4.57e-4, not 4.57e-7"),
]

exam = {
    "examCode": "22B-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ב, מועד ב'",
    "year": 2022,
    "examDate": "12/07/2022",
    "sourceFile": "calculus-1/22B-B exam+solution.pdf",
    "solutionFile": "calculus-1/22B-B exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

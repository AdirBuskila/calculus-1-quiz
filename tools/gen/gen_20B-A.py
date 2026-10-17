# -*- coding: utf-8 -*-
"""Generator for tools/raw/20B-A.json -- calculus-1 (20151), semester A 2020, moed B (01/05/2020).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_20B-A.py

Source: sitting 20B-A, pp.1-5 (typed "פתרון המבחן": every question is restated and followed by the official worked
solution). Part A (mandatory): Q1 (weight not printed). Part B: choose 4 of Q2-Q6 (a/b parts, 10% each).

Transcription notes
- Q1 sketch (p.2) is shipped as a figure inside the solution.
- Q1 f'' line: the printed intermediate numerator reads (2e^{2x}(2x-1) - 2e^{2x})x^2 ...; the derivative of
  e^{2x}(2x-1) is 2e^{2x}(2x-1) + 2e^{2x}, so the sign is corrected to "+" (the simplified f'' printed next is right).
  Intermediate slip, no student-facing label; logged in docs/ASK_ADIR.md.
- Q2a keeps the official wording "מהמעבר לגבול ... נוסחת הנסיגה".

Checks (tools/verify/20B-A/check.py, sympy): every derivative, sign claim, limit, integral, tangent line, arc length,
parameter value and area matches the official answer. 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20B-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
נחקור את הפונקציה לפי הסעיפים הבאים:
**תחום ההגדרה:** $x\neq 0$, ונמצא את הגבולות החד-צדדיים ב-$0$:
$$\lim_{x\to0^-}\frac{e^{2x}}{x}=-\infty,\qquad \lim_{x\to0^+}\frac{e^{2x}}{x}=+\infty$$
לכן הנקודה $x=0$ היא נקודת אי-רציפות מסוג שני, ואז $x=0$ היא אסימפטוטה אנכית לגרף הפונקציה.
**אסימפטוטות:** נמצא אסימפטוטות משופעות/אופקיות עבור $x\to+\infty$ ו-$x\to-\infty$ כי התנהגות של $e^{2x}$ עבור השאיפות אלו שונה.
$$k_1=\lim_{x\to+\infty}\frac{f(x)}{x}=\lim_{x\to+\infty}\frac{e^{2x}}{x^2}=\left\{\frac{\infty}{\infty}\right\}=\lim_{x\to+\infty}\frac{2e^{2x}}{2x}=\lim_{x\to+\infty}\frac{e^{2x}}{x}=\left\{\frac{\infty}{\infty}\right\}=\lim_{x\to+\infty}\frac{2e^{2x}}{1}=\infty$$
$$k_2=\lim_{x\to-\infty}\frac{f(x)}{x}=\lim_{x\to-\infty}\frac{e^{2x}}{x^2}=0,\qquad b_2=\lim_{x\to-\infty}\left(f(x)-k_2x\right)=\lim_{x\to-\infty}\frac{e^{2x}}{x}=0$$
לגרף הפונקציה אין אסימפטוטות ימניות, אך יש אסימפטוטה אופקית שמאלית $y=0$.
**זוגיות:** הפונקציה אינה בעלת זוגיות מוגדרת כי $f(-x)=-\frac{e^{-2x}}{x}\neq f(x)$ ו-$f(-x)=-\frac{e^{-2x}}{x}\neq -f(x)$.
**מונוטוניות וקיצון מקומי:**
$$f'(x)=\frac{2e^{2x}x-e^{2x}}{x^2}=\frac{e^{2x}(2x-1)}{x^2},\qquad f'(x)=0\ \Rightarrow\ x=\frac{1}{2}$$
טבלת סימנים של $f'$: שלילית ב-$x<0$ (ויורדת), שלילית ב-$0<x<\frac12$ (ויורדת), חיובית ב-$x>\frac12$ (עולה).
הנקודה $x=\frac{1}{2}$ היא נקודת מינימום מקומי ו-$f\left(\frac12\right)=2e$.
**קמירות/קעירות ונקודות פיתול:**
$$f''(x)=\frac{\left(2e^{2x}(2x-1)+2e^{2x}\right)x^2-e^{2x}(2x-1)2x}{x^4}=\frac{2e^{2x}\left(2x^2-2x+1\right)}{x^3},\qquad f''(x)\neq0$$
טבלת סימנים של $f''$: שלילית ב-$x<0$ (הפונקציה קעורה), חיובית ב-$x>0$ (הפונקציה קמורה).
הנקודה $x=0$ אינה בתחום ההגדרה ולכן אין נקודות פיתול. נשרטט את הגרף:
![שרטוט הגרף של y = e^(2x)/x עם האסימפטוטה האנכית x=0, האסימפטוטה השמאלית y=0 והמינימום ב-x=1/2](images/exams/20B-A-Q1-graph.png)
"""

SOL2A = r"""
נתבונן ב-$a_{n+1}-a_n$ ונקבל
$$a_{n+1}-a_n=3-\frac{2}{a_n}-a_n=\frac{(2-a_n)(a_n-1)}{a_n}.$$
נוכיח באמצעות אינדוקציה מתמטית ש-$1<a_n<2$. אמנם, $2>a_1>1$. נניח כי $2>a_k>1$ ונוכיח כי $2>a_{k+1}>1$. אם $1<a_k<2$ אז $1<\frac{2}{a_k}<2$ ו-$-2<-\frac{2}{a_k}<-1$, לכן $1<3-\frac{2}{a_k}<2$.
מההוכחה $1<a_n<2$ נובע כי $a_{n+1}-a_n>0$ ואז הסדרה עולה. מונוטוניות וחסימות גוררות כי הסדרה מתכנסת ונסמן את גבולה ב-$L$. מהמעבר לגבול בנוסחת הנסיגה נובע כי $L=3-\frac{2}{L}$ או $\frac{L^2-3L+2}{L}=0$ ולכן $L=1$ או $L=2$. לפי המונוטוניות (עולה) נקבל שהגבול שווה ל-$2$.
"""

SOL2B = r"""
העקומות נחתכות בנקודה $(1,1)$ והשיפועים לכל גרף שונים ב-$x=1$ כי $g'(1)=2$ ו-$f'(1)=-1$, לכן אין נקודת ההשקה המשותפת. נסמן את נקודת ההשקה של $f$ ב-$x_1$ ושל $g$ ב-$x_2$. אז נקבל את המערכת עבור אותו קו משיק:
$$\begin{cases}y-\frac{1}{x_1}=-\frac{1}{x_1^2}(x-x_1)\\ y-x_2^2=2x_2(x-x_2)\end{cases}\Rightarrow\begin{cases}y=-\frac{1}{x_1^2}x+\frac{2}{x_1}\\ y=2x_2x-x_2^2\end{cases}\Rightarrow\begin{cases}-\frac{1}{x_1^2}=2x_2\\ \frac{2}{x_1}=-x_2^2\end{cases}\Rightarrow\begin{cases}x_2=-\frac{1}{2x_1^2}\\ \frac{2}{x_1}=-\frac{1}{4x_1^4}\end{cases}$$
אז $x_1=-\frac{1}{2},\ x_2=-2$ ומשוואת המשיק לשני הגרפים היא $y=-4x-4$.
"""

SOL3A = r"""
$$\lim_{x\to0}\left(\frac{\sin x}{x}\right)^{\frac{1}{x^2}}=\{1^{\infty}\}=A$$
$$\ln A=\lim_{x\to0}\frac{\ln\frac{\sin x}{x}}{x^2}=\left\{\frac{0}{0}\right\}=\lim_{x\to0}\frac{\ln\sin x-\ln x}{x^2}=\lim_{x\to0}\frac{\frac{\cos x}{\sin x}-\frac{1}{x}}{2x}=\lim_{x\to0}\frac{x\cos x-\sin x}{2x^2\sin x}=$$
$$=\left\{\frac{0}{0}\right\}=\lim_{x\to0}\frac{-x\sin x}{4x\sin x+2x^2\cos x}=\lim_{x\to0}\frac{-\sin x}{4\sin x+2x\cos x}=\left\{\frac{0}{0}\right\}=\lim_{x\to0}\frac{-\cos x}{6\cos x-2x\sin x}=-\frac{1}{6}$$
התשובה: $e^{-\frac{1}{6}}$.
"""

SOL3B = r"""
נפרק את השבר לשברים אלמנטריים:
$$\frac{2x^2+15}{x(x^2+2x+5)}=\frac{A}{x}+\frac{Bx+C}{x^2+2x+5}=\frac{A(x^2+2x+5)+x(Bx+C)}{x(x^2+2x+5)}$$
מהשוואת הפולינומים נקבל $\begin{cases}A+B=2\\2A+C=0\\5A=15\end{cases}$ או $\begin{cases}A=3\\B=-1\\C=-6\end{cases}$, לכן
$$\int\frac{2x^2+15}{x(x^2+2x+5)}dx=\int\left(\frac{3}{x}-\frac{x+6}{x^2+2x+5}\right)dx=3\ln|x|-\int\frac{x+6}{x^2+2x+5}dx$$
$$\int\frac{x+6}{x^2+2x+5}dx=\begin{vmatrix}t=x+1\\x=t-1\\dx=dt\end{vmatrix}=\int\frac{t+5}{t^2+4}dt=\int\frac{t\,dt}{t^2+4}+5\int\frac{dt}{t^2+4}=\frac{1}{2}\ln(t^2+4)+\frac{5}{2}\arctan\frac{t}{2}+C=\frac{1}{2}\ln(x^2+2x+5)+\frac{5}{2}\arctan\frac{x+1}{2}+C$$
$$\int\frac{2x^2+15}{x(x^2+2x+5)}dx=3\ln|x|-\frac{1}{2}\ln(x^2+2x+5)-\frac{5}{2}\arctan\frac{x+1}{2}+C$$
"""

SOL4A = r"""
$$\lim_{x\to+\infty}\left[x\left(\sqrt{x^2+x+a}-\sqrt{x^2-bx}\right)\right]=\lim_{x\to+\infty}x\,\frac{x^2+x+a-(x^2-bx)}{\sqrt{x^2+x+a}+\sqrt{x^2-bx}}=$$
$$=\lim_{x\to+\infty}\frac{(1+b)x^2+ax}{\sqrt{x^2+x+a}+\sqrt{x^2-bx}}$$
החזקה הגבוהה ביותר במונה היא $x^2$ אם $b\neq-1$ והחזקה של המכנה $x$. לכן הגבול קיים רק עבור $b=-1$ ואז
$$\lim_{x\to+\infty}\frac{ax}{\sqrt{x^2+x+a}+\sqrt{x^2+x}}=\lim_{x\to+\infty}\frac{a}{\sqrt{1+\frac{1}{x}+\frac{a}{x^2}}+\sqrt{1+\frac{1}{x}}}=\frac{a}{2}.$$
השוויון מתקיים רק כאשר $a=6,\ b=-1$.
"""

SOL4B = r"""
$$\int\frac{\sin x\cos x\,dx}{1+\sin^2x}=\begin{vmatrix}t=\sin x\\dt=\cos x\,dx\end{vmatrix}=\int\frac{t\,dt}{1+t^2}=\frac{1}{2}\ln(1+t^2)+C=\frac{1}{2}\ln\left(1+\sin^2x\right)+C$$
"""

SOL5A = r"""
הערך של הפונקציה בנקודה $x=1$ שווה ל-$0$. נבדוק את הגזירות לפי ההגדרה:
$$f'(1)=\lim_{h\to0}\frac{f(1+h)-f(1)}{h}=\lim_{h\to0}\frac{\sqrt[3]{h^2}\sin h}{h}=\lim_{h\to0}\sqrt[3]{h^2}=0$$
לכן הפונקציה גזירה ב-$1$ והנגזרת שלה שווה ל-$0$ בנקודה זאת.
"""

SOL5B = r"""
לפי הנוסחה: $L=\int_0^1\sqrt{1+(y')^2}\,dx$, אז נמצא את הנגזרת של הפונקציה:
$$y'=\frac{2}{5}\cdot\frac{5}{4}x^{\frac14}-\frac{2}{3}\cdot\frac{3}{4}x^{-\frac14}=\frac{1}{2}\left(x^{\frac14}-x^{-\frac14}\right),$$
$$1+(y')^2=1+\frac{x^{\frac12}-2+x^{-\frac12}}{4}=\frac{x^{\frac12}+2+x^{-\frac12}}{4}=\left(\frac{x^{\frac14}+x^{-\frac14}}{2}\right)^2,$$
$$L=\int_0^1\sqrt{1+(y')^2}\,dx=\frac{1}{2}\int_0^1\left(x^{\frac14}+x^{-\frac14}\right)dx=\frac{1}{2}\left(\frac{4}{5}x^{\frac54}+\frac{4}{3}x^{\frac34}\right)\Big|_0^1=\frac{2}{5}+\frac{2}{3}=\frac{16}{15}$$
"""

SOL6A = r"""
נמצא את הנגזרת של הפונקציה:
$$g'(x)=\frac{2x(x-b)-(x^2+a)}{(x-b)^2}=\frac{x^2-2bx-a}{(x-b)^2}.$$
מקיום הקיצון המקומי ב-$x=2$ נובע $g'(2)=0$ או $4-4b-a=0$. השיפוע של אסימפטוטה $y=kx+m$ הוא
$$k=\lim_{x\to\infty}\frac{g(x)}{x}=\lim_{x\to\infty}\frac{x^2+a}{x(x-b)}=1$$
והאיבר החופשי
$$m=\lim_{x\to\infty}\left(g(x)-x\right)=\lim_{x\to\infty}\left(\frac{x^2+a}{x-b}-x\right)=\lim_{x\to\infty}\frac{bx+a}{x-b}=b.$$
מהתנאי נקבל $b=7$ ו-$a=4-4b=-24$.
"""

SOL6B = r"""
נציין כי בקטע $[0,1]$ הפונקציה מקבלת ערכים לא שליליים כי $\ln(x+1)\ge0$ ו-$\sqrt{x+1}\ge1$, לכן
$$S=\int_0^1\frac{\ln(x+1)}{\sqrt{x+1}}\,dx.$$
לפי אינטגרציה בחלקים נקבל, עם $u=\ln(x+1),\ dv=\frac{dx}{\sqrt{x+1}},\ du=\frac{dx}{x+1},\ v=2\sqrt{x+1}$:
$$S=2\sqrt{x+1}\ln(x+1)\Big|_0^1-2\int_0^1\frac{\sqrt{x+1}}{x+1}\,dx=2\sqrt{2}\ln2-2\int_0^1\frac{dx}{\sqrt{x+1}}=2\sqrt{2}\ln2-4\sqrt{x+1}\Big|_0^1=2\sqrt{2}\ln2-4\sqrt{2}+4$$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $y=\frac{e^{2x}}{x}$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, נקודות קיצון, "
      "תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1),

    Q(2, "proof", "sequences_limits",
      "נתונה הסדרה " r"$a_{n+1}=3-\frac{2}{a_n},\quad a_1=\frac{3}{2}$" ". הראו כי היא מונוטונית, חסומה וחשבו את גבולה.",
      SOL2A, part="א", points=10),

    Q(2, "computation", "derivatives_tangents",
      r"מצאו את משוואת המשיק המשותף לגרפים של שתי הפונקציות $f(x)=\frac{1}{x}$ ו-$g(x)=x^2$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\left(\frac{\sin x}{x}\right)^{\frac{1}{x^2}}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{2x^2+15}{x\left(x^2+2x+5\right)}\,dx$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "function_limits",
      r"מצאו עבור אילו פרמטרים ממשיים $a,b$ מתקיים השוויון: $\lim_{x\to+\infty}\left[x\left(\sqrt{x^2+x+a}-\sqrt{x^2-bx}\right)\right]=3$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\sin x\cos x\,dx}{1+\sin^2x}$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "derivatives_tangents",
      r"בדקו האם הפונקציה $f(x)=\sqrt[3]{(x-1)^2}\,\sin(x-1)$ גזירה בנקודה $x=1$?",
      SOL5A, part="א", points=10),

    Q(5, "computation", "definite_integrals",
      r"חשבו את אורך הקשת של העקומה $y=\frac{2}{5}x\sqrt[4]{x}-\frac{2}{3}\sqrt[4]{x^3}$ בתחום $0\le x\le1$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "function_investigation",
      r"נתונה הפונקציה $g(x)=\frac{x^2+a}{x-b}$ וידוע כי היא מקבלת קיצון מקומי ב-$x=2$ והקו $y=x+7$ הוא אסימפטוטה משופעת "
      "של גרף הפונקציה באינסוף. מצאו את $a$ ו-$b$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "definite_integrals",
      r"חשבו את השטח של התחום הנמצא בין גרף הפונקציה $f(x)=\frac{\ln(x+1)}{\sqrt{x+1}}$ לבין ציר ה-$x$ בקטע $[0,1]$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "20B-A",
    "examLabel": "מבחן סוף סמסטר א' תש\"פ, מועד ב'",
    "year": 2020,
    "examDate": "01/05/2020",
    "sourceFile": "calculus-1/20B-A exam+solution.pdf",
    "solutionFile": "calculus-1/20B-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

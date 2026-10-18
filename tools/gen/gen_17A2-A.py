# -*- coding: utf-8 -*-
"""Generator for tools/raw/17A2-A.json -- calculus-1 (20151), semester A 2017, moed A version 2 (06/02/2017).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_17A2-A.py

Source: sitting 17A2-A, pp.1-9 (typed exam with the official worked solution after every question).
Part A (mandatory): Q1 (20%). Part B: choose 4 of Q2-Q6 (Q2 one part, Q3-Q6 a/b parts, 10% each).

Transcription notes
- Q1/Q3b/Q4b: plots printed in the official solution are cropped as figures inside the solutions.
  The sketched sign diagrams (arrows / arcs) are transcribed as sentences.
- Q6b "הערה" (alternative partial-fraction route, p.9) transcribed in full. Slips there are fixed silently
  (printed z=t^2 should be z=x^2; stray letters A and B in the substituted line, which must read
  1/(x^4-1) = 1/2 * 1/(x^2-1) - 1/2 * 1/(x^2+1)); logged in docs/ASK_ADIR.md.

Checks: tools/verify/17A2-A/check.py (sympy), 0 mismatches with the official answers. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "17A2-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**1. תחום ההגדרה:** כל $x$ ממשי. נקודות חיתוך עם הצירים: $(1,0)$ ו-$(0,-1)$.
**2. תחומי עלייה וירידה, נקודות קיצון:** $y'=e^x+(x-1)e^x=xe^x=0$, $x=0$.
טבלת סימנים של $y'$: שלילית ב-$x<0$ (יורדת), חיובית ב-$x>0$ (עולה). נקודת מינימום: $x=0$, מתקיים $y(0)=-1$.
**3. תחומי קמירות וקעירות, נקודות פיתול:** $y''=e^x+xe^x=(x+1)e^x=0$, $x=-1$.
טבלת סימנים של $y''$: שלילית ב-$x<-1$ (קעורה, $\\cap$), חיובית ב-$x>-1$ (קמורה, $\\cup$). $x=-1$ נקודת פיתול, מתקיים $y(-1)=-\frac2e$.
**4. אסימפטוטות אנכיות:** אין.
**אסימפטוטות משופעות:** נזכיר כי אם לפונקציה $f(x)$ קיימת אסימפטוטה משופעת $y=ax+b$ אז בהכרח $a=\lim\frac{f(x)}{x}$ ו-$b=\lim\left(f(x)-ax\right)$.
ב-$+\infty$: $a=\lim_{x\to+\infty}\frac{(x-1)e^x}{x}=\lim_{x\to+\infty}\frac{xe^x}{1}=+\infty$. אין אסימפטוטה.
ב-$-\infty$: $a=\lim_{x\to-\infty}\frac{(x-1)e^x}{x}=\lim_{x\to-\infty}\frac{x-1}{x}e^x=0$, $b=\lim_{x\to-\infty}\left((x-1)e^x-0\cdot x\right)=\lim_{x\to-\infty}(x-1)e^x=0$, אסימפטוטה אופקית $y=0$.
**5. שרטוט:**
![שרטוט הגרף של y = (x−1)e^x בין x=−3 ל-x=2, עם אסימפטוטה אופקית y=0 משמאל](images/exams/17A2-A-Q1-graph.png)
"""

SOL2 = r"""
מתקיים $a_1=5$, $a_2=2.9,\dots$ השערה: הסדרה יורדת וחסומה מלרע. אם זה נכון, אז הסדרה מתכנסת וגבולה מקיים את המשוואה:
$$L=\frac12\left(L+\frac4L\right),\quad L^2=4,\quad L=2$$
(על פניו הסדרה חיובית). במקרה זה $L=2$ הוא החסם התחתון של הסדרה.
נוכיח באינדוקציה שהסדרה באמת חסומה מלרע ע"י $2$. בסיס האינדוקציה: $a_1=5>2$.
שלב האינדוקציה: נניח ש-$a_n>2$, בפרט $a_n$ חיובי וניתן להשתמש באי-שוויון הממוצעים:
$$a_{n+1}=\frac12\left(a_n+\frac4{a_n}\right)\ge\sqrt{a_n\cdot\frac4{a_n}}=2$$
נותר להראות כי הסדרה מונוטונית יורדת. נקבל:
$$\frac{a_{n+1}}{a_n}=\frac12\left(1+\frac4{a_n^2}\right)<\frac12\left(1+\frac44\right)=1$$
כלומר הסדרה יורדת. לפי חישוב עזר שעשינו מקודם $L=2$.
"""

SOL3A = r"""
מתקיים
$$\lim_{x\to+\infty}x\ln\frac{x+1}{x-1}=\{\infty\cdot0\}=\lim_{x\to+\infty}\frac{\ln\frac{x+1}{x-1}}{\frac1x}=\lim_{x\to+\infty}\frac{\ln(x+1)-\ln(x-1)}{\frac1x}=\lim_{x\to+\infty}\frac{\frac{1}{x+1}-\frac{1}{x-1}}{-\frac{1}{x^2}}=$$
$$=\lim_{x\to+\infty}\frac{\frac{-2}{x^2-1}}{-\frac{1}{x^2}}=\lim_{x\to+\infty}\frac{2x^2}{x^2-1}=2$$
**דרך אחרת:**
$$\lim_{x\to+\infty}x\ln\frac{x+1}{x-1}=\{\infty\cdot0\}=\lim_{x\to+\infty}\ln\left(\frac{x+1}{x-1}\right)^x=\lim_{x\to+\infty}\ln\left(1+\frac{2}{x-1}\right)^x=$$
$$=\lim_{x\to+\infty}\ln\left(\left(1+\frac{2}{x-1}\right)^{\frac{x-1}{2}}\right)^{\frac{2}{x-1}\cdot x}=\ln e^2=2$$
"""

SOL3B = r"""
התחום המסתובב נראה כך:
![התחום הכלוא בין y = 4/x לבין y = 5 − x, מסומן בכחול](images/exams/17A2-A-Q3b-fig.png)
נקודות החיתוך של $y=5-x$ ו-$y=\frac4x$ הן $x=1$ ו-$x=4$. נחשב את הנפח לפי שיטת הפרוסות:
$$V=\pi\int_1^4\left((5-x)^2-\frac{4^2}{x^2}\right)dx=\pi\int_1^4\left(25-10x+x^2-\frac{16}{x^2}\right)dx=\pi\left(25x-5x^2+\frac{x^3}{3}+\frac{16}{x}\right)\Big|_1^4=9\pi$$
"""

SOL4A = r"""
נתון שהפונקציות משיקות זו לזו, פירוש הדבר: יש להן אותה נגזרת בנקודת ההשקה:
$$-\frac{1}{x^2}=-x,\quad x^3=1,\quad x=1$$
בנוסף לזה לפונקציות אותו ערך בנקודת ההשקה: $f(1)=g(1)$, כלומר $1=-\frac12+k$, $k=1.5$. נקודת ההשקה היא $(1,1)$.
"""

SOL4B = r"""
נגזור את הפונקציה: $y'=\frac{x^3}{2}-\frac{1}{2x^3}$. לפי הנוסחה של אורך קשת נקבל
$$L=\int_1^4\sqrt{1+\left(\frac{x^3}{2}-\frac{1}{2x^3}\right)^2}\,dx=\int_1^4\sqrt{\frac{x^{12}+2x^6+1}{4x^6}}\,dx=\int_1^4\sqrt{\left(\frac{x^6+1}{2x^3}\right)^2}\,dx=$$
$$=\int_1^4\frac{x^6+1}{2x^3}\,dx=\int_1^4\left(\frac{x^3}{2}+\frac{1}{2x^3}\right)dx=\left(\frac{x^4}{8}-\frac{1}{4x^2}\right)\Big|_1^4=\frac{2055}{64}$$
![גרף העקומה y = x⁴/8 + 1/(4x²) בקטע מ-1 עד 4](images/exams/17A2-A-Q4b-graph.png)
"""

SOL5A = r"""
משפט לגרנז' אומר שאם $f(x)$ רציפה בקטע $[a,b]$ וגזירה בקטע $(a,b)$ אז קיימת נקודה $a<c<b$ כך ש-$f'(c)=\frac{f(b)-f(a)}{b-a}$.
הפונקציה $f(x)=2x^2+5x-7$ מקיימת את כל התנאים הללו בכל קטע. מתקיים $f'(c)=4c+5$,
$$\frac{f(b)-f(a)}{b-a}=\frac{\left(2b^2+5b-7\right)-\left(2a^2+5a-7\right)}{b-a}=\frac{2b^2-2a^2+5b-5a}{b-a}=\frac{2(b-a)(b+a)+5(b-a)}{b-a}=2b+2a+5$$
לכן לפי משפט לגרנז' נקבל $2b+2a+5=4c+5$, $c=\frac{a+b}{2}$, אמצע הקטע.
"""

SOL5B = r"""
מתקיים:
$$\int x^3e^{-x^2}dx=\int x^2e^{-x^2}\cdot x\,dx=\left[\begin{matrix}t=x^2\\dt=2x\,dx\end{matrix}\right]=\frac12\int te^{-t}dt=\left[\begin{matrix}u=t&dv=e^{-t}dt\\du=dt&v=-e^{-t}\end{matrix}\right]=\frac12\left(-e^{-t}t+\int e^{-t}dt\right)=$$
$$=\frac12\left(-e^{-t}t-e^{-t}\right)+c=-\frac12e^{-x^2}\left(x^2+1\right)+c$$
"""

SOL6A = r"""
נחשב את הגבולות החד-צדדיים של הפונקציה ב-$0$ בעזרת כלל לופיטל:
$$\lim_{x\to0^-}\frac{e^{ax}-a^{-ax}}{\ln(1+bx)}=\lim_{x\to0^-}\frac{ae^{ax}+a^{-ax}a\ln a}{\frac{b}{1+bx}}=\frac{(1+\ln a)a}{b}$$
$$\lim_{x\to0^+}\frac{2x}{\arcsin(ax)}=\lim_{x\to0^+}\frac{2}{\frac{a}{\sqrt{1-a^2x^2}}}=\frac2a$$
על מנת שהפונקציה תהיה רציפה ב-$0$, הגבולות החד-צדדים חייבים להיות שווים זה לזה ולערכה של הפונקציה ב-$0$. כלומר:
$$\frac{(1+\ln a)a}{b}=\frac2a=4$$
מכאן $a=0.5$, $b=\frac{1+\ln0.5}{8}$.
"""

SOL6B = r"""
מתקיים
$$\frac{1}{x^4-1}=\frac{1}{\left(x^2-1\right)\left(x^2+1\right)}=\frac{1}{(x-1)(x+1)\left(x^2+1\right)}=\frac{A}{x-1}+\frac{B}{x+1}+\frac{Cx+D}{x^2+1}$$
כאשר $A=\frac14$, $B=-\frac14$, $C=0$, $D=-\frac12$. לכן
$$\int\frac{dx}{x^4-1}=\frac14\int\frac{dx}{x-1}-\frac14\int\frac{dx}{x+1}-\frac12\int\frac{dx}{x^2+1}=\frac14\ln|x-1|-\frac14\ln|x+1|-\frac12\arctan x+c=\frac14\ln\left|\frac{x-1}{x+1}\right|-\frac12\arctan x+c$$
**הערה:** ניתן לפרק את הביטוי בתוך האינטגרל בדרך מקוצרת:
$$\frac{1}{x^4-1}=\frac{1}{\left(x^2-1\right)\left(x^2+1\right)}=\left[z=x^2\right]=\frac{1}{(z-1)(z+1)}=\frac{A}{z-1}+\frac{B}{z+1},\qquad A=\frac12,\ B=-\frac12$$
אזי
$$\frac{1}{x^4-1}=\frac12\cdot\frac{1}{x^2-1}-\frac12\cdot\frac{1}{x^2+1}$$
$$\int\frac{dx}{x^4-1}=\frac12\int\frac{dx}{x^2-1}-\frac12\int\frac{dx}{x^2+1}=\frac14\ln\left|\frac{x-1}{x+1}\right|-\frac12\arctan x+c$$
"""

HEAD1 = (r"חקרו את הפונקציה הבאה $y=(x-1)e^x$ על פי הסעיפים הבאים: תחום הגדרה, תחומי עליה וירידה, "
         "נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.")

questions = [
    Q(1, "computation", "function_investigation", HEAD1, SOL1),

    Q(2, "proof", "sequences_limits",
      r"הוכיחו כי הסדרה הבאה מתכנסת ומצאו את גבולה: $a_1=5,\quad a_{n+1}=\frac12\left(a_n+\frac{4}{a_n}\right)$.",
      SOL2, points=20),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to+\infty}x\ln\frac{x+1}{x-1}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום המישורי הכלוא בין הקווים $xy=4,\ x+y=5$ סביב ציר ה-$x$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "derivatives_tangents",
      r"הפונקציות $f(x)=\frac1x$ ו-$g(x)=-\frac12x^2+k$ משיקות זו לזו. מצאו את $k$ ונקודת ההשקה.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"מצאו את אורך הקשת של העקומה $y=\frac{x^4}{8}+\frac{1}{4x^2}$ מ-$x=1$ ל-$x=4$.",
      SOL4B, part="ב", points=10),

    Q(5, "proof", "mean_value_theorems",
      r"נתונה הפונקציה $f(x)=2x^2+5x-7$. הראו כי הנקודה $c$ במשפט ערך הביניים של לגרנז' היא תמיד אמצע הקטע $[a,b]$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל: $\int x^3\cdot e^{-x^2}\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "continuity",
      r"עבור אילו ערכים של $a$ ו-$b$ הפונקציה "
      r"$f(x)=\begin{cases}\dfrac{e^{ax}-a^{-ax}}{\ln(1+bx)},&x<0\\[2mm]4,&x=0\\[2mm]\dfrac{2x}{\arcsin(ax)},&x>0\end{cases}$ "
      r"תהיה רציפה ב-$0$?",
      SOL6A, part="א", points=10),

    Q(6, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{dx}{x^4-1}$.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "17A2-A",
    "examLabel": "מבחן סוף סמסטר א' תשע\"ז, מועד א', גרסה 2",
    "year": 2017,
    "examDate": "06/02/2017",
    "sourceFile": "calculus-1/17A2-A exam+solution.pdf",
    "solutionFile": "calculus-1/17A2-A exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

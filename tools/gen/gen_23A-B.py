# -*- coding: utf-8 -*-
"""Generator for tools/raw/23A-B.json -- calculus-1 (20151), semester B 2023, moed A (19/06/2023).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23A-B.py

Source: sitting 23A-B, pp.1-7 (typed exam with the official worked solution; Q4a and Q4b solutions are handwritten
pages inside the same official PDF, transcribed to text; no handwriting crops are shipped).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each). Weight of every question 20%.

Transcription notes
- Official solution transcribed in full, as printed. Rubric and steps are intentionally not written.
- Q1: the official graph (p.2) is shipped as a figure (a red pen annotation next to it was whited out; the pen
  arrow and circle marking the open point (0,1) remain).
- Q4b: the handwritten region sketch is described in words in the question, not shipped.
- Q6b (as printed): the bound is written 1/(3000*0.9^3) = 0.00045; the exact value is 0.000457, so 0.00045 is a
  truncation (the actual error is 0.00036). Final answer ln 0.9 ~ -0.105 is correct.

Checks (tools/verify/23A-B/check.py, sympy): every derivative, limit, integral, sign table, volume, area and the
Taylor estimate match the official answers.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23A-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**א.** תחום הגדרה הוא $D=\{x>0,\ x\neq1\}$.
**ב.** נק' חיתוך עם הצירים היא $(e,0)$.
**ג.** $f'(x)=\frac{\frac{1}{x}\ln x-(\ln x-1)\frac{1}{x}}{(\ln x)^2}=\frac{\frac{1}{x}}{(\ln x)^2}>0$ ולכן הפונקציה עולה ממש כל הזמן ללא נקודת קיצון.
**ד.** $f''(x)=\frac{-(\ln x+2)}{x^2(\ln x)^3}$ ולכן פונקציה קעורה כאשר $e^{-2}<x<1$ וקמורה כאשר $x>1$ או $x<e^{-2}$. בנקודה $x=e^{-2}$ הפונקציה בעלת נקודת פיתול.
**ה. אסימפטוטות:** אם נחשב $\begin{cases}\lim_{x\to1^-}f(x)=+\infty\\ \lim_{x\to1^+}f(x)=-\infty\end{cases}$, אז נקבל שקו ישר $x=1$ מהווה אסימפטוטה אנכית לגרף הפונקציה. בנוסף, $\begin{cases}\lim_{x\to+\infty}\frac{f(x)}{x}=0\\ \lim_{x\to+\infty}f(x)=1\end{cases}$ ולכן קו ישר $y=1$ מהווה אסימפטוטה אופקית באינסוף לגרף הפונקציה.
נקי' אי-רציפות מימין בנק' $x=0$: $\lim_{x\to0^+}f(x)=1$.

![הגרף הרשמי של הפונקציה](images/exams/23A-B-Q1-graph.png)
"""

SOL2A = r"""
מנות פולינומים והדרגה במונה קטנה מהדרגה במכנה. לכן נפרק לסכום של מנות פולינומים:
$$\frac{2x^2+x+4}{(x+1)(x^2+4)}=\frac{A}{x+1}+\frac{Bx+C}{x^2+4}$$
$$A(x^2+4)+(Bx+C)(x+1)=2x^2+x+4\Rightarrow$$
מכאן
$$x=0\Rightarrow4A+C=4$$
$$x=-1\Rightarrow5A=5\Rightarrow A=1\Rightarrow C=0$$
$$x=1\Rightarrow5A+(B+C)\cdot2=7\Rightarrow5+2B=7\Rightarrow B=1$$
לכן:
$$\int\frac{2x^2+x+4}{(x+1)(x^2+4)}dx=\int\frac{1}{x+1}dx+\int\frac{x}{x^2+4}dx=\ln|x+1|+\frac{1}{2}\ln(x^2+4)+C$$
"""

SOL2B = r"""
$$a_1=3$$
$$a_2=\frac{1}{2}\left(3+\frac{7}{3}\right)=\frac{8}{3}<3$$
$$a_3=\frac{1}{2}\left(\frac{8}{3}+\frac{21}{8}\right)=\frac{127}{48}<\frac{8}{3}$$
נראה באינדוקציה כי הסדרה יורדת וחיובית.
**הוכחת חסימות:** קודם כל, לפי אי שיוויון הממוצעים, $a_{n+1}=\frac{1}{2}\left(a_n+\frac{7}{a_n}\right)\ge\sqrt{a_n\cdot\frac{7}{a_n}}=\sqrt{7}$. לכן לכל $n$, $a_n\ge\sqrt{7}$.
**הוכחת מונוטוניות:** $a_1=3$. $a_2=\frac{1}{2}\left(3+\frac{7}{3}\right)=\frac{8}{3}<3=a_1$. נניח $a_n<a_{n-1}$. צריך להוכיח כי $a_{n+1}<a_n$.
נסתכל על
$$a_{n+1}-a_n=\frac{1}{2}\left(a_n+\frac{7}{a_n}\right)-a_n=-\frac{1}{2}a_n+\frac{7}{2a_n}=\frac{7-a_n^2}{2a_n}=\frac{\left[\sqrt{7}-a_n\right]\left[\sqrt{7}+a_n\right]}{2a_n}$$
המכנה שלילי כי $a_n\ge\sqrt{7}$ ו-$a_n>0$. המכנה חיובי.
לכן $a_{n+1}-a_n<0$. לכן הסדרה מונוטונית יורדת.
כמו כן הסדרה חסומה מלרע כי ראינו כי $a_n\ge\sqrt{7}$. ולפי משפט סידרה מונוטונית וחסומה מתכנסת.
נניח שהגבול הוא $L$, כך ש-$\lim_{n\to\infty}a_n=\lim_{n\to\infty}a_{n+1}=L$.
מתוך ההגדרה הרקורסיבית של הסדרה $a_{n+1}=\frac{1}{2}\left(a_n+\frac{7}{a_n}\right)$ ואריתמטיקה של גבולות נקבל:
$$L=\frac{1}{2}\left(L+\frac{7}{L}\right)\Rightarrow\frac{1}{2}L=\frac{7}{2L}\Rightarrow L^2=7\Rightarrow L=\pm\sqrt{7}$$
אבל הסדרה חיובית ולכן לא ייתכן שהגבול שלה שלילי. לכן $L=\sqrt{7}$.
"""

SOL3A = r"""
$$\lim_{x\to0}\frac{\int_0^{x^4}(1+t)^{\frac{2}{t}}dt}{x^4}=\lim_{x\to0}\frac{(1+x^4)^{\frac{2}{x^4}}4x^3}{4x^3}=\lim_{x\to0}(1+x^4)^{\frac{2}{x^4}}=e^2$$
"""

SOL3B = r"""
$$\int\frac{dx}{x\cdot(\ln^2x+2\ln x+5)}\left\{\begin{matrix}t=\ln x\\ dt=\frac{dx}{x}\end{matrix}\right\}=\int\frac{dt}{(t^2+2t+5)}$$
$$=\int\frac{dt}{(t+1)^2+2^2}=\frac{1}{2}\arctan\frac{(t+1)}{2}+C=\frac{1}{2}\arctan\frac{(\ln(x)+1)}{2}+C$$
"""

SOL4A = r"""
נגדיר הפונקציה $f(x)=(x+2)\sqrt{4-x^2}$. הפונקציה היא רציפה ב-$[-2,2]$ ו-$f(-2)=f(2)=0$.
$$f'(x)=\sqrt{4-x^2}+(x+2)\frac{1}{2}(4-x^2)^{-\frac{1}{2}}(-2x)=(4-x^2)^{\frac{1}{2}}-\frac{x^2+2x}{(4-x^2)^{\frac{1}{2}}}$$
$$=\frac{-2x^2-2x+4}{(4-x^2)^{\frac{1}{2}}}=-2\cdot\frac{x^2+x-2}{(4-x^2)^{\frac{1}{2}}},$$
$f'(x)=0\iff x^2+x-2=0\iff x=\begin{cases}1\\-2\end{cases}$.
$$\Rightarrow f'(x)=-2\frac{(x-1)(x+2)}{(2-x)^{\frac{1}{2}}(2+x)^{\frac{1}{2}}}=-2\frac{(x-1)(x+2)^{\frac{1}{2}}}{(2-x)^{\frac{1}{2}}}$$
אזי הפונקציה רציפה ב-$[-2,2]$ וגזירה ב-$(-2,2)$.
$f(1)=3\sqrt{3}$. כך ש-$x=1$ מקסימום מוחלט של $f$ ב-$[-2,2]$.
לכן: $f(x)\le f(1)=3\sqrt{3}\quad\forall x\in[-2,2]$.
"""

SOL4B = r"""
נגדיר הפונקציה $y=f(x)=\sqrt{x\ln x}$; $y(1)=0$, $y(2)\approx1.177$, $y(e)\approx1.64$. התחום הוא בין הגרף של $f$ לציר ה-$X$ בין $x=1$ ל-$x=e$.
$$V=\pi\int_1^ef^2(x)\,dx=\pi\int_1^ex\ln x\,dx=\left|\begin{matrix}u=\ln x & du=\frac{1}{x}dx\\ dv=x\,dx & v=\frac{1}{2}x^2\end{matrix}\right|=$$
$$=\pi\left(\frac{1}{2}x^2\ln x\Big|_1^e-\frac{1}{2}\int_1^ex\,dx\right)=\pi\left(\frac{e^2}{2}-\frac{1}{2}\frac{x^2}{2}\Big|_1^e\right)=$$
$$=\pi\left(\frac{e^2}{2}-\left(\frac{e^2}{4}-\frac{1}{4}\right)\right)=\pi\left(\frac{e^2}{4}+\frac{1}{4}\right)=\frac{\pi}{4}\left(e^2+1\right)$$
"""

SOL5A = r"""
$$\lim_{x\to1}x^{\frac{1}{\sin(2x-2)}}=\lim_{x\to1}(1+x-1)^{\frac{1}{\sin(2x-2)}}$$
$$=\lim_{x\to1}(1+x-1)^{\frac{x-1}{(x-1)\sin(2x-2)}}=\sqrt{e}$$
"""

SOL5B = r"""
$$\lim_{\Delta x\to0}\frac{\Delta x\arctan\frac{1}{\Delta x^2}-0}{\Delta x}=\lim_{\Delta x\to0}\arctan\frac{1}{\Delta x^2}=\frac{\pi}{2}$$
"""

SOL6A = r"""
$$y=\frac{3}{9+x^2},\qquad y=\frac{1}{1+x^2}$$
$$\frac{3}{9+x^2}=\frac{1}{1+x^2},\qquad3+3x^2=9+x^2,\qquad x^2=3,\ x=\pm\sqrt{3}$$
$$S=2S_1=2\int_0^{\sqrt{3}}\left(\frac{1}{1+x^2}-\frac{3}{9+x^2}\right)dx=2\left(\arctan x-3\cdot\frac{1}{3}\arctan\frac{x}{3}\right)\Big|_0^{\sqrt{3}}=$$
$$=2\left(\arctan\sqrt{3}-\arctan\frac{\sqrt{3}}{3}\right)=2\left(\frac{\pi}{3}-\frac{\pi}{6}\right)=\frac{\pi}{3}$$
תשובה: $\frac{\pi}{3}$
"""

SOL6B = r"""
$$\ln(1+x)=x-\frac{x^2}{2}+R_2(x),\qquad R_2(x)=\frac{\left(\ln(1+x)\right)^{(3)}(c)}{3!}x^3=\frac{1}{3(1+c)^3}x^3,$$
$c$ בין $x$ ל-$0$.
$$\ln0.9=\ln(1+(-0.1))=-0.1-\frac{(-0.1)^2}{2}+R_2(x)\approx-0.105,$$
$$R_2(x)=\frac{1}{3(1+c)^3}(-0.1)^3,\qquad-0.1<c<0$$
$$|R_2(x)|=\left|\frac{1}{3(1+c)^3}(-0.1)^3\right|<\frac{1}{3000\cdot0.9^3}=0.00045=\delta$$
תשובה: $\ln0.9\approx-0.105,\qquad\delta<0.00045$
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=\frac{\ln(x)-1}{\ln(x)}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, "
      "תחומי עליה וירידה, נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{2x^2+x+4}{(x+1)(x^2+4)}\,dx$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "sequences_limits",
      r"נתונה הסדרה: $a_1=3,\ a_{n+1}=\frac{1}{2}\left(a_n+\frac{7}{a_n}\right)$." "\nהוכיחו כי הסדרה מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "lhopital_taylor",
      r"חשבו את הגבול הבא: $\lim_{x\to0}\frac{\int_0^{x^4}(1+t)^{\frac{2}{t}}\,dt}{x^4}$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{dx}{x\cdot(\ln^2x+2\ln x+5)}$.",
      SOL3B, part="ב", points=10),

    Q(4, "proof", "extrema_optimization",
      r"הוכיחו כי לכל $x\in[-2,2]$ מתקיים את האי-שוויון הבא: $(x+2)\sqrt{4-x^2}\le3\sqrt{3}$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר מסיבוב של התחום המישורי הכלוא בין הקווים: $y=\sqrt{x\ln x},\ y=0,\ x=1,\ x=e$ סביב ציר ה-$X$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to1}x^{\frac{1}{\sin(2x-2)}}$.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "derivatives_tangents",
      r"נתונה הפונקציה $f(x)=\begin{cases}x\arctan\frac{1}{x^2}, & x\neq0\\ 0, & x=0\end{cases}$"
      "\n" r"בדקו האם הפונקציה גזירה בנקודה $x=0$. אם כן, מצאו את הנגזרת, אם לא, נמקו.",
      SOL5B, part="ב", points=10),

    Q(6, "computation", "definite_integrals",
      r"חשבו את השטח הכלוא בין הגרפים של הפונקציות: $y=\frac{3}{9+x^2},\ y=\frac{1}{1+x^2}$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "lhopital_taylor",
      r"חשבו בקירוב $\ln(0.9)$ באמצעות נוסחת מקלורן מסדר 2 של פונקציה $y=\ln(1+x)$ והעריכו את שגיאת החישוב.",
      SOL6B, part="ב", points=10),
]

exam = {
    "examCode": "23A-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ג, מועד א'",
    "year": 2023,
    "examDate": "19/06/2023",
    "sourceFile": "calculus-1/23A-B exam+solution.pdf",
    "solutionFile": "calculus-1/23A-B exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

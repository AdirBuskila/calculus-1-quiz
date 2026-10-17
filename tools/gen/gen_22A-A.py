# -*- coding: utf-8 -*-
"""Generator for tools/raw/22A-A.json -- calculus-1 (20151), semester A 2022, moed A (25/01/2022).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22A-A.py

Source: sitting 22A-A, pp.1-2 (printed exam), pp.3-9 (the lecturer's handwritten solutions, symbolic in A, B, C).
Instructions: 3 hours, solve 5 of 6 questions, 20% each (two parts of 10% each). Parameters A, B, C appear in some parts
(last three digits of the student's ID; the example in the header gives A=7, B=8, C=9).

Transcription notes
- The parameter rule from the header is shipped as shared context c0 and attached to every part that uses A, B or C.
- Q1b, Q2a: the handwritten reasoning lines are partly hard to read (cut off at the margin); the Hebrew connective words
  of those lines are the transcriber's reading, the formulas are exact.
- Q4: the solution page writes 'x != -1' as the reason for choosing x=1; transcribed as the domain condition x>0 of ln x
  (the only point where the slopes agree in the domain is x=1).
- Q5a: the handwritten derivative has a stray factor 2 in the last term (2x^2/sqrt((1-x^2)^3)); the correct term
  x^2/(1-x^2)^(3/2) is written here (the sign conclusion f'<=0 is unchanged).
- Q5b and Q6b: the hand-drawn sketches of the solution are shipped as images.

Checks (tools/verify/22A-A/check.py, sympy plus numeric iteration over all digit values): every limit, derivative,
antiderivative, tangent line, area and volume matches the official answers. 0 mismatches.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22A-A.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


CTX0 = (r"בחלק מסעיפי המבחן מופיעים הפרמטרים $A$, $B$ ו-$C$. חובה להציב בתחילת הפתרון לכל שאלה את ערכי הפרמטרים, "
        r"בהתאם לשלוש הספרות האחרונות של מספר תעודת הזהות שלכם: למשל עבור ת.ז. 123456789 נקבל $A=7$, $B=8$, $C=9$. "
        r"שאלות בהן $A$, $B$ ו-$C$ יוצבו רק בשלב התשובה הסופית לא ייבדקו.")

SOL1A = r"""
תחום הגדרה: $D(f)=(-\infty,\infty)$.
$$f'(x)=\frac{4}{5}-\frac{4}{5}\cdot\frac{1}{\sqrt[5]{x-1}}=\frac{4}{5}\cdot\frac{\sqrt[5]{x-1}-1}{\sqrt[5]{x-1}}$$
$f'(x)=0$ כאשר $\sqrt[5]{x-1}=1$, כלומר $x=2$. בנקודה $x=1$ הנגזרת $f'(x)$ אינה קיימת.
הנקודות החשודות בקטע $[0,3]$ הן: $1,\ 2,\ 0,\ 3$.
$$f(0)=1,\quad f(1)=\frac{14}{5},\quad f(2)=\frac{13}{5},\quad f(3)=\frac{22}{5}-\sqrt[5]{16}\approx 2.66$$
$$\max_{[0,3]}f=f(1)=\frac{14}{5},\qquad \min_{[0,3]}f=f(0)=1$$
"""

SOL1B = r"""
לפי אי-שוויון הממוצעים:
$$a_{n+1}=\frac{1}{2}\left(a_n+\frac{A+1}{a_n}\right)\ge\sqrt{a_n\cdot\frac{A+1}{a_n}}=\sqrt{A+1}$$
לכן הסדרה חסומה מלמטה על ידי $\sqrt{A+1}$.
$$a_{n+1}-a_n=\frac{1}{2}\left(a_n+\frac{A+1}{a_n}\right)-a_n=\frac{1}{2}\left(\frac{A+1}{a_n}-a_n\right)=\frac{1}{2}\cdot\frac{(A+1)-a_n^2}{a_n}=\frac{\left(\sqrt{A+1}-a_n\right)\left(\sqrt{A+1}+a_n\right)}{2a_n}\le 0$$
לכן הסדרה יורדת. מכיוון שהיא יורדת וחסומה מלמטה, יש לה גבול. נסמן אותו ב-$L$. נעבור לגבול בנוסחת הנסיגה:
$$L=\frac{1}{2}\left(L+\frac{A+1}{L}\right)\ \Rightarrow\ L^2=A+1\ \Rightarrow\ L=\sqrt{A+1}$$
או $L=-\sqrt{A+1}$.
מכיוון ש-$a_n\ge 0$ מתקבל:
$$\lim_{n\to\infty}a_n=\sqrt{A+1}$$
"""

SOL2A = r"""
$$\lim_{n\to\infty}\left(\sqrt{n^2+C+1}-n\right)\sin\left(2^{(B+1)n}\right)=\lim_{n\to\infty}\frac{n^2+C+1-n^2}{\sqrt{n^2+C+1}+n}\cdot\sin\left(2^{(B+1)n}\right)=0$$
כי $-1\le\sin\left(2^{(B+1)n}\right)\le 1$ (סדרה חסומה), והסדרה $\frac{C+1}{\sqrt{n^2+C+1}+n}$ שואפת ל-$0$.
"""

SOL2B = r"""
$$\int x\arctan\left(x^2\right)dx=\left|\begin{array}{l}t=x^2\\ dt=2x\,dx\end{array}\right|=\frac{1}{2}\int\arctan t\,dt=$$
$$=\left|\begin{array}{ll}u=\arctan t & du=\frac{dt}{1+t^2}\\ dv=dt & v=t\end{array}\right|=\frac{1}{2}\left(t\arctan t-\int\frac{t\,dt}{1+t^2}\right)=$$
$$=\frac{1}{2}\left(t\arctan t-\frac{1}{2}\ln\left(1+t^2\right)\right)+c=\frac{1}{2}\left(x^2\arctan\left(x^2\right)-\frac{1}{2}\ln\left(1+x^4\right)\right)+c$$
"""

SOL3A = r"""
$$f(x)=\frac{(A+2)\,x\,|x-B-1|}{\left(2x^2-(2B+3)x+B+1\right)\arctan\left((C+3)x\right)}$$
$$2x^2-(2B+3)x+B+1=0\ \Rightarrow\ x=\frac{1}{2},\ x=B+1$$
$$f(x)=\frac{(A+2)\,x\,|x-(B+1)|}{2\left(x-\frac{1}{2}\right)\left(x-(B+1)\right)\arctan\left((C+3)x\right)}$$
הנקודות החשודות כנקודות אי-רציפות הן: $x=0,\ x=\frac{1}{2},\ x=B+1$.
$$\lim_{x\to0}f(x)=\frac{(A+2)\,|-(B+1)|}{2\cdot\left(-\frac{1}{2}\right)\left(-(B+1)\right)}\lim_{x\to0}\frac{x}{\arctan\left((C+3)x\right)}=(A+2)\lim_{x\to0}\frac{1}{\frac{C+3}{1+(C+3)^2x^2}}=\frac{A+2}{C+3}$$
לכן $x=0$ היא נקודת אי-רציפות סליקה.
$$\lim_{x\to\frac{1}{2}}f(x)=\frac{(A+2)\cdot\frac{1}{2}\left|\frac{1}{2}-(B+1)\right|}{2\left(\frac{1}{2}-(B+1)\right)\arctan\frac{C+3}{2}}\lim_{x\to\frac{1}{2}}\frac{1}{x-\frac{1}{2}}=\infty$$
לכן $x=\frac{1}{2}$ היא נקודת אי-רציפות מסוג שני.
$$\lim_{x\to B+1}f(x)=\frac{(A+2)(B+1)}{2\left(B+1-\frac{1}{2}\right)\arctan\left((C+3)(B+1)\right)}\lim_{x\to B+1}\frac{|x-(B+1)|}{x-(B+1)}$$
הגבול $\lim_{x\to B+1}\frac{|x-(B+1)|}{x-(B+1)}$ אינו קיים, אך הגבול הימני שלו שווה ל-$1$ והגבול השמאלי שלו שווה ל-$-1$. לכן $x=B+1$ היא נקודת אי-רציפות מסוג ראשון.
"""

SOL3B = r"""
נמצא את הנגזרת של $f$ ב-$x=0$ לפי ההגדרה:
$$f'(0)=\lim_{h\to0}\frac{f(h)-f(0)}{h}$$
נעבור לגבולות חד-צדדיים.
$$\lim_{h\to0^+}\frac{f(h)-f(0)}{h}=\lim_{h\to0^+}\frac{e^{ph}-ph-1}{h^2}=\left\{\tfrac{0}{0}\right\}=\lim_{h\to0^+}\frac{pe^{ph}-p}{2h}=\left\{\tfrac{0}{0}\right\}=\lim_{h\to0^+}\frac{p^2e^{ph}}{2}=\frac{p^2}{2}$$
$$\lim_{h\to0^-}\frac{f(h)-f(0)}{h}=\lim_{h\to0^-}\frac{h-\sin h}{h^3}=\left\{\tfrac{0}{0}\right\}=\lim_{h\to0^-}\frac{1-\cos h}{3h^2}=\left\{\tfrac{0}{0}\right\}=\lim_{h\to0^-}\frac{\sin h}{6h}=\frac{1}{6}$$
לכן $f$ גזירה ב-$0$ אם ורק אם $\frac{p^2}{2}=\frac{1}{6}$, כלומר $p=\pm\frac{1}{\sqrt{3}}$.
"""

SOL4A = r"""
עבור הפונקציה $y=2(A+1)\ln x+C$ נקבל $y'=\frac{2(A+1)}{x}$.
ועבור הפונקציה $y=(A+1)\left(x^2-1\right)+C$ נקבל $y'=2(A+1)x$.
מכאן נקבל שהנגזרות שוות כאשר $\frac{2(A+1)}{x}=2(A+1)x$, כלומר $x^2=1$. מכיוון שתחום ההגדרה של $\ln x$ הוא $x>0$, מתקבל $x=1$.
שתי הפונקציות נחתכות ב-$x=1$ כי בנקודה זו $y=C$ בשתיהן, ולכן $x=1$ היא נקודת ההשקה והשיפוע המשותף הוא $2(A+1)$. משוואת המשיק:
$$y-C=2(A+1)(x-1)$$
כלומר $y=2(A+1)x-2A+C-2$.
"""

SOL4B = r"""
$$\frac{3x^3+x^2+4x+8}{x^2\left(x^2+4\right)}=\frac{A}{x^2}+\frac{B}{x}+\frac{Cx+D}{x^2+4}=\frac{A\left(x^2+4\right)+Bx\left(x^2+4\right)+(Cx+D)x^2}{x^2\left(x^2+4\right)}$$
נמצא את המקדמים מהשוואת הפולינומים (כאן $A,B,C,D$ הם מקדמי הפירוק ולא הפרמטרים של המבחן):
$$\begin{array}{c|l}x^3 & B+C=3\\ x^2 & A+D=1\\ x & 4B=4\\ 1 & 4A=8\end{array}\ \Longrightarrow\ A=2,\ B=1,\ C=2,\ D=-1$$
$$\int\frac{3x^3+x^2+4x+8}{x^2\left(x^2+4\right)}dx=\int\left(\frac{2}{x^2}+\frac{1}{x}+\frac{2x-1}{x^2+4}\right)dx=\int\left(\frac{2}{x^2}+\frac{1}{x}+\frac{2x}{x^2+4}-\frac{1}{x^2+4}\right)dx$$
$$=-\frac{2}{x}+\ln|x|+\ln\left(x^2+4\right)-\frac{1}{2}\arctan\frac{x}{2}+c$$
"""

SOL5A = r"""
נגדיר $f(x)=\arcsin x-\frac{x}{\sqrt{1-x^2}}$. אז
$$f'(x)=\frac{1}{\sqrt{1-x^2}}-\frac{\sqrt{1-x^2}-x\cdot\frac{-x}{\sqrt{1-x^2}}}{1-x^2}=\frac{1}{\sqrt{1-x^2}}-\frac{1}{\sqrt{1-x^2}}-\frac{x^2}{\sqrt{\left(1-x^2\right)^3}}\le 0$$
לכן $f$ יורדת. מכיוון ש-$f(0)=0$ נקבל עבור $x\in[0,1)$ כי $f(x)\le 0$, כלומר
$$\arcsin x\le\frac{x}{\sqrt{1-x^2}}$$
"""

SOL5B = r"""
נמצא את נקודות החיתוך של שני הגרפים:
$$\frac{A+2}{1+x^2}+B=\frac{(A+2)x^2}{2}+B\ \Rightarrow\ \frac{1}{1+x^2}=\frac{x^2}{2}\ \Rightarrow\ x^4+x^2-2=0$$
נסמן $t=x^2\ge 0$: $t^2+t-2=0$, ולכן $t=-2$ (לא מתקבל, כי $t\ge 0$) או $t=1$. מכאן $x=\pm 1$.
![שרטוט שני הגרפים והתחום הכלוא ביניהם](images/exams/22A-A-Q5b-sketch.png)
$$S=2\int_0^1\left(\frac{A+2}{1+x^2}+B-\left(\frac{(A+2)x^2}{2}+B\right)\right)dx=2(A+2)\int_0^1\left(\frac{1}{1+x^2}-\frac{x^2}{2}\right)dx=2(A+2)\left(\arctan x-\frac{x^3}{6}\right)\Big|_0^1$$
$$=2(A+2)\left(\frac{\pi}{4}-\frac{1}{6}\right)$$
"""

SOL6A = r"""
$$\lim_{x\to0}\frac{x-\arcsin x}{\int_0^x\ln\left(1+t^2\right)dt}=\left\{\tfrac{0}{0}\right\}\overset{\text{L'H}}{=}\lim_{x\to0}\frac{1-\frac{1}{\sqrt{1-x^2}}}{\ln\left(1+x^2\right)}=\lim_{x\to0}\frac{\sqrt{1-x^2}-1}{\sqrt{1-x^2}\,\ln\left(1+x^2\right)}$$
$$=\lim_{x\to0}\frac{1-x^2-1}{\sqrt{1-x^2}\left(\sqrt{1-x^2}+1\right)\ln\left(1+x^2\right)}=-\lim_{x\to0}\frac{x^2}{\ln\left(1+x^2\right)}\cdot\frac{1}{\sqrt{1-x^2}\left(\sqrt{1-x^2}+1\right)}=-\frac{1}{2}$$
(כאשר $\lim_{x\to0}\frac{x^2}{\ln\left(1+x^2\right)}=1$.)
"""

SOL6B = r"""
![שרטוט התחום המסתובב סביב ציר ה-y](images/exams/22A-A-Q6b-sketch.png)
$$V=2\pi\int_0^{C+1}x\sqrt[5]{x^2+B+1}\,dx=\left|\begin{array}{l}t=x^2+B+1\\ dt=2x\,dx\\ x=0\Rightarrow t=B+1\\ x=C+1\Rightarrow t=(C+1)^2+B+1\end{array}\right|=\frac{2\pi}{2}\int_{B+1}^{(C+1)^2+B+1}\sqrt[5]{t}\,dt$$
$$=\pi\,\frac{t^{6/5}}{\frac{6}{5}}\Bigg|_{B+1}^{(C+1)^2+B+1}=\frac{5\pi}{6}\left(\left[(C+1)^2+B+1\right]^{6/5}-\left[B+1\right]^{6/5}\right)$$
"""

questions = [
    Q(1, "computation", "extrema_optimization",
      r"מצאו את הערך הגדול ביותר ואת הערך הקטן ביותר של הפונקציה $f(x)=\frac{4}{5}x-\sqrt[5]{(x-1)^4}+2$ בקטע $[0,3]$.",
      SOL1A, part="א", points=10),
    Q(1, "proof", "sequences_limits",
      r"הוכיחו כי הסדרה $a_{n+1}=\frac{1}{2}\left(a_n+\frac{A+1}{a_n}\right),\ a_1=A+B+2$ מתכנסת וחשבו את גבולה.",
      SOL1B, part="ב", points=10, contextId="c0"),

    Q(2, "computation", "sequences_limits",
      r"חשבו את הגבול $\lim_{n\to\infty}\left(\sqrt{n^2+C+1}-n\right)\sin\left(2^{(B+1)n}\right)$.",
      SOL2A, part="א", points=10, contextId="c0"),
    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int x\arctan\left(x^2\right)dx$.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "continuity",
      r"מצאו את נקודות האי-רציפות של הפונקציה $f(x)=\frac{(A+2)\,x\,|x-B-1|}{\left(2x^2-(2B+3)x+B+1\right)\arctan\left((C+3)x\right)}$ ומיינו אותן.",
      SOL3A, part="א", points=10, contextId="c0"),
    Q(3, "computation", "derivatives_tangents",
      r"נתונה הפונקציה $f(x)=\begin{cases}\frac{x-\sin x}{x^2}, & x<0\\ 0, & x=0\\ \frac{e^{px}-px-1}{x}, & x>0\end{cases}$ "
      r"כאשר $p$ פרמטר ממשי. מצאו את כל הערכים של $p$ כך ש-$f$ תהיה גזירה ב-$x=0$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "derivatives_tangents",
      r"מצאו משיק משותף לשני הגרפים של הפונקציות $y=2(A+1)\ln x+C$ ו-$y=(A+1)\left(x^2-1\right)+C$.",
      SOL4A, part="א", points=10, contextId="c0"),
    Q(4, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{3x^3+x^2+4x+8}{x^4+4x^2}\,dx$.",
      SOL4B, part="ב", points=10),

    Q(5, "proof", "mean_value_theorems",
      r"הוכיחו את האי-שוויון: $\arcsin x\le\frac{x}{\sqrt{1-x^2}}$ עבור כל $x\in[0,1)$.",
      SOL5A, part="א", points=10),
    Q(5, "computation", "definite_integrals",
      r"חשבו את שטח התחום הכלוא בין הקווים: $y=\frac{(A+2)x^2}{2}+B$ ו-$y=\frac{A+2}{1+x^2}+B$.",
      SOL5B, part="ב", points=10, contextId="c0"),

    Q(6, "computation", "lhopital_taylor",
      r"חשבו את הגבול: $\lim_{x\to0}\frac{x-\arcsin x}{\int_0^x\ln\left(1+t^2\right)dt}$.",
      SOL6A, part="א", points=10),
    Q(6, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום המישורי הכלוא בין הקווים: "
      r"$y=\sqrt[5]{x^2+B+1},\ x=0,\ x=C+1,\ y=0$ סביב ציר ה-$y$.",
      SOL6B, part="ב", points=10, contextId="c0"),
]

exam = {
    "examCode": "22A-A",
    "examLabel": "מבחן סוף סמסטר א' תשפ\"ב, מועד א'",
    "year": 2022,
    "examDate": "25/01/2022",
    "sourceFile": "calculus-1/22A-A exam+solution.pdf",
    "solutionFile": "calculus-1/22A-A exam+solution.pdf",
    "contexts": {"c0": {"kind": "text", "title": "הפרמטרים A, B, C", "text": CTX0}},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

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
הערה (השלמה): גם אם מניחים נקודות השקה שונות $x=p$ ו-$x=q$ על שני הגרפים, שוויון השיפועים נותן $p=\frac{1}{q}$ ושוויון המשיקים נותן $q^2-1-2\ln q=0$. לפונקציה $h(q)=q^2-1-2\ln q$ יש מינימום יחיד $h(1)=0$ (כי $h'(q)=2q-\frac{2}{q}$), ולכן $q=1$ ו-$p=1$: המשיק משותף ונוגע בשני הגרפים באותה נקודה.
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


# ---- steps / rubric / pitfalls (ai-draft); every value below is computed or asserted with sympy / mpmath ----
import sympy as sp
import mpmath as mp

IDS = "abcdef"
_rot = [0]
x, t, a, b = sp.symbols('x t a b', real=True)
R = sp.Rational
mp.mp.dps = 60


def T(e):
    """TeX of a sympy expression, wrapped in $...$."""
    return "$" + sp.latex(e) + "$"


def rub(*items):
    return [{"text": s, "points": p} for s, p in items]


def _opts(vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def ch(prompt, good, bads, explain):
    """choice step; the correct option rotates through the positions a, b, c, ..."""
    k = _rot[0] % (len(bads) + 1)
    _rot[0] += 1
    vals = list(bads)
    vals.insert(k, good)
    assert len(set(vals)) == len(vals), "duplicate options"
    return {"type": "choice", "prompt": prompt, "options": _opts(vals), "correctId": IDS[k], "explain": explain}


def chx(prompt, good, bads, ok, explain):
    """choice over expressions: ok(e) must hold for the good one and fail for every distractor."""
    assert ok(good), "good option fails its test"
    for e in bads:
        assert not ok(e), "distractor passes the test: %s" % e
    return ch(prompt, T(good), [T(e) for e in bads], explain)


def num(prompt, val, explain, tol=0.001):
    v = sp.N(val, 15)
    f = float(v)
    ans = int(round(f)) if abs(f - round(f)) < 1e-12 else round(f, 4)
    return {"type": "numeric", "prompt": prompt, "answer": ans, "tol": tol, "explain": explain}


def order(prompt, lines, explain):
    return {"type": "order", "prompt": prompt, "lines": lines, "explain": explain}


def findbug(prompt, lines, idx, explain):
    return {"type": "findbug", "prompt": prompt, "lines": lines, "bugIndex": idx, "explain": explain}


def add(num_, part=None, **kw):
    for q in questions:
        if q["num"] == num_ and q.get("part") == part:
            assert not q.get("hold"), "held item"
            q.update(kw)
            return
    raise KeyError((num_, part))


def same(e1, e2):
    return sp.simplify(e1 - e2) == 0


def dnum(F, g, pts):
    """numeric check that F' = g at each point (F, g sympy expressions in x)"""
    return all(abs(sp.N((sp.diff(F, x) - g).subs(x, p), 30)) < 1e-15 for p in pts)


def rc(v):
    """real odd root helper: real 5th root of v"""
    v = mp.mpf(v)
    return mp.sign(v)*abs(v)**(mp.mpf(1)/5)

# ===== Q1a: f = 4/5 x - (x-1)^(4/5) + 2 on [0,3] =====
def f1(v):
    v = mp.mpf(v)
    return mp.mpf(4)/5*v - abs(v - 1)**(mp.mpf(4)/5) + 2

fp1 = lambda v: mp.mpf(4)/5 - mp.mpf(4)/5/rc(mp.mpf(v) - 1)
assert abs(fp1(33) - mp.mpf(2)/5) < 1e-30 and abs(fp1(2)) < 1e-30
assert abs(f1(0) - 1) < 1e-30 and abs(f1(1) - mp.mpf(14)/5) < 1e-30 and abs(f1(2) - mp.mpf(13)/5) < 1e-30
assert abs(f1(3) - (mp.mpf(22)/5 - mp.mpf(16)**(mp.mpf(1)/5))) < 1e-30 and f1(3) < f1(1)
grid1 = [f1(mp.mpf(k)/1000) for k in range(0, 3001)]
assert abs(max(grid1) - mp.mpf(14)/5) < 1e-9 and abs(min(grid1) - 1) < 1e-9
assert abs(mp.diff(f1, mp.mpf('2.5')) - fp1(mp.mpf('2.5'))) < 1e-20

add(1, "א",
    rubric=rub(("נגזרת $f'(x)=\\frac{4}{5}\\cdot\\frac{\\sqrt[5]{x-1}-1}{\\sqrt[5]{x-1}}$", 3),
               ("נקודות חשודות: $x=2$ (הנגזרת מתאפסת), $x=1$ (הנגזרת אינה קיימת) וקצות הקטע $0,3$", 2),
               ("חישוב $f$ בארבע הנקודות: $1,\\frac{14}{5},\\frac{13}{5},\\approx2.66$", 3),
               ("מקסימום $\\frac{14}{5}$ ב-$x=1$ ומינימום $1$ ב-$x=0$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את $x=1$, שבה הנגזרת אינה קיימת, כנקודה חשודה לקיצון מוחלט.",
              "לשכוח את קצות הקטע $0$ ו-$3$ בהשוואה הסופית.",
              "לחשב $\\sqrt[5]{(x-1)^4}$ בצורה לא נכונה כשהבסיס שלילי."],
    steps=[
        num("מהו הערך של $f'(x)=\\frac{4}{5}-\\frac{4}{5\\sqrt[5]{x-1}}$ בנקודה $x=33$? (עשרוני)", R(2, 5),
            "$\\sqrt[5]{32}=2$ ולכן $f'(33)=\\frac{4}{5}-\\frac{4}{10}=0.4$."),
        num("באיזה ערך $x$ בקטע $[0,3]$ מתאפסת הנגזרת?", 2, "$\\sqrt[5]{x-1}=1$ ולכן $x=2$."),
        num("מהו $f(1)$? (עשרוני)", R(14, 5), "$f(1)=\\frac{4}{5}-0+2=\\frac{14}{5}=2.8$."),
        ch("מהם הערך הגדול ביותר והקטן ביותר של $f$ בקטע $[0,3]$?",
           "הגדול $\\frac{14}{5}$ (ב-$x=1$) והקטן $1$ (ב-$x=0$)",
           ["הגדול $\\frac{22}{5}-\\sqrt[5]{16}$ (ב-$x=3$) והקטן $1$ (ב-$x=0$)", "הגדול $\\frac{14}{5}$ והקטן $\\frac{13}{5}$ (ב-$x=2$)",
            "הגדול $\\frac{14}{5}$ והקטן $0$"],
           "הערכים $f(0)=1$, $f(1)=2.8$, $f(2)=2.6$, $f(3)\\approx2.66$; המקסימום $2.8$ והמינימום $1$ (נבדק על רשת צפופה)."),
    ],
    stepsSource="ai-verified")

# ===== Q1b: a_{n+1} = (a_n + (A+1)/a_n)/2 =====
def it1(av, bv, n=60):
    s_ = mp.mpf(av + bv + 2)
    for _ in range(n):
        s_ = (s_ + mp.mpf(av + 1)/s_)/2
    return s_

for av in range(10):
    assert abs(it1(av, 3) - mp.sqrt(av + 1)) < 1e-25
assert (R(1, 2)*(5 + R(4, 5))) == R(29, 10) and it1(8, 2) == 3
L1b = ["לפי אי-שוויון הממוצעים $a_{n+1}=\\frac{1}{2}\\left(a_n+\\frac{A+1}{a_n}\\right)\\ge\\sqrt{A+1}$, לכן הסדרה חסומה מלמטה.",
       "$a_{n+1}-a_n=\\frac{(A+1)-a_n^2}{2a_n}\\le0$ כי $a_n\\ge\\sqrt{A+1}$, ולכן הסדרה יורדת.",
       "סדרה יורדת וחסומה מלמטה מתכנסת, נסמן את גבולה $L$.",
       "מנוסחת הנסיגה $L^2=A+1$, ומכיוון ש-$a_n\\ge0$ מתקבל $L=\\sqrt{A+1}$."]

add(1, "ב",
    rubric=rub(("חסימה מלמטה $a_n\\ge\\sqrt{A+1}$ בעזרת אי-שוויון הממוצעים", 3),
               ("מונוטוניות: $a_{n+1}-a_n\\le0$", 3),
               ("מסקנת ההתכנסות", 1),
               ("משוואת הגבול $L^2=A+1$ ובחירת השורש החיובי", 3)),
    rubricSource="ai-verified",
    pitfalls=["לטעון שהסדרה מתכנסת רק כי היא נראית יורדת מהאיברים הראשונים.",
              "לשכוח לפסול את $L=-\\sqrt{A+1}$ כי האיברים חיוביים.",
              "להשתמש בגבול בנוסחת הנסיגה לפני שהוכחה התכנסות."],
    steps=[
        num("עבור $A=3$, מהו החסם התחתון $\\sqrt{A+1}$ מאי-שוויון הממוצעים?", 2, "$\\sqrt{3+1}=2$."),
        num("עבור $A=3$ ו-$B=0$ (כלומר $a_1=5$), מהו $a_2$? (עשרוני)", R(29, 10), "$a_2=\\frac{1}{2}\\left(5+\\frac{4}{5}\\right)=2.9$."),
        num("עבור $A=8$, מהו גבול הסדרה?", 3, "$L=\\sqrt{A+1}=\\sqrt{9}=3$ (נבדק באיטרציה נומרית לכל $A=0..9$)."),
        order("סדרו את שלבי ההוכחה.", L1b,
              "החסימה קודמת למונוטוניות (הסימן תלוי בה), שתיהן קודמות להתכנסות, וההתכנסות קודמת למעבר לגבול."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: (sqrt(n^2+C+1)-n) sin(2^((B+1)n)) =====
n_ = mp.mpf(10)**9
for cv in (0, 3, 9):
    assert abs((mp.sqrt(n_**2 + cv + 1) - n_) - (cv + 1)/(mp.sqrt(n_**2 + cv + 1) + n_)) < 1e-30
    assert abs((mp.sqrt(n_**2 + cv + 1) - n_)*mp.sin(mp.mpf(2)**(3*7))) < 1e-8
c3 = 4/(mp.sqrt(13) + 3)

add(2, "א",
    rubric=rub(("כפל בצמוד: $\\sqrt{n^2+C+1}-n=\\frac{C+1}{\\sqrt{n^2+C+1}+n}$", 4),
               ("הוכחה שהגורם הראשון שואף ל-$0$", 2),
               ("חסימות הסינוס $-1\\le\\sin(\\cdot)\\le1$", 2),
               ("מסקנה: שואפת ל-$0$ כפול חסומה, ולכן הגבול $0$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לטעון ש-$\\sin\\left(2^{(B+1)n}\\right)$ שואף לגבול כלשהו. הוא חסום ואינו מתכנס, ואין בכך צורך.",
              "לא להכפיל בצמוד ולהישאר עם $\\infty-\\infty$.",
              "לכתוב $\\infty\\cdot0=0$ בלי הנמקה."],
    steps=[
        num("עבור $C=3$ ו-$n=3$, מהו $\\sqrt{n^2+C+1}-n=\\frac{C+1}{\\sqrt{n^2+C+1}+n}$? (עשרוני)", c3,
            "$\\frac{4}{\\sqrt{13}+3}\\approx0.6056$; שני הביטויים שווים (נבדק מספרית)."),
        num("מהו $\\lim_{n\\to\\infty}\\frac{C+1}{\\sqrt{n^2+C+1}+n}$?", 0, "המכנה שואף ל-$\\infty$ והמונה קבוע."),
        ch("מדוע הגבול של המכפלה הוא $0$?", "מכפלה של סדרה שואפת ל-$0$ בסדרה חסומה",
           ["כי $\\sin\\left(2^{(B+1)n}\\right)$ שואף ל-$0$", "כי $\\sin\\left(2^{(B+1)n}\\right)$ שואף ל-$1$", "אין גבול כי הסינוס מתנדנד"],
           "הסינוס חסום בין $-1$ ל-$1$ והגורם השני שואף ל-$0$, ולכן המכפלה שואפת ל-$0$ (נבדק מספרית עם $n=10^9$)."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: int x arctan(x^2) dx =====
g2b = x*sp.atan(x**2)
F2b = (x**2*sp.atan(x**2) - sp.log(1 + x**4)/2)/2
pts2 = [R(1, 3), 1, 2]
F2b_bads = [(x**2*sp.atan(x**2) + sp.log(1 + x**4)/2)/2, x**2*sp.atan(x**2) - sp.log(1 + x**4)/2,
            (x**2*sp.atan(x**2) - sp.log(1 + x**2)/2)/2]
assert dnum(F2b, g2b, pts2) and not any(dnum(e, g2b, pts2) for e in F2b_bads)
q2b = mp.quad(lambda v: v*mp.atan(v**2), [0, 1])
assert abs(q2b - (mp.pi/4 - mp.log(2)/2)/2) < 1e-25

add(2, "ב",
    rubric=rub(("הצבה $t=x^2$ ו-$x\\,dx=\\frac{dt}{2}$", 2),
               ("אינטגרציה בחלקים של $\\int\\arctan t\\,dt$ עם $u=\\arctan t$, $v=t$", 3),
               ("חישוב $\\int\\frac{t}{1+t^2}dt=\\frac{1}{2}\\ln(1+t^2)$", 3),
               ("הצבה חזרה וקבוע האינטגרציה", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את הגורם $\\frac{1}{2}$ מההצבה $t=x^2$.",
              "לבחור $u=t$ ו-$dv=\\arctan t\\,dt$: האינטגרל של $\\arctan$ אינו ידוע מראש.",
              "לשכוח את החזרה ל-$x$ ולהשאיר $\\ln(1+t^2)$ במקום $\\ln(1+x^4)$."],
    steps=[
        ch("איזו הצבה פותחת את החישוב בפתרון הרשמי?", "$t=x^2$", ["$t=\\arctan x$", "$t=x^4$", "$t=\\arctan\\left(x^2\\right)$"],
           "$dt=2x\\,dx$ ולכן $\\int x\\arctan\\left(x^2\\right)dx=\\frac{1}{2}\\int\\arctan t\\,dt$."),
        num("מהו המקדם $c$ ב-$\\int x\\arctan\\left(x^2\\right)dx=c\\int\\arctan t\\,dt$? (עשרוני)", R(1, 2), "$x\\,dx=\\frac{dt}{2}$."),
        chx("איזו קדומה נכונה?", F2b, F2b_bads, lambda e: dnum(e, g2b, pts2),
            "הנגזרת של $\\frac{1}{2}\\left(x^2\\arctan\\left(x^2\\right)-\\frac{1}{2}\\ln\\left(1+x^4\\right)\\right)$ שווה לאינטגרנד; לשאר האפשרויות לא (נבדק מספרית)."),
        num("מהו הערך של $\\int_0^1x\\arctan\\left(x^2\\right)dx$? (עשרוני)", (mp.pi/4 - mp.log(2)/2)/2,
            "$\\frac{1}{2}\\left(\\frac{\\pi}{4}-\\frac{\\ln2}{2}\\right)\\approx0.2194$ (נבדק באינטגרציה נומרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: discontinuities =====
def f3(av, bv, cv):
    return lambda v: (av + 2)*v*abs(v - bv - 1)/((2*v**2 - (2*bv + 3)*v + bv + 1)*mp.atan((cv + 3)*v))

assert sp.factor(2*x**2 - (2*b + 3)*x + b + 1) == (2*x - 1)*(x - b - 1)
e_ = mp.mpf('1e-9')
for av, bv, cv in ((1, 2, 2), (0, 0, 0), (9, 7, 5)):
    ff = f3(av, bv, cv)
    assert abs(ff(e_) - mp.mpf(av + 2)/(cv + 3)) < 1e-6 and abs(ff(-e_) - mp.mpf(av + 2)/(cv + 3)) < 1e-6   # removable at 0
    h_ = mp.mpf(1)/2
    assert abs(ff(h_ + e_)) > 1e6 and abs(ff(h_ - e_)) > 1e6 and ff(h_ + e_)*ff(h_ - e_) < 0              # infinite at 1/2
    r_, l_ = ff(bv + 1 + e_), ff(bv + 1 - e_)
    assert abs(r_) < 1e3 and abs(l_) < 1e3 and abs(r_ + l_) < 1e-6 and abs(r_) > 1e-3                      # finite, opposite at B+1
assert abs(f3(1, 2, 2)(e_) - mp.mpf(3)/5) < 1e-6

add(3, "א",
    rubric=rub(("פירוק המכנה $2x^2-(2B+3)x+B+1=(2x-1)(x-B-1)$ וזיהוי נקודות החשד $0,\\frac12,B+1$", 2),
               ("$x=0$: הגבול $\\frac{A+2}{C+3}$ קיים, אי-רציפות סליקה", 3),
               ("$x=\\frac12$: הגבול אינסופי, אי-רציפות ממין שני", 2),
               ("$x=B+1$: גבולות חד-צדדיים סופיים ושונים, אי-רציפות ממין ראשון", 3)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את $x=0$ כי הפונקציה נראית מוגדרת שם: המכנה $\\arctan\\left((C+3)x\\right)$ מתאפס בו.",
              "לא לפצל את $|x-B-1|$ לשני צדדים בעת בדיקת $x=B+1$.",
              "לסווג את $x=\\frac12$ כסליקה בלי לבדוק שהמונה אינו מתאפס שם."],
    steps=[
        num("עבור $B=3$, מהו השורש הגדול של $2x^2-(2B+3)x+B+1$?", 4,
            "הפירוק $(2x-1)(x-B-1)$ נותן שורשים $\\frac12$ ו-$B+1=4$ (sympy)."),
        num("עבור $A=1$ ו-$C=2$, מהו $\\lim_{x\\to0}f(x)=\\frac{A+2}{C+3}$? (עשרוני)", R(3, 5),
            "$\\frac{x}{\\arctan((C+3)x)}\\to\\frac{1}{C+3}$ ו-$\\frac{(A+2)|x-B-1|}{(2x-1)(x-B-1)}\\to A+2$ (נבדק מספרית משני הצדדים)."),
        ch("מהו סוג אי-הרציפות ב-$x=\\frac12$?", "מסוג שני (גבול אינסופי)",
           ["סליקה", "מסוג ראשון (גבולות חד-צדדיים סופיים ושונים)", "אין שם אי-רציפות"],
           "המכנה מתאפס והמונה אינו, ולכן $|f|\\to\\infty$ משני הצדדים (נבדק מספרית)."),
        ch("מהו סוג אי-הרציפות ב-$x=B+1$?", "מסוג ראשון (הגבולות החד-צדדיים סופיים ושווים בערכם המוחלט בסימנים הפוכים)",
           ["סליקה", "מסוג שני", "אין שם אי-רציפות"],
           "בגלל $\\frac{|x-B-1|}{x-B-1}=\\pm1$ מתקבלים שני גבולות סופיים שונים (נבדק מספרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: differentiability at 0 =====
hp, hm = mp.mpf('1e-4'), mp.mpf('-1e-4')
for pv in (mp.mpf(1)/mp.sqrt(3), -mp.mpf(1)/mp.sqrt(3)):
    right = (mp.exp(pv*hp) - pv*hp - 1)/hp**2
    left = (hm - mp.sin(hm))/hm**3
    assert abs(right - mp.mpf(1)/6) < 1e-3 and abs(left - mp.mpf(1)/6) < 1e-6
assert abs((mp.exp(2*hp) - 2*hp - 1)/hp**2 - 2) < 1e-3
assert set(sp.solve(sp.Eq(a**2/2, R(1, 6)), a)) == {1/sp.sqrt(3), -1/sp.sqrt(3)}

add(3, "ב",
    rubric=rub(("הצבה בהגדרת הנגזרת $\\lim\\frac{f(h)-f(0)}{h}$ ומעבר לגבולות חד-צדדיים", 2),
               ("הגבול הימני $\\frac{p^2}{2}$ (לופיטל פעמיים)", 3),
               ("הגבול השמאלי $\\frac{1}{6}$ (לופיטל פעמיים)", 3),
               ("השוואה $\\frac{p^2}{2}=\\frac{1}{6}$ ופתרון $p=\\pm\\frac{1}{\\sqrt3}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחשב רק את הנגזרת החד-צדדית מצד אחד.",
              "לשכוח את הפתרון השלילי $p=-\\frac{1}{\\sqrt3}$.",
              "להפעיל לופיטל פעם אחת בלבד כשהמונה והמכנה עדיין מתאפסים."],
    steps=[
        num("מהו הגבול הימני $\\lim_{h\\to0^+}\\frac{e^{ph}-ph-1}{h^2}$ עבור $p=2$?", 2, "התוצאה $\\frac{p^2}{2}=2$ (נבדק מספרית)."),
        num("מהו הגבול השמאלי $\\lim_{h\\to0^-}\\frac{h-\\sin h}{h^3}$? (עשרוני)", R(1, 6), "לופיטל פעמיים נותן $\\frac{1}{6}\\approx0.1667$ (sympy ומספרית)."),
        num("עבור $p>0$, מהו $p$ המקיים $\\frac{p^2}{2}=\\frac{1}{6}$? (עשרוני)", 1/sp.sqrt(3), "$p^2=\\frac{1}{3}$ ולכן $p=\\frac{1}{\\sqrt3}\\approx0.5774$."),
        ch("מהם כל הערכים של $p$?", "$p=\\pm\\frac{1}{\\sqrt3}$",
           ["$p=\\frac{1}{\\sqrt3}$ בלבד", "$p=\\pm\\sqrt3$", "$p=\\pm\\frac13$"],
           "המשוואה $\\frac{p^2}{2}=\\frac16$ מתקיימת בשני הסימנים (שני הערכים נבדקו מספרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: common tangent =====
for av in (0, 2, 7):
    for cv in (0, 4, 9):
        k_ = 2*(av + 1)
        l1 = lambda v: k_*mp.log(v) + cv
        l2 = lambda v: (av + 1)*(v**2 - 1) + cv
        assert abs(l1(1) - cv) < 1e-30 and abs(l2(1) - cv) < 1e-30
        assert abs(mp.diff(l1, 1) - k_) < 1e-20 and abs(mp.diff(l2, 1) - k_) < 1e-20
        assert abs((k_*1 - 2*av + cv - 2) - cv) < 1e-30            # line passes through (1, C)
for xv in (R(1, 2), 2, 3):
    assert 2*(2 + 1)/xv != 2*(2 + 1)*xv                              # slopes differ away from x=1 (A=2)
assert 6*2 - 2 == 10
# common tangent touches both curves at the same point: h(q)=q^2-1-2ln q >= 0 with equality only at q=1
_h = lambda q_: q_**2 - 1 - 2*mp.log(q_)
assert abs(_h(1)) < 1e-30 and all(_h(mp.mpf(i)/100) > 1e-9 for i in list(range(1, 99)) + list(range(101, 1000)))

add(4, "א",
    rubric=rub(("נגזרות $y_1'=\\frac{2(A+1)}{x}$ ו-$y_2'=2(A+1)x$", 2),
               ("השוואת שיפועים $x^2=1$ ובחירת $x=1$ (תחום $\\ln x$)", 2),
               ("בדיקה ששני הגרפים עוברים דרך $(1,C)$", 3),
               ("משוואת המשיק $y=2(A+1)x-2A+C-2$", 3)),
    rubricSource="ai-verified",
    pitfalls=["להשוות את הפונקציות במקום את הנגזרות ולשכוח שיש להשוות גם ערך וגם שיפוע.",
              "לכלול את $x=-1$, שאינה בתחום ההגדרה של $\\ln x$.",
              "טעות אלגברית בשלב $y-C=2(A+1)(x-1)$ לצורה $y=mx+n$."],
    steps=[
        num("עבור $A=2$, מהו השיפוע של $y=2(A+1)\\ln x+C$ בנקודה $x=1$?", 6, "$y'=\\frac{2(A+1)}{x}=6$ ב-$x=1$."),
        ch("באיזה $x$ יש לשני הגרפים אותו שיפוע (בתחום ההגדרה)?", "$x=1$",
           ["$x=-1$", "$x=2$", "$x=0$"],
           "$\\frac{2(A+1)}{x}=2(A+1)x$ נותן $x^2=1$; $x=-1$ מחוץ לתחום של $\\ln x$, ובשאר הערכים השיפועים שונים (נבדק מספרית)."),
        num("עבור $A=2$ ו-$C=4$, מהו ערך המשיק $y=2(A+1)x-2A+C-2$ בנקודה $x=1$?", 4,
            "$6-4+4-2=4=C$, כלומר המשיק עובר דרך נקודת ההשקה $(1,C)$ (נבדק לכמה $A,C$)."),
        num("עבור $A=2$ ו-$C=4$, מהו ערך המשיק בנקודה $x=2$?", 10, "$y=6x-2$ ולכן $y(2)=10$."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: partial fractions =====
Ac, Bc, Cc, Dc = sp.symbols('Ac Bc Cc Dc')
integrand4 = (3*x**3 + x**2 + 4*x + 8)/(x**2*(x**2 + 4))
cs = sp.solve(sp.Poly(sp.expand(Ac*(x**2 + 4) + Bc*x*(x**2 + 4) + (Cc*x + Dc)*x**2 - (3*x**3 + x**2 + 4*x + 8)), x).all_coeffs(),
              [Ac, Bc, Cc, Dc], dict=True)[0]
assert cs == {Ac: 2, Bc: 1, Cc: 2, Dc: -1}
assert same(sp.apart(integrand4, x), 2/x**2 + 1/x + (2*x - 1)/(x**2 + 4))
F4 = -2/x + sp.log(x) + sp.log(x**2 + 4) - sp.atan(x/2)/2
F4_bads = [-2/x + sp.log(x) + sp.log(x**2 + 4) + sp.atan(x/2)/2, 2/x + sp.log(x) + sp.log(x**2 + 4) - sp.atan(x/2)/2,
           -2/x + sp.log(x) + sp.log(x**2 + 4) - sp.atan(x/2)]
pts4 = [R(1, 2), 1, 3]
assert dnum(F4, integrand4, pts4) and not any(dnum(e, integrand4, pts4) for e in F4_bads)

add(4, "ב",
    rubric=rub(("צורת הפירוק $\\frac{A}{x^2}+\\frac{B}{x}+\\frac{Cx+D}{x^2+4}$", 2),
               ("השוואת מקדמים: $A=2$, $B=1$, $C=2$, $D=-1$", 4),
               ("אינטגרציה של $\\frac{2}{x^2}$ ו-$\\frac{1}{x}$ ו-$\\frac{2x}{x^2+4}$", 2),
               ("אינטגרציה של $\\frac{1}{x^2+4}$ ל-$\\frac12\\arctan\\frac{x}{2}$ והתוצאה הסופית", 2)),
    rubricSource="ai-verified",
    pitfalls=["לכתוב רק $\\frac{A}{x^2}$ בלי האיבר $\\frac{B}{x}$ עבור הגורם הכפול $x^2$.",
              "לשכוח את הגורם $\\frac12$ באינטגרל $\\int\\frac{dx}{x^2+4}=\\frac12\\arctan\\frac{x}{2}$.",
              "בלבול בין מקדמי הפירוק $A,B,C,D$ לבין הפרמטרים $A,B,C$ של המבחן."],
    steps=[
        num("מהו מקדם $A$ (של $\\frac{1}{x^2}$) בפירוק? קבוע המקיים $4A=8$.", cs[Ac], "השוואת המקדם החופשי: $4A=8$ ולכן $A=2$ (sympy)."),
        num("מהו מקדם $B$ (של $\\frac{1}{x}$) בפירוק?", cs[Bc], "השוואת מקדם $x$: $4B=4$ ולכן $B=1$ (sympy)."),
        chx("איזו קדומה נכונה? (בתחום $x>0$)", F4, F4_bads, lambda e: dnum(e, integrand4, pts4),
            "הפירוק הוא $\\frac{2}{x^2}+\\frac{1}{x}+\\frac{2x-1}{x^2+4}$; הנגזרת של כל אפשרות נבדקה מספרית מול האינטגרנד."),
        num("מהו המקדם $c$ ב-$\\int\\frac{dx}{x^2+4}=c\\arctan\\frac{x}{2}$? (עשרוני)", R(1, 2),
            "$\\int\\frac{dx}{x^2+a^2}=\\frac{1}{a}\\arctan\\frac{x}{a}$ עם $a=2$."),
    ],
    stepsSource="ai-verified")

# ===== Q5a: arcsin x <= x/sqrt(1-x^2) =====
fin = sp.asin(x) - x/sp.sqrt(1 - x**2)
assert same(sp.diff(fin, x), -x**2/(1 - x**2)**R(3, 2))
fpv = sp.diff(fin, x).subs(x, R(3, 5))
assert fpv == -R(45, 64) or sp.simplify(fpv + R(45, 64)) == 0
assert fin.subs(x, 0) == 0
assert sp.N(fin.subs(x, R(1, 2))) < 0 and all(sp.N(fin.subs(x, R(k, 20))) <= 0 for k in range(0, 20))
L5a2 = ["נגדיר $f(x)=\\arcsin x-\\frac{x}{\\sqrt{1-x^2}}$ ונחשב $f'(x)=-\\frac{x^2}{\\left(1-x^2\\right)^{3/2}}$.",
        "לכל $x\\in[0,1)$ מתקיים $f'(x)\\le0$, ולכן $f$ יורדת.",
        "מכיוון ש-$f(0)=0$ ו-$f$ יורדת, מתקיים $f(x)\\le0$ לכל $x\\in[0,1)$.",
        "כלומר $\\arcsin x\\le\\frac{x}{\\sqrt{1-x^2}}$."]
L5a2_b = list(L5a2)
L5a2_b[2] = "מכיוון ש-$f(0)=0$ ו-$f$ יורדת, מתקיים $f(x)\\ge0$ לכל $x\\in[0,1)$."

add(5, "א",
    rubric=rub(("הגדרת $f(x)=\\arcsin x-\\frac{x}{\\sqrt{1-x^2}}$", 1),
               ("חישוב הנגזרת $f'(x)=-\\frac{x^2}{(1-x^2)^{3/2}}$", 4),
               ("$f'\\le0$ ולכן $f$ יורדת", 2),
               ("$f(0)=0$ ולכן $f(x)\\le0$", 2),
               ("העברת אגפים והמסקנה", 1)),
    rubricSource="ai-verified",
    pitfalls=["טעות בנגזרת של $\\frac{x}{\\sqrt{1-x^2}}$: צריך כלל מנה, והתוצאה $\\frac{1}{(1-x^2)^{3/2}}$.",
              "להסיק $f\\ge0$ מכך ש-$f$ יורדת ו-$f(0)=0$ (הכיוון הפוך).",
              "לבדוק את אי-השוויון רק בנקודות בודדות."],
    steps=[
        num("מהו $f'(x)=-\\frac{x^2}{(1-x^2)^{3/2}}$ בנקודה $x=0.6$? (עשרוני)", -R(45, 64),
            "$-\\frac{0.36}{0.64^{1.5}}=-\\frac{0.36}{0.512}=-0.703125$ (sympy)."),
        num("מהו $f(0.5)=\\arcsin0.5-\\frac{0.5}{\\sqrt{0.75}}$? (עשרוני)", sp.N(fin.subs(x, R(1, 2))),
            "$\\frac{\\pi}{6}-\\frac{1}{\\sqrt3}\\approx-0.0538<0$, בהתאם ל-$f(x)\\le0$."),
        order("סדרו את שלבי ההוכחה.", L5a2, "כל שלב נשען על קודמו: נגזרת, ירידה, השוואה ל-$f(0)$, מסקנה."),
        findbug("בהוכחה הבאה שורה אחת שגויה. מצאו אותה.", L5a2_b, 2,
                "פונקציה יורדת עם $f(0)=0$ נותנת $f(x)\\le0$, לא $\\ge0$ (למשל $f(0.5)\\approx-0.054$, נבדק)."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: area between two even curves =====
def area5(av):
    return 2*(av + 2)*(mp.pi/4 - mp.mpf(1)/6)

for av in (0, 3, 9):
    for bv in (0, 5):
        g1 = lambda v: (av + 2)/(1 + v**2) + bv
        g2 = lambda v: (av + 2)*v**2/2 + bv
        assert abs(g1(1) - g2(1)) < 1e-30 and g1(0.5) > g2(0.5) and g1(-0.7) == g1(0.7) and g2(-0.7) == g2(0.7)
        assert abs(mp.quad(lambda v: g1(v) - g2(v), [-1, 1]) - area5(av)) < 1e-25
assert sp.solve(t**2 + t - 2, t) in ([-2, 1], [1, -2])
assert abs(mp.quad(lambda v: 1/(1 + v**2) - v**2/2, [0, 1]) - (mp.pi/4 - mp.mpf(1)/6)) < 1e-25

add(5, "ב",
    rubric=rub(("השוואת הפונקציות ופתרון $x^4+x^2-2=0$ עם $t=x^2$", 3),
               ("קביעת הקטע $[-1,1]$ וסימטריה, כלומר $S=2\\int_0^1$", 3),
               ("אינטגרל $\\arctan x-\\frac{x^3}{6}$", 2),
               ("תוצאה $2(A+2)\\left(\\frac{\\pi}{4}-\\frac16\\right)$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את השורש $x=-1$ ולחשב רק את הצד החיובי בלי להכפיל ב-$2$.",
              "להשאיר את $t=-2$ כאפשרות. $t=x^2\\ge0$ ולכן נפסל.",
              "לחשב את ההפרש בכיוון ההפוך ולקבל שטח שלילי."],
    steps=[
        num("מהו הפתרון החיובי של $t^2+t-2=0$ (כאשר $t=x^2$)?", 1, "$(t+2)(t-1)=0$ ו-$t\\ge0$, ולכן $t=1$ ו-$x=\\pm1$."),
        ch("מדוע אפשר לחשב $S=2\\int_0^1$?", "שתי הפונקציות זוגיות, ולכן התחום סימטרי ביחס לציר $y$",
           ["שתי הפונקציות אי-זוגיות", "הקטע $[-1,0]$ אינו חלק מהתחום", "כי $A$ ו-$B$ מבטלים זה את זה"],
           "$f(-x)=f(x)$ לשתי הפונקציות (נבדק מספרית), והחיתוך ב-$x=\\pm1$."),
        num("מהו $\\int_0^1\\left(\\frac{1}{1+x^2}-\\frac{x^2}{2}\\right)dx$? (עשרוני)", mp.pi/4 - mp.mpf(1)/6,
            "$\\left(\\arctan x-\\frac{x^3}{6}\\right)\\Big|_0^1=\\frac{\\pi}{4}-\\frac16\\approx0.6187$ (נבדק באינטגרציה נומרית)."),
        num("עבור $A=0$, מהו השטח $2(A+2)\\left(\\frac{\\pi}{4}-\\frac16\\right)$? (עשרוני)", area5(0),
            "$4\\cdot0.61873\\approx2.4749$ (נבדק באינטגרציה נומרית על $[-1,1]$)."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: lim (x - arcsin x)/int_0^x ln(1+t^2) =====
def lim6(v):
    v = mp.mpf(v)
    return (v - mp.asin(v))/mp.quad(lambda s: mp.log(1 + s**2), [0, v])

assert abs(lim6('1e-3') + mp.mpf(1)/2) < 1e-3
assert sp.limit((x - sp.asin(x))/sp.integrate(sp.log(1 + t**2), (t, 0, x)), x, 0) == -R(1, 2)
assert abs((1 - 1/mp.sqrt(1 - mp.mpf('0.36'))) + mp.mpf(1)/4) < 1e-30
assert sp.limit(x**2/sp.log(1 + x**2), x, 0) == 1

add(6, "א",
    rubric=rub(("זיהוי $\\frac00$ והפעלת לופיטל", 2),
               ("גזירת המכנה לפי המשפט היסודי: $\\ln(1+x^2)$, וגזירת המונה $1-\\frac{1}{\\sqrt{1-x^2}}$", 3),
               ("כפל בצמוד והגעה ל-$-\\frac{x^2}{\\ln(1+x^2)}\\cdot\\frac{1}{\\sqrt{1-x^2}\\left(\\sqrt{1-x^2}+1\\right)}$", 3),
               ("ערך הגבול $-\\frac12$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לגזור את האינטגרל במכנה כאילו הגבול התחתון תלוי ב-$x$.",
              "לא להשתמש בגבול המפורסם $\\lim\\frac{x^2}{\\ln(1+x^2)}=1$.",
              "טעות סימן ב-$\\sqrt{1-x^2}-1$ ולהגיע ל-$+\\frac12$."],
    steps=[
        ch("מהי הנגזרת של המכנה $\\int_0^x\\ln\\left(1+t^2\\right)dt$?", "$\\ln\\left(1+x^2\\right)$",
           ["$\\frac{2x}{1+x^2}$", "$x\\ln\\left(1+x^2\\right)$", "$\\ln\\left(1+x^2\\right)-\\ln1$ כפול $x$"],
           "לפי המשפט היסודי של החשבון האינטגרלי, $\\frac{d}{dx}\\int_0^xg(t)\\,dt=g(x)$."),
        num("מהו ערך הנגזרת של המונה $x-\\arcsin x$ בנקודה $x=0.6$? (עשרוני)", -R(1, 4),
            "$1-\\frac{1}{\\sqrt{1-0.36}}=1-1.25=-0.25$."),
        num("מהו $\\lim_{x\\to0}\\frac{x^2}{\\ln\\left(1+x^2\\right)}$?", 1, "גבול מפורסם $\\frac{u}{\\ln(1+u)}\\to1$ עם $u=x^2$ (sympy)."),
        num("מהו ערך הגבול? (עשרוני)", -R(1, 2), "$-1\\cdot\\frac{1}{1\\cdot(1+1)}=-\\frac12$ (נבדק נומרית ב-$x=10^{-3}$ ובעזרת sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: shells volume of y = (x^2+B+1)^(1/5) =====
def vol6b(bv, cv):
    return 2*mp.pi*mp.quad(lambda v: v*(v**2 + bv + 1)**(mp.mpf(1)/5), [0, cv + 1])

def vol6b_closed(bv, cv):
    return 5*mp.pi/6*(((cv + 1)**2 + bv + 1)**(mp.mpf(6)/5) - (bv + 1)**(mp.mpf(6)/5))

for bv in (0, 1, 8):
    for cv in (0, 2, 9):
        assert abs(vol6b(bv, cv) - vol6b_closed(bv, cv)) < 1e-20, (bv, cv)

add(6, "ב",
    rubric=rub(("שיטת הקליפות: $V=2\\pi\\int_0^{C+1}x\\sqrt[5]{x^2+B+1}\\,dx$", 3),
               ("הצבה $t=x^2+B+1$ ושינוי הגבולות ל-$B+1$ ו-$(C+1)^2+B+1$", 3),
               ("אינטגרל $\\int\\sqrt[5]{t}\\,dt=\\frac{5}{6}t^{6/5}$", 2),
               ("הצבת הגבולות והתוצאה הסופית", 2)),
    rubricSource="ai-verified",
    pitfalls=["להשתמש בטבעות סביב ציר $y$: דורש להפוך את הפונקציה.",
              "לשכוח לשנות את גבולות האינטגרציה בהצבה.",
              "לשכוח את הגורם $\\frac12$ מ-$dt=2x\\,dx$ (הוא מצטמצם עם $2\\pi$ ל-$\\pi$)."],
    steps=[
        ch("באיזו שיטה משתמש הפתרון הרשמי לחישוב הנפח?", "שיטת הקליפות הגליליות",
           ["שיטת הטבעות (חתכים) סביב ציר $y$", "משפט פפוס בלבד, בלי אינטגרל"],
           "הסיבוב סביב ציר $y$ של תחום מתחת לגרף של $y(x)$ נותן קליפות: $V=2\\pi\\int x\\,y\\,dx$."),
        num("עבור $B=1$ ו-$C=2$, מהו הגבול העליון החדש $t=(C+1)^2+B+1$ אחרי ההצבה?", 11, "$x=C+1=3$ נותן $t=9+2=11$."),
        num("עבור $B=1$ ו-$C=2$, מהו הנפח? (עשרוני)", vol6b_closed(1, 2),
            "$\\frac{5\\pi}{6}\\left(11^{6/5}-2^{6/5}\\right)\\approx40.51$ (נבדק באינטגרציה נומרית של הקליפות, לכל $B,C$ שנבדקו)."),
    ],
    stepsSource="ai-verified")


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

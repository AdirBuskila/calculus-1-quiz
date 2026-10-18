# -*- coding: utf-8 -*-
"""Generator for tools/raw/23A-B.json -- calculus-1 (20151), semester B 2023, moed A (19/06/2023).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_23A-B.py

Source: sitting 23A-B, pp.1-7 (typed exam with the official worked solution; Q4a and Q4b solutions are handwritten
pages inside the same official PDF, transcribed to text; no handwriting crops are shipped).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each). Weight of every question 20%.

Transcription notes
- Official solution transcribed in full, as printed. Rubric, pitfalls and steps are ai-draft (block below the questions).
- Q1: the official graph (p.2) is shipped as a figure (a red pen annotation next to it was whited out; the pen
  arrow and circle marking the open point (0,1) remain).
- Q4b: the handwritten region sketch is described in words in the question, not shipped.
- Q6b: the bound is printed 1/(3000*0.9^3) = 0.00045; the exact value is 0.000457247, so 0.00045 is a truncation and
  not a valid upper bound (the actual error is 0.00036). Final-answer error -> "הפתרון הרשמי עם תיקון" label, minimal
  fix delta < 0.000457, solutionSource solved, official False. ln 0.9 ~ -0.105 is correct.
- Q2b: the official text says "המכנה שלילי" where the numerator 7-a_n^2 is meant; corrected silently, logged in ASK_ADIR.
- Q1: the official uses "קעורה" for f''>0; the symbols (cup/cap) were added beside the words, wording otherwise unchanged.

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
**ד.** $f''(x)=\frac{-(\ln x+2)}{x^2(\ln x)^3}$ ולכן פונקציה קעורה ($\cup$) כאשר $e^{-2}<x<1$ וקמורה ($\cap$) כאשר $x>1$ או $x<e^{-2}$. בנקודה $x=e^{-2}$ הפונקציה בעלת נקודת פיתול.
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
המונה שלילי כי $a_n\ge\sqrt{7}$ ו-$a_n>0$. המכנה חיובי.
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
**הפתרון הרשמי עם תיקון:** בפתרון הרשמי החסם $\frac{1}{3000\cdot0.9^3}$ נכתב $0.00045$, אך ערכו $0.000457247\ldots$ ולכן $0.00045$ אינו חסם עליון תקף (הוא נקצץ ולא עוגל כלפי מעלה). התשובה הסופית מתוקנת ל-$\delta<0.000457$. התיקון נבדק (sympy).
$$\ln(1+x)=x-\frac{x^2}{2}+R_2(x),\qquad R_2(x)=\frac{\left(\ln(1+x)\right)^{(3)}(c)}{3!}x^3=\frac{1}{3(1+c)^3}x^3,$$
$c$ בין $x$ ל-$0$.
$$\ln0.9=\ln(1+(-0.1))=-0.1-\frac{(-0.1)^2}{2}+R_2(x)\approx-0.105,$$
$$R_2(x)=\frac{1}{3(1+c)^3}(-0.1)^3,\qquad-0.1<c<0$$
$$|R_2(x)|=\left|\frac{1}{3(1+c)^3}(-0.1)^3\right|<\frac{1}{3000\cdot0.9^3}\approx0.000457=\delta$$
תשובה: $\ln0.9\approx-0.105,\qquad\delta<0.000457$
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
      SOL6B, part="ב", points=10, solutionSource="solved", official=False),
]

# ---- steps / rubric / pitfalls (ai-draft); every value below is computed or asserted with sympy ----
import sympy as sp

IDS = "abcdef"
_rot = [0]
x, t, a, b = sp.symbols('x t a b', real=True)
R = sp.Rational
PTS = (0.35, 0.8, 1.3, 1.9, 2.6, 3.4)


def T(e):
    """TeX of a sympy expression, wrapped in $...$."""
    return "$" + sp.latex(e, ln_notation=True) + "$"


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


def same(e1, e2, pts=PTS, var=None):
    """True iff the two expressions agree (numerically, >= 3 valid sample points) and are never seen to differ."""
    v = var if var is not None else x
    ok_pts = 0
    for p in pts:
        try:
            d = complex(sp.N(e1.subs(v, p) - e2.subs(v, p), 30))
        except Exception:
            continue
        if d != d:
            continue
        if abs(d) > 1e-9:
            return False
        ok_pts += 1
    return ok_pts >= 3


def chx(prompt, good, bads, ok, explain):
    """choice over sympy expressions: ok(e) must hold for the good one and fail for every distractor."""
    assert ok(good), "good option fails its test"
    for e in bads:
        assert not ok(e), "distractor passes the test: %s" % e
    return ch(prompt, T(good), [T(e) for e in bads], explain)


def num(prompt, val, explain, tol=0.001, nd=4):
    f = float(sp.N(val, 30))
    ans = int(round(f)) if abs(f - round(f)) < 1e-12 else round(f, nd)
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


def lim_iter(f, a1, n=40):
    """first n terms of a recursive sequence, exact rationals/floats via sympy Float(50)."""
    seq = [sp.N(a1, 50)]
    for _ in range(n - 1):
        seq.append(sp.N(f(seq[-1]), 50))
    return seq


import mpmath as _mp
an = sp.Symbol('a_n', real=True)

# ===== Q1: f = (ln x - 1)/ln x =====
f1 = (sp.log(x) - 1)/sp.log(x)
f1p = sp.diff(f1, x)
f1pp = sp.diff(f1, x, 2)
P1 = (0.3, 0.6, 1.5, 2.5, 4.0)
assert same(f1p, 1/(x*sp.log(x)**2), pts=P1) and same(f1pp, -(sp.log(x) + 2)/(x**2*sp.log(x)**3), pts=P1)
assert sp.solve(sp.Eq(sp.log(x), 1), x) == [sp.E]
assert sp.solve(sp.Eq(sp.log(x) + 2, 0), x) == [sp.exp(-2)]
assert sp.limit(f1, x, 1, '-') == sp.oo and sp.limit(f1, x, 1, '+') == -sp.oo and sp.limit(f1, x, sp.oo) == 1

add(1,
    rubric=rub(("תחום הגדרה $x>0,\\ x\\neq1$ ונקודת החיתוך היחידה עם הצירים $(e,0)$", 4),
               ("נגזרת $f'(x)=\\frac{1}{x\\ln^2x}>0$: עולה ממש בכל התחום, ללא קיצון", 4),
               ("נגזרת שנייה $f''(x)=\\frac{-(\\ln x+2)}{x^2\\ln^3x}$, תחומי קמירות וקעירות ונקודת פיתול ב-$x=e^{-2}$", 6),
               ("אסימפטוטה אנכית $x=1$ (גבולות $+\\infty$ ו-$-\\infty$) ואופקית $y=1$, והגבול $f\\to1$ ב-$0^+$", 4),
               ("שרטוט הגרף בהתאם לכל הנתונים", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח ש-$x=1$ מחוץ לתחום ההגדרה ($\\ln1=0$ במכנה) ולכן יש שם אסימפטוטה אנכית.",
              "לטעון לקיצון כי $f'$ לא מוגדרת ב-$x=1$: $x=1$ אינה בתחום, ו-$f'>0$ בכל התחום.",
              "לשכוח שבאינסוף האסימפטוטה האופקית היא $y=1$ ($\\frac{\\ln x-1}{\\ln x}=1-\\frac{1}{\\ln x}$)."],
    steps=[
        num("באיזה $x$ חותכת הפונקציה את ציר ה-$X$? (עשרוני)", sp.E, "$f(x)=0\\iff\\ln x=1\\iff x=e\\approx2.7183$."),
        chx("מהי הנגזרת של $f(x)=1-\\frac{1}{\\ln x}$?", 1/(x*sp.log(x)**2),
            [1/(x*sp.log(x)), 1/sp.log(x)**2, -1/(x*sp.log(x)**2)],
            lambda e: same(e, f1p, pts=P1),
            "$\\left(\\frac{1}{\\ln x}\\right)'=-\\frac{1}{x\\ln^2x}$, ולכן $f'=\\frac{1}{x\\ln^2x}$, חיובית בכל התחום (נבדק ב-sympy)."),
        num("באיזה $x$ מתאפסת $f''(x)=\\frac{-(\\ln x+2)}{x^2\\ln^3x}$ ומשנה סימן? (עשרוני)", sp.exp(-2),
            "$\\ln x+2=0$ נותן $x=e^{-2}\\approx0.1353$."),
        ch("מהם הגבולות החד-צדדיים של $f$ ב-$x=1$?",
           "$\\lim_{x\\to1^-}f=+\\infty$ ו-$\\lim_{x\\to1^+}f=-\\infty$",
           ["$\\lim_{x\\to1^-}f=-\\infty$ ו-$\\lim_{x\\to1^+}f=+\\infty$", "שני הגבולות $+\\infty$", "שני הגבולות $-\\infty$"],
           "$f=1-\\frac{1}{\\ln x}$: משמאל $\\ln x\\to0^-$ ולכן $-\\frac{1}{\\ln x}\\to+\\infty$, ומימין $\\ln x\\to0^+$ ולכן $f\\to-\\infty$ (אומת ב-sympy)."),
        num("מהו $\\lim_{x\\to+\\infty}f(x)$ (האסימפטוטה האופקית $y=?$)", 1, "$f=1-\\frac{1}{\\ln x}\\to1$."),
    ],
    stepsSource="ai-verified")

# ===== Q2a: (2x^2 + x + 4)/((x+1)(x^2+4)) =====
g2a = (2*x**2 + x + 4)/((x + 1)*(x**2 + 4))
A_, B_, C_ = sp.symbols('A B C')
s2a = sp.solve(sp.Poly(sp.expand(A_*(x**2 + 4) + (B_*x + C_)*(x + 1) - (2*x**2 + x + 4)), x).all_coeffs(), [A_, B_, C_], dict=True)[0]
assert s2a == {A_: 1, B_: 1, C_: 0}
F2a = sp.log(x + 1) + sp.log(x**2 + 4)/2
assert same(sp.diff(F2a, x), g2a)
assert sp.solve(sp.Poly(sp.expand(A_*(x**2 + 4) + B_*(x + 1) - (2*x**2 + x + 4)), x).all_coeffs(), [A_, B_], dict=True) == []
assert sp.solve(sp.Poly(sp.expand((A_*x + B_)*(x**2 + 4) + C_*(x + 1) - (2*x**2 + x + 4)), x).all_coeffs(), [A_, B_, C_], dict=True) == []

add(2, "א",
    rubric=rub(("פירוק לשברים חלקיים בצורה $\\frac{A}{x+1}+\\frac{Bx+C}{x^2+4}$", 2),
               ("חישוב המקדמים $A=1$, $B=1$, $C=0$", 4),
               ("אינטגרל $\\int\\frac{dx}{x+1}=\\ln|x+1|$", 1),
               ("אינטגרל $\\int\\frac{x\\,dx}{x^2+4}=\\frac{1}{2}\\ln\\left(x^2+4\\right)$", 2),
               ("תשובה סופית עם $+C$", 1)),
    rubricSource="ai-verified",
    pitfalls=["לכתוב $\\frac{B}{x^2+4}$ במקום מונה לינארי $Bx+C$: אז אין פתרון למערכת המקדמים.",
              "לשכוח את הגורם $\\frac{1}{2}$ באינטגרל $\\int\\frac{x}{x^2+4}dx$.",
              "טעות בהצבת $x=-1$: $A\\left((-1)^2+4\\right)=5A=5$."],
    steps=[
        ch("איזה פירוק לשברים חלקיים מתאים ל-$\\frac{2x^2+x+4}{(x+1)(x^2+4)}$?", "$\\frac{A}{x+1}+\\frac{Bx+C}{x^2+4}$",
           ["$\\frac{A}{x+1}+\\frac{B}{x^2+4}$", "$\\frac{Ax+B}{x+1}+\\frac{C}{x^2+4}$"],
           "$x^2+4$ אי-פריק ולכן מעליו מונה לינארי. בשתי האפשרויות האחרות מערכת המקדמים חסרת פתרון (אומת ב-sympy)."),
        num("מהו המקדם $A$?", s2a[A_], "הצבת $x=-1$ ב-$A(x^2+4)+(Bx+C)(x+1)=2x^2+x+4$ נותנת $5A=5$, כלומר $A=1$."),
        num("מהו המקדם $B$?", s2a[B_], "משווים מקדמי $x^2$: $A+B=2$, ולכן $B=1$ (ו-$C=0$)."),
        chx("מהי התוצאה (בלי הקבוע, בתחום $x>-1$)?", F2a,
            [sp.log(x + 1) + sp.log(x**2 + 4), sp.log(x + 1) + sp.atan(x/2)/2, sp.log(x + 1)/2 + sp.log(x**2 + 4)],
            lambda e: same(sp.diff(e, x), g2a),
            "$\\int\\frac{x}{x^2+4}dx=\\frac{1}{2}\\ln\\left(x^2+4\\right)$; הנגזרת של כל אפשרות נבדקה ב-sympy."),
    ],
    stepsSource="ai-verified")

# ===== Q2b: a_1 = 3, a_{n+1} = (a_n + 7/a_n)/2 =====
seq2 = lim_iter(lambda v: (v + 7/v)/2, 3, n=6)
s7 = sp.sqrt(7)
assert all(v >= sp.N(s7, 50) - 1e-40 for v in seq2) and all(seq2[i + 1] < seq2[i] for i in range(len(seq2) - 1))
assert abs(seq2[1] - R(8, 3)) < 1e-40
assert seq2[1] < 3 and any(v < 3 for v in seq2) and any(v < 2.7 for v in seq2) and any(v < sp.N(R(7, 2)) for v in seq2)
assert sp.simplify(((an + 7/an)/2 - an) - (7 - an**2)/(2*an)) == 0

L2b = [r"לפי אי-שוויון הממוצעים $a_{n+1}=\frac12\left(a_n+\frac{7}{a_n}\right)\ge\sqrt{a_n\cdot\frac{7}{a_n}}=\sqrt7$; לכן $a_n\ge\sqrt7$ לכל $n$.",
       r"$a_{n+1}-a_n=\frac{7-a_n^2}{2a_n}\le0$ כי $a_n\ge\sqrt7$ ו-$a_n>0$; לכן הסדרה יורדת.",
       r"הסדרה יורדת וחסומה מלמטה, ולכן מתכנסת לגבול $L$.",
       r"מנוסחת הנסיגה $L=\frac12\left(L+\frac7L\right)$, כלומר $L^2=7$, ומכיוון שהאיברים חיוביים $L=\sqrt7$."]

add(2, "ב",
    rubric=rub(("חסם תחתון $a_n\\ge\\sqrt{7}$ מאי-שוויון הממוצעים", 3),
               ("מונוטוניות: $a_{n+1}-a_n=\\frac{7-a_n^2}{2a_n}\\le0$ והסקה שהסדרה יורדת", 3),
               ("סדרה יורדת וחסומה מלמטה מתכנסת", 1),
               ("מעבר לגבול בנוסחת הנסיגה וקבלת $L^2=7$", 2),
               ("פסילת $L=-\\sqrt{7}$ ומסקנה $L=\\sqrt{7}$", 1)),
    rubricSource="ai-verified",
    pitfalls=["להסיק מהאיברים הראשונים ($3,\\frac{8}{3},\\frac{127}{48}$) שהסדרה יורדת, בלי הוכחה.",
              "לשכוח לפסול את $L=-\\sqrt{7}$ אף שכל האיברים חיוביים.",
              "להוכיח מונוטוניות בלי החסם $a_n\\ge\\sqrt{7}$, שהוא מה שקובע את סימן $7-a_n^2$."],
    steps=[
        num("מהו $a_2=\\frac{1}{2}\\left(3+\\frac{7}{3}\\right)$? (עשרוני)", R(8, 3), "$a_2=\\frac{8}{3}\\approx2.6667<3=a_1$."),
        ch("איזה חסם תחתון מתקבל מאי-שוויון הממוצעים ומתקיים לכל איברי הסדרה?", "$a_n\\ge\\sqrt{7}$",
           ["$a_n\\ge3$", "$a_n\\ge2.7$", "$a_n\\ge\\frac{7}{2}$"],
           "$a_2=\\frac{8}{3}<3$, ו-$a_3=\\frac{127}{48}\\approx2.646<2.7$ ו-$a_1=3<3.5$; רק $\\sqrt{7}\\approx2.6458$ נשמר לכל $n$ (נבדק ב-6 האיברים הראשונים)."),
        chx("מהו $a_{n+1}-a_n$ כביטוי ב-$a_n$?", (7 - an**2)/(2*an),
            [(an**2 - 7)/(2*an), (7 - an**2)/an, (7 + an**2)/(2*an)],
            lambda e: sp.simplify(e - ((an + 7/an)/2 - an)) == 0,
            "$\\frac{1}{2}\\left(a_n+\\frac{7}{a_n}\\right)-a_n=\\frac{7-a_n^2}{2a_n}$ (נבדק ב-sympy)."),
        order("סדרו את שלבי ההוכחה.", L2b,
              "קודם החסם התחתון (הוא קובע את סימן המונוטוניות), אחר כך המונוטוניות, ההתכנסות, וחישוב הגבול."),
    ],
    stepsSource="ai-verified")

# ===== Q3a: lim (int_0^{x^4} (1+t)^{2/t} dt)/x^4 =====
gt = (1 + t)**(2/t)
assert sp.limit(gt, t, 0, '+') == sp.exp(2)
_mp.mp.dps = 25
_G = lambda s: _mp.quad(lambda u: (1 + u)**(2/u), [0, s**4])
_pt = _mp.mpf('0.7')
_ftc = (1 + _pt**4)**(2/_pt**4)*4*_pt**3
assert abs(_mp.diff(_G, _pt) - _ftc) < 1e-8
good3a = (1 + x**4)**(2/x**4)*4*x**3
P3a = (0.5, 0.7, 0.9, 1.2, 1.6)
assert same(good3a, gt.subs(t, x**4)*4*x**3, pts=P3a)

add(3, "א",
    rubric=rub(("זיהוי הצורה $\\frac{0}{0}$ והפעלת לופיטל", 2),
               ("גזירת האינטגרל במונה לפי המשפט היסודי וכלל השרשרת: $(1+x^4)^{\\frac{2}{x^4}}\\cdot4x^3$", 4),
               ("גזירת המכנה $4x^3$ וצמצום", 1),
               ("חישוב $\\lim_{x\\to0}(1+x^4)^{\\frac{2}{x^4}}=e^2$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את כלל השרשרת: הגבול העליון הוא $x^4$ ולכן יש להכפיל ב-$4x^3$.",
              "להציב $t=x$ במקום $t=x^4$ באינטגרנד אחרי הגזירה.",
              "לא לזהות את הגבול $(1+u)^{\\frac{1}{u}}\\to e$ עם $u=x^4$ והמעריך $\\frac{2}{u}$, ולהסיק $e$ במקום $e^2$."],
    steps=[
        ch("מהי הצורה הלא מוגדרת של הגבול ב-$x\\to0$?", "$\\frac{0}{0}$",
           ["$\\frac{\\infty}{\\infty}$", "$1^\\infty$", "$0\\cdot\\infty$"],
           "המונה $\\int_0^0\\ldots=0$ והמכנה $x^4\\to0$."),
        chx("מהי הנגזרת של המונה $\\int_0^{x^4}(1+t)^{\\frac{2}{t}}dt$ לפי $x$?", good3a,
            [(1 + x**4)**(2/x**4), (1 + x)**(2/x)*4*x**3, (1 + x**4)**(2/x**4)*x**4],
            lambda e: same(e, gt.subs(t, x**4)*4*x**3, pts=P3a),
            "משפט יסודי עם כלל השרשרת: מציבים $t=x^4$ באינטגרנד ומכפילים ב-$\\left(x^4\\right)'=4x^3$ (נבדק מספרית)."),
        num("מהו $\\lim_{t\\to0^+}(1+t)^{\\frac{2}{t}}$, הגבול של המנה אחרי הצמצום של $4x^3$? (עשרוני)", sp.exp(2),
            "$(1+t)^{\\frac{2}{t}}=\\left((1+t)^{\\frac{1}{t}}\\right)^2\\to e^2\\approx7.3891$ (אומת ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q3b: int dx/(x(ln^2 x + 2 ln x + 5)) =====
g3b = 1/(x*(sp.log(x)**2 + 2*sp.log(x) + 5))
F3b = sp.atan((sp.log(x) + 1)/2)/2
assert same(sp.diff(F3b, x), g3b)
P3b = (0.4, 0.9, 1.7, 2.6, 4.2)
tt = sp.Symbol('t', real=True)

add(3, "ב",
    rubric=rub(("הצבה $t=\\ln x$, $dt=\\frac{dx}{x}$", 3),
               ("האינטגרל $\\int\\frac{dt}{t^2+2t+5}$ והשלמה לריבוע $(t+1)^2+4$", 2),
               ("אינטגרל $\\frac{1}{2}\\arctan\\frac{t+1}{2}$", 3),
               ("הצבה חוזרת $t=\\ln x$", 1),
               ("קבוע האינטגרציה $+C$", 1)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח שה-$\\frac{dx}{x}$ באינטגרנד הוא בדיוק $dt$, ולנסות לפתור את האינטגרל ב-$x$.",
              "לאנטגרל $\\frac{1}{(t+1)^2+4}$ כ-$\\arctan(t+1)$ בלי הגורם $\\frac{1}{2}$ והחלוקה ב-$2$ בתוך הארקטנגנס.",
              "להשאיר את התשובה במשתנה $t$ במקום לחזור ל-$x$."],
    steps=[
        ch("איזו הצבה משמש הפתרון הרשמי?", "$t=\\ln x$",
           ["$t=x$", "$t=\\ln^2x+2\\ln x+5$", "$t=\\sqrt{x}$"],
           "$\\frac{dx}{x}=dt$, והמכנה הוא פולינום ריבועי ב-$\\ln x$."),
        chx("מהו האינטגרנד $e(t)$ אחרי ההצבה $t=\\ln x$ (כך ש-$e(\\ln x)\\cdot\\frac{1}{x}$ הוא האינטגרנד המקורי)?",
            1/(tt**2 + 2*tt + 5),
            [tt/(tt**2 + 2*tt + 5), 1/(tt**2 + 2*tt + 4), 1/(tt*(tt**2 + 2*tt + 5))],
            lambda e: same(e.subs(tt, sp.log(x))/x, g3b, pts=P3b),
            "$t^2+2t+5=\\ln^2x+2\\ln x+5$ ו-$dt=\\frac{dx}{x}$ (נבדק ב-sympy)."),
        chx("מהי הצורה של $t^2+2t+5$ אחרי השלמה לריבוע?", (tt + 1)**2 + 4,
            [(tt + 1)**2 + 5, (tt + 1)**2 + 3, (tt - 1)**2 + 4],
            lambda e: sp.expand(e - (tt**2 + 2*tt + 5)) == 0,
            "$(t+1)^2=t^2+2t+1$, ולכן צריך להוסיף $4$ (נבדק ב-sympy)."),
        chx("מהי התוצאה (בלי הקבוע)?", F3b,
            [sp.atan((sp.log(x) + 1)/2), sp.atan(sp.log(x) + 1)/2, -sp.atan((sp.log(x) + 1)/2)/2],
            lambda e: same(sp.diff(e, x), g3b, pts=P3b),
            "$\\int\\frac{dt}{(t+1)^2+4}=\\frac{1}{2}\\arctan\\frac{t+1}{2}$ ואז $t=\\ln x$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q4a: (x+2) sqrt(4-x^2) <= 3 sqrt(3) on [-2,2] =====
f4 = (x + 2)*sp.sqrt(4 - x**2)
P4 = (-1.5, -0.5, 0.5, 1.0, 1.5)
f4p = -2*(x**2 + x - 2)/sp.sqrt(4 - x**2)
assert same(sp.diff(f4, x), f4p, pts=P4)
assert sorted(sp.solve(sp.Eq(x**2 + x - 2, 0), x)) == [-2, 1]
assert sp.simplify(f4.subs(x, 1) - 3*sp.sqrt(3)) == 0 and f4.subs(x, 2) == 0 and f4.subs(x, -2) == 0
import numpy as _np
_g = _np.linspace(-2, 2, 400001)
assert (( _g + 2)*_np.sqrt(4 - _g**2)).max() <= 3*3**0.5 + 1e-9

L4a = [r"$f'(x)=-2\frac{x^2+x-2}{\sqrt{4-x^2}}=-2\frac{(x-1)(x+2)}{\sqrt{4-x^2}}$ ב-$(-2,2)$, ולכן הנקודה הקריטית הפנימית היחידה היא $x=1$.",
       r"$f(1)=3\sqrt3>0=f(\pm2)$ ו-$f$ רציפה ב-$[-2,2]$, ולכן $x=1$ היא נקודת מקסימום מוחלט.",
       r"לכן $f(x)\le f(1)=3\sqrt3$ לכל $x\in[-2,2]$, כלומר $(x+2)\sqrt{4-x^2}\le3\sqrt3$."]

add(4, "א",
    rubric=rub(("הגדרת $f(x)=(x+2)\\sqrt{4-x^2}$, רציפות ב-$[-2,2]$ וערכי הקצה $f(\\pm2)=0$", 2),
               ("נגזרת $f'(x)=-2\\frac{x^2+x-2}{\\sqrt{4-x^2}}$", 3),
               ("נקודה קריטית פנימית $x=1$ ($x=-2$ היא קצה)", 2),
               ("חישוב $f(1)=3\\sqrt{3}$ והשוואה לקצוות: מקסימום מוחלט", 2),
               ("מסקנה: $f(x)\\le3\\sqrt{3}$ לכל $x\\in[-2,2]$", 1)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח לבדוק את ערכי הקצה: מקסימום מוחלט נקבע מהשוואה בין הנקודות הקריטיות לקצוות.",
              "לטעות בגזירת השורש: $\\left(\\sqrt{4-x^2}\\right)'=\\frac{-x}{\\sqrt{4-x^2}}$.",
              "להתייחס ל-$x=-2$ כנקודה קריטית פנימית, אף שהיא בקצה ו-$f'$ לא מוגדרת בה."],
    steps=[
        chx("מהי הנגזרת של $f(x)=(x+2)\\sqrt{4-x^2}$ ב-$(-2,2)$?", f4p,
            [-2*(x**2 + x + 2)/sp.sqrt(4 - x**2), 2*(x**2 + x - 2)/sp.sqrt(4 - x**2), -(x**2 + 2*x - 4)/sp.sqrt(4 - x**2)],
            lambda e: same(e, sp.diff(f4, x), pts=P4),
            "$f'=\\sqrt{4-x^2}-\\frac{x(x+2)}{\\sqrt{4-x^2}}=\\frac{4-x^2-x^2-2x}{\\sqrt{4-x^2}}=-2\\frac{x^2+x-2}{\\sqrt{4-x^2}}$ (נבדק ב-sympy)."),
        num("מהי הנקודה הקריטית של $f$ בתוך הקטע $(-2,2)$?", 1,
            "$x^2+x-2=(x-1)(x+2)=0$ נותן $x=1$ או $x=-2$; רק $x=1$ פנימית."),
        num("מהו $f(1)=3\\sqrt{3}$? (עשרוני)", 3*sp.sqrt(3), "$f(1)=3\\sqrt{3}\\approx5.1962$, לעומת $f(\\pm2)=0$ (נבדק גם על רשת צפופה)."),
        order("סדרו את שלבי ההוכחה.", L4a,
              "קודם הנגזרת והנקודה הקריטית, אחר כך השוואת הערכים וקביעת המקסימום המוחלט, ולבסוף האי-שוויון."),
    ],
    stepsSource="ai-verified")

# ===== Q4b: volume of y = sqrt(x ln x), 1 <= x <= e =====
_mp.mp.dps = 25
e_ = _mp.e
vals4 = {
    "good": _mp.pi*_mp.quad(lambda u: u*_mp.log(u), [1, e_]),
    "b1": _mp.pi*_mp.quad(lambda u: _mp.sqrt(u*_mp.log(u)), [1, e_]),
    "b2": 2*_mp.pi*_mp.quad(lambda u: u*_mp.log(u), [1, e_]),
    "b3": _mp.pi*_mp.quad(lambda u: (u*_mp.log(u))**2, [1, e_]),
}
assert abs(vals4["good"] - _mp.pi*(e_**2 + 1)/4) < 1e-15
assert all(abs(vals4[k] - vals4["good"]) > 1e-3 for k in ("b1", "b2", "b3"))
AF4 = x**2*sp.log(x)/2 - x**2/4
assert same(sp.diff(AF4, x), x*sp.log(x))
I4 = sp.integrate(x*sp.log(x), (x, 1, sp.E))
assert sp.simplify(I4 - (sp.E**2 + 1)/4) == 0

add(4, "ב",
    rubric=rub(("נוסחת הדיסקות $V=\\pi\\int_1^e f^2(x)\\,dx=\\pi\\int_1^ex\\ln x\\,dx$", 3),
               ("אינטגרציה בחלקים עם $u=\\ln x$, $dv=x\\,dx$", 2),
               ("קדומה $\\frac{x^2}{2}\\ln x-\\frac{x^2}{4}$ והצבת הגבולות", 3),
               ("תשובה סופית $V=\\frac{\\pi}{4}\\left(e^2+1\\right)$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח לרבע את הפונקציה: $\\left(\\sqrt{x\\ln x}\\right)^2=x\\ln x$, בלי שורש.",
              "לבחור $u=x$ ו-$dv=\\ln x\\,dx$: זה מסבך את החישוב ללא צורך.",
              "לטעות בהצבת הגבול התחתון: ב-$x=1$ מתקבל $\\frac{1}{2}\\ln1-\\frac{1}{4}=-\\frac{1}{4}$ ולא $0$."],
    steps=[
        ch("איזה ביטוי נותן את נפח הסיבוב סביב ציר ה-$X$?", r"$V=\pi\int_1^ex\ln x\,dx$",
           [r"$V=\pi\int_1^e\sqrt{x\ln x}\,dx$", r"$V=2\pi\int_1^ex\ln x\,dx$", r"$V=\pi\int_1^e\left(x\ln x\right)^2dx$"],
           "שיטת הדיסקות: $V=\\pi\\int y^2dx$ ו-$y^2=x\\ln x$. ערכי האפשרויות שונים זה מזה (נבדק מספרית)."),
        chx("מהי הקדומה של $x\\ln x$ (בלי הקבוע)?", AF4,
            [x**2*sp.log(x)/2 - x**2/2, x**2*sp.log(x)/2, x*sp.log(x) - x],
            lambda e: same(sp.diff(e, x), x*sp.log(x)),
            "בחלקים: $\\frac{x^2}{2}\\ln x-\\int\\frac{x}{2}dx=\\frac{x^2}{2}\\ln x-\\frac{x^2}{4}$ (נבדק ב-sympy)."),
        num("מהו $\\int_1^ex\\ln x\\,dx$? (עשרוני)", I4, "$\\frac{e^2+1}{4}\\approx2.0973$."),
        num("מהו הנפח $V=\\frac{\\pi}{4}\\left(e^2+1\\right)$? (עשרוני)", sp.pi*I4, "$V\\approx6.589$.", nd=3),
    ],
    stepsSource="ai-verified")

# ===== Q5a: lim x^{1/sin(2x-2)}, x -> 1 =====
assert sp.limit((1 + x)**(1/x), x, 0) == sp.E and sp.limit(x/sp.sin(2*x), x, 0) == R(1, 2)
_mp.mp.dps = 30
_h = _mp.mpf('1e-9')
_val = (1 + _h)**(1/_mp.sin(2*_h))
assert abs(_val - _mp.sqrt(_mp.e)) < 1e-6

add(5, "א",
    rubric=rub(("זיהוי הצורה $1^\\infty$", 2),
               ("כתיבה כ-$(1+(x-1))^{\\frac{1}{x-1}\\cdot\\frac{x-1}{\\sin(2x-2)}}$", 3),
               ("שימוש ב-$\\lim_{u\\to0}(1+u)^{\\frac{1}{u}}=e$", 1),
               ("חישוב גבול המעריך $\\frac{x-1}{\\sin(2x-2)}\\to\\frac{1}{2}$", 2),
               ("תשובה סופית $\\sqrt{e}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להניח ש-$1^\\infty=1$: הבסיס מתקרב ל-$1$ אבל המעריך מתפוצץ.",
              "לשכוח את החלוקה ב-$2$: $\\sin(2x-2)\\approx2(x-1)$, ולכן המעריך הוא $\\frac{1}{2}$ ולא $1$.",
              "להפעיל לופיטל ישירות על הביטוי החזקתי בלי לקחת לוגריתם."],
    steps=[
        ch("מהי הצורה הלא מוגדרת של $\\lim_{x\\to1}x^{\\frac{1}{\\sin(2x-2)}}$?", "$1^\\infty$",
           ["$0^0$", "$\\infty^0$", "$\\frac{0}{0}$"],
           "הבסיס $x\\to1$ והמעריך $\\frac{1}{\\sin(2x-2)}\\to\\pm\\infty$."),
        num("מהו $\\lim_{u\\to0}(1+u)^{\\frac{1}{u}}$ (עם $u=x-1$)? (עשרוני)", sp.E, "זהו הגבול היסודי $e\\approx2.7183$."),
        num("מהו $\\lim_{x\\to1}\\frac{x-1}{\\sin(2x-2)}$?", R(1, 2),
            "$\\frac{x-1}{\\sin(2(x-1))}=\\frac{1}{2}\\cdot\\frac{2(x-1)}{\\sin(2(x-1))}\\to\\frac{1}{2}$."),
        ch("מהו הגבול המבוקש?", "$\\sqrt{e}$", ["$e$", "$e^2$", "$1$"],
           "$e^{\\frac{1}{2}}=\\sqrt{e}$ (נבדק מספרית)."),
    ],
    stepsSource="ai-verified")

# ===== Q5b: differentiability at 0 of x arctan(1/x^2) =====
f5 = x*sp.atan(1/x**2)
P5 = (0.3, 0.8, -0.5, 1.5, -1.2)
assert same(f5/x, sp.atan(1/x**2), pts=P5)
assert sp.limit(sp.atan(1/x**2), x, 0, '+') == sp.pi/2 and sp.limit(sp.atan(1/x**2), x, 0, '-') == sp.pi/2
assert sp.limit(f5, x, 0) == 0

add(5, "ב",
    rubric=rub(("הגדרת הנגזרת כגבול $\\lim_{\\Delta x\\to0}\\frac{f(\\Delta x)-f(0)}{\\Delta x}$", 3),
               ("פישוט למנה $\\arctan\\frac{1}{\\Delta x^2}$", 2),
               ("חישוב הגבול $\\frac{\\pi}{2}$ משני הצדדים", 3),
               ("מסקנה: הפונקציה גזירה ב-$0$ ו-$f'(0)=\\frac{\\pi}{2}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לגזור את הנוסחה $x\\arctan\\frac{1}{x^2}$ ולהציב $x=0$: הנוסחה לא מוגדרת ב-$0$, ולכן חייבים להשתמש בהגדרה.",
              "לטעון ש-$\\arctan\\frac{1}{\\Delta x^2}\\to0$ כי המעריך \"קטן\": הארגומנט $\\frac{1}{\\Delta x^2}\\to\\infty$ ולכן הערך $\\frac{\\pi}{2}$.",
              "לשכוח לבדוק שהגבול זהה משני הצדדים (כאן הוא זהה כי $\\Delta x^2$ זוגית)."],
    steps=[
        chx("מהו מנת ההפרש $\\frac{f(\\Delta x)-f(0)}{\\Delta x}$ עבור $\\Delta x\\neq0$ (כאשר $f(\\Delta x)=\\Delta x\\arctan\\frac{1}{\\Delta x^2}$)?",
            sp.atan(1/x**2),
            [x*sp.atan(1/x**2), sp.atan(1/x**2)/x, sp.atan(x**2)],
            lambda e: same(e, f5/x, pts=P5),
            "המונה הוא $\\Delta x\\arctan\\frac{1}{\\Delta x^2}-0$, ולכן חלוקה ב-$\\Delta x$ משאירה $\\arctan\\frac{1}{\\Delta x^2}$ (נבדק ב-sympy)."),
        num("מהו $\\lim_{\\Delta x\\to0}\\arctan\\frac{1}{\\Delta x^2}$? (עשרוני)", sp.pi/2,
            "הארגומנט $\\frac{1}{\\Delta x^2}\\to+\\infty$ משני הצדדים, ו-$\\arctan\\to\\frac{\\pi}{2}\\approx1.5708$ (אומת ב-sympy)."),
        ch("מהי המסקנה לגבי גזירות $f$ ב-$x=0$?", "גזירה ב-$0$ ו-$f'(0)=\\frac{\\pi}{2}$",
           ["גזירה ב-$0$ ו-$f'(0)=0$", "לא גזירה: הגבול משמאל שונה מהגבול מימין", "לא גזירה כי $f$ אינה רציפה ב-$0$"],
           "שני הגבולות החד-צדדיים שווים ל-$\\frac{\\pi}{2}$, ו-$f$ רציפה ב-$0$ כי $|f(x)|\\le\\frac{\\pi}{2}|x|\\to0=f(0)$ (נבדק ב-sympy)."),
    ],
    stepsSource="ai-verified")

# ===== Q6a: area between 1/(1+x^2) and 3/(9+x^2) =====
u6, l6 = 1/(1 + x**2), 3/(9 + x**2)
S6 = 2*(sp.atan(sp.sqrt(3)) - sp.atan(sp.sqrt(3)/3))
assert abs(sp.N(S6 - 2*sp.Integral(u6 - l6, (x, 0, sp.sqrt(3))), 20)) < 1e-12 and sp.simplify(S6 - sp.pi/3) == 0 and sorted(sp.solve(sp.Eq(u6, l6), x)) == [-sp.sqrt(3), sp.sqrt(3)]
assert u6.subs(x, 0) > l6.subs(x, 0) and u6.subs(x, 1) > l6.subs(x, 1)

add(6, "א",
    rubric=rub(("נקודות החיתוך של הגרפים: $x=\\pm\\sqrt{3}$", 3),
               ("זיהוי הפונקציה העליונה $\\frac{1}{1+x^2}$ ובניית $S=2\\int_0^{\\sqrt{3}}\\left(\\frac{1}{1+x^2}-\\frac{3}{9+x^2}\\right)dx$", 3),
               ("קדומות: $\\arctan x$ ו-$\\arctan\\frac{x}{3}$", 2),
               ("הצבת הגבולות ותשובה $\\frac{\\pi}{3}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח שהפונקציות זוגיות, ולחשב מ-$0$ עד $\\sqrt{3}$ בלי להכפיל ב-$2$ (או לחשב מ-$-\\sqrt{3}$ עד $\\sqrt{3}$).",
              "לאנטגרל $\\frac{3}{9+x^2}$ כ-$3\\arctan\\frac{x}{3}$ במקום $\\arctan\\frac{x}{3}$.",
              "להחסיר בסדר הפוך (התחתונה פחות העליונה) ולקבל שטח שלילי."],
    steps=[
        num("מהו הערך החיובי של $x$ שבו הגרפים נחתכים? (עשרוני)", sp.sqrt(3),
            "$3+3x^2=9+x^2$ נותן $x^2=3$, ולכן $x=\\sqrt{3}\\approx1.7321$."),
        ch("איזו פונקציה נמצאת מעל השנייה בקטע $\\left(-\\sqrt{3},\\sqrt{3}\\right)$?", "$y=\\frac{1}{1+x^2}$ (מעל $y=\\frac{3}{9+x^2}$)",
           ["$y=\\frac{3}{9+x^2}$ (מעל $y=\\frac{1}{1+x^2}$)", "הגרפים משתנים לסירוגין", "הגרפים מתלכדים בכל הקטע"],
           "ב-$x=0$: $1>\\frac{1}{3}$, ואין חיתוך נוסף בקטע, ולכן $\\frac{1}{1+x^2}$ למעלה (נבדק ב-sympy)."),
        chx("מהי קדומה של $\\frac{3}{9+x^2}$?", sp.atan(x/3),
            [3*sp.atan(x/3), sp.atan(x/3)/3, sp.atan(3*x)],
            lambda e: same(sp.diff(e, x), l6),
            "$\\int\\frac{3}{9+x^2}dx=3\\cdot\\frac{1}{3}\\arctan\\frac{x}{3}=\\arctan\\frac{x}{3}$ (נבדק ב-sympy)."),
        num("מהו השטח הכלוא? (עשרוני)", S6, "$2\\left(\\frac{\\pi}{3}-\\frac{\\pi}{6}\\right)=\\frac{\\pi}{3}\\approx1.0472$."),
    ],
    stepsSource="ai-verified")

# ===== Q6b: Maclaurin of ln(1+x) of order 2, ln 0.9 =====
y6 = sp.log(1 + x)
assert sp.diff(y6, x, 2).subs(x, 0) == -1 and sp.diff(y6, x).subs(x, 0) == 1
T2 = x - x**2/2
assert T2.subs(x, R(-1, 10)) == R(-21, 200)
coef6 = sp.diff(y6, x, 3)/6
assert same(coef6, 1/(3*(1 + x)**3), pts=(0.2, 0.5, 1.0, 2.0, 3.0))
bound6 = R(1, 10)**3/(3*R(9, 10)**3)
assert sp.N(bound6) > abs(sp.N(sp.log(R(9, 10)) - T2.subs(x, R(-1, 10))))

add(6, "ב",
    rubric=rub(("פולינום מקלורן מסדר 2: $y(0)=0$, $y'(0)=1$, $y''(0)=-1$, כלומר $x-\\frac{x^2}{2}$", 3),
               ("הצבה $x=-0.1$ וקירוב $\\ln0.9\\approx-0.105$", 2),
               ("שארית לגרנז' $R_2(x)=\\frac{1}{3(1+c)^3}x^3$ עם $c$ בין $x$ ל-$0$", 2),
               ("חסם $\\left|R_2\\right|<\\frac{(0.1)^3}{3\\cdot(0.9)^3}\\approx0.00046$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את החלוקה ב-$2!$ באיבר $-\\frac{x^2}{2}$.",
              "להעריך את השארית עם $c=0$ במקום להשתמש בכך ש-$1+c>0.9$ כדי לחסום את המכנה מלמטה.",
              "לחשב את הנגזרת השלישית כ-$\\frac{1}{(1+x)^3}$ בלי הגורם $2$: $y'''=\\frac{2}{(1+x)^3}$, ואז לחלק ב-$3!$ נותן $\\frac{1}{3(1+x)^3}$."],
    steps=[
        num("מהו $y''(0)$ עבור $y=\\ln(1+x)$?", -1, "$y'=\\frac{1}{1+x}$ ו-$y''=-\\frac{1}{(1+x)^2}$, ולכן $y''(0)=-1$."),
        num("מהו הקירוב $T_2(-0.1)=-0.1-\\frac{(-0.1)^2}{2}$ ל-$\\ln0.9$? (עשרוני)", R(-21, 200),
            "$-0.1-0.005=-0.105$.", tol=0.0005),
        chx("מהו מקדם השארית $\\frac{y'''(c)}{3!}$ עבור $y=\\ln(1+x)$?", 1/(3*(1 + x)**3),
            [1/(6*(1 + x)**3), 2/(1 + x)**3, 1/(3*(1 + x)**2)],
            lambda e: same(e.subs(x, x), coef6, pts=(0.2, 0.5, 1.0, 2.0, 3.0)),
            "$y'''=\\frac{2}{(1+x)^3}$ ולכן $\\frac{y'''}{3!}=\\frac{1}{3(1+x)^3}$ (נבדק ב-sympy)."),
        num("מהו החסם $\\frac{(0.1)^3}{3\\cdot0.9^3}$ על השגיאה? (עשרוני)", bound6,
            "$\\frac{0.001}{3\\cdot0.729}\\approx0.000457$. הפתרון הרשמי כותב $0.00045$ (קיצוץ); השגיאה בפועל כ-$0.00036$.",
            tol=0.00001, nd=6),
    ],
    stepsSource="ai-verified")


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

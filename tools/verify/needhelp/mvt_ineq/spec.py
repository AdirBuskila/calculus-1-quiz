# -*- coding: utf-8 -*-
"""Source + machine check for the guided course "mvt_ineq" (calculus-1, topic mean_value_theorems).

Every option of every question is written next to a boolean computed by sympy / a dense numeric grid.
Importing this module evaluates all of them and asserts that exactly one option of each mcq is true.
check.py then emits courses/mvt_ineq/C0N.js from LEVELS and re-reads the emitted files to confirm they match.
"""
import numpy as np
import sympy as sp
from sympy.calculus.util import continuous_domain

x = sp.Symbol('x', real=True)
t = sp.Symbol('t', real=True)
a_, b_, c_ = sp.symbols('a b c', real=True)
oo = sp.oo
E = sp.E
R = sp.Rational
exp, log, sqrt = sp.exp, sp.log, sp.sqrt
LEVELS = []
FACTS = []
_pos = [0]


def fact(desc, cond):
    assert bool(cond), "FACT FAILED: " + desc
    FACTS.append(desc)


def eq(a, b):
    return sp.simplify(a - b) == 0


def grid(lo, hi, n=40001):
    """Open-interval grid, endpoints excluded; infinite ends are replaced by a large finite number."""
    lo = -60.0 if lo == -oo else float(lo)
    hi = 60.0 if hi == oo else float(hi)
    d = (hi - lo) * 1e-6
    return np.linspace(lo + d, hi - d, n)


def forall(cond, lo, hi, n=40001):
    """cond(xs) -> boolean ndarray, evaluated on a dense grid of the open interval (lo,hi)."""
    xs = grid(lo, hi, n)
    with np.errstate(all='ignore'):
        r = cond(xs)
    return bool(np.all(r))


def forall2(cond, lo, hi, n=700):
    """cond(a,b) on a dense grid of pairs lo<a<b<hi."""
    g = grid(lo, hi, n)
    A, B = np.meshgrid(g, g)
    m = A < B
    with np.errstate(all='ignore'):
        r = cond(A[m], B[m])
    return bool(np.all(r))


def ineq(desc, lhs, rhs, lo, hi, strict=True, var=x):
    """Numeric grid check of lhs < rhs (or <=) on (lo,hi) for sympy expressions in var, plus record as fact."""
    fl = sp.lambdify(var, lhs, 'numpy')
    fr = sp.lambdify(var, rhs, 'numpy')
    ok = forall(lambda v: (fl(v) < fr(v)) if strict else (fl(v) <= fr(v) + 1e-12), lo, hi)
    assert ok, "INEQ FAILED: " + desc
    FACTS.append("ineq: " + desc)


def sgn(expr, lo, hi, var=x):
    """Sign of a continuous expression on the open interval (lo,hi): verified zero-free, sign at one interior point."""
    I = sp.Interval.open(lo, hi)
    assert sp.solveset(expr, var, I) == sp.EmptySet, ("zero inside", expr, lo, hi)
    if lo == -oo and hi == oo:
        m = 0
    elif lo == -oo:
        m = hi - 1
    elif hi == oo:
        m = lo + 1
    else:
        m = (lo + hi) / 2
    v = sp.N(expr.subs(var, m))
    assert v != 0
    return 1 if v > 0 else -1


def mcq(qid, question, opts, explanation, recap):
    """opts: list of (text, truth). Exactly one truth is True; it is moved to a rotating position."""
    truths = [bool(tv) for _, tv in opts]
    assert sum(truths) == 1, (qid, truths)
    assert len({tx for tx, _ in opts}) == len(opts), qid
    k = _pos[0]
    _pos[0] += 1
    ci = truths.index(True)
    items = list(opts)
    correct = items.pop(ci)
    at = [2, 0, 3, 1][k % 4] % len(opts)
    items.insert(at, correct)
    options = [{"id": "abcdefgh"[i], "value": tx} for i, (tx, _) in enumerate(items)]
    return {"id": qid, "question": question, "options": options, "correctId": "abcdefgh"[at],
            "explanation": explanation, "recap": recap}


def numeric(qid, prompt, answer, truth, explain, recap, tol=0):
    assert abs(float(truth) - float(answer)) <= max(tol, 1e-9), (qid, answer, truth)
    return {"id": qid, "step": {"type": "numeric", "prompt": prompt, "answer": answer, "tol": tol, "explain": explain},
            "recap": recap}


def level(lid, order, icon, title, goal, lesson, questions, boss=False):
    LEVELS.append({"id": lid, "order": order, "icon": icon, "title": title, "goal": goal, "boss": boss,
                   "lesson": lesson, "questions": questions})


def cont_closed(f, lo, hi):
    """f is continuous on the closed interval [lo,hi] (sympy continuous_domain, f given in x)."""
    return sp.Interval(lo, hi).is_subset(continuous_domain(f, x, sp.S.Reals))


def diff_open(f, lo, hi):
    """f' exists and is continuous on the open interval (lo,hi)."""
    return sp.Interval.open(lo, hi).is_subset(continuous_domain(sp.diff(f, x), x, sp.S.Reals))


# ===================================================================== C01  the theorem and its conditions
L1 = r"""
<p>משפט לגרנז' אומר שבין שתי נקודות על גרף חלק יש נקודה שבה <b>המשיק מקביל למיתר</b>. זה הכלי שמאחורי רוב אי-השוויונות במבחנים.</p>
<h3>הנוסחה</h3>
<div class="lesson-formula">אם $f$ רציפה ב-$[a,b]$ וגזירה ב-$(a,b)$, אז קיימת $c\in(a,b)$ כך ש-$\frac{f(b)-f(a)}{b-a}=f'(c)$</div>
<ul>
<li><b>רציפה בקטע סגור:</b> כולל הקצוות $a$ ו-$b$. הפונקציה חייבת להיות מוגדרת בהם.</li>
<li><b>גזירה בקטע פתוח:</b> בקצוות אין צורך בגזירות.</li>
<li>הנקודה $c$ נמצאת <b>בתוך</b> הקטע: $a<c<b$ בשני אי-שוויונות חזקים.</li>
</ul>
<p><b>רול</b> הוא המקרה $f(a)=f(b)$: אז השיפוע הוא $0$ וקיימת $c$ עם $f'(c)=0$.</p>
<div class="lesson-ex">דוגמה: $f(x)=x^2$ ב-$[1,3]$. השיפוע של המיתר: $\frac{9-1}{3-1}=4$. נפתור $f'(c)=2c=4$ ונקבל $c=2$, והיא בתוך $(1,3)$.</div>
<div class="lesson-trap">⚠️ המשפט אומר שקיימת לפחות נקודה אחת. הוא לא אומר שהיא יחידה, ולא נותן נוסחה ל-$c$ בכל מקרה. ב-$x^3$ על $[-1,1]$ יש שתי נקודות, $c=\pm\frac{1}{\sqrt3}$.</div>
<div class="lesson-trap">⚠️ אם תנאי אחד נכשל, המשפט לא חל. ב-$|x|$ על $[-1,1]$ הפונקציה רציפה אבל לא גזירה ב-$0$, ואכן אין שם נקודה עם $f'(c)=0$ למרות $f(-1)=f(1)$.</div>
"""

f1 = x**2
fact("lesson C01: x^2 on [1,3] slope 4, c=2", (f1.subs(x, 3) - f1.subs(x, 1)) / 2 == 4 and sp.solve(sp.diff(f1, x) - 4, x) == [2])
fact("lesson C01: x^3 on [-1,1] has two c = +-1/sqrt3",
     set(sp.solve(sp.diff(x**3, x) - 1, x)) == {1/sqrt(3), -1/sqrt(3)})

q = []
# which function satisfies the hypotheses on [0,4]
sqrt_ok = sp.limit(sqrt(x), x, 0, '+') == 0 and diff_open(sqrt(x), 0, 4) and cont_closed(sqrt(x), 0, 4)
recip_ok = sp.Interval(0, 4).is_subset(continuous_domain(1/(x - 2), x, sp.S.Reals))
absf = sp.Abs(x - 1)
abs_ok = sp.limit((absf - absf.subs(x, 1)) / (x - 1), x, 1, '-') == sp.limit((absf - absf.subs(x, 1)) / (x - 1), x, 1, '+')
ln_ok = sp.limit(log(x), x, 0, '+') != -oo
q.append(mcq("C01-Q1", r"באיזו מהפונקציות הבאות מתקיימים תנאי משפט לגרנז' בקטע $[0,4]$ ?", [
    (r"$f(x)=\sqrt{x}$", sqrt_ok),
    (r"$f(x)=\frac{1}{x-2}$", recip_ok),
    (r"$f(x)=|x-1|$", abs_ok),
    (r"$f(x)=\ln x$", ln_ok),
], r"$\sqrt{x}$ רציפה ב-$[0,4]$ (גם ב-$0$, כי $\sqrt0=0$) וגזירה ב-$(0,4)$, והנגזרת $\frac{1}{2\sqrt{x}}$ קיימת בכל הקטע הפתוח. ‏$\frac{1}{x-2}$ לא מוגדרת ב-$x=2$ שבתוך הקטע. ‏$|x-1|$ לא גזירה ב-$x=1$ (הנגזרות החד-צדדיות הן $-1$ ו-$1$). ‏$\ln x$ לא מוגדרת בקצה $x=0$.",
    "בודקים: מוגדרת ורציפה בכל הקטע הסגור, וגזירה בקטע הפתוח"))
fact("C01-Q1 sqrt ok, others fail", sqrt_ok and not recip_ok and not abs_ok and not ln_ok)

c2 = sp.solve(sp.diff(x**3, x) - (8 - 0) / sp.Integer(2), x)
c2 = [s for s in c2 if 0 < s < 2][0]
q.append(numeric("C01-Q2", r"מצאו את הנקודה $c\in(0,2)$ שמובטחת על ידי משפט לגרנז' עבור $f(x)=x^3$ בקטע $[0,2]$ (בעשרוני)",
                 1.1547, c2, r"השיפוע של המיתר: $\frac{8-0}{2-0}=4$. הנגזרת $f'(c)=3c^2=4$ נותנת $c=\pm\frac{2}{\sqrt3}$. רק $c=\frac{2}{\sqrt3}\approx1.1547$ בתוך $(0,2)$.",
                 "משווים f'(c) לשיפוע המיתר ובוחרים את הפתרון שבתוך הקטע", tol=0.001))

c3 = sp.solve(1/c_ - 1/(E - 1), c_)[0]
assert 1 < c3 < E
q.append(numeric("C01-Q3", r"מצאו את הנקודה $c\in(1,e)$ שמובטחת על ידי משפט לגרנז' עבור $f(x)=\ln x$ בקטע $[1,e]$ (בעשרוני)",
                 1.7183, c3, r"השיפוע של המיתר: $\frac{\ln e-\ln1}{e-1}=\frac{1}{e-1}$. הנגזרת $f'(c)=\frac1c$, ולכן $\frac1c=\frac{1}{e-1}$ ו-$c=e-1\approx1.7183$, שנמצא בין $1$ ל-$e\approx2.718$.",
                 "f'(c) = 1/c: משווים לשיפוע ופותרים", tol=0.001))

fr_ = x**2 - 4*x + 3
assert fr_.subs(x, 1) == fr_.subs(x, 3) == 0
c4 = sp.solve(sp.diff(fr_, x), x)[0]
q.append(numeric("C01-Q4", r"עבור $f(x)=x^2-4x+3$ מתקיים $f(1)=f(3)$. לפי משפט רול, באיזו נקודה $c\in(1,3)$ מתקיים $f'(c)=0$ ?",
                 2, c4, r"$f(1)=f(3)=0$, ולכן קיימת $c$ עם $f'(c)=0$. ‏$f'(x)=2x-4=0$ נותן $c=2$, בתוך הקטע.",
                 "רול: ערכי הקצוות שווים ← נגזרת מתאפסת באמצע"))

# theorem content
xs3 = [s for s in sp.solve(sp.diff(x**3, x) - 1, x) if -1 < s < 1]
mid_ok = abs(float(c2) - 1.0) < 1e-9
q.append(mcq("C01-Q5", r"מה קובע משפט לגרנז' עבור $f$ המקיימת את התנאים בקטע $[a,b]$ ?", [
    (r"קיימת לפחות נקודה אחת $c\in(a,b)$ שבה $f'(c)$ שווה לשיפוע המיתר", True),
    (r"קיימת בדיוק נקודה אחת $c$ כזו", len(xs3) == 1),
    (r"בכל נקודה $c\in(a,b)$ מתקיים ש-$f'(c)$ שווה לשיפוע המיתר", sp.diff(x**2, x).subs(x, R(1, 2)) == 2),
    (r"הנקודה $c$ היא תמיד אמצע הקטע $\frac{a+b}{2}$", mid_ok),
], r"המשפט מבטיח **לפחות** נקודה אחת בקטע הפתוח. ‏$x^3$ ב-$[-1,1]$ נותנת שתי נקודות ($\pm\frac1{\sqrt3}$), ולכן אין יחידות. ‏$x^2$ ב-$[0,2]$ נותנת $f'(c)=2c$ ששווה לשיפוע $2$ רק ב-$c=1$, לא בכל נקודה. ‏$x^3$ ב-$[0,2]$ נותנת $c\approx1.15$ ולא $1$, ולכן $c$ אינה בהכרח האמצע.",
    "לפחות נקודה אחת c בתוך הקטע הפתוח, בלי יחידות ובלי מיקום"))
fact("C01-Q5 counterexamples", len(xs3) == 2 and not mid_ok)

q.append(mcq("C01-Q6", r"עבור $f(x)=|x|$ בקטע $[-1,1]$ מתקיים $f(-1)=f(1)$, אבל אין $c$ עם $f'(c)=0$. איזה תנאי של משפט רול נכשל ?", [
    (r"גזירות ב-$0$, שבתוך הקטע הפתוח", sp.limit(sp.Abs(x) / x, x, 0, '-') != sp.limit(sp.Abs(x) / x, x, 0, '+')),
    (r"רציפות בקטע הסגור", not cont_closed(sp.Abs(x), -1, 1)),
    (r"השוויון $f(-1)=f(1)$", sp.Abs(-1) != sp.Abs(1)),
    (r"אף תנאי לא נכשל", False),
], r"‏$|x|$ רציפה בכל הקטע, וגם $f(-1)=f(1)=1$. מה שנכשל הוא הגזירות ב-$x=0$, כי הנגזרת החד-צדדית משמאל היא $-1$ ומימין $+1$. בכל נקודה אחרת $f'=\pm1\neq0$, ולכן הטענה של רול באמת לא מתקיימת. אילו כל התנאים התקיימו, הייתה $c$.",
    "אם תנאי אחד נכשל, המסקנה יכולה להיכשל"))
level("C01", 1, "📐", "משפט לגרנז' ותנאיו",
      "לנסח את משפט לגרנז' ורול, לבדוק מתי הם חלים, ולמצוא את הנקודה $c$ במקרים פשוטים.",
      L1, q)

# ===================================================================== C02  bounding f'(c)
L2 = r"""
<p>מהמשפט מקבלים $f'(c)$ עבור $c$ <b>לא ידועה</b>, ויודעים רק שהיא בין $a$ ל-$b$. הטריק: לחסום את $f'(c)$ לפי המיקום של $c$.</p>
<h3>כלל החסימה</h3>
<ul>
<li>אם $f'$ <b>עולה</b> בקטע ($f''>0$): מ-$a<c<b$ נובע $f'(a)<f'(c)<f'(b)$.</li>
<li>אם $f'$ <b>יורדת</b> בקטע ($f''<0$): מ-$a<c<b$ נובע $f'(b)<f'(c)<f'(a)$. החסם התחתון בא מהקצה הימני.</li>
</ul>
<p>הנגזרות שחוזרות בשאלות:</p>
<table>
<tr><td>$(\ln(1+t))'=\frac{1}{1+t}$</td><td>יורדת עבור $t>0$</td></tr>
<tr><td>$(\ln t)'=\frac1t$</td><td>יורדת עבור $t>0$</td></tr>
<tr><td>$(e^t)'=e^t$</td><td>עולה</td></tr>
<tr><td>$(\arctan t)'=\frac{1}{1+t^2}$</td><td>יורדת עבור $t>0$</td></tr>
<tr><td>$(\arcsin t)'=\frac{1}{\sqrt{1-t^2}}$</td><td>עולה עבור $0<t<1$</td></tr>
</table>
<div class="lesson-ex">דוגמה: $\frac{\ln(1+x)}{x}=\frac{1}{1+c}$ עם $0<c<x$. מ-$1<1+c<1+x$ נובע, אחרי היפוך, $\frac{1}{1+x}<\frac{1}{1+c}<1$.</div>
<div class="lesson-rule">🔑 בסוף מכפילים את כל השרשרת ב-$b-a$. כשהוא חיובי, כיוון האי-שוויונות נשמר, ואז אפשר להעביר את המכנה של המנה.</div>
<div class="lesson-trap">⚠️ היפוך מחליף כיוון: מ-$1<c<2$ נובע $\frac12<\frac1c<1$, ולא $1<\frac1c<2$.</div>
"""
fact("lesson C02: 1/(1+t) decreasing, 1/sqrt(1-t^2) increasing on (0,1)",
     sgn(sp.diff(1/(1 + x), x), 0, oo) == -1 and sgn(sp.diff(1/sqrt(1 - x**2), x), 0, 1) == 1)
fact("lesson C02: e^t increasing, 1/t and arctan' decreasing for t>0",
     sgn(sp.diff(exp(x), x), -oo, oo) == 1 and sgn(sp.diff(1/x, x), 0, oo) == -1 and sgn(sp.diff(1/(1 + x**2), x), 0, oo) == -1)

q = []
cv = lambda lo, hi: np.linspace(lo, hi, 20001)[1:-1]
q.append(mcq("C02-Q1", r"אם $1<c<2$, בין אילו ערכים נמצא $\frac1c$ ?", [
    (r"$\frac12<\frac1c<1$", forall(lambda v: (0.5 < 1/v) & (1/v < 1), 1, 2)),
    (r"$1<\frac1c<2$", forall(lambda v: (1 < 1/v) & (1/v < 2), 1, 2)),
    (r"$\frac1c<\frac12$", forall(lambda v: 1/v < 0.5, 1, 2)),
    (r"$\frac1c>1$", forall(lambda v: 1/v > 1, 1, 2)),
], r"‏$\frac1t$ יורדת: ככל ש-$c$ גדלה מ-$1$ ל-$2$, הערך $\frac1c$ קטן מ-$1$ ל-$\frac12$, ולכן $\frac12<\frac1c<1$. בבדיקה ב-$c=1.5$ מתקבל $\frac1c\approx0.67$: זה לא קטן מ-$\frac12$, לא גדול מ-$1$, ולא נמצא בין $1$ ל-$2$.",
    "פונקציה יורדת: החסם התחתון בא מהקצה הימני"))

lo_ = 1 / sqrt(1 - a_**2)
q.append(mcq("C02-Q2", r"$f(x)=\arcsin x$, ו-$0<c<a<1$. בין אילו ערכים נמצא $f'(c)=\frac{1}{\sqrt{1-c^2}}$ ?", [
    (r"$1<f'(c)<\frac{1}{\sqrt{1-a^2}}$", forall2(lambda A, B: (1 < 1/np.sqrt(1 - (A + (B - A)/2)**2)) & (1/np.sqrt(1 - (A + (B - A)/2)**2) < 1/np.sqrt(1 - B**2)), 0, 1)),
    (r"$\frac{1}{\sqrt{1-a^2}}<f'(c)<1$", False),
    (r"$0<f'(c)<1$", False),
    (r"$f'(c)>\frac{1}{\sqrt{1-a^2}}$", False),
], r"‏$\frac{1}{\sqrt{1-t^2}}$ עולה עבור $0<t<1$. ב-$t=0$ ערכה $1$, וב-$t=a$ ערכה $\frac{1}{\sqrt{1-a^2}}$. ‏$c$ בתוך $(0,a)$, ולכן $1<f'(c)<\frac{1}{\sqrt{1-a^2}}$. הסדר ההפוך מתאים לפונקציה יורדת. הטענות $0<f'(c)<1$ ו-$f'(c)>\frac{1}{\sqrt{1-a^2}}$ שגויות, כי $\frac{1}{\sqrt{1-c^2}}>1$ תמיד, והיא קטנה מהערך ב-$a$.",
    "פונקציה עולה: החסם התחתון בא מהקצה השמאלי"))
fact("C02-Q2 arcsin' > 1 on (0,1) and < value at a",
     forall(lambda v: 1/np.sqrt(1 - v**2) > 1, 0, 1) and not forall(lambda v: 1/np.sqrt(1 - v**2) < 1, 0, 1))

q.append(numeric("C02-Q3", r"אם $1<c<3$ ו-$f'(c)=\frac{1}{1+c}$, מהו החסם העליון על $f'(c)$ שמתקבל מקצות הקטע ? (עשרוני)",
                 0.5, R(1, 2), r"‏$\frac{1}{1+c}$ יורדת, ולכן החסם העליון בא מהקצה השמאלי $c=1$: $\frac{1}{1+1}=0.5$. החסם התחתון הוא $\frac{1}{1+3}=0.25$.",
                 "יורדת: החסם העליון מהקצה השמאלי"))

q.append(mcq("C02-Q4", r"ידוע ש-$\frac{1}{1+x}<\frac{\ln(1+x)}{x}<1$ עבור $x>0$. מה מתקבל אחרי הכפלה ב-$x$ ?", [
    (r"$\frac{x}{1+x}<\ln(1+x)<x$", forall(lambda v: (v/(1+v) < np.log1p(v)) & (np.log1p(v) < v), 0, oo)),
    (r"$x(1+x)<\ln(1+x)<x^2$", forall(lambda v: (v*(1+v) < np.log1p(v)) & (np.log1p(v) < v**2), 0, oo)),
    (r"$\frac{1}{1+x}<\ln(1+x)<1$", forall(lambda v: (1/(1+v) < np.log1p(v)) & (np.log1p(v) < 1), 0, oo)),
    (r"$x<\ln(1+x)<\frac{x}{1+x}$", forall(lambda v: (v < np.log1p(v)) & (np.log1p(v) < v/(1+v)), 0, oo)),
], r"הכפלה במספר חיובי $x$ שומרת את הכיוון ומכפילה כל אגף: $\frac{x}{1+x}<\ln(1+x)<x$. בדיקה ב-$x=3$: $0.75<1.386<3$ נכון, ואילו האפשרות עם $x^2$ נכשלת כבר ב-$x=1$ ($2<0.69$ שקר), האפשרות בלי הכפלה נכשלת ב-$x=3$ ($1.386<1$ שקר), והאפשרות ההפוכה נכשלת ב-$x=1$.",
    "מכפילים את כל האגפים ב-(b−a) החיובי, הכיוון נשמר"))

q.append(numeric("C02-Q5", r"מהאי-שוויון $\frac{x}{1+x}<\ln(1+x)<x$ עבור $x=1$ מקבלים חסם תחתון על $\ln2$. מהו ? (עשרוני)",
                 0.5, R(1, 1) / 2, r"מציבים $x=1$: החסם התחתון $\frac{1}{1+1}=0.5$ והעליון $1$. בפועל $\ln2\approx0.693$, בין השניים.",
                 "מציבים ערך ספציפי באי-שוויון שהוכח"))
fact("C02-Q5 ln2 between", 0.5 < float(sp.log(2)) < 1)
level("C02", 2, "🔍", "לחסום את f'(c)",
      "לחסום את $f'(c)$ לפי מיקום $c$ בקטע, ולהכפיל בחזרה בארך הקטע.",
      L2, q)

# ===================================================================== C03  choosing the function and interval
L3 = r"""
<p>החלק הקשה בשאלה הוא <b>איזו פונקציה ואיזה קטע</b>. כלל אצבע: מסתכלים על הביטוי באמצע האי-שוויון, ומחפשים $f$ ו-$[a,b]$ כך ש-$\frac{f(b)-f(a)}{b-a}$ שווה בדיוק לו.</p>
<ul>
<li>הביטוי באמצע הוא $\ln(1+x)$ ← $f(t)=\ln(1+t)$ בקטע $[0,x]$, כי $\frac{\ln(1+x)-\ln1}{x-0}=\frac{\ln(1+x)}{x}$.</li>
<li>הביטוי באמצע הוא $\arcsin a$ ← $f(t)=\arcsin t$ בקטע $[0,a]$.</li>
<li>הביטוי באמצע הוא $\tan x$ ← $f(t)=\tan t$ בקטע $[0,x]$.</li>
<li>הביטוי באמצע הוא $\ln x$ עם $x>1$ ← $f(t)=\ln t$ בקטע $[1,x]$, כי $\ln1=0$.</li>
</ul>
<p>הקצה שבו הפונקציה מתאפסת ($0$ או $1$) מפשט את ההפרש.</p>
<div class="lesson-rule">🔑 לפני שמתחילים: האם הפונקציה מוגדרת ורציפה בכל הקטע הסגור? אם הקטע כולל נקודה שבה היא לא מוגדרת, בוחרים קטע אחר.</div>
<div class="lesson-trap">⚠️ $\ln t$ בקטע $[0,x]$ לא עובד ($\ln0$ לא מוגדר), וגם $\tan t$ בקטע $[0,\frac\pi2]$ לא עובד ($\tan$ לא מוגדרת ב-$\frac\pi2$).</div>
"""
q = []
opt = lambda f, lo, hi: sp.simplify((f.subs(x, hi) - f.subs(x, lo)) / (hi - lo))

def quo_is(f, lo, hi, target):
    return eq((f.subs(x, hi) - f.subs(x, lo)) / (hi - lo), target)

xx = sp.Symbol('xx', positive=True)
q.append(mcq("C03-Q1", r"כדי להוכיח $\frac{x}{1+x}<\ln(1+x)<x$ עבור $x>0$ מפעילים את לגרנז' בקטע $[0,x]$. איזו $f$ נותנת $\frac{f(x)-f(0)}{x-0}=\frac{\ln(1+x)}{x}$ ומקיימת את התנאים ?", [
    (r"$f(t)=\ln(1+t)$", sp.simplify((log(1 + x) - log(1 + 0)) / x - log(1 + x)/x) == 0 and cont_closed(log(1 + x), 0, 5)),
    (r"$f(t)=\ln t$", sp.limit(log(x), x, 0, '+') != -oo),
    (r"$f(t)=t-\ln(1+t)$", quo_is(x - log(1 + x), 0, x, log(1 + x)/x)),
    (r"$f(t)=e^t$", quo_is(exp(x), 0, x, log(1 + x)/x)),
], r"‏$f(t)=\ln(1+t)$ נותנת $\frac{\ln(1+x)-\ln1}{x}=\frac{\ln(1+x)}{x}$ והיא רציפה וגזירה בכל $[0,x]$. ‏$\ln t$ לא מוגדרת ב-$0$. ‏$t-\ln(1+t)$ נותנת $1-\frac{\ln(1+x)}{x}$, ו-$e^t$ נותנת $\frac{e^x-1}{x}$. לאף אחת מהן המנה אינה $\frac{\ln(1+x)}{x}$.",
    "בוחרים f שההפרש שלה על הקטע הוא בדיוק הביטוי שבאמצע"))

q.append(mcq("C03-Q2", r"להוכחת $a<\arcsin a<\frac{a}{\sqrt{1-a^2}}$ עבור $0<a<1$ מפעילים את לגרנז' בקטע $[0,a]$. איזו $f$ נותנת מנה השווה ל-$\frac{\arcsin a}{a}$ ?", [
    (r"$f(t)=\arcsin t$", quo_is(sp.asin(x), 0, a_, sp.asin(a_)/a_)),
    (r"$f(t)=\sin t$", quo_is(sp.sin(x), 0, a_, sp.asin(a_)/a_)),
    (r"$f(t)=\arcsin t-t$", quo_is(sp.asin(x) - x, 0, a_, sp.asin(a_)/a_)),
    (r"$f(t)=\frac{t}{\sqrt{1-t^2}}$", quo_is(x/sqrt(1 - x**2), 0, a_, sp.asin(a_)/a_)),
], r"‏$\arcsin$ מוגדרת ורציפה ב-$[0,a]$ וגזירה ב-$(0,a)$ (כי $a<1$), והמנה היא $\frac{\arcsin a-0}{a}$. ‏$\sin t$ נותנת $\frac{\sin a}{a}$, ‏$\arcsin t-t$ נותנת $\frac{\arcsin a}{a}-1$, ו-$\frac{t}{\sqrt{1-t^2}}$ נותנת $\frac{1}{\sqrt{1-a^2}}$.",
    "הביטוי באמצע הוא f(a), עם f(0)=0 בקצה השני"))

tan_q = sp.tan(x)
tan_cont = lambda hi: hi < sp.pi/2
q.append(mcq("C03-Q3", r"להוכחת $\tan x>x$ עבור $0<x<\frac\pi2$ בוחרים $f(t)=\tan t$. באיזה קטע מתקיימים תנאי המשפט לכל $x$ כזה, והמנה היא $\frac{\tan x}{x}$ ?", [
    (r"$[0,x]$", True),
    (r"$\left[0,\frac\pi2\right]$", tan_cont(sp.pi/2)),
    (r"$[0,\pi]$", tan_cont(sp.pi)),
    (r"$\left[x,\frac\pi2\right]$", tan_cont(sp.pi/2)),
], r"‏$\tan t$ רציפה בכל $[0,x]$ כל עוד $x<\frac\pi2$, והמנה היא $\frac{\tan x-\tan0}{x-0}=\frac{\tan x}{x}$. בשלושת הקטעים האחרים הנקודה $\frac\pi2$ נכללת, ושם $\tan$ לא מוגדרת, ולכן הרציפות נכשלת. הקטע האחרון גם נותן מנה אחרת.",
    "הקטע חייב להישאר בתוך תחום הרציפות של הפונקציה"))
fact("C03-Q3 tan blows up at pi/2", sp.limit(sp.tan(x), x, sp.pi/2, '-') == oo and quo_is(sp.tan(x), 0, a_, sp.tan(a_)/a_))

q.append(mcq("C03-Q4", r"להוכחת $\frac{x-1}{x}<\ln x<x-1$ עבור $x>1$ מפעילים את לגרנז' על $f(t)=\ln t$. באיזה קטע המנה היא $\frac{\ln x}{x-1}$ ?", [
    (r"$[1,x]$", quo_is(log(x), 1, a_, log(a_)/(a_ - 1))),
    (r"$[0,x]$", sp.limit(log(x), x, 0, '+') != -oo),
    (r"$[0,1]$", sp.limit(log(x), x, 0, '+') != -oo),
    (r"$[x,2x]$", quo_is(log(x), a_, 2*a_, log(a_)/(a_ - 1))),
], r"‏$\ln1=0$, ולכן $\frac{\ln x-\ln1}{x-1}=\frac{\ln x}{x-1}$, והקטע $[1,x]$ נמצא כולו בתחום של $\ln$. ‏$[0,x]$ ו-$[0,1]$ כוללים את $0$ שבו $\ln$ לא מוגדרת. ‏$[x,2x]$ נותן את המנה $\frac{\ln2}{x}$ (השונה מ-$\frac{\ln x}{x-1}$).",
    "ln 1 = 0, ולכן הקצה הוא 1"))

q.append(mcq("C03-Q5", r"להוכחת $e^{\sin^2b}-e^{\sin^2a}\le e(b-a)$ עבור $a<b$ מפעילים את לגרנז' בקטע $[a,b]$. איזו $f$ נותנת את ההפרש בדיוק ?", [
    (r"$f(t)=e^{\sin^2t}$", True),
    (r"$f(t)=e^{t}$", False),
    (r"$f(t)=\sin^2t$", False),
    (r"$f(t)=e^{\sin t}$", False),
], r"‏$f(b)-f(a)$ צריך להיות $e^{\sin^2b}-e^{\sin^2a}$, ולכן $f(t)=e^{\sin^2t}$. ‏$f(t)=e^t$ נותנת $e^b-e^a$, ‏$f(t)=\sin^2t$ נותנת $\sin^2b-\sin^2a$, ו-$f(t)=e^{\sin t}$ נותנת $e^{\sin b}-e^{\sin a}$. הפונקציה $e^{\sin^2t}$ מוגדרת וגזירה בכל הישר, ולכן כל קטע $[a,b]$ מתאים.",
    "f(b) − f(a) צריך להתלכד עם ההפרש הנתון"))
fp = lambda f, v, w: float((f.subs(x, w) - f.subs(x, v)))
assert abs(fp(exp(sp.sin(x)**2), 0.3, 1.1) - (np.exp(np.sin(1.1)**2) - np.exp(np.sin(0.3)**2))) < 1e-9
assert abs(fp(exp(sp.sin(x)**2), 0.3, 1.1) - fp(exp(x), 0.3, 1.1)) > 0.1
assert abs(fp(exp(sp.sin(x)**2), 0.3, 1.1) - fp(sp.sin(x)**2, 0.3, 1.1)) > 0.1
assert abs(fp(exp(sp.sin(x)**2), 0.3, 1.1) - fp(exp(sp.sin(x)), 0.3, 1.1)) > 0.01

q.append(numeric("C03-Q6", r"עבור $f(t)=\arcsin t$ בקטע $[0,a]$, כמה שווה $f'\left(\frac35\right)$ ? (עשרוני)",
                 1.25, sp.diff(sp.asin(x), x).subs(x, R(3, 5)), r"‏$f'(t)=\frac{1}{\sqrt{1-t^2}}$, ולכן $f'\left(\frac35\right)=\frac{1}{\sqrt{1-\frac9{25}}}=\frac{1}{\frac45}=\frac54=1.25$.",
                 "הנגזרת של arcsin היא 1/√(1−t²)"))
level("C03", 3, "🎯", "בחירת הפונקציה והקטע",
      "לבחור פונקציה וקטע כך שהמנה של לגרנז' תהיה הביטוי שבאמצע האי-שוויון, ושהתנאים יתקיימו.",
      L3, q)

# ===================================================================== C04  two free endpoints
L4 = r"""
<p>לפעמים שני הקצוות חופשיים, $0<a<b$, ולא רק $[0,x]$. הדרך זהה, אבל צריך להחליט איזה קצה נותן איזה חסם.</p>
<div class="lesson-rule">🔑 $f'$ עולה: החסם התחתון הוא $f'(a)$ והעליון $f'(b)$. ‏$f'$ יורדת: להפך, התחתון $f'(b)$ והעליון $f'(a)$.</div>
<div class="lesson-ex">דוגמה: $f=\ln t$ בקטע $[a,b]$. ‏$\frac{\ln b-\ln a}{b-a}=\frac1c$ עם $a<c<b$. ‏$\frac1t$ יורדת, ולכן $\frac1b<\frac1c<\frac1a$.<br>
מכפילים ב-$b-a>0$: $\frac{b-a}{b}<\ln b-\ln a<\frac{b-a}{a}$.</div>
<p>עבור $f=\arcsin t$ ו-$0<a<b<1$ הנגזרת $\frac{1}{\sqrt{1-t^2}}$ עולה, ולכן $\frac{1}{\sqrt{1-a^2}}<f'(c)<\frac{1}{\sqrt{1-b^2}}$.</p>
<div class="lesson-trap">⚠️ כשעוברים להציב מספרים, מציבים את הקצה הנכון בכל חסם. אם הקצוות מוחלפים, הסדר מתהפך והאי-שוויון שגוי.</div>
"""
fact("lesson C04: ln b - ln a bounds", forall2(lambda A, B: ((B - A)/B < np.log(B) - np.log(A)) & (np.log(B) - np.log(A) < (B - A)/A), 0.001, 50))
q = []
q.append(mcq("C04-Q1", r"$f(t)=\ln t$, ו-$0<a<c<b$. בין אילו ערכים נמצא $f'(c)=\frac1c$ ?", [
    (r"$\frac1b<\frac1c<\frac1a$", forall2(lambda A, B: (1/B < 1/((A + B)/2)) & (1/((A + B)/2) < 1/A), 0.001, 50)),
    (r"$\frac1a<\frac1c<\frac1b$", False),
    (r"$a<\frac1c<b$", False),
    (r"$\frac1c<\frac1b$", False),
], r"‏$\frac1t$ יורדת. ‏$c$ גדולה מ-$a$ וקטנה מ-$b$, ולכן $\frac1c$ קטן מ-$\frac1a$ וגדול מ-$\frac1b$. הסדר $\frac1a<\frac1c<\frac1b$ הוא של פונקציה עולה. בבדיקה ב-$a=1,\ b=2,\ c=1.5$: ‏$\frac1c=0.67$, בין $0.5=\frac1b$ ל-$1=\frac1a$. האפשרויות $a<\frac1c<b$ ו-$\frac1c<\frac1b$ נכשלות באותה בדיקה.",
    "1/t יורדת: הקצה הימני נותן את החסם התחתון"))

q.append(mcq("C04-Q2", r"מה מתקבל מהכפלת $\frac1b<\frac{\ln b-\ln a}{b-a}<\frac1a$ ב-$b-a>0$ ?", [
    (r"$\frac{b-a}{b}<\ln b-\ln a<\frac{b-a}{a}$", forall2(lambda A, B: ((B - A)/B < np.log(B) - np.log(A)) & (np.log(B) - np.log(A) < (B - A)/A), 0.001, 50)),
    (r"$\frac{b-a}{a}<\ln b-\ln a<\frac{b-a}{b}$", forall2(lambda A, B: ((B - A)/A < np.log(B) - np.log(A)) & (np.log(B) - np.log(A) < (B - A)/B), 0.001, 50)),
    (r"$\frac{1}{b}<\ln b-\ln a<\frac1a$", forall2(lambda A, B: (1/B < np.log(B) - np.log(A)) & (np.log(B) - np.log(A) < 1/A), 0.001, 50)),
    (r"$b(b-a)<\ln b-\ln a<a(b-a)$", forall2(lambda A, B: (B*(B - A) < np.log(B) - np.log(A)) & (np.log(B) - np.log(A) < A*(B - A)), 0.001, 50)),
], r"מכפילים כל אגף ב-$b-a$: ‏$\frac1b(b-a)=\frac{b-a}{b}$ ו-$\frac1a(b-a)=\frac{b-a}{a}$, והאמצע הופך ל-$\ln b-\ln a$. הסדר ההפוך נכשל ב-$a=1,\ b=2$: ‏$1<0.69$ אינו נכון. האפשרות בלי הכפלה ב-$b-a$ נכשלת ב-$a=1,\ b=3$: ‏$\ln3\approx1.10$ אינו קטן מ-$\frac1a=1$. והאפשרות עם $b(b-a)$ נכשלת ב-$a=1,\ b=2$: ‏$2<0.69$ שקר.",
    "הכפל ב-(b−a) מעביר את b−a לשני האגפים החיצוניים"))

q.append(mcq("C04-Q3", r"$f(t)=\arcsin t$ ו-$0<a<c<b<1$. בין אילו ערכים נמצא $f'(c)$ ?", [
    (r"$\frac{1}{\sqrt{1-a^2}}<f'(c)<\frac{1}{\sqrt{1-b^2}}$", forall2(lambda A, B: (1/np.sqrt(1 - A**2) < 1/np.sqrt(1 - ((A + B)/2)**2)) & (1/np.sqrt(1 - ((A + B)/2)**2) < 1/np.sqrt(1 - B**2)), 0, 1)),
    (r"$\frac{1}{\sqrt{1-b^2}}<f'(c)<\frac{1}{\sqrt{1-a^2}}$", False),
    (r"$a<f'(c)<b$", False),
    (r"$0<f'(c)<\frac{1}{\sqrt{1-a^2}}$", False),
], r"‏$\frac{1}{\sqrt{1-t^2}}$ עולה ב-$(0,1)$, ולכן החסם התחתון בא מ-$a$ והעליון מ-$b$. הסדר ההפוך הוא של פונקציה יורדת. הערך $f'(c)$ גדול מ-$1$ ולכן אינו בין $a$ ל-$b$. האפשרות האחרונה נכשלת ב-$a=0.5,\ c=0.8$: ‏$f'(c)=1.67$ גדול מ-$\frac{1}{\sqrt{1-0.25}}=1.155$.",
    "arcsin' עולה: התחתון מ-a והעליון מ-b"))
fact("C04-Q3 arcsin'' > 0 on (0,1)", sgn(sp.diff(sp.asin(x), x, 2), 0, 1) == 1)
assert 1/np.sqrt(1 - 0.8**2) > 1/np.sqrt(1 - 0.25)

q.append(numeric("C04-Q4", r"מהאי-שוויון $\frac{b-a}{b}<\ln b-\ln a<\frac{b-a}{a}$ עם $a=2,\ b=3$ מקבלים חסם עליון על $\ln\frac32$. מהו ? (עשרוני)",
                 0.5, R(3 - 2, 2), r"החסם העליון הוא $\frac{b-a}{a}=\frac{1}{2}=0.5$, והתחתון $\frac{b-a}{b}=\frac13$. בפועל $\ln1.5\approx0.405$, בין השניים.",
                 "העליון הוא (b−a)/a: מחלקים בקצה השמאלי"))
fact("C04-Q4 ln1.5 between 1/3 and 1/2", 1/3 < float(log(R(3, 2))) < 0.5)

lb = (R(6, 10) - R(5, 10)) / sqrt(1 - R(5, 10)**2)
q.append(numeric("C04-Q5", r"מהחסם $\arcsin b-\arcsin a>\frac{b-a}{\sqrt{1-a^2}}$ עם $a=0.5,\ b=0.6$ מקבלים חסם תחתון על $\arcsin0.6-\arcsin0.5$. מהו ? (עשרוני)",
                 0.1155, lb, r"הצבה: $\frac{0.1}{\sqrt{1-0.25}}=\frac{0.1}{0.8660}\approx0.1155$. בפועל ההפרש הוא $\arcsin0.6-\arcsin0.5\approx0.1199$, גדול מהחסם התחתון וקטן מהעליון $\frac{0.1}{\sqrt{1-0.36}}=0.125$.",
                 "החסם התחתון משתמש ב-a, הקצה הקטן", tol=0.0005))
fact("C04-Q5 true difference between bounds", float(lb) < float(sp.asin(R(6, 10)) - sp.asin(R(1, 2))) < 0.125)

q.append(mcq("C04-Q6", r"$f(t)=\sqrt t$ ו-$0<a<b$. מה מתקבל מלגרנז' ? (רמז: ‏$f'(t)=\frac{1}{2\sqrt t}$ יורדת)", [
    (r"$\frac{b-a}{2\sqrt b}<\sqrt b-\sqrt a<\frac{b-a}{2\sqrt a}$", forall2(lambda A, B: ((B - A)/(2*np.sqrt(B)) < np.sqrt(B) - np.sqrt(A)) & (np.sqrt(B) - np.sqrt(A) < (B - A)/(2*np.sqrt(A))), 0.001, 50)),
    (r"$\frac{b-a}{2\sqrt a}<\sqrt b-\sqrt a<\frac{b-a}{2\sqrt b}$", forall2(lambda A, B: ((B - A)/(2*np.sqrt(A)) < np.sqrt(B) - np.sqrt(A)) & (np.sqrt(B) - np.sqrt(A) < (B - A)/(2*np.sqrt(B))), 0.001, 50)),
    (r"$\frac{b-a}{2b}<\sqrt b-\sqrt a<\frac{b-a}{2a}$", forall2(lambda A, B: ((B - A)/(2*B) < np.sqrt(B) - np.sqrt(A)) & (np.sqrt(B) - np.sqrt(A) < (B - A)/(2*A)), 0.001, 50)),
    (r"$\frac{1}{2\sqrt b}<\sqrt b-\sqrt a<\frac{1}{2\sqrt a}$", forall2(lambda A, B: (1/(2*np.sqrt(B)) < np.sqrt(B) - np.sqrt(A)) & (np.sqrt(B) - np.sqrt(A) < 1/(2*np.sqrt(A))), 0.001, 50)),
], r"הנגזרת יורדת, לכן $\frac{1}{2\sqrt b}<f'(c)<\frac{1}{2\sqrt a}$, ואחרי הכפלה ב-$b-a$ מקבלים את האפשרות הנכונה. הסדר ההפוך הוא של פונקציה עולה. האפשרות עם $2b$ ו-$2a$ שוכחת את השורש: ב-$a=1,\ b=100$ היא נותנת $0.495<9<49.5$, שקר. והאפשרות האחרונה שוכחת להכפיל ב-$b-a$ ונכשלת באותה נקודה ($0.05<9<0.5$ שקר).",
    "לפני שמציבים: האם הנגזרת עולה או יורדת ?"))
level("C04", 4, "↔️", "שני קצוות חופשיים: a ו-b",
      "להפעיל לגרנז' בקטע $[a,b]$ כללי, ולהחליט איזה קצה נותן את החסם התחתון ואיזה את העליון.",
      L4, q)

# ===================================================================== C05  bounding |f'| (Lipschitz inequalities)
L5 = r"""
<p>בשאלות מהצורה $|f(b)-f(a)|\le M|b-a|$ אין צורך בחסם דק על $c$. מספיק <b>חסם אחד על $|f'|$ בכל התחום</b>.</p>
<div class="lesson-formula">אם $|f'(t)|\le M$ לכל $t$ ב-$[a,b]$, אז $|f(b)-f(a)|=|f'(c)|\,|b-a|\le M|b-a|$</div>
<p>איך מוצאים $M$:</p>
<ul>
<li>מגדירים את $f'$ ושואלים כמה היא יכולה להיות בערך מוחלט.</li>
<li>$|\sin|\le1$, ‏$|\cos|\le1$, ‏$\frac{1}{1+t^2}\le1$, ‏$e^{\sin^2t}\le e$, כי $\sin^2t\le1$.</li>
<li>הקבוע הקטן ביותר שעובד הוא $\sup|f'|$.</li>
</ul>
<div class="lesson-ex">דוגמה: $f(t)=\sin t$. ‏$f'=\cos t$ ו-$|\cos t|\le1$ לכל $t$, ולכן $|\sin b-\sin a|\le|b-a|$ לכל $a,b$.</div>
<div class="lesson-trap">⚠️ אם $f'$ לא חסומה בתחום, אין $M$ כזה. ב-$f=t^2$ מתקבל $f'=2t$, שגדלה בלי גבול.</div>
"""
q = []
tt = sp.Symbol('tt', real=True)
fs = sp.sin(2*x)
M1 = sp.Abs(sp.diff(fs, x)).subs(x, 0)
assert forall(lambda v: np.abs(2*np.cos(2*v)) <= 2 + 1e-12, -60, 60)
q.append(numeric("C05-Q1", r"מהו הקבוע $M$ הקטן ביותר שעבורו $|\sin2b-\sin2a|\le M|b-a|$ לכל $a,b$ ?",
                 2, M1, r"‏$f(t)=\sin2t$ ולכן $f'(t)=2\cos2t$ ו-$|f'|\le2$, עם שוויון ב-$t=0$. לכן $M=2$ מספיק. אי אפשר פחות: עבור $a=0$ ו-$b$ קטן, $\sin2b\approx2b$, ולכן $M<2$ היה נכשל.",
                 "M הוא הערך המקסימלי של |f'|"))
assert M1 == 2

M2 = sp.Abs(sp.diff(sp.atan(x), x)).subs(x, 0)
assert forall(lambda v: 1/(1 + v**2) <= 1 + 1e-12, -60, 60)
q.append(numeric("C05-Q2", r"מהו הקבוע $M$ הקטן ביותר שעבורו $|\arctan b-\arctan a|\le M|b-a|$ לכל $a,b$ ?",
                 1, M2, r"‏$f'(t)=\frac{1}{1+t^2}$ חיובית וקטנה או שווה ל-$1$, עם שוויון ב-$t=0$. לכן $M=1$. ל-$M<1$ אין מספיק: עבור $a=0$ ו-$b$ קטן, $\arctan b\approx b$.",
                 "arctan' = 1/(1+t²) ≤ 1"))
assert M2 == 1

q.append(mcq("C05-Q3", r"האם קיים קבוע $M$ כך ש-$|b^2-a^2|\le M|b-a|$ לכל $a,b\in\mathbb R$ ?", [
    (r"לא, כי $f'(t)=2t$ אינה חסומה", all(sp.Abs((M + 1)**2 - M**2) > M*1 for M in range(1, 40))),
    (r"כן, $M=1$", forall(lambda v: np.abs((v + 1)**2 - v**2) <= 1, -50, 50)),
    (r"כן, $M=2$", forall(lambda v: np.abs((v + 1)**2 - v**2) <= 2, -50, 50)),
    (r"כן, $M=4$", forall(lambda v: np.abs((v + 1)**2 - v**2) <= 4, -50, 50)),
], r"‏$|b^2-a^2|=|b+a|\,|b-a|$, והגורם $|a+b|$ אינו חסום. לכל $M$ אפשר לקחת $a=M$ ו-$b=M+1$: ‏$|b^2-a^2|=2M+1>M=M|b-a|$. לכן אין קבוע, והערכים $M=1,2,4$ נכשלים כבר ב-$a=10,b=11$ ($21$ מול $1,2,4$).",
    "f' לא חסומה ← אין קבוע M"))

q.append(mcq("C05-Q4", r"עבור $f(t)=e^{\sin^2t}$ מתקבל $f'(t)=e^{\sin^2t}\sin2t$. מהחסמים $e^{\sin^2t}\le e$ ו-$|\sin2t|\le1$ מסיקים אי-שוויון מהצורה $|f(b)-f(a)|\le M|b-a|$. איזה ערך של $M$ מתקיים לכל $a,b$ ?", [
    (r"$M=e$", forall2(lambda A, B: np.abs(np.exp(np.sin(B)**2) - np.exp(np.sin(A)**2)) <= np.e*(B - A), -20, 20)),
    (r"$M=\frac e2$", forall2(lambda A, B: np.abs(np.exp(np.sin(B)**2) - np.exp(np.sin(A)**2)) <= np.e/2*(B - A), -20, 20)),
    (r"$M=1$", forall2(lambda A, B: np.abs(np.exp(np.sin(B)**2) - np.exp(np.sin(A)**2)) <= (B - A), -20, 20)),
    (r"$M=\frac32$", forall2(lambda A, B: np.abs(np.exp(np.sin(B)**2) - np.exp(np.sin(A)**2)) <= 1.5*(B - A), -20, 20)),
], r"‏$|f'(t)|=e^{\sin^2t}\,|\sin2t|\le e\cdot1=e$, ולכן $|f(b)-f(a)|\le e|b-a|$ לכל $a,b$. הערכים הקטנים יותר נכשלים: ב-$a=0.9,\ b=1.1$ ההפרש $e^{\sin^21.1}-e^{\sin^20.9}\approx0.37$ ו-$b-a=0.2$, כלומר היחס $\approx1.83$, גדול מ-$1$, מ-$\frac32$ ומ-$\frac e2\approx1.36$.",
    "מכפילים את החסמים של הגורמים ב-f'"))
pa, pb = 0.9, 1.1
assert (np.exp(np.sin(pb)**2) - np.exp(np.sin(pa)**2)) / (pb - pa) > 1.8
fact("C05-Q4 e bound valid, smaller fail", forall2(lambda A, B: np.abs(np.exp(np.sin(B)**2) - np.exp(np.sin(A)**2)) <= np.e*(B - A), -20, 20))
q.append(numeric("C05-Q5", r"מהו הקבוע $M$ הקטן ביותר שעבורו $|\sqrt b-\sqrt a|\le M|b-a|$ לכל $a,b\ge1$ ? (עשרוני)",
                 0.5, sp.limit(sp.diff(sqrt(x), x), x, 1, '+'), r"‏$f'(t)=\frac{1}{2\sqrt t}$ יורדת, ולכן עבור $t\ge1$ היא קטנה מ-$\frac12$ וקרובה ל-$\frac12$ כש-$t$ קרוב ל-$1$. כלומר $M=\frac12$ מספיק, ואי אפשר פחות.",
                 "בקטע t ≥ 1, ‏|f'| ≤ 1/2"))
fact("C05-Q5 sqrt Lipschitz 1/2", forall2(lambda A, B: np.sqrt(B) - np.sqrt(A) <= 0.5*(B - A), 1, 60) and not forall2(lambda A, B: np.sqrt(B) - np.sqrt(A) <= 0.499*(B - A), 1, 1.01, 200))
level("C05", 5, "🧱", "חסם על |f'|: אי-שוויונות מהצורה |f(b)−f(a)| ≤ M|b−a|",
      "למצוא חסם על $|f'|$ בכל התחום ולהסיק ממנו אי-שוויון בין שני ערכים כלשהם של הפונקציה.",
      L5, q)

# ===================================================================== C06  auxiliary function and monotonicity
L6 = r"""
<p>כשאי-שוויון נכון לכל $x>0$ אפשר להוכיח אותו בלי לגרנז'. ממירים אותו לשאלת סימן של פונקציה אחת.</p>
<h3>המתכון</h3>
<ol>
<li>מעבירים אגפים ומגדירים $f$ כאגף הימני פחות אגף השמאלי, כך שצריך להוכיח $f>0$.</li>
<li>מחשבים את $f$ בקצה, בדרך כלל $f(0)=0$.</li>
<li>מראים ש-$f'>0$ בקטע, ולכן $f$ עולה ממש.</li>
<li>מסיקים $f(x)>f(0)=0$.</li>
</ol>
<div class="lesson-ex">דוגמה: $\ln(1+x)<x$ עבור $x>0$. ‏$f(x)=x-\ln(1+x)$ נותנת $f(0)=0$ ו-$f'(x)=1-\frac{1}{1+x}=\frac{x}{1+x}>0$. לכן $f(x)>0$.</div>
<div class="lesson-trap">⚠️ אם $f'$ משנה סימן, $f$ לא מונוטונית בכל הקטע. מוצאים נקודה שבה $f'=0$, בודקים את הסימנים משני הצדדים ומסיקים שהיא מינימום או מקסימום. ב-$e^x\ge x+1$ מגדירים $f(x)=e^x-x-1$ ומקבלים $f'(x)=e^x-1$, שמשנה סימן ב-$0$.</div>
"""
fact("lesson C06: ln(1+x)<x", True)
ineq("ln(1+x) < x on x>0", log(1 + x), x, 0, oo)
fact("lesson C06: f' = x/(1+x)", eq(sp.diff(x - log(1 + x), x), x/(1 + x)))
q = []
Rhs, Lhs = x, log(1 + x)
cands = [x - log(1 + x), log(1 + x) - x, x + log(1 + x), x*log(1 + x)]
q.append(mcq("C06-Q1", r"להוכחת $\ln(1+x)<x$ עבור $x>0$ בוחרים $f$ עם $f(0)=0$, כך ש-$f(x)>0$ הוא בדיוק האי-שוויון הנדרש (אחרי העברת אגפים). איזו ?", [
    (r"$f(x)=x-\ln(1+x)$", eq(cands[0], Rhs - Lhs)),
    (r"$f(x)=\ln(1+x)-x$", eq(cands[1], Rhs - Lhs)),
    (r"$f(x)=x+\ln(1+x)$", eq(cands[2], Rhs - Lhs)),
    (r"$f(x)=x\ln(1+x)$", eq(cands[3], Rhs - Lhs)),
], r"‏$f(x)>0$ צריך להיות $x>\ln(1+x)$, כלומר $f=x-\ln(1+x)$ (ימין פחות שמאל). ‏$\ln(1+x)-x$ מתאימה להפוך, כלומר $f>0$ אומר $\ln(1+x)>x$. ‏$x+\ln(1+x)>0$ נכון אך לא מתייחס לטענה, וגם $x\ln(1+x)>0$ אומר רק ש-$\ln(1+x)>0$.",
    "f = ימין − שמאל, ואז צריך להוכיח f > 0"))
assert all(abs(float(g.subs(x, 0))) < 1e-12 for g in cands)

q.append(numeric("C06-Q2", r"להוכחת $\arctan x<x$ עבור $x>0$ מגדירים $f(x)=x-\arctan x$. מהו $f'(1)$ ? (עשרוני)",
                 0.5, sp.diff(x - sp.atan(x), x).subs(x, 1), r"‏$f'(x)=1-\frac{1}{1+x^2}=\frac{x^2}{1+x^2}$, ולכן $f'(1)=\frac12=0.5$. הנגזרת חיובית לכל $x>0$, ולכן $f$ עולה, ו-$f(0)=0$ נותן $f(x)>0$.",
                 "f' = x²/(1+x²) > 0"))
ineq("arctan x < x on x>0", sp.atan(x), x, 0, oo)
assert eq(sp.diff(x - sp.atan(x), x), x**2/(1 + x**2))

g6 = sp.atan(x) - x/(1 + x**2)
q.append(mcq("C06-Q3", r"להוכחת $\arctan x>\frac{x}{1+x^2}$ עבור $x>0$ מגדירים $f(x)=\arctan x-\frac{x}{1+x^2}$. מהי $f'(x)$ ?", [
    (r"$\frac{2x^2}{\left(1+x^2\right)^2}$", eq(sp.diff(g6, x), 2*x**2/(1 + x**2)**2)),
    (r"$-\frac{2x^2}{\left(1+x^2\right)^2}$", eq(sp.diff(g6, x), -2*x**2/(1 + x**2)**2)),
    (r"$\frac{1}{1+x^2}-\frac{1}{\left(1+x^2\right)^2}$", eq(sp.diff(g6, x), 1/(1 + x**2) - 1/(1 + x**2)**2)),
    (r"$0$", eq(sp.diff(g6, x), 0)),
], r"נגזרת המנה: $\left(\frac{x}{1+x^2}\right)'=\frac{(1+x^2)-2x^2}{(1+x^2)^2}=\frac{1-x^2}{(1+x^2)^2}$. אז $f'=\frac{1}{1+x^2}-\frac{1-x^2}{(1+x^2)^2}=\frac{(1+x^2)-(1-x^2)}{(1+x^2)^2}=\frac{2x^2}{(1+x^2)^2}>0$. הסימן השלילי נובע מטעות בסימן של נגזרת המנה, האפשרות השלישית שוכחת את הגורם $1-x^2$ במונה, ו-$0$ שגוי כי $f$ לא קבועה.",
    "נגזרת של מנה, ואז סימן חיובי ← f עולה"))
ineq("arctan x > x/(1+x^2) on x>0", x/(1 + x**2), sp.atan(x), 0, oo)
assert g6.subs(x, 0) == 0

q.append({"id": "C06-Q4", "step": {"type": "findbug", "prompt": "בהוכחת $\\arctan x<x$ עבור $x>0$ נפלה טעות בשורה אחת. איזו ?",
          "lines": [r"נגדיר $f(x)=x-\arctan x$. מתקיים $f(0)=0$",
                    r"$f'(x)=1-\frac{1}{1+x^2}=\frac{x^2}{1+x^2}$",
                    r"לכל $x>0$ מתקיים $f'(x)<0$, ולכן $f$ עולה",
                    r"לכן $f(x)>f(0)=0$, כלומר $x>\arctan x$"],
          "bugIndex": 2,
          "explain": r"‏$\frac{x^2}{1+x^2}$ חיובית לכל $x\neq0$, ולכן $f'(x)>0$ ואז $f$ עולה. נגזרת שלילית הייתה אומרת ש-$f$ יורדת, וזה לא מתיישב עם המסקנה. שאר השורות נכונות."},
     "recap": "f' חיובית ← f עולה; סימן שלילי ← יורדת"})
assert sgn(x**2/(1 + x**2), 0, oo) == 1

fg = exp(x) - x - 1
q.append(mcq("C06-Q5", r"להוכחת $e^x\ge x+1$ לכל $x$ ממשי מגדירים $f(x)=e^x-x-1$. מה נכון ?", [
    (r"‏$f'<0$ ב-$(-\infty,0)$ ו-$f'>0$ ב-$(0,\infty)$, ולכן $f(0)=0$ הוא המינימום ו-$f\ge0$", sgn(sp.diff(fg, x), -oo, 0) == -1 and sgn(sp.diff(fg, x), 0, oo) == 1 and fg.subs(x, 0) == 0),
    (r"‏$f$ עולה ממש בכל הישר, ולכן $f\ge0$", sgn(sp.diff(fg, x), -oo, 0) == 1),
    (r"‏$f'(x)>0$ לכל $x$", sgn(sp.diff(fg, x), -oo, 0) == 1),
    (r"‏$f(x)\le0$ לכל $x$", forall(lambda v: np.exp(v) - v - 1 <= 0, -50, 50)),
], r"‏$f'(x)=e^x-1$ מתאפסת רק ב-$x=0$, שלילית משמאלו וחיובית מימינו. ‏$f$ יורדת ואז עולה, ולכן הערך המינימלי הוא $f(0)=0$ וכל הערכים אחרים אי-שליליים. ‏$f$ לא עולה בכל הישר: ‏$f'(-1)=e^{-1}-1<0$ ו-$f(-1)=e^{-1}>f(0)=0$. והטענה $f\le0$ שגויה כי $f(1)=e-2>0$.",
    "f' משנה סימן: מצאו מינימום, לא מונוטוניות"))
ineq("e^x >= x+1 on R", x + 1, exp(x), -oo, oo, strict=False)
level("C06", 6, "🧪", "פונקציית עזר ומונוטוניות",
      "להפוך אי-שוויון לשאלה על סימן של פונקציית עזר, ולהכריע בין מונוטוניות לקיצון.",
      L6, q)

# ===================================================================== C07  Rolle and roots
L7 = r"""
<p>רול עונה על שאלות מהסוג "הוכיחו שלמשוואה יש פתרון" ו"כמה פתרונות יש".</p>
<h3>לקיים שורש</h3>
<p>רוצים להוכיח של-$g(x)=0$ יש פתרון ב-$(a,b)$. מוצאים פונקציה $F$ כך ש-$F'=g$ ו-$F(a)=F(b)$. אז לפי רול יש $c$ עם $F'(c)=g(c)=0$.</p>
<h3>לספור שורשים</h3>
<ul>
<li>בין שני שורשים של $f$ יש שורש של $f'$ (רול).</li>
<li>לכן אם $f'$ בעלת $k$ שורשים לכל היותר, ל-$f$ יש לכל היותר $k+1$ שורשים.</li>
<li>אם $f'$ בלי שורשים, ל-$f$ שורש אחד לכל היותר.</li>
<li>כדי להראות שיש <b>לפחות</b> שורש אחד, משתמשים במשפט ערך הביניים: ‏$f$ רציפה ו-$f(a)<0<f(b)$ נותנים שורש ב-$(a,b)$.</li>
</ul>
<div class="lesson-ex">דוגמה: ל-$x^3+x-1$ יש שורש אחד בדיוק. ‏$f(0)=-1<0<1=f(1)$ נותן שורש. ‏$f'=3x^2+1>0$, ולכן לא יותר מאחד.</div>
<div class="lesson-trap">⚠️ מ-$f'$ בעלת שני שורשים לא נובע שלפונקציה יש שלושה שורשים, אלא לכל היותר שלושה. את המספר המדויק מחשבים בעזרת ערכי $f$ בנקודות.</div>
"""
q = []
Fc = [x**6 - 2*x**2 + x, x**6 - 2*x**2, x**6 - 4*x**2 + x, 6*x**5 - 4*x + 1]
gg = 6*x**5 - 4*x + 1
q.append(mcq("C07-Q1", r"להוכחת של-$6x^5-4x+1=0$ יש פתרון ב-$(0,1)$ מחפשים $F$ עם $F'(x)=6x^5-4x+1$ ו-$F(0)=F(1)$. איזו ?", [
    (r"$F(x)=x^6-2x^2+x$", eq(sp.diff(Fc[0], x), gg) and Fc[0].subs(x, 0) == Fc[0].subs(x, 1)),
    (r"$F(x)=x^6-2x^2$", eq(sp.diff(Fc[1], x), gg) and Fc[1].subs(x, 0) == Fc[1].subs(x, 1)),
    (r"$F(x)=x^6-4x^2+x$", eq(sp.diff(Fc[2], x), gg) and Fc[2].subs(x, 0) == Fc[2].subs(x, 1)),
    (r"$F(x)=6x^5-4x+1$", eq(sp.diff(Fc[3], x), gg) and Fc[3].subs(x, 0) == Fc[3].subs(x, 1)),
], r"‏$F(x)=x^6-2x^2+x$ מקיימת $F'=6x^5-4x+1$, ו-$F(0)=0=F(1)$. ‏$x^6-2x^2$ נותנת נגזרת $6x^5-4x$ (בלי $+1$). ‏$x^6-4x^2+x$ נותנת $6x^5-8x+1$. ‏$g$ עצמה לא מקיימת $F'=g$ ($g(0)=1\neq g(1)=3$). לכן לפי רול קיימת $c\in(0,1)$ עם $F'(c)=0$.",
    "מחפשים הפונקציה הקדומה שמקבלת ערכים שווים בקצוות"))

q.append(numeric("C07-Q2", r"כמה פתרונות ממשיים יש למשוואה $x^3+3x+1=0$ ?", 1, len(sp.real_roots(x**3 + 3*x + 1)),
                 r"‏$f'(x)=3x^2+3>0$, ולכן $f$ עולה ממש ויש לה לכל היותר שורש אחד. ‏$f(-1)=-3<0<1=f(0)$, ולכן לפי משפט ערך הביניים יש שורש. בסך הכול בדיוק אחד.",
                 "f' ללא שורשים: לכל היותר שורש אחד; עם החלפת סימן: בדיוק אחד"))
assert sgn(3*x**2 + 3, -oo, oo) == 1 and (x**3 + 3*x + 1).subs(x, -1) < 0 < (x**3 + 3*x + 1).subs(x, 0)

h3 = x**3 - 3*x + 1
q.append(numeric("C07-Q3", r"כמה פתרונות ממשיים יש למשוואה $x^3-3x+1=0$ ? (רמז: ‏$f'(x)=3x^2-3$ מתאפסת ב-$\pm1$, ו-$f(-2)=-1,\ f(-1)=3,\ f(1)=-1,\ f(2)=3$)",
                 3, len(sp.real_roots(h3)),
                 r"‏$f'$ בעלת שני שורשים, ולכן ל-$f$ יש לכל היותר $3$. ‏$f$ מחליפה סימן בין $-2$ ל-$-1$ (מ-$-1$ ל-$3$), בין $-1$ ל-$1$ (מ-$3$ ל-$-1$) ובין $1$ ל-$2$ (מ-$-1$ ל-$3$). זה נותן שלושה שורשים לפחות, ולכן בדיוק $3$.",
                 "שני שורשים לנגזרת ← עד 3 שורשים; בודקים סימנים כדי לאשר"))
assert [h3.subs(x, v) for v in (-2, -1, 1, 2)] == [-1, 3, -1, 3]

q.append({"id": "C07-Q4", "step": {"type": "order", "prompt": "סדרו את ההוכחה ש-$f(x)=x^3+x-1$ מתאפסת בדיוק פעם אחת.",
          "lines": [r"$f$ רציפה, ו-$f(0)=-1<0$ וגם $f(1)=1>0$",
                    r"לפי משפט ערך הביניים קיים שורש $r\in(0,1)$",
                    r"נניח בשלילה ש-$s\neq r$ הוא שורש נוסף. לפי רול קיימת $c$ בין $r$ ל-$s$ עם $f'(c)=0$",
                    r"אבל $f'(x)=3x^2+1>0$ לכל $x$, וזו סתירה",
                    r"לכן השורש $r$ יחיד"],
          "explain": r"כל שורה נשענת על הקודמת: קודם מוצאים שורש, אחר כך מניחים שורש שני, אחר כך מקבלים נקודה $c$, ואז מגיעים לסתירה, ורק אז מסיקים יחידות."},
     "recap": "קיום מערך הביניים, יחידות מרול וסתירה"})
fx7 = x**3 + x - 1
assert fx7.subs(x, 0) == -1 and fx7.subs(x, 1) == 1 and sgn(sp.diff(fx7, x), -oo, oo) == 1 and len(sp.real_roots(fx7)) == 1

pol5 = x*(x - 1)*(x - 2)*(x - 3)*(x - 4)
q.append(numeric("C07-Q5", r"לפונקציה גזירה $f$ יש $5$ שורשים ממשיים שונים. כמה שורשים ל-$f'$ מובטחים בהכרח לפחות ?",
                 4, len(sp.real_roots(sp.Poly(sp.diff(pol5, x), x))),
                 r"בין כל שני שורשים עוקבים של $f$ רול נותן שורש של $f'$. יש $4$ זוגות עוקבים, ולכן $f'$ בעלת $4$ שורשים לפחות. אי אפשר להבטיח יותר: ל-$f(x)=x(x-1)(x-2)(x-3)(x-4)$ יש בדיוק $4$ שורשים בנגזרת, כי היא פולינום ממעלה $4$.",
                 "n שורשים ל-f ← לפחות n−1 שורשים ל-f'"))
level("C07", 7, "🌱", "רול ושורשים",
      "להשתמש ברול כדי להוכיח שלמשוואה יש פתרון ולספור כמה פתרונות יש לה.",
      L7, q)

# ===================================================================== C08  assemble and debug a proof
L8 = r"""
<p>הוכחה מלאה של אי-שוויון עם לגרנז' כוללת תמיד אותם חמישה חלקים, בסדר הזה:</p>
<ol>
<li><b>הגדרה:</b> איזו $f$ ואיזה קטע.</li>
<li><b>תנאים:</b> רציפה בקטע הסגור וגזירה בקטע הפתוח.</li>
<li><b>המשפט:</b> קיימת $c$ בקטע הפתוח כך ש-$\frac{f(b)-f(a)}{b-a}=f'(c)$.</li>
<li><b>חסימת $c$:</b> מ-$a<c<b$ חוסמים את $f'(c)$.</li>
<li><b>מסקנה:</b> מכפילים ב-$b-a$ ומקבלים את האי-שוויון.</li>
</ol>
<div class="lesson-ex">דוגמה: $\ln(1+x)<x$. ‏$f=\ln(1+t)$ ב-$[0,x]$, קיימת $c\in(0,x)$ עם $\frac{\ln(1+x)}{x}=\frac{1}{1+c}$. מ-$c>0$ נובע $\frac{1}{1+c}<1$, ולכן $\ln(1+x)<x$.</div>
<div class="lesson-trap">⚠️ שגיאות נפוצות: להמיר את כיוון האי-שוויון אחרי היפוך, לבחור קטע שמכיל נקודה שבה הפונקציה לא מוגדרת, ולדלג על בדיקת התנאים.</div>
"""
q = []
q.append({"id": "C08-Q1", "step": {"type": "order", "prompt": "סדרו את ההוכחה ש-$\\ln(1+x)>\\frac{x}{1+x}$ עבור $x>0$.",
          "lines": [r"נגדיר $f(t)=\ln(1+t)$ בקטע $[0,x]$. היא רציפה בקטע וגזירה בקטע הפתוח $(0,x)$",
                    r"לפי לגרנז' קיימת $c\in(0,x)$ כך ש-$\frac{\ln(1+x)-\ln1}{x}=\frac{1}{1+c}$",
                    r"מכיוון ש-$0<c<x$ מתקיים $1+c<1+x$, ולכן $\frac{1}{1+c}>\frac{1}{1+x}$",
                    r"לכן $\frac{\ln(1+x)}{x}>\frac{1}{1+x}$, ומכפילים ב-$x>0$: $\ln(1+x)>\frac{x}{1+x}$"],
          "explain": r"קודם מגדירים ובודקים תנאים, אחר כך מפעילים את המשפט, ואחר כך חוסמים את $c$ (שורה שמשתמשת ב-$c$ מהמשפט), ובסוף מסיקים."},
     "recap": "הגדרה ← תנאים ← משפט ← חסימה ← מסקנה"})
ineq("ln(1+x) > x/(1+x)", x/(1 + x), log(1 + x), 0, oo)

q.append({"id": "C08-Q2", "step": {"type": "findbug", "prompt": "בהוכחת $\\arcsin a>a$ עבור $0<a<1$ נפלה טעות בשורה אחת. איזו ?",
          "lines": [r"נגדיר $f(t)=\arcsin t$. היא רציפה ב-$[0,a]$ וגזירה ב-$(0,a)$",
                    r"לפי לגרנז' קיימת $c\in(0,a)$ כך ש-$\frac{\arcsin a}{a}=\frac{1}{\sqrt{1-c^2}}$",
                    r"מכיוון ש-$0<c<1$ מתקיים $0<1-c^2<1$, ולכן $\frac{1}{\sqrt{1-c^2}}<1$",
                    r"לכן $\frac{\arcsin a}{a}>1$, ומכפילים ב-$a>0$: $\arcsin a>a$"],
          "bugIndex": 2,
          "explain": r"מ-$0<1-c^2<1$ נובע $\sqrt{1-c^2}<1$, ולכן ההפוך $\frac{1}{\sqrt{1-c^2}}$ **גדול** מ-$1$. הכיוון התהפך אחרי היפוך. השורה הרביעית מתאימה לכיוון הנכון, ושאר השורות נכונות."},
     "recap": "הפיכה של 0<u<1 נותנת 1/u > 1"})
ineq("arcsin a > a", x, sp.asin(x), 0, 1)
assert sgn(1/sqrt(1 - x**2) - 1, 0, 1) == 1

q.append({"id": "C08-Q3", "step": {"type": "findbug", "prompt": "בהוכחת $\\tan x>x$ עבור $0<x<\\frac\\pi2$ נפלה טעות בשורה אחת. איזו ?",
          "lines": [r"נגדיר $f(t)=\tan t$ בקטע $\left[0,\frac\pi2\right]$. היא רציפה וגזירה שם",
                    r"לפי לגרנז' קיימת $c$ כך ש-$\frac{\tan x-\tan0}{x-0}=\frac{1}{\cos^2c}$",
                    r"מכיוון ש-$0<\cos^2c<1$ מתקיים $\frac{1}{\cos^2c}>1$",
                    r"לכן $\frac{\tan x}{x}>1$ ומכפילים ב-$x>0$: $\tan x>x$"],
          "bugIndex": 0,
          "explain": r"‏$\tan$ לא מוגדרת ב-$\frac\pi2$, ולכן אינה רציפה ב-$\left[0,\frac\pi2\right]$ ותנאי המשפט לא מתקיימים. הקטע הנכון הוא $[0,x]$ עם $x<\frac\pi2$. שאר השורות נכונות ביחס לקטע זה."},
     "recap": "בודקים שהקטע לא מכיל את π/2"})
ineq("tan x > x on (0,pi/2)", x, sp.tan(x), 0, sp.pi/2)
fact("C08-Q3 tan undefined at pi/2", sp.limit(sp.tan(x), x, sp.pi/2, '-') == oo)

q.append({"id": "C08-Q4", "step": {"type": "fillblank", "prompt": "משלימים את שלב החסימה בהוכחת $\\ln(1+x)>\\frac{x}{1+x}$.",
          "lines": [r"קיימת $c\in(0,x)$ כך ש-$\frac{\ln(1+x)}{x}=\frac{1}{1+c}$",
                    r"מכיוון ש-$0<c<x$ מתקיים ___"],
          "blankIndex": 1,
          "options": [{"id": "a", "value": r"$\frac{1}{1+x}<\frac{1}{1+c}<1$"},
                      {"id": "b", "value": r"$1<\frac{1}{1+c}<\frac{1}{1+x}$"},
                      {"id": "c", "value": r"$\frac{1}{1+c}>1$"},
                      {"id": "d", "value": r"$\frac{1}{1+c}<\frac{1}{1+x}$"}],
          "correctId": "a",
          "explain": r"‏$\frac{1}{1+t}$ יורדת: מ-$0<c<x$ נובע $1<1+c<1+x$ ולכן $\frac{1}{1+x}<\frac{1}{1+c}<1$. האפשרות השנייה מחליפה את הכיוון, והשלישית והרביעית אינן נכונות ($\frac1{1+c}<1$ ו-$\frac{1}{1+c}>\frac{1}{1+x}$)."},
     "recap": "1/(1+t) יורדת: החסם התחתון מ-x והעליון מ-0"})
cc = np.linspace(0.001, 5, 30)
assert all((1/(1 + cv_) > 1/(1 + 5.01)) and (1/(1 + cv_) < 1) for cv_ in cc)     # (a) for c in (0,5.01)
assert not all(1/(1 + cv_) > 1 for cv_ in cc) and not all(1/(1 + cv_) < 1/(1 + 5.01) for cv_ in cc) and not all(1 < 1/(1 + cv_) for cv_ in cc)

q.append(mcq("C08-Q5", r"בהוכחה מופיע רק: \"נגדיר $f(t)=\ln(1+t)$. לפי לגרנז' קיימת $c\in(0,x)$ עם $\frac{\ln(1+x)}{x}=\frac1{1+c}$\". מה חסר ?", [
    (r"ציון ש-$f$ רציפה ב-$[0,x]$ וגזירה ב-$(0,x)$", True),
    (r"חישוב הערך המדויק של $c$", False),
    (r"אינדוקציה על $x$", False),
    (r"הוכחה ש-$f(0)=1$", sp.log(1 + 0) == 1),
], r"המשפט חל רק כשהפונקציה רציפה בקטע הסגור וגזירה בקטע הפתוח, וצריך לציין זאת (כאן זה נכון כי $1+t>0$ בכל $[0,x]$). אין צורך לחשב את $c$ המדויקת, כי המשפט לא נותן אותה. אין צורך באינדוקציה. והטענה $f(0)=1$ שגויה: ‏$f(0)=\ln1=0$.",
    "תמיד כותבים את תנאי המשפט"))
level("C08", 8, "🧩", "בונים הוכחה: סדר ובאגים",
      "לסדר הוכחה מלאה של אי-שוויון עם לגרנז' ולאתר שורה שגויה בהוכחה.",
      L8, q)

# ===================================================================== C09  boss
L9 = r"""
<p>ארבע הוכחות אי-שוויון אמיתיות מהמבחנים. לפני שמתחילים, שלוש שאלות לעצמכם:</p>
<ul>
<li><b>האם אפשר בקלות לגרנז'?</b> האם אחד הקצוות הוא $0$ או $1$, והאם הביטוי הוא הפרש $f(b)-f(a)$? ‏$\arcsin a$ ו-$\tan x$ הם דוגמאות כאלה.</li>
<li><b>האם מתאים פונקציית עזר?</b> $f$ = ימין פחות שמאל, מחשבים $f(0)$ ובודקים את סימן $f'$. לדוגמה $\ln(1+x)<x$.</li>
<li><b>האם צריך קיצון?</b> אם אי-השוויון נכון לכל $x$ ויש שוויון בנקודה אחת, מחפשים מינימום של $f$.</li>
</ul>
<div class="lesson-rule">🔑 תמיד כתבו את התנאים: רציפה בקטע הסגור, גזירה בקטע הפתוח. אי-שוויון חזק מגיע מכך ש-$c$ בקטע פתוח.</div>
<div class="lesson-trap">⚠️ אחרי היפוך מחליפים כיוון. ואם $f'$ משנה סימן, אין מונוטוניות בכל הקטע.</div>
"""
q = [
    {"bankId": "24B-A-Q2b", "recap": "פונקציית עזר x − ln(1+x): f(0)=0 ו-f' = x/(1+x) > 0"},
    {"bankId": "24B-B-Q6a", "recap": "e^x − x − 1: f' משנה סימן ב-0, מינימום שווה 0 ולכן f ≥ 0"},
    {"bankId": "24A-A-Q6a", "recap": "לגרנז' על tan ב-[0,x]: 1/cos²c > 1"},
    {"bankId": "23B-B-Q4a", "recap": "arcsin על [0,a]: 1 < 1/√(1−c²) < 1/√(1−a²)"},
]
level("C09", 9, "🏆", "מבחן מסכם: הוכחות אי-שוויון מהמבחנים",
      "להוכיח ארבעה אי-שוויונות מהמבחנים, בחירת שיטה מתאימה בכל פעם.",
      L9, q, boss=True)

# sanity on the claims quoted in the boss recaps
ineq("boss 24B-A: ln(1+x)<x", log(1 + x), x, 0, oo)
ineq("boss 24B-B: e^x >= x+1", x + 1, exp(x), -oo, oo, strict=False)
ineq("boss 24A-A: tan x > x", x, sp.tan(x), 0, sp.pi/2)
ineq("boss 23B-B: a < arcsin a", x, sp.asin(x), 0, 1)
ineq("boss 23B-B: arcsin a < a/sqrt(1-a^2)", sp.asin(x), x/sqrt(1 - x**2), 0, 1)
fact("boss 24B-A: f' = x/(1+x)", eq(sp.diff(x - log(1 + x), x), x/(1 + x)))
fact("boss 24A-A: tan' = 1/cos^2", eq(sp.diff(sp.tan(x), x), 1/sp.cos(x)**2))
fact("boss 23B-B: arcsin' = 1/sqrt(1-x^2) and g' = x^2/(1-x^2)^(3/2)",
     eq(sp.diff(sp.asin(x), x), 1/sqrt(1 - x**2)) and eq(sp.diff(x/sqrt(1 - x**2) - sp.asin(x), x), x**2/(1 - x**2)**R(3, 2)))

# ---- extra falsification of the hard-coded distractors (counterexample at the midpoint c of (a,b))
_m = lambda A, B: (A + B) / 2
_d = lambda c: 1/np.sqrt(1 - c**2)
assert not forall2(lambda A, B: (1/np.sqrt(1 - B**2) < _d(_m(A, B))) & (_d(_m(A, B)) < 1), 0, 1)          # C02-Q2 opt2 (with a:=A... reversed)
assert not forall2(lambda A, B: _d(_m(A, B)) < 1, 0, 1)                                                      # C02-Q2 opt3
assert not forall2(lambda A, B: _d(_m(A, B)) > _d(B), 0, 1)                                                  # C02-Q2 opt4
assert not forall2(lambda A, B: (1/A < 1/_m(A, B)) & (1/_m(A, B) < 1/B), 0.01, 50)                          # C04-Q1 opt2
assert not forall2(lambda A, B: (A < 1/_m(A, B)) & (1/_m(A, B) < B), 0.01, 50)                              # C04-Q1 opt3
assert not forall2(lambda A, B: 1/_m(A, B) < 1/B, 0.01, 50)                                                  # C04-Q1 opt4
assert not forall2(lambda A, B: (_d(B) < _d(_m(A, B))) & (_d(_m(A, B)) < _d(A)), 0, 1)                      # C04-Q3 opt2
assert not forall2(lambda A, B: (A < _d(_m(A, B))) & (_d(_m(A, B)) < B), 0, 1)                              # C04-Q3 opt3
assert not forall2(lambda A, B: (0 < _d(_m(A, B))) & (_d(_m(A, B)) < _d(A)), 0, 1)                          # C04-Q3 opt4
FACTS.append("distractor counterexamples for C02-Q2, C04-Q1, C04-Q3")

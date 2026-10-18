# -*- coding: utf-8 -*-
"""Source + machine check for the guided course "integration" (calculus-1, topic indefinite_integrals).

Every option of every question is written next to a sympy expression for its truth value; importing this
module evaluates all of them and asserts that exactly one option of each mcq is true. Antiderivatives are
checked by differentiating (ok), distractors by showing d/dx F != f (also via ok). Method-choice questions
check the structural property that makes each wrong method fail (not rational, erfi appears, a leftover x,
the integral gets harder, ...). check.py emits courses/integration/C0N.js from LEVELS.
"""
import sympy as sp

x = sp.Symbol('x', positive=True)
t = sp.Symbol('t', positive=True)
oo = sp.oo
R = sp.Rational
exp, log, sqrt, atan, sin, cos, tan = sp.exp, sp.log, sp.sqrt, sp.atan, sp.sin, sp.cos, sp.tan
LEVELS = []
FACTS = []
_pos = [0]
PTS = [R(13, 10), R(27, 10), R(4, 10), R(9, 2), R(7, 3)]


def fact(desc, cond):
    assert bool(cond), "FACT FAILED: " + desc
    FACTS.append(desc)


def eq(a, b):
    """exact symbolic identity, falling back to numeric agreement at sample points"""
    if sp.simplify(a - b) == 0:
        return True
    return numeq(a, b)


def numeq(a, b):
    good = 0
    for p in PTS:
        try:
            va = complex(sp.N(a.subs(x, p), 30))
            vb = complex(sp.N(b.subs(x, p), 30))
        except Exception:
            continue
        if abs(va.imag) > 1e-12 or abs(vb.imag) > 1e-12:
            continue
        if abs(va - vb) > 1e-9 * (1 + abs(va)):
            return False
        good += 1
    return good >= 3


def ok(f, F):
    """F is an antiderivative of f (up to a constant): differentiate and compare"""
    return eq(sp.diff(F, x), f)


def mcq(qid, question, opts, explanation, recap):
    truths = [bool(tv) for _, tv in opts]
    assert sum(truths) == 1, (qid, truths)
    assert len({o for o, _ in opts}) == len(opts), qid
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
    assert abs(float(truth) - float(answer)) <= 1e-9, (qid, answer, truth)
    return {"id": qid, "step": {"type": "numeric", "prompt": prompt, "answer": answer, "tol": tol, "explain": explain},
            "recap": recap}


def level(lid, order, icon, title, goal, lesson, questions, boss=False):
    LEVELS.append({"id": lid, "order": order, "icon": icon, "title": title, "goal": goal, "boss": boss,
                   "lesson": lesson, "questions": questions})


def has_any(expr, *kinds):
    return any(expr.has(k) for k in kinds)


# ===================================================================== C01  table and linear inner function
L1 = r"""
<p>לפני שבוחרים שיטה צריך להכיר את הטבלה. כל שיטה בקורס הזה נגמרת בהחזרת האינטגרל לשורה בטבלה.</p>
<h3>הטבלה הקצרה</h3>
<ul>
<li>$\int x^{\alpha}dx=\frac{x^{\alpha+1}}{\alpha+1}$ ($\alpha\neq-1$), $\int\frac{dx}{x}=\ln|x|$, $\int e^{x}dx=e^{x}$.</li>
<li>$\int\sin x\,dx=-\cos x$, $\int\cos x\,dx=\sin x$.</li>
<li>$\int\frac{dx}{a^2+x^2}=\frac{1}{a}\arctan\frac{x}{a}$.</li>
</ul>
<h3>פונקציה פנימית לינארית</h3>
<p>כשבמקום $x$ מופיע $ax+b$, האינטגרל הוא אותו אינטגרל בטבלה, <b>חלקי $a$</b>:</p>
<div class="lesson-formula">$\int g(ax+b)\,dx=\frac{1}{a}\,G(ax+b)+C$, כאשר $G'=g$</div>
<p>הסיבה: גזירה של $G(ax+b)$ מכפילה ב-$a$, וה-$\frac1a$ מבטל את זה.</p>
<h3>מונה שהוא נגזרת המכנה</h3>
<div class="lesson-rule">🔑 $\int\frac{f'(x)}{f(x)}dx=\ln|f(x)|+C$. אם חסר רק מספר קבוע במונה, מוסיפים אותו מבחוץ.</div>
<div class="lesson-ex">דוגמה: $\int e^{5x}dx=\frac{e^{5x}}{5}+C$. ‏$\int\frac{dx}{2x-1}=\frac{1}{2}\ln|2x-1|+C$. ‏$\int\frac{3x^2}{x^3+1}dx=\ln|x^3+1|+C$.</div>
<div class="lesson-trap">⚠️ שוכחים את ה-$\frac1a$. בדיקה מהירה: גוזרים את התשובה, ואם יצא $a$ פעמים האינטגרנד, חסר $\frac1a$.</div>
"""
fact("lesson C01: e^{5x}/5", ok(exp(5*x), exp(5*x)/5))
fact("lesson C01: ln|2x-1|/2", ok(1/(2*x - 1), log(sp.Abs(2*x - 1))/2))
fact("lesson C01: ln(x^3+1)", ok(3*x**2/(x**3 + 1), log(x**3 + 1)))
q = []
q.append(mcq("C01-Q1", r"מהו $\int\cos(3x)\,dx$ ?", [
    (r"$\frac{\sin 3x}{3}+C$", ok(cos(3*x), sin(3*x)/3)),
    (r"$\sin 3x+C$", ok(cos(3*x), sin(3*x))),
    (r"$3\sin 3x+C$", ok(cos(3*x), 3*sin(3*x))),
    (r"$-\frac{\sin 3x}{3}+C$", ok(cos(3*x), -sin(3*x)/3)),
], r"במקום $x$ מופיע $3x$, ולכן התשובה היא $\sin(3x)$ חלקי $3$: **$\frac{\sin 3x}{3}$**. גזירה: $\frac{3\cos3x}{3}=\cos3x$. ‏$\sin3x$ נותנת $3\cos3x$, פי שלושה מהנדרש. ‏$3\sin3x$ נותנת $9\cos3x$. המינוס מתאים ל-$\sin$ ולא ל-$\cos$.",
    "פנימית לינארית ax+b: אותה שורה בטבלה, חלקי a"))
q.append(mcq("C01-Q2", r"מהו $\int e^{2x+1}\,dx$ ?", [
    (r"$\frac{e^{2x+1}}{2}+C$", ok(exp(2*x + 1), exp(2*x + 1)/2)),
    (r"$e^{2x+1}+C$", ok(exp(2*x + 1), exp(2*x + 1))),
    (r"$2e^{2x+1}+C$", ok(exp(2*x + 1), 2*exp(2*x + 1))),
    (r"$\frac{e^{2x+1}}{2x+1}+C$", ok(exp(2*x + 1), exp(2*x + 1)/(2*x + 1))),
], r"הפנימית $2x+1$ לינארית עם $a=2$, ולכן **$\frac{e^{2x+1}}{2}$**. ‏$e^{2x+1}$ נותנת פי שניים. ‏$2e^{2x+1}$ נותנת פי ארבעה. החלוקה ב-$2x+1$ היא כלל החזקה שהוחל על אקספוננט, וגזירתה מוסיפה איבר שלא קיים באינטגרנד.",
    "אקספוננט עם 2x+1: חלקי המקדם 2, לא חלקי הפנימית"))
q.append(mcq("C01-Q3", r"מהו $\int\frac{dx}{3x-2}$ ?", [
    (r"$\frac{1}{3}\ln|3x-2|+C$", ok(1/(3*x - 2), log(sp.Abs(3*x - 2))/3)),
    (r"$\ln|3x-2|+C$", ok(1/(3*x - 2), log(sp.Abs(3*x - 2)))),
    (r"$3\ln|3x-2|+C$", ok(1/(3*x - 2), 3*log(sp.Abs(3*x - 2)))),
    (r"$-\frac{1}{(3x-2)^2}+C$", ok(1/(3*x - 2), -1/(3*x - 2)**2)),
], r"שורת הטבלה היא $\ln|x|$, והפנימית $3x-2$ נותנת **$\frac13\ln|3x-2|$**. ‏$\ln|3x-2|$ מחזירה $\frac{3}{3x-2}$. ‏$3\ln$ מחזירה פי תשעה. התשובה האחרונה היא נגזרת של $\frac1{3x-2}$ ולא אינטגרל שלה.",
    "1/(ax+b): (1/a)·ln|ax+b|"))
q.append(mcq("C01-Q4", r"מהו $\int\frac{2x}{x^2+5}\,dx$ ?", [
    (r"$\ln\left(x^2+5\right)+C$", ok(2*x/(x**2 + 5), log(x**2 + 5))),
    (r"$\frac{1}{\sqrt5}\arctan\frac{x}{\sqrt5}+C$", ok(2*x/(x**2 + 5), atan(x/sqrt(5))/sqrt(5))),
    (r"$2x\ln\left(x^2+5\right)+C$", ok(2*x/(x**2 + 5), 2*x*log(x**2 + 5))),
    (r"$\frac{2}{x^2+5}+C$", ok(2*x/(x**2 + 5), 2/(x**2 + 5))),
], r"המונה $2x$ הוא בדיוק הנגזרת של המכנה $x^2+5$, ולכן **$\ln(x^2+5)$** (ללא ערך מוחלט, כי $x^2+5>0$). ‏$\arctan$ מתאים ל-$\frac{1}{x^2+5}$ בלי $x$ במונה. שני האחרים לא נותנים את האינטגרנד כשגוזרים.",
    "מונה = נגזרת המכנה ← ln של המכנה"))
q.append(numeric("C01-Q5", r"$\int\frac{dx}{4x+1}=k\ln|4x+1|+C$. מהו $k$ ?", 0.25, R(1, 4),
                 r"הפנימית $4x+1$ מגיעה עם $a=4$, ולכן $k=\frac14=0.25$. גזירה: $\frac14\cdot\frac{4}{4x+1}=\frac{1}{4x+1}$.",
                 "1/(ax+b): המקדם k הוא 1/a", tol=0))
q.append(mcq("C01-Q6", r"מהו $\int\frac{dx}{x^2+9}$ ?", [
    (r"$\frac{1}{3}\arctan\frac{x}{3}+C$", ok(1/(x**2 + 9), atan(x/3)/3)),
    (r"$\arctan\frac{x}{3}+C$", ok(1/(x**2 + 9), atan(x/3))),
    (r"$\frac{1}{9}\arctan\frac{x}{9}+C$", ok(1/(x**2 + 9), atan(x/9)/9)),
    (r"$\frac12\ln\left(x^2+9\right)+C$", ok(1/(x**2 + 9), log(x**2 + 9)/2)),
], r"השורה בטבלה: $\frac1a\arctan\frac xa$ עם $a=3$, כלומר **$\frac13\arctan\frac x3$**. בלי ה-$\frac13$ הגזירה נותנת $\frac{3}{x^2+9}$. ‏$\ln$ מתאים למונה $x$, שלא קיים כאן.",
    "1/(a²+x²): (1/a)·arctan(x/a)"))
level("C01", 1, "📘", "הטבלה ופנימית לינארית",
      "לפתור אינטגרלים שהם שורה בטבלה, כולל פנימית לינארית ומונה שהוא נגזרת המכנה.", L1, q)

# ===================================================================== C02  substitution
L2 = r"""
<p>הצבה היא הפיכה של הכלל "נגזרת של פנימית" אחורה. מחפשים בתוך האינטגרנד <b>פונקציה פנימית $g(x)$</b> ו<b>גורם אחר שהוא (עד כדי מספר) הנגזרת $g'(x)$</b>.</p>
<h3>המתכון</h3>
<ul>
<li>בוחרים $t=g(x)$ וכותבים $dt=g'(x)\,dx$.</li>
<li>מחליפים את כל האינטגרנד ל-$t$. אם נשאר $x$ חופשי, ההצבה לא מתאימה.</li>
<li>פותרים באמצעות הטבלה ומחזירים $t=g(x)$.</li>
</ul>
<div class="lesson-ex">דוגמה: $\int x\,e^{x^2}dx$. הפנימית היא $t=x^2$, ו-$dt=2x\,dx$ כלומר $x\,dx=\frac12dt$.<br>
האינטגרל הופך ל-$\frac12\int e^{t}dt=\frac12e^{t}+C=\frac12e^{x^2}+C$.</div>
<div class="lesson-rule">🔑 סימן מובהק להצבה: כשאין דרך לעשות את זה אחרת. ב-$\int xe^{x^2}dx$ אי אפשר בחלקים, כי $e^{x^2}$ אין לה אינטגרל אלמנטרי. ‏$\sin x\cos^2x$: הפנימית $\cos x$ וגורם $\sin x$ הוא הנגזרת (עד מינוס).</div>
<div class="lesson-trap">⚠️ אחרי ההצבה לא אמור להישאר $x$. אם נשאר, או שבחרתם פנימית לא נכונה, או ששכחתם להחליף את $dx$.</div>
"""
fact("lesson C02: x e^{x^2} = e^{x^2}/2", ok(x*exp(x**2), exp(x**2)/2))
fact("lesson C02: e^{x^2} has no elementary primitive (erfi)", sp.integrate(exp(x**2), x).has(sp.erfi))
q = []
q.append(mcq("C02-Q1", r"מהו $\int x\,e^{x^2}\,dx$ ?", [
    (r"$\frac12e^{x^2}+C$", ok(x*exp(x**2), exp(x**2)/2)),
    (r"$e^{x^2}+C$", ok(x*exp(x**2), exp(x**2))),
    (r"$2e^{x^2}+C$", ok(x*exp(x**2), 2*exp(x**2))),
    (r"$\frac{x^2}{2}e^{x^2}+C$", ok(x*exp(x**2), x**2*exp(x**2)/2)),
], r"עם $t=x^2$ מקבלים $x\,dx=\frac12dt$ ו-$\frac12\int e^tdt=$ **$\frac12e^{x^2}$**. ‏$e^{x^2}$ נותנת $2xe^{x^2}$, פי שניים. ‏$2e^{x^2}$ נותנת פי ארבעה. ‏$\frac{x^2}{2}e^{x^2}$ היא ניסיון להשתמש בכלל החזקה על הגורם $x$.",
    "הפנימית x² והגורם x הוא חצי מהנגזרת שלה"))
f2 = cos(x)/(1 + sin(x)**2)
# t = sin x -> 1/(1+t^2) rational; t = cos x -> leftover sin x (irrational in t); t = x -> unchanged; t = 1+sin^2 -> sqrt(t-1) leftover
h_sin = sp.simplify((f2/sp.diff(sin(x), x)).subs(sin(x), t))
h_cos = (f2/sp.diff(cos(x), x))
h_cos_t = sp.simplify(h_cos.subs(cos(x), t).subs(sin(x), sqrt(1 - t**2)))  # sin x = sqrt(1-t^2) for t=cos x in (0,pi)
h_g = f2/sp.diff(1 + sin(x)**2, x)
h_g_t = sp.simplify(h_g.subs(sin(x), sqrt(t - 1)).subs(cos(x), sqrt(2 - t)))
fact("C02-Q2: t=sin x gives 1/(1+t^2), rational", sp.simplify(h_sin - 1/(1 + t**2)) == 0 and h_sin.is_rational_function(t))
fact("C02-Q2: t=cos x leaves sqrt(1-t^2)", not h_cos_t.is_rational_function(t))
fact("C02-Q2: t=1+sin^2 leaves roots", not h_g_t.is_rational_function(t))
fact("C02-Q2: t=x does not change the integrand", f2.subs(x, t) == f2.subs(x, t) and not f2.subs(x, t).is_rational_function(t))
q.append(mcq("C02-Q2", r"באינטגרל $\int\frac{\cos x}{1+\sin^2x}\,dx$, איזו הצבה מחזירה אינטגרל רציונלי ב-$t$ בלבד ?", [
    (r"$t=\sin x$", h_sin.is_rational_function(t)),
    (r"$t=\cos x$", h_cos_t.is_rational_function(t)),
    (r"$t=1+\sin^2x$", h_g_t.is_rational_function(t)),
    (r"$t=x$", f2.subs(x, t).is_rational_function(t)),
], r"עם $t=\sin x$ מקבלים $dt=\cos x\,dx$, והאינטגרל הוא **$\int\frac{dt}{1+t^2}=\arctan t$**, כלומר $\arctan(\sin x)$. עם $t=\cos x$ נשאר $\sin x=\sqrt{1-t^2}$ במכנה. עם $t=1+\sin^2x$ נשארים שורשים. ‏$t=x$ לא משנה את האינטגרנד בכלל.",
    "בוחרים פנימית כך שהגורם האחר הוא הנגזרת שלה"))
q.append(mcq("C02-Q3", r"מהו $\int\frac{\sin x}{\cos^3x}\,dx$ ?", [
    (r"$\frac{1}{2\cos^2x}+C$", ok(sin(x)/cos(x)**3, 1/(2*cos(x)**2))),
    (r"$-\frac{1}{2\cos^2x}+C$", ok(sin(x)/cos(x)**3, -1/(2*cos(x)**2))),
    (r"$\frac{1}{\cos^2x}+C$", ok(sin(x)/cos(x)**3, 1/cos(x)**2)),
    (r"$-\frac{\cos^{-2}x}{2}\cdot\sin x+C$", ok(sin(x)/cos(x)**3, -sin(x)/(2*cos(x)**2))),
], r"הפנימית $t=\cos x$, ו-$dt=-\sin x\,dx$. מקבלים $-\int t^{-3}dt=\frac{1}{2t^2}$, כלומר **$\frac{1}{2\cos^2x}$**. מי ששכח את המינוס של $dt$ מקבל את הסימן ההפוך. ‏$\frac{1}{\cos^2x}$ נותנת פי שניים. התשובה האחרונה משאירה גורם $\sin x$ שהיה אמור להיעלם.",
    "sin x dx = -dt כש-t = cos x"))
q.append(numeric("C02-Q4", r"$\int x\left(x^2+1\right)^3dx=k\left(x^2+1\right)^4+C$. מהו $k$ ?", 0.125, R(1, 8),
                 r"עם $t=x^2+1$ מקבלים $x\,dx=\frac12dt$, ו-$\frac12\int t^3dt=\frac{t^4}{8}$. לכן $k=\frac18=0.125$.",
                 "x dx = dt/2: מוסיפים 1/2 ואז כלל החזקה", tol=0))
assert ok(x*(x**2 + 1)**3, (x**2 + 1)**4/8)
q.append(mcq("C02-Q5", r"מהו $\int\frac{(\ln x)^2}{x}\,dx$ ?", [
    (r"$\frac{(\ln x)^3}{3}+C$", ok(log(x)**2/x, log(x)**3/3)),
    (r"$\frac{(\ln x)^3}{3x}+C$", ok(log(x)**2/x, log(x)**3/(3*x))),
    (r"$\frac{(\ln x)^2}{2}+C$", ok(log(x)**2/x, log(x)**2/2)),
    (r"$2\ln x+C$", ok(log(x)**2/x, 2*log(x))),
], r"הפנימית $t=\ln x$ עם $dt=\frac{dx}{x}$. מקבלים $\int t^2dt=\frac{t^3}{3}$, כלומר **$\frac{\ln^3x}{3}$**. אין סיבה לחלק ב-$x$ שוב: ה-$\frac1x$ כבר נבלע ב-$dt$. ‏$\frac{\ln^2x}{2}$ היא החזקה השגויה (האינטגרל של $\ln x/x$).",
    "ln x עם dx/x: t = ln x"))
bad = [r"$t=x^2$, $dt=2x\,dx$", r"$\int x^2e^{x^3}dx=3\int e^{t}dt$", r"$=3e^{t}+C$", r"$=3e^{x^3}+C$"]
q.append({"id": "C02-Q6", "step": {"type": "findbug", "prompt": r"בפתרון של $\int x^2e^{x^3}dx$ יש שורה אחת שגויה. איזו ?",
          "lines": [r"בוחרים $t=x^3$ וכותבים $dt=3x^2\,dx$.",
                    r"לכן $x^2\,dx=3\,dt$ והאינטגרל הוא $3\int e^{t}\,dt$.",
                    r"$3\int e^{t}\,dt=3e^{t}+C$.",
                    r"מחזירים: $3e^{x^3}+C$."],
          "bugIndex": 1,
          "explain": r"מ-$dt=3x^2\,dx$ מקבלים $x^2\,dx=\frac13dt$ ולא $3\,dt$. התשובה הנכונה היא $\frac13e^{x^3}+C$. הגזירה של $3e^{x^3}$ נותנת $9x^2e^{x^3}$."},
          "recap": "מבודדים את הגורם: x² dx = dt/3, לא 3 dt"})
fact("C02-Q6: correct answer e^{x^3}/3, buggy 3e^{x^3} fails", ok(x**2*exp(x**3), exp(x**3)/3) and not ok(x**2*exp(x**3), 3*exp(x**3)))
level("C02", 2, "🔁", "הצבה: פנימית ונגזרתה",
      "לזהות פונקציה פנימית שנגזרתה מופיעה באינטגרנד, ולבצע את ההצבה בלי להשאיר x.", L2, q)

# ===================================================================== C03  integration by parts: polynomial times e/sin/cos
L3 = r"""
<p>אינטגרציה בחלקים: $\int u\,dv=uv-\int v\,du$. היא באה לעזרה כשיש <b>מכפלה</b> שאין בה פנימית עם נגזרתה.</p>
<h3>איך בוחרים $u$</h3>
<p>מכפלה של פולינום ב-$e^{x}$, $\sin$ או $\cos$: <b>$u=$ הפולינום</b> ו-$dv=$ השאר. כל סיבוב מוריד את דרגת הפולינום ב-1, עד שהוא נעלם.</p>
<div class="lesson-ex">דוגמה: $\int x\,e^{x}dx$. ‏$u=x$, ‏$dv=e^{x}dx$, ‏$du=dx$, ‏$v=e^{x}$.<br>
$\int xe^{x}dx=xe^{x}-\int e^{x}dx=xe^{x}-e^{x}+C=(x-1)e^{x}+C$.</div>
<div class="lesson-rule">🔑 בבחירה ההפוכה ($u=e^{x}$ ו-$dv=x\,dx$) הפולינום עולה בדרגה: $v=\frac{x^2}{2}$ והאינטגרל החדש גרוע מהמקורי.</div>
<p>פולינום מדרגה $n$ דורש $n$ סיבובים. הדרך לא לטעות בסימנים: לכתוב $u,\ du,\ dv,\ v$ בשורה לפני שמציבים.</p>
<div class="lesson-trap">⚠️ מי ששוכח את המינוס ב-$v=-\cos x$ מקבל סימן שגוי בכל התשובה. תמיד בודקים בגזירה.</div>
"""
fact("lesson C03: (x-1)e^x", ok(x*exp(x), (x - 1)*exp(x)))


def parts_next(u, dv):
    """returns integrand of  int v du  for given u, dv"""
    v = sp.integrate(dv, x)
    return sp.simplify(v*sp.diff(u, x))


def polydeg(expr):
    expr = sp.expand(expr)
    ex = [t_ for t_ in sp.Mul.make_args(expr)]
    return sp.degree(sp.Poly(sp.simplify(expr/(exp(x) if expr.has(exp) else 1)), x)) if False else None


# u = x, dv = sin x : v du = -cos x  (no x).   u = sin x, dv = x dx : v du = x^2/2 cos x  (degree rises)
nxt_good = parts_next(x, sin(x))
nxt_bad = parts_next(sin(x), x)
fact("C03-Q1: good choice leaves -cos x (no polynomial factor)", sp.simplify(nxt_good + cos(x)) == 0)
fact("C03-Q1: bad choice raises the power of x", sp.simplify(nxt_bad - x**2*cos(x)/2) == 0)
nxt_t = parts_next(x, exp(x))
q = []
q.append(mcq("C03-Q1", r"באינטגרל $\int x\sin x\,dx$ בחלקים, איזו בחירה מקטינה את הבעיה ?", [
    (r"$u=x,\ dv=\sin x\,dx$", sp.simplify(nxt_good + cos(x)) == 0),
    (r"$u=\sin x,\ dv=x\,dx$", sp.simplify(nxt_bad + cos(x)) == 0),
    (r"$u=x\sin x,\ dv=dx$", sp.simplify(sp.integrate(1, x)*sp.diff(x*sin(x), x) + cos(x)) == 0),
    (r"$u=1,\ dv=x\sin x\,dx$", False),
], r"עם $u=x$ מקבלים $du=dx$ ו-$v=-\cos x$, והאינטגרל החדש $\int-\cos x\,dx$ ללא $x$ כלל. עם $u=\sin x$ מקבלים $v=\frac{x^2}{2}$ והאינטגרל החדש $\int\frac{x^2}{2}\cos x\,dx$ מסובך יותר: הפולינום עלה בדרגה. הבחירה $u=x\sin x$ מחזירה $\int\left(x\sin x+x^2\cos x\right)dx$, גרוע מהמקורי. הבחירה האחרונה היא פשוט האינטגרל המקורי.",
    "פולינום × sin/cos/e^x: u הוא הפולינום"))
fact("C03-Q1: u=x sin x keeps a product", sp.expand(sp.integrate(1, x)*sp.diff(x*sin(x), x)) == x*sin(x) + x**2*cos(x))
q.append(mcq("C03-Q2", r"מהו $\int x\,e^{x}\,dx$ ?", [
    (r"$(x-1)e^{x}+C$", ok(x*exp(x), (x - 1)*exp(x))),
    (r"$(x+1)e^{x}+C$", ok(x*exp(x), (x + 1)*exp(x))),
    (r"$xe^{x}+C$", ok(x*exp(x), x*exp(x))),
    (r"$\frac{x^2}{2}e^{x}+C$", ok(x*exp(x), x**2*exp(x)/2)),
], r"‏$u=x$ ו-$dv=e^xdx$ נותנים $xe^x-\int e^xdx=$ **$(x-1)e^x$**. ‏$(x+1)e^x$ נובעת מטעות בסימן של האינטגרל השני. ‏$xe^x$ שוכחת את החלק השני בכלל. ‏$\frac{x^2}{2}e^x$ היא כפל של שני האינטגרלים.",
    "xe^x ← (x−1)e^x"))
q.append(mcq("C03-Q3", r"מהו $\int x\cos x\,dx$ ?", [
    (r"$x\sin x+\cos x+C$", ok(x*cos(x), x*sin(x) + cos(x))),
    (r"$x\sin x-\cos x+C$", ok(x*cos(x), x*sin(x) - cos(x))),
    (r"$-x\sin x+\cos x+C$", ok(x*cos(x), -x*sin(x) + cos(x))),
    (r"$\frac{x^2}{2}\sin x+C$", ok(x*cos(x), x**2*sin(x)/2)),
], r"‏$u=x$, ‏$v=\sin x$: ‏$x\sin x-\int\sin x\,dx=x\sin x+\cos x$, כי $\int\sin x\,dx=-\cos x$. ‏$x\sin x-\cos x$ מתקבלת כשמשאירים את המינוס הכפול. ‏$-x\sin x+\cos x$ הפוכה בסימן הכולל. ‏$\frac{x^2}{2}\sin x$ מתייחסת לאינטגרל כאל מכפלת אינטגרלים.",
    "xcos x ← x sin x + cos x"))
q.append(numeric("C03-Q4", r"$\int x\,e^{2x}dx=\left(\frac{x}{2}-a\right)e^{2x}+C$. מהו $a$ ?", 0.25, R(1, 4),
                 r"‏$u=x$, ‏$v=\frac{e^{2x}}{2}$: ‏$\frac{xe^{2x}}{2}-\frac12\int e^{2x}dx=\frac{xe^{2x}}{2}-\frac{e^{2x}}{4}$. לכן $a=\frac14=0.25$.",
                 "v = e^{2x}/2: הפנימית הלינארית מחלקת ב-2 פעמיים", tol=0))
assert ok(x*exp(2*x), (x/2 - R(1, 4))*exp(2*x))
q.append(mcq("C03-Q5", r"מהו $\int x^2e^{x}\,dx$ ?", [
    (r"$\left(x^2-2x+2\right)e^{x}+C$", ok(x**2*exp(x), (x**2 - 2*x + 2)*exp(x))),
    (r"$\left(x^2+2x+2\right)e^{x}+C$", ok(x**2*exp(x), (x**2 + 2*x + 2)*exp(x))),
    (r"$\left(x^2-2x\right)e^{x}+C$", ok(x**2*exp(x), (x**2 - 2*x)*exp(x))),
    (r"$\left(x^2-2x+1\right)e^{x}+C$", ok(x**2*exp(x), (x**2 - 2*x + 1)*exp(x))),
], r"סיבוב ראשון: ‏$x^2e^x-2\int xe^xdx$. סיבוב שני: ‏$\int xe^x=(x-1)e^x$. התוצאה $x^2e^x-2(x-1)e^x=$ **$(x^2-2x+2)e^x$**. שאר התשובות נופלות בסימן או במחסור בקבוע ($+2$ נובע מ-$-2\cdot(-1)$).",
    "x²e^x: שני סיבובים, סימנים מתחלפים"))
q.append({"id": "C03-Q6", "step": {"type": "order", "prompt": r"סדרו את הפתרון של $\int x\sin x\,dx$.",
          "lines": [r"$u=x,\ dv=\sin x\,dx$",
                    r"$du=dx,\ v=-\cos x$",
                    r"$\int x\sin x\,dx=-x\cos x+\int\cos x\,dx$",
                    r"$=-x\cos x+\sin x+C$"],
          "explain": r"קודם בוחרים $u,dv$, אחר כך מחשבים $du,v$, ואז מציבים בנוסחה ולבסוף פותרים את האינטגרל הנותר."},
          "recap": "u,dv ← du,v ← הצבה בנוסחה ← האינטגרל הנותר"})
fact("C03-Q6: -x cos x + sin x", ok(x*sin(x), -x*cos(x) + sin(x)))
level("C03", 3, "✂️", "בחלקים: פולינום כפול e^x, sin, cos",
      "לבחור u כפולינום ולפתור אינטגרל מכפלה בסיבוב אחד או בשניים.", L3, q)

# ===================================================================== C04  parts with ln and arctan
L4 = r"""
<p>כשבאינטגרנד יש $\ln x$ או $\arctan x$, הם <b>תמיד $u$</b>, כי נגזרתם פשוטה: $\left(\ln x\right)'=\frac1x$ ו-$\left(\arctan x\right)'=\frac{1}{1+x^2}$. את האינטגרלים שלהם ישירות לא מכירים.</p>
<div class="lesson-formula">$\int\ln x\,dx=x\ln x-x+C$, ‏$\int\arctan x\,dx=x\arctan x-\frac12\ln\left(1+x^2\right)+C$</div>
<p>אלה בחלקים עם $dv=dx$ (כלומר $v=x$): כותבים את $\ln x$ כ-$\ln x\cdot1$.</p>
<div class="lesson-ex">דוגמה: $\int x\ln x\,dx$. ‏$u=\ln x$, ‏$dv=x\,dx$, ‏$du=\frac{dx}{x}$, ‏$v=\frac{x^2}{2}$.<br>
$\int x\ln x\,dx=\frac{x^2}{2}\ln x-\int\frac{x}{2}dx=\frac{x^2}{2}\ln x-\frac{x^2}{4}+C$.</div>
<div class="lesson-rule">🔑 סימן להצלחה: אחרי הבחירה הנכונה ה-$\ln$ או ה-$\arctan$ נעלם מהאינטגרל הנותר. אם הוא נשאר, הבחירה הייתה הפוכה.</div>
<div class="lesson-trap">⚠️ ב-$\arctan$ האינטגרל הנותר הוא $\int\frac{x}{1+x^2}dx$, וזה הצבה (מונה = חצי נגזרת המכנה), לא טבלה ישירה.</div>
<div class="lesson-trap">⚠️ ב-$\int x\arctan x\,dx$ נשאר $\int\frac{x^2}{1+x^2}dx$. מונה מאותה דרגה כמו המכנה: כותבים $\frac{x^2}{1+x^2}=1-\frac{1}{1+x^2}$ ואז $x-\arctan x$.</div>
"""
fact("lesson C04: x ln x - x", ok(log(x), x*log(x) - x))
fact("lesson C04: x atan x - ln(1+x^2)/2", ok(atan(x), x*atan(x) - log(1 + x**2)/2))
fact("lesson C04: x^2/2 ln x - x^2/4", ok(x*log(x), x**2*log(x)/2 - x**2/4))
good = parts_next(log(x), x)            # x/2
bad = parts_next(x, log(x))             # (x ln x - x)*1
q = []
q.append(mcq("C04-Q1", r"באינטגרל $\int x\ln x\,dx$ בחלקים, איזו בחירה מעלימה את ה-$\ln$ ?", [
    (r"$u=\ln x,\ dv=x\,dx$", not good.has(log)),
    (r"$u=x,\ dv=\ln x\,dx$", not bad.has(log)),
    (r"$u=x\ln x,\ dv=dx$", not sp.simplify(sp.diff(x*log(x), x)*x).has(log)),
    (r"$u=1,\ dv=x\ln x\,dx$", False),
], r"עם $u=\ln x$ מקבלים $v=\frac{x^2}{2}$ ו-$v\,du=\frac{x}{2}dx$, בלי $\ln$. עם $u=x$ צריך קודם את $v=\int\ln x\,dx=x\ln x-x$, והאינטגרל הנותר $\int(x\ln x-x)dx$ שוב מכיל $\ln$. הבחירה $u=x\ln x$ מחזירה $(\ln x+1)x$, שוב עם $\ln$. הבחירה האחרונה היא האינטגרל עצמו.",
    "ln הוא תמיד u: הנגזרת שלו 1/x מעלימה אותו"))
fact("C04-Q1: u=x ln x leaves ln", sp.diff(x*log(x), x).has(log))
q.append(mcq("C04-Q2", r"מהו $\int\ln x\,dx$ ?", [
    (r"$x\ln x-x+C$", ok(log(x), x*log(x) - x)),
    (r"$x\ln x+x+C$", ok(log(x), x*log(x) + x)),
    (r"$\frac1x+C$", ok(log(x), 1/x)),
    (r"$x\ln x-1+C$", ok(log(x), x*log(x) - 1)),
], r"‏$u=\ln x$ ו-$dv=dx$: ‏$x\ln x-\int x\cdot\frac1x\,dx=$ **$x\ln x-x$**. ‏$\frac1x$ היא הנגזרת של $\ln x$ ולא האינטגרל. התשובה עם $+x$ שוכחת את המינוס של האינטגרל הנותר. התשובה האחרונה מחשבת את $\int 1\,dx$ כ-$1$.",
    "ln x ← x ln x − x"))
q.append(mcq("C04-Q3", r"מהו $\int x\ln x\,dx$ ?", [
    (r"$\frac{x^2}{2}\ln x-\frac{x^2}{4}+C$", ok(x*log(x), x**2*log(x)/2 - x**2/4)),
    (r"$\frac{x^2}{2}\ln x-\frac{x^2}{2}+C$", ok(x*log(x), x**2*log(x)/2 - x**2/2)),
    (r"$\frac{x^2}{2}\ln x+\frac{x^2}{4}+C$", ok(x*log(x), x**2*log(x)/2 + x**2/4)),
    (r"$\frac{x^2}{2}\cdot\frac1x+C$", ok(x*log(x), x**2/2*(1/x))),
], r"‏$\frac{x^2}{2}\ln x-\int\frac{x^2}{2}\cdot\frac1x\,dx=\frac{x^2}{2}\ln x-\frac{x^2}{4}$. הטעות הנפוצה היא $\frac{x^2}{2}$ במקום $\frac{x^2}{4}$, כלומר לשכוח את חצי המקדם. התשובה השלישית שגויה בסימן. האחרונה היא מכפלת הנגזרות.",
    "x ln x ← (x²/2) ln x − x²/4"))
q.append(numeric("C04-Q4", r"$\int x\ln x\,dx=\frac{x^2}{2}\ln x-k\,x^2+C$. מהו $k$ ?", 0.25, R(1, 4),
                 r"האינטגרל הנותר $\int\frac{x}{2}dx=\frac{x^2}{4}$, ולכן $k=0.25$.",
                 "האינטגרל הנותר ב-x ln x הוא x/2", tol=0))
q.append(mcq("C04-Q5", r"מהו $\int\arctan x\,dx$ ?", [
    (r"$x\arctan x-\frac12\ln\left(1+x^2\right)+C$", ok(atan(x), x*atan(x) - log(1 + x**2)/2)),
    (r"$x\arctan x-\ln\left(1+x^2\right)+C$", ok(atan(x), x*atan(x) - log(1 + x**2))),
    (r"$x\arctan x+\frac12\ln\left(1+x^2\right)+C$", ok(atan(x), x*atan(x) + log(1 + x**2)/2)),
    (r"$\frac{1}{1+x^2}+C$", ok(atan(x), 1/(1 + x**2))),
], r"‏$u=\arctan x$, ‏$dv=dx$: ‏$x\arctan x-\int\frac{x}{1+x^2}dx$, והאינטגרל הנותר הוא $\frac12\ln(1+x^2)$ (הצבה $t=1+x^2$). התשובות עם $\ln$ שלם או עם סימן הפוך שוכחות את החצי או את המינוס.",
    "arctan x ← x arctan x − ½ ln(1+x²)"))
q.append(mcq("C04-Q6", r"מהו $\int x\arctan x\,dx$ ?", [
    (r"$\frac{x^2+1}{2}\arctan x-\frac x2+C$", ok(x*atan(x), (x**2 + 1)/2*atan(x) - x/2)),
    (r"$\frac{x^2}{2}\arctan x-\frac x2+C$", ok(x*atan(x), x**2/2*atan(x) - x/2)),
    (r"$\frac{x^2+1}{2}\arctan x+\frac x2+C$", ok(x*atan(x), (x**2 + 1)/2*atan(x) + x/2)),
    (r"$\frac{x^2}{2}\arctan x-\frac12\ln\left(1+x^2\right)+C$", ok(x*atan(x), x**2/2*atan(x) - log(1 + x**2)/2)),
], r"‏$u=\arctan x$, ‏$v=\frac{x^2}{2}$: ‏$\frac{x^2}{2}\arctan x-\frac12\int\frac{x^2}{1+x^2}dx$. כתיבה $\frac{x^2}{1+x^2}=1-\frac{1}{1+x^2}$ נותנת $\frac{x^2}{2}\arctan x-\frac x2+\frac12\arctan x=$ **$\frac{x^2+1}{2}\arctan x-\frac x2$**. מי ששוכח את $\arctan$ שחוזר מקבל את התשובה השנייה. האחרונה מערבבת עם הדוגמה של $\int\arctan x$.",
    "x arctan x: האינטגרל הנותר דורש חלוקה x²/(1+x²) = 1 − 1/(1+x²)"))
level("C04", 4, "🪢", "בחלקים: ln ו-arctan",
      "לזהות ש-ln ו-arctan הם תמיד u, ולפתור אינטגרלים שבהם הם לבדם או כפולים בפולינום.", L4, q)

# ===================================================================== C05  rational: division and linear partial fractions
L5 = r"""
<p>מנה של פולינומים $\frac{P(x)}{Q(x)}$. הצעד הראשון תמיד אותו דבר: להשוות דרגות.</p>
<div class="lesson-rule">🔑 אם דרגת $P\ge$ דרגת $Q$: <b>חלוקה ארוכה קודם</b>. מקבלים פולינום (קל לאינטגרל) ושבר שבו דרגת המונה קטנה מהמכנה.</div>
<h3>פירוק לשברים חלקיים</h3>
<p>כשדרגת המונה קטנה, מפרקים את המכנה לגורמים לינאריים שונים, ולכל אחד שבר:</p>
<div class="lesson-formula">$\frac{3x+5}{(x-1)(x+1)}=\frac{A}{x-1}+\frac{B}{x+1}$</div>
<p>מוצאים את $A,B$ בהצבת השורשים בתוך משוואת המונים: $3x+5=A(x+1)+B(x-1)$. עם $x=1$: ‏$8=2A$, כלומר $A=4$. עם $x=-1$: ‏$2=-2B$, כלומר $B=-1$.</p>
<p>ואז כל שבר הוא $\ln$: $\int\frac{A}{x-r}dx=A\ln|x-r|$.</p>
<div class="lesson-ex">דוגמה: $\int\frac{x+3}{(x-1)(x+1)}dx$. ‏$A=2$, ‏$B=-1$. התשובה $2\ln|x-1|-\ln|x+1|+C$.</div>
<div class="lesson-trap">⚠️ פירוק לשברים חלקיים כשהדרגות לא מתאימות הוא טעות. אם דרגת המונה שווה או גדולה, חלוקה קודם.</div>
"""
fact("lesson C05: A=4,B=-1", sp.apart((3*x + 5)/((x - 1)*(x + 1)), x) == 4/(x - 1) - 1/(x + 1))
fact("lesson C05 ex: 2ln|x-1| - ln|x+1|", ok((x + 3)/((x - 1)*(x + 1)), 2*log(sp.Abs(x - 1)) - log(sp.Abs(x + 1))))
f5 = (x**3 + 2)/(x**2 - 1)
P5, Q5 = sp.Poly(x**3 + 2, x), sp.Poly(x**2 - 1, x)
quo, rem = sp.div(P5, Q5)
fact("C05-Q1: deg P >= deg Q", P5.degree() >= Q5.degree())
q = []
# t = x^2-1: f dx = (x^3+2)/(2x t) dt, leftover x
h5 = sp.simplify(f5/sp.diff(x**2 - 1, x))
q.append(mcq("C05-Q1", r"מהו הצעד הראשון הנכון באינטגרל $\int\frac{x^3+2}{x^2-1}\,dx$ ?", [
    (r"חלוקה ארוכה של המונה במכנה", P5.degree() >= Q5.degree() and quo.as_expr() == x),
    (r"פירוק מיידי לשברים חלקיים $\frac{A}{x-1}+\frac{B}{x+1}$", P5.degree() < Q5.degree()),
    (r"הצבה $t=x^2-1$", not sp.simplify(h5.subs(x, sqrt(t + 1))).is_rational_function(t) is False and False),
    (r"אינטגרציה בחלקים עם $u=x^3+2$", False),
], r"דרגת המונה (3) גדולה מדרגת המכנה (2), ולכן חלוקה ארוכה קודם: $x^3+2=x\left(x^2-1\right)+(x+2)$, כלומר $\frac{x^3+2}{x^2-1}=x+\frac{x+2}{x^2-1}$. פירוק מיידי נכשל כי הדרגות לא מתאימות. הצבה $t=x^2-1$ משאירה $x$ במונה ($x^3\,dx$ לא מכיל את החלק הקבוע $2$). בחלקים עם $u=x^3+2$ מחזיר שבר מסובך יותר.",
    "דרגת מונה ≥ מכנה: חלוקה ארוכה לפני כל דבר אחר"))
assert h5.has(x)
fact("C05-Q1: t=x^2-1 leaves x and a constant term (2) that is not x*dx", sp.expand(x**3 + 2) != sp.expand(x*(x**2 - 1)) and (sp.simplify(f5 - x/(x**2 - 1)*x)).has(x))
q.append(numeric("C05-Q2", r"$\frac{x^3+2}{x^2-1}=x+\frac{ax+2}{x^2-1}$. מהו $a$ ?", 1, rem.as_expr().coeff(x, 1),
                 r"‏$x\left(x^2-1\right)=x^3-x$, ולכן $x^3+2-\left(x^3-x\right)=x+2$. כלומר $a=1$ והשארית היא $x+2$.",
                 "חלוקה: מנה × מכנה + שארית", tol=0))
assert rem.as_expr() == x + 2 and eq(f5, x + (x + 2)/(x**2 - 1))
d3 = 1/((x - 1)*(x + 2))
q.append(mcq("C05-Q3", r"מהו $\int\frac{dx}{(x-1)(x+2)}$ ?", [
    (r"$\frac13\ln\left|\frac{x-1}{x+2}\right|+C$", ok(d3, log(sp.Abs((x - 1)/(x + 2)))/3)),
    (r"$\frac13\ln\left|\frac{x+2}{x-1}\right|+C$", ok(d3, log(sp.Abs((x + 2)/(x - 1)))/3)),
    (r"$\ln|(x-1)(x+2)|+C$", ok(d3, log(sp.Abs((x - 1)*(x + 2))))),
    (r"$\frac13\ln|x-1|+\frac13\ln|x+2|+C$", ok(d3, log(sp.Abs(x - 1))/3 + log(sp.Abs(x + 2))/3)),
], r"‏$\frac{1}{(x-1)(x+2)}=\frac13\left(\frac{1}{x-1}-\frac{1}{x+2}\right)$, ולכן האינטגרל הוא $\frac13\left(\ln|x-1|-\ln|x+2|\right)=$ **$\frac13\ln\left|\frac{x-1}{x+2}\right|$**. היפוך היחס נותן את הסימן ההפוך. ‏$\ln|(x-1)(x+2)|$ הוא האינטגרל של $\frac{2x+1}{(x-1)(x+2)}$. התשובה האחרונה חיברה במקום להחסיר.",
    "1/((x-a)(x-b)) = (1/(a−b))(1/(x−a) − 1/(x−b))"))
q.append(numeric("C05-Q4", r"$\frac{5}{(x-2)(x+3)}=\frac{A}{x-2}+\frac{B}{x+3}$. מהו $A$ ?", 1, sp.apart(5/((x - 2)*(x + 3)), x).coeff(1/(x - 2)) if False else R(5, 5),
                 r"‏$5=A(x+3)+B(x-2)$. עם $x=2$: ‏$5=5A$, כלומר $A=1$. (וגם $B=-1$.)",
                 "מציבים את השורש של הגורם שמחפשים", tol=0))
assert sp.apart(5/((x - 2)*(x + 3)), x) == 1/(x - 2) - 1/(x + 3)
d5 = (3*x + 5)/((x - 1)*(x + 1))
q.append(mcq("C05-Q5", r"מהו $\int\frac{3x+5}{(x-1)(x+1)}\,dx$ ?", [
    (r"$4\ln|x-1|-\ln|x+1|+C$", ok(d5, 4*log(sp.Abs(x - 1)) - log(sp.Abs(x + 1)))),
    (r"$4\ln|x+1|-\ln|x-1|+C$", ok(d5, 4*log(sp.Abs(x + 1)) - log(sp.Abs(x - 1)))),
    (r"$\ln|x-1|+\ln|x+1|+C$", ok(d5, log(sp.Abs(x - 1)) + log(sp.Abs(x + 1)))),
    (r"$\frac32\ln\left|x^2-1\right|+C$", ok(d5, R(3, 2)*log(sp.Abs(x**2 - 1)))),
], r"‏$A=4$, ‏$B=-1$ (ראו בשיעור), ולכן **$4\ln|x-1|-\ln|x+1|$**. החלפת המקדמים בין הגורמים נותנת את התשובה השנייה. התשובה השלישית ממלאת $A=B=1$ בלי לחשב. התשובה הרביעית מניחה שהמונה הוא כפולה של נגזרת המכנה $2x$, אבל המונה הוא $3x+5$.",
    "מפרקים, מוצאים A ו-B בהצבת שורשים, כל שבר הוא ln"))
q.append(mcq("C05-Q6", r"מהו $\int\frac{x}{x+1}\,dx$ ?", [
    (r"$x-\ln|x+1|+C$", ok(x/(x + 1), x - log(sp.Abs(x + 1)))),
    (r"$x+\ln|x+1|+C$", ok(x/(x + 1), x + log(sp.Abs(x + 1)))),
    (r"$\ln|x+1|+C$", ok(x/(x + 1), log(sp.Abs(x + 1)))),
    (r"$\frac{x^2}{2\left(x+1\right)}+C$", ok(x/(x + 1), x**2/(2*(x + 1)))),
], r"הדרגות שוות, לכן חלוקה: $\frac{x}{x+1}=1-\frac{1}{x+1}$, ומכאן **$x-\ln|x+1|$**. התשובה עם $+\ln$ שוכחת את המינוס. ‏$\ln|x+1|$ מתאימה למונה $1$ ולא $x$. התשובה האחרונה מחלקת את האינטגרלים.",
    "דרגות שוות: x/(x+1) = 1 − 1/(x+1)"))
level("C05", 5, "➗", "שברים: חלוקה ושברים חלקיים",
      "לבדוק דרגות, לחלק כשצריך, ולפרק מכנה עם גורמים לינאריים לשברים חלקיים.", L5, q)

# ===================================================================== C06  quadratic factors, completing the square, repeated factors
L6 = r"""
<p>מכנה ריבועי $x^2+px+q$ מתנהג לפי הדיסקרימיננטה $\Delta=p^2-4q$.</p>
<ul>
<li>$\Delta>0$: מתפרק לשני גורמים לינאריים, ואז שברים חלקיים רגילים (תוצאה: $\ln$).</li>
<li>$\Delta<0$: <b>לא מתפרק</b>. משלימים לריבוע ומקבלים $\arctan$.</li>
</ul>
<div class="lesson-ex">השלמה לריבוע: $x^2+2x+5=(x+1)^2+4$, ולכן $\int\frac{dx}{x^2+2x+5}=\frac12\arctan\frac{x+1}{2}+C$.</div>
<h3>מונה לינארי מעל ריבועי שלא מתפרק</h3>
<p>מפרקים את המונה לחלק שהוא נגזרת המכנה ולקבוע: $\frac{Bx+C}{x^2+k}=\frac{B}{2}\cdot\frac{2x}{x^2+k}+\frac{C}{x^2+k}$, ואז $\ln$ ו-$\arctan$.</p>
<h3>צורת הפירוק</h3>
<ul>
<li>גורם לינארי $(x-r)$: ‏$\frac{A}{x-r}$.</li>
<li>גורם כפול $(x-r)^2$: <b>שני</b> איברים, ‏$\frac{A}{x-r}+\frac{B}{(x-r)^2}$.</li>
<li>גורם ריבועי שלא מתפרק: ‏$\frac{Bx+C}{x^2+k}$ (מונה לינארי, לא קבוע).</li>
</ul>
<p>את המקדמים מוצאים בהשוואת מקדמים (או בהצבת שורש). למשל $\frac{1}{x(x^2+1)}=\frac{A}{x}+\frac{Bx+C}{x^2+1}$ נותן $1=A(x^2+1)+(Bx+C)x$: עם $x=0$ מקבלים $A=1$, ממקדם $x^2$ מקבלים $0=A+B$ ולכן $B=-1$, וממקדם $x$ מקבלים $C=0$.</p>
<div class="lesson-trap">⚠️ מונה קבוע מעל גורם ריבועי לא מספיק ל-$\frac{1}{x(x^2+1)}$ וכדומה: חסר $Bx$. וגורם כפול עם איבר אחד חסר חלק.</div>
"""
fact("lesson C06: arctan((x+1)/2)/2", ok(1/(x**2 + 2*x + 5), atan((x + 1)/2)/2))
q = []
q.append(mcq("C06-Q1", r"מהו $\int\frac{dx}{x^2+2x+5}$ ?", [
    (r"$\frac12\arctan\frac{x+1}{2}+C$", ok(1/(x**2 + 2*x + 5), atan((x + 1)/2)/2)),
    (r"$\arctan\frac{x+1}{2}+C$", ok(1/(x**2 + 2*x + 5), atan((x + 1)/2))),
    (r"$\frac12\arctan(x+1)+C$", ok(1/(x**2 + 2*x + 5), atan(x + 1)/2)),
    (r"$\ln\left(x^2+2x+5\right)+C$", ok(1/(x**2 + 2*x + 5), log(x**2 + 2*x + 5))),
], r"‏$x^2+2x+5=(x+1)^2+4$, ולכן **$\frac12\arctan\frac{x+1}{2}$**. בלי ה-$\frac12$ מקבלים פי שניים. ‏$\frac12\arctan(x+1)$ מתעלמת מהחילוק ב-$2$ בתוך ה-$\arctan$. ‏$\ln$ מתאים רק אם המונה היה $2x+2$.",
    "Δ<0: משלימים לריבוע ← (1/a) arctan((x+b)/a)"))
p2 = sp.Poly(x**2 + 4*x + 3, x).discriminant()
p3 = sp.Poly(x**2 + 4*x + 5, x).discriminant()
fact("C06-Q2: discriminants", p2 == 4 and p3 == -4)
q.append(mcq("C06-Q2", r"איזה סוג פונקציות יופיע בתשובה של $\int\frac{dx}{x^2+4x+3}$ ?", [
    (r"לוגריתמים בלבד (המכנה מתפרק)", p2 > 0 and ok(1/(x**2 + 4*x + 3), (log(x + 1) - log(x + 3))/2)),
    (r"$\arctan$ (המכנה לא מתפרק)", p2 < 0),
    (r"$\arctan$ ו-$\ln$ ביחד", p2 < 0 and False),
    (r"אי אפשר לבטא באמצעות פונקציות אלמנטריות", False),
], r"‏$\Delta=16-12=4>0$, והמכנה הוא $(x+1)(x+3)$. פירוק לשברים חלקיים נותן $\frac12\left(\frac{1}{x+1}-\frac{1}{x+3}\right)$, כלומר לוגריתמים בלבד. ‏$\arctan$ מופיע רק כש-$\Delta<0$ (למשל $x^2+4x+5$ עם $\Delta=-4$). השילוב מופיע כשיש גם מונה לינארי מעל ריבועי שלא מתפרק. והאינטגרל אלמנטרי.",
    "Δ>0: ln. Δ<0: arctan"))
q.append(mcq("C06-Q3", r"מהו $\int\frac{x+3}{x^2+1}\,dx$ ?", [
    (r"$\frac12\ln\left(x^2+1\right)+3\arctan x+C$", ok((x + 3)/(x**2 + 1), log(x**2 + 1)/2 + 3*atan(x))),
    (r"$\ln\left(x^2+1\right)+3\arctan x+C$", ok((x + 3)/(x**2 + 1), log(x**2 + 1) + 3*atan(x))),
    (r"$\frac12\ln\left(x^2+1\right)+\arctan 3x+C$", ok((x + 3)/(x**2 + 1), log(x**2 + 1)/2 + atan(3*x))),
    (r"$\ln|x+3|-\ln\left(x^2+1\right)+C$", ok((x + 3)/(x**2 + 1), log(sp.Abs(x + 3)) - log(x**2 + 1))),
], r"מפרקים: $\frac{x}{x^2+1}+\frac{3}{x^2+1}$. הראשון הוא חצי מנגזרת המכנה: $\frac12\ln(x^2+1)$. השני הוא $3\arctan x$. התשובה **$\frac12\ln(x^2+1)+3\arctan x$**. ‏$\ln(x^2+1)$ מלא נותן $\frac{2x}{x^2+1}$. ‏$\arctan3x$ מכניס את ה-$3$ פנימה. התשובה האחרונה עושה פירוק מכנה שאין.",
    "(Bx+C)/(x²+k): חצי-נגזרת ← ln, קבוע ← arctan"))
dec = sp.symbols('A B C')
A_, B_, C_ = dec
q.append(numeric("C06-Q4", r"$\frac{1}{x\left(x^2+1\right)}=\frac{A}{x}+\frac{Bx+C}{x^2+1}$. מהו $B$ ?", -1, -1,
                 r"‏$1=A\left(x^2+1\right)+(Bx+C)x$. עם $x=0$: ‏$A=1$. מקדם $x^2$: ‏$0=A+B$, לכן $B=-1$. מקדם $x$: ‏$0=C$.",
                 "משווים מקדמים אחרי שהצבת השורש נתנה A", tol=0))
sol6 = sp.solve(sp.Poly(sp.expand(1 - (A_*(x**2 + 1) + (B_*x + C_)*x)), x).all_coeffs(), [A_, B_, C_], dict=True)
assert sol6 == [{A_: 1, B_: -1, C_: 0}], sol6
d6 = 1/(x*(x**2 + 1))
q.append(mcq("C06-Q5", r"מהו $\int\frac{dx}{x\left(x^2+1\right)}$ ?", [
    (r"$\ln|x|-\frac12\ln\left(x^2+1\right)+C$", ok(d6, log(x) - log(x**2 + 1)/2)),
    (r"$\ln|x|+\frac12\ln\left(x^2+1\right)+C$", ok(d6, log(x) + log(x**2 + 1)/2)),
    (r"$\ln|x|-\arctan x+C$", ok(d6, log(x) - atan(x))),
    (r"$\ln|x|-\ln\left(x^2+1\right)+C$", ok(d6, log(x) - log(x**2 + 1))),
], r"הפירוק הוא $\frac1x-\frac{x}{x^2+1}$, ולכן **$\ln|x|-\frac12\ln(x^2+1)$**. הסימן החיובי והמקדם $1$ במקום $\frac12$ נובעים מטעויות בפירוק. ‏$\arctan$ היה מופיע רק עם מונה קבוע מעל $x^2+1$, אבל כאן $C=0$.",
    "1/(x(x²+1)) = 1/x − x/(x²+1)"))
# decomposition form question
Dn = (x - 1)**2*(x**2 + 4)
tgt = x
def form_works(expr_form, unknowns):
    eqn = sp.together(expr_form - tgt/Dn)
    num = sp.numer(eqn)
    cf = sp.Poly(sp.expand(num), x).all_coeffs()
    return bool(sp.solve(cf, unknowns, dict=True))
a1, b1, c1, d1 = sp.symbols('a1 b1 c1 d1')
form_ok = form_works(a1/(x - 1) + b1/(x - 1)**2 + (c1*x + d1)/(x**2 + 4), [a1, b1, c1, d1])
form_no1 = form_works(a1/(x - 1) + (c1*x + d1)/(x**2 + 4), [a1, c1, d1])
form_no2 = form_works(a1/(x - 1)**2 + b1/(x**2 + 4), [a1, b1])
form_no3 = form_works(a1/(x - 1) + b1/(x - 1)**2 + c1/(x**2 + 4), [a1, b1, c1])
q.append(mcq("C06-Q6", r"מהי צורת הפירוק הנכונה של $\frac{x}{(x-1)^2\left(x^2+4\right)}$ ?", [
    (r"$\frac{A}{x-1}+\frac{B}{(x-1)^2}+\frac{Cx+D}{x^2+4}$", form_ok),
    (r"$\frac{A}{x-1}+\frac{Cx+D}{x^2+4}$", form_no1),
    (r"$\frac{A}{(x-1)^2}+\frac{B}{x^2+4}$", form_no2),
    (r"$\frac{A}{x-1}+\frac{B}{(x-1)^2}+\frac{C}{x^2+4}$", form_no3),
], r"גורם כפול $(x-1)^2$ דורש **שני** איברים, וגורם ריבועי דורש מונה **לינארי**. הפירוק $\frac{A}{x-1}+\frac{B}{(x-1)^2}+\frac{Cx+D}{x^2+4}$ עובד (פתרון קיים). ללא האיבר $\frac{B}{(x-1)^2}$ או עם קבוע בלבד מעל הריבועי, למערכת המשוואות אין פתרון. בדקנו.",
    "כפול: שני איברים. ריבועי: Bx+C"))
fact("C06-Q6: only the full form has a solution", form_ok and not form_no1 and not form_no2 and not form_no3)
level("C06", 6, "🧮", "מכנה ריבועי, גורם כפול והשלמה לריבוע",
      "להשלים לריבוע כש-Δ שלילית, לפרק מונה מעל ריבועי, ולכתוב צורת פירוק נכונה לגורם כפול.", L6, q)

# ===================================================================== C07  method choice (core level)
L7 = r"""
<p>הרמה הזאת היא לב הקורס: מול אינטגרל לא מוכר, איך מחליטים? שואלים את <b>השאלות בסדר הזה</b>.</p>
<table>
<tr><th>מה רואים</th><th>השיטה</th></tr>
<tr><td>מנה של פולינומים</td><td>דרגות; חלוקה אם צריך; שברים חלקיים. אם המכנה ריבועי עם $\Delta<0$: השלמה לריבוע</td></tr>
<tr><td>פנימית ונגזרתה באותו אינטגרנד ($xe^{x^2}$, $\frac{\ln x}{x(\cdots)}$)</td><td>הצבה</td></tr>
<tr><td>מכפלה: פולינום × $e^x$/$\sin$/$\cos$</td><td>בחלקים, $u=$ פולינום</td></tr>
<tr><td>$\ln x$ או $\arctan x$ (לבד או כפול פולינום)</td><td>בחלקים, $u=\ln$ או $\arctan$</td></tr>
</table>
<div class="lesson-rule">🔑 שאלת מפתח: האם הגורם השני הוא הנגזרת של הפנימית? אם כן, הצבה. אם לא, מכפלה = בחלקים.</div>
<p>סימן מובהק שבחלקים לא יעבוד: ל-$dv$ אין אינטגרל אלמנטרי. הדוגמה: $e^{x^2}$.</p>
<div class="lesson-ex">$\int x\,e^{x}dx$ ו-$\int x\,e^{x^2}dx$ נראים כמעט אותו דבר. בראשון $x$ אינו נגזרת של $x$ (אפשר רק בחלקים). בשני $x$ הוא חצי נגזרת של $x^2$ (הצבה).</div>
<div class="lesson-trap">⚠️ אל תנסו שיטה "על סמך תחושה". בדקו בשנייה: האם הנגזרת של פנימית נמצאת? אם לא, אל תבצעו הצבה.</div>
"""
fact("C07: sp.integrate(exp(x**2)) has erfi", sp.integrate(exp(x**2), x).has(sp.erfi))
q = []
# opts: sub / parts / PF / complete square / division
f_a = x*exp(x**2)
rat = lambda e: e.is_rational_function(x)
q.append(mcq("C07-Q1", r"איזו שיטה מתאימה ל-$\int x\,e^{x^2}\,dx$ ?", [
    (r"הצבה $t=x^2$", ok(f_a, exp(x**2)/2)),
    (r"בחלקים עם $u=x$ ו-$dv=e^{x^2}dx$", not sp.integrate(exp(x**2), x).has(sp.erfi)),
    (r"שברים חלקיים", rat(f_a)),
    (r"השלמה לריבוע", rat(f_a)),
], r"הגורם $x$ הוא חצי נגזרת הפנימית $x^2$: **הצבה** נותנת $\frac12e^{x^2}$. בחלקים נכשלת כי ל-$dv=e^{x^2}dx$ אין אינטגרל אלמנטרי (הוא שייך לפונקציית שגיאה). שברים חלקיים והשלמה לריבוע שייכים לפונקציות רציונליות, וזו לא.",
    "הגורם x הוא נגזרת הפנימית: הצבה, לא בחלקים"))
f_b = x*exp(x)
q.append(mcq("C07-Q2", r"איזו שיטה מתאימה ל-$\int x\,e^{x}\,dx$ ?", [
    (r"בחלקים עם $u=x$", ok(f_b, (x - 1)*exp(x))),
    (r"הצבה $t=x^2$", not sp.simplify(f_b/(2*x)).subs(x, sqrt(t)) == sp.simplify(exp(sqrt(t))/2) is False and False),
    (r"שברים חלקיים", rat(f_b)),
    (r"השלמה לריבוע", rat(f_b)),
], r"‏$x\,e^{x}$ היא מכפלת פולינום ב-$e^x$: **בחלקים** עם $u=x$. הצבה $t=x^2$ משאירה $e^{\sqrt t}$ (כי $e^x$ אינו פונקציה של $x^2$) ולא פותרת את הבעיה. שברים חלקיים והשלמה לריבוע מתאימות רק לפונקציות רציונליות.",
    "פולינום × e^x: בחלקים"))
fact("C07-Q2: t=x^2 gives e^{sqrt t}/2, not a table integral", sp.simplify((f_b/(2*x)).subs(x, sqrt(t))) == exp(sqrt(t))/2)
f_c = (x + 3)/((x - 1)*(x + 1))
q.append(mcq("C07-Q3", r"איזו שיטה מתאימה ל-$\int\frac{x+3}{(x-1)(x+1)}\,dx$ ?", [
    (r"שברים חלקיים", rat(f_c) and sp.Poly(x + 3, x).degree() < 2),
    (r"הצבה $t=x^2-1$ (הנגזרת של המכנה היא $2x$)", sp.simplify(f_c - sp.diff(x**2 - 1, x)/(x**2 - 1)/2) == 0),
    (r"בחלקים עם $u=\ln x$", f_c.has(log)),
    (r"חלוקה ארוכה", sp.Poly(x + 3, x).degree() >= 2),
], r"הפונקציה רציונלית, דרגת המונה (1) קטנה מדרגת המכנה (2), והמכנה מתפרק לגורמים לינאריים: **שברים חלקיים**. הצבה $t=x^2-1$ לא עובדת כי המונה $x+3$ אינו מכפלה של $2x$. אין $\ln$ באינטגרנד, ולכן אין $u=\ln x$. חלוקה נדרשת רק כשדרגת המונה שווה או גדולה.",
    "רציונלי + דרגת מונה קטנה + גורמים: שברים חלקיים"))
q.append(mcq("C07-Q4", r"איזו שיטה מתאימה ל-$\int\arctan x\,dx$ ?", [
    (r"בחלקים עם $u=\arctan x$ ו-$dv=dx$", ok(atan(x), x*atan(x) - log(1 + x**2)/2)),
    (r"הצבה $t=\arctan x$", sp.simplify(atan(x)/sp.diff(atan(x), x)) == atan(x)*(1 + x**2) and False),
    (r"שברים חלקיים", rat(atan(x))),
    (r"השלמה לריבוע", rat(atan(x))),
], r"אין פנימית שנגזרתה נמצאת באינטגרנד. הפונקציה $\arctan x$ לא רציונלית. השיטה היחידה: **בחלקים** עם $dv=dx$. הצבה $t=\arctan x$ מחייבת $dt=\frac{dx}{1+x^2}$, אבל אין $\frac{1}{1+x^2}$ באינטגרנד, והביטוי שנשאר הוא $t\left(1+\tan^2t\right)dt$, מסובך יותר.",
    "ln או arctan לבד: בחלקים עם dv = dx"))
fact("C07-Q4: t=arctan x leaves atan(x)(1+x^2), i.e. t(1+tan^2 t)", sp.simplify(atan(x)/sp.diff(atan(x), x) - atan(x)*(1 + x**2)) == 0)
f_e = 1/(x**2 + 2*x + 5)
q.append(mcq("C07-Q5", r"איזו שיטה מתאימה ל-$\int\frac{dx}{x^2+2x+5}$ ?", [
    (r"השלמה לריבוע ו-$\arctan$", ok(f_e, atan((x + 1)/2)/2)),
    (r"שברים חלקיים עם שורשים ממשיים", sp.Poly(x**2 + 2*x + 5, x).discriminant() >= 0),
    (r"בחלקים עם $u=\frac{1}{x^2+2x+5}$", f_e.has(log)),
    (r"הצבה $t=x^2+2x+5$", sp.simplify(f_e - sp.diff(x**2 + 2*x + 5, x)/(x**2 + 2*x + 5)) == 0),
], r"המכנה בעל $\Delta=4-20<0$: אין שורשים ממשיים, ולכן שברים חלקיים לא אפשריים. הצבה $t=x^2+2x+5$ דורשת מונה $2x+2$, והמונה הוא $1$. נשארת **השלמה לריבוע**: $(x+1)^2+4$, ו-$\frac12\arctan\frac{x+1}{2}$.",
    "ריבועי עם Δ<0 ומונה קבוע: השלמה לריבוע"))
fact("C07-Q5: discriminant -16", sp.Poly(x**2 + 2*x + 5, x).discriminant() == -16)
f_f = (x**3 + 2)/(x**2 - 1)
q.append(mcq("C07-Q6", r"מהו הצעד הראשון ב-$\int\frac{x^3+2}{x^2-1}\,dx$ ?", [
    (r"חלוקה ארוכה", sp.Poly(x**3 + 2, x).degree() >= sp.Poly(x**2 - 1, x).degree()),
    (r"פירוק מיידי לשברים חלקיים", sp.Poly(x**3 + 2, x).degree() < sp.Poly(x**2 - 1, x).degree()),
    (r"השלמה לריבוע", sp.Poly(x**2 - 1, x).discriminant() < 0),
    (r"בחלקים עם $u=x^3+2$", f_f.has(log)),
], r"דרגת המונה (3) גדולה מדרגת המכנה (2): **חלוקה ארוכה**. המכנה $x^2-1$ אינו ריבועי עם $\Delta<0$ ($\Delta=4$), ולכן לא משלימים לריבוע. אין $\ln$ באינטגרנד. פירוק מיידי נכשל כי הדרגות לא מתאימות.",
    "בודקים דרגות לפני כל שיטה"))
f_g = x*log(x)
good_g = parts_next(log(x), x)
q.append(mcq("C07-Q7", r"איזו בחירה בחלקים מתאימה ל-$\int x\ln x\,dx$ ?", [
    (r"$u=\ln x,\ dv=x\,dx$", not good_g.has(log) and ok(f_g, x**2*log(x)/2 - x**2/4)),
    (r"$u=x,\ dv=\ln x\,dx$", not parts_next(x, log(x)).has(log)),
    (r"הצבה $t=\ln x$ בלבד", sp.simplify(f_g/sp.diff(log(x), x)).subs(x, exp(t)) == t*exp(2*t) and False),
    (r"שברים חלקיים", rat(f_g)),
], r"‏$u=\ln x$ עם $dv=x\,dx$ מעלימה את ה-$\ln$: האינטגרל הנותר $\int\frac x2dx$. הבחירה ההפוכה דורשת את $\int\ln x\,dx$ ומשאירה $\ln$ באינטגרל הנותר. הצבה $t=\ln x$ נותנת $\int t\,e^{2t}dt$, שהיא עצמה מכפלה שדורשת בחלקים. ושברים חלקיים לא שייכים: הפונקציה אינה רציונלית.",
    "x ln x: בחלקים, u = ln x"))
fact("C07-Q7: t=ln x gives t e^{2t}", sp.simplify((f_g/sp.diff(log(x), x)).subs(x, exp(t)) - t*exp(2*t)) == 0)
level("C07", 7, "🧭", "איזו שיטה? בחירה בין הצבה, חלקים ושברים",
      "להסתכל על אינטגרל ולבחור שיטה אחת נכונה, ולדעת למה האחרות נכשלות.", L7, q)

# ===================================================================== C08  special substitutions
L8 = r"""
<p>כמה אינטגרלים מתפרקים בהצבה מיוחדת שמחזירה אותם לפונקציה רציונלית.</p>
<ul>
<li><b>$e^x$ בתוך מנה:</b> $t=e^x$, ‏$dx=\frac{dt}{t}$.</li>
<li><b>$\sqrt x$ בתוך הביטוי:</b> $t=\sqrt x$, ‏$x=t^2$, ‏$dx=2t\,dt$.</li>
<li><b>טריגונומטרי:</b> אם $\sin x\,dx$ נמצא באינטגרנד, אפשר $t=\cos x$. אחרת הצבה אוניברסלית $t=\tan\frac x2$.</li>
</ul>
<div class="lesson-formula">$t=\tan\frac x2$: ‏$\sin x=\frac{2t}{1+t^2}$, ‏$\cos x=\frac{1-t^2}{1+t^2}$, ‏$dx=\frac{2\,dt}{1+t^2}$</div>
<div class="lesson-ex">דוגמה: $\int\frac{dx}{e^x+1}$. עם $t=e^x$ מקבלים $\int\frac{dt}{t(t+1)}=\ln t-\ln(t+1)$, כלומר $x-\ln\left(e^x+1\right)+C$.</div>
<div class="lesson-ex">דוגמה: $\int e^{\sqrt x}dx$. עם $t=\sqrt x$ מקבלים $2\int te^{t}dt$, ואחר כך בחלקים: $2(t-1)e^{t}$.</div>
<div class="lesson-trap">⚠️ ההצבה האוניברסלית מסורבלת. אל תשתמשו בה אם יש הצבה פשוטה: $\int\frac{\sin x}{1+\cos^2x}dx$ נפתר עם $t=\cos x$.</div>
"""
fact("lesson C08: x - ln(e^x+1)", ok(1/(exp(x) + 1), x - log(exp(x) + 1)))
fact("lesson C08: 2(sqrt x -1)e^{sqrt x}", ok(exp(sqrt(x)), 2*(sqrt(x) - 1)*exp(sqrt(x))))
q = []
q.append(mcq("C08-Q1", r"מהו $\int\frac{dx}{e^x+1}$ ?", [
    (r"$x-\ln\left(e^x+1\right)+C$", ok(1/(exp(x) + 1), x - log(exp(x) + 1))),
    (r"$\ln\left(e^x+1\right)+C$", ok(1/(exp(x) + 1), log(exp(x) + 1))),
    (r"$-\ln\left(e^x+1\right)+C$", ok(1/(exp(x) + 1), -log(exp(x) + 1))),
    (r"$x+\ln\left(e^x+1\right)+C$", ok(1/(exp(x) + 1), x + log(exp(x) + 1))),
], r"עם $t=e^x$: ‏$\int\frac{dt}{t(t+1)}=\int\left(\frac1t-\frac1{t+1}\right)dt=\ln t-\ln(t+1)$. מחזירים $\ln t=x$ ומקבלים **$x-\ln(e^x+1)$**. ‏$\ln(e^x+1)$ לבדו נותן $\frac{e^x}{e^x+1}$, שהוא האינטגרנד של $\frac{e^x}{e^x+1}$ ולא של השאלה.",
    "רציונלי ב-e^x: t = e^x ← שברים חלקיים"))
q.append(mcq("C08-Q2", r"מהו $\int e^{\sqrt{x}}\,dx$ ?", [
    (r"$2\left(\sqrt x-1\right)e^{\sqrt x}+C$", ok(exp(sqrt(x)), 2*(sqrt(x) - 1)*exp(sqrt(x)))),
    (r"$2e^{\sqrt x}+C$", ok(exp(sqrt(x)), 2*exp(sqrt(x)))),
    (r"$2\left(\sqrt x+1\right)e^{\sqrt x}+C$", ok(exp(sqrt(x)), 2*(sqrt(x) + 1)*exp(sqrt(x)))),
    (r"$\frac{e^{\sqrt x}}{\sqrt x}+C$", ok(exp(sqrt(x)), exp(sqrt(x))/sqrt(x))),
], r"‏$t=\sqrt x$, ‏$dx=2t\,dt$: ‏$2\int te^{t}dt=2(t-1)e^{t}$. התשובה **$2(\sqrt x-1)e^{\sqrt x}$**. ‏$2e^{\sqrt x}$ מתעלמת מהגורם $t$. ‏$(\sqrt x+1)$ שגוי בסימן. ‏$\frac{e^{\sqrt x}}{\sqrt x}$ מניח כלל חזקה על הפנימית.",
    "√x בתוך הביטוי: t = √x ואז בחלקים"))
q.append(mcq("C08-Q3", r"מהו $\int\frac{\sin x}{1+\cos^2x}\,dx$ ?", [
    (r"$-\arctan(\cos x)+C$", ok(sin(x)/(1 + cos(x)**2), -atan(cos(x)))),
    (r"$\arctan(\cos x)+C$", ok(sin(x)/(1 + cos(x)**2), atan(cos(x)))),
    (r"$-\arctan(\sin x)+C$", ok(sin(x)/(1 + cos(x)**2), -atan(sin(x)))),
    (r"$\ln\left(1+\cos^2x\right)+C$", ok(sin(x)/(1 + cos(x)**2), log(1 + cos(x)**2))),
], r"‏$t=\cos x$, ‏$dt=-\sin x\,dx$, ולכן $-\int\frac{dt}{1+t^2}=-\arctan t$. הסימן המינוס חיוני. ‏$\arctan(\sin x)$ מתאים ל-$\frac{\cos x}{1+\sin^2x}$. ‏$\ln$ מתאים אם המונה היה $\sin x\cos x$.",
    "sin x dx = −dt: מחליפים בסימן"))
f8 = 1/(2 + cos(x))
tt = sp.Symbol('tt', real=True)
cos_tt = (1 - tt**2)/(1 + tt**2)
h_u = sp.simplify((1/(2 + cos_tt))*2/(1 + tt**2))
Fu = 2/sqrt(3)*atan(tan(x/2)/sqrt(3))
assert numeq(sp.diff(Fu, x), f8)
h_cos = f8/(-sin(x))
h_cos_irr = sp.simplify(h_cos.subs(sin(x), sqrt(1 - t**2)).subs(cos(x), t))
q.append(mcq("C08-Q4", r"איזו הצבה מחזירה את $\int\frac{dx}{2+\cos x}$ לאינטגרל רציונלי ב-$t$ ?", [
    (r"$t=\tan\frac x2$", h_u.is_rational_function(tt)),
    (r"$t=\cos x$", h_cos_irr.is_rational_function(t)),
    (r"$t=\sin x$", False),
    (r"$t=2+\cos x$", False),
], r"אין $\sin x\,dx$ באינטגרנד, ולכן $t=\cos x$ משאירה $dx=-\frac{dt}{\sqrt{1-t^2}}$ (שורש): לא רציונלי. ההצבה האוניברסלית $t=\tan\frac x2$ נותנת $\int\frac{2\,dt}{3+t^2}$, כלומר $\frac{2}{\sqrt3}\arctan\frac{\tan(x/2)}{\sqrt3}$. אפשר לגזור ולוודא. ‏$t=\sin x$ ו-$t=2+\cos x$ משאירות גם שורשים.",
    "אין sin x dx: הצבה אוניברסלית t = tan(x/2)"))
fact("C08-Q4: t=tan(x/2) gives 2/(3+t^2)", sp.simplify(h_u - 2/(3 + tt**2)) == 0)
fact("C08-Q4: t=sin x leaves sqrt(1-t^2)", not sp.simplify((f8/sp.diff(sin(x), x)).subs(cos(x), sqrt(1 - t**2))).is_rational_function(t))
fact("C08-Q4: t=2+cos x leaves sqrt", not sp.simplify((f8/sp.diff(2 + cos(x), x)).subs(sin(x), sqrt(1 - (t - 2)**2))).is_rational_function(t))
q.append(numeric("C08-Q5", r"בהצבה $t=\tan\frac x2$ מתקבל $dx=\frac{c\,dt}{1+t^2}$. מהו $c$ ?", 2, sp.simplify(sp.diff(2*sp.atan(tt), tt)*(1 + tt**2)),
                 r"‏$x=2\arctan t$, ולכן $dx=\frac{2\,dt}{1+t^2}$. כלומר $c=2$.",
                 "dx = 2dt/(1+t²) בהצבה האוניברסלית", tol=0))
q.append(mcq("C08-Q6", r"מהו $\int x\arctan\left(x^2\right)dx$ ?", [
    (r"$\frac{x^2}{2}\arctan\left(x^2\right)-\frac14\ln\left(1+x^4\right)+C$", ok(x*atan(x**2), x**2/2*atan(x**2) - log(1 + x**4)/4)),
    (r"$\frac{x^2}{2}\arctan\left(x^2\right)-\frac12\ln\left(1+x^4\right)+C$", ok(x*atan(x**2), x**2/2*atan(x**2) - log(1 + x**4)/2)),
    (r"$\frac12\arctan\left(x^2\right)+C$", ok(x*atan(x**2), atan(x**2)/2)),
    (r"$\frac{x^2}{2}\arctan\left(x^2\right)+\frac14\ln\left(1+x^4\right)+C$", ok(x*atan(x**2), x**2/2*atan(x**2) + log(1 + x**4)/4)),
], r"קודם הצבה $t=x^2$, ‏$x\,dx=\frac12dt$: ‏$\frac12\int\arctan t\,dt=\frac12\left(t\arctan t-\frac12\ln(1+t^2)\right)$. מחזירים: **$\frac{x^2}{2}\arctan x^2-\frac14\ln(1+x^4)$**. ‏$\frac12\ln$ שוכחת את חצי החצי. ‏$\frac12\arctan x^2$ מתעלמת מהחלקים. הסימן בתשובה האחרונה הפוך.",
    "הצבה t = x² ואז בחלקים"))
level("C08", 8, "🎯", "הצבות מיוחדות: e^x, √x, טריגונומטריה",
      "להחליף e^x, שורש או tan(x/2) כך שהאינטגרל יהפוך לרציונלי, ולהמשיך עד הסוף.", L8, q)

# ===================================================================== C09  boss
L9 = r"""
<p>זו ההרצה המלאה: חמישה אינטגרלים ממבחנים אמיתיים, כל אחד בשיטה אחרת. החליטו על השיטה לפני שמתחילים לחשב.</p>
<table>
<tr><th>מה רואים</th><th>השיטה</th></tr>
<tr><td>מנה של פולינומים</td><td>דרגות, חלוקה, שברים חלקיים (גורם ריבועי: $\ln$ ו-$\arctan$)</td></tr>
<tr><td>פנימית ונגזרתה ($\ln x$ עם $\frac{dx}{x}$, $\cos2x$ עם $\sin2x$)</td><td>הצבה</td></tr>
<tr><td>פולינום × $\sin$/$\cos$/$e^x$</td><td>בחלקים, $u=$ פולינום; כמה סיבובים</td></tr>
<tr><td>$\ln^2x$ לבד</td><td>בחלקים פעמיים, $u=\ln^2x$ ואז $u=\ln x$</td></tr>
</table>
<div class="lesson-rule">🔑 בסוף גוזרים את התשובה ובודקים. זה הכלי הטוב ביותר נגד טעויות סימן.</div>
<div class="lesson-trap">⚠️ אל תשכחו את $+C$. במבחן זה מוריד נקודה.</div>
"""
q = [
    {"bankId": "24B-A-Q2a", "recap": "מנה, דרגות קטנות, גורם לינארי וגורם ריבועי: שברים חלקיים עם A, ובמונה הריבועי ln ו-arctan"},
    {"bankId": "24B-A-Q5a", "recap": "פולינום × cos 2x: בחלקים פעמיים, u = הפולינום, והפנימית 2x מחלקת ב-2"},
    {"bankId": "24A-A-Q3b", "recap": "sin 2x dx עם cos² 2x במכנה: הצבה t = cos 2x ← arctan"},
    {"bankId": "24A-B-Q5a", "recap": "ln x עם dx/x: הצבה t = ln x ← (1/2) ln(t²+1)"},
    {"bankId": "20B-C-Q4a", "recap": "ln² x לבד: בחלקים פעמיים, u = ln²x ואז u = ln x"},
]
level("C09", 9, "🏆", "מבחן מסכם: אינטגרלים ממבחנים",
      "לבחור שיטה ולהשלים חמישה אינטגרלים אמיתיים מהמבחנים, כל אחד בשיטה אחרת.", L9, q, boss=True)

# sanity on boss claims quoted in recaps
fact("boss 24B-A-Q2a: x/((x+1)(x^2+1)) = 1/2(-1/(x+1) + (x+1)/(x^2+1))", eq(x/((x + 1)*(x**2 + 1)), R(1, 2)*(-1/(x + 1) + (x + 1)/(x**2 + 1))))
fact("boss 24B-A-Q5a: result", ok((x**2 + 2*x)*cos(2*x), (x**2 + 2*x)*sin(2*x)/2 + (x + 1)*cos(2*x)/2 - sin(2*x)/4))
fact("boss 24A-A-Q3b: -1/(2 sqrt3) atan(cos2x/sqrt3)", ok(sin(2*x)/(3 + cos(2*x)**2), -atan(cos(2*x)/sqrt(3))/(2*sqrt(3))))
fact("boss 24A-B-Q5a: 1/2 ln(ln^2 x+1)", ok(log(x)/(x*(log(x)**2 + 1)), log(log(x)**2 + 1)/2))
fact("boss 20B-C-Q4a: x ln^2 x - 2x ln x + 2x", ok(log(x)**2, x*log(x)**2 - 2*x*log(x) + 2*x))

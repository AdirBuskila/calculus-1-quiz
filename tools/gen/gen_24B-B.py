# -*- coding: utf-8 -*-
"""Generator for tools/raw/24B-B.json -- calculus-1 (20151), semester B 2024, moed B (12/08/2024), flagship sitting.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24B-B.py

Source: sitting 24B-B, pp.1-6 (typed exam with the official worked solution after each "פתרון" label).
Part A (mandatory): Q1. Part B: choose 4 of Q2-Q6 (a/b parts, 10% each). Weight of every question 20%.

Transcription notes
- Q1 is kept as ONE item: the printed question is a single instruction list; the official solution is the
  sequence of sections a-f. Its two figures (graph of f on p.2, the plot in Q6b on p.6) belong to the official
  solution and the raw schema has no solution-image field, so they are described in words, not shipped.
- Q3a: the solution sits on p.4 (the p.3 "פתרון" label is followed by a page break).
- Q2b: the official text solves L(L-1)=0 after clearing denominators; transcribed as printed.

Checks (tools/verify/24B-B/check.py, sympy): every derivative, limit, integral, extremum value, the area and the
volume match the official answers. 0 mismatches. No code in this sitting.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24B-B.json"


def Q(num, kind, topic, question, solution, part=None, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution.strip("\n"),
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    if part:
        q["part"] = part
    q.update(kw)
    return q


SOL1 = r"""
**א. תחום הגדרה:** $D=\{x\in\mathbb{R}: x\neq \pm 1\}$.
**ב. נקודות חיתוך עם צירי הקואורדינטות:** $(0,0)$.
**ג. נגזרת:** $y'=\frac{x^2(x^2-3)}{(x^2-1)^2}$, ומכאן רואים שהנגזרת מתאפסת ב-$x=0,\pm\sqrt{3}$ ובנוסף $y'>0$ כאשר $x<-\sqrt{3}$ או $x>\sqrt{3}$, וגם $y'<0$ כאשר $-\sqrt{3}<x<-1$ או $-1<x<1$ או $1<x<\sqrt{3}$.
**ד. קיצון:** $x_{min}=\sqrt{3}$ הנקודה היא נקודת מינימום מקומי, $y(x_{min})=\frac{\sqrt{27}}{2}$; $x_{max}=-\sqrt{3}$ הנקודה היא נקודת מקסימום מקומי, $y(x_{max})=\frac{-\sqrt{27}}{2}$.
**ה. נגזרת שנייה:** $y''=\frac{2x(x^2+3)}{(x^2-1)^3}$. הנקודה $(0,0)$ היא נקודת פיתול. בנוסף, $y''>0$ עבור $x>1$ או $-1<x<0$, הפונקציה קמורה (כלפי מעלה, $\\cup$); $y''<0$ עבור $x<-1$ או $0<x<1$, הפונקציה קעורה (כלפי מטה, $\\cap$).
**ו. אסימפטוטות:** קווים ישרים $x=\pm 1$ מהווים אסימפטוטות אנכיות לגרף הפונקציה, כי
$$\lim_{x\to -1^-}\frac{x^3}{x^2-1}=-\infty,\quad \lim_{x\to -1^+}\frac{x^3}{x^2-1}=+\infty,\quad \lim_{x\to 1^-}\frac{x^3}{x^2-1}=-\infty,\quad \lim_{x\to 1^+}\frac{x^3}{x^2-1}=+\infty$$
$$a=\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim_{x\to\pm\infty}\frac{x^3}{x(x^2-1)}=1$$
$$b=\lim_{x\to\pm\infty}(f(x)-x)=\lim_{x\to\pm\infty}\left(\frac{x^3}{x^2-1}-x\right)=\lim_{x\to\pm\infty}\left(\frac{x}{x^2-1}\right)=0$$
לכן הישר $y=x$ הוא האסימפטוטה המשופעת של הפונקציה. השרטוט הרשמי מציג את הגרף יחד עם האסימפטוטות $x=\pm1$ ו-$y=x$.
"""

SOL2A = r"""
כיוון ש-$\frac{x^2+8}{x^4+4x^2}=\frac{x^2+8}{x^2(x^2+4)}$ קיימים $A,B,C,D\in\mathbb{R}$ כך ש:
$$\frac{x^2+8}{x^2(x^2+4)}=\frac{A}{x}+\frac{B}{x^2}+\frac{Cx+D}{x^2+4}.$$
על-ידי השוואת מקדמים או הצבת ערכים ב-$x$, מקבלים ש-$A=C=0$, $B=2$ ו-$D=-1$. לכן
$$\int\frac{x^2+8}{x^2(x^2+4)}dx=\int\frac{2}{x^2}dx-\int\frac{1}{x^2+4}dx=-\frac{2}{x}-\frac{1}{2}\arctan\frac{x}{2}+c,\qquad c\in\mathbb{R}$$
"""

SOL2B = r"""
ראשית, נוכיח באינדוקציה שהסדרה יורדת. נשים לב שאכן $a_2=\frac{6}{5}\le 2=a_1$. יהא $n\in\mathbb{N}$, ונניח ש-$a_{n+1}\le a_n$ מתקיים. אז
$$a_{n+2}=\frac{3}{2+\frac{1}{a_{n+1}}}\le\frac{3}{2+\frac{1}{a_n}}=a_{n+1}.$$
לכן, לפי עקרון האינדוקציה, $a_{n+1}\le a_n$ לכל $n\in\mathbb{N}$.
כעת נוכיח באינדוקציה שהסדרה חסומה מלרע (מלמטה) על-ידי $1$. נשים לב שאכן $a_1=2\ge 1$. יהא $n\in\mathbb{N}$, ונניח ש-$a_n\ge 1$ מתקיים. אז כיוון שפונקציית השורש עולה מתקיים
$$a_{n+1}=\frac{3}{2+\frac{1}{a_n}}\ge\frac{3}{2+\frac{1}{1}}=1.$$
לכן, לפי עקרון האינדוקציה, $a_n\ge 1$ לכל $n\in\mathbb{N}$.
לפיכך, הסדרה יורדת וחסומה מלרע, ולכן, לפי משפט, מתכנסת. נסמן $L=\lim_{n\to\infty}a_n$. אז גם $\lim_{n\to\infty}a_{n+1}=L$. מאריתמטיקה של גבולות מתקיים
$$L=\lim_{n\to\infty}a_{n+1}=\lim_{n\to\infty}\frac{3}{2+\frac{1}{a_n}}=\frac{3}{2+\frac{1}{L}},$$
כלומר $L^2-L=0$ ולכן $L(L-1)=0$. אבל כיוון שהסדרה חסומה מלרע על-ידי $1$, גם גבולה חסום מלרע על-ידי $1$, ולכן לא ייתכן שגבולה הוא $0$. מכאן שגבול הסדרה הוא $1$.
"""

SOL3A = r"""
$$\lim_{n\to\infty}\left(\sqrt{1+n+n^2}-\sqrt{1-2n+n^2}\right)=\lim_{n\to\infty}\frac{\left(\sqrt{1+n+n^2}-\sqrt{1-2n+n^2}\right)\left(\sqrt{1+n+n^2}+\sqrt{1-2n+n^2}\right)}{\sqrt{1+n+n^2}+\sqrt{1-2n+n^2}}$$
$$=\lim_{n\to\infty}\frac{1+n+n^2-(1-2n+n^2)}{\sqrt{1+n+n^2}+\sqrt{1-2n+n^2}}=\lim_{n\to\infty}\frac{3n}{\sqrt{1+n+n^2}+\sqrt{1-2n+n^2}}$$
$$=\lim_{n\to\infty}\frac{3}{\sqrt{\frac{1}{n^2}+\frac{1}{n}+1}+\sqrt{\frac{1}{n^2}-\frac{2}{n}+1}}=\frac{3}{2}.$$
"""

SOL3B = r"""
שיטת קליפות:
$$V=2\pi\int_0^1 x\left(e+1-(e^x+1)\right)dx=2\pi\int_0^1 x\left(e-e^x\right)dx=2\pi\left(e\int_0^1 x\,dx-\int_0^1 xe^x\,dx\right)$$
באינטגרציה בחלקים, עם $u=x,\ v'=e^x,\ du=dx,\ v=e^x$:
$$=2\pi\left(e\frac{x^2}{2}\Big|_0^1-\left(xe^x\Big|_0^1-\int_0^1 e^x\,dx\right)\right)=2\pi\left(\frac{1}{2}e-e+e^x\Big|_0^1\right)=2\pi\left(\frac{e}{2}-1\right)$$
"""

SOL4A = r"""
$$y'=2(\ln x)\cdot\frac{1}{x}-\frac{2}{x}=0$$
$$\frac{2}{x}(\ln x-1)=0,\quad x=e$$
$$y(\sqrt{e})=-0.75,\quad y(e)=-1,\quad y(e^2)=0$$
$$y_{max}=y(e^2)=0,\quad y_{min}=y(e)=-1$$
"""

SOL4B = r"""
$$\lim_{x\to+\infty}\left(\frac{3x^4}{x^3+2x+9}-ax-b\right)=\lim_{x\to+\infty}\frac{3x^4-ax^4-2ax^2-9ax}{x^3+2x+9}-b=0$$
לקיום גבול נדרש $a=3$, אז מקבלים:
$$\lim_{x\to+\infty}\frac{-6x^2-27x}{x^3+2x+9}=b\ \Longrightarrow\ b=0$$
אז התשובה היא $a=3,\ b=0$.
"""

SOL5A = r"""
ראשית, נחשב גבולות חד צדדיים בנקודות התפר:
$$\lim_{x\to-2^-}f(x)=\lim_{x\to-2^-}e^{\frac{-x|x+2|}{(x+2)^2}}\to e^{+\infty}=+\infty$$
$$\lim_{x\to-2^+}f(x)=\lim_{x\to-2^+}(x+3)=1$$
**סיכום:** $x=-2$ היא נקודת אי רציפות מסוג שני.
$$\lim_{x\to0^-}f(x)=\lim_{x\to0^-}(x+3)=3$$
$$\lim_{x\to0^+}f(x)=\lim_{x\to0^+}\arctan\left(\frac{1}{x}\right)\to\arctan(+\infty)=\frac{\pi}{2}$$
**סיכום:** $x=0$ היא נקודת אי רציפות מסוג ראשון (קפיצה סופית).
"""

SOL5B = r"""
$$\int x\cos(x^2)\,dx=\left|\begin{matrix}t=x^2\\dt=2x\,dx\end{matrix}\right|=\frac{1}{2}\int\cos(t)\,dt=\frac{1}{2}\sin(t)+C=\frac{1}{2}\sin(x^2)+C$$
"""

SOL6A = r"""
נגדיר פונקציית עזר: $f(x)=e^x-x-1$. הפונקציה גזירה. נגזור ונקבל: $f'(x)=e^x-1$. מתקיים: $f'(0)=0$. כמו כן $f''(x)=e^x$ ולכן $f''(0)=e^0=1>0$. לכן $x=0$ היא נקודת מינימום מקומי. $f(0)=0$ ולכן הפונקציה מקיימת לכל $x$ כי $f(x)=e^x-x-1\ge f(0)=0$. מכאן: $e^x-x-1\ge 0\Rightarrow e^x\ge x+1$.
"""

SOL6B = r"""
הפונקציות $y=x,\ y=\frac{1}{x}$ נחתכות ב-$x=\pm1$. אבל ברביע הראשון זה ב-$x=1$.
השטח המבוקש מורכב ממשולש ישר זוית שנסמן ב-$S_1$, שקדקדיו: $(1,1),(4,4),(1,4)$. שטחו הוא $\frac{9}{2}$.
שטח נוסף שצריך לחשב הוא השטח בין $y=4$, הפונקציה $y=\frac{1}{x}$ ו-$x=1$. נסמן אותו ב-$S_2$. נסמן ב-$S_4$ את המלבן שקדקודיו הם: $(0,1),(1,1),(1,4),(0,4)$. מקבלים:
$$S_2=S_4-S_3=3-\int_1^4\frac{1}{y}\,dy=3-\ln 4.$$
בסה"כ: $S=S_1+S_2=\frac{15}{2}-\ln 4$.
"""

questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=\frac{x^3}{x^2-1}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, "
      "תחומי עליה וירידה, נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.",
      SOL1, points=20),

    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int \frac{x^2+8}{x^4+4x^2}\,dx$.",
      SOL2A, part="א", points=10),

    Q(2, "proof", "sequences_limits",
      "נתונה הסדרה:\n" r"$$a_{n+1}=\frac{3}{2+\frac{1}{a_n}},\quad a_1=2$$" "\nהוכיחו כי הסדרה מתכנסת וחשבו את הגבול של הסדרה.",
      SOL2B, part="ב", points=10),

    Q(3, "computation", "sequences_limits",
      r"חשבו את הגבול הבא: $\lim_{n\to\infty}\left(\sqrt{1+n+n^2}-\sqrt{1-2n+n^2}\right)$.",
      SOL3A, part="א", points=10),

    Q(3, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר מסיבוב התחום המישורי הכלוא בין הקווים: $y=e^x+1,\ y=e+1,\ x=0$ סביב ציר ה-$Y$.",
      SOL3B, part="ב", points=10),

    Q(4, "computation", "extrema_optimization",
      r"מצאו את הערך המקסימלי ואת הערך המינימלי של הפונקציה: $y=\ln^2 x-2\ln x$, בקטע הסגור $[\sqrt{e},e^2]$.",
      SOL4A, part="א", points=10),

    Q(4, "computation", "function_limits",
      r"מצאו לאלו ערכים של $a,b$ (ממשיים) מתקיים: $\lim_{x\to+\infty}\left(\frac{3x^4}{x^3+2x+9}-ax-b\right)=0$.",
      SOL4B, part="ב", points=10),

    Q(5, "computation", "continuity",
      r"נתונה הפונקציה: $f(x)=\begin{cases} e^{\frac{-x|x+2|}{(x+2)^2}} & x<-2\\ x+3 & -2\le x\le 0\\ \arctan\left(\frac{1}{x}\right) & x>0\end{cases}$"
      "\nמצאו את נקודות אי הרציפות שלה, וציינו את סוג אי הרציפות בנקודה.",
      SOL5A, part="א", points=10),

    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int x\cdot\cos(x^2)\,dx$.",
      SOL5B, part="ב", points=10),

    Q(6, "proof", "extrema_optimization",
      r"הוכיחו כי לכל $x$ ממשי מתקיים אי השוויון $e^x\ge x+1$.",
      SOL6A, part="א", points=10),

    Q(6, "computation", "definite_integrals",
      r"מצאו את השטח התחום החסום בין הגרפים של הפונקציות: $y=\frac{1}{x},\ y=x,\ y=4$.",
      SOL6B, part="ב", points=10),
]

# ---- rubric / pitfalls / steps (ai-draft); every expected value is re-derived by sympy in tools/verify/24B-B/check.py ----
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def add(num, part, **kw):
    for q in questions:
        if q["num"] == num and q.get("part") == part:
            q.update(kw)
            return
    raise KeyError((num, part))


# Q1 -- function investigation
add(1, None,
    rubric=rub(("תחום הגדרה ונקודות חיתוך עם הצירים", 3),
               ("נגזרת ראשונה, תחומי עליה וירידה ונקודות קיצון עם ערכיהן", 5),
               ("נגזרת שנייה, קמירות וקעירות ונקודת הפיתול", 4),
               ("אסימפטוטות אנכיות (גבולות חד-צדדיים) ואסימפטוטה משופעת (חישוב $a$ ו-$b$)", 6),
               ("שרטוט הגרף בהתאם לכל הנתונים", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח שהנקודות $x=\\pm 1$ מחוץ לתחום ההגדרה, ולכן הן אינן קיצון אלא אסימפטוטות אנכיות.",
              "לקבוע קיצון רק לפי $f'(x)=0$ בלי לבדוק את סימן הנגזרת: ב-$x=0$ הנגזרת מתאפסת אך אין שם קיצון (שם נקודת פיתול).",
              "לחשב אסימפטוטה משופעת בלי לחשב את $b=\\lim(f(x)-ax)$, או לשכוח לבדוק את שני הכיוונים $x\\to\\pm\\infty$."],
    steps=[
        {"type": "choice", "prompt": r"באילו נקודות מתאפסת הנגזרת $f'(x)=\frac{x^2(x^2-3)}{(x^2-1)^2}$?",
         "options": opts(r"$x=0,\ \pm\sqrt{3}$", r"$x=\pm\sqrt{3}$ בלבד", r"$x=0,\ \pm 1$", r"$x=\pm 1$"), "correctId": "a",
         "explain": r"המונה $x^2(x^2-3)$ מתאפס ב-$x=0$ וב-$x=\pm\sqrt{3}$. הנקודות $\pm1$ מאפסות את המכנה ולכן אינן בתחום."},
        {"type": "numeric", "prompt": r"מהו הערך $f(\sqrt{3})$ (מינימום מקומי)? עגלו לשלוש ספרות אחרי הנקודה.",
         "answer": 2.598, "tol": 0.001,
         "explain": r"$f(\sqrt{3})=\frac{3\sqrt{3}}{2}=\frac{\sqrt{27}}{2}\approx 2.598$."},
        {"type": "choice", "prompt": r"נתון $f''(x)=\frac{2x(x^2+3)}{(x^2-1)^3}$. מה אופי הפונקציה בקטע $(0,1)$?",
         "options": opts("קעורה (כלפי מטה, $\\cap$)", "קמורה (כלפי מעלה, $\\cup$)", "ישרה", "אין מספיק נתונים"), "correctId": "a",
         "explain": r"ב-$(0,1)$ המונה חיובי והמכנה $(x^2-1)^3$ שלילי, לכן $f''<0$ והפונקציה קעורה ($\\cap$)."},
        {"type": "numeric", "prompt": r"מהו שיפוע האסימפטוטה המשופעת, $a=\lim_{x\to\infty}\frac{f(x)}{x}$?",
         "answer": 1, "tol": 0,
         "explain": r"$\frac{f(x)}{x}=\frac{x^2}{x^2-1}\to 1$, ואז $b=\lim(f(x)-x)=0$ ולכן $y=x$."},
        {"type": "order", "prompt": "סדרו את שלבי החקירה לפי סדר הפתרון הרשמי.",
         "lines": [r"תחום הגדרה: $x\neq\pm1$",
                   r"נקודות חיתוך עם הצירים: $(0,0)$",
                   r"נגזרת ראשונה וקיצון: מינימום ב-$x=\sqrt{3}$ ומקסימום ב-$x=-\sqrt{3}$",
                   r"נגזרת שנייה, קמירות ופיתול: נקודת פיתול ב-$(0,0)$",
                   r"אסימפטוטות: $x=\pm1$ ו-$y=x$"],
         "explain": "הסדר הוא סדר הסעיפים א-ו בפתרון."},
    ],
    stepsSource="ai-verified")

# Q2a -- partial fractions
add(2, "א",
    rubric=rub(("פירוק המכנה $x^2(x^2+4)$ וכתיבת פירוק לשברים חלקיים בצורה הנכונה", 3),
               ("מציאת המקדמים $A=C=0$, $B=2$, $D=-1$", 3),
               ("אינטגרציה של כל איבר: $-\\frac{2}{x}$ ו-$-\\frac{1}{2}\\arctan\\frac{x}{2}$", 3),
               ("הוספת הקבוע $c$", 1)),
    rubricSource="ai-verified",
    pitfalls=["לכתוב $\\frac{Cx+D}{x^2+4}$ כשני שברים עם $x\\pm 2$: הביטוי $x^2+4$ אינו פריק מעל הממשיים.",
              "לשכוח את האיבר $\\frac{A}{x}$ מהפירוק עבור הגורם הריבועי $x^2$ (צריך גם חזקה ראשונה וגם שנייה).",
              "לשכוח את הגורם $\\frac12$ באינטגרל של $\\frac{1}{x^2+4}$."],
    steps=[
        {"type": "choice", "prompt": r"מהי צורת הפירוק לשברים חלקיים של $\frac{x^2+8}{x^2(x^2+4)}$?",
         "options": opts(r"$\frac{A}{x}+\frac{B}{x^2}+\frac{Cx+D}{x^2+4}$",
                         r"$\frac{A}{x}+\frac{B}{x+2}+\frac{C}{x-2}$",
                         r"$\frac{A}{x}+\frac{B}{x^2+4}$"), "correctId": "a",
         "explain": r"הגורם $x^2$ נותן $\frac{A}{x}+\frac{B}{x^2}$, והגורם הריבועי הבלתי פריק $x^2+4$ נותן מונה לינארי $Cx+D$."},
        {"type": "numeric", "prompt": "מהו המקדם $B$ בפירוק?", "answer": 2, "tol": 0,
         "explain": r"הצבה/השוואת מקדמים נותנת $A=C=0$, $B=2$, $D=-1$ (בדיקה: $\frac{2}{x^2}-\frac{1}{x^2+4}=\frac{x^2+8}{x^2(x^2+4)}$)."},
        {"type": "numeric", "prompt": "מהו המקדם $D$ בפירוק?", "answer": -1, "tol": 0,
         "explain": r"$D=-1$, ולכן האיבר השני הוא $-\frac{1}{x^2+4}$."},
        {"type": "choice", "prompt": "מהו האינטגרל?",
         "options": opts(r"$-\frac{2}{x}-\frac{1}{2}\arctan\frac{x}{2}+c$", r"$-\frac{2}{x}-\arctan\frac{x}{2}+c$",
                         r"$-\frac{2}{x}+\frac{1}{2}\arctan\frac{x}{2}+c$", r"$\frac{2}{x}-\frac{1}{2}\arctan\frac{x}{2}+c$"),
         "correctId": "a",
         "explain": r"$\int\frac{2}{x^2}dx=-\frac{2}{x}$ ו-$\int\frac{1}{x^2+4}dx=\frac12\arctan\frac{x}{2}$, עם סימן מינוס לפני האחרון."},
    ],
    stepsSource="ai-verified")

# Q2b -- recursive sequence
add(2, "ב",
    rubric=rub(("הוכחה באינדוקציה שהסדרה יורדת (בסיס $a_2\\le a_1$ וצעד)", 3),
               ("הוכחה באינדוקציה שהסדרה חסומה מלרע על-ידי $1$", 3),
               ("שימוש במשפט: סדרה מונוטונית וחסומה מתכנסת", 1),
               ("מעבר לגבול במשוואה הרקורסיבית והגעה ל-$L(L-1)=0$", 2),
               ("פסילת $L=0$ בעזרת החסם התחתון ומסקנה $L=1$", 1)),
    rubricSource="ai-verified",
    pitfalls=["להניח שהגבול קיים ולפתור את משוואת נקודת השבת $L=\\frac{3}{2+1/L}$ לפני שהוכחנו התכנסות.",
              "להוכיח רק מונוטוניות בלי חסם (או להפך): שניהם נדרשים כדי להשתמש במשפט.",
              "לא לפסול את הפתרון $L=0$ לפי החסם $a_n\\ge1$."],
    steps=[
        {"type": "choice", "prompt": "באיזו שיטה מוכיחים את ההתכנסות?",
         "options": opts("שתי אינדוקציות: הסדרה יורדת וחסומה מלרע, ואז משפט הסדרה המונוטונית החסומה",
                         "משפט הסנדוויץ' עם שתי סדרות קבועות",
                         "הגדרת הגבול ישירות עם $\\varepsilon$ לכל $n$",
                         "מבחן המנה לסדרות"), "correctId": "a",
         "explain": "הפתרון הרשמי מראה $a_{n+1}\\le a_n$ ו-$a_n\\ge1$ באינדוקציה, ומסיק התכנסות ממשפט."},
        {"type": "numeric", "prompt": r"מהו $a_3$? עגלו לשלוש ספרות אחרי הנקודה.", "answer": 1.059, "tol": 0.001,
         "explain": r"$a_2=\frac{6}{5}$ ו-$a_3=\frac{3}{2+\frac56}=\frac{18}{17}\approx1.059$. הסדרה אכן יורדת: $2>1.2>1.059$."},
        {"type": "order", "prompt": "סדרו את שורות ההוכחה שהסדרה יורדת.",
         "lines": [r"בסיס: $a_2=\frac{6}{5}\le 2=a_1$",
                   r"הנחת האינדוקציה: $a_{n+1}\le a_n$",
                   r"צעד: $a_{n+2}=\frac{3}{2+\frac{1}{a_{n+1}}}\le\frac{3}{2+\frac{1}{a_n}}=a_{n+1}$",
                   r"לפי עקרון האינדוקציה $a_{n+1}\le a_n$ לכל $n$"],
         "explain": "בסיס, הנחה, צעד, מסקנה."},
        {"type": "findbug", "prompt": "בהוכחת החסם התחתון $a_n\\ge1$ שורה אחת שונתה והיא שגויה. מצאו אותה.",
         "lines": [r"בסיס: $a_1=2\ge 1$",
                   r"הנחת האינדוקציה: $a_n\ge 1$",
                   r"צעד: $a_{n+1}=\frac{3}{2+\frac{1}{a_n}}\ge\frac{3}{2+\frac{1}{1}}=\frac{3}{2}$",
                   r"לפי עקרון האינדוקציה $a_n\ge 1$ לכל $n$"],
         "bugIndex": 2,
         "explain": r"$\frac{3}{2+1}=1$ ולא $\frac32$. הערך הנכון הוא בדיוק החסם $1$."},
        {"type": "numeric", "prompt": r"פותרים $L=\frac{3}{2+\frac1L}$ ופוסלים $L=0$ לפי החסם. מהו הגבול?", "answer": 1, "tol": 0,
         "explain": r"$L^2-L=0$ ולכן $L\in\{0,1\}$. כיוון ש-$a_n\ge1$ מקבלים $L=1$."},
    ],
    stepsSource="ai-verified")

# Q3a -- sequence limit with conjugate
add(3, "א",
    rubric=rub(("זיהוי הצורה $\\infty-\\infty$ וכפל בצמוד", 3),
               ("פישוט המונה ל-$3n$", 3),
               ("חילוק המונה והמכנה ב-$n$", 2),
               ("חישוב הגבול $\\frac{3}{2}$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לקבוע שהגבול הוא $0$ כי \"אינסוף פחות אינסוף\": זו צורה לא מוגדרת.",
              "אחרי הכפל בצמוד לשכוח לחלק גם את המכנה ב-$n$ ולקבל גבול שגוי.",
              "טעות סימן בפישוט המונה: $(1+n+n^2)-(1-2n+n^2)=3n$ ולא $-n$."],
    steps=[
        {"type": "choice", "prompt": "איזו שיטה מתאימה לגבול ההפרש של שני שורשים?",
         "options": opts("כפל בצמוד (סכום השורשים) ופישוט המונה",
                         "הצבת $n=\\infty$ בכל שורש והסקה שההפרש הוא $0$",
                         "חלוקת כל איבר בנפרד ב-$n$ בלי כפל בצמוד",
                         "פירוק לגורמים וצמצום"), "correctId": "a",
         "explain": "ההפרש הוא מצורה $\\infty-\\infty$. כפל בצמוד הופך אותו לשבר שאפשר לחשב."},
        {"type": "numeric", "prompt": r"אחרי הכפל בצמוד המונה הוא $kn$. מהו $k$?", "answer": 3, "tol": 0,
         "explain": r"$(1+n+n^2)-(1-2n+n^2)=3n$."},
        {"type": "numeric", "prompt": r"לאחר חילוק המכנה ב-$n$, לאיזה ערך שואף $\frac{\sqrt{1+n+n^2}+\sqrt{1-2n+n^2}}{n}$?",
         "answer": 2, "tol": 0,
         "explain": r"כל שורש מחולק ב-$n$ שואף ל-$1$, ובסך הכול $1+1=2$."},
        {"type": "order", "prompt": "סדרו את שלבי החישוב.",
         "lines": [r"כפל בצמוד: $\frac{\left(\sqrt{1+n+n^2}-\sqrt{1-2n+n^2}\right)\left(\sqrt{1+n+n^2}+\sqrt{1-2n+n^2}\right)}{\sqrt{1+n+n^2}+\sqrt{1-2n+n^2}}$",
                   r"פישוט המונה: $\frac{3n}{\sqrt{1+n+n^2}+\sqrt{1-2n+n^2}}$",
                   r"חילוק ב-$n$: $\frac{3}{\sqrt{\frac{1}{n^2}+\frac{1}{n}+1}+\sqrt{\frac{1}{n^2}-\frac{2}{n}+1}}$",
                   r"גבול: $\frac{3}{2}$"],
         "explain": "כפל בצמוד, פישוט, חילוק בחזקה הגבוהה, ואז גבול."},
    ],
    stepsSource="ai-verified")

# Q3b -- shells
add(3, "ב",
    rubric=rub(("זיהוי שיטת קליפות וקביעת הגבולות $0\\le x\\le1$", 2),
               ("כתיבת האינטגרל $2\\pi\\int_0^1 x(e-e^x)\\,dx$ (רדיוס $x$, גובה $e-e^x$)", 3),
               ("אינטגרציה בחלקים של $\\int xe^x\\,dx$", 3),
               ("הצבת גבולות והתוצאה $2\\pi\\left(\\frac{e}{2}-1\\right)$", 2)),
    rubricSource="ai-verified",
    pitfalls=["להשתמש בשיטת דיסקים סביב ציר $y$ בלי להפוך את הפונקציות לפי $y$, או לשכוח את הגורם $x$ (הרדיוס) באינטגרל.",
              "טעות בגובה הקליפה: הגובה הוא $(e+1)-(e^x+1)=e-e^x$ ולא $e^x+1$.",
              "בעיית סימן באינטגרציה בחלקים: $\\int xe^x\\,dx=xe^x-\\int e^x\\,dx$."],
    steps=[
        {"type": "choice", "prompt": "איזה אינטגרל נותן את הנפח בשיטת קליפות?",
         "options": opts(r"$V=2\pi\int_0^1 x\,(e-e^x)\,dx$", r"$V=\pi\int_0^1 (e-e^x)^2\,dx$",
                         r"$V=2\pi\int_0^1 (e-e^x)\,dx$", r"$V=2\pi\int_0^1 x\,(e^x+1)\,dx$"), "correctId": "a",
         "explain": r"קליפה ברדיוס $x$ וגובה $(e+1)-(e^x+1)=e-e^x$ נותנת $2\pi x(e-e^x)\,dx$."},
        {"type": "numeric", "prompt": r"חשבו $\int_0^1 xe^x\,dx$.", "answer": 1, "tol": 0,
         "explain": r"$\left[xe^x-e^x\right]_0^1=(e-e)-(0-1)=1$."},
        {"type": "numeric", "prompt": r"מהו הנפח $V$? עגלו לשלוש ספרות אחרי הנקודה.", "answer": 2.257, "tol": 0.001,
         "explain": r"$V=2\pi\left(\frac{e}{2}-1\right)\approx 2.257$."},
        {"type": "order", "prompt": "סדרו את שלבי החישוב.",
         "lines": [r"$V=2\pi\int_0^1 x\left(e-e^x\right)dx=2\pi\left(e\int_0^1 x\,dx-\int_0^1 xe^x\,dx\right)$",
                   r"אינטגרציה בחלקים עם $u=x,\ v'=e^x$: $\int_0^1 xe^x\,dx=xe^x\Big|_0^1-\int_0^1 e^x\,dx$",
                   r"$V=2\pi\left(\frac{1}{2}e-e+e^x\Big|_0^1\right)$",
                   r"$V=2\pi\left(\frac{e}{2}-1\right)$"],
         "explain": "הצבת האינטגרל, אינטגרציה בחלקים, הצבת גבולות ותוצאה."},
    ],
    stepsSource="ai-verified")

# Q4a -- extrema on closed interval
add(4, "א",
    rubric=rub(("גזירה: $y'=\\frac{2}{x}(\\ln x-1)$", 3),
               ("נקודה קריטית $x=e$ ובדיקה שהיא בתוך הקטע", 2),
               ("חישוב ערכי הפונקציה בשני הקצוות ובנקודה הקריטית", 3),
               ("קביעת המקסימום $0$ והמינימום $-1$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לא לבדוק את קצוות הקטע: המקסימום מתקבל בקצה $x=e^2$.",
              "לפתור $\\ln x=1$ ולכתוב $x=1$ במקום $x=e$.",
              "לפרש את הנקודה הקריטית כמקסימום בלי להשוות עם הערכים בקצוות."],
    steps=[
        {"type": "choice", "prompt": "איך מוצאים מקסימום ומינימום של פונקציה רציפה בקטע סגור?",
         "options": opts("משווים את ערכי הפונקציה בנקודות הקריטיות שבתוך הקטע ובשני הקצוות",
                         "בודקים רק את הנקודות שבהן הנגזרת מתאפסת",
                         "בודקים רק את שני הקצוות",
                         "לוקחים את הנקודה בה הנגזרת השנייה חיובית"), "correctId": "a",
         "explain": "משפט ויירשטראס: הקיצון מתקבל בקצה או בנקודה קריטית."},
        {"type": "numeric", "prompt": r"פותרים $y'=\frac{2}{x}(\ln x-1)=0$. מהו $x$? עגלו לשלוש ספרות אחרי הנקודה.",
         "answer": 2.718, "tol": 0.001, "explain": r"$\ln x=1$ ולכן $x=e\approx2.718$, והוא בתוך הקטע $[\sqrt{e},e^2]$."},
        {"type": "numeric", "prompt": r"מהו $y(\sqrt{e})$?", "answer": -0.75, "tol": 0,
         "explain": r"$\ln\sqrt{e}=\frac12$, ולכן $\frac14-1=-\frac34$."},
        {"type": "numeric", "prompt": r"מהו $y(e^2)$?", "answer": 0, "tol": 0,
         "explain": r"$\ln e^2=2$, ולכן $4-4=0$."},
        {"type": "numeric", "prompt": "מהו הערך המינימלי של הפונקציה בקטע?", "answer": -1, "tol": 0,
         "explain": r"$y(e)=1-2=-1$ הוא הנמוך מבין $-\frac34,\,-1,\,0$."},
    ],
    stepsSource="ai-verified")

# Q4b -- oblique asymptote parameters
add(4, "ב",
    rubric=rub(("איחוד לשבר אחד ודרישה שמקדם $x^4$ במונה יתאפס", 3),
               ("קביעה ש-$a=3$", 3),
               ("חישוב הגבול הנותר ומציאת $b=0$", 3),
               ("ניסוח התשובה $a=3,\\ b=0$", 1)),
    rubricSource="ai-verified",
    pitfalls=["לבחור $a\\neq3$: אז המונה מדרגה $4$ והמכנה מדרגה $3$ והגבול אינסופי ולא $0$.",
              "לחשב רק את $a$ ולשכוח שגם $b$ נקבע (כאן $b=0$).",
              "לחלק ב-$x^4$ במקום להשוות דרגות אחרי האיחוד לשבר אחד."],
    steps=[
        {"type": "choice", "prompt": "מה המשמעות של הגבול הנתון?",
         "options": opts("הישר $y=ax+b$ הוא אסימפטוטה משופעת של $f$",
                         "הישר $y=ax+b$ משיק לגרף בראשית",
                         "$f$ חסומה על-ידי $ax+b$",
                         "$f$ רציפה בכל נקודה"), "correctId": "a",
         "explain": "הפרש שואף ל-0 בדיוק כשהישר הוא אסימפטוטה משופעת."},
        {"type": "numeric", "prompt": r"מהו $a=\lim_{x\to\infty}\frac{3x^4}{x(x^3+2x+9)}$?", "answer": 3, "tol": 0,
         "explain": r"דרגות שוות והמקדמים המובילים $3$ ו-$1$."},
        {"type": "choice", "prompt": r"אם בוחרים $a=2$ (ו-$b=0$), למה שואף ההפרש $\frac{3x^4}{x^3+2x+9}-2x$ כש-$x\to+\infty$?",
         "options": opts(r"$+\infty$", r"$0$", r"$-\infty$", r"$1$"), "correctId": "a",
         "explain": r"המונה מכיל $x^4$ במקדם $3-2=1>0$ והמכנה מדרגה 3, לכן הגבול הוא $+\infty$."},
        {"type": "numeric", "prompt": r"עם $a=3$, מהו $b=\lim_{x\to\infty}\left(\frac{3x^4}{x^3+2x+9}-3x\right)$?",
         "answer": 0, "tol": 0,
         "explain": r"$\frac{-6x^2-27x}{x^3+2x+9}\to0$ כי דרגת המונה קטנה מדרגת המכנה."},
    ],
    stepsSource="ai-verified")

# Q5a -- discontinuities
add(5, "א",
    rubric=rub(("זיהוי נקודות החשד $x=-2$ ו-$x=0$", 2),
               ("חישוב הגבולות החד-צדדיים ב-$x=-2$: $+\\infty$ משמאל ו-$1$ מימין", 3),
               ("חישוב הגבולות החד-צדדיים ב-$x=0$: $3$ משמאל ו-$\\frac{\\pi}{2}$ מימין", 3),
               ("סיווג: אי רציפות מסוג שני ב-$-2$ ומסוג ראשון (קפיצה) ב-$0$", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחשב רק את הערך של הפונקציה בנקודה ולא את הגבולות החד-צדדיים משני הצדדים.",
              "לפשט את המעריך בלי לשים לב שעבור $x<-2$ מתקיים $|x+2|=-(x+2)$.",
              "לסווג את $x=-2$ כקפיצה למרות שאחד הגבולות החד-צדדיים אינסופי."],
    steps=[
        {"type": "numeric", "prompt": r"מהו $\lim_{x\to-2^+}f(x)$?", "answer": 1, "tol": 0,
         "explain": r"מימין ל-$-2$ מתקיים $f(x)=x+3\to1$."},
        {"type": "choice", "prompt": r"משמאל ל-$-2$ מתקיים $f(x)=e^{x/(x+2)}\to e^{+\infty}=+\infty$. מהו סוג אי הרציפות ב-$x=-2$?",
         "options": opts("מסוג שני (גבול חד-צדדי אינסופי)", "מסוג ראשון (קפיצה סופית)", "סליקה", "הפונקציה רציפה שם"),
         "correctId": "a", "explain": "כשאחד הגבולות החד-צדדיים אינו סופי, אי הרציפות היא מסוג שני."},
        {"type": "numeric", "prompt": r"מהו $\lim_{x\to0^-}f(x)$?", "answer": 3, "tol": 0,
         "explain": r"משמאל ל-$0$ מתקיים $f(x)=x+3\to3$."},
        {"type": "numeric", "prompt": r"מהו $\lim_{x\to0^+}f(x)$? עגלו לשלוש ספרות אחרי הנקודה.", "answer": 1.571, "tol": 0.001,
         "explain": r"$\arctan(\frac1x)\to\arctan(+\infty)=\frac{\pi}{2}\approx1.571$."},
        {"type": "choice", "prompt": r"מהו סוג אי הרציפות ב-$x=0$?",
         "options": opts("מסוג ראשון (קפיצה סופית)", "מסוג שני", "סליקה", "הפונקציה רציפה שם"), "correctId": "a",
         "explain": r"שני הגבולות החד-צדדיים סופיים אך שונים ($3\neq\frac{\pi}{2}$), לכן זו קפיצה."},
    ],
    stepsSource="ai-verified")

# Q5b -- substitution
add(5, "ב",
    rubric=rub(("בחירת ההצבה $t=x^2$", 3),
               ("חישוב $dt=2x\\,dx$ והמרת האינטגרל ל-$\\frac12\\int\\cos t\\,dt$", 4),
               ("אינטגרציה וחזרה למשתנה המקורי: $\\frac12\\sin(x^2)+C$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את הגורם $\\frac12$ אחרי ההצבה, ולכתוב $\\sin(x^2)+C$.",
              "לא להמיר את $dx$ ולהשאיר את $x$ בתוך האינטגרל במשתנה $t$.",
              "לא לחזור למשתנה $x$ בסוף."],
    steps=[
        {"type": "choice", "prompt": r"איזו הצבה מתאימה ל-$\int x\cos(x^2)\,dx$?",
         "options": opts(r"$t=x^2$", r"$t=\cos(x^2)$", r"$t=x$", r"$t=\sin x$"), "correctId": "a",
         "explain": r"$x\,dx$ הוא הנגזרת של הפנימית $x^2$ עד כדי קבוע, לכן $t=x^2$ מתאים."},
        {"type": "numeric", "prompt": r"אם $dt=2x\,dx$, אז $x\,dx=k\,dt$. מהו $k$?", "answer": 0.5, "tol": 0,
         "explain": r"$x\,dx=\frac{1}{2}dt$."},
        {"type": "choice", "prompt": "מהי התוצאה בחזרה למשתנה $x$?",
         "options": opts(r"$\frac{1}{2}\sin(x^2)+C$", r"$\sin(x^2)+C$", r"$-\frac{1}{2}\sin(x^2)+C$", r"$\frac{1}{2}\cos(x^2)+C$"),
         "correctId": "a", "explain": r"$\frac12\int\cos t\,dt=\frac12\sin t+C$. נגזרת התוצאה היא $x\cos(x^2)$."},
        {"type": "order", "prompt": "סדרו את שלבי הפתרון.",
         "lines": [r"הצבה: $t=x^2,\ dt=2x\,dx$",
                   r"$\int x\cos(x^2)\,dx=\frac{1}{2}\int\cos(t)\,dt$",
                   r"$=\frac{1}{2}\sin(t)+C$",
                   r"חזרה למשתנה המקורי: $=\frac{1}{2}\sin(x^2)+C$"],
         "explain": "הצבה, המרה, אינטגרציה, חזרה."},
    ],
    stepsSource="ai-verified")

# Q6a -- e^x >= x+1
add(6, "א",
    rubric=rub(("הגדרת פונקציית העזר $f(x)=e^x-x-1$", 2),
               ("חישוב $f'(x)=e^x-1$ ומציאת הנקודה הקריטית $x=0$", 3),
               ("נגזרת שנייה $f''(0)=1>0$ ולכן מינימום מקומי", 2),
               ("$f(0)=0$ והמסקנה $f(x)\\ge0$, כלומר $e^x\\ge x+1$", 3)),
    rubricSource="ai-verified",
    pitfalls=["להציב ערכים מספריים בלבד: הטענה היא לכל $x$ ממשי ולא נבדקת על דוגמאות.",
              "להגדיר $f(x)=e^x$ ולהשוות ל-$x+1$ בלי פונקציית עזר ובלי חקירת נגזרת.",
              "לשכוח לחשב את $f(0)$ ולכן לא להגיע ל-$f(x)\\ge0$."],
    steps=[
        {"type": "choice", "prompt": "איזו שיטה מוכיחה את אי-השוויון לכל $x$?",
         "options": opts(r"פונקציית עזר $f(x)=e^x-x-1$ וחקירת המינימום שלה בעזרת נגזרות",
                         "אינדוקציה על $x$",
                         "הצבת $x=0$ בלבד",
                         "משפט ערך הביניים על $e^x$ בלבד"), "correctId": "a",
         "explain": "הפתרון הרשמי מראה שערך המינימום של $f$ הוא $0$."},
        {"type": "numeric", "prompt": r"מהו $f''(0)$ עבור $f(x)=e^x-x-1$?", "answer": 1, "tol": 0,
         "explain": r"$f''(x)=e^x$ ולכן $f''(0)=1>0$: מינימום מקומי ב-$0$."},
        {"type": "numeric", "prompt": r"מהו $f(0)$?", "answer": 0, "tol": 0,
         "explain": r"$f(0)=e^0-0-1=0$, ולכן $f(x)\ge f(0)=0$."},
        {"type": "order", "prompt": "סדרו את שורות ההוכחה.",
         "lines": [r"נגדיר $f(x)=e^x-x-1$",
                   r"$f'(x)=e^x-1$ ולכן $f'(0)=0$",
                   r"$f''(x)=e^x$ ולכן $f''(0)=1>0$ ו-$x=0$ מינימום מקומי",
                   r"$f(0)=0$ ולכן $f(x)\ge f(0)=0$ לכל $x$",
                   r"מכאן $e^x\ge x+1$"],
         "explain": "הגדרה, נגזרת ראשונה, נגזרת שנייה, ערך המינימום, מסקנה."},
        {"type": "findbug", "prompt": "שורה אחת בהוכחה שונתה והיא שגויה. מצאו אותה.",
         "lines": [r"נגדיר $f(x)=e^x-x-1$",
                   r"$f'(x)=e^x+1$ ולכן $f'(0)=2$",
                   r"$f''(x)=e^x$ ולכן $f''(0)=1>0$ ו-$x=0$ מינימום מקומי",
                   r"$f(0)=0$ ולכן $f(x)\ge f(0)=0$ לכל $x$",
                   r"מכאן $e^x\ge x+1$"],
         "bugIndex": 1,
         "explain": r"$f'(x)=e^x-1$, ולכן $f'(0)=0$ ויש נקודה קריטית. עם $e^x+1$ הנגזרת אינה מתאפסת."},
    ],
    stepsSource="ai-verified")

# Q6b -- area
add(6, "ב",
    rubric=rub(("נקודת החיתוך $y=x$ עם $y=\\frac1x$ ברביע הראשון: $(1,1)$, ושרטוט התחום", 2),
               ("חלוקת התחום למשולש $S_1$ ולשטח $S_2$ מתחת ל-$y=4$ ומעל $y=\\frac1x$", 2),
               ("שטח המשולש $S_1=\\frac92$", 2),
               ("שטח $S_2=3-\\ln4$ באינטגרל $\\int_1^4\\frac1y\\,dy$", 3),
               ("סכום $S=\\frac{15}{2}-\\ln4$", 1)),
    rubricSource="ai-verified",
    pitfalls=["להתעלם מהקו $y=4$ ולחשב רק את השטח בין $y=x$ ל-$y=\\frac1x$.",
              "לשכוח שהתחום ממשיך שמאלה ל-$x=\\frac14$ בנקודה שבה $y=\\frac1x$ פוגש את $y=4$.",
              "טעות בשטח המלבן ($S_4=3$) או בסימן של $\\ln4$."],
    steps=[
        {"type": "numeric", "prompt": r"באיזה $x>0$ נחתכים $y=x$ ו-$y=\frac1x$?", "answer": 1, "tol": 0,
         "explain": r"$x=\frac1x$ נותן $x=\pm1$, ובתחום החיובי $x=1$."},
        {"type": "numeric", "prompt": r"שטח המשולש $S_1$ שקדקדיו $(1,1),(4,4),(1,4)$?", "answer": 4.5, "tol": 0,
         "explain": r"משולש ישר זווית עם ניצבים באורך $3$: $\frac{3\cdot3}{2}=\frac92$."},
        {"type": "numeric", "prompt": r"חשבו $\int_1^4\frac1y\,dy$. עגלו לשלוש ספרות אחרי הנקודה.", "answer": 1.386, "tol": 0.001,
         "explain": r"$\ln4\approx1.386$, ו-$S_2=3-\ln4$."},
        {"type": "numeric", "prompt": r"מהו השטח הכולל $S=S_1+S_2$? עגלו לשלוש ספרות אחרי הנקודה.", "answer": 6.114, "tol": 0.001,
         "explain": r"$S=\frac{15}{2}-\ln4\approx6.114$."},
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "24B-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ד, מועד ב'",
    "year": 2024,
    "examDate": "12/08/2024",
    "sourceFile": "calculus-1/24B-B exam+solution.pdf",
    "solutionFile": "calculus-1/24B-B exam+solution.pdf",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

# -*- coding: utf-8 -*-
"""Generator for tools/raw/20B-C.json -- calculus-1 (20151), semester C (summer) 2020, moed B (27/10/2020).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_20B-C.py

Source: sitting 20B-C, pp.1-2 (typed exam only, NO solution or key anywhere). The header lists the course as a joint
exam for electrical/electronics engineering AND computer science, so it is in scope. Six questions, 20% each,
Q1 mandatory, choose 4 of Q2-Q6 (a/b parts 10% each). Every question is transcribed and HELD with reason "no-key";
the orchestrator routes them to the solver.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20B-C.json"
NOKEY = "no-key"


def Q(num, kind, topic, question, part=None, points=None):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "hold": NOKEY}
    if part:
        q["part"] = part
    if points:
        q["points"] = points
    return q


questions = [
    Q(1, "computation", "function_investigation",
      r"חקרו את הפונקציה $f(x)=\frac{x^3}{2(x+1)^2}$ לפי הסעיפים הבאים: תחום הגדרה, תחומי עליה/ירידה, נקודות קיצון, "
      "קמירות ונקודות פיתול, אסימפטוטות. שרטטו את גרף הפונקציה.", points=20),

    Q(2, "computation", "sequences_limits",
      r"חשבו את גבול הסדרה $\lim_{n\to\infty}\frac{3^n}{3^n+b^n}$, כאשר $b>0$ הוא פרמטר ממשי.",
      part="א", points=10),
    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{x^3+2x+5}{x^2-1}\,dx$.", part="ב", points=10),

    Q(3, "computation", "continuity",
      "האם הפונקציה\n"
      r"$$f(x)=\begin{cases}\frac{e^x-1}{\sin 2x}, & x<0\ \frac{1}{2}, & x=0\ x\cdot\ln x+\frac{\arcsin x}{2x}, & x>0\end{cases}$$"
      "\n" r"רציפה ב-$x=0$?", part="א", points=10),
    Q(3, "computation", "extrema_optimization",
      r"מצאו את הערך המקסימלי ואת הערך המינימלי של הפונקציה $f(x)=x\sqrt{18-x^2}$ בקטע $[0,4]$.",
      part="ב", points=10),

    Q(4, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\ln^2 x\,dx$.", part="א", points=10),
    Q(4, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to2}\frac{\sqrt{3x-2}-\sqrt{x+2}}{x^2-4}$.", part="ב", points=10),

    Q(5, "proof", "definite_integrals",
      r"הוכיחו את אי-השוויון הבא: $\frac{2}{3}\le\int_{-1}^{1}\frac{1}{2x^4+1}\,dx\le2$.", part="א", points=10),
    Q(5, "computation", "function_limits",
      r"חשבו את הגבול $\lim_{x\to0}\frac{1}{x^3}\int_0^x\frac{t^2}{1+t^4}\,dt$.", part="ב", points=10),

    Q(6, "computation", "derivatives_tangents",
      r"בעזרת דיפרנציאל של הפונקציה $y=\tan x$ בנקודה $x=\frac{\pi}{4}$ חשבו בקירוב את $\tan 48^\circ$.",
      part="א", points=10),
    Q(6, "computation", "definite_integrals",
      r"חשבו את השטח הכלוא בין הקווים $y=2x,\quad y=\frac{x}{2},\quad y=\frac{1}{x}$.", part="ב", points=10),
]

exam = {
    "examCode": "20B-C",
    "examLabel": "מבחן סוף סמסטר קיץ תש\"פ, מועד ב'",
    "year": 2020,
    "examDate": "27/10/2020",
    "sourceFile": "calculus-1/20B-C exam.pdf",
    "solutionFile": "",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

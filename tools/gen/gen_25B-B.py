# -*- coding: utf-8 -*-
"""Generator for tools/raw/25B-B.json -- calculus-1 (20151), semester B 2025, moed B (11/08/2025).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_25B-B.py

Source: sitting 25B-B, pp.1-2 (scanned exam only, NO solution or key anywhere). Six questions, 25% each,
solve 4 (Q1 is a single 25% investigation; Q2-Q6 have a 13% and a 12% part). Every question is transcribed
and HELD with reason "no-key"; the orchestrator routes them to the solver.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25B-B.json"
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
      r"חקרו את הפונקציה $f(x)=x\cdot e^{\frac{1}{x-2}}$ על פי הסעיפים הבאים: תחום הגדרה, נקודות חיתוך עם הצירים, "
      "תחומי עליה וירידה, נקודות קיצון, תחומי קמירות וקעירות, נקודות פיתול, אסימפטוטות, שרטוט.", points=25),

    Q(2, "proof", "sequences_limits",
      "נתונה הסדרה: " r"$a_1=\sqrt{20}$ ו-$a_{n+1}=\sqrt{20+a_n}$." "\nהוכיחו כי הסדרה מתכנסת וחשבו את גבולה.",
      part="א", points=13),
    Q(2, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int(4x+6)\arctan x\,dx$.", part="ב", points=12),

    Q(3, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to0^+}\left(\frac{1}{x}\right)^{\tan 2x}$.", part="א", points=13),
    Q(3, "computation", "derivatives_tangents",
      r"מצאו את משוואת המשיק של גרף הפונקציה: $y=(\tan x)^{\cos x}$ בנקודה $x=\frac{\pi}{4}$.", part="ב", points=12),

    Q(4, "computation", "function_limits",
      r"חשבו את הגבול הבא: $\lim_{x\to2}\frac{\sqrt{x+2}-\sqrt{3x-2}}{\sqrt{4x+1}-\sqrt{5x-1}}$.", part="א", points=13),
    Q(4, "computation", "definite_integrals",
      r'חשבו את שטח התחום שחסום ע"י גרף הפונקציה $f(x)=x^2$, הישר המשיק לגרף הפונקציה $f(x)$ בנקודה $(2,4)$ וציר ה-$X$.',
      part="ב", points=12),

    Q(5, "proof", "mean_value_theorems",
      r"הוכיחו כי מתקיים האי שוויון: $e^{\sin^2 b}-e^{\sin^2 a}\le e(b-a)$, עבור $-\infty<a<b<\infty$.",
      part="א", points=13),
    Q(5, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל הבא: $\int\frac{\sin(x)\,dx}{5+2\cos(x)+\cos^2(x)}$.", part="ב", points=12),

    Q(6, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום הכלוא בין חצי המעגל $y=\sqrt{25-x^2}$ לבין הישר $y=3$ סביב ציר ה-$X$.",
      part="א", points=13),
    Q(6, "computation", "derivatives_tangents",
      r"נתונה הפונקציה $f(x)=\begin{cases}\sin(ax), & x\le0\\ x^2\ln(x), & x>0\end{cases}$ כאשר $a$ הוא פרמטר ממשי. "
      r"עבור אילו ערכי $a$ הפונקציה תהיה גזירה בנקי $x=0$?",
      part="ב", points=12),
]

exam = {
    "examCode": "25B-B",
    "examLabel": "מבחן סוף סמסטר ב' תשפ\"ה, מועד ב'",
    "year": 2025,
    "examDate": "11/08/2025",
    "sourceFile": "calculus-1/25B-B exam (scan).pdf",
    "solutionFile": "",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

# -*- coding: utf-8 -*-
"""Generator for tools/raw/22B-A.json -- calculus-1 (20151), semester A 2022, moed B (22/02/2022).
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_22B-A.py

Source: sitting 22B-A, pp.1-2 (printed exam only, NO solution or key anywhere). Six questions, 20% each (two parts of
10%), solve 5 of 6. Parameters A, B, C (last three digits of the student's ID) appear in some parts; the header rule is
shipped as context c0. Every part is transcribed and HELD with reason "no-key"; the orchestrator routes them to the solver.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22B-A.json"
NOKEY = "no-key"


def Q(num, kind, topic, question, part=None, points=10, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "hold": NOKEY, "points": points}
    if part:
        q["part"] = part
    q.update(kw)
    return q


CTX0 = (r"בחלק מסעיפי המבחן מופיעים הפרמטרים $A$, $B$ ו-$C$. חובה להציב בתחילת הפתרון לכל שאלה את ערכי הפרמטרים, "
        r"בהתאם לשלוש הספרות האחרונות של מספר תעודת הזהות שלכם: למשל עבור ת.ז. 123456789 נקבל $A=7$, $B=8$, $C=9$. "
        r"שאלות בהן $A$, $B$ ו-$C$ יוצבו רק בשלב התשובה הסופית לא ייבדקו.")

questions = [
    Q(1, "computation", "extrema_optimization",
      r"מצאו ומיינו את כל הנקודות החשודות לקיצון מקומי של הפונקציה $f(x)=2x+3\sqrt[3]{x^2}$.", part="א"),
    Q(1, "computation", "sequences_limits",
      r"חשבו את הגבול $\lim_{n\to\infty}\frac{(n+2)!+(A+1)\,n\,(n+1)!}{(n+1)!-n\cdot n!}\sin\frac{C+1}{(n+1)^2}$.",
      part="ב", contextId="c0"),

    Q(2, "proof", "mean_value_theorems",
      r"הראו כי לכל $x>0$ מתקיים האי-שוויון $\frac{x}{1+x^2}<\arctan x<x$.", part="א"),
    Q(2, "proof", "sequences_limits",
      r"הוכיחו כי הסדרה $a_{n+1}=\frac{(B+3)a_n}{(B+2)a_n+1},\ a_1=C+2$ מתכנסת וחשבו את גבולה.",
      part="ב", contextId="c0"),

    Q(3, "computation", "function_limits",
      r"מצאו את כל האסימפטוטות לגרף הפונקציה $f(x)=(x+A)\left(2+\cos\frac{B+1}{x+A}\right)$.",
      part="א", contextId="c0"),
    Q(3, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{dx}{1+\sin x+3\cos x}$.", part="ב"),

    Q(4, "proof", "continuity",
      r"הוכיחו כי למשוואה $x^3+(C+1)x+\cos\left((C+1)x\right)=B+1$ קיים שורש ממשי אחד בלבד.",
      part="א", contextId="c0"),
    Q(4, "computation", "indefinite_integrals",
      r"חשבו את האינטגרל $\int\frac{\arctan^3\left(\sqrt{x}\right)}{(x+1)\sqrt{x}}\,dx$.", part="ב"),

    Q(5, "computation", "function_limits",
      r"חשבו את הגבול: $\lim_{x\to+\infty}\left(x^3+A\right)\left(\sqrt{x^2+\sqrt{x^4+C+1}}-x\sqrt{2}\right)$.",
      part="א", contextId="c0"),
    Q(5, "computation", "definite_integrals",
      r"חשבו את אורך הקשת של העקומה $y=\ln(\sin x)$ בקטע $\left[\frac{\pi}{3},\frac{\pi}{2}\right]$.", part="ב"),

    Q(6, "computation", "derivatives_tangents",
      r"תהיה $f(x)=\begin{cases}\frac{1}{\sin x}-\frac{1}{x}, & x\neq0\\ p, & x=0\end{cases}$. "
      r"מצאו ערך פרמטר ממשי $p$ כך שפונקציה $f$ תהיה גזירה ב-$x=0$. מהו $f'(0)$?", part="א"),
    Q(6, "computation", "definite_integrals",
      r"חשבו את נפח גוף הסיבוב הנוצר כסיבוב של התחום המישורי הכלוא בין הקווים: "
      r"$y=\sin^2\left((B+1)x\right),\ y=0,\ x=0,\ x=\frac{\pi}{B+1}$ סביב ציר ה-$y$.",
      part="ב", contextId="c0"),
]

exam = {
    "examCode": "22B-A",
    "examLabel": "מבחן סוף סמסטר א' תשפ\"ב, מועד ב'",
    "year": 2022,
    "examDate": "22/02/2022",
    "sourceFile": "calculus-1/22B-A exam.pdf",
    "solutionFile": "",
    "contexts": {"c0": {"kind": "text", "title": "הפרמטרים A, B, C", "text": CTX0}},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")

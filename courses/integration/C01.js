/* integration course, level 1: הטבלה ופנימית לינארית */
COURSE_LEVEL("integration", {
  id: "C01", order: 1, icon: "📘", title: "הטבלה ופנימית לינארית",
  goal: "לפתור אינטגרלים שהם שורה בטבלה, כולל פנימית לינארית ומונה שהוא נגזרת המכנה.",
  source: "ai-verified",
  lesson: { html: String.raw`
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
` },
  questions: [
  {
    "id": "C01-Q1",
    "question": "מהו $\\int\\cos(3x)\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\sin 3x+C$"
      },
      {
        "id": "b",
        "value": "$3\\sin 3x+C$"
      },
      {
        "id": "c",
        "value": "$\\frac{\\sin 3x}{3}+C$"
      },
      {
        "id": "d",
        "value": "$-\\frac{\\sin 3x}{3}+C$"
      }
    ],
    "correctId": "c",
    "explanation": "במקום $x$ מופיע $3x$, ולכן התשובה היא $\\sin(3x)$ חלקי $3$: **$\\frac{\\sin 3x}{3}$**. גזירה: $\\frac{3\\cos3x}{3}=\\cos3x$. ‏$\\sin3x$ נותנת $3\\cos3x$, פי שלושה מהנדרש. ‏$3\\sin3x$ נותנת $9\\cos3x$. המינוס מתאים ל-$\\sin$ ולא ל-$\\cos$.",
    "recap": "פנימית לינארית ax+b: אותה שורה בטבלה, חלקי a"
  },
  {
    "id": "C01-Q2",
    "question": "מהו $\\int e^{2x+1}\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\frac{e^{2x+1}}{2}+C$"
      },
      {
        "id": "b",
        "value": "$e^{2x+1}+C$"
      },
      {
        "id": "c",
        "value": "$2e^{2x+1}+C$"
      },
      {
        "id": "d",
        "value": "$\\frac{e^{2x+1}}{2x+1}+C$"
      }
    ],
    "correctId": "a",
    "explanation": "הפנימית $2x+1$ לינארית עם $a=2$, ולכן **$\\frac{e^{2x+1}}{2}$**. ‏$e^{2x+1}$ נותנת פי שניים. ‏$2e^{2x+1}$ נותנת פי ארבעה. החלוקה ב-$2x+1$ היא כלל החזקה שהוחל על אקספוננט, וגזירתה מוסיפה איבר שלא קיים באינטגרנד.",
    "recap": "אקספוננט עם 2x+1: חלקי המקדם 2, לא חלקי הפנימית"
  },
  {
    "id": "C01-Q3",
    "question": "מהו $\\int\\frac{dx}{3x-2}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\ln|3x-2|+C$"
      },
      {
        "id": "b",
        "value": "$3\\ln|3x-2|+C$"
      },
      {
        "id": "c",
        "value": "$-\\frac{1}{(3x-2)^2}+C$"
      },
      {
        "id": "d",
        "value": "$\\frac{1}{3}\\ln|3x-2|+C$"
      }
    ],
    "correctId": "d",
    "explanation": "שורת הטבלה היא $\\ln|x|$, והפנימית $3x-2$ נותנת **$\\frac13\\ln|3x-2|$**. ‏$\\ln|3x-2|$ מחזירה $\\frac{3}{3x-2}$. ‏$3\\ln$ מחזירה פי תשעה. התשובה האחרונה היא נגזרת של $\\frac1{3x-2}$ ולא אינטגרל שלה.",
    "recap": "1/(ax+b): (1/a)·ln|ax+b|"
  },
  {
    "id": "C01-Q4",
    "question": "מהו $\\int\\frac{2x}{x^2+5}\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\frac{1}{\\sqrt5}\\arctan\\frac{x}{\\sqrt5}+C$"
      },
      {
        "id": "b",
        "value": "$\\ln\\left(x^2+5\\right)+C$"
      },
      {
        "id": "c",
        "value": "$2x\\ln\\left(x^2+5\\right)+C$"
      },
      {
        "id": "d",
        "value": "$\\frac{2}{x^2+5}+C$"
      }
    ],
    "correctId": "b",
    "explanation": "המונה $2x$ הוא בדיוק הנגזרת של המכנה $x^2+5$, ולכן **$\\ln(x^2+5)$** (ללא ערך מוחלט, כי $x^2+5>0$). ‏$\\arctan$ מתאים ל-$\\frac{1}{x^2+5}$ בלי $x$ במונה. שני האחרים לא נותנים את האינטגרנד כשגוזרים.",
    "recap": "מונה = נגזרת המכנה ← ln של המכנה"
  },
  {
    "id": "C01-Q5",
    "step": {
      "type": "numeric",
      "prompt": "$\\int\\frac{dx}{4x+1}=k\\ln|4x+1|+C$. מהו $k$ ?",
      "answer": 0.25,
      "tol": 0,
      "explain": "הפנימית $4x+1$ מגיעה עם $a=4$, ולכן $k=\\frac14=0.25$. גזירה: $\\frac14\\cdot\\frac{4}{4x+1}=\\frac{1}{4x+1}$."
    },
    "recap": "1/(ax+b): המקדם k הוא 1/a"
  },
  {
    "id": "C01-Q6",
    "question": "מהו $\\int\\frac{dx}{x^2+9}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\arctan\\frac{x}{3}+C$"
      },
      {
        "id": "b",
        "value": "$\\frac{1}{9}\\arctan\\frac{x}{9}+C$"
      },
      {
        "id": "c",
        "value": "$\\frac{1}{3}\\arctan\\frac{x}{3}+C$"
      },
      {
        "id": "d",
        "value": "$\\frac12\\ln\\left(x^2+9\\right)+C$"
      }
    ],
    "correctId": "c",
    "explanation": "השורה בטבלה: $\\frac1a\\arctan\\frac xa$ עם $a=3$, כלומר **$\\frac13\\arctan\\frac x3$**. בלי ה-$\\frac13$ הגזירה נותנת $\\frac{3}{x^2+9}$. ‏$\\ln$ מתאים למונה $x$, שלא קיים כאן.",
    "recap": "1/(a²+x²): (1/a)·arctan(x/a)"
  }
],
});

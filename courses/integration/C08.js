/* integration course, level 8: הצבות מיוחדות: eˣ, √x, טריגונומטריה */
COURSE_LEVEL("integration", {
  id: "C08", order: 8, icon: "🎯", title: "הצבות מיוחדות: eˣ, √x, טריגונומטריה",
  goal: "להחליף $e^x$, שורש או $\\tan(x/2)$ כך שהאינטגרל יהפוך לרציונלי, ולהמשיך עד הסוף.",
  source: "ai-verified",
  lesson: { html: String.raw`
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
` },
  questions: [
  {
    "id": "C08-Q1",
    "question": "מהו $\\int\\frac{dx}{e^x+1}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\ln\\left(e^x+1\\right)+C$"
      },
      {
        "id": "b",
        "value": "$-\\ln\\left(e^x+1\\right)+C$"
      },
      {
        "id": "c",
        "value": "$x+\\ln\\left(e^x+1\\right)+C$"
      },
      {
        "id": "d",
        "value": "$x-\\ln\\left(e^x+1\\right)+C$"
      }
    ],
    "correctId": "d",
    "explanation": "עם $t=e^x$: ‏$\\int\\frac{dt}{t(t+1)}=\\int\\left(\\frac1t-\\frac1{t+1}\\right)dt=\\ln t-\\ln(t+1)$. מחזירים $\\ln t=x$ ומקבלים **$x-\\ln(e^x+1)$**. ‏$\\ln(e^x+1)$ לבדו נותן $\\frac{e^x}{e^x+1}$, שהוא האינטגרנד של $\\frac{e^x}{e^x+1}$ ולא של השאלה.",
    "recap": "רציונלי ב-$e^x$: $t=e^x$, ואז שברים חלקיים"
  },
  {
    "id": "C08-Q2",
    "question": "מהו $\\int e^{\\sqrt{x}}\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$2e^{\\sqrt x}+C$"
      },
      {
        "id": "b",
        "value": "$2\\left(\\sqrt x-1\\right)e^{\\sqrt x}+C$"
      },
      {
        "id": "c",
        "value": "$2\\left(\\sqrt x+1\\right)e^{\\sqrt x}+C$"
      },
      {
        "id": "d",
        "value": "$\\frac{e^{\\sqrt x}}{\\sqrt x}+C$"
      }
    ],
    "correctId": "b",
    "explanation": "‏$t=\\sqrt x$, ‏$dx=2t\\,dt$: ‏$2\\int te^{t}dt=2(t-1)e^{t}$. התשובה **$2(\\sqrt x-1)e^{\\sqrt x}$**. ‏$2e^{\\sqrt x}$ מתעלמת מהגורם $t$. ‏$(\\sqrt x+1)$ שגוי בסימן. ‏$\\frac{e^{\\sqrt x}}{\\sqrt x}$ מניח כלל חזקה על הפנימית.",
    "recap": "√x בתוך הביטוי: t = √x ואז בחלקים"
  },
  {
    "id": "C08-Q3",
    "question": "מהו $\\int\\frac{\\sin x}{1+\\cos^2x}\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\arctan(\\cos x)+C$"
      },
      {
        "id": "b",
        "value": "$-\\arctan(\\sin x)+C$"
      },
      {
        "id": "c",
        "value": "$-\\arctan(\\cos x)+C$"
      },
      {
        "id": "d",
        "value": "$\\ln\\left(1+\\cos^2x\\right)+C$"
      }
    ],
    "correctId": "c",
    "explanation": "‏$t=\\cos x$, ‏$dt=-\\sin x\\,dx$, ולכן $-\\int\\frac{dt}{1+t^2}=-\\arctan t$. הסימן המינוס חיוני. ‏$\\arctan(\\sin x)$ מתאים ל-$\\frac{\\cos x}{1+\\sin^2x}$. ‏$\\ln$ מתאים אם המונה היה $\\sin x\\cos x$.",
    "recap": "sin x dx = −dt: מחליפים בסימן"
  },
  {
    "id": "C08-Q4",
    "question": "איזו הצבה מחזירה את $\\int\\frac{dx}{2+\\cos x}$ לאינטגרל רציונלי ב-$t$ ?",
    "options": [
      {
        "id": "a",
        "value": "$t=\\tan\\frac x2$"
      },
      {
        "id": "b",
        "value": "$t=\\cos x$"
      },
      {
        "id": "c",
        "value": "$t=\\sin x$"
      },
      {
        "id": "d",
        "value": "$t=2+\\cos x$"
      }
    ],
    "correctId": "a",
    "explanation": "אין $\\sin x\\,dx$ באינטגרנד, ולכן $t=\\cos x$ משאירה $dx=-\\frac{dt}{\\sqrt{1-t^2}}$ (שורש): לא רציונלי. ההצבה האוניברסלית $t=\\tan\\frac x2$ נותנת $\\int\\frac{2\\,dt}{3+t^2}$, כלומר $\\frac{2}{\\sqrt3}\\arctan\\frac{\\tan(x/2)}{\\sqrt3}$. אפשר לגזור ולוודא. ‏$t=\\sin x$ ו-$t=2+\\cos x$ משאירות גם שורשים.",
    "recap": "אין sin x dx: הצבה אוניברסלית t = tan(x/2)"
  },
  {
    "id": "C08-Q5",
    "step": {
      "type": "numeric",
      "prompt": "בהצבה $t=\\tan\\frac x2$ מתקבל $dx=\\frac{c\\,dt}{1+t^2}$. מהו $c$ ?",
      "answer": 2,
      "tol": 0,
      "explain": "‏$x=2\\arctan t$, ולכן $dx=\\frac{2\\,dt}{1+t^2}$. כלומר $c=2$."
    },
    "recap": "dx = 2dt/(1+t²) בהצבה האוניברסלית"
  },
  {
    "id": "C08-Q6",
    "question": "מהו $\\int x\\arctan\\left(x^2\\right)dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\frac{x^2}{2}\\arctan\\left(x^2\\right)-\\frac12\\ln\\left(1+x^4\\right)+C$"
      },
      {
        "id": "b",
        "value": "$\\frac12\\arctan\\left(x^2\\right)+C$"
      },
      {
        "id": "c",
        "value": "$\\frac{x^2}{2}\\arctan\\left(x^2\\right)+\\frac14\\ln\\left(1+x^4\\right)+C$"
      },
      {
        "id": "d",
        "value": "$\\frac{x^2}{2}\\arctan\\left(x^2\\right)-\\frac14\\ln\\left(1+x^4\\right)+C$"
      }
    ],
    "correctId": "d",
    "explanation": "קודם הצבה $t=x^2$, ‏$x\\,dx=\\frac12dt$: ‏$\\frac12\\int\\arctan t\\,dt=\\frac12\\left(t\\arctan t-\\frac12\\ln(1+t^2)\\right)$. מחזירים: **$\\frac{x^2}{2}\\arctan x^2-\\frac14\\ln(1+x^4)$**. ‏$\\frac12\\ln$ שוכחת את חצי החצי. ‏$\\frac12\\arctan x^2$ מתעלמת מהחלקים. הסימן בתשובה $\\frac{x^2}{2}\\arctan\\left(x^2\\right)+\\frac14\\ln\\left(1+x^4\\right)+C$ הפוך.",
    "recap": "הצבה t = x² ואז בחלקים"
  }
],
});

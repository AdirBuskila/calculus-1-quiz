/* integration course, level 4: בחלקים: ln ו-arctan */
COURSE_LEVEL("integration", {
  id: "C04", order: 4, icon: "🪢", title: "בחלקים: ln ו-arctan",
  goal: "לזהות ש-ln ו-arctan הם תמיד u, ולפתור אינטגרלים שבהם הם לבדם או כפולים בפולינום.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>כשבאינטגרנד יש $\ln x$ או $\arctan x$, הם <b>תמיד $u$</b>, כי נגזרתם פשוטה: $\left(\ln x\right)'=\frac1x$ ו-$\left(\arctan x\right)'=\frac{1}{1+x^2}$. את האינטגרלים שלהם ישירות לא מכירים.</p>
<div class="lesson-formula">$\int\ln x\,dx=x\ln x-x+C$, ‏$\int\arctan x\,dx=x\arctan x-\frac12\ln\left(1+x^2\right)+C$</div>
<p>אלה בחלקים עם $dv=dx$ (כלומר $v=x$): כותבים את $\ln x$ כ-$\ln x\cdot1$.</p>
<div class="lesson-ex">דוגמה: $\int x\ln x\,dx$. ‏$u=\ln x$, ‏$dv=x\,dx$, ‏$du=\frac{dx}{x}$, ‏$v=\frac{x^2}{2}$.<br>
$\int x\ln x\,dx=\frac{x^2}{2}\ln x-\int\frac{x}{2}dx=\frac{x^2}{2}\ln x-\frac{x^2}{4}+C$.</div>
<div class="lesson-rule">🔑 סימן להצלחה: אחרי הבחירה הנכונה ה-$\ln$ או ה-$\arctan$ נעלם מהאינטגרל הנותר. אם הוא נשאר, הבחירה הייתה הפוכה.</div>
<div class="lesson-trap">⚠️ ב-$\arctan$ האינטגרל הנותר הוא $\int\frac{x}{1+x^2}dx$, וזה הצבה (מונה = חצי נגזרת המכנה), לא טבלה ישירה.</div>
<div class="lesson-trap">⚠️ ב-$\int x\arctan x\,dx$ נשאר $\int\frac{x^2}{1+x^2}dx$. מונה מאותה דרגה כמו המכנה: כותבים $\frac{x^2}{1+x^2}=1-\frac{1}{1+x^2}$ ואז $x-\arctan x$.</div>
` },
  questions: [
  {
    "id": "C04-Q1",
    "question": "באינטגרל $\\int x\\ln x\\,dx$ בחלקים, איזו בחירה מעלימה את ה-$\\ln$ ?",
    "options": [
      {
        "id": "a",
        "value": "$u=\\ln x,\\ dv=x\\,dx$"
      },
      {
        "id": "b",
        "value": "$u=x,\\ dv=\\ln x\\,dx$"
      },
      {
        "id": "c",
        "value": "$u=x\\ln x,\\ dv=dx$"
      },
      {
        "id": "d",
        "value": "$u=1,\\ dv=x\\ln x\\,dx$"
      }
    ],
    "correctId": "a",
    "explanation": "עם $u=\\ln x$ מקבלים $v=\\frac{x^2}{2}$ ו-$v\\,du=\\frac{x}{2}dx$, בלי $\\ln$. עם $u=x$ צריך קודם את $v=\\int\\ln x\\,dx=x\\ln x-x$, והאינטגרל הנותר $\\int(x\\ln x-x)dx$ שוב מכיל $\\ln$. הבחירה $u=x\\ln x$ מחזירה $(\\ln x+1)x$, שוב עם $\\ln$. הבחירה $u=1,\\ dv=x\\ln x\\,dx$ היא האינטגרל עצמו.",
    "recap": "ln הוא תמיד u: הנגזרת שלו 1/x מעלימה אותו"
  },
  {
    "id": "C04-Q2",
    "question": "מהו $\\int\\ln x\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$x\\ln x+x+C$"
      },
      {
        "id": "b",
        "value": "$\\frac1x+C$"
      },
      {
        "id": "c",
        "value": "$x\\ln x-1+C$"
      },
      {
        "id": "d",
        "value": "$x\\ln x-x+C$"
      }
    ],
    "correctId": "d",
    "explanation": "‏$u=\\ln x$ ו-$dv=dx$: ‏$x\\ln x-\\int x\\cdot\\frac1x\\,dx=$ **$x\\ln x-x$**. ‏$\\frac1x$ היא הנגזרת של $\\ln x$ ולא האינטגרל. התשובה עם $+x$ שוכחת את המינוס של האינטגרל הנותר. התשובה $x\\ln x-x+C$ מחשבת את $\\int 1\\,dx$ כ-$1$.",
    "recap": "ln x ← x ln x − x"
  },
  {
    "id": "C04-Q3",
    "question": "מהו $\\int x\\ln x\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\frac{x^2}{2}\\ln x-\\frac{x^2}{2}+C$"
      },
      {
        "id": "b",
        "value": "$\\frac{x^2}{2}\\ln x-\\frac{x^2}{4}+C$"
      },
      {
        "id": "c",
        "value": "$\\frac{x^2}{2}\\ln x+\\frac{x^2}{4}+C$"
      },
      {
        "id": "d",
        "value": "$\\frac{x^2}{2}\\cdot\\frac1x+C$"
      }
    ],
    "correctId": "b",
    "explanation": "‏$\\frac{x^2}{2}\\ln x-\\int\\frac{x^2}{2}\\cdot\\frac1x\\,dx=\\frac{x^2}{2}\\ln x-\\frac{x^2}{4}$. הטעות הנפוצה היא $\\frac{x^2}{2}$ במקום $\\frac{x^2}{4}$, כלומר לשכוח את חצי המקדם. התשובה $\\frac{x^2}{2}\\ln x+\\frac{x^2}{4}+C$ שגויה בסימן. האחרונה היא מכפלת הנגזרות.",
    "recap": "x ln x ← (x²/2) ln x − x²/4"
  },
  {
    "id": "C04-Q4",
    "step": {
      "type": "numeric",
      "prompt": "$\\int x\\ln x\\,dx=\\frac{x^2}{2}\\ln x-k\\,x^2+C$. מהו $k$ ?",
      "answer": 0.25,
      "tol": 0,
      "explain": "האינטגרל הנותר $\\int\\frac{x}{2}dx=\\frac{x^2}{4}$, ולכן $k=0.25$."
    },
    "recap": "האינטגרל הנותר ב-x ln x הוא x/2"
  },
  {
    "id": "C04-Q5",
    "question": "מהו $\\int\\arctan x\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$x\\arctan x-\\ln\\left(1+x^2\\right)+C$"
      },
      {
        "id": "b",
        "value": "$x\\arctan x+\\frac12\\ln\\left(1+x^2\\right)+C$"
      },
      {
        "id": "c",
        "value": "$x\\arctan x-\\frac12\\ln\\left(1+x^2\\right)+C$"
      },
      {
        "id": "d",
        "value": "$\\frac{1}{1+x^2}+C$"
      }
    ],
    "correctId": "c",
    "explanation": "‏$u=\\arctan x$, ‏$dv=dx$: ‏$x\\arctan x-\\int\\frac{x}{1+x^2}dx$, והאינטגרל הנותר הוא $\\frac12\\ln(1+x^2)$ (הצבה $t=1+x^2$). התשובות עם $\\ln$ שלם או עם סימן הפוך שוכחות את החצי או את המינוס.",
    "recap": "arctan x ← x arctan x − ½ ln(1+x²)"
  },
  {
    "id": "C04-Q6",
    "question": "מהו $\\int x\\arctan x\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\frac{x^2+1}{2}\\arctan x-\\frac x2+C$"
      },
      {
        "id": "b",
        "value": "$\\frac{x^2}{2}\\arctan x-\\frac x2+C$"
      },
      {
        "id": "c",
        "value": "$\\frac{x^2+1}{2}\\arctan x+\\frac x2+C$"
      },
      {
        "id": "d",
        "value": "$\\frac{x^2}{2}\\arctan x-\\frac12\\ln\\left(1+x^2\\right)+C$"
      }
    ],
    "correctId": "a",
    "explanation": "‏$u=\\arctan x$, ‏$v=\\frac{x^2}{2}$: ‏$\\frac{x^2}{2}\\arctan x-\\frac12\\int\\frac{x^2}{1+x^2}dx$. כתיבה $\\frac{x^2}{1+x^2}=1-\\frac{1}{1+x^2}$ נותנת $\\frac{x^2}{2}\\arctan x-\\frac x2+\\frac12\\arctan x=$ **$\\frac{x^2+1}{2}\\arctan x-\\frac x2$**. מי ששוכח את $\\arctan$ שחוזר מקבל את התשובה $\\frac{x^2}{2}\\arctan x-\\frac x2+C$. האחרונה מערבבת עם הדוגמה של $\\int\\arctan x$.",
    "recap": "x arctan x: האינטגרל הנותר דורש חלוקה x²/(1+x²) = 1 − 1/(1+x²)"
  }
],
});

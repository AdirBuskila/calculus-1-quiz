/* integration course, level 2: הצבה: פנימית ונגזרתה */
COURSE_LEVEL("integration", {
  id: "C02", order: 2, icon: "🔁", title: "הצבה: פנימית ונגזרתה",
  goal: "לזהות פונקציה פנימית שנגזרתה מופיעה באינטגרנד, ולבצע את ההצבה בלי להשאיר x.",
  source: "ai-verified",
  lesson: { html: String.raw`
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
` },
  questions: [
  {
    "id": "C02-Q1",
    "question": "מהו $\\int x\\,e^{x^2}\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\frac12e^{x^2}+C$"
      },
      {
        "id": "b",
        "value": "$e^{x^2}+C$"
      },
      {
        "id": "c",
        "value": "$2e^{x^2}+C$"
      },
      {
        "id": "d",
        "value": "$\\frac{x^2}{2}e^{x^2}+C$"
      }
    ],
    "correctId": "a",
    "explanation": "עם $t=x^2$ מקבלים $x\\,dx=\\frac12dt$ ו-$\\frac12\\int e^tdt=$ **$\\frac12e^{x^2}$**. ‏$e^{x^2}$ נותנת $2xe^{x^2}$, פי שניים. ‏$2e^{x^2}$ נותנת פי ארבעה. ‏$\\frac{x^2}{2}e^{x^2}$ היא ניסיון להשתמש בכלל החזקה על הגורם $x$.",
    "recap": "הפנימית x² והגורם x הוא חצי מהנגזרת שלה"
  },
  {
    "id": "C02-Q2",
    "question": "באינטגרל $\\int\\frac{\\cos x}{1+\\sin^2x}\\,dx$, איזו הצבה מחזירה אינטגרל רציונלי ב-$t$ בלבד ?",
    "options": [
      {
        "id": "a",
        "value": "$t=\\cos x$"
      },
      {
        "id": "b",
        "value": "$t=1+\\sin^2x$"
      },
      {
        "id": "c",
        "value": "$t=x$"
      },
      {
        "id": "d",
        "value": "$t=\\sin x$"
      }
    ],
    "correctId": "d",
    "explanation": "עם $t=\\sin x$ מקבלים $dt=\\cos x\\,dx$, והאינטגרל הוא **$\\int\\frac{dt}{1+t^2}=\\arctan t$**, כלומר $\\arctan(\\sin x)$. עם $t=\\cos x$ נשאר $\\sin x=\\sqrt{1-t^2}$ במכנה. עם $t=1+\\sin^2x$ נשארים שורשים. ‏$t=x$ לא משנה את האינטגרנד בכלל.",
    "recap": "בוחרים פנימית כך שהגורם האחר הוא הנגזרת שלה"
  },
  {
    "id": "C02-Q3",
    "question": "מהו $\\int\\frac{\\sin x}{\\cos^3x}\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$-\\frac{1}{2\\cos^2x}+C$"
      },
      {
        "id": "b",
        "value": "$\\frac{1}{2\\cos^2x}+C$"
      },
      {
        "id": "c",
        "value": "$\\frac{1}{\\cos^2x}+C$"
      },
      {
        "id": "d",
        "value": "$-\\frac{\\cos^{-2}x}{2}\\cdot\\sin x+C$"
      }
    ],
    "correctId": "b",
    "explanation": "הפנימית $t=\\cos x$, ו-$dt=-\\sin x\\,dx$. מקבלים $-\\int t^{-3}dt=\\frac{1}{2t^2}$, כלומר **$\\frac{1}{2\\cos^2x}$**. מי ששכח את המינוס של $dt$ מקבל את הסימן ההפוך. ‏$\\frac{1}{\\cos^2x}$ נותנת פי שניים. התשובה $-\\frac{\\cos^{-2}x}{2}\\cdot\\sin x+C$ משאירה גורם $\\sin x$ שהיה אמור להיעלם.",
    "recap": "sin x dx = -dt כש-t = cos x"
  },
  {
    "id": "C02-Q4",
    "step": {
      "type": "numeric",
      "prompt": "$\\int x\\left(x^2+1\\right)^3dx=k\\left(x^2+1\\right)^4+C$. מהו $k$ ?",
      "answer": 0.125,
      "tol": 0,
      "explain": "עם $t=x^2+1$ מקבלים $x\\,dx=\\frac12dt$, ו-$\\frac12\\int t^3dt=\\frac{t^4}{8}$. לכן $k=\\frac18=0.125$."
    },
    "recap": "x dx = dt/2: מוסיפים 1/2 ואז כלל החזקה"
  },
  {
    "id": "C02-Q5",
    "question": "מהו $\\int\\frac{(\\ln x)^2}{x}\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\frac{(\\ln x)^3}{3x}+C$"
      },
      {
        "id": "b",
        "value": "$\\frac{(\\ln x)^2}{2}+C$"
      },
      {
        "id": "c",
        "value": "$\\frac{(\\ln x)^3}{3}+C$"
      },
      {
        "id": "d",
        "value": "$2\\ln x+C$"
      }
    ],
    "correctId": "c",
    "explanation": "הפנימית $t=\\ln x$ עם $dt=\\frac{dx}{x}$. מקבלים $\\int t^2dt=\\frac{t^3}{3}$, כלומר **$\\frac{\\ln^3x}{3}$**. אין סיבה לחלק ב-$x$ שוב: ה-$\\frac1x$ כבר נבלע ב-$dt$. ‏$\\frac{\\ln^2x}{2}$ היא החזקה השגויה (האינטגרל של $\\ln x/x$).",
    "recap": "ln x עם dx/x: t = ln x"
  },
  {
    "id": "C02-Q6",
    "step": {
      "type": "findbug",
      "prompt": "בפתרון של $\\int x^2e^{x^3}dx$ יש שורה אחת שגויה. איזו ?",
      "lines": [
        "בוחרים $t=x^3$ וכותבים $dt=3x^2\\,dx$.",
        "לכן $x^2\\,dx=3\\,dt$ והאינטגרל הוא $3\\int e^{t}\\,dt$.",
        "$3\\int e^{t}\\,dt=3e^{t}+C$.",
        "מחזירים: $3e^{x^3}+C$."
      ],
      "bugIndex": 1,
      "explain": "מ-$dt=3x^2\\,dx$ מקבלים $x^2\\,dx=\\frac13dt$ ולא $3\\,dt$. התשובה הנכונה היא $\\frac13e^{x^3}+C$. הגזירה של $3e^{x^3}$ נותנת $9x^2e^{x^3}$."
    },
    "recap": "מבודדים את הגורם: x² dx = dt/3, לא 3 dt"
  }
],
});

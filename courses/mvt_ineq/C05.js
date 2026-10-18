/* mvt_ineq course, level 5: חסם על |f'|: אי-שוויונות מהצורה |f(b)−f(a)| ≤ M|b−a| */
COURSE_LEVEL("mvt_ineq", {
  id: "C05", order: 5, icon: "🧱", title: "חסם על |f'|: אי-שוויונות מהצורה |f(b)−f(a)| ≤ M|b−a|",
  goal: "למצוא חסם על $|f'|$ בכל התחום ולהסיק ממנו אי-שוויון בין שני ערכים כלשהם של הפונקציה.",
  source: "ai-verified",
  lesson: { html: String.raw`
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
` },
  questions: [
  {
    "id": "C05-Q1",
    "step": {
      "type": "numeric",
      "prompt": "מהו הקבוע $M$ הקטן ביותר שעבורו $|\\sin2b-\\sin2a|\\le M|b-a|$ לכל $a,b$ ?",
      "answer": 2,
      "tol": 0,
      "explain": "‏$f(t)=\\sin2t$ ולכן $f'(t)=2\\cos2t$ ו-$|f'|\\le2$, עם שוויון ב-$t=0$. לכן $M=2$ מספיק. אי אפשר פחות: עבור $a=0$ ו-$b$ קטן, $\\sin2b\\approx2b$, ולכן $M<2$ היה נכשל."
    },
    "recap": "M הוא הערך המקסימלי של |f'|"
  },
  {
    "id": "C05-Q2",
    "step": {
      "type": "numeric",
      "prompt": "מהו הקבוע $M$ הקטן ביותר שעבורו $|\\arctan b-\\arctan a|\\le M|b-a|$ לכל $a,b$ ?",
      "answer": 1,
      "tol": 0,
      "explain": "‏$f'(t)=\\frac{1}{1+t^2}$ חיובית וקטנה או שווה ל-$1$, עם שוויון ב-$t=0$. לכן $M=1$. ל-$M<1$ אין מספיק: עבור $a=0$ ו-$b$ קטן, $\\arctan b\\approx b$."
    },
    "recap": "arctan' = 1/(1+t²) ≤ 1"
  },
  {
    "id": "C05-Q3",
    "question": "האם קיים קבוע $M$ כך ש-$|b^2-a^2|\\le M|b-a|$ לכל $a,b\\in\\mathbb R$ ?",
    "options": [
      {
        "id": "a",
        "value": "כן, $M=1$"
      },
      {
        "id": "b",
        "value": "לא, כי $f'(t)=2t$ אינה חסומה"
      },
      {
        "id": "c",
        "value": "כן, $M=2$"
      },
      {
        "id": "d",
        "value": "כן, $M=4$"
      }
    ],
    "correctId": "b",
    "explanation": "‏$|b^2-a^2|=|b+a|\\,|b-a|$, והגורם $|a+b|$ אינו חסום. לכל $M$ אפשר לקחת $a=M$ ו-$b=M+1$: ‏$|b^2-a^2|=2M+1>M=M|b-a|$. לכן אין קבוע, והערכים $M=1,2,4$ נכשלים כבר ב-$a=10,b=11$ ($21$ מול $1,2,4$).",
    "recap": "f' לא חסומה ← אין קבוע M"
  },
  {
    "id": "C05-Q4",
    "question": "עבור $f(t)=e^{\\sin^2t}$ מתקבל $f'(t)=e^{\\sin^2t}\\sin2t$. מהחסמים $e^{\\sin^2t}\\le e$ ו-$|\\sin2t|\\le1$ מסיקים אי-שוויון מהצורה $|f(b)-f(a)|\\le M|b-a|$. איזה ערך של $M$ מתקיים לכל $a,b$ ?",
    "options": [
      {
        "id": "a",
        "value": "$M=\\frac e2$"
      },
      {
        "id": "b",
        "value": "$M=1$"
      },
      {
        "id": "c",
        "value": "$M=e$"
      },
      {
        "id": "d",
        "value": "$M=\\frac32$"
      }
    ],
    "correctId": "c",
    "explanation": "‏$|f'(t)|=e^{\\sin^2t}\\,|\\sin2t|\\le e\\cdot1=e$, ולכן $|f(b)-f(a)|\\le e|b-a|$ לכל $a,b$. הערכים הקטנים יותר נכשלים: ב-$a=0.9,\\ b=1.1$ ההפרש $e^{\\sin^21.1}-e^{\\sin^20.9}\\approx0.37$ ו-$b-a=0.2$, כלומר היחס $\\approx1.83$, גדול מ-$1$, מ-$\\frac32$ ומ-$\\frac e2\\approx1.36$.",
    "recap": "מכפילים את החסמים של הגורמים ב-f'"
  },
  {
    "id": "C05-Q5",
    "step": {
      "type": "numeric",
      "prompt": "מהו הקבוע $M$ הקטן ביותר שעבורו $|\\sqrt b-\\sqrt a|\\le M|b-a|$ לכל $a,b\\ge1$ ? (עשרוני)",
      "answer": 0.5,
      "tol": 0,
      "explain": "‏$f'(t)=\\frac{1}{2\\sqrt t}$ יורדת, ולכן עבור $t\\ge1$ היא קטנה מ-$\\frac12$ וקרובה ל-$\\frac12$ כש-$t$ קרוב ל-$1$. כלומר $M=\\frac12$ מספיק, ואי אפשר פחות."
    },
    "recap": "בקטע t ≥ 1, ‏|f'| ≤ 1/2"
  }
],
});

/* mvt_ineq course, level 4: שני קצוות חופשיים: a ו-b */
COURSE_LEVEL("mvt_ineq", {
  id: "C04", order: 4, icon: "↔️", title: "שני קצוות חופשיים: a ו-b",
  goal: "להפעיל לגרנז' בקטע $[a,b]$ כללי, ולהחליט איזה קצה נותן את החסם התחתון ואיזה את העליון.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>לפעמים שני הקצוות חופשיים, $0<a<b$, ולא רק $[0,x]$. הדרך זהה, אבל צריך להחליט איזה קצה נותן איזה חסם.</p>
<div class="lesson-rule">🔑 $f'$ עולה: החסם התחתון הוא $f'(a)$ והעליון $f'(b)$. ‏$f'$ יורדת: להפך, התחתון $f'(b)$ והעליון $f'(a)$.</div>
<div class="lesson-ex">דוגמה: $f=\ln t$ בקטע $[a,b]$. ‏$\frac{\ln b-\ln a}{b-a}=\frac1c$ עם $a<c<b$. ‏$\frac1t$ יורדת, ולכן $\frac1b<\frac1c<\frac1a$.<br>
מכפילים ב-$b-a>0$: $\frac{b-a}{b}<\ln b-\ln a<\frac{b-a}{a}$.</div>
<p>עבור $f=\arcsin t$ ו-$0<a<b<1$ הנגזרת $\frac{1}{\sqrt{1-t^2}}$ עולה, ולכן $\frac{1}{\sqrt{1-a^2}}<f'(c)<\frac{1}{\sqrt{1-b^2}}$.</p>
<div class="lesson-trap">⚠️ כשעוברים להציב מספרים, מציבים את הקצה הנכון בכל חסם. אם הקצוות מוחלפים, הסדר מתהפך והאי-שוויון שגוי.</div>
` },
  questions: [
  {
    "id": "C04-Q1",
    "question": "$f(t)=\\ln t$, ו-$0<a<c<b$. בין אילו ערכים נמצא $f'(c)=\\frac1c$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\frac1a<\\frac1c<\\frac1b$"
      },
      {
        "id": "b",
        "value": "$\\frac1b<\\frac1c<\\frac1a$"
      },
      {
        "id": "c",
        "value": "$a<\\frac1c<b$"
      },
      {
        "id": "d",
        "value": "$\\frac1c<\\frac1b$"
      }
    ],
    "correctId": "b",
    "explanation": "‏$\\frac1t$ יורדת. ‏$c$ גדולה מ-$a$ וקטנה מ-$b$, ולכן $\\frac1c$ קטן מ-$\\frac1a$ וגדול מ-$\\frac1b$. הסדר $\\frac1a<\\frac1c<\\frac1b$ הוא של פונקציה עולה. בבדיקה ב-$a=1,\\ b=2,\\ c=1.5$: ‏$\\frac1c=0.67$, בין $0.5=\\frac1b$ ל-$1=\\frac1a$. האפשרויות $a<\\frac1c<b$ ו-$\\frac1c<\\frac1b$ נכשלות באותה בדיקה.",
    "recap": "1/t יורדת: הקצה הימני נותן את החסם התחתון"
  },
  {
    "id": "C04-Q2",
    "question": "מה מתקבל מהכפלת $\\frac1b<\\frac{\\ln b-\\ln a}{b-a}<\\frac1a$ ב-$b-a>0$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\frac{b-a}{a}<\\ln b-\\ln a<\\frac{b-a}{b}$"
      },
      {
        "id": "b",
        "value": "$\\frac{1}{b}<\\ln b-\\ln a<\\frac1a$"
      },
      {
        "id": "c",
        "value": "$\\frac{b-a}{b}<\\ln b-\\ln a<\\frac{b-a}{a}$"
      },
      {
        "id": "d",
        "value": "$b(b-a)<\\ln b-\\ln a<a(b-a)$"
      }
    ],
    "correctId": "c",
    "explanation": "מכפילים כל אגף ב-$b-a$: ‏$\\frac1b(b-a)=\\frac{b-a}{b}$ ו-$\\frac1a(b-a)=\\frac{b-a}{a}$, והאמצע הופך ל-$\\ln b-\\ln a$. הסדר ההפוך נכשל ב-$a=1,\\ b=2$: ‏$1<0.69$ אינו נכון. האפשרות בלי הכפלה ב-$b-a$ נכשלת ב-$a=1,\\ b=3$: ‏$\\ln3\\approx1.10$ אינו קטן מ-$\\frac1a=1$. והאפשרות עם $b(b-a)$ נכשלת ב-$a=1,\\ b=2$: ‏$2<0.69$ שקר.",
    "recap": "הכפל ב-(b−a) מעביר את b−a לשני האגפים החיצוניים"
  },
  {
    "id": "C04-Q3",
    "question": "$f(t)=\\arcsin t$ ו-$0<a<c<b<1$. בין אילו ערכים נמצא $f'(c)$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\frac{1}{\\sqrt{1-a^2}}<f'(c)<\\frac{1}{\\sqrt{1-b^2}}$"
      },
      {
        "id": "b",
        "value": "$\\frac{1}{\\sqrt{1-b^2}}<f'(c)<\\frac{1}{\\sqrt{1-a^2}}$"
      },
      {
        "id": "c",
        "value": "$a<f'(c)<b$"
      },
      {
        "id": "d",
        "value": "$0<f'(c)<\\frac{1}{\\sqrt{1-a^2}}$"
      }
    ],
    "correctId": "a",
    "explanation": "‏$\\frac{1}{\\sqrt{1-t^2}}$ עולה ב-$(0,1)$, ולכן החסם התחתון בא מ-$a$ והעליון מ-$b$. הסדר ההפוך הוא של פונקציה יורדת. הערך $f'(c)$ גדול מ-$1$ ולכן אינו בין $a$ ל-$b$. האפשרות האחרונה נכשלת ב-$a=0.5,\\ c=0.8$: ‏$f'(c)=1.67$ גדול מ-$\\frac{1}{\\sqrt{1-0.25}}=1.155$.",
    "recap": "$\\arcsin'$ עולה: התחתון מ-$a$ והעליון מ-$b$"
  },
  {
    "id": "C04-Q4",
    "step": {
      "type": "numeric",
      "prompt": "מהאי-שוויון $\\frac{b-a}{b}<\\ln b-\\ln a<\\frac{b-a}{a}$ עם $a=2,\\ b=3$ מקבלים חסם עליון על $\\ln\\frac32$. מהו ? (עשרוני)",
      "answer": 0.5,
      "tol": 0,
      "explain": "החסם העליון הוא $\\frac{b-a}{a}=\\frac{1}{2}=0.5$, והתחתון $\\frac{b-a}{b}=\\frac13$. בפועל $\\ln1.5\\approx0.405$, בין השניים."
    },
    "recap": "העליון הוא (b−a)/a: מחלקים בקצה השמאלי"
  },
  {
    "id": "C04-Q5",
    "step": {
      "type": "numeric",
      "prompt": "מהחסם $\\arcsin b-\\arcsin a>\\frac{b-a}{\\sqrt{1-a^2}}$ עם $a=0.5,\\ b=0.6$ מקבלים חסם תחתון על $\\arcsin0.6-\\arcsin0.5$. מהו ? (עשרוני)",
      "answer": 0.1155,
      "tol": 0.0005,
      "explain": "הצבה: $\\frac{0.1}{\\sqrt{1-0.25}}=\\frac{0.1}{0.8660}\\approx0.1155$. בפועל ההפרש הוא $\\arcsin0.6-\\arcsin0.5\\approx0.1199$, גדול מהחסם התחתון וקטן מהעליון $\\frac{0.1}{\\sqrt{1-0.36}}=0.125$."
    },
    "recap": "החסם התחתון משתמש ב-a, הקצה הקטן"
  },
  {
    "id": "C04-Q6",
    "question": "$f(t)=\\sqrt t$ ו-$0<a<b$. מה מתקבל מלגרנז' ? (רמז: ‏$f'(t)=\\frac{1}{2\\sqrt t}$ יורדת)",
    "options": [
      {
        "id": "a",
        "value": "$\\frac{b-a}{2\\sqrt a}<\\sqrt b-\\sqrt a<\\frac{b-a}{2\\sqrt b}$"
      },
      {
        "id": "b",
        "value": "$\\frac{b-a}{2b}<\\sqrt b-\\sqrt a<\\frac{b-a}{2a}$"
      },
      {
        "id": "c",
        "value": "$\\frac{1}{2\\sqrt b}<\\sqrt b-\\sqrt a<\\frac{1}{2\\sqrt a}$"
      },
      {
        "id": "d",
        "value": "$\\frac{b-a}{2\\sqrt b}<\\sqrt b-\\sqrt a<\\frac{b-a}{2\\sqrt a}$"
      }
    ],
    "correctId": "d",
    "explanation": "הנגזרת יורדת, לכן $\\frac{1}{2\\sqrt b}<f'(c)<\\frac{1}{2\\sqrt a}$, ואחרי הכפלה ב-$b-a$ מקבלים את האפשרות הנכונה. הסדר ההפוך הוא של פונקציה עולה. האפשרות עם $2b$ ו-$2a$ שוכחת את השורש: ב-$a=1,\\ b=100$ היא נותנת $0.495<9<49.5$, שקר. והאפשרות האחרונה שוכחת להכפיל ב-$b-a$ ונכשלת באותה נקודה ($0.05<9<0.5$ שקר).",
    "recap": "לפני שמציבים: האם הנגזרת עולה או יורדת ?"
  }
],
});

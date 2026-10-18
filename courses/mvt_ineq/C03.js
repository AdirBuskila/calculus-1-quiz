/* mvt_ineq course, level 3: בחירת הפונקציה והקטע */
COURSE_LEVEL("mvt_ineq", {
  id: "C03", order: 3, icon: "🎯", title: "בחירת הפונקציה והקטע",
  goal: "לבחור פונקציה וקטע כך שהמנה של לגרנז' תהיה הביטוי שבאמצע האי-שוויון, ושהתנאים יתקיימו.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>החלק הקשה בשאלה הוא <b>איזו פונקציה ואיזה קטע</b>. כלל אצבע: מסתכלים על הביטוי באמצע האי-שוויון, ומחפשים $f$ ו-$[a,b]$ כך ש-$\frac{f(b)-f(a)}{b-a}$ שווה בדיוק לו.</p>
<ul>
<li>הביטוי באמצע הוא $\ln(1+x)$ ← $f(t)=\ln(1+t)$ בקטע $[0,x]$, כי $\frac{\ln(1+x)-\ln1}{x-0}=\frac{\ln(1+x)}{x}$.</li>
<li>הביטוי באמצע הוא $\arcsin a$ ← $f(t)=\arcsin t$ בקטע $[0,a]$.</li>
<li>הביטוי באמצע הוא $\tan x$ ← $f(t)=\tan t$ בקטע $[0,x]$.</li>
<li>הביטוי באמצע הוא $\ln x$ עם $x>1$ ← $f(t)=\ln t$ בקטע $[1,x]$, כי $\ln1=0$.</li>
</ul>
<p>הקצה שבו הפונקציה מתאפסת ($0$ או $1$) מפשט את ההפרש.</p>
<div class="lesson-rule">🔑 לפני שמתחילים: האם הפונקציה מוגדרת ורציפה בכל הקטע הסגור? אם הקטע כולל נקודה שבה היא לא מוגדרת, בוחרים קטע אחר.</div>
<div class="lesson-trap">⚠️ $\ln t$ בקטע $[0,x]$ לא עובד ($\ln0$ לא מוגדר), וגם $\tan t$ בקטע $[0,\frac\pi2]$ לא עובד ($\tan$ לא מוגדרת ב-$\frac\pi2$).</div>
` },
  questions: [
  {
    "id": "C03-Q1",
    "question": "כדי להוכיח $\\frac{x}{1+x}<\\ln(1+x)<x$ עבור $x>0$ מפעילים את לגרנז' בקטע $[0,x]$. איזו $f$ נותנת $\\frac{f(x)-f(0)}{x-0}=\\frac{\\ln(1+x)}{x}$ ומקיימת את התנאים ?",
    "options": [
      {
        "id": "a",
        "value": "$f(t)=\\ln t$"
      },
      {
        "id": "b",
        "value": "$f(t)=t-\\ln(1+t)$"
      },
      {
        "id": "c",
        "value": "$f(t)=e^t$"
      },
      {
        "id": "d",
        "value": "$f(t)=\\ln(1+t)$"
      }
    ],
    "correctId": "d",
    "explanation": "‏$f(t)=\\ln(1+t)$ נותנת $\\frac{\\ln(1+x)-\\ln1}{x}=\\frac{\\ln(1+x)}{x}$ והיא רציפה וגזירה בכל $[0,x]$. ‏$\\ln t$ לא מוגדרת ב-$0$. ‏$t-\\ln(1+t)$ נותנת $1-\\frac{\\ln(1+x)}{x}$, ו-$e^t$ נותנת $\\frac{e^x-1}{x}$. לאף אחת מהן המנה אינה $\\frac{\\ln(1+x)}{x}$.",
    "recap": "בוחרים f שההפרש שלה על הקטע הוא בדיוק הביטוי שבאמצע"
  },
  {
    "id": "C03-Q2",
    "question": "להוכחת $a<\\arcsin a<\\frac{a}{\\sqrt{1-a^2}}$ עבור $0<a<1$ מפעילים את לגרנז' בקטע $[0,a]$. איזו $f$ נותנת מנה השווה ל-$\\frac{\\arcsin a}{a}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$f(t)=\\sin t$"
      },
      {
        "id": "b",
        "value": "$f(t)=\\arcsin t$"
      },
      {
        "id": "c",
        "value": "$f(t)=\\arcsin t-t$"
      },
      {
        "id": "d",
        "value": "$f(t)=\\frac{t}{\\sqrt{1-t^2}}$"
      }
    ],
    "correctId": "b",
    "explanation": "‏$\\arcsin$ מוגדרת ורציפה ב-$[0,a]$ וגזירה ב-$(0,a)$ (כי $a<1$), והמנה היא $\\frac{\\arcsin a-0}{a}$. ‏$\\sin t$ נותנת $\\frac{\\sin a}{a}$, ‏$\\arcsin t-t$ נותנת $\\frac{\\arcsin a}{a}-1$, ו-$\\frac{t}{\\sqrt{1-t^2}}$ נותנת $\\frac{1}{\\sqrt{1-a^2}}$.",
    "recap": "הביטוי באמצע הוא f(a), עם f(0)=0 בקצה השני"
  },
  {
    "id": "C03-Q3",
    "question": "להוכחת $\\tan x>x$ עבור $0<x<\\frac\\pi2$ בוחרים $f(t)=\\tan t$. באיזה קטע מתקיימים תנאי המשפט לכל $x$ כזה, והמנה היא $\\frac{\\tan x}{x}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\left[0,\\frac\\pi2\\right]$"
      },
      {
        "id": "b",
        "value": "$[0,\\pi]$"
      },
      {
        "id": "c",
        "value": "$[0,x]$"
      },
      {
        "id": "d",
        "value": "$\\left[x,\\frac\\pi2\\right]$"
      }
    ],
    "correctId": "c",
    "explanation": "‏$\\tan t$ רציפה בכל $[0,x]$ כל עוד $x<\\frac\\pi2$, והמנה היא $\\frac{\\tan x-\\tan0}{x-0}=\\frac{\\tan x}{x}$. בשלושת הקטעים האחרים הנקודה $\\frac\\pi2$ נכללת, ושם $\\tan$ לא מוגדרת, ולכן הרציפות נכשלת. הקטע $\\left[x,\\frac\\pi2\\right]$ גם נותן מנה אחרת.",
    "recap": "הקטע חייב להישאר בתוך תחום הרציפות של הפונקציה"
  },
  {
    "id": "C03-Q4",
    "question": "להוכחת $\\frac{x-1}{x}<\\ln x<x-1$ עבור $x>1$ מפעילים את לגרנז' על $f(t)=\\ln t$. באיזה קטע המנה היא $\\frac{\\ln x}{x-1}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$[1,x]$"
      },
      {
        "id": "b",
        "value": "$[0,x]$"
      },
      {
        "id": "c",
        "value": "$[0,1]$"
      },
      {
        "id": "d",
        "value": "$[x,2x]$"
      }
    ],
    "correctId": "a",
    "explanation": "‏$\\ln1=0$, ולכן $\\frac{\\ln x-\\ln1}{x-1}=\\frac{\\ln x}{x-1}$, והקטע $[1,x]$ נמצא כולו בתחום של $\\ln$. ‏$[0,x]$ ו-$[0,1]$ כוללים את $0$ שבו $\\ln$ לא מוגדרת. ‏$[x,2x]$ נותן את המנה $\\frac{\\ln2}{x}$ (השונה מ-$\\frac{\\ln x}{x-1}$).",
    "recap": "ln 1 = 0, ולכן הקצה הוא 1"
  },
  {
    "id": "C03-Q5",
    "question": "להוכחת $e^{\\sin^2b}-e^{\\sin^2a}\\le e(b-a)$ עבור $a<b$ מפעילים את לגרנז' בקטע $[a,b]$. איזו $f$ נותנת את ההפרש בדיוק ?",
    "options": [
      {
        "id": "a",
        "value": "$f(t)=e^{t}$"
      },
      {
        "id": "b",
        "value": "$f(t)=\\sin^2t$"
      },
      {
        "id": "c",
        "value": "$f(t)=e^{\\sin t}$"
      },
      {
        "id": "d",
        "value": "$f(t)=e^{\\sin^2t}$"
      }
    ],
    "correctId": "d",
    "explanation": "‏$f(b)-f(a)$ צריך להיות $e^{\\sin^2b}-e^{\\sin^2a}$, ולכן $f(t)=e^{\\sin^2t}$. ‏$f(t)=e^t$ נותנת $e^b-e^a$, ‏$f(t)=\\sin^2t$ נותנת $\\sin^2b-\\sin^2a$, ו-$f(t)=e^{\\sin t}$ נותנת $e^{\\sin b}-e^{\\sin a}$. הפונקציה $e^{\\sin^2t}$ מוגדרת וגזירה בכל הישר, ולכן כל קטע $[a,b]$ מתאים.",
    "recap": "f(b) − f(a) צריך להתלכד עם ההפרש הנתון"
  },
  {
    "id": "C03-Q6",
    "step": {
      "type": "numeric",
      "prompt": "עבור $f(t)=\\arcsin t$ בקטע $[0,a]$, כמה שווה $f'\\left(\\frac35\\right)$ ? (עשרוני)",
      "answer": 1.25,
      "tol": 0,
      "explain": "‏$f'(t)=\\frac{1}{\\sqrt{1-t^2}}$, ולכן $f'\\left(\\frac35\\right)=\\frac{1}{\\sqrt{1-\\frac9{25}}}=\\frac{1}{\\frac45}=\\frac54=1.25$."
    },
    "recap": "הנגזרת של arcsin היא 1/√(1−t²)"
  }
],
});

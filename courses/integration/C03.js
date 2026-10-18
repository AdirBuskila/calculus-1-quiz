/* integration course, level 3: בחלקים: פולינום כפול eˣ, sin, cos */
COURSE_LEVEL("integration", {
  id: "C03", order: 3, icon: "✂️", title: "בחלקים: פולינום כפול eˣ, sin, cos",
  goal: "לבחור u כפולינום ולפתור אינטגרל מכפלה בסיבוב אחד או בשניים.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>אינטגרציה בחלקים: $\int u\,dv=uv-\int v\,du$. היא באה לעזרה כשיש <b>מכפלה</b> שאין בה פנימית עם נגזרתה.</p>
<h3>איך בוחרים $u$</h3>
<p>מכפלה של פולינום ב-$e^{x}$, $\sin$ או $\cos$: <b>$u=$ הפולינום</b> ו-$dv=$ השאר. כל סיבוב מוריד את דרגת הפולינום ב-1, עד שהוא נעלם.</p>
<div class="lesson-ex">דוגמה: $\int x\,e^{x}dx$. ‏$u=x$, ‏$dv=e^{x}dx$, ‏$du=dx$, ‏$v=e^{x}$.<br>
$\int xe^{x}dx=xe^{x}-\int e^{x}dx=xe^{x}-e^{x}+C=(x-1)e^{x}+C$.</div>
<div class="lesson-rule">🔑 בבחירה ההפוכה ($u=e^{x}$ ו-$dv=x\,dx$) הפולינום עולה בדרגה: $v=\frac{x^2}{2}$ והאינטגרל החדש גרוע מהמקורי.</div>
<p>פולינום מדרגה $n$ דורש $n$ סיבובים. הדרך לא לטעות בסימנים: לכתוב $u,\ du,\ dv,\ v$ בשורה לפני שמציבים.</p>
<div class="lesson-trap">⚠️ מי ששוכח את המינוס ב-$v=-\cos x$ מקבל סימן שגוי בכל התשובה. תמיד בודקים בגזירה.</div>
` },
  questions: [
  {
    "id": "C03-Q1",
    "question": "באינטגרל $\\int x\\sin x\\,dx$ בחלקים, איזו בחירה מקטינה את הבעיה ?",
    "options": [
      {
        "id": "a",
        "value": "$u=x,\\ dv=\\sin x\\,dx$"
      },
      {
        "id": "b",
        "value": "$u=\\sin x,\\ dv=x\\,dx$"
      },
      {
        "id": "c",
        "value": "$u=x\\sin x,\\ dv=dx$"
      },
      {
        "id": "d",
        "value": "$u=1,\\ dv=x\\sin x\\,dx$"
      }
    ],
    "correctId": "a",
    "explanation": "עם $u=x$ מקבלים $du=dx$ ו-$v=-\\cos x$, והאינטגרל החדש $\\int-\\cos x\\,dx$ ללא $x$ כלל. עם $u=\\sin x$ מקבלים $v=\\frac{x^2}{2}$ והאינטגרל החדש $\\int\\frac{x^2}{2}\\cos x\\,dx$ מסובך יותר: הפולינום עלה בדרגה. הבחירה $u=x\\sin x$ מחזירה $\\int\\left(x\\sin x+x^2\\cos x\\right)dx$, גרוע מהמקורי. הבחירה האחרונה היא פשוט האינטגרל המקורי.",
    "recap": "פולינום × $\\sin/\\cos/e^x$: $u$ הוא הפולינום"
  },
  {
    "id": "C03-Q2",
    "question": "מהו $\\int x\\,e^{x}\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$(x+1)e^{x}+C$"
      },
      {
        "id": "b",
        "value": "$xe^{x}+C$"
      },
      {
        "id": "c",
        "value": "$\\frac{x^2}{2}e^{x}+C$"
      },
      {
        "id": "d",
        "value": "$(x-1)e^{x}+C$"
      }
    ],
    "correctId": "d",
    "explanation": "‏$u=x$ ו-$dv=e^xdx$ נותנים $xe^x-\\int e^xdx=$ **$(x-1)e^x$**. ‏$(x+1)e^x$ נובעת מטעות בסימן של האינטגרל השני. ‏$xe^x$ שוכחת את החלק השני בכלל. ‏$\\frac{x^2}{2}e^x$ היא כפל של שני האינטגרלים.",
    "recap": "$xe^x \\to (x-1)e^x$"
  },
  {
    "id": "C03-Q3",
    "question": "מהו $\\int x\\cos x\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$x\\sin x-\\cos x+C$"
      },
      {
        "id": "b",
        "value": "$x\\sin x+\\cos x+C$"
      },
      {
        "id": "c",
        "value": "$-x\\sin x+\\cos x+C$"
      },
      {
        "id": "d",
        "value": "$\\frac{x^2}{2}\\sin x+C$"
      }
    ],
    "correctId": "b",
    "explanation": "‏$u=x$, ‏$v=\\sin x$: ‏$x\\sin x-\\int\\sin x\\,dx=x\\sin x+\\cos x$, כי $\\int\\sin x\\,dx=-\\cos x$. ‏$x\\sin x-\\cos x$ מתקבלת כשמשאירים את המינוס הכפול. ‏$-x\\sin x+\\cos x$ הפוכה בסימן הכולל. ‏$\\frac{x^2}{2}\\sin x$ מתייחסת לאינטגרל כאל מכפלת אינטגרלים.",
    "recap": "xcos x ← x sin x + cos x"
  },
  {
    "id": "C03-Q4",
    "step": {
      "type": "numeric",
      "prompt": "$\\int x\\,e^{2x}dx=\\left(\\frac{x}{2}-a\\right)e^{2x}+C$. מהו $a$ ?",
      "answer": 0.25,
      "tol": 0,
      "explain": "‏$u=x$, ‏$v=\\frac{e^{2x}}{2}$: ‏$\\frac{xe^{2x}}{2}-\\frac12\\int e^{2x}dx=\\frac{xe^{2x}}{2}-\\frac{e^{2x}}{4}$. לכן $a=\\frac14=0.25$."
    },
    "recap": "$v=e^{2x}/2$: הפנימית הלינארית מחלקת ב-2 פעמיים"
  },
  {
    "id": "C03-Q5",
    "question": "מהו $\\int x^2e^{x}\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\left(x^2+2x+2\\right)e^{x}+C$"
      },
      {
        "id": "b",
        "value": "$\\left(x^2-2x\\right)e^{x}+C$"
      },
      {
        "id": "c",
        "value": "$\\left(x^2-2x+2\\right)e^{x}+C$"
      },
      {
        "id": "d",
        "value": "$\\left(x^2-2x+1\\right)e^{x}+C$"
      }
    ],
    "correctId": "c",
    "explanation": "סיבוב ראשון: ‏$x^2e^x-2\\int xe^xdx$. סיבוב שני: ‏$\\int xe^x=(x-1)e^x$. התוצאה $x^2e^x-2(x-1)e^x=$ **$(x^2-2x+2)e^x$**. שאר התשובות נופלות בסימן או במחסור בקבוע ($+2$ נובע מ-$-2\\cdot(-1)$).",
    "recap": "$x^2e^x$: שני סיבובים, סימנים מתחלפים"
  },
  {
    "id": "C03-Q6",
    "step": {
      "type": "order",
      "prompt": "סדרו את הפתרון של $\\int x\\sin x\\,dx$.",
      "lines": [
        "$u=x,\\ dv=\\sin x\\,dx$",
        "$du=dx,\\ v=-\\cos x$",
        "$\\int x\\sin x\\,dx=-x\\cos x+\\int\\cos x\\,dx$",
        "$=-x\\cos x+\\sin x+C$"
      ],
      "explain": "קודם בוחרים $u,dv$, אחר כך מחשבים $du,v$, ואז מציבים בנוסחה ולבסוף פותרים את האינטגרל הנותר."
    },
    "recap": "u,dv ← du,v ← הצבה בנוסחה ← האינטגרל הנותר"
  }
],
});

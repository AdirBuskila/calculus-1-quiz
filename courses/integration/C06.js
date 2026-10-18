/* integration course, level 6: מכנה ריבועי, גורם כפול והשלמה לריבוע */
COURSE_LEVEL("integration", {
  id: "C06", order: 6, icon: "🧮", title: "מכנה ריבועי, גורם כפול והשלמה לריבוע",
  goal: "להשלים לריבוע כש-Δ שלילית, לפרק מונה מעל ריבועי, ולכתוב צורת פירוק נכונה לגורם כפול.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>מכנה ריבועי $x^2+px+q$ מתנהג לפי הדיסקרימיננטה $\Delta=p^2-4q$.</p>
<ul>
<li>$\Delta>0$: מתפרק לשני גורמים לינאריים, ואז שברים חלקיים רגילים (תוצאה: $\ln$).</li>
<li>$\Delta<0$: <b>לא מתפרק</b>. משלימים לריבוע ומקבלים $\arctan$.</li>
</ul>
<div class="lesson-ex">השלמה לריבוע: $x^2+2x+5=(x+1)^2+4$, ולכן $\int\frac{dx}{x^2+2x+5}=\frac12\arctan\frac{x+1}{2}+C$.</div>
<h3>מונה לינארי מעל ריבועי שלא מתפרק</h3>
<p>מפרקים את המונה לחלק שהוא נגזרת המכנה ולקבוע: $\frac{Bx+C}{x^2+k}=\frac{B}{2}\cdot\frac{2x}{x^2+k}+\frac{C}{x^2+k}$, ואז $\ln$ ו-$\arctan$.</p>
<h3>צורת הפירוק</h3>
<ul>
<li>גורם לינארי $(x-r)$: ‏$\frac{A}{x-r}$.</li>
<li>גורם כפול $(x-r)^2$: <b>שני</b> איברים, ‏$\frac{A}{x-r}+\frac{B}{(x-r)^2}$.</li>
<li>גורם ריבועי שלא מתפרק: ‏$\frac{Bx+C}{x^2+k}$ (מונה לינארי, לא קבוע).</li>
</ul>
<p>את המקדמים מוצאים בהשוואת מקדמים (או בהצבת שורש). למשל $\frac{1}{x(x^2+1)}=\frac{A}{x}+\frac{Bx+C}{x^2+1}$ נותן $1=A(x^2+1)+(Bx+C)x$: עם $x=0$ מקבלים $A=1$, ממקדם $x^2$ מקבלים $0=A+B$ ולכן $B=-1$, וממקדם $x$ מקבלים $C=0$.</p>
<div class="lesson-trap">⚠️ מונה קבוע מעל גורם ריבועי לא מספיק ל-$\frac{1}{x(x^2+1)}$ וכדומה: חסר $Bx$. וגורם כפול עם איבר אחד חסר חלק.</div>
` },
  questions: [
  {
    "id": "C06-Q1",
    "question": "מהו $\\int\\frac{dx}{x^2+2x+5}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\arctan\\frac{x+1}{2}+C$"
      },
      {
        "id": "b",
        "value": "$\\frac12\\arctan(x+1)+C$"
      },
      {
        "id": "c",
        "value": "$\\ln\\left(x^2+2x+5\\right)+C$"
      },
      {
        "id": "d",
        "value": "$\\frac12\\arctan\\frac{x+1}{2}+C$"
      }
    ],
    "correctId": "d",
    "explanation": "‏$x^2+2x+5=(x+1)^2+4$, ולכן **$\\frac12\\arctan\\frac{x+1}{2}$**. בלי ה-$\\frac12$ מקבלים פי שניים. ‏$\\frac12\\arctan(x+1)$ מתעלמת מהחילוק ב-$2$ בתוך ה-$\\arctan$. ‏$\\ln$ מתאים רק אם המונה היה $2x+2$.",
    "recap": "Δ<0: משלימים לריבוע ← (1/a) arctan((x+b)/a)"
  },
  {
    "id": "C06-Q2",
    "question": "איזה סוג פונקציות יופיע בתשובה של $\\int\\frac{dx}{x^2+4x+3}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\arctan$ (המכנה לא מתפרק)"
      },
      {
        "id": "b",
        "value": "לוגריתמים בלבד (המכנה מתפרק)"
      },
      {
        "id": "c",
        "value": "$\\arctan$ ו-$\\ln$ ביחד"
      },
      {
        "id": "d",
        "value": "אי אפשר לבטא באמצעות פונקציות אלמנטריות"
      }
    ],
    "correctId": "b",
    "explanation": "‏$\\Delta=16-12=4>0$, והמכנה הוא $(x+1)(x+3)$. פירוק לשברים חלקיים נותן $\\frac12\\left(\\frac{1}{x+1}-\\frac{1}{x+3}\\right)$, כלומר לוגריתמים בלבד. ‏$\\arctan$ מופיע רק כש-$\\Delta<0$ (למשל $x^2+4x+5$ עם $\\Delta=-4$). השילוב מופיע כשיש גם מונה לינארי מעל ריבועי שלא מתפרק. והאינטגרל אלמנטרי.",
    "recap": "Δ>0: ln. Δ<0: arctan"
  },
  {
    "id": "C06-Q3",
    "question": "מהו $\\int\\frac{x+3}{x^2+1}\\,dx$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\ln\\left(x^2+1\\right)+3\\arctan x+C$"
      },
      {
        "id": "b",
        "value": "$\\frac12\\ln\\left(x^2+1\\right)+\\arctan 3x+C$"
      },
      {
        "id": "c",
        "value": "$\\frac12\\ln\\left(x^2+1\\right)+3\\arctan x+C$"
      },
      {
        "id": "d",
        "value": "$\\ln|x+3|-\\ln\\left(x^2+1\\right)+C$"
      }
    ],
    "correctId": "c",
    "explanation": "מפרקים: $\\frac{x}{x^2+1}+\\frac{3}{x^2+1}$. הראשון הוא חצי מנגזרת המכנה: $\\frac12\\ln(x^2+1)$. השני הוא $3\\arctan x$. התשובה **$\\frac12\\ln(x^2+1)+3\\arctan x$**. ‏$\\ln(x^2+1)$ מלא נותן $\\frac{2x}{x^2+1}$. ‏$\\arctan3x$ מכניס את ה-$3$ פנימה. התשובה האחרונה עושה פירוק מכנה שאין.",
    "recap": "(Bx+C)/(x²+k): חצי-נגזרת ← ln, קבוע ← arctan"
  },
  {
    "id": "C06-Q4",
    "step": {
      "type": "numeric",
      "prompt": "$\\frac{1}{x\\left(x^2+1\\right)}=\\frac{A}{x}+\\frac{Bx+C}{x^2+1}$. מהו $B$ ?",
      "answer": -1,
      "tol": 0,
      "explain": "‏$1=A\\left(x^2+1\\right)+(Bx+C)x$. עם $x=0$: ‏$A=1$. מקדם $x^2$: ‏$0=A+B$, לכן $B=-1$. מקדם $x$: ‏$0=C$."
    },
    "recap": "משווים מקדמים אחרי שהצבת השורש נתנה A"
  },
  {
    "id": "C06-Q5",
    "question": "מהו $\\int\\frac{dx}{x\\left(x^2+1\\right)}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\ln|x|-\\frac12\\ln\\left(x^2+1\\right)+C$"
      },
      {
        "id": "b",
        "value": "$\\ln|x|+\\frac12\\ln\\left(x^2+1\\right)+C$"
      },
      {
        "id": "c",
        "value": "$\\ln|x|-\\arctan x+C$"
      },
      {
        "id": "d",
        "value": "$\\ln|x|-\\ln\\left(x^2+1\\right)+C$"
      }
    ],
    "correctId": "a",
    "explanation": "הפירוק הוא $\\frac1x-\\frac{x}{x^2+1}$, ולכן **$\\ln|x|-\\frac12\\ln(x^2+1)$**. הסימן החיובי והמקדם $1$ במקום $\\frac12$ נובעים מטעויות בפירוק. ‏$\\arctan$ היה מופיע רק עם מונה קבוע מעל $x^2+1$, אבל כאן $C=0$.",
    "recap": "1/(x(x²+1)) = 1/x − x/(x²+1)"
  },
  {
    "id": "C06-Q6",
    "question": "מהי צורת הפירוק הנכונה של $\\frac{x}{(x-1)^2\\left(x^2+4\\right)}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$\\frac{A}{x-1}+\\frac{Cx+D}{x^2+4}$"
      },
      {
        "id": "b",
        "value": "$\\frac{A}{(x-1)^2}+\\frac{B}{x^2+4}$"
      },
      {
        "id": "c",
        "value": "$\\frac{A}{x-1}+\\frac{B}{(x-1)^2}+\\frac{C}{x^2+4}$"
      },
      {
        "id": "d",
        "value": "$\\frac{A}{x-1}+\\frac{B}{(x-1)^2}+\\frac{Cx+D}{x^2+4}$"
      }
    ],
    "correctId": "d",
    "explanation": "גורם כפול $(x-1)^2$ דורש **שני** איברים, וגורם ריבועי דורש מונה **לינארי**. הפירוק $\\frac{A}{x-1}+\\frac{B}{(x-1)^2}+\\frac{Cx+D}{x^2+4}$ עובד (פתרון קיים). ללא האיבר $\\frac{B}{(x-1)^2}$ או עם קבוע בלבד מעל הריבועי, למערכת המשוואות אין פתרון. בדקנו.",
    "recap": "כפול: שני איברים. ריבועי: Bx+C"
  }
],
});

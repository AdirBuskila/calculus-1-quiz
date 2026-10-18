/* investigation course, level 6: אסימפטוטה משופעת */
COURSE_LEVEL("investigation", {
  id: "C06", order: 6, icon: "📐", title: "אסימפטוטה משופעת",
  goal: "לחשב a ו-b לכל צד בנפרד, בחילוק פולינומים או בגבול עם אקספוננט, ולקבוע אם יש אסימפטוטה משופעת.",
  source: "ai-verified",
  lesson: { html: String.raw`
<p>כשהגרף מתקרב לקו ישר שאינו אופקי, זו <b>אסימפטוטה משופעת</b> $y=ax+b$.</p>
<div class="lesson-formula">$a=\lim\frac{f(x)}{x}$ וגם $b=\lim\left(f(x)-ax\right)$</div>
<ul>
<li>מחשבים את שני הגבולות ב-$+\infty$ ובנפרד ב-$-\infty$, כי כל צד עשוי להתנהג אחרת.</li>
<li>אם $a$ אינסופי, או ש-$b$ אינו קיים, אין אסימפטוטה משופעת בצד הזה. אם $a=0$ זו אסימפטוטה אופקית.</li>
</ul>
<h3>פונקציה רציונלית</h3>
<p>כשדרגת המונה גדולה ב-1 מדרגת המכנה, מחלקים פולינומים ומקבלים את הישר מיד: $\frac{x^2+1}{x}=x+\frac1x$, והשארית $\frac1x\to0$, ולכן $y=x$.</p>
<h3>הגבול $\frac{e^u-1}{u}$</h3>
<p>הגבול $\lim_{u\to0}\frac{e^u-1}{u}=1$ (זו הנגזרת של $e^u$ ב-$0$). עם הצבה $u=\frac cx$ מקבלים $\lim x\left(e^{c/x}-1\right)=c$.</p>
<div class="lesson-ex">דוגמה: $f(x)=xe^{1/x}$.<br>
$a=\lim e^{1/x}=e^0=1$.<br>
$b=\lim\left(xe^{1/x}-x\right)=\lim x\left(e^{1/x}-1\right)$. עם $u=\frac1x\to0$ זה $\lim\frac{e^u-1}{u}=1$.<br>
האסימפטוטה המשופעת: $y=x+1$, ובשני הצדדים.</div>
<div class="lesson-ex">דוגמה לצד אחד בלבד: $f(x)=x+e^{x}$. ב-$-\infty$: $a=1$ ו-$b=\lim e^{x}=0$, כלומר $y=x$. ב-$+\infty$: $\frac{f}{x}=1+\frac{e^x}{x}\to\infty$, ולכן אין אסימפטוטה משופעת שם.</div>
` },
  questions: [
  {
    "id": "C06-Q1",
    "question": "מהי האסימפטוטה המשופעת של $f(x)=\\frac{x^2+1}{x}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$y=x+1$"
      },
      {
        "id": "b",
        "value": "$y=x$"
      },
      {
        "id": "c",
        "value": "$y=0$"
      },
      {
        "id": "d",
        "value": "$y=x-1$"
      }
    ],
    "correctId": "b",
    "explanation": "$f(x)=x+\\frac1x$, ו-$\\frac1x\\to0$. לכן $a=1$ ו-$b=0$: **$y=x$**. ‏$y=x+1$ ו-$y=x-1$ מתקבלות מ-$b=1$ ו-$b=-1$, אבל $b=0$. ‏$y=0$ אינה אסימפטוטה כי $f\\to\\infty$.",
    "recap": "מחלקים פולינומים: השארית שואפת ל-0, והמנה היא הישר"
  },
  {
    "id": "C06-Q2",
    "question": "מהי האסימפטוטה המשופעת של $f(x)=\\frac{x^2+x+1}{x-1}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$y=x+1$"
      },
      {
        "id": "b",
        "value": "$y=x$"
      },
      {
        "id": "c",
        "value": "$y=x+2$"
      },
      {
        "id": "d",
        "value": "$y=x-2$"
      }
    ],
    "correctId": "c",
    "explanation": "חילוק: $x^2+x+1=(x-1)(x+2)+3$, ולכן $f=x+2+\\frac{3}{x-1}$. השארית שואפת ל-$0$ בשני הצדדים: **$y=x+2$**. הבחירות האחרות מתקבלות מחילוק שגוי ($x+1$ מתעלמת מהאיבר $x$ בשארית, ו-$x-2$ מטעות בסימן של $-1$).",
    "recap": "חילוק פולינומים נותן את b כפשוט"
  },
  {
    "id": "C06-Q3",
    "step": {
      "type": "numeric",
      "prompt": "האסימפטוטה המשופעת של $f(x)=\\frac{2x^2-x}{x+1}$ היא $y=2x+b$. מהו $b$ ?",
      "answer": -3,
      "tol": 0,
      "explain": "$a=\\lim\\frac{2x-1}{x+1}=2$. אז $f-2x=\\frac{2x^2-x-2x^2-2x}{x+1}=\\frac{-3x}{x+1}\\to-3$. אותו ערך ב-$-\\infty$."
    },
    "recap": "b = lim (f − ax), מאחדים לשבר אחד"
  },
  {
    "id": "C06-Q4",
    "question": "מהי האסימפטוטה המשופעת של $f(x)=xe^{2/x}$ ב-$+\\infty$ ?",
    "options": [
      {
        "id": "a",
        "value": "$y=x+2$"
      },
      {
        "id": "b",
        "value": "$y=x+1$"
      },
      {
        "id": "c",
        "value": "$y=x$"
      },
      {
        "id": "d",
        "value": "$y=x+e^2$"
      }
    ],
    "correctId": "a",
    "explanation": "$a=\\lim e^{2/x}=1$. אז $b=\\lim x\\left(e^{2/x}-1\\right)$. עם $u=\\frac2x$ מקבלים $x=\\frac2u$ ולכן $b=2\\lim\\frac{e^u-1}{u}=2$. התשובה **$y=x+2$**. ‏$y=x+1$ שוכחת את הגורם 2. ‏$y=x$ מניחה $b=0$. ‏$y=x+e^2$ מציבה את $x=1$ במקום לשאוף לאינסוף.",
    "recap": "$x\\left(e^{c/x}-1\\right)\\to c$"
  },
  {
    "id": "C06-Q5",
    "question": "מה נכון לגבי אסימפטוטה משופעת של $f(x)=x+e^{x}$ ?",
    "options": [
      {
        "id": "a",
        "value": "$y=x$ בשני הכיוונים"
      },
      {
        "id": "b",
        "value": "$y=x+1$ ב-$+\\infty$"
      },
      {
        "id": "c",
        "value": "אין אסימפטוטה משופעת באף כיוון"
      },
      {
        "id": "d",
        "value": "$y=x$ ב-$-\\infty$ בלבד"
      }
    ],
    "correctId": "d",
    "explanation": "ב-$-\\infty$: $e^{x}\\to0$ ולכן $f-x\\to0$ ו-$y=x$ משופעת. ב-$+\\infty$: $\\frac{f}{x}=1+\\frac{e^x}{x}\\to\\infty$, ולכן אין אסימפטוטה שם. לכן **ב-$-\\infty$ בלבד**. ‏$y=x$ בשני הכיוונים מתעלמת מהצד הימני, ו-$y=x+1$ אינה מתקבלת כי $b=\\lim e^x$ אינו קיים ב-$+\\infty$. ויש אסימפטוטה בצד שמאל.",
    "recap": "בודקים כל צד בנפרד: a יכול להיות אינסוף בצד אחד"
  },
  {
    "id": "C06-Q6",
    "step": {
      "type": "findbug",
      "prompt": "בחישוב האסימפטוטה המשופעת של $f(x)=xe^{3/x}$ נפלה טעות בשורה אחת. איזו ?",
      "lines": [
        "$a=\\lim\\frac{f(x)}{x}=\\lim e^{3/x}=1$",
        "$b=\\lim\\left(f(x)-x\\right)=\\lim x\\left(e^{3/x}-1\\right)$",
        "מציבים $u=\\frac3x$, ‏$x=\\frac3u$ ומקבלים $\\lim_{u\\to0}\\frac{e^u-1}{u}$",
        "הגבול ‏$\\lim_{u\\to0}\\frac{e^u-1}{u}=1$, ולכן $b=3\\cdot1=3$",
        "האסימפטוטה המשופעת היא $y=x+3$"
      ],
      "bugIndex": 2,
      "explain": "$x\\left(e^{3/x}-1\\right)=\\frac3u\\left(e^u-1\\right)=3\\cdot\\frac{e^u-1}{u}$. בשורה 2 נשמט הגורם $3$, ולכן שורה 3 (שמכפילה ב-3) לא עוקבת."
    },
    "recap": "x = c/u: הגורם c יוצא החוצה"
  }
],
});

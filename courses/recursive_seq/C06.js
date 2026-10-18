/* recursive_seq · level 6 - rational recursions a_{n+1} = p/(q - a_n) */
COURSE_LEVEL("recursive_seq", {
  id: "C06", order: 6, icon: "➗", title: "רקורסיה עם שבר",
  goal: "להוכיח חסימה ומונוטוניות לסדרה מהצורה מונה קבוע חלקי (קבוע פחות איבר), בלי לטעות בכיוון אי-השוויון.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>סדרות כמו $a_{n+1}=\frac{2}{3-a_n}$ מופיעות הרבה במבחנים. שלוש נקודות ייחודיות להן:</p>
    <ul>
      <li><b>המכנה חייב להישאר חיובי.</b> בחסם $a_n\le1$ מתקבל $3-a_n\ge2>0$.</li>
      <li><b>הפיכת שבר הופכת אי-שוויון</b> (למספרים חיוביים): $x\ge2\Rightarrow\frac1x\le\frac12$.</li>
      <li><b>$f$ עולה</b> כל עוד המכנה חיובי, כי כש-$a_n$ גדל המכנה קטן והשבר גדל.</li>
    </ul>
    <div class="lesson-ex">$a_1=0,\ a_{n+1}=\frac{2}{3-a_n}$. נקודות שבת: $L(3-L)=2$, כלומר $(L-1)(L-2)=0$.<br>
    חסם: $a_n\le1$. בסיס $0\le1$. צעד: $3-a_n\ge2$, ולכן $\frac{1}{3-a_n}\le\frac12$ ו-$a_{n+1}\le1$.<br>
    עולה: $\frac{2}{3-a_n}\ge a_n$. כופלים במכנה החיובי: $2\ge a_n(3-a_n)$, כלומר $(a_n-1)(a_n-2)\ge0$, וזה נכון כי $a_n\le1$ (שני הגורמים אי-חיוביים).<br>
    לכן מתכנסת, ו-$L=1$ ולא $2$, כי $a_n\le1$ ולכן $L\le1$.</div>
    <div class="lesson-rule">🔑 בוחרים את החסם בין שתי נקודות השבת לפי האיבר הראשון: מתחילים מתחת לשתיהן, לכן עולים עד הקרובה, והיא החסם.</div>
    <div class="lesson-trap">⚠️ כופלים אי-שוויון במכנה רק אחרי שמוכיחים שהוא חיובי. כפל במספר שלילי הופך את הכיוון.</div>` },
  questions: [
    { id: "C06-Q1",
      step: { type: "numeric", prompt: String.raw`נתונה $a_1=0,\ a_{n+1}=\frac{2}{3-a_n}$. מהו $a_3$ ? (עיגול לשלוש ספרות אחרי הנקודה)`, answer: 0.857, tol: 0.001,
              explain: String.raw`$a_2=\frac23$ ואז $a_3=\frac{2}{3-\frac23}=\frac{2}{7/3}=\frac67\approx0.857$.` },
      recap: "מציבים צעד אחר צעד" },
    { id: "C06-Q2", question: String.raw`נתונה $a_{n+1}=\frac{2}{3-a_n}$ ומניחים $a_n\le1$. מה מקבלים על $a_{n+1}$ ?`,
      options: [{ id: "a", value: "$a_{n+1}\\le1$" }, { id: "b", value: "$a_{n+1}\\ge1$" }, { id: "c", value: "$a_{n+1}\\le\\frac12$" }, { id: "d", value: "$a_{n+1}\\ge2$" }],
      correctId: "a",
      explanation: String.raw`$a_n\le1\Rightarrow3-a_n\ge2>0\Rightarrow\frac{1}{3-a_n}\le\frac12\Rightarrow a_{n+1}\le1$. הכיוון $\ge1$ נובע מטעות של אי-הפיכת הכיוון, והחסם $\frac12$ חזק מדי ($a_3\approx0.857$).`,
      recap: "מכנה גדול יותר, שבר קטן יותר" },
    { id: "C06-Q3",
      step: { type: "order", prompt: String.raw`סדרו את ההוכחה ש-$a_{n+1}\ge a_n$ עבור $a_{n+1}=\frac{2}{3-a_n}$, כשידוע $a_n\le1$.`,
              lines: [String.raw`צריך להראות $\frac{2}{3-a_n}\ge a_n$`,
                      String.raw`$3-a_n>0$, ולכן כופלים בלי להפוך כיוון: $2\ge a_n(3-a_n)$`,
                      String.raw`שקול ל-$a_n^2-3a_n+2\ge0$`,
                      String.raw`כלומר $(a_n-1)(a_n-2)\ge0$`,
                      String.raw`נכון, כי $a_n\le1$ ולכן שני הגורמים אי-חיוביים`],
              explain: String.raw`הכפל במכנה חייב לבוא אחרי שמצהירים שהמכנה חיובי; רק אז פותחים סוגריים ומפרקים.` },
      recap: "מכנה חיובי, כפל, פירוק, סימן" },
    { id: "C06-Q4", question: String.raw`בסדרה $a_1=0,\ a_{n+1}=\frac{2}{3-a_n}$ (עולה וחסומה ב-$1$) נקודות השבת הן $1$ ו-$2$. מה הגבול ולמה?`,
      options: [{ id: "a", value: "$1$, כי $a_n\\le1$ ולכן $L\\le1$" }, { id: "b", value: "$2$, כי הוא הגדול מבין השניים" }, { id: "c", value: "$1$, כי הוא קטן מ-$2$" }, { id: "d", value: "$2$, כי הסדרה עולה" }],
      correctId: "a",
      explanation: String.raw`הנימוק הוא החסם: $a_n\le1$ נשמר בגבול, $L\le1$, ולכן רק $1$ אפשרי. "הגדול", "הקטן" ו"עולה" אינם נימוקים: סדרה עולה יכולה להתכנס לערך קטן אם היא חסומה בו.`,
      recap: "השורש נבחר לפי החסם" },
    { id: "C06-Q5",
      step: { type: "numeric", prompt: String.raw`הסדרה $a_1=0,\ a_{n+1}=\frac{12}{7-a_n}$ עולה וחסומה מלמעלה ב-$3$. מהו הגבול?`, answer: 3, tol: 0,
              explain: String.raw`$L(7-L)=12\Rightarrow L^2-7L+12=0\Rightarrow(L-3)(L-4)=0$. מ-$a_n\le3$ נובע $L\le3$, ולכן $L=3$.` },
      recap: "שני שורשים: החסם מכריע" },
    { id: "C06-Q6",
      step: { type: "findbug", prompt: String.raw`בהוכחה ש-$a_n\le1$ עבור $a_1=0,\ a_{n+1}=\frac{2}{3-a_n}$ יש שגיאה אחת. באיזו שורה?`,
              lines: [String.raw`בסיס: $a_1=0\le1$`,
                      String.raw`הנחה: $a_n\le1$`,
                      String.raw`לכן $3-a_n\ge2$, ובפרט המכנה חיובי`,
                      String.raw`בהפיכת שברים האי-שוויון נשמר: $\frac{1}{3-a_n}\ge\frac12$`,
                      String.raw`לכן $a_{n+1}=\frac{2}{3-a_n}\le1$`],
              bugIndex: 3,
              explain: String.raw`הפיכת מספרים חיוביים הופכת את הכיוון: $3-a_n\ge2\Rightarrow\frac{1}{3-a_n}\le\frac12$. רק כך מגיעים ל-$a_{n+1}\le1$.` },
      recap: "הפיכה הופכת את כיוון האי-שוויון" },
  ],
});

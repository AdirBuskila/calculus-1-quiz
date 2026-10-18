/* recursive_seq · level 3 - bounding by induction */
COURSE_LEVEL("recursive_seq", {
  id: "C03", order: 3, icon: "🧱", title: "חסימה באינדוקציה",
  goal: "להוכיח באינדוקציה שסדרה רקורסיבית חסומה, ולבחור חסם שמתאים גם לאיבר הראשון.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>סדרה <b>חסומה מלמעלה</b> אם יש $M$ כך ש-$a_n\le M$ לכל $n$. <b>חסומה מלמטה</b> אם $a_n\ge m$ לכל $n$. את החסם מוכיחים באינדוקציה:</p>
    <ul>
      <li><b>בסיס:</b> בודקים שהחסם נכון עבור $a_1$ <b>עצמו</b>.</li>
      <li><b>הנחה:</b> $a_n\le M$.</li>
      <li><b>צעד:</b> מפעילים את $f$ על שני צדדי אי-השוויון ומקבלים $a_{n+1}=f(a_n)\le M$. כש-$f$ עולה, אי-השוויון נשמר.</li>
    </ul>
    <div class="lesson-rule">🔑 איזה $M$ בוחרים? את נקודת השבת מהרמה הקודמת. הצעד עובד בדיוק כי $f(M)=M$: מ-$a_n\le M$ נובע $f(a_n)\le f(M)=M$.</div>
    <div class="lesson-ex">$a_1=1,\ a_{n+1}=\sqrt{2+a_n}$ ו-$M=2$ (נקודת שבת). בסיס: $a_1=1<2$. הנחה: $a_n<2$. צעד: $2+a_n<4$, ולכן $\sqrt{2+a_n}<\sqrt4=2$, כלומר $a_{n+1}<2$.</div>
    <div class="lesson-trap">⚠️ החסם חייב להתקיים כבר ב-$a_1$. הטענה $a_n<2$ <b>שגויה</b> כשהסדרה $a_1=3,\ a_{n+1}=\sqrt{2+a_n}$ מתחילה מעל $2$. אז הסדרה יורדת והחסם הנכון הוא מלמטה: $a_n\ge2$. נקודת ההתחלה קובעת אם החסם הוא מלמעלה או מלמטה.</div>` },
  questions: [
    { id: "C03-Q1",
      step: { type: "order", prompt: String.raw`סדרו את ההוכחה ש-$a_n<2$ לכל $n$ עבור $a_1=1,\ a_{n+1}=\sqrt{2+a_n}$.`,
              lines: [String.raw`בסיס: $a_1=1<2$`,
                      String.raw`הנחה: $a_n<2$`,
                      String.raw`מכאן $2+a_n<4$`,
                      String.raw`פונקציית השורש עולה, ולכן $\sqrt{2+a_n}<\sqrt4=2$`,
                      String.raw`כלומר $a_{n+1}<2$, ולפי אינדוקציה $a_n<2$ לכל $n$`],
              explain: String.raw`סדר ההוכחה: בסיס, הנחה, ואז שרשרת צעדים שמסתיימת בטענה עבור $n+1$.` },
      recap: "בסיס, הנחה, צעד" },
    { id: "C03-Q2", question: String.raw`נתונה $a_1=3,\ a_{n+1}=\sqrt{2+a_n}$. איזו טענה נכונה לכל $n$ וניתנת להוכחה באינדוקציה?`,
      options: [{ id: "a", value: "$a_n\\le2$" }, { id: "b", value: "$a_n\\ge2$" }, { id: "c", value: "$a_n\\ge4$" }, { id: "d", value: "$a_n\\le1$" }],
      correctId: "b",
      explanation: String.raw`בסיס: $a_1=3\ge2$. צעד: $a_n\ge2\Rightarrow2+a_n\ge4\Rightarrow a_{n+1}\ge2$. הטענות $a_n\le2$, $a_n\ge4$ ו-$a_n\le1$ שגויות כבר ב-$a_1=3$.`,
      recap: "בודקים את הבסיס על a_1 עצמו" },
    { id: "C03-Q3",
      step: { type: "findbug", prompt: String.raw`בהוכחה ש-$a_n<4$ עבור $a_1=1,\ a_{n+1}=\sqrt{a_n+12}$ יש שגיאה אחת. באיזו שורה?`,
              lines: [String.raw`בסיס: $a_1=1<4$`,
                      String.raw`הנחה: $a_n<4$`,
                      String.raw`לכן $a_n+12<12$`,
                      String.raw`פונקציית השורש עולה, ולכן $\sqrt{a_n+12}<\sqrt{16}$`,
                      String.raw`כלומר $a_{n+1}<4$`],
              bugIndex: 2,
              explain: String.raw`מ-$a_n<4$ מקבלים $a_n+12<16$ ולא $12$. החסם החדש הוא $4+12=16$.` },
      recap: "מוסיפים את הקבוע גם לחסם" },
    { id: "C03-Q4",
      step: { type: "numeric", prompt: String.raw`עבור $a_{n+1}=\frac{a_n}{2}+1$, מניחים $a_n<2$. מהו המספר $c$ המדויק שמקבלים כך ש-$a_{n+1}<c$ ?`, answer: 2, tol: 0,
              explain: String.raw`$a_n<2\Rightarrow\frac{a_n}{2}<1\Rightarrow\frac{a_n}{2}+1<2$, ולכן $c=2$ ושמרנו על אותו חסם.` },
      recap: "הצעד חוזר לאותו חסם" },
    { id: "C03-Q5", question: String.raw`מנסים להוכיח $a_n\le1.5$ עבור $a_1=1,\ a_{n+1}=\sqrt{2+a_n}$. מה קורה?`,
      options: [{ id: "a", value: "הבסיס נכשל" }, { id: "b", value: "הצעד נכשל: מ-$a_n\\le1.5$ מקבלים רק $a_{n+1}\\le\\sqrt{3.5}\\approx1.87$" }, { id: "c", value: "ההוכחה מצליחה" }, { id: "d", value: "אי אפשר להפעיל שורש על אי-שוויון" }],
      correctId: "b",
      explanation: String.raw`בסיס: $a_1=1\le1.5$ תקין. בצעד, $2+a_n\le3.5$ נותן $a_{n+1}\le\sqrt{3.5}\approx1.87>1.5$, ולא מסיקים את החסם. אכן $a_3\approx1.93>1.5$, כך שהטענה שגויה. החסם שעובד הוא נקודת השבת $2$. שורש הוא פונקציה עולה ולכן מותר להפעיל אותו.`,
      recap: "חסם שאינו נקודת שבת לא סוגר את הצעד" },
    { id: "C03-Q6",
      step: { type: "numeric", prompt: String.raw`עבור $a_1=1,\ a_{n+1}=\sqrt{3a_n+10}$ מחפשים חסם עליון $M$ שהצעד עובד עבורו בדיוק ($f(M)=M$, $M>0$). מהו $M$ ?`, answer: 5, tol: 0,
              explain: String.raw`$M=\sqrt{3M+10}\Rightarrow M^2-3M-10=0\Rightarrow(M-5)(M+2)=0$, ולכן $M=5$. אכן $a_n\le5\Rightarrow3a_n+10\le25\Rightarrow a_{n+1}\le5$.` },
      recap: "החסם הטבעי הוא נקודת השבת" },
  ],
});

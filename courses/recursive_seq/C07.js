/* recursive_seq · level 7 - a_{n+1} = (a_n + c/a_n)/2 and AM-GM */
COURSE_LEVEL("recursive_seq", {
  id: "C07", order: 7, icon: "⚖️", title: "ממוצע חשבוני ושורש: אי-שוויון הממוצעים",
  goal: "להוכיח התכנסות לסדרה מהצורה חצי של (איבר ועוד קבוע חלקי איבר) בעזרת אי-שוויון הממוצעים, ולטפל נכון בחסם שמתחיל רק מ-$n=2$.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>סדרה כמו $a_{n+1}=\frac12\left(a_n+\frac{c}{a_n}\right)$ עם $c>0$ ו-$a_1>0$ היא שיטה קדומה לחישוב $\sqrt c$. החסם שלה לא מגיע מאינדוקציה אלא מ<b>אי-שוויון הממוצעים</b>: לכל $x,y>0$,</p>
    <div class="lesson-formula">$$\frac{x+y}{2}\ge\sqrt{xy}$$</div>
    <p>עם $x=a_n$ ו-$y=\frac{c}{a_n}$ מקבלים $a_{n+1}\ge\sqrt{a_n\cdot\frac{c}{a_n}}=\sqrt c$.</p>
    <div class="lesson-trap">⚠️ החסם $a_n\ge\sqrt c$ מובטח מ-$n=2$ ואילך, ולא בהכרח עבור $a_1$. עבור $c=10,\ a_1=1$ מתקיים $a_1=1<\sqrt{10}$, אבל $a_2=5.5\ge\sqrt{10}$. לכן כותבים "לכל $n\ge2$" ומתחילים את המונוטוניות מ-$a_2$ (או בודקים את $a_1$ בנפרד).</div>
    <h3>מונוטוניות</h3>
    <p>$a_{n+1}-a_n=\frac12\left(\frac{c}{a_n}-a_n\right)=\frac{c-a_n^2}{2a_n}$. כש-$a_n\ge\sqrt c$ מתקבל $c-a_n^2\le0$, ולכן ההפרש אי-חיובי והסדרה יורדת (מ-$a_2$ ואילך).</p>
    <div class="lesson-rule">🔑 חסומה מלמטה ב-$\sqrt c$ ויורדת, ולכן מתכנסת. הגבול: $L=\frac12\left(L+\frac cL\right)\Rightarrow L^2=c\Rightarrow L=\sqrt c$ (חיובי, כי $a_n>0$).</div>
    <div class="lesson-ex">$c=10,\ a_1=4$: $a_2=\frac12\left(4+\frac{10}{4}\right)=3.25$, $a_3\approx3.163$. הם יורדים אל $\sqrt{10}\approx3.162$.</div>` },
  questions: [
    { id: "C07-Q1",
      step: { type: "numeric", prompt: String.raw`נתונה $a_1=4,\ a_{n+1}=\frac12\left(a_n+\frac{10}{a_n}\right)$. מהו $a_2$ ?`, answer: 3.25, tol: 0,
              explain: String.raw`$a_2=\frac12\left(4+\frac{10}{4}\right)=\frac12(4+2.5)=3.25$.` },
      recap: "מציבים ומחלקים בשתיים" },
    { id: "C07-Q2", question: String.raw`עבור $a_{n+1}=\frac12\left(a_n+\frac{c}{a_n}\right)$, מהו ההפרש $a_{n+1}-a_n$ ?`,
      options: [{ id: "a", value: String.raw`$\frac{c-a_n^2}{2a_n}` + "$" }, { id: "b", value: String.raw`$\frac{a_n^2-c}{2a_n}` + "$" }, { id: "c", value: String.raw`$\frac{c+a_n^2}{2a_n}` + "$" }, { id: "d", value: String.raw`$\frac{c}{2a_n}` + "$" }],
      correctId: "a",
      explanation: String.raw`$\frac12a_n+\frac{c}{2a_n}-a_n=\frac{c}{2a_n}-\frac{a_n}{2}=\frac{c-a_n^2}{2a_n}$. האפשרות עם $a_n^2-c$ היא ההפרש בסימן הפוך.`,
      recap: "ההפרש הוא (c − a²) חלקי 2a" },
    { id: "C07-Q3", question: String.raw`נתונה $c=10,\ a_1=1,\ a_{n+1}=\frac12\left(a_n+\frac{10}{a_n}\right)$. מה נכון לגבי הטענה $a_n\ge\sqrt{10}$ ?`,
      options: [{ id: "a", value: "נכונה לכל $n\\ge1$" }, { id: "b", value: "נכונה לכל $n\\ge2$, אבל לא עבור $n=1$" }, { id: "c", value: "אף פעם לא נכונה" }, { id: "d", value: "נכונה רק עבור $n$ זוגי" }],
      correctId: "b",
      explanation: String.raw`$a_1=1<\sqrt{10}\approx3.16$, ולכן הטענה כבר לא נכונה ב-$n=1$. מאי-שוויון הממוצעים $a_2=5.5\ge\sqrt{10}$, וכך לכל $n\ge2$ (כי $a_{n+1}\ge\sqrt{10}$ לכל $n\ge1$).`,
      recap: "החסם מאי-שוויון הממוצעים מתחיל ב-n=2" },
    { id: "C07-Q4",
      step: { type: "order", prompt: String.raw`סדרו את ההוכחה ש-$a_{n+1}\ge\sqrt{10}$ עבור $a_{n+1}=\frac12\left(a_n+\frac{10}{a_n}\right),\ a_1=4$.`,
              lines: [String.raw`כל האיברים חיוביים, ולכן אפשר להפעיל את אי-שוויון הממוצעים על $a_n$ ו-$\frac{10}{a_n}$`,
                      String.raw`$a_{n+1}=\frac12\left(a_n+\frac{10}{a_n}\right)\ge\sqrt{a_n\cdot\frac{10}{a_n}}$`,
                      String.raw`$\sqrt{a_n\cdot\frac{10}{a_n}}=\sqrt{10}$`,
                      String.raw`לכן $a_{n+1}\ge\sqrt{10}$ לכל $n$`],
              explain: String.raw`צריך להצדיק חיוביות לפני אי-שוויון הממוצעים (הוא מוגדר ל-$x,y>0$), אחר כך להפעיל אותו, לצמצם ולהסיק.` },
      recap: "חיוביות, ממוצעים, צמצום" },
    { id: "C07-Q5",
      step: { type: "numeric", prompt: String.raw`הסדרה $a_1=4,\ a_{n+1}=\frac12\left(a_n+\frac{10}{a_n}\right)$ מתכנסת, וכל איבריה חיוביים. מהו הגבול? (עיגול לשלוש ספרות אחרי הנקודה)`, answer: 3.162, tol: 0.001,
              explain: String.raw`$L=\frac12\left(L+\frac{10}{L}\right)\Rightarrow L^2=10\Rightarrow L=\sqrt{10}\approx3.162$ (הגבול חיובי).` },
      recap: "הגבול הוא שורש c" },
    { id: "C07-Q6",
      step: { type: "findbug", prompt: String.raw`בבדיקת המונוטוניות של $a_{n+1}=\frac12\left(a_n+\frac{c}{a_n}\right)$ יש שגיאה אחת. באיזו שורה?`,
              lines: [String.raw`$a_{n+1}-a_n=\frac12\left(a_n+\frac{c}{a_n}\right)-a_n$`,
                      String.raw`$=\frac12\left(\frac{c}{a_n}-a_n\right)$`,
                      String.raw`$=\frac{c-a_n^2}{2a_n}$`,
                      String.raw`כש-$a_n\ge\sqrt c$ נקבל $c-a_n^2\ge0$, ולכן $a_{n+1}\ge a_n$ והסדרה עולה`],
              bugIndex: 3,
              explain: String.raw`אם $a_n\ge\sqrt c$ אז $a_n^2\ge c$ ו-$c-a_n^2\le0$. ההפרש אי-חיובי והסדרה **יורדת**.` },
      recap: "מעל שורש c ההפרש שלילי: יורדת" },
  ],
});

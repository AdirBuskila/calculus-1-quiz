/* recursive_seq · level 4 - monotonicity */
COURSE_LEVEL("recursive_seq", {
  id: "C04", order: 4, icon: "📈", title: "מונוטוניות: עולה או יורדת",
  goal: "להוכיח שסדרה רקורסיבית עולה או יורדת, בשתי שיטות: הפרש ואינדוקציה.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>יש שתי דרכים להוכיח ש-$a_{n+1}\ge a_n$ לכל $n$.</p>
    <h3>שיטה א: הפרש</h3>
    <p>מחשבים $a_{n+1}-a_n$ כביטוי ב-$a_n$ בלבד, ובודקים את הסימן בעזרת <b>החסם שכבר הוכחנו</b>. לכן קודם מוכיחים חסימה ואחר כך מונוטוניות.</p>
    <div class="lesson-ex">$a_{n+1}=\frac{a_n}{2}+1$: ההפרש הוא $a_{n+1}-a_n=1-\frac{a_n}{2}=\frac{2-a_n}{2}$. אם הוכחנו $a_n<2$ ההפרש חיובי והסדרה עולה. אם $a_n>2$ ההפרש שלילי והסדרה יורדת.</div>
    <h3>שיטה ב: אינדוקציה (כש-$f$ עולה)</h3>
    <p>בסיס: $a_1\le a_2$. הנחה: $a_n\le a_{n+1}$. צעד: מפעילים את $f$ העולה על שני הצדדים ומקבלים $f(a_n)\le f(a_{n+1})$, כלומר $a_{n+1}\le a_{n+2}$.</p>
    <div class="lesson-rule">🔑 שיטה ב עובדת רק אם $f$ <b>עולה</b> (על התחום שבו נמצאים האיברים). אם $f$ יורדת, למשל $f(x)=\frac1x$, אי-השוויון מתהפך והסדרה מתנודדת.</div>
    <div class="lesson-ex">$a_1=1,\ a_{n+1}=\sqrt{a_n+6}$. בסיס: $a_2=\sqrt7>1=a_1$. הנחה: $a_n<a_{n+1}$. אז $a_n+6<a_{n+1}+6$ ובשורש (שעולה) $a_{n+1}<a_{n+2}$.</div>
    <div class="lesson-trap">⚠️ בשיטת ההפרש מקבלים ביטוי שהסימן שלו תלוי ב-$a_n$. אם לא הוכחתם חסם על $a_n$, אי אפשר להכריע את הסימן.</div>` },
  questions: [
    { id: "C04-Q1", question: String.raw`באיזו סדרה אפשר להוכיח מונוטוניות באינדוקציה בעזרת "הפעלת $f$ על אי-שוויון" (כלומר $f$ עולה על האיברים)?`,
      options: [{ id: "a", value: String.raw`$a_{n+1}=\sqrt{a_n+3}$, $a_1=1$` }, { id: "b", value: String.raw`$a_{n+1}=\frac{4}{a_n+1}$, $a_1=1$` }, { id: "c", value: String.raw`$a_{n+1}=2-a_n$, $a_1=0$` }, { id: "d", value: String.raw`$a_{n+1}=\frac{1}{a_n}$, $a_1=2$` }],
      correctId: "a",
      explanation: String.raw`רק $f(x)=\sqrt{x+3}$ עולה. ב-$\frac{4}{x+1}$, ב-$2-x$ וב-$\frac1x$ הפונקציה יורדת, ולכן הפעלתה מהפכת את האי-שוויון.`,
      recap: "אינדוקציה על מונוטוניות מחייבת f עולה" },
    { id: "C04-Q2",
      step: { type: "numeric", prompt: String.raw`נתונה $a_1=1,\ a_{n+1}=\sqrt{a_n+6}$. מהו $a_2$ ? (עיגול לשלוש ספרות אחרי הנקודה)`, answer: 2.646, tol: 0.001,
              explain: String.raw`$a_2=\sqrt{1+6}=\sqrt7\approx2.646>1=a_1$. זה בסיס האינדוקציה $a_1<a_2$.` },
      recap: "בסיס: משווים את a_1 ל-a_2" },
    { id: "C04-Q3",
      step: { type: "order", prompt: String.raw`סדרו את ההוכחה ש-$a_n<a_{n+1}$ לכל $n$ עבור $a_1=1,\ a_{n+1}=\sqrt{a_n+6}$.`,
              lines: [String.raw`בסיס: $a_1=1<\sqrt7=a_2$`,
                      String.raw`הנחה: $a_n<a_{n+1}$`,
                      String.raw`מוסיפים 6: $a_n+6<a_{n+1}+6$`,
                      String.raw`השורש עולה, לכן $\sqrt{a_n+6}<\sqrt{a_{n+1}+6}$`,
                      String.raw`כלומר $a_{n+1}<a_{n+2}$`],
              explain: String.raw`הצעד מפעיל על ההנחה בדיוק את הפעולות של $f$: הוספת $6$ ואחר כך שורש.` },
      recap: "בסיס, הנחה, הפעלת f על ההנחה" },
    { id: "C04-Q4", question: String.raw`עבור $a_{n+1}=\frac{a_n}{2}+1$, מהו ההפרש $a_{n+1}-a_n$ ?`,
      options: [{ id: "a", value: String.raw`$\frac{a_n-2}{2}$` }, { id: "b", value: String.raw`$\frac{2-a_n}{2}$` }, { id: "c", value: String.raw`$1+\frac{a_n}{2}$` }, { id: "d", value: String.raw`$\frac{a_n}{2}$` }],
      correctId: "b",
      explanation: String.raw`$\frac{a_n}{2}+1-a_n=1-\frac{a_n}{2}=\frac{2-a_n}{2}$. הביטוי $\frac{a_n-2}{2}$ הוא ההפרש בסימן הפוך.`,
      recap: "מחסרים את a_n ומאחדים" },
    { id: "C04-Q5", question: String.raw`נתונה $a_1=10,\ a_{n+1}=\frac{a_n}{2}+1$. כבר הוכחנו $a_n>2$ לכל $n$. מה מסיקים מהפרש $\frac{2-a_n}{2}$ ?`,
      options: [{ id: "a", value: "הסדרה עולה וחסומה מלמעלה" }, { id: "b", value: "הסדרה יורדת וחסומה מלמטה, ולכן מתכנסת" }, { id: "c", value: "הסדרה עולה וחסומה מלמטה, ולכן מתכנסת" }, { id: "d", value: "אי אפשר להכריע את הסימן" }],
      correctId: "b",
      explanation: String.raw`מ-$a_n>2$ ההפרש $\frac{2-a_n}{2}<0$, ולכן $a_{n+1}<a_n$: הסדרה יורדת. יחד עם החסם $a_n>2$ היא חסומה מלמטה ולכן מתכנסת. אילולא החסם, הסימן לא היה ידוע.`,
      recap: "הסימן של ההפרש נקבע על ידי החסם" },
    { id: "C04-Q6",
      step: { type: "findbug", prompt: String.raw`עבור $a_{n+1}=\sqrt{2+a_n}$ ו-$0<a_n<2$ נבדקת מונוטוניות דרך ההפרש של הריבועים. בשורה אחת יש שגיאה. איזו?`,
              lines: [String.raw`$a_{n+1}^2-a_n^2=2+a_n-a_n^2$`,
                      String.raw`$=(a_n-2)(a_n+1)$`,
                      String.raw`מ-$0<a_n<2$ נובע שהגורם $2-a_n$ חיובי וגם $a_n+1$ חיובי`,
                      String.raw`לכן $a_{n+1}^2>a_n^2$, ומכיוון שהאיברים חיוביים $a_{n+1}>a_n$`],
              bugIndex: 1,
              explain: String.raw`$2+a-a^2=-(a^2-a-2)=-(a-2)(a+1)=(2-a)(a+1)$. השורה השנייה כתבה $(a-2)(a+1)$, שהוא הפוך בסימן ($(a-2)(a+1)=a^2-a-2$).` },
      recap: "בודקים את הפירוק לגורמים על ידי פתיחה" },
  ],
});

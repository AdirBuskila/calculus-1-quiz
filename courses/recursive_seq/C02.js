/* recursive_seq · level 2 - fixed points: the candidate limit */
COURSE_LEVEL("recursive_seq", {
  id: "C02", order: 2, icon: "🎯", title: "נקודת שבת: הגבול המועמד",
  goal: "למצוא מהכלל הרקורסיבי את הערכים שהגבול יכול לקבל, ולבחור ביניהם.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>נניח שהסדרה מתכנסת ל-$L$. אז $a_n\to L$ וגם $a_{n+1}\to L$ (זו אותה סדרה, מוסטת באינדקס אחד). אם $f$ רציפה, הגבול של $f(a_n)$ הוא $f(L)$. מכאן שמתקיים:</p>
    <div class="lesson-formula">$$L=f(L)$$</div>
    <p>פותרים את המשוואה, וכל פתרון הוא <b>מועמד</b> לגבול (נקרא גם נקודת שבת של $f$).</p>
    <div class="lesson-ex">$a_{n+1}=\sqrt{2+a_n}$ עם $a_1=1$. מציבים: $L=\sqrt{2+L}$, מעלים בריבוע $L^2=L+2$, כלומר $L^2-L-2=0$ ו-$(L-2)(L+1)=0$.<br>
    המועמדים הם $L=2$ ו-$L=-1$. כל האיברים חיוביים, ולכן הגבול אינו שלילי ו-$L=2$.</div>
    <div class="lesson-rule">🔑 כשיש כמה מועמדים בוחרים לפי מה שכבר ידוע על הסדרה: סימן האיברים, האיבר הראשון והכיוון (סדרה עולה מ-$a_1$ לא יכולה להגיע לערך קטן מ-$a_1$).</div>
    <div class="lesson-trap">⚠️ חישוב $L$ <b>אינו הוכחת התכנסות</b>. הסדרה $a_1=1,\ a_{n+1}=2a_n+1$ נותנת $L=2L+1$, כלומר $L=-1$, אבל האיברים $1,3,7,15,\dots$ גדלים לאינסוף. המשוואה מניחה שהגבול קיים. את זה מוכיחים בנפרד (ברמות הבאות).</div>` },
  questions: [
    { id: "C02-Q1",
      step: { type: "numeric", prompt: String.raw`הסדרה $a_1=1,\ a_{n+1}=\frac{a_n}{2}+1$ מתכנסת. מהו הגבול שלה?`, answer: 2, tol: 0,
              explain: String.raw`$L=\frac{L}{2}+1\Rightarrow\frac{L}{2}=1\Rightarrow L=2$.` },
      recap: "פותרים L=f(L)" },
    { id: "C02-Q2", question: String.raw`הסדרה $a_1=1,\ a_{n+1}=\sqrt{2+a_n}$ מתכנסת, וכל איבריה חיוביים. מהו הגבול?`,
      options: [{ id: "a", value: "$-1$" }, { id: "b", value: "$2$" }, { id: "c", value: String.raw`$\sqrt2$` }, { id: "d", value: "$4$" }],
      correctId: "b",
      explanation: String.raw`$L^2=L+2$ נותן $L=2$ או $L=-1$. האיברים חיוביים ולכן $L\ge0$ ונפסל $-1$. הערכים $\sqrt2$ ו-$4$ אינם פתרונות של המשוואה.`,
      recap: "פותרים את L=f(L) ופוסלים שורש שלא מתאים לסימן האיברים" },
    { id: "C02-Q3", question: String.raw`נתונה $a_1=1,\ a_{n+1}=\frac{6}{5-a_n}$, ומתקבלים האיברים $1,\ 1.5,\ 1.71,\ 1.83,\ 1.89\dots$ מהן נקודות השבת, ולאיזו מהן הסדרה מתקרבת?`,
      options: [{ id: "a", value: "$2$ ו-$3$, והיא מתקרבת ל-$2$" }, { id: "b", value: "$2$ ו-$3$, והיא מתקרבת ל-$3$" }, { id: "c", value: "$-2$ ו-$-3$, והיא מתקרבת ל-$-2$" }, { id: "d", value: "$1$ ו-$6$, והיא מתקרבת ל-$1$" }],
      correctId: "a",
      explanation: String.raw`$L(5-L)=6\Rightarrow L^2-5L+6=0\Rightarrow(L-2)(L-3)=0$, כלומר $L=2,3$. האיברים עולים ומתקרבים ל-$2$ מלמטה, ולכן הגבול הוא $2$ ולא $3$. הזוגות $-2,-3$ ו-$1,6$ אינם פתרונות.`,
      recap: "שני מועמדים: בוחרים לפי האיברים והכיוון" },
    { id: "C02-Q4", question: String.raw`נתונה $a_1=1,\ a_{n+1}=2a_n+1$. מ-$L=2L+1$ מקבלים $L=-1$. מה נכון?`,
      options: [{ id: "a", value: "הסדרה מתכנסת ל-$-1$" }, { id: "b", value: "הסדרה לא מתכנסת, והמשוואה נותנת רק מועמד" }, { id: "c", value: "הסדרה מתכנסת ל-$1$" }, { id: "d", value: "הסדרה מתכנסת ל-$0$" }],
      correctId: "b",
      explanation: String.raw`$a_n=2^n-1$ (האיברים $1,3,7,15,\dots$) ושואפת ל-$\infty$. הפתרון $L=-1$ נובע מההנחה שהסדרה מתכנסת, וההנחה הזו שגויה כאן.`,
      recap: "L=f(L) לא מוכיחה שהגבול קיים" },
    { id: "C02-Q5",
      step: { type: "numeric", prompt: String.raw`הסדרה $a_1=3,\ a_{n+1}=\frac{1}{2}\left(a_n+\frac{7}{a_n}\right)$ מתכנסת וכל איבריה חיוביים. מהו הגבול? (עיגול לשלוש ספרות אחרי הנקודה)`, answer: 2.646, tol: 0.001,
              explain: String.raw`$L=\frac12\left(L+\frac7L\right)\Rightarrow2L=L+\frac7L\Rightarrow L=\frac7L\Rightarrow L^2=7$. חיובי, לכן $L=\sqrt7\approx2.646$.` },
      recap: "L=½(L+c/L) נותן L²=c" },
    { id: "C02-Q6",
      step: { type: "order", prompt: String.raw`סדרו את הפתרון של הגבול של $a_1=1,\ a_{n+1}=\sqrt{6+a_n}$ (נתון שהיא מתכנסת).`,
              lines: [String.raw`נסמן $L=\lim a_n$, ואז גם $a_{n+1}\to L$`,
                      String.raw`בכלל הרקורסיבי מקבלים $L=\sqrt{6+L}$`,
                      String.raw`מעלים בריבוע: $L^2-L-6=0$, כלומר $(L-3)(L+2)=0$`,
                      String.raw`כל האיברים חיוביים ולכן $L\ge0$ ו-$L=3$`],
              explain: String.raw`קודם מגדירים את $L$, אחר כך מציבים בכלל, פותרים את המשוואה, ורק בסוף בוחרים את השורש המתאים.` },
      recap: "מגדירים L, פותרים L=f(L), בוחרים שורש" },
  ],
});

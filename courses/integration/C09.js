/* integration course, level 9: מבחן מסכם: אינטגרלים ממבחנים */
COURSE_LEVEL("integration", {
  id: "C09", order: 9, icon: "🏆", title: "מבחן מסכם: אינטגרלים ממבחנים",
  goal: "לבחור שיטה ולהשלים חמישה אינטגרלים אמיתיים מהמבחנים, כל אחד בשיטה אחרת.",
  boss: true,
  source: "ai-verified",
  lesson: { html: String.raw`
<p>זו ההרצה המלאה: חמישה אינטגרלים ממבחנים אמיתיים, כל אחד בשיטה אחרת. החליטו על השיטה לפני שמתחילים לחשב.</p>
<table>
<tr><th>מה רואים</th><th>השיטה</th></tr>
<tr><td>מנה של פולינומים</td><td>דרגות, חלוקה, שברים חלקיים (גורם ריבועי: $\ln$ ו-$\arctan$)</td></tr>
<tr><td>פנימית ונגזרתה ($\ln x$ עם $\frac{dx}{x}$, $\cos2x$ עם $\sin2x$)</td><td>הצבה</td></tr>
<tr><td>פולינום × $\sin$/$\cos$/$e^x$</td><td>בחלקים, $u=$ פולינום; כמה סיבובים</td></tr>
<tr><td>$\ln^2x$ לבד</td><td>בחלקים פעמיים, $u=\ln^2x$ ואז $u=\ln x$</td></tr>
</table>
<div class="lesson-rule">🔑 בסוף גוזרים את התשובה ובודקים. זה הכלי הטוב ביותר נגד טעויות סימן.</div>
<div class="lesson-trap">⚠️ אל תשכחו את $+C$. במבחן זה מוריד נקודה.</div>
` },
  questions: [
  {
    "bankId": "24B-A-Q2a",
    "recap": "מנה, דרגות קטנות, גורם לינארי וגורם ריבועי: שברים חלקיים עם A, ובמונה הריבועי ln ו-arctan"
  },
  {
    "bankId": "24B-A-Q5a",
    "recap": "פולינום × cos 2x: בחלקים פעמיים, u = הפולינום, והפנימית 2x מחלקת ב-2"
  },
  {
    "bankId": "24A-A-Q3b",
    "recap": "sin 2x dx עם cos² 2x במכנה: הצבה t = cos 2x ← arctan"
  },
  {
    "bankId": "24A-B-Q5a",
    "recap": "ln x עם dx/x: הצבה t = ln x ← (1/2) ln(t²+1)"
  },
  {
    "bankId": "20B-C-Q4a",
    "recap": "ln² x לבד: בחלקים פעמיים, u = ln²x ואז u = ln x"
  }
],
});

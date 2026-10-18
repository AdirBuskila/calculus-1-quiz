window.COURSES = {
 "investigation": {
  "levels": [
   {
    "id": "C01",
    "order": 1,
    "icon": "🗺️",
    "title": "תחום הגדרה וחיתוכים",
    "goal": "למצוא את תחום ההגדרה של פונקציה ואת נקודות החיתוך שלה עם הצירים, בלי להכניס נקודה שמחוץ לתחום.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>חקירת פונקציה היא סדרה קבועה של צעדים. הצעד הראשון: <b>איפה הפונקציה בכלל קיימת</b>, ואיפה היא חותכת את הצירים.</p>\n<h3>תחום הגדרה</h3>\n<p>תחום ההגדרה הוא כל ערכי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> שאפשר להציב. מוציאים ממנו:</p>\n<ul>\n<li><b>מכנה שווה ל-0:</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>1</mn><mrow><mi>x</mi><mo>−</mo><mn>3</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{1}{x-3}</annotation></semantics></math></span> לא מוגדרת ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x=3</annotation></semantics></math></span>.</li>\n<li><b>שורש של מספר שלילי:</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msqrt><mi>g</mi></msqrt></mrow><annotation encoding=\"application/x-tex\">\\sqrt{g}</annotation></semantics></math></span> דורש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">g\\ge 0</annotation></semantics></math></span>.</li>\n<li><b>לוגריתם של מספר שאינו חיובי:</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>ln</mi><mo>⁡</mo><mi>g</mi></mrow><annotation encoding=\"application/x-tex\">\\ln g</annotation></semantics></math></span> דורש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">g&gt;0</annotation></semantics></math></span>.</li>\n</ul>\n<p>הפונקציה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mi>g</mi></msup></mrow><annotation encoding=\"application/x-tex\">e^{g}</annotation></semantics></math></span> מוגדרת בכל מקום שבו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi></mrow><annotation encoding=\"application/x-tex\">g</annotation></semantics></math></span> מוגדרת. למשל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mrow><mn>1</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">e^{1/x}</annotation></semantics></math></span> מוגדרת לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq 0</annotation></semantics></math></span>.</p>\n<div class=\"lesson-rule\">🔑 כותבים את תחום ההגדרה לפני כל חישוב אחר. נקודה שנפסלה כאן לא תהיה חיתוך, קיצון או פיתול.</div>\n<h3>חיתוך עם הצירים</h3>\n<ul>\n<li><b>ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span>:</b> מציבים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span>, אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> בתחום. יוצאת לכל היותר נקודה אחת.</li>\n<li><b>ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span>:</b> פותרים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f(x)=0</annotation></semantics></math></span> ובודקים שכל פתרון נמצא בתחום ההגדרה.</li>\n</ul>\n<p>עובדה שחוסכת עבודה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mi>g</mi></msup><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">e^{g}&gt;0</annotation></semantics></math></span> תמיד, ולכן גורם אקספוננטי לעולם לא מאפס את הפונקציה.</p>\n<div class=\"lesson-ex\">דוגמה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>4</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{x^2-4}{x+1}</annotation></semantics></math></span>.<br>\nתחום: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq -1</annotation></semantics></math></span>. ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><mo>−</mo><mn>4</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mo>−</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">f(0)=\\frac{-4}{1}=-4</annotation></semantics></math></span>, הנקודה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>4</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,-4)</annotation></semantics></math></span>.<br>\nציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>4</mn><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x^2-4=0</annotation></semantics></math></span> נותן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>±</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=\\pm 2</annotation></semantics></math></span>, ושניהם בתחום. הנקודות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(2,0)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-2,0)</annotation></semantics></math></span>.</div>\n<div class=\"lesson-trap\">⚠️ פתרון של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f(x)=0</annotation></semantics></math></span> שנופל מחוץ לתחום הוא לא חיתוך. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{x^2-1}{x-1}</annotation></semantics></math></span> המונה מתאפס ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=\\pm1</annotation></semantics></math></span>, אבל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> לא בתחום, ולכן רק <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,0)</annotation></semantics></math></span> הוא חיתוך.</div>\n"
    },
    "questions": [
     {
      "id": "C01-Q1",
      "question": "מהו תחום ההגדרה של $f(x)=\\frac{x}{x^2-9}$ ?",
      "options": [
       {
        "id": "a",
        "value": "$x\\neq 3$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq 3</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$x\\neq 9$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>9</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq 9</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$x\\neq \\pm 3$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mo>±</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq \\pm 3</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$x\\neq 0$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq 0</annotation></semantics></math></span>"
       }
      ],
      "correctId": "c",
      "explanation": "המכנה מתאפס כאשר $x^2-9=0$, כלומר $x=3$ או $x=-3$. התשובה **$x\\neq\\pm3$** נכונה. ‏$x\\neq 3$ שוכחת את $-3$. ‏$x\\neq 9$ נובעת מ-\\\"$x^2=9$ ולכן $x=9$\\\", אבל $9^2-9=72\\neq0$. ב-$x=0$ המכנה הוא $-9$, והפונקציה מוגדרת ושווה $0$.",
      "recap": "מכנה שווה 0 מוציא נקודה מהתחום: פותרים את המכנה ומוציאים כל פתרון",
      "questionHtml": "מהו תחום ההגדרה של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mi>x</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>9</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{x}{x^2-9}</annotation></semantics></math></span> ?",
      "explanationHtml": "המכנה מתאפס כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>9</mn><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x^2-9=0</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x=3</annotation></semantics></math></span> או <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x=-3</annotation></semantics></math></span>. התשובה <strong><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mo>±</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq\\pm3</annotation></semantics></math></span></strong> נכונה. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq 3</annotation></semantics></math></span> שוכחת את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">-3</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>9</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq 9</annotation></semantics></math></span> נובעת מ-\\\"<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn></mrow><annotation encoding=\"application/x-tex\">x^2=9</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>9</mn></mrow><annotation encoding=\"application/x-tex\">x=9</annotation></semantics></math></span>\\\", אבל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mn>9</mn><mn>2</mn></msup><mo>−</mo><mn>9</mn><mo>=</mo><mn>72</mn><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">9^2-9=72\\neq0</annotation></semantics></math></span>. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> המכנה הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>9</mn></mrow><annotation encoding=\"application/x-tex\">-9</annotation></semantics></math></span>, והפונקציה מוגדרת ושווה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>.",
      "recapHtml": "מכנה שווה 0 מוציא נקודה מהתחום: פותרים את המכנה ומוציאים כל פתרון"
     },
     {
      "id": "C01-Q2",
      "question": "מהו תחום ההגדרה של $f(x)=\\ln\\left(4-x^2\\right)$ ?",
      "options": [
       {
        "id": "a",
        "value": "$-2<x<2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>2</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">-2&lt;x&lt;2</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$x\\neq \\pm 2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mo>±</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq \\pm 2</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$|x|>2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi mathvariant=\"normal\">∣</mi><mi>x</mi><mi mathvariant=\"normal\">∣</mi><mo>&gt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">|x|&gt;2</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$x<2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;2</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "הלוגריתם דורש ארגומנט חיובי: $4-x^2>0$ אם ורק אם $x^2<4$, כלומר **$-2<x<2$**. ‏$x\\neq\\pm2$ מתייחסת אליו כאל מכנה. ‏$|x|>2$ היא התחום שבו הארגומנט שלילי. ‏$x<2$ כוללת את $x=-5$ שבו $4-25<0$.",
      "recap": "ln g דורש g > 0 (אי-שוויון חזק)",
      "questionHtml": "מהו תחום ההגדרה של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>ln</mi><mo>⁡</mo><mrow><mo fence=\"true\">(</mo><mn>4</mn><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mo fence=\"true\">)</mo></mrow></mrow><annotation encoding=\"application/x-tex\">f(x)=\\ln\\left(4-x^2\\right)</annotation></semantics></math></span> ?",
      "explanationHtml": "הלוגריתם דורש ארגומנט חיובי: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">4-x^2&gt;0</annotation></semantics></math></span> אם ורק אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&lt;</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">x^2&lt;4</annotation></semantics></math></span>, כלומר <strong><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>2</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">-2&lt;x&lt;2</annotation></semantics></math></span></strong>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mo>±</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq\\pm2</annotation></semantics></math></span> מתייחסת אליו כאל מכנה. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi mathvariant=\"normal\">∣</mi><mi>x</mi><mi mathvariant=\"normal\">∣</mi><mo>&gt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">|x|&gt;2</annotation></semantics></math></span> היא התחום שבו הארגומנט שלילי. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;2</annotation></semantics></math></span> כוללת את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>−</mo><mn>5</mn></mrow><annotation encoding=\"application/x-tex\">x=-5</annotation></semantics></math></span> שבו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn><mo>−</mo><mn>25</mn><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">4-25&lt;0</annotation></semantics></math></span>.",
      "recapHtml": "ln g דורש g &gt; 0 (אי-שוויון חזק)"
     },
     {
      "id": "C01-Q3",
      "question": "מהו תחום ההגדרה של $f(x)=\\frac{\\sqrt{x}}{x-1}$ ?",
      "options": [
       {
        "id": "a",
        "value": "$x>0$ וגם $x\\neq 1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;0</annotation></semantics></math></span> וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq 1</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$x\\neq 1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq 1</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$x\\ge 0$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x\\ge 0</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$x\\ge 0$ וגם $x\\neq 1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x\\ge 0</annotation></semantics></math></span> וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq 1</annotation></semantics></math></span>"
       }
      ],
      "correctId": "d",
      "explanation": "השורש דורש $x\\ge0$ (שימו לב: $x=0$ מותר, $\\sqrt0=0$), והמכנה דורש $x\\neq1$. התחום: **$x\\ge0$ וגם $x\\neq1$**. ‏$x>0$ מוציאה את $0$ שלא לצורך, שם $f(0)=0$. ‏$x\\neq1$ שוכחת את השורש, ו-$f(-4)$ לא מוגדרת. ‏$x\\ge0$ שוכחת את המכנה.",
      "recap": "שורש: g ≥ 0 (כולל 0). מכנה: g ≠ 0. מחברים את שני התנאים",
      "questionHtml": "מהו תחום ההגדרה של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><msqrt><mi>x</mi></msqrt><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{\\sqrt{x}}{x-1}</annotation></semantics></math></span> ?",
      "explanationHtml": "השורש דורש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x\\ge0</annotation></semantics></math></span> (שימו לב: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> מותר, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msqrt><mn>0</mn></msqrt><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">\\sqrt0=0</annotation></semantics></math></span>), והמכנה דורש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq1</annotation></semantics></math></span>. התחום: <strong><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x\\ge0</annotation></semantics></math></span> וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq1</annotation></semantics></math></span></strong>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;0</annotation></semantics></math></span> מוציאה את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> שלא לצורך, שם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f(0)=0</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq1</annotation></semantics></math></span> שוכחת את השורש, ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mo>−</mo><mn>4</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f(-4)</annotation></semantics></math></span> לא מוגדרת. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x\\ge0</annotation></semantics></math></span> שוכחת את המכנה.",
      "recapHtml": "שורש: g ≥ 0 (כולל 0). מכנה: g ≠ 0. מחברים את שני התנאים"
     },
     {
      "id": "C01-Q4",
      "step": {
       "type": "numeric",
       "prompt": "מהו ערך ה-$y$ של נקודת החיתוך של $f(x)=\\frac{2x^2+x-6}{x-2}$ עם ציר ה-$y$ ?",
       "answer": 3,
       "tol": 0,
       "explain": "$f(0)=\\frac{-6}{-2}=3$. ‏$0$ נמצא בתחום ($x\\neq2$), ולכן החיתוך הוא $(0,3)$.",
       "promptHtml": "מהו ערך ה-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> של נקודת החיתוך של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>−</mo><mn>6</mn></mrow><mrow><mi>x</mi><mo>−</mo><mn>2</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{2x^2+x-6}{x-2}</annotation></semantics></math></span> עם ציר ה-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> ?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><mo>−</mo><mn>6</mn></mrow><mrow><mo>−</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">f(0)=\\frac{-6}{-2}=3</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> נמצא בתחום (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq2</annotation></semantics></math></span>), ולכן החיתוך הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>3</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,3)</annotation></semantics></math></span>."
      },
      "recap": "ציר y: מציבים x = 0 (אם 0 בתחום)",
      "recapHtml": "ציר y: מציבים x = 0 (אם 0 בתחום)"
     },
     {
      "id": "C01-Q5",
      "question": "מהן נקודות החיתוך של $f(x)=\\frac{x^2-1}{x-1}$ עם ציר ה-$x$ ?",
      "options": [
       {
        "id": "a",
        "value": "$(1,0)$ ו-$(-1,0)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,0)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,0)</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$(-1,0)$ בלבד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,0)</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "c",
        "value": "$(1,0)$ בלבד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,0)</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "d",
        "value": "אין חיתוך עם ציר ה-$x$",
        "type": "text",
        "html": "אין חיתוך עם ציר ה-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span>"
       }
      ],
      "correctId": "b",
      "explanation": "המונה מתאפס ב-$x=\\pm1$, אבל $x=1$ מחוץ לתחום ההגדרה. נשאר **$(-1,0)$** בלבד: $f(-1)=\\frac{0}{-2}=0$. ‏$(1,0)$ אינה על הגרף כי $f(1)$ לא מוגדרת. התשובה שאין חיתוך שגויה כי $x=-1$ בתחום.",
      "recap": "פתרון של f = 0 מחוץ לתחום הוא לא חיתוך",
      "questionHtml": "מהן נקודות החיתוך של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{x^2-1}{x-1}</annotation></semantics></math></span> עם ציר ה-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> ?",
      "explanationHtml": "המונה מתאפס ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=\\pm1</annotation></semantics></math></span>, אבל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> מחוץ לתחום ההגדרה. נשאר <strong><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,0)</annotation></semantics></math></span></strong> בלבד: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mn>0</mn><mrow><mo>−</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f(-1)=\\frac{0}{-2}=0</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,0)</annotation></semantics></math></span> אינה על הגרף כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f(1)</annotation></semantics></math></span> לא מוגדרת. התשובה שאין חיתוך שגויה כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=-1</annotation></semantics></math></span> בתחום.",
      "recapHtml": "פתרון של f = 0 מחוץ לתחום הוא לא חיתוך"
     },
     {
      "id": "C01-Q6",
      "question": "מהן נקודות החיתוך של $f(x)=xe^{\\frac{1}{x-3}}$ עם הצירים ?",
      "options": [
       {
        "id": "a",
        "value": "$(0,0)$ ו-$(3,0)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,0)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(3,0)</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$(3,0)$ בלבד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(3,0)</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "c",
        "value": "$(0,0)$ בלבד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,0)</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "d",
        "value": "אין חיתוך עם הצירים",
        "type": "text",
        "html": "אין חיתוך עם הצירים"
       }
      ],
      "correctId": "c",
      "explanation": "התחום: $x\\neq3$. ציר $y$: $f(0)=0\\cdot e^{-1/3}=0$, הנקודה $(0,0)$. ציר $x$: $e^{g}>0$ תמיד, ולכן $f=0$ רק כאשר $x=0$. ‏$(3,0)$ אינה על הגרף: $x=3$ מחוץ לתחום. ‏$(0,0)$ היא גם על ציר $y$ וגם על ציר $x$, לכן יש חיתוך.",
      "recap": "e^g לא מתאפס, ולכן החיתוך נקבע על ידי הגורם האחר",
      "questionHtml": "מהן נקודות החיתוך של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mfrac><mn>1</mn><mrow><mi>x</mi><mo>−</mo><mn>3</mn></mrow></mfrac></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{\\frac{1}{x-3}}</annotation></semantics></math></span> עם הצירים ?",
      "explanationHtml": "התחום: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq3</annotation></semantics></math></span>. ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn><mo>⋅</mo><msup><mi>e</mi><mrow><mo>−</mo><mn>1</mn><mi mathvariant=\"normal\">/</mi><mn>3</mn></mrow></msup><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f(0)=0\\cdot e^{-1/3}=0</annotation></semantics></math></span>, הנקודה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,0)</annotation></semantics></math></span>. ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mi>g</mi></msup><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">e^{g}&gt;0</annotation></semantics></math></span> תמיד, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f=0</annotation></semantics></math></span> רק כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(3,0)</annotation></semantics></math></span> אינה על הגרף: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x=3</annotation></semantics></math></span> מחוץ לתחום. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,0)</annotation></semantics></math></span> היא גם על ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> וגם על ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span>, לכן יש חיתוך.",
      "recapHtml": "e^g לא מתאפס, ולכן החיתוך נקבע על ידי הגורם האחר"
     }
    ]
   },
   {
    "id": "C02",
    "order": 2,
    "icon": "📈",
    "title": "נגזרת ראשונה: עלייה וירידה",
    "goal": "לגזור, לפרק לגורמים ולבנות טבלת סימנים כדי לקבוע באילו קטעים הפונקציה עולה ובאילו יורדת.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>הנגזרת הראשונה מספרת לאן הגרף הולך. אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)&gt;0</annotation></semantics></math></span> בקטע, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> <b>עולה</b> בו. אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)&lt;0</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> <b>יורדת</b>.</p>\n<h3>כללי גזירה שנצטרך</h3>\n<ul>\n<li>מכפלה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>u</mi><mi>v</mi><msup><mo stretchy=\"false\">)</mo><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><msup><mi>u</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mi>v</mi><mo>+</mo><mi>u</mi><msup><mi>v</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup></mrow><annotation encoding=\"application/x-tex\">(uv)&#x27;=u&#x27;v+uv&#x27;</annotation></semantics></math></span>.</li>\n<li>מנה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mrow><mo fence=\"true\">(</mo><mfrac><mi>u</mi><mi>v</mi></mfrac><mo fence=\"true\">)</mo></mrow><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><mfrac><mrow><msup><mi>u</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mi>v</mi><mo>−</mo><mi>u</mi><msup><mi>v</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup></mrow><msup><mi>v</mi><mn>2</mn></msup></mfrac></mrow><annotation encoding=\"application/x-tex\">\\left(\\frac{u}{v}\\right)&#x27;=\\frac{u&#x27;v-uv&#x27;}{v^2}</annotation></semantics></math></span>.</li>\n<li>אקספוננט: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mrow><mo fence=\"true\">(</mo><msup><mi>e</mi><mi>g</mi></msup><mo fence=\"true\">)</mo></mrow><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><msup><mi>g</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mtext> </mtext><msup><mi>e</mi><mi>g</mi></msup></mrow><annotation encoding=\"application/x-tex\">\\left(e^{g}\\right)&#x27;=g&#x27;\\,e^{g}</annotation></semantics></math></span>.</li>\n</ul>\n<h3>המתכון: טבלת סימנים</h3>\n<ul>\n<li>גוזרים ומפרקים לגורמים.</li>\n<li><b>נקודות חשודות:</b> שם ש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;=0</annotation></semantics></math></span>, או ש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;</annotation></semantics></math></span> לא מוגדרת בתוך תחום ההגדרה. נקודה שמחוץ לתחום לא חשודה, אבל היא כן מפרידה בין קטעים.</li>\n<li>בכל קטע בין הנקודות בוחרים נקודת בדיקה ובודקים את סימן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;</annotation></semantics></math></span>.</li>\n</ul>\n<div class=\"lesson-rule\">🔑 <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mi>g</mi></msup></mrow><annotation encoding=\"application/x-tex\">e^{g}</annotation></semantics></math></span> תמיד חיובי, והגורם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mi>a</mi><msup><mo stretchy=\"false\">)</mo><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">(x-a)^2</annotation></semantics></math></span> אף פעם לא שלילי. הם לא משנים סימן, והסימן נקבע על ידי שאר הגורמים.</div>\n<div class=\"lesson-ex\">דוגמה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">f(x)=x^3-3x</annotation></semantics></math></span>. אז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>3</mn><mo>=</mo><mn>3</mn><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)=3x^2-3=3(x-1)(x+1)</annotation></semantics></math></span>.<br>\nנקודות חשודות: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=\\pm1</annotation></semantics></math></span>. בדיקה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>9</mn><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;(-2)=9&gt;0</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>3</mn><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;(0)=-3&lt;0</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>9</mn><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;(2)=9&gt;0</annotation></semantics></math></span>.<br>\n<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> עולה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi><mo separator=\"true\">,</mo><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-\\infty,-1)</annotation></semantics></math></span> וב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mi mathvariant=\"normal\">∞</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,\\infty)</annotation></semantics></math></span>, ויורדת ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,1)</annotation></semantics></math></span>.</div>\n<div class=\"lesson-ex\">עוד דוגמה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mrow><mo fence=\"true\">(</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo fence=\"true\">)</mo></mrow><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>x</mi><mo>⋅</mo><mrow><mo fence=\"true\">(</mo><mo>−</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo fence=\"true\">)</mo></mrow><mo>=</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">\\left(xe^{-x}\\right)&#x27;=e^{-x}+x\\cdot\\left(-e^{-x}\\right)=(1-x)e^{-x}</annotation></semantics></math></span>. הגורם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">e^{-x}</annotation></semantics></math></span> חיובי, ולכן הסימן הוא הסימן של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>−</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">1-x</annotation></semantics></math></span>: עולה כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;1</annotation></semantics></math></span>, יורדת כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span>.</div>\n<div class=\"lesson-trap\">⚠️ אם נקודה באמצע הקטע לא בתחום, לא כותבים \"יורדת בקטע <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,2)</annotation></semantics></math></span>\" כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span> חסרה. כותבים שני קטעים נפרדים, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,1)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span>.</div>\n"
    },
    "questions": [
     {
      "id": "C02-Q1",
      "question": "באילו קטעים הפונקציה $f(x)=x^3-3x$ עולה ?",
      "options": [
       {
        "id": "a",
        "value": "$x<-1$ וגם $x>1$ (שני קטעים)",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;-1</annotation></semantics></math></span> וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span> (שני קטעים)"
       },
       {
        "id": "b",
        "value": "$-1<x<1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>1</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">-1&lt;x&lt;1</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$x>0$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;0</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$x<1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;1</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "$f'=3(x-1)(x+1)$ חיובית כאשר $x<-1$ או $x>1$, ושלילית בין $-1$ ל-$1$. לכן **$x<-1$ ו-$x>1$**. הקטע $-1<x<1$ הוא דווקא קטע הירידה. ‏$x>0$ שגויה כי $f'(0.5)=-2.25<0$. ‏$x<1$ שגויה כי $f$ יורדת ב-$(-1,1)$.",
      "recap": "עולה היכן ש-f' חיובית: טבלת סימנים סביב האפסים",
      "questionHtml": "באילו קטעים הפונקציה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">f(x)=x^3-3x</annotation></semantics></math></span> עולה ?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><mn>3</mn><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f&#x27;=3(x-1)(x+1)</annotation></semantics></math></span> חיובית כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;-1</annotation></semantics></math></span> או <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span>, ושלילית בין <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">-1</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span>. לכן <strong><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;-1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span></strong>. הקטע <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>1</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">-1&lt;x&lt;1</annotation></semantics></math></span> הוא דווקא קטע הירידה. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;0</annotation></semantics></math></span> שגויה כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mn>0.5</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>2.25</mn><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;(0.5)=-2.25&lt;0</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;1</annotation></semantics></math></span> שגויה כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> יורדת ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,1)</annotation></semantics></math></span>.",
      "recapHtml": "עולה היכן ש-f' חיובית: טבלת סימנים סביב האפסים"
     },
     {
      "id": "C02-Q2",
      "question": "מהי הנגזרת של $f(x)=xe^{-x}$ ?",
      "options": [
       {
        "id": "a",
        "value": "$(1+x)e^{-x}$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">(1+x)e^{-x}</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$e^{-x}$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">e^{-x}</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$-xe^{-x}$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">-xe^{-x}</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$(1-x)e^{-x}$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">(1-x)e^{-x}</annotation></semantics></math></span>"
       }
      ],
      "correctId": "d",
      "explanation": "כלל המכפלה נותן $1\\cdot e^{-x}+x\\cdot\\left(-e^{-x}\\right)=(1-x)e^{-x}$. ‏$(1+x)e^{-x}$ שוכחת שהנגזרת של $e^{-x}$ היא $-e^{-x}$. ‏$e^{-x}$ גוזרת רק את הגורם $x$. ‏$-xe^{-x}$ גוזרת רק את האקספוננט.",
      "recap": "מכפלה עם e^g: שני אברים, ו-(e^g)' = g'·e^g",
      "questionHtml": "מהי הנגזרת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{-x}</annotation></semantics></math></span> ?",
      "explanationHtml": "כלל המכפלה נותן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>⋅</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>x</mi><mo>⋅</mo><mrow><mo fence=\"true\">(</mo><mo>−</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo fence=\"true\">)</mo></mrow><mo>=</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">1\\cdot e^{-x}+x\\cdot\\left(-e^{-x}\\right)=(1-x)e^{-x}</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">(1+x)e^{-x}</annotation></semantics></math></span> שוכחת שהנגזרת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">e^{-x}</annotation></semantics></math></span> היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">-e^{-x}</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">e^{-x}</annotation></semantics></math></span> גוזרת רק את הגורם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">-xe^{-x}</annotation></semantics></math></span> גוזרת רק את האקספוננט.",
      "recapHtml": "מכפלה עם e^g: שני אברים, ו-(e^g)' = g'·e^g"
     },
     {
      "id": "C02-Q3",
      "question": "באילו קטעים הפונקציה $f(x)=\\frac{x^2}{x-1}$ יורדת ? (נתון: $f'(x)=\\frac{x(x-2)}{(x-1)^2}$)",
      "options": [
       {
        "id": "a",
        "value": "בקטע $(0,2)$ כולו",
        "type": "text",
        "html": "בקטע <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,2)</annotation></semantics></math></span> כולו"
       },
       {
        "id": "b",
        "value": "בכל אחד מהקטעים $(0,1)$ ו-$(1,2)$ בנפרד",
        "type": "text",
        "html": "בכל אחד מהקטעים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,1)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span> בנפרד"
       },
       {
        "id": "c",
        "value": "בקטע $(-\\infty,0)$",
        "type": "text",
        "html": "בקטע <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-\\infty,0)</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "בקטע $(2,\\infty)$",
        "type": "text",
        "html": "בקטע <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>2</mn><mo separator=\"true\">,</mo><mi mathvariant=\"normal\">∞</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(2,\\infty)</annotation></semantics></math></span>"
       }
      ],
      "correctId": "b",
      "explanation": "המכנה $(x-1)^2$ חיובי, והסימן הוא של $x(x-2)$: שלילי כאשר $0<x<2$ (בלי $x=1$). ‏$f$ לא מוגדרת ב-$1$ ולכן יורדת **בכל אחד מ-$(0,1)$ ו-$(1,2)$ בנפרד**. בקטע $(0,2)$ כולו לא: $f(0.9)=-8.1$ ו-$f(1.1)=12.1$, כלומר הערך עולה בין שני צדי האסימפטוטה. ב-$(-\\infty,0)$ ו-$(2,\\infty)$ הנגזרת חיובית והפונקציה עולה.",
      "recap": "ליד נקודה שמחוץ לתחום כותבים קטעים נפרדים, לא קטע אחד",
      "questionHtml": "באילו קטעים הפונקציה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{x^2}{x-1}</annotation></semantics></math></span> יורדת ? (נתון: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><mi>x</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><msup><mo stretchy=\"false\">)</mo><mn>2</mn></msup></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)=\\frac{x(x-2)}{(x-1)^2}</annotation></semantics></math></span>)",
      "explanationHtml": "המכנה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><msup><mo stretchy=\"false\">)</mo><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">(x-1)^2</annotation></semantics></math></span> חיובי, והסימן הוא של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">x(x-2)</annotation></semantics></math></span>: שלילי כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">0&lt;x&lt;2</annotation></semantics></math></span> (בלי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span>). ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> לא מוגדרת ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span> ולכן יורדת <strong>בכל אחד מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,1)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span> בנפרד</strong>. בקטע <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,2)</annotation></semantics></math></span> כולו לא: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>0.9</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>8.1</mn></mrow><annotation encoding=\"application/x-tex\">f(0.9)=-8.1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1.1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>12.1</mn></mrow><annotation encoding=\"application/x-tex\">f(1.1)=12.1</annotation></semantics></math></span>, כלומר הערך עולה בין שני צדי האסימפטוטה. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-\\infty,0)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>2</mn><mo separator=\"true\">,</mo><mi mathvariant=\"normal\">∞</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(2,\\infty)</annotation></semantics></math></span> הנגזרת חיובית והפונקציה עולה.",
      "recapHtml": "ליד נקודה שמחוץ לתחום כותבים קטעים נפרדים, לא קטע אחד"
     },
     {
      "id": "C02-Q4",
      "step": {
       "type": "numeric",
       "prompt": "נתון $f(x)=\\frac{x^2}{x-1}$. מהו $f'(3)$ ?",
       "answer": 0.75,
       "tol": 0,
       "explain": "$f'(x)=\\frac{x(x-2)}{(x-1)^2}$, ולכן $f'(3)=\\frac{3\\cdot1}{4}=0.75$. הערך חיובי: $f$ עולה ב-$x=3$.",
       "promptHtml": "נתון <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{x^2}{x-1}</annotation></semantics></math></span>. מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mn>3</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f&#x27;(3)</annotation></semantics></math></span> ?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><mi>x</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><msup><mo stretchy=\"false\">)</mo><mn>2</mn></msup></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)=\\frac{x(x-2)}{(x-1)^2}</annotation></semantics></math></span>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mn>3</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><mn>3</mn><mo>⋅</mo><mn>1</mn></mrow><mn>4</mn></mfrac><mo>=</mo><mn>0.75</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;(3)=\\frac{3\\cdot1}{4}=0.75</annotation></semantics></math></span>. הערך חיובי: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> עולה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x=3</annotation></semantics></math></span>."
      },
      "recap": "מציבים בנגזרת המפורקת, זה מהיר יותר מלגזור שוב",
      "recapHtml": "מציבים בנגזרת המפורקת, זה מהיר יותר מלגזור שוב"
     },
     {
      "id": "C02-Q5",
      "step": {
       "type": "findbug",
       "prompt": "בחישוב הבא של נקודות החשודות של $f(x)=x^2e^{-x}$ נפלה טעות בשורה אחת. איזו ?",
       "lines": [
        "$f(x)=x^2e^{-x}$ ומחפשים נקודות חשודות",
        "$f'(x)=2xe^{-x}+x^2\\cdot\\left(-e^{-x}\\right)$",
        "$f'(x)=e^{-x}\\left(2x-x^2\\right)=xe^{-x}(2-x)$",
        "$e^{-x}>0$ ולכן $f'(x)=0$ כאשר $x=0$ או $x=-2$",
        "$f'>0$ בקטע $(0,2)$ ולכן $f$ עולה שם"
       ],
       "bugIndex": 3,
       "explain": "$xe^{-x}(2-x)=0$ כאשר $x=0$ או $2-x=0$, כלומר $x=2$ ולא $x=-2$. שורה אחרונה נכונה: ב-$(0,2)$ גם $x>0$ וגם $2-x>0$.",
       "promptHtml": "בחישוב הבא של נקודות החשודות של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=x^2e^{-x}</annotation></semantics></math></span> נפלה טעות בשורה אחת. איזו ?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo stretchy=\"false\">(</mo><mn>2</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">xe^{-x}(2-x)=0</annotation></semantics></math></span> כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> או <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>−</mo><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">2-x=0</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=2</annotation></semantics></math></span> ולא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=-2</annotation></semantics></math></span>. שורה אחרונה נכונה: ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,2)</annotation></semantics></math></span> גם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;0</annotation></semantics></math></span> וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>−</mo><mi>x</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">2-x&gt;0</annotation></semantics></math></span>.",
       "linesHtml": [
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=x^2e^{-x}</annotation></semantics></math></span> ומחפשים נקודות חשודות",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>2</mn><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>⋅</mo><mrow><mo fence=\"true\">(</mo><mo>−</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo fence=\"true\">)</mo></mrow></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)=2xe^{-x}+x^2\\cdot\\left(-e^{-x}\\right)</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mrow><mo fence=\"true\">(</mo><mn>2</mn><mi>x</mi><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mo fence=\"true\">)</mo></mrow><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo stretchy=\"false\">(</mo><mn>2</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)=e^{-x}\\left(2x-x^2\\right)=xe^{-x}(2-x)</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">e^{-x}&gt;0</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)=0</annotation></semantics></math></span> כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> או <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=-2</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&gt;0</annotation></semantics></math></span> בקטע <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,2)</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> עולה שם"
       ]
      },
      "recap": "אפסי הנגזרת מהגורם (2 − x): x = 2, לא −2",
      "recapHtml": "אפסי הנגזרת מהגורם (2 − x): x = 2, לא −2"
     }
    ]
   },
   {
    "id": "C03",
    "order": 3,
    "icon": "⛰️",
    "title": "נקודות קיצון",
    "goal": "לסווג נקודה קריטית כמקסימום, מינימום או כלום, ולחשב את ערך ה-y שלה.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>נקודת קיצון מקומי היא נקודה שבה הנגזרת <b>משנה סימן</b>.</p>\n<ul>\n<li>מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">+</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo></mrow><annotation encoding=\"application/x-tex\">-</annotation></semantics></math></span> (עולה ואחר כך יורדת): <b>מקסימום מקומי</b>.</li>\n<li>מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo></mrow><annotation encoding=\"application/x-tex\">-</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">+</annotation></semantics></math></span> (יורדת ואחר כך עולה): <b>מינימום מקומי</b>.</li>\n<li>בלי החלפת סימן: <b>אין קיצון</b>, גם אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;=0</annotation></semantics></math></span>. הדוגמה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=x^3</annotation></semantics></math></span> עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;=3x^2\\ge0</annotation></semantics></math></span>, שמתאפסת ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> אבל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> עולה כל הזמן.</li>\n</ul>\n<p>נקודה כותבים כזוג <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><msub><mi>x</mi><mn>0</mn></msub><mo separator=\"true\">,</mo><mi>f</mi><mo stretchy=\"false\">(</mo><msub><mi>x</mi><mn>0</mn></msub><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(x_0,f(x_0))</annotation></semantics></math></span>, לכן מחשבים גם את ערך ה-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span>.</p>\n<h3>קיצור עם הנגזרת השנייה</h3>\n<p>אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><msub><mi>x</mi><mn>0</mn></msub><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x_0)=0</annotation></semantics></math></span> וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><msub><mi>x</mi><mn>0</mn></msub><mo stretchy=\"false\">)</mo><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(x_0)&gt;0</annotation></semantics></math></span>, זה מינימום מקומי. אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><msub><mi>x</mi><mn>0</mn></msub><mo stretchy=\"false\">)</mo><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(x_0)&lt;0</annotation></semantics></math></span>, מקסימום מקומי. אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><msub><mi>x</mi><mn>0</mn></msub><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(x_0)=0</annotation></semantics></math></span>, הבדיקה לא מכריעה וחוזרים לטבלת הסימנים.</p>\n<div class=\"lesson-ex\">דוגמה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{-x}</annotation></semantics></math></span>. אז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)=(1-x)e^{-x}</annotation></semantics></math></span> חיובית כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;1</annotation></semantics></math></span> ושלילית כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span>.<br>\nהסימן עובר מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">+</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo></mrow><annotation encoding=\"application/x-tex\">-</annotation></semantics></math></span>, ולכן מקסימום מקומי ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> עם ערך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mn>1</mn><mi>e</mi></mfrac><mo>≈</mo><mn>0.368</mn></mrow><annotation encoding=\"application/x-tex\">f(1)=\\frac1e\\approx0.368</annotation></semantics></math></span>.</div>\n<div class=\"lesson-trap\">⚠️ \"מקסימום מקומי\" אינו \"הערך הגדול ביותר\". בפונקציה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=x+\\frac1x</annotation></semantics></math></span> יש מקסימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,-2)</annotation></semantics></math></span> ומינימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span>, והמקסימום נמוך מהמינימום.</div>\n<div class=\"lesson-trap\">⚠️ נקודה שמחוץ לתחום ההגדרה אף פעם לא קיצון, גם אם הנגזרת משנה שם סימן.</div>\n"
    },
    "questions": [
     {
      "id": "C03-Q1",
      "question": "מהי נקודת המינימום המקומי של $f(x)=x^3-3x$ ?",
      "options": [
       {
        "id": "a",
        "value": "$(-1,2)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,2)</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$(1,2)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$(1,-2)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,-2)</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$(-1,-2)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,-2)</annotation></semantics></math></span>"
       }
      ],
      "correctId": "c",
      "explanation": "$f'=3(x-1)(x+1)$ מתאפסת ב-$\\pm1$. ‏$f''=6x$: ב-$x=1$ היא $6>0$ ולכן מינימום, והערך $f(1)=1-3=-2$. התשובה **$(1,-2)$**. ‏$(-1,2)$ היא המקסימום המקומי ($f''(-1)=-6<0$). ‏$(1,2)$ ו-$(-1,-2)$ הן נקודות עם ערך $y$ שגוי: $f(1)=-2$ ו-$f(-1)=2$.",
      "recap": "מינימום: f' עוברת מ-− ל-+ (או f'' > 0), ומחשבים גם את ה-y",
      "questionHtml": "מהי נקודת המינימום המקומי של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">f(x)=x^3-3x</annotation></semantics></math></span> ?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><mn>3</mn><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f&#x27;=3(x-1)(x+1)</annotation></semantics></math></span> מתאפסת ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">\\pm1</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mn>6</mn><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=6x</annotation></semantics></math></span>: ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>6</mn><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">6&gt;0</annotation></semantics></math></span> ולכן מינימום, והערך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>1</mn><mo>−</mo><mn>3</mn><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">f(1)=1-3=-2</annotation></semantics></math></span>. התשובה <strong><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,-2)</annotation></semantics></math></span></strong>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,2)</annotation></semantics></math></span> היא המקסימום המקומי (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>6</mn><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(-1)=-6&lt;0</annotation></semantics></math></span>). ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,-2)</annotation></semantics></math></span> הן נקודות עם ערך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> שגוי: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">f(1)=-2</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">f(-1)=2</annotation></semantics></math></span>.",
      "recapHtml": "מינימום: f' עוברת מ-− ל-+ (או f'' &gt; 0), ומחשבים גם את ה-y"
     },
     {
      "id": "C03-Q2",
      "step": {
       "type": "numeric",
       "prompt": "מהו הערך של $f(x)=xe^{-x}$ בנקודת המקסימום המקומי שלה ? (עשרוני, ‏3 ספרות אחרי הנקודה)",
       "answer": 0.368,
       "tol": 0.001,
       "explain": "המקסימום ב-$x=1$ (ראו בשיעור), והערך $f(1)=e^{-1}\\approx0.368$.",
       "promptHtml": "מהו הערך של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{-x}</annotation></semantics></math></span> בנקודת המקסימום המקומי שלה ? (עשרוני, ‏3 ספרות אחרי הנקודה)",
       "explainHtml": "המקסימום ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> (ראו בשיעור), והערך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mo>≈</mo><mn>0.368</mn></mrow><annotation encoding=\"application/x-tex\">f(1)=e^{-1}\\approx0.368</annotation></semantics></math></span>."
      },
      "recap": "אחרי שמצאנו x של הקיצון, מציבים בפונקציה ולא בנגזרת",
      "recapHtml": "אחרי שמצאנו x של הקיצון, מציבים בפונקציה ולא בנגזרת"
     },
     {
      "id": "C03-Q3",
      "question": "מה נכון לגבי $f(x)=(x-1)^3+2$ בנקודה $x=1$ ?",
      "options": [
       {
        "id": "a",
        "value": "אין קיצון, כי $f'$ מתאפסת אבל לא משנה סימן",
        "type": "text",
        "html": "אין קיצון, כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;</annotation></semantics></math></span> מתאפסת אבל לא משנה סימן"
       },
       {
        "id": "b",
        "value": "מינימום מקומי ב-$(1,2)$",
        "type": "text",
        "html": "מינימום מקומי ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "מקסימום מקומי ב-$(1,2)$",
        "type": "text",
        "html": "מקסימום מקומי ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "מינימום מקומי ב-$(1,0)$",
        "type": "text",
        "html": "מינימום מקומי ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,0)</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "$f'=3(x-1)^2\\ge0$ משני צדי $1$, ומתאפסת רק ב-$x=1$. אין החלפת סימן, ולכן **אין קיצון**: הפונקציה עולה כל הזמן. טענות הקיצון (מינימום או מקסימום) דורשות החלפת סימן שלא קיימת. בנוסף $f(1)=2$ ולא $0$.",
      "recap": "f' = 0 בלי החלפת סימן: אין קיצון",
      "questionHtml": "מה נכון לגבי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><msup><mo stretchy=\"false\">)</mo><mn>3</mn></msup><mo>+</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">f(x)=(x-1)^3+2</annotation></semantics></math></span> בנקודה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> ?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><mn>3</mn><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><msup><mo stretchy=\"false\">)</mo><mn>2</mn></msup><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;=3(x-1)^2\\ge0</annotation></semantics></math></span> משני צדי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span>, ומתאפסת רק ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span>. אין החלפת סימן, ולכן <strong>אין קיצון</strong>: הפונקציה עולה כל הזמן. טענות הקיצון (מינימום או מקסימום) דורשות החלפת סימן שלא קיימת. בנוסף <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">f(1)=2</annotation></semantics></math></span> ולא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>.",
      "recapHtml": "f' = 0 בלי החלפת סימן: אין קיצון"
     },
     {
      "id": "C03-Q4",
      "step": {
       "type": "numeric",
       "prompt": "נתון $f(x)=x^4-4x^3$ ו-$f'(x)=4x^2(x-3)$. מהו ערך ה-$y$ של נקודת הקיצון היחידה של $f$ ?",
       "answer": -27,
       "tol": 0,
       "explain": "הגורם $4x^2$ אף פעם לא שלילי, ולכן סימן $f'$ הוא סימן $x-3$. ב-$x=0$ אין החלפת סימן ($f'<0$ משני הצדדים) ולכן שם אין קיצון. ב-$x=3$ הסימן עובר מ-$-$ ל-$+$: מינימום, $f(3)=81-108=-27$.",
       "promptHtml": "נתון <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>4</mn></msup><mo>−</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=x^4-4x^3</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>3</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)=4x^2(x-3)</annotation></semantics></math></span>. מהו ערך ה-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> של נקודת הקיצון היחידה של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> ?",
       "explainHtml": "הגורם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">4x^2</annotation></semantics></math></span> אף פעם לא שלילי, ולכן סימן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;</annotation></semantics></math></span> הוא סימן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x-3</annotation></semantics></math></span>. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> אין החלפת סימן (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&lt;0</annotation></semantics></math></span> משני הצדדים) ולכן שם אין קיצון. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x=3</annotation></semantics></math></span> הסימן עובר מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo></mrow><annotation encoding=\"application/x-tex\">-</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">+</annotation></semantics></math></span>: מינימום, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>3</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>81</mn><mo>−</mo><mn>108</mn><mo>=</mo><mo>−</mo><mn>27</mn></mrow><annotation encoding=\"application/x-tex\">f(3)=81-108=-27</annotation></semantics></math></span>."
      },
      "recap": "גורם ריבועי (x − a)^2 לא משנה סימן: אין קיצון ב-a",
      "recapHtml": "גורם ריבועי (x − a)^2 לא משנה סימן: אין קיצון ב-a"
     },
     {
      "id": "C03-Q5",
      "question": "מהם הקיצונים המקומיים של $f(x)=x+\\frac1x$ ? (נתון: $f'(x)=\\frac{(x-1)(x+1)}{x^2}$)",
      "options": [
       {
        "id": "a",
        "value": "מקסימום מקומי $(1,2)$ ומינימום מקומי $(-1,-2)$",
        "type": "text",
        "html": "מקסימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span> ומינימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,-2)</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "מינימום מקומי ב-$x=0$",
        "type": "text",
        "html": "מינימום מקומי ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "אין קיצון, כי המקסימום נמוך מהמינימום",
        "type": "text",
        "html": "אין קיצון, כי המקסימום נמוך מהמינימום"
       },
       {
        "id": "d",
        "value": "מקסימום מקומי $(-1,-2)$ ומינימום מקומי $(1,2)$",
        "type": "text",
        "html": "מקסימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,-2)</annotation></semantics></math></span> ומינימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span>"
       }
      ],
      "correctId": "d",
      "explanation": "הסימן של $f'$: חיובי ל-$x<-1$, שלילי ב-$(-1,0)$ וב-$(0,1)$, חיובי ל-$x>1$. ב-$x=-1$ עובר מ-$+$ ל-$-$: מקסימום מקומי, $f(-1)=-2$. ב-$x=1$ מ-$-$ ל-$+$: מינימום מקומי, $f(1)=2$. ‏$x=0$ לא בתחום, ולכן שם אין קיצון. העובדה שהמקסימום המקומי ($-2$) נמוך מהמינימום המקומי ($2$) לא מבטלת אותם: הם קיצונים מקומיים בלבד.",
      "recap": "קיצון מקומי נבדק מול הסביבה, לא מול שאר הגרף",
      "questionHtml": "מהם הקיצונים המקומיים של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=x+\\frac1x</annotation></semantics></math></span> ? (נתון: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)=\\frac{(x-1)(x+1)}{x^2}</annotation></semantics></math></span>)",
      "explanationHtml": "הסימן של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;</annotation></semantics></math></span>: חיובי ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;-1</annotation></semantics></math></span>, שלילי ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,0)</annotation></semantics></math></span> וב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,1)</annotation></semantics></math></span>, חיובי ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span>. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=-1</annotation></semantics></math></span> עובר מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">+</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo></mrow><annotation encoding=\"application/x-tex\">-</annotation></semantics></math></span>: מקסימום מקומי, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">f(-1)=-2</annotation></semantics></math></span>. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo></mrow><annotation encoding=\"application/x-tex\">-</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">+</annotation></semantics></math></span>: מינימום מקומי, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">f(1)=2</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> לא בתחום, ולכן שם אין קיצון. העובדה שהמקסימום המקומי (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">-2</annotation></semantics></math></span>) נמוך מהמינימום המקומי (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span>) לא מבטלת אותם: הם קיצונים מקומיים בלבד.",
      "recapHtml": "קיצון מקומי נבדק מול הסביבה, לא מול שאר הגרף"
     },
     {
      "id": "C03-Q6",
      "question": "נתון $f(x)=x^2e^{-x}$ עם $f'(x)=x(2-x)e^{-x}$ ו-$f''(x)=\\left(x^2-4x+2\\right)e^{-x}$. מה סוג הנקודות הקריטיות ?",
      "options": [
       {
        "id": "a",
        "value": "מקסימום ב-$x=0$ ומינימום ב-$x=2$",
        "type": "text",
        "html": "מקסימום ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> ומינימום ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=2</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "מינימום ב-$x=0$ ומקסימום ב-$x=2$",
        "type": "text",
        "html": "מינימום ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> ומקסימום ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=2</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "מינימום בשתי הנקודות",
        "type": "text",
        "html": "מינימום בשתי הנקודות"
       },
       {
        "id": "d",
        "value": "$f''(0)=0$ ולכן אי אפשר להכריע",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(0)=0</annotation></semantics></math></span> ולכן אי אפשר להכריע"
       }
      ],
      "correctId": "b",
      "explanation": "הנקודות הקריטיות הן $0$ ו-$2$. ‏$f''(0)=2>0$: מינימום. ‏$f''(2)=(4-8+2)e^{-2}=-2e^{-2}<0$: מקסימום. הסדר ההפוך מתקבל מטעות בסימן. ‏$f''(0)$ אינה $0$, ולכן הבדיקה כן מכריעה.",
      "recap": "f'' חיובית = מינימום, f'' שלילית = מקסימום",
      "questionHtml": "נתון <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=x^2e^{-x}</annotation></semantics></math></span> עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><mo stretchy=\"false\">(</mo><mn>2</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)=x(2-x)e^{-x}</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mrow><mo fence=\"true\">(</mo><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo fence=\"true\">)</mo></mrow><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(x)=\\left(x^2-4x+2\\right)e^{-x}</annotation></semantics></math></span>. מה סוג הנקודות הקריטיות ?",
      "explanationHtml": "הנקודות הקריטיות הן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>2</mn><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(0)=2&gt;0</annotation></semantics></math></span>: מינימום. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mn>4</mn><mo>−</mo><mn>8</mn><mo>+</mo><mn>2</mn><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mn>2</mn></mrow></msup><mo>=</mo><mo>−</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>−</mo><mn>2</mn></mrow></msup><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(2)=(4-8+2)e^{-2}=-2e^{-2}&lt;0</annotation></semantics></math></span>: מקסימום. הסדר ההפוך מתקבל מטעות בסימן. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(0)</annotation></semantics></math></span> אינה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>, ולכן הבדיקה כן מכריעה.",
      "recapHtml": "f'' חיובית = מינימום, f'' שלילית = מקסימום"
     }
    ]
   },
   {
    "id": "C04",
    "order": 4,
    "icon": "〰️",
    "title": "קמירות ונקודות פיתול",
    "goal": "לקבוע לפי סימן הנגזרת השנייה לאן הגרף מתעקל, ולזהות נקודת פיתול אמיתית.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>הנגזרת השנייה מספרת איך הגרף מתעקל.</p>\n<ul>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;&gt;0</annotation></semantics></math></span>: הגרף מתעקל <b>כלפי מעלה</b>, בצורת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∪</mo></mrow><annotation encoding=\"application/x-tex\">\\cup</annotation></semantics></math></span> (כמו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">y=x^2</annotation></semantics></math></span>).</li>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;&lt;0</annotation></semantics></math></span>: הגרף מתעקל <b>כלפי מטה</b>, בצורת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∩</mo></mrow><annotation encoding=\"application/x-tex\">\\cap</annotation></semantics></math></span>.</li>\n</ul>\n<div class=\"lesson-trap\">⚠️ <b>שמות:</b> בקורס <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;&gt;0</annotation></semantics></math></span> נקראת \"קעורה (כלפי מעלה)\" ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;&lt;0</annotation></semantics></math></span> נקראת \"קמורה (כלפי מטה)\". בפתרונות של מבחנים שונים השמות \"קמורה\" ו\"קעורה\" מתחלפים. לכן תמיד סומכים על הכיוון, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∪</mo></mrow><annotation encoding=\"application/x-tex\">\\cup</annotation></semantics></math></span> או <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∩</mo></mrow><annotation encoding=\"application/x-tex\">\\cap</annotation></semantics></math></span>, ועל סימן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;</annotation></semantics></math></span>. כך גם בשאלות כאן.</div>\n<h3>נקודת פיתול</h3>\n<p>נקודת פיתול היא נקודה שבה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;</annotation></semantics></math></span> <b>משנה סימן</b> והנקודה <b>בתחום ההגדרה</b>. שני התנאים נדרשים.</p>\n<ul>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=0</annotation></semantics></math></span> בלי החלפת סימן אינו פיתול: ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>=</mo><msup><mi>x</mi><mn>4</mn></msup></mrow><annotation encoding=\"application/x-tex\">f=x^4</annotation></semantics></math></span> יש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=12x^2</annotation></semantics></math></span> שאינה משנה סימן ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>.</li>\n<li>החלפת סימן בנקודה שמחוץ לתחום אינה פיתול: ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">f=\\frac1x</annotation></semantics></math></span> יש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mfrac><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=\\frac{2}{x^3}</annotation></semantics></math></span> שמשנה סימן ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>, אבל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> לא בתחום.</li>\n</ul>\n<div class=\"lesson-ex\">דוגמה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=x^3-3x^2</annotation></semantics></math></span>. אז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>6</mn><mi>x</mi><mo>−</mo><mn>6</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(x)=6x-6</annotation></semantics></math></span>, שלילית ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;1</annotation></semantics></math></span> וחיובית ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span>. הגרף <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∩</mo></mrow><annotation encoding=\"application/x-tex\">\\cap</annotation></semantics></math></span> משמאל ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∪</mo></mrow><annotation encoding=\"application/x-tex\">\\cup</annotation></semantics></math></span> מימין. נקודת פיתול ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>1</mn><mo>−</mo><mn>3</mn><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">f(1)=1-3=-2</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,-2)</annotation></semantics></math></span>.</div>\n<div class=\"lesson-ex\">עוד דוגמה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{-x}</annotation></semantics></math></span>. אז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;=(1-x)e^{-x}</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mo>−</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo>−</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo>=</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=-e^{-x}-(1-x)e^{-x}=(x-2)e^{-x}</annotation></semantics></math></span>. סימן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;</annotation></semantics></math></span> הוא סימן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x-2</annotation></semantics></math></span>: פיתול ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=2</annotation></semantics></math></span>.</div>\n"
    },
    "questions": [
     {
      "id": "C04-Q1",
      "question": "מה נכון לגבי $f(x)=x^3-3x^2$ ?",
      "options": [
       {
        "id": "a",
        "value": "הגרף כלפי מעלה ($\\cup$) כאשר $x<1$, ונקודת הפיתול היא $(1,-2)$",
        "type": "text",
        "html": "הגרף כלפי מעלה (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∪</mo></mrow><annotation encoding=\"application/x-tex\">\\cup</annotation></semantics></math></span>) כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;1</annotation></semantics></math></span>, ונקודת הפיתול היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,-2)</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "הגרף כלפי מעלה ($\\cup$) כאשר $x>1$, ונקודת הפיתול היא $(1,2)$",
        "type": "text",
        "html": "הגרף כלפי מעלה (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∪</mo></mrow><annotation encoding=\"application/x-tex\">\\cup</annotation></semantics></math></span>) כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span>, ונקודת הפיתול היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "הגרף כלפי מעלה ($\\cup$) כאשר $x>1$, ונקודת הפיתול היא $(1,-2)$",
        "type": "text",
        "html": "הגרף כלפי מעלה (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∪</mo></mrow><annotation encoding=\"application/x-tex\">\\cup</annotation></semantics></math></span>) כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span>, ונקודת הפיתול היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,-2)</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "הגרף כלפי מטה ($\\cap$) בכל התחום ואין נקודות פיתול",
        "type": "text",
        "html": "הגרף כלפי מטה (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∩</mo></mrow><annotation encoding=\"application/x-tex\">\\cap</annotation></semantics></math></span>) בכל התחום ואין נקודות פיתול"
       }
      ],
      "correctId": "c",
      "explanation": "$f''=6x-6$ חיובית ל-$x>1$ (כלפי מעלה, $\\cup$) ושלילית ל-$x<1$ (כלפי מטה, $\\cap$). ההחלפה ב-$x=1$ בתחום, לכן פיתול, ו-$f(1)=-2$. התשובה עם $x<1$ הפוכה בסימן. התשובה עם $(1,2)$ טועה בחישוב $f(1)$. ‏$f''$ משנה סימן ולכן יש פיתול.",
      "recap": "פיתול = f'' מחליפה סימן בנקודה בתחום, וה-y מחושב מ-f",
      "questionHtml": "מה נכון לגבי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=x^3-3x^2</annotation></semantics></math></span> ?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mn>6</mn><mi>x</mi><mo>−</mo><mn>6</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=6x-6</annotation></semantics></math></span> חיובית ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span> (כלפי מעלה, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∪</mo></mrow><annotation encoding=\"application/x-tex\">\\cup</annotation></semantics></math></span>) ושלילית ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;1</annotation></semantics></math></span> (כלפי מטה, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∩</mo></mrow><annotation encoding=\"application/x-tex\">\\cap</annotation></semantics></math></span>). ההחלפה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> בתחום, לכן פיתול, ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">f(1)=-2</annotation></semantics></math></span>. התשובה עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;1</annotation></semantics></math></span> הפוכה בסימן. התשובה עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span> טועה בחישוב <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f(1)</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;</annotation></semantics></math></span> משנה סימן ולכן יש פיתול.",
      "recapHtml": "פיתול = f'' מחליפה סימן בנקודה בתחום, וה-y מחושב מ-f"
     },
     {
      "id": "C04-Q2",
      "step": {
       "type": "numeric",
       "prompt": "מהו ערך ה-$x$ של נקודת הפיתול של $f(x)=xe^{-x}$ ?",
       "answer": 2,
       "tol": 0,
       "explain": "$f''=(x-2)e^{-x}$ מחליפה סימן מ-$-$ ל-$+$ ב-$x=2$, שהוא בתחום.",
       "promptHtml": "מהו ערך ה-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> של נקודת הפיתול של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{-x}</annotation></semantics></math></span> ?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=(x-2)e^{-x}</annotation></semantics></math></span> מחליפה סימן מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo></mrow><annotation encoding=\"application/x-tex\">-</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">+</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=2</annotation></semantics></math></span>, שהוא בתחום."
      },
      "recap": "מאפסים את f'' ובודקים שהסימן מתחלף",
      "recapHtml": "מאפסים את f'' ובודקים שהסימן מתחלף"
     },
     {
      "id": "C04-Q3",
      "question": "האם ל-$f(x)=x^4$ יש נקודת פיתול ב-$x=0$ ?",
      "options": [
       {
        "id": "a",
        "value": "לא: $f''=12x^2$ מתאפסת ב-$0$ אבל לא משנה סימן",
        "type": "text",
        "html": "לא: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=12x^2</annotation></semantics></math></span> מתאפסת ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> אבל לא משנה סימן"
       },
       {
        "id": "b",
        "value": "כן: $f''(0)=0$",
        "type": "text",
        "html": "כן: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(0)=0</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "כן: $f'(0)=0$",
        "type": "text",
        "html": "כן: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;(0)=0</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "לא: אין בכלל נקודה שבה $f''=0$",
        "type": "text",
        "html": "לא: אין בכלל נקודה שבה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=0</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "$f''=12x^2\\ge0$, כלומר הגרף $\\cup$ משני צדי $0$. אין החלפת סימן ולכן אין פיתול. ‏$f''(0)=0$ לבדו לא מספיק. ‏$f'(0)=0$ קשור לקיצון (כאן מינימום) ולא לפיתול. ו-$f''(0)=0$ כן מתקיים, ולכן הטענה שאין נקודה כזו שגויה.",
      "recap": "f'' = 0 הוא תנאי הכרחי בלבד לפיתול. צריך החלפת סימן",
      "questionHtml": "האם ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>4</mn></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=x^4</annotation></semantics></math></span> יש נקודת פיתול ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> ?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=12x^2\\ge0</annotation></semantics></math></span>, כלומר הגרף <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∪</mo></mrow><annotation encoding=\"application/x-tex\">\\cup</annotation></semantics></math></span> משני צדי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>. אין החלפת סימן ולכן אין פיתול. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(0)=0</annotation></semantics></math></span> לבדו לא מספיק. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;(0)=0</annotation></semantics></math></span> קשור לקיצון (כאן מינימום) ולא לפיתול. ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(0)=0</annotation></semantics></math></span> כן מתקיים, ולכן הטענה שאין נקודה כזו שגויה.",
      "recapHtml": "f'' = 0 הוא תנאי הכרחי בלבד לפיתול. צריך החלפת סימן"
     },
     {
      "id": "C04-Q4",
      "question": "האם ל-$f(x)=\\frac1x$ יש נקודת פיתול ?",
      "options": [
       {
        "id": "a",
        "value": "כן: נקודת פיתול ב-$(0,0)$",
        "type": "text",
        "html": "כן: נקודת פיתול ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,0)</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "כן: ב-$x=0$ ולכן יש אסימפטוטה אנכית",
        "type": "text",
        "html": "כן: ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> ולכן יש אסימפטוטה אנכית"
       },
       {
        "id": "c",
        "value": "לא: $f''$ אינה משנה סימן",
        "type": "text",
        "html": "לא: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;</annotation></semantics></math></span> אינה משנה סימן"
       },
       {
        "id": "d",
        "value": "לא: $f''=\\frac{2}{x^3}$ משנה סימן ב-$0$ אבל $0$ מחוץ לתחום ההגדרה",
        "type": "text",
        "html": "לא: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mfrac><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=\\frac{2}{x^3}</annotation></semantics></math></span> משנה סימן ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> אבל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> מחוץ לתחום ההגדרה"
       }
      ],
      "correctId": "d",
      "explanation": "‏$f''=\\frac{2}{x^3}$ שלילית ל-$x<0$ וחיובית ל-$x>0$, ולכן היא כן משנה סימן. אבל $f(0)$ לא מוגדרת, ואין נקודה על הגרף: **אין פיתול**. ‏$(0,0)$ לא על הגרף. הטענה שיש אסימפטוטה אנכית נכונה לגופה, אך אסימפטוטה אינה נקודת פיתול. הטענה ש-$f''$ אינה משנה סימן שגויה.",
      "recap": "פיתול רק בנקודה שבתחום",
      "questionHtml": "האם ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac1x</annotation></semantics></math></span> יש נקודת פיתול ?",
      "explanationHtml": "‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mfrac><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=\\frac{2}{x^3}</annotation></semantics></math></span> שלילית ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;0</annotation></semantics></math></span> וחיובית ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;0</annotation></semantics></math></span>, ולכן היא כן משנה סימן. אבל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f(0)</annotation></semantics></math></span> לא מוגדרת, ואין נקודה על הגרף: <strong>אין פיתול</strong>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,0)</annotation></semantics></math></span> לא על הגרף. הטענה שיש אסימפטוטה אנכית נכונה לגופה, אך אסימפטוטה אינה נקודת פיתול. הטענה ש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;</annotation></semantics></math></span> אינה משנה סימן שגויה.",
      "recapHtml": "פיתול רק בנקודה שבתחום"
     },
     {
      "id": "C04-Q5",
      "step": {
       "type": "numeric",
       "prompt": "נתון $f(x)=x^2e^{-x}$ עם $f''(x)=\\left(x^2-4x+2\\right)e^{-x}$. מהו ערך ה-$x$ הגדול מבין שתי נקודות הפיתול ? (עשרוני, ‏3 ספרות אחרי הנקודה)",
       "answer": 3.414,
       "tol": 0.001,
       "explain": "$x^2-4x+2=0$ נותן $x=2\\pm\\sqrt2$. הגדול הוא $2+\\sqrt2\\approx3.414$. בשני הפתרונות $f''$ מחליפה סימן (שורשים פשוטים של הפולינום), והם בתחום.",
       "promptHtml": "נתון <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=x^2e^{-x}</annotation></semantics></math></span> עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mrow><mo fence=\"true\">(</mo><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo fence=\"true\">)</mo></mrow><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(x)=\\left(x^2-4x+2\\right)e^{-x}</annotation></semantics></math></span>. מהו ערך ה-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> הגדול מבין שתי נקודות הפיתול ? (עשרוני, ‏3 ספרות אחרי הנקודה)",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x^2-4x+2=0</annotation></semantics></math></span> נותן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>2</mn><mo>±</mo><msqrt><mn>2</mn></msqrt></mrow><annotation encoding=\"application/x-tex\">x=2\\pm\\sqrt2</annotation></semantics></math></span>. הגדול הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>+</mo><msqrt><mn>2</mn></msqrt><mo>≈</mo><mn>3.414</mn></mrow><annotation encoding=\"application/x-tex\">2+\\sqrt2\\approx3.414</annotation></semantics></math></span>. בשני הפתרונות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;</annotation></semantics></math></span> מחליפה סימן (שורשים פשוטים של הפולינום), והם בתחום."
      },
      "recap": "פיתול: שורשי f'' עם החלפת סימן",
      "recapHtml": "פיתול: שורשי f'' עם החלפת סימן"
     },
     {
      "id": "C04-Q6",
      "step": {
       "type": "findbug",
       "prompt": "בחישוב הנגזרת השנייה של $f(x)=xe^{-x}$ נפלה טעות בשורה אחת. איזו ?",
       "lines": [
        "$f(x)=xe^{-x}$",
        "$f'(x)=(1-x)e^{-x}$",
        "$f''(x)=-e^{-x}+(1-x)e^{-x}$",
        "$f''(x)=(x-2)e^{-x}$",
        "$f''<0$ ל-$x<2$ ו-$f''>0$ ל-$x>2$, ולכן פיתול ב-$x=2$"
       ],
       "bugIndex": 2,
       "explain": "הנגזרת של $(1-x)e^{-x}$ היא $-1\\cdot e^{-x}+(1-x)\\cdot\\left(-e^{-x}\\right)$. השורה השגויה משאירה את האיבר השני חיובי. שורה 3 היא התוצאה הנכונה.",
       "promptHtml": "בחישוב הנגזרת השנייה של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{-x}</annotation></semantics></math></span> נפלה טעות בשורה אחת. איזו ?",
       "explainHtml": "הנגזרת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">(1-x)e^{-x}</annotation></semantics></math></span> היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>1</mn><mo>⋅</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo>+</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>⋅</mo><mrow><mo fence=\"true\">(</mo><mo>−</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo fence=\"true\">)</mo></mrow></mrow><annotation encoding=\"application/x-tex\">-1\\cdot e^{-x}+(1-x)\\cdot\\left(-e^{-x}\\right)</annotation></semantics></math></span>. השורה השגויה משאירה את האיבר השני חיובי. שורה 3 היא התוצאה הנכונה.",
       "linesHtml": [
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{-x}</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)=(1-x)e^{-x}</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup><mo>+</mo><mo stretchy=\"false\">(</mo><mn>1</mn><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(x)=-e^{-x}+(1-x)e^{-x}</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(x)=(x-2)e^{-x}</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;&lt;0</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;2</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;&gt;0</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;2</annotation></semantics></math></span>, ולכן פיתול ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=2</annotation></semantics></math></span>"
       ]
      },
      "recap": "גוזרים את e^{-x} ← מינוס. בכל כלל מכפלה",
      "recapHtml": "גוזרים את e^{-x} ← מינוס. בכל כלל מכפלה"
     }
    ]
   },
   {
    "id": "C05",
    "order": 5,
    "icon": "🧱",
    "title": "אסימפטוטות אנכיות ואופקיות",
    "goal": "לחשב גבולות חד-צדדיים ולקבוע איפה יש אסימפטוטה אנכית ואיפה אופקית, בכל צד בנפרד.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<h3>אסימפטוטה אנכית</h3>\n<p>הישר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><msub><mi>x</mi><mn>0</mn></msub></mrow><annotation encoding=\"application/x-tex\">x=x_0</annotation></semantics></math></span> הוא אסימפטוטה אנכית אם <b>לפחות גבול חד-צדדי אחד</b> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>x</mi><mn>0</mn></msub></mrow><annotation encoding=\"application/x-tex\">x_0</annotation></semantics></math></span> הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>±</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\pm\\infty</annotation></semantics></math></span>. בודקים את הנקודות שנפסלו מהתחום ואת קצות התחום, ומחשבים את שני הצדדים בנפרד.</p>\n<p>אם הגבול סופי, זו \"חור\" בגרף ולא אסימפטוטה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>→</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">\\frac{x^2-1}{x-1}=x+1\\to2</annotation></semantics></math></span> כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\to1</annotation></semantics></math></span>.</p>\n<h3>אסימפטוטה אופקית</h3>\n<p>הישר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">y=L</annotation></semantics></math></span> הוא אסימפטוטה אופקית אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mrow><mi>lim</mi><mo>⁡</mo></mrow><mrow><mi>x</mi><mo>→</mo><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow></msub><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">\\lim_{x\\to+\\infty}f(x)=L</annotation></semantics></math></span> או <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mrow><mi>lim</mi><mo>⁡</mo></mrow><mrow><mi>x</mi><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow></msub><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">\\lim_{x\\to-\\infty}f(x)=L</annotation></semantics></math></span>. בודקים כל צד בנפרד, ויכולה להיות אסימפטוטה בצד אחד בלבד.</p>\n<h3>גבולות שחוזרים</h3>\n<ul>\n<li>פולינומים שווי דרגה: היחס בין המקדמים המובילים. למשל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfrac><mo>→</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">\\frac{3x^2+1}{x^2+5}\\to3</annotation></semantics></math></span>.</li>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mi>x</mi></msup></mrow><annotation encoding=\"application/x-tex\">e^{x}</annotation></semantics></math></span> מנצחת כל חזקה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mi>x</mi></msup><mi mathvariant=\"normal\">/</mi><msup><mi>x</mi><mi>n</mi></msup><mo>→</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">e^{x}/x^n\\to\\infty</annotation></semantics></math></span> כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">x\\to\\infty</annotation></semantics></math></span>, ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>x</mi><mi>n</mi></msup><msup><mi>e</mi><mi>x</mi></msup><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x^ne^{x}\\to0</annotation></semantics></math></span> כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">x\\to-\\infty</annotation></semantics></math></span>.</li>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>ln</mi><mo>⁡</mo><mi>x</mi><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\ln x\\to-\\infty</annotation></semantics></math></span> כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><msup><mn>0</mn><mo>+</mo></msup></mrow><annotation encoding=\"application/x-tex\">x\\to0^+</annotation></semantics></math></span>.</li>\n</ul>\n<p>כשהגבול בצורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mi mathvariant=\"normal\">∞</mi><mi mathvariant=\"normal\">∞</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{\\infty}{\\infty}</annotation></semantics></math></span> אפשר להשתמש בלופיטל: גוזרים מונה ומכנה בנפרד. כדי להשתמש בו, כותבים מכפלה כמנה. למשל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mfrac><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mfrac></mrow><annotation encoding=\"application/x-tex\">xe^{x}=\\frac{x}{e^{-x}}</annotation></semantics></math></span>.</p>\n<div class=\"lesson-ex\">דוגמה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>e</mi><mrow><mn>1</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=e^{1/x}</annotation></semantics></math></span>. כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><msup><mn>0</mn><mo>+</mo></msup></mrow><annotation encoding=\"application/x-tex\">x\\to0^+</annotation></semantics></math></span> מתקיים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>→</mo><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\frac1x\\to+\\infty</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>→</mo><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">f\\to+\\infty</annotation></semantics></math></span>. כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><msup><mn>0</mn><mo>−</mo></msup></mrow><annotation encoding=\"application/x-tex\">x\\to0^-</annotation></semantics></math></span> מתקיים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\frac1x\\to-\\infty</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f\\to0</annotation></semantics></math></span>.<br>\nמספיק צד אחד: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> אסימפטוטה אנכית (מימין). ובשני הצדדים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">\\frac1x\\to0</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>→</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">f\\to1</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=1</annotation></semantics></math></span> אופקית.</div>\n<div class=\"lesson-trap\">⚠️ גבול סופי ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>x</mi><mn>0</mn></msub></mrow><annotation encoding=\"application/x-tex\">x_0</annotation></semantics></math></span> משמעותו שאין אסימפטוטה אנכית שם, גם אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> לא מוגדרת ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>x</mi><mn>0</mn></msub></mrow><annotation encoding=\"application/x-tex\">x_0</annotation></semantics></math></span>.</div>\n"
    },
    "questions": [
     {
      "id": "C05-Q1",
      "question": "מה נכון לגבי $f(x)=\\frac{x^2-1}{x-1}$ בנקודה $x=1$ ?",
      "options": [
       {
        "id": "a",
        "value": "$x=1$ אסימפטוטה אנכית, כי המכנה מתאפס",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> אסימפטוטה אנכית, כי המכנה מתאפס"
       },
       {
        "id": "b",
        "value": "אין אסימפטוטה אנכית: הגבול ב-$x=1$ סופי ושווה ל-$2$",
        "type": "text",
        "html": "אין אסימפטוטה אנכית: הגבול ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> סופי ושווה ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$x=1$ אסימפטוטה אנכית, כי $f(1)$ לא מוגדרת",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> אסימפטוטה אנכית, כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f(1)</annotation></semantics></math></span> לא מוגדרת"
       },
       {
        "id": "d",
        "value": "אין אסימפטוטה אנכית, כי הגבול ב-$x=1$ שווה ל-$0$",
        "type": "text",
        "html": "אין אסימפטוטה אנכית, כי הגבול ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> שווה ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>"
       }
      ],
      "correctId": "b",
      "explanation": "אחרי צמצום $f(x)=x+1$ לכל $x\\neq1$, ולכן שני הגבולות החד-צדדיים ב-$1$ שווים ל-$2$. הגבול סופי ולכן **אין אסימפטוטה** (יש חור ב-$(1,2)$). מכנה שמתאפס ולכך ש-$f(1)$ לא מוגדרת הם רק סיבות לבדוק, לא סיבות להכריז על אסימפטוטה. הגבול אינו $0$ אלא $2$.",
      "recap": "מכנה 0 ≠ אסימפטוטה. מחשבים את הגבול",
      "questionHtml": "מה נכון לגבי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{x^2-1}{x-1}</annotation></semantics></math></span> בנקודה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> ?",
      "explanationHtml": "אחרי צמצום <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">f(x)=x+1</annotation></semantics></math></span> לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq1</annotation></semantics></math></span>, ולכן שני הגבולות החד-צדדיים ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span> שווים ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span>. הגבול סופי ולכן <strong>אין אסימפטוטה</strong> (יש חור ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span>). מכנה שמתאפס ולכך ש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f(1)</annotation></semantics></math></span> לא מוגדרת הם רק סיבות לבדוק, לא סיבות להכריז על אסימפטוטה. הגבול אינו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> אלא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span>.",
      "recapHtml": "מכנה 0 ≠ אסימפטוטה. מחשבים את הגבול"
     },
     {
      "id": "C05-Q2",
      "question": "מה נכון לגבי $f(x)=e^{1/x}$ ב-$x=0$ ?",
      "options": [
       {
        "id": "a",
        "value": "$x=0$ אסימפטוטה אנכית משני הצדדים",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> אסימפטוטה אנכית משני הצדדים"
       },
       {
        "id": "b",
        "value": "אין אסימפטוטה אנכית, כי משמאל הגבול סופי",
        "type": "text",
        "html": "אין אסימפטוטה אנכית, כי משמאל הגבול סופי"
       },
       {
        "id": "c",
        "value": "$x=0$ אסימפטוטה אנכית מימין בלבד, ומשמאל $f\\to0$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> אסימפטוטה אנכית מימין בלבד, ומשמאל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f\\to0</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$x=0$ אסימפטוטה אנכית משמאל בלבד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> אסימפטוטה אנכית משמאל בלבד"
       }
      ],
      "correctId": "c",
      "explanation": "מימין $\\frac1x\\to+\\infty$ ולכן $e^{1/x}\\to+\\infty$. משמאל $\\frac1x\\to-\\infty$ ולכן $e^{1/x}\\to0$. מספיק צד אחד אינסופי: **אסימפטוטה אנכית מימין**. הטענה שהיא משני הצדדים או משמאל שגויה כי משמאל הגבול הוא $0$, והטענה שאין אסימפטוטה מתעלמת מהצד הימני.",
      "recap": "אסימפטוטה אנכית: מספיק גבול חד-צדדי אחד אינסופי",
      "questionHtml": "מה נכון לגבי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>e</mi><mrow><mn>1</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=e^{1/x}</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> ?",
      "explanationHtml": "מימין <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>→</mo><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\frac1x\\to+\\infty</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mrow><mn>1</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup><mo>→</mo><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">e^{1/x}\\to+\\infty</annotation></semantics></math></span>. משמאל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\frac1x\\to-\\infty</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mrow><mn>1</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">e^{1/x}\\to0</annotation></semantics></math></span>. מספיק צד אחד אינסופי: <strong>אסימפטוטה אנכית מימין</strong>. הטענה שהיא משני הצדדים או משמאל שגויה כי משמאל הגבול הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>, והטענה שאין אסימפטוטה מתעלמת מהצד הימני.",
      "recapHtml": "אסימפטוטה אנכית: מספיק גבול חד-צדדי אחד אינסופי"
     },
     {
      "id": "C05-Q3",
      "step": {
       "type": "numeric",
       "prompt": "מהו $L$ באסימפטוטה האופקית $y=L$ של $f(x)=\\frac{3x^2+1}{x^2+5}$ ?",
       "answer": 3,
       "tol": 0,
       "explain": "מחלקים מונה ומכנה ב-$x^2$: $\\frac{3+1/x^2}{1+5/x^2}\\to3$. אותו הגבול גם ב-$-\\infty$.",
       "promptHtml": "מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">L</annotation></semantics></math></span> באסימפטוטה האופקית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">y=L</annotation></semantics></math></span> של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{3x^2+1}{x^2+5}</annotation></semantics></math></span> ?",
       "explainHtml": "מחלקים מונה ומכנה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">x^2</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><mn>3</mn><mo>+</mo><mn>1</mn><mi mathvariant=\"normal\">/</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>5</mn><mi mathvariant=\"normal\">/</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>→</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">\\frac{3+1/x^2}{1+5/x^2}\\to3</annotation></semantics></math></span>. אותו הגבול גם ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span>."
      },
      "recap": "דרגות שוות: היחס בין המקדמים המובילים",
      "recapHtml": "דרגות שוות: היחס בין המקדמים המובילים"
     },
     {
      "id": "C05-Q4",
      "question": "מהן האסימפטוטות האופקיות של $f(x)=x^2e^{x}$ ?",
      "options": [
       {
        "id": "a",
        "value": "$y=0$ ב-$-\\infty$ בלבד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "b",
        "value": "$y=0$ בשני הכיוונים",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span> בשני הכיוונים"
       },
       {
        "id": "c",
        "value": "אין אסימפטוטה אופקית",
        "type": "text",
        "html": "אין אסימפטוטה אופקית"
       },
       {
        "id": "d",
        "value": "$y=1$ ב-$+\\infty$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=1</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "כש-$x\\to-\\infty$ האקספוננט מנצח את החזקה: $x^2e^{x}\\to0$. כש-$x\\to+\\infty$ שני הגורמים גדלים ו-$f\\to+\\infty$. לכן **$y=0$ ב-$-\\infty$ בלבד**. הטענה שאין אסימפטוטה אופקית מתעלמת מ-$-\\infty$ שבו הגבול הוא $0$. ‏$y=1$ לא מתקבלת באף כיוון.",
      "recap": "מנסים כל צד בנפרד: x²eˣ → 0 ב-−∞ ולא ב-+∞",
      "questionHtml": "מהן האסימפטוטות האופקיות של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mi>x</mi></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=x^2e^{x}</annotation></semantics></math></span> ?",
      "explanationHtml": "כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">x\\to-\\infty</annotation></semantics></math></span> האקספוננט מנצח את החזקה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mi>x</mi></msup><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x^2e^{x}\\to0</annotation></semantics></math></span>. כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">x\\to+\\infty</annotation></semantics></math></span> שני הגורמים גדלים ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>→</mo><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">f\\to+\\infty</annotation></semantics></math></span>. לכן <strong><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span> בלבד</strong>. הטענה שאין אסימפטוטה אופקית מתעלמת מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span> שבו הגבול הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=1</annotation></semantics></math></span> לא מתקבלת באף כיוון.",
      "recapHtml": "מנסים כל צד בנפרד: x²eˣ → 0 ב-−∞ ולא ב-+∞"
     },
     {
      "id": "C05-Q5",
      "question": "מהן האסימפטוטות של $f(x)=\\frac{\\ln x}{x}$ ?",
      "options": [
       {
        "id": "a",
        "value": "אנכית $x=0$ בלבד",
        "type": "text",
        "html": "אנכית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "b",
        "value": "אופקית $y=0$ בלבד",
        "type": "text",
        "html": "אופקית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "c",
        "value": "אנכית $x=1$ ואופקית $y=0$",
        "type": "text",
        "html": "אנכית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> ואופקית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "אנכית $x=0$ ואופקית $y=0$ (ב-$+\\infty$)",
        "type": "text",
        "html": "אנכית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> ואופקית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span> (ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span>)"
       }
      ],
      "correctId": "d",
      "explanation": "התחום הוא $x>0$. כש-$x\\to0^+$ המונה $\\ln x\\to-\\infty$ והמכנה קטן וחיובי, ולכן $f\\to-\\infty$: אנכית $x=0$. כש-$x\\to\\infty$ הלוגריתם גדל לאט מ-$x$ ולכן $f\\to0$: אופקית $y=0$. ב-$x=1$ מתקבל $f(1)=0$, בלי אסימפטוטה. ‏$f$ אינה מוגדרת ב-$-\\infty$, ולכן האופקית רק בצד ימין.",
      "recap": "בקצה התחום הפתוח (x → 0⁺) בודקים אסימפטוטה אנכית",
      "questionHtml": "מהן האסימפטוטות של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><mi>ln</mi><mo>⁡</mo><mi>x</mi></mrow><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{\\ln x}{x}</annotation></semantics></math></span> ?",
      "explanationHtml": "התחום הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;0</annotation></semantics></math></span>. כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><msup><mn>0</mn><mo>+</mo></msup></mrow><annotation encoding=\"application/x-tex\">x\\to0^+</annotation></semantics></math></span> המונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>ln</mi><mo>⁡</mo><mi>x</mi><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\ln x\\to-\\infty</annotation></semantics></math></span> והמכנה קטן וחיובי, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">f\\to-\\infty</annotation></semantics></math></span>: אנכית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span>. כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">x\\to\\infty</annotation></semantics></math></span> הלוגריתם גדל לאט מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f\\to0</annotation></semantics></math></span>: אופקית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span>. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> מתקבל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f(1)=0</annotation></semantics></math></span>, בלי אסימפטוטה. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> אינה מוגדרת ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span>, ולכן האופקית רק בצד ימין.",
      "recapHtml": "בקצה התחום הפתוח (x → 0⁺) בודקים אסימפטוטה אנכית"
     },
     {
      "id": "C05-Q6",
      "step": {
       "type": "order",
       "prompt": "סדרו את החישוב של $\\lim_{x\\to-\\infty}xe^{x}$ בסדר הנכון.",
       "lines": [
        "כותבים כמנה: $xe^{x}=\\frac{x}{e^{-x}}$, וכאשר $x\\to-\\infty$ זו צורה $\\frac{-\\infty}{\\infty}$",
        "לופיטל: גוזרים מונה ומכנה בנפרד ומקבלים $\\frac{1}{-e^{-x}}$",
        "כאשר $x\\to-\\infty$ המכנה $-e^{-x}$ שואף ל-$-\\infty$",
        "לכן הגבול הוא $0$, והישר $y=0$ אסימפטוטה אופקית משמאל"
       ],
       "explain": "כל שורה משתמשת בקודמתה: קודם הופכים למנה, אחר כך גוזרים, אחר כך בודקים את המכנה, ורק אז מסיקים.",
       "promptHtml": "סדרו את החישוב של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mrow><mi>lim</mi><mo>⁡</mo></mrow><mrow><mi>x</mi><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow></msub><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup></mrow><annotation encoding=\"application/x-tex\">\\lim_{x\\to-\\infty}xe^{x}</annotation></semantics></math></span> בסדר הנכון.",
       "explainHtml": "כל שורה משתמשת בקודמתה: קודם הופכים למנה, אחר כך גוזרים, אחר כך בודקים את המכנה, ורק אז מסיקים.",
       "linesHtml": [
        "כותבים כמנה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mfrac><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mfrac></mrow><annotation encoding=\"application/x-tex\">xe^{x}=\\frac{x}{e^{-x}}</annotation></semantics></math></span>, וכאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">x\\to-\\infty</annotation></semantics></math></span> זו צורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><mi mathvariant=\"normal\">∞</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{-\\infty}{\\infty}</annotation></semantics></math></span>",
        "לופיטל: גוזרים מונה ומכנה בנפרד ומקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>1</mn><mrow><mo>−</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{1}{-e^{-x}}</annotation></semantics></math></span>",
        "כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">x\\to-\\infty</annotation></semantics></math></span> המכנה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">-e^{-x}</annotation></semantics></math></span> שואף ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span>",
        "לכן הגבול הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>, והישר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span> אסימפטוטה אופקית משמאל"
       ]
      },
      "recap": "מכפלה שמשאירה אותנו ב-∞·0: כותבים כמנה ← לופיטל",
      "recapHtml": "מכפלה שמשאירה אותנו ב-∞·0: כותבים כמנה ← לופיטל"
     }
    ]
   },
   {
    "id": "C06",
    "order": 6,
    "icon": "📐",
    "title": "אסימפטוטה משופעת",
    "goal": "לחשב a ו-b לכל צד בנפרד, בחילוק פולינומים או בגבול עם אקספוננט, ולקבוע אם יש אסימפטוטה משופעת.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>כשהגרף מתקרב לקו ישר שאינו אופקי, זו <b>אסימפטוטה משופעת</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></mrow><annotation encoding=\"application/x-tex\">y=ax+b</annotation></semantics></math></span>.</p>\n<div class=\"lesson-formula\"><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><mfrac><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo></mrow><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">a=\\lim\\frac{f(x)}{x}</annotation></semantics></math></span> וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><mrow><mo fence=\"true\">(</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>−</mo><mi>a</mi><mi>x</mi><mo fence=\"true\">)</mo></mrow></mrow><annotation encoding=\"application/x-tex\">b=\\lim\\left(f(x)-ax\\right)</annotation></semantics></math></span></div>\n<ul>\n<li>מחשבים את שני הגבולות ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span> ובנפרד ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span>, כי כל צד עשוי להתנהג אחרת.</li>\n<li>אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi></mrow><annotation encoding=\"application/x-tex\">a</annotation></semantics></math></span> אינסופי, או ש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi></mrow><annotation encoding=\"application/x-tex\">b</annotation></semantics></math></span> אינו קיים, אין אסימפטוטה משופעת בצד הזה. אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">a=0</annotation></semantics></math></span> זו אסימפטוטה אופקית.</li>\n</ul>\n<h3>פונקציה רציונלית</h3>\n<p>כשדרגת המונה גדולה ב-1 מדרגת המכנה, מחלקים פולינומים ומקבלים את הישר מיד: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mi>x</mi></mfrac><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{x^2+1}{x}=x+\\frac1x</annotation></semantics></math></span>, והשארית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">\\frac1x\\to0</annotation></semantics></math></span>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span>.</p>\n<h3>הגבול <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><msup><mi>e</mi><mi>u</mi></msup><mo>−</mo><mn>1</mn></mrow><mi>u</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{e^u-1}{u}</annotation></semantics></math></span></h3>\n<p>הגבול <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mrow><mi>lim</mi><mo>⁡</mo></mrow><mrow><mi>u</mi><mo>→</mo><mn>0</mn></mrow></msub><mfrac><mrow><msup><mi>e</mi><mi>u</mi></msup><mo>−</mo><mn>1</mn></mrow><mi>u</mi></mfrac><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">\\lim_{u\\to0}\\frac{e^u-1}{u}=1</annotation></semantics></math></span> (זו הנגזרת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mi>u</mi></msup></mrow><annotation encoding=\"application/x-tex\">e^u</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>). עם הצבה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>u</mi><mo>=</mo><mfrac><mi>c</mi><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">u=\\frac cx</annotation></semantics></math></span> מקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>lim</mi><mo>⁡</mo><mi>x</mi><mrow><mo fence=\"true\">(</mo><msup><mi>e</mi><mrow><mi>c</mi><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup><mo>−</mo><mn>1</mn><mo fence=\"true\">)</mo></mrow><mo>=</mo><mi>c</mi></mrow><annotation encoding=\"application/x-tex\">\\lim x\\left(e^{c/x}-1\\right)=c</annotation></semantics></math></span>.</p>\n<div class=\"lesson-ex\">דוגמה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mn>1</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{1/x}</annotation></semantics></math></span>.<br>\n<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><msup><mi>e</mi><mrow><mn>1</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mn>0</mn></msup><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=\\lim e^{1/x}=e^0=1</annotation></semantics></math></span>.<br>\n<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><mrow><mo fence=\"true\">(</mo><mi>x</mi><msup><mi>e</mi><mrow><mn>1</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup><mo>−</mo><mi>x</mi><mo fence=\"true\">)</mo></mrow><mo>=</mo><mi>lim</mi><mo>⁡</mo><mi>x</mi><mrow><mo fence=\"true\">(</mo><msup><mi>e</mi><mrow><mn>1</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup><mo>−</mo><mn>1</mn><mo fence=\"true\">)</mo></mrow></mrow><annotation encoding=\"application/x-tex\">b=\\lim\\left(xe^{1/x}-x\\right)=\\lim x\\left(e^{1/x}-1\\right)</annotation></semantics></math></span>. עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>u</mi><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">u=\\frac1x\\to0</annotation></semantics></math></span> זה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>lim</mi><mo>⁡</mo><mfrac><mrow><msup><mi>e</mi><mi>u</mi></msup><mo>−</mo><mn>1</mn></mrow><mi>u</mi></mfrac><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">\\lim\\frac{e^u-1}{u}=1</annotation></semantics></math></span>.<br>\nהאסימפטוטה המשופעת: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x+1</annotation></semantics></math></span>, ובשני הצדדים.</div>\n<div class=\"lesson-ex\">דוגמה לצד אחד בלבד: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=x+e^{x}</annotation></semantics></math></span>. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">b=\\lim e^{x}=0</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span>. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mi>f</mi><mi>x</mi></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><msup><mi>e</mi><mi>x</mi></msup><mi>x</mi></mfrac><mo>→</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\frac{f}{x}=1+\\frac{e^x}{x}\\to\\infty</annotation></semantics></math></span>, ולכן אין אסימפטוטה משופעת שם.</div>\n"
    },
    "questions": [
     {
      "id": "C06-Q1",
      "question": "מהי האסימפטוטה המשופעת של $f(x)=\\frac{x^2+1}{x}$ ?",
      "options": [
       {
        "id": "a",
        "value": "$y=x+1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x+1</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$y=x$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$y=0$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$y=x-1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x-1</annotation></semantics></math></span>"
       }
      ],
      "correctId": "b",
      "explanation": "$f(x)=x+\\frac1x$, ו-$\\frac1x\\to0$. לכן $a=1$ ו-$b=0$: **$y=x$**. ‏$y=x+1$ ו-$y=x-1$ מתקבלות מ-$b=1$ ו-$b=-1$, אבל $b=0$. ‏$y=0$ אינה אסימפטוטה כי $f\\to\\infty$.",
      "recap": "מחלקים פולינומים: השארית שואפת ל-0, והמנה היא הישר",
      "questionHtml": "מהי האסימפטוטה המשופעת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{x^2+1}{x}</annotation></semantics></math></span> ?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=x+\\frac1x</annotation></semantics></math></span>, ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">\\frac1x\\to0</annotation></semantics></math></span>. לכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">b=0</annotation></semantics></math></span>: <strong><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span></strong>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x+1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x-1</annotation></semantics></math></span> מתקבלות מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">b=1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">b=-1</annotation></semantics></math></span>, אבל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">b=0</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span> אינה אסימפטוטה כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>→</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">f\\to\\infty</annotation></semantics></math></span>.",
      "recapHtml": "מחלקים פולינומים: השארית שואפת ל-0, והמנה היא הישר"
     },
     {
      "id": "C06-Q2",
      "question": "מהי האסימפטוטה המשופעת של $f(x)=\\frac{x^2+x+1}{x-1}$ ?",
      "options": [
       {
        "id": "a",
        "value": "$y=x+1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x+1</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$y=x$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$y=x+2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">y=x+2</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$y=x-2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">y=x-2</annotation></semantics></math></span>"
       }
      ],
      "correctId": "c",
      "explanation": "חילוק: $x^2+x+1=(x-1)(x+2)+3$, ולכן $f=x+2+\\frac{3}{x-1}$. השארית שואפת ל-$0$ בשני הצדדים: **$y=x+2$**. הבחירות האחרות מתקבלות מחילוק שגוי ($x+1$ מתעלמת מהאיבר $x$ בשארית, ו-$x-2$ מטעות בסימן של $-1$).",
      "recap": "חילוק פולינומים נותן את b כפשוט",
      "questionHtml": "מהי האסימפטוטה המשופעת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{x^2+x+1}{x-1}</annotation></semantics></math></span> ?",
      "explanationHtml": "חילוק: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>+</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">x^2+x+1=(x-1)(x+2)+3</annotation></semantics></math></span>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>+</mo><mfrac><mn>3</mn><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f=x+2+\\frac{3}{x-1}</annotation></semantics></math></span>. השארית שואפת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span> בשני הצדדים: <strong><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">y=x+2</annotation></semantics></math></span></strong>. הבחירות האחרות מתקבלות מחילוק שגוי (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x+1</annotation></semantics></math></span> מתעלמת מהאיבר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> בשארית, ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x-2</annotation></semantics></math></span> מטעות בסימן של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">-1</annotation></semantics></math></span>).",
      "recapHtml": "חילוק פולינומים נותן את b כפשוט"
     },
     {
      "id": "C06-Q3",
      "step": {
       "type": "numeric",
       "prompt": "האסימפטוטה המשופעת של $f(x)=\\frac{2x^2-x}{x+1}$ היא $y=2x+b$. מהו $b$ ?",
       "answer": -3,
       "tol": 0,
       "explain": "$a=\\lim\\frac{2x-1}{x+1}=2$. אז $f-2x=\\frac{2x^2-x-2x^2-2x}{x+1}=\\frac{-3x}{x+1}\\to-3$. אותו ערך ב-$-\\infty$.",
       "promptHtml": "האסימפטוטה המשופעת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{2x^2-x}{x+1}</annotation></semantics></math></span> היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>b</mi></mrow><annotation encoding=\"application/x-tex\">y=2x+b</annotation></semantics></math></span>. מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi></mrow><annotation encoding=\"application/x-tex\">b</annotation></semantics></math></span> ?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>−</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a=\\lim\\frac{2x-1}{x+1}=2</annotation></semantics></math></span>. אז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>−</mo><mn>2</mn><mi>x</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mi>x</mi><mo>−</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>−</mo><mn>3</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>→</mo><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">f-2x=\\frac{2x^2-x-2x^2-2x}{x+1}=\\frac{-3x}{x+1}\\to-3</annotation></semantics></math></span>. אותו ערך ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span>."
      },
      "recap": "b = lim (f − ax), מאחדים לשבר אחד",
      "recapHtml": "b = lim (f − ax), מאחדים לשבר אחד"
     },
     {
      "id": "C06-Q4",
      "question": "מהי האסימפטוטה המשופעת של $f(x)=xe^{2/x}$ ב-$+\\infty$ ?",
      "options": [
       {
        "id": "a",
        "value": "$y=x+2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">y=x+2</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$y=x+1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x+1</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$y=x$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$y=x+e^2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">y=x+e^2</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "$a=\\lim e^{2/x}=1$. אז $b=\\lim x\\left(e^{2/x}-1\\right)$. עם $u=\\frac2x$ מקבלים $x=\\frac2u$ ולכן $b=2\\lim\\frac{e^u-1}{u}=2$. התשובה **$y=x+2$**. ‏$y=x+1$ שוכחת את הגורם 2. ‏$y=x$ מניחה $b=0$. ‏$y=x+e^2$ מציבה את $x=1$ במקום לשאוף לאינסוף.",
      "recap": "x(e^{c/x} − 1) → c",
      "questionHtml": "מהי האסימפטוטה המשופעת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mn>2</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{2/x}</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span> ?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><msup><mi>e</mi><mrow><mn>2</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=\\lim e^{2/x}=1</annotation></semantics></math></span>. אז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><mi>x</mi><mrow><mo fence=\"true\">(</mo><msup><mi>e</mi><mrow><mn>2</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup><mo>−</mo><mn>1</mn><mo fence=\"true\">)</mo></mrow></mrow><annotation encoding=\"application/x-tex\">b=\\lim x\\left(e^{2/x}-1\\right)</annotation></semantics></math></span>. עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>u</mi><mo>=</mo><mfrac><mn>2</mn><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">u=\\frac2x</annotation></semantics></math></span> מקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mfrac><mn>2</mn><mi>u</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">x=\\frac2u</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>2</mn><mi>lim</mi><mo>⁡</mo><mfrac><mrow><msup><mi>e</mi><mi>u</mi></msup><mo>−</mo><mn>1</mn></mrow><mi>u</mi></mfrac><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">b=2\\lim\\frac{e^u-1}{u}=2</annotation></semantics></math></span>. התשובה <strong><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">y=x+2</annotation></semantics></math></span></strong>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x+1</annotation></semantics></math></span> שוכחת את הגורם 2. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span> מניחה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">b=0</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">y=x+e^2</annotation></semantics></math></span> מציבה את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> במקום לשאוף לאינסוף.",
      "recapHtml": "x(e^{c/x} − 1) → c"
     },
     {
      "id": "C06-Q5",
      "question": "מה נכון לגבי אסימפטוטה משופעת של $f(x)=x+e^{x}$ ?",
      "options": [
       {
        "id": "a",
        "value": "$y=x$ בשני הכיוונים",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span> בשני הכיוונים"
       },
       {
        "id": "b",
        "value": "$y=x+1$ ב-$+\\infty$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x+1</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "אין אסימפטוטה משופעת באף כיוון",
        "type": "text",
        "html": "אין אסימפטוטה משופעת באף כיוון"
       },
       {
        "id": "d",
        "value": "$y=x$ ב-$-\\infty$ בלבד",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span> בלבד"
       }
      ],
      "correctId": "d",
      "explanation": "ב-$-\\infty$: $e^{x}\\to0$ ולכן $f-x\\to0$ ו-$y=x$ משופעת. ב-$+\\infty$: $\\frac{f}{x}=1+\\frac{e^x}{x}\\to\\infty$, ולכן אין אסימפטוטה שם. לכן **ב-$-\\infty$ בלבד**. ‏$y=x$ בשני הכיוונים מתעלמת מהצד הימני, ו-$y=x+1$ אינה מתקבלת כי $b=\\lim e^x$ אינו קיים ב-$+\\infty$. ויש אסימפטוטה בצד שמאל.",
      "recap": "בודקים כל צד בנפרד: a יכול להיות אינסוף בצד אחד",
      "questionHtml": "מה נכון לגבי אסימפטוטה משופעת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=x+e^{x}</annotation></semantics></math></span> ?",
      "explanationHtml": "ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">e^{x}\\to0</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>−</mo><mi>x</mi><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f-x\\to0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span> משופעת. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mi>f</mi><mi>x</mi></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><msup><mi>e</mi><mi>x</mi></msup><mi>x</mi></mfrac><mo>→</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\frac{f}{x}=1+\\frac{e^x}{x}\\to\\infty</annotation></semantics></math></span>, ולכן אין אסימפטוטה שם. לכן <strong>ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span> בלבד</strong>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span> בשני הכיוונים מתעלמת מהצד הימני, ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x+1</annotation></semantics></math></span> אינה מתקבלת כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><msup><mi>e</mi><mi>x</mi></msup></mrow><annotation encoding=\"application/x-tex\">b=\\lim e^x</annotation></semantics></math></span> אינו קיים ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span>. ויש אסימפטוטה בצד שמאל.",
      "recapHtml": "בודקים כל צד בנפרד: a יכול להיות אינסוף בצד אחד"
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
       "explain": "$x\\left(e^{3/x}-1\\right)=\\frac3u\\left(e^u-1\\right)=3\\cdot\\frac{e^u-1}{u}$. בשורה 2 נשמט הגורם $3$, ולכן שורה 3 (שמכפילה ב-3) לא עוקבת.",
       "promptHtml": "בחישוב האסימפטוטה המשופעת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mn>3</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{3/x}</annotation></semantics></math></span> נפלה טעות בשורה אחת. איזו ?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mrow><mo fence=\"true\">(</mo><msup><mi>e</mi><mrow><mn>3</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup><mo>−</mo><mn>1</mn><mo fence=\"true\">)</mo></mrow><mo>=</mo><mfrac><mn>3</mn><mi>u</mi></mfrac><mrow><mo fence=\"true\">(</mo><msup><mi>e</mi><mi>u</mi></msup><mo>−</mo><mn>1</mn><mo fence=\"true\">)</mo></mrow><mo>=</mo><mn>3</mn><mo>⋅</mo><mfrac><mrow><msup><mi>e</mi><mi>u</mi></msup><mo>−</mo><mn>1</mn></mrow><mi>u</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">x\\left(e^{3/x}-1\\right)=\\frac3u\\left(e^u-1\\right)=3\\cdot\\frac{e^u-1}{u}</annotation></semantics></math></span>. בשורה 2 נשמט הגורם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span>, ולכן שורה 3 (שמכפילה ב-3) לא עוקבת.",
       "linesHtml": [
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><mfrac><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo></mrow><mi>x</mi></mfrac><mo>=</mo><mi>lim</mi><mo>⁡</mo><msup><mi>e</mi><mrow><mn>3</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a=\\lim\\frac{f(x)}{x}=\\lim e^{3/x}=1</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><mrow><mo fence=\"true\">(</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>−</mo><mi>x</mi><mo fence=\"true\">)</mo></mrow><mo>=</mo><mi>lim</mi><mo>⁡</mo><mi>x</mi><mrow><mo fence=\"true\">(</mo><msup><mi>e</mi><mrow><mn>3</mn><mi mathvariant=\"normal\">/</mi><mi>x</mi></mrow></msup><mo>−</mo><mn>1</mn><mo fence=\"true\">)</mo></mrow></mrow><annotation encoding=\"application/x-tex\">b=\\lim\\left(f(x)-x\\right)=\\lim x\\left(e^{3/x}-1\\right)</annotation></semantics></math></span>",
        "מציבים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>u</mi><mo>=</mo><mfrac><mn>3</mn><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">u=\\frac3x</annotation></semantics></math></span>, ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mfrac><mn>3</mn><mi>u</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">x=\\frac3u</annotation></semantics></math></span> ומקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mrow><mi>lim</mi><mo>⁡</mo></mrow><mrow><mi>u</mi><mo>→</mo><mn>0</mn></mrow></msub><mfrac><mrow><msup><mi>e</mi><mi>u</mi></msup><mo>−</mo><mn>1</mn></mrow><mi>u</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">\\lim_{u\\to0}\\frac{e^u-1}{u}</annotation></semantics></math></span>",
        "הגבול ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mrow><mi>lim</mi><mo>⁡</mo></mrow><mrow><mi>u</mi><mo>→</mo><mn>0</mn></mrow></msub><mfrac><mrow><msup><mi>e</mi><mi>u</mi></msup><mo>−</mo><mn>1</mn></mrow><mi>u</mi></mfrac><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">\\lim_{u\\to0}\\frac{e^u-1}{u}=1</annotation></semantics></math></span>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi><mo>=</mo><mn>3</mn><mo>⋅</mo><mn>1</mn><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">b=3\\cdot1=3</annotation></semantics></math></span>",
        "האסימפטוטה המשופעת היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">y=x+3</annotation></semantics></math></span>"
       ]
      },
      "recap": "x = c/u: הגורם c יוצא החוצה",
      "recapHtml": "x = c/u: הגורם c יוצא החוצה"
     }
    ]
   },
   {
    "id": "C07",
    "order": 7,
    "icon": "🔍",
    "title": "חקירה מלאה: פונקציה עם אקספוננט",
    "goal": "להריץ את כל רשימת החקירה על פונקציה עם אקספוננט, כולל סימטריה, שלוש נקודות פיתול ואסימפטוטה אופקית.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>עכשיו מחברים את כל הצעדים. רשימת הבדיקה, בסדר הזה:</p>\n<ul>\n<li>תחום הגדרה, חיתוכים, וסימטריה.</li>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;</annotation></semantics></math></span>: עלייה, ירידה וקיצון.</li>\n<li><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;</annotation></semantics></math></span>: קמירות ופיתול.</li>\n<li>אסימפטוטות: אנכית, אופקית, משופעת.</li>\n</ul>\n<h3>סימטריה</h3>\n<p><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> <b>זוגית</b> אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f(-x)=f(x)</annotation></semantics></math></span> (הגרף סימטרי סביב ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span>). <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> <b>אי-זוגית</b> אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f(-x)=-f(x)</annotation></semantics></math></span> (הגרף סימטרי סביב הראשית). כך חוקרים רק את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x\\ge0</annotation></semantics></math></span> ומשלימים את הצד השני.</p>\n<div class=\"lesson-ex\">דוגמה מלאה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mi>x</mi></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=(x-1)e^{x}</annotation></semantics></math></span>.<br>\n<b>תחום וחיתוכים:</b> כל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi mathvariant=\"double-struck\">R</mi></mrow><annotation encoding=\"application/x-tex\">\\mathbb{R}</annotation></semantics></math></span>. ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">f(0)=-1</annotation></semantics></math></span>. ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">e^x&gt;0</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span>. הנקודות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,-1)</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,0)</annotation></semantics></math></span>.<br>\n<b>נגזרת:</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;=e^{x}+(x-1)e^{x}=xe^{x}</annotation></semantics></math></span>. שלילית ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;0</annotation></semantics></math></span>, חיובית ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;0</annotation></semantics></math></span>. מינימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,-1)</annotation></semantics></math></span>.<br>\n<b>נגזרת שנייה:</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mi>x</mi></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=(x+1)e^{x}</annotation></semantics></math></span>. שלילית ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;-1</annotation></semantics></math></span> (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∩</mo></mrow><annotation encoding=\"application/x-tex\">\\cap</annotation></semantics></math></span>), חיובית ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;-1</annotation></semantics></math></span> (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∪</mo></mrow><annotation encoding=\"application/x-tex\">\\cup</annotation></semantics></math></span>). פיתול ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=-1</annotation></semantics></math></span> עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mfrac><mn>2</mn><mi>e</mi></mfrac><mo>≈</mo><mo>−</mo><mn>0.736</mn></mrow><annotation encoding=\"application/x-tex\">f(-1)=-\\frac2e\\approx-0.736</annotation></semantics></math></span>.<br>\n<b>אסימפטוטות:</b> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><msup><mi>e</mi><mi>x</mi></msup><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">(x-1)e^{x}\\to0</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span> אופקית. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>→</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">f\\to\\infty</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mi>f</mi><mi>x</mi></mfrac><mo>→</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\frac fx\\to\\infty</annotation></semantics></math></span>, לכן אין משופעת. אין אנכית.</div>\n<div class=\"lesson-rule\">🔑 גבול של מכפלה כמו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup></mrow><annotation encoding=\"application/x-tex\">xe^{-x^2/2}</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\infty</annotation></semantics></math></span>: הכותבים מנה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mi>x</mi><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{x}{e^{x^2/2}}</annotation></semantics></math></span> ובלופיטל מקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>1</mn><mrow><mi>x</mi><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup></mrow></mfrac><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">\\frac{1}{xe^{x^2/2}}\\to0</annotation></semantics></math></span>. האקספוננט מנצח את החזקה.</div>\n"
    },
    "questions": [
     {
      "id": "C07-Q1",
      "question": "מה נכון לגבי $f(x)=xe^{-x^2/2}$ ?",
      "options": [
       {
        "id": "a",
        "value": "$f$ זוגית, ונקודת החיתוך היחידה עם הצירים היא $(0,0)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> זוגית, ונקודת החיתוך היחידה עם הצירים היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,0)</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$f$ אי-זוגית, ונקודת החיתוך היחידה עם הצירים היא $(0,0)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> אי-זוגית, ונקודת החיתוך היחידה עם הצירים היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,0)</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$f$ אי-זוגית, ואין לה חיתוך עם הצירים",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> אי-זוגית, ואין לה חיתוך עם הצירים"
       },
       {
        "id": "d",
        "value": "$f$ אינה זוגית ואינה אי-זוגית",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> אינה זוגית ואינה אי-זוגית"
       }
      ],
      "correctId": "b",
      "explanation": "‏$f(-x)=-x\\,e^{-x^2/2}=-f(x)$, כלומר **אי-זוגית**. ‏$f=0$ רק כאשר $x=0$ כי האקספוננט חיובי, ו-$f(0)=0$. ‏$f$ זוגית שגויה כי הסימן מתהפך. הטענה שאין חיתוך שגויה כי $(0,0)$ על הגרף.",
      "recap": "f(−x) = −f(x): אי-זוגית",
      "questionHtml": "מה נכון לגבי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{-x^2/2}</annotation></semantics></math></span> ?",
      "explanationHtml": "‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mo>−</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mi>x</mi><mtext> </mtext><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup><mo>=</mo><mo>−</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f(-x)=-x\\,e^{-x^2/2}=-f(x)</annotation></semantics></math></span>, כלומר <strong>אי-זוגית</strong>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f=0</annotation></semantics></math></span> רק כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> כי האקספוננט חיובי, ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f(0)=0</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> זוגית שגויה כי הסימן מתהפך. הטענה שאין חיתוך שגויה כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,0)</annotation></semantics></math></span> על הגרף.",
      "recapHtml": "f(−x) = −f(x): אי-זוגית"
     },
     {
      "id": "C07-Q2",
      "question": "באילו קטעים $f(x)=xe^{-x^2/2}$ עולה ? (נתון: $f'(x)=\\left(1-x^2\\right)e^{-x^2/2}$)",
      "options": [
       {
        "id": "a",
        "value": "$x<-1$ וגם $x>1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;-1</annotation></semantics></math></span> וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$x>0$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;0</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$-1<x<1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>1</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">-1&lt;x&lt;1</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$x<0$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;0</annotation></semantics></math></span>"
       }
      ],
      "correctId": "c",
      "explanation": "האקספוננט חיובי, והסימן הוא של $1-x^2$: חיובי ב-$(-1,1)$ ושלילי מחוץ לו. לכן **עולה ב-$(-1,1)$**, ויורדת ב-$x<-1$ וב-$x>1$. הבחירה של $x<-1$ ו-$x>1$ היא קטעי הירידה. ‏$x>0$ כוללת את $x>1$ שבו הפונקציה יורדת, ו-$x<0$ כוללת את $x<-1$ שבו הפונקציה יורדת.",
      "recap": "הסימן של 1 − x² מחוץ ל-(−1,1) שלילי",
      "questionHtml": "באילו קטעים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{-x^2/2}</annotation></semantics></math></span> עולה ? (נתון: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mrow><mo fence=\"true\">(</mo><mn>1</mn><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mo fence=\"true\">)</mo></mrow><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;(x)=\\left(1-x^2\\right)e^{-x^2/2}</annotation></semantics></math></span>)",
      "explanationHtml": "האקספוננט חיובי, והסימן הוא של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><annotation encoding=\"application/x-tex\">1-x^2</annotation></semantics></math></span>: חיובי ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,1)</annotation></semantics></math></span> ושלילי מחוץ לו. לכן <strong>עולה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(-1,1)</annotation></semantics></math></span></strong>, ויורדת ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;-1</annotation></semantics></math></span> וב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span>. הבחירה של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;-1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span> היא קטעי הירידה. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;0</annotation></semantics></math></span> כוללת את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span> שבו הפונקציה יורדת, ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;0</annotation></semantics></math></span> כוללת את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;-1</annotation></semantics></math></span> שבו הפונקציה יורדת.",
      "recapHtml": "הסימן של 1 − x² מחוץ ל-(−1,1) שלילי"
     },
     {
      "id": "C07-Q3",
      "step": {
       "type": "numeric",
       "prompt": "מהו ערך ה-$y$ של המקסימום המקומי של $f(x)=xe^{-x^2/2}$ ? (עשרוני, ‏3 ספרות אחרי הנקודה)",
       "answer": 0.607,
       "tol": 0.001,
       "explain": "המקסימום ב-$x=1$ (שם $f'$ עוברת מ-$+$ ל-$-$): $f(1)=e^{-1/2}\\approx0.607$. ‏$f(-1)=-0.607$ הוא המינימום.",
       "promptHtml": "מהו ערך ה-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> של המקסימום המקומי של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{-x^2/2}</annotation></semantics></math></span> ? (עשרוני, ‏3 ספרות אחרי הנקודה)",
       "explainHtml": "המקסימום ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> (שם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;</annotation></semantics></math></span> עוברת מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">+</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo></mrow><annotation encoding=\"application/x-tex\">-</annotation></semantics></math></span>): <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>−</mo><mn>1</mn><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup><mo>≈</mo><mn>0.607</mn></mrow><annotation encoding=\"application/x-tex\">f(1)=e^{-1/2}\\approx0.607</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>0.607</mn></mrow><annotation encoding=\"application/x-tex\">f(-1)=-0.607</annotation></semantics></math></span> הוא המינימום."
      },
      "recap": "ערך הקיצון: מציבים בפונקציה",
      "recapHtml": "ערך הקיצון: מציבים בפונקציה"
     },
     {
      "id": "C07-Q4",
      "question": "כמה נקודות פיתול יש ל-$f(x)=xe^{-x^2/2}$ ? (נתון: $f''(x)=\\left(x^3-3x\\right)e^{-x^2/2}$)",
      "options": [
       {
        "id": "a",
        "value": "שלוש: $x=0$ ו-$x=\\pm\\sqrt3$",
        "type": "text",
        "html": "שלוש: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>±</mo><msqrt><mn>3</mn></msqrt></mrow><annotation encoding=\"application/x-tex\">x=\\pm\\sqrt3</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "אחת: $x=0$ בלבד",
        "type": "text",
        "html": "אחת: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "c",
        "value": "שתיים: $x=\\pm1$",
        "type": "text",
        "html": "שתיים: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=\\pm1</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "אין נקודות פיתול",
        "type": "text",
        "html": "אין נקודות פיתול"
       }
      ],
      "correctId": "a",
      "explanation": "$x^3-3x=x\\left(x^2-3\\right)=x(x-\\sqrt3)(x+\\sqrt3)$, והאקספוננט חיובי. שלושה שורשים פשוטים, ובכל אחד $f''$ משנה סימן: $-,+,-,+$. לכן **שלוש**. ‏$x=\\pm1$ הם הקיצונים (שם $f'=0$) ולא אפסי $f''$: $f''(1)=-2e^{-1/2}\\neq0$.",
      "recap": "פיתול בכל שורש פשוט של f''",
      "questionHtml": "כמה נקודות פיתול יש ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{-x^2/2}</annotation></semantics></math></span> ? (נתון: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mrow><mo fence=\"true\">(</mo><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><mi>x</mi><mo fence=\"true\">)</mo></mrow><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(x)=\\left(x^3-3x\\right)e^{-x^2/2}</annotation></semantics></math></span>)",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>−</mo><mn>3</mn><mi>x</mi><mo>=</mo><mi>x</mi><mrow><mo fence=\"true\">(</mo><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>3</mn><mo fence=\"true\">)</mo></mrow><mo>=</mo><mi>x</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><msqrt><mn>3</mn></msqrt><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>+</mo><msqrt><mn>3</mn></msqrt><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">x^3-3x=x\\left(x^2-3\\right)=x(x-\\sqrt3)(x+\\sqrt3)</annotation></semantics></math></span>, והאקספוננט חיובי. שלושה שורשים פשוטים, ובכל אחד <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;</annotation></semantics></math></span> משנה סימן: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mo separator=\"true\">,</mo><mo>+</mo><mo separator=\"true\">,</mo><mo>−</mo><mo separator=\"true\">,</mo><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">-,+,-,+</annotation></semantics></math></span>. לכן <strong>שלוש</strong>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=\\pm1</annotation></semantics></math></span> הם הקיצונים (שם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;=0</annotation></semantics></math></span>) ולא אפסי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;</annotation></semantics></math></span>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>−</mo><mn>1</mn><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup><mo mathvariant=\"normal\">≠</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;(1)=-2e^{-1/2}\\neq0</annotation></semantics></math></span>.",
      "recapHtml": "פיתול בכל שורש פשוט של f''"
     },
     {
      "id": "C07-Q5",
      "question": "מהן האסימפטוטות של $f(x)=xe^{-x^2/2}$ ?",
      "options": [
       {
        "id": "a",
        "value": "אופקית $y=0$ ב-$+\\infty$ בלבד",
        "type": "text",
        "html": "אופקית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "b",
        "value": "אנכית $x=0$ ואופקית $y=0$",
        "type": "text",
        "html": "אנכית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> ואופקית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "משופעת $y=x$",
        "type": "text",
        "html": "משופעת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "אופקית $y=0$ בשני הכיוונים, בלי אנכית ובלי משופעת",
        "type": "text",
        "html": "אופקית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span> בשני הכיוונים, בלי אנכית ובלי משופעת"
       }
      ],
      "correctId": "d",
      "explanation": "הפונקציה מוגדרת בכל $\\mathbb{R}$, ולכן אין אנכית. ב-$+\\infty$ ו-$-\\infty$ האקספוננט $e^{-x^2/2}$ מנצח את $x$ ולכן $f\\to0$ (גם בצד השמאלי, בגלל אי-הזוגיות). לכן **$y=0$ בשני הכיוונים**. הטענה על $+\\infty$ בלבד מחמיצה את $-\\infty$. ‏$y=x$ אינה אסימפטוטה כי $f-x\\to-\\infty$.",
      "recap": "אקספוננט ריבועי שלילי מנצח כל חזקה בשני הכיוונים",
      "questionHtml": "מהן האסימפטוטות של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f(x)=xe^{-x^2/2}</annotation></semantics></math></span> ?",
      "explanationHtml": "הפונקציה מוגדרת בכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi mathvariant=\"double-struck\">R</mi></mrow><annotation encoding=\"application/x-tex\">\\mathbb{R}</annotation></semantics></math></span>, ולכן אין אנכית. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span> האקספוננט <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant=\"normal\">/</mi><mn>2</mn></mrow></msup></mrow><annotation encoding=\"application/x-tex\">e^{-x^2/2}</annotation></semantics></math></span> מנצח את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f\\to0</annotation></semantics></math></span> (גם בצד השמאלי, בגלל אי-הזוגיות). לכן <strong><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">y=0</annotation></semantics></math></span> בשני הכיוונים</strong>. הטענה על <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span> בלבד מחמיצה את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">-\\infty</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span> אינה אסימפטוטה כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>−</mo><mi>x</mi><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">f-x\\to-\\infty</annotation></semantics></math></span>.",
      "recapHtml": "אקספוננט ריבועי שלילי מנצח כל חזקה בשני הכיוונים"
     }
    ]
   },
   {
    "id": "C08",
    "order": 8,
    "icon": "🧩",
    "title": "חקירה מלאה: פונקציה רציונלית",
    "goal": "לחלק פולינומים ולהריץ את כל רשימת החקירה על פונקציה רציונלית עם אסימפטוטה אנכית ומשופעת.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n<p>בפונקציה רציונלית שדרגת המונה גדולה ב-1 מדרגת המכנה יש כמעט תמיד אסימפטוטה אנכית ומשופעת. הצעד הכי חשוב: <b>לחלק פולינומים לפני שגוזרים</b>. אחרי החילוק מתקבל ישר ועוד שבר שמכנהו הוא המכנה המקורי. הישר הוא האסימפטוטה המשופעת, והנגזרות פשוטות.</p>\n<div class=\"lesson-ex\">דוגמה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac{x^2}{x-1}=x+1+\\frac{1}{x-1}</annotation></semantics></math></span>.<br>\n<b>תחום:</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq1</annotation></semantics></math></span>. חיתוך: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,0)</annotation></semantics></math></span>.<br>\n<b>נגזרת:</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><mn>1</mn><mo>−</mo><mfrac><mn>1</mn><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><msup><mo stretchy=\"false\">)</mo><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><msup><mo stretchy=\"false\">)</mo><mn>2</mn></msup></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f&#x27;=1-\\frac{1}{(x-1)^2}=\\frac{x(x-2)}{(x-1)^2}</annotation></semantics></math></span>. חיובית ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;0</annotation></semantics></math></span> ול-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;2</annotation></semantics></math></span>, שלילית ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,1)</annotation></semantics></math></span> וב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span>. מקסימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,0)</annotation></semantics></math></span> ומינימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>4</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(2,4)</annotation></semantics></math></span>.<br>\n<b>נגזרת שנייה:</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mfrac><mn>2</mn><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><msup><mo stretchy=\"false\">)</mo><mn>3</mn></msup></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;=\\frac{2}{(x-1)^3}</annotation></semantics></math></span>. אינה מתאפסת, ומשנה סימן רק ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> שמחוץ לתחום: אין פיתול. כלפי מטה (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∩</mo></mrow><annotation encoding=\"application/x-tex\">\\cap</annotation></semantics></math></span>) ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;1</annotation></semantics></math></span> וכלפי מעלה (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∪</mo></mrow><annotation encoding=\"application/x-tex\">\\cup</annotation></semantics></math></span>) ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;1</annotation></semantics></math></span>.<br>\n<b>אסימפטוטות:</b> אנכית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">f\\to-\\infty</annotation></semantics></math></span> משמאל, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">+\\infty</annotation></semantics></math></span> מימין), משופעת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x+1</annotation></semantics></math></span> בשני הצדדים.</div>\n<div class=\"lesson-trap\">⚠️ בפונקציה רציונלית החלפת הסימן של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;</annotation></semantics></math></span> ליד אסימפטוטה אנכית היא עניין רגיל. היא לא נקודת פיתול כי הנקודה לא בתחום.</div>\n<div class=\"lesson-trap\">⚠️ מקסימום מקומי יכול להיות נמוך ממינימום מקומי, כמו בדוגמה: המקסימום המקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,0)</annotation></semantics></math></span> נמוך מהמינימום המקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>4</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(2,4)</annotation></semantics></math></span>. זה תקין כשיש אסימפטוטה אנכית באמצע.</div>\n"
    },
    "questions": [
     {
      "id": "C08-Q1",
      "question": "מהם תחום ההגדרה והחיתוכים של $g(x)=\\frac{x^2-2x+2}{x-1}$ ?",
      "options": [
       {
        "id": "a",
        "value": "$x\\neq1$. חיתוך עם ציר $y$ ב-$(0,2)$, ובלי חיתוך עם ציר $x$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq1</annotation></semantics></math></span>. חיתוך עם ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,2)</annotation></semantics></math></span>, ובלי חיתוך עם ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$x\\neq1$. חיתוך עם ציר $y$ ב-$(0,-2)$, ובלי חיתוך עם ציר $x$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq1</annotation></semantics></math></span>. חיתוך עם ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,-2)</annotation></semantics></math></span>, ובלי חיתוך עם ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$x\\neq1$. חיתוך עם ציר $y$ ב-$(0,-2)$, ועם ציר $x$ ב-$(1,0)$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq1</annotation></semantics></math></span>. חיתוך עם ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,-2)</annotation></semantics></math></span>, ועם ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,0)</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$x\\neq\\pm1$. חיתוך עם ציר $y$ ב-$(0,-2)$, ובלי חיתוך עם ציר $x$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mo>±</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq\\pm1</annotation></semantics></math></span>. חיתוך עם ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,-2)</annotation></semantics></math></span>, ובלי חיתוך עם ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span>"
       }
      ],
      "correctId": "b",
      "explanation": "המכנה מתאפס רק ב-$x=1$. ‏$g(0)=\\frac{2}{-1}=-2$. המונה $x^2-2x+2=(x-1)^2+1\\ge1$ אף פעם לא מתאפס, ולכן אין חיתוך עם ציר $x$. ‏$(0,2)$ היא טעות בסימן. ‏$(1,0)$ מחוץ לתחום. ‏$x\\neq-1$ אינו תנאי: $g(-1)=\\frac{5}{-2}$ מוגדרת.",
      "recap": "מונה חיובי תמיד ← אין חיתוך עם ציר x",
      "questionHtml": "מהם תחום ההגדרה והחיתוכים של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">g(x)=\\frac{x^2-2x+2}{x-1}</annotation></semantics></math></span> ?",
      "explanationHtml": "המכנה מתאפס רק ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mn>2</mn><mrow><mo>−</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">g(0)=\\frac{2}{-1}=-2</annotation></semantics></math></span>. המונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><msup><mo stretchy=\"false\">)</mo><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>≥</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x^2-2x+2=(x-1)^2+1\\ge1</annotation></semantics></math></span> אף פעם לא מתאפס, ולכן אין חיתוך עם ציר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">x</annotation></semantics></math></span>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,2)</annotation></semantics></math></span> היא טעות בסימן. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,0)</annotation></semantics></math></span> מחוץ לתחום. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo mathvariant=\"normal\">≠</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x\\neq-1</annotation></semantics></math></span> אינו תנאי: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mn>5</mn><mrow><mo>−</mo><mn>2</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">g(-1)=\\frac{5}{-2}</annotation></semantics></math></span> מוגדרת.",
      "recapHtml": "מונה חיובי תמיד ← אין חיתוך עם ציר x"
     },
     {
      "id": "C08-Q2",
      "step": {
       "type": "fillblank",
       "prompt": "משלימים את החילוק של $g(x)=\\frac{x^2-2x+2}{x-1}$ בפולינום.",
       "lines": [
        "$(x-1)(x-1)=x^2-2x+1$",
        "$\\frac{x^2-2x+2}{x-1}=(x-1)+\\frac{r}{x-1}$ כאשר השארית היא $r=$ ___"
       ],
       "blankIndex": 1,
       "options": [
        {
         "id": "a",
         "value": "0",
         "type": "text",
         "html": "0"
        },
        {
         "id": "b",
         "value": "1",
         "type": "text",
         "html": "1"
        },
        {
         "id": "c",
         "value": "2",
         "type": "text",
         "html": "2"
        },
        {
         "id": "d",
         "value": "-1",
         "type": "text",
         "html": "-1"
        }
       ],
       "correctId": "b",
       "explain": "$(x-1)(x-1)=x^2-2x+1$, והשארית היא $\\left(x^2-2x+2\\right)-\\left(x^2-2x+1\\right)=1$. כלומר $g=x-1+\\frac{1}{x-1}$.",
       "promptHtml": "משלימים את החילוק של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">g(x)=\\frac{x^2-2x+2}{x-1}</annotation></semantics></math></span> בפולינום.",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">(x-1)(x-1)=x^2-2x+1</annotation></semantics></math></span>, והשארית היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mrow><mo fence=\"true\">(</mo><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo fence=\"true\">)</mo></mrow><mo>−</mo><mrow><mo fence=\"true\">(</mo><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo fence=\"true\">)</mo></mrow><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">\\left(x^2-2x+2\\right)-\\left(x^2-2x+1\\right)=1</annotation></semantics></math></span>. כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo>=</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">g=x-1+\\frac{1}{x-1}</annotation></semantics></math></span>.",
       "linesHtml": [
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">(x-1)(x-1)=x^2-2x+1</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>+</mo><mfrac><mi>r</mi><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{x^2-2x+2}{x-1}=(x-1)+\\frac{r}{x-1}</annotation></semantics></math></span> כאשר השארית היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo>=</mo></mrow><annotation encoding=\"application/x-tex\">r=</annotation></semantics></math></span> ___"
       ]
      },
      "recap": "מחלקים פולינומים לפני הגזירה",
      "recapHtml": "מחלקים פולינומים לפני הגזירה"
     },
     {
      "id": "C08-Q3",
      "question": "מה הקיצונים המקומיים של $g(x)=x-1+\\frac{1}{x-1}$ ? (נתון: $g'(x)=\\frac{x(x-2)}{(x-1)^2}$)",
      "options": [
       {
        "id": "a",
        "value": "מינימום מקומי $(0,-2)$ ומקסימום מקומי $(2,2)$",
        "type": "text",
        "html": "מינימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,-2)</annotation></semantics></math></span> ומקסימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(2,2)</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "מקסימום מקומי בנקודה $x=1$",
        "type": "text",
        "html": "מקסימום מקומי בנקודה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "מקסימום מקומי $(0,-2)$ ומינימום מקומי $(2,2)$",
        "type": "text",
        "html": "מקסימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,-2)</annotation></semantics></math></span> ומינימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(2,2)</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "מינימום מקומי $(2,2)$ בלבד",
        "type": "text",
        "html": "מינימום מקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(2,2)</annotation></semantics></math></span> בלבד"
       }
      ],
      "correctId": "c",
      "explanation": "הסימן של $g'$ הוא של $x(x-2)$: ‏$+$ ל-$x<0$, ‏$-$ ב-$(0,1)$ וב-$(1,2)$, ‏$+$ ל-$x>2$. ב-$x=0$ מ-$+$ ל-$-$: מקסימום $g(0)=-2$. ב-$x=2$ מ-$-$ ל-$+$: מינימום $g(2)=2$. ב-$x=1$ הפונקציה לא מוגדרת ולכן אין שם קיצון. הסדר ההפוך (מינימום ב-$0$) מתקבל מקריאה הפוכה של הסימנים, והטענה על $x=1$ מתעלמת מכך שהפונקציה לא מוגדרת שם. ‏$(2,2)$ בלבד מחמיצה את המקסימום ב-$x=0$.",
      "recap": "הסימן לא מתחלף ב-1 (גורם ריבועי), אבל 1 מפרידה קטעים",
      "questionHtml": "מה הקיצונים המקומיים של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">g(x)=x-1+\\frac{1}{x-1}</annotation></semantics></math></span> ? (נתון: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>g</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><mi>x</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><msup><mo stretchy=\"false\">)</mo><mn>2</mn></msup></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">g&#x27;(x)=\\frac{x(x-2)}{(x-1)^2}</annotation></semantics></math></span>)",
      "explanationHtml": "הסימן של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>g</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup></mrow><annotation encoding=\"application/x-tex\">g&#x27;</annotation></semantics></math></span> הוא של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">x(x-2)</annotation></semantics></math></span>: ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">+</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;0</annotation></semantics></math></span>, ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo></mrow><annotation encoding=\"application/x-tex\">-</annotation></semantics></math></span> ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(0,1)</annotation></semantics></math></span> וב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(1,2)</annotation></semantics></math></span>, ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">+</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&gt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x&gt;2</annotation></semantics></math></span>. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">+</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo></mrow><annotation encoding=\"application/x-tex\">-</annotation></semantics></math></span>: מקסימום <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">g(0)=-2</annotation></semantics></math></span>. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=2</annotation></semantics></math></span> מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo></mrow><annotation encoding=\"application/x-tex\">-</annotation></semantics></math></span> ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>+</mo></mrow><annotation encoding=\"application/x-tex\">+</annotation></semantics></math></span>: מינימום <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo stretchy=\"false\">(</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">g(2)=2</annotation></semantics></math></span>. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> הפונקציה לא מוגדרת ולכן אין שם קיצון. הסדר ההפוך (מינימום ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>) מתקבל מקריאה הפוכה של הסימנים, והטענה על <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> מתעלמת מכך שהפונקציה לא מוגדרת שם. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>2</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(2,2)</annotation></semantics></math></span> בלבד מחמיצה את המקסימום ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span>.",
      "recapHtml": "הסימן לא מתחלף ב-1 (גורם ריבועי), אבל 1 מפרידה קטעים"
     },
     {
      "id": "C08-Q4",
      "question": "האם ל-$g(x)$ יש נקודת פיתול ? (נתון: $g''(x)=\\frac{2}{(x-1)^3}$)",
      "options": [
       {
        "id": "a",
        "value": "לא: $g''$ משנה סימן רק ב-$x=1$, שמחוץ לתחום",
        "type": "text",
        "html": "לא: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>g</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">g&#x27;&#x27;</annotation></semantics></math></span> משנה סימן רק ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span>, שמחוץ לתחום"
       },
       {
        "id": "b",
        "value": "כן: ב-$x=1$",
        "type": "text",
        "html": "כן: ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "כן: ב-$x=0$ וב-$x=2$, שם $g'=0$",
        "type": "text",
        "html": "כן: ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">x=0</annotation></semantics></math></span> וב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=2</annotation></semantics></math></span>, שם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>g</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">g&#x27;=0</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "לא: $g''$ חיובית בכל התחום",
        "type": "text",
        "html": "לא: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>g</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">g&#x27;&#x27;</annotation></semantics></math></span> חיובית בכל התחום"
       }
      ],
      "correctId": "a",
      "explanation": "‏$g''=\\frac{2}{(x-1)^3}$ אינה מתאפסת בשום מקום, והסימן שלה משתנה רק ב-$x=1$ שאינו בתחום: **אין פיתול**. ‏$x=0,2$ הם הקיצונים ולא פיתולים ($g''(0)=-2$ ו-$g''(2)=2$ שונות מאפס). ו-$g''$ שלילית ל-$x<1$ ולכן אינה חיובית בכל התחום.",
      "recap": "פיתול דורש החלפת סימן בנקודה בתחום. כאן הנקודה היא האסימפטוטה",
      "questionHtml": "האם ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">g(x)</annotation></semantics></math></span> יש נקודת פיתול ? (נתון: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>g</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mn>2</mn><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><msup><mo stretchy=\"false\">)</mo><mn>3</mn></msup></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">g&#x27;&#x27;(x)=\\frac{2}{(x-1)^3}</annotation></semantics></math></span>)",
      "explanationHtml": "‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>g</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>=</mo><mfrac><mn>2</mn><mrow><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><msup><mo stretchy=\"false\">)</mo><mn>3</mn></msup></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">g&#x27;&#x27;=\\frac{2}{(x-1)^3}</annotation></semantics></math></span> אינה מתאפסת בשום מקום, והסימן שלה משתנה רק ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> שאינו בתחום: <strong>אין פיתול</strong>. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>0</mn><mo separator=\"true\">,</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">x=0,2</annotation></semantics></math></span> הם הקיצונים ולא פיתולים (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>g</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">g&#x27;&#x27;(0)=-2</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>g</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo stretchy=\"false\">(</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">g&#x27;&#x27;(2)=2</annotation></semantics></math></span> שונות מאפס). ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>g</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">g&#x27;&#x27;</annotation></semantics></math></span> שלילית ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x&lt;1</annotation></semantics></math></span> ולכן אינה חיובית בכל התחום.",
      "recapHtml": "פיתול דורש החלפת סימן בנקודה בתחום. כאן הנקודה היא האסימפטוטה"
     },
     {
      "id": "C08-Q5",
      "question": "מהן האסימפטוטות של $g(x)=x-1+\\frac{1}{x-1}$ ?",
      "options": [
       {
        "id": "a",
        "value": "אנכית $x=1$ ומשופעת $y=x$",
        "type": "text",
        "html": "אנכית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> ומשופעת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "אנכית $x=1$ בלבד",
        "type": "text",
        "html": "אנכית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "c",
        "value": "משופעת $y=x-1$ בלבד",
        "type": "text",
        "html": "משופעת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x-1</annotation></semantics></math></span> בלבד"
       },
       {
        "id": "d",
        "value": "אנכית $x=1$ ומשופעת $y=x-1$ בשני הצדדים",
        "type": "text",
        "html": "אנכית <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> ומשופעת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x-1</annotation></semantics></math></span> בשני הצדדים"
       }
      ],
      "correctId": "d",
      "explanation": "כש-$x\\to1^+$ האיבר $\\frac{1}{x-1}\\to+\\infty$ ולכן $g\\to+\\infty$; כש-$x\\to1^-$ הוא $\\to-\\infty$. זו אסימפטוטה אנכית. בנוסף $g-(x-1)=\\frac{1}{x-1}\\to0$ בשני הצדדים, כלומר $y=x-1$ משופעת. ‏$y=x$ שגויה ($g-x\\to-1$). וקיימות שתי האסימפטוטות, ולא אחת בלבד.",
      "recap": "אחרי חילוק: האיבר הפולינומי הוא הישר, והשבר הוא האנכית",
      "questionHtml": "מהן האסימפטוטות של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">g(x)=x-1+\\frac{1}{x-1}</annotation></semantics></math></span> ?",
      "explanationHtml": "כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><msup><mn>1</mn><mo>+</mo></msup></mrow><annotation encoding=\"application/x-tex\">x\\to1^+</annotation></semantics></math></span> האיבר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>1</mn><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac><mo>→</mo><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\frac{1}{x-1}\\to+\\infty</annotation></semantics></math></span> ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo>→</mo><mo>+</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">g\\to+\\infty</annotation></semantics></math></span>; כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>→</mo><msup><mn>1</mn><mo>−</mo></msup></mrow><annotation encoding=\"application/x-tex\">x\\to1^-</annotation></semantics></math></span> הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>→</mo><mo>−</mo><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\to-\\infty</annotation></semantics></math></span>. זו אסימפטוטה אנכית. בנוסף <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo>−</mo><mo stretchy=\"false\">(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac><mo>→</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">g-(x-1)=\\frac{1}{x-1}\\to0</annotation></semantics></math></span> בשני הצדדים, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">y=x-1</annotation></semantics></math></span> משופעת. ‏<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">y=x</annotation></semantics></math></span> שגויה (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo>−</mo><mi>x</mi><mo>→</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">g-x\\to-1</annotation></semantics></math></span>). וקיימות שתי האסימפטוטות, ולא אחת בלבד.",
      "recapHtml": "אחרי חילוק: האיבר הפולינומי הוא הישר, והשבר הוא האנכית"
     },
     {
      "id": "C08-Q6",
      "step": {
       "type": "numeric",
       "prompt": "מהו ההפרש בין ערך ה-$y$ של המינימום המקומי לערך ה-$y$ של המקסימום המקומי של $g(x)=\\frac{x^2-2x+2}{x-1}$ ?",
       "answer": 4,
       "tol": 0,
       "explain": "המינימום המקומי $g(2)=2$ והמקסימום המקומי $g(0)=-2$. ההפרש $2-(-2)=4$, חיובי: המינימום המקומי גבוה מהמקסימום המקומי, כי האסימפטוטה האנכית ב-$x=1$ מפרידה את הענפים.",
       "promptHtml": "מהו ההפרש בין ערך ה-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> של המינימום המקומי לערך ה-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span> של המקסימום המקומי של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">g(x)=\\frac{x^2-2x+2}{x-1}</annotation></semantics></math></span> ?",
       "explainHtml": "המינימום המקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo stretchy=\"false\">(</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">g(2)=2</annotation></semantics></math></span> והמקסימום המקומי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>g</mi><mo stretchy=\"false\">(</mo><mn>0</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">g(0)=-2</annotation></semantics></math></span>. ההפרש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>−</mo><mo stretchy=\"false\">(</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">2-(-2)=4</annotation></semantics></math></span>, חיובי: המינימום המקומי גבוה מהמקסימום המקומי, כי האסימפטוטה האנכית ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">x=1</annotation></semantics></math></span> מפרידה את הענפים."
      },
      "recap": "מקסימום מקומי יכול להיות נמוך ממינימום מקומי",
      "recapHtml": "מקסימום מקומי יכול להיות נמוך ממינימום מקומי"
     }
    ]
   },
   {
    "id": "C09",
    "order": 9,
    "icon": "🏆",
    "title": "מבחן מסכם: חקירות מהמבחנים",
    "goal": "לפתור ארבע חקירות מלאות מהמבחנים, ברצף, בלי להחמיץ סעיף.",
    "source": "ai-verified",
    "boss": true,
    "lesson": {
     "html": "\n<p>זו ההרצה המלאה: ארבע חקירות מלאות ממבחנים אמיתיים. לפני שמתחילים, הרשימה:</p>\n<ul>\n<li><b>תחום וחיתוכים:</b> מכנה, שורש, ln. אקספוננט לא מתאפס.</li>\n<li><b><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mo mathvariant=\"normal\" lspace=\"0em\" rspace=\"0em\">′</mo></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;</annotation></semantics></math></span>:</b> מפרקים לגורמים, טבלת סימנים. קיצון = החלפת סימן + ערך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>y</mi></mrow><annotation encoding=\"application/x-tex\">y</annotation></semantics></math></span>.</li>\n<li><b><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;</annotation></semantics></math></span>:</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">&gt;0</annotation></semantics></math></span> כלפי מעלה (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∪</mo></mrow><annotation encoding=\"application/x-tex\">\\cup</annotation></semantics></math></span>), <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">&lt;0</annotation></semantics></math></span> כלפי מטה (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∩</mo></mrow><annotation encoding=\"application/x-tex\">\\cap</annotation></semantics></math></span>). פיתול = החלפת סימן בנקודה בתחום.</li>\n<li><b>אסימפטוטות:</b> אנכית (גבול חד-צדדי אינסופי), אופקית ומשופעת (כל צד בנפרד: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>a</mi></mrow><annotation encoding=\"application/x-tex\">a</annotation></semantics></math></span> ואז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>b</mi></mrow><annotation encoding=\"application/x-tex\">b</annotation></semantics></math></span>).</li>\n</ul>\n<div class=\"lesson-rule\">🔑 בכל שאלה: ראשית חשבו נגזרת, וודאו אותה על נקודה אחת, ורק אז טבלת סימנים. הרוב המכריע של הטעויות הוא בנגזרת או בסימן.</div>\n<div class=\"lesson-trap\">⚠️ בפתרונות מבחנים השמות \"קמורה\" ו\"קעורה\" מתחלפים בין שאלה לשאלה. ענו לפי הכיוון: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∪</mo></mrow><annotation encoding=\"application/x-tex\">\\cup</annotation></semantics></math></span> כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;&gt;0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>∩</mo></mrow><annotation encoding=\"application/x-tex\">\\cap</annotation></semantics></math></span> כאשר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>f</mi><mrow><mo mathvariant=\"normal\">′</mo><mo mathvariant=\"normal\">′</mo></mrow></msup><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">f&#x27;&#x27;&lt;0</annotation></semantics></math></span>.</div>\n<div class=\"lesson-trap\">⚠️ מכנה שמתאפס אינו אסימפטוטה אוטומטית. חשבו גבול חד-צדדי בכל נקודה כזו.</div>\n"
    },
    "questions": [
     {
      "bankId": "24B-A-Q1",
      "recap": "לחלק פולינומים לפני הגזירה: x − 1/x². אין פיתול כי f'' שלילית משני צדי 0, והנקודה 0 מחוץ לתחום",
      "recapHtml": "לחלק פולינומים לפני הגזירה: x − 1/x². אין פיתול כי f'' שלילית משני צדי 0, והנקודה 0 מחוץ לתחום"
     },
     {
      "bankId": "24B-B-Q1",
      "recap": "מנה עם שני אסימפטוטות אנכיות. הפונקציה אי-זוגית ולכן (0,0) פיתול, והמשופעת y = x",
      "recapHtml": "מנה עם שני אסימפטוטות אנכיות. הפונקציה אי-זוגית ולכן (0,0) פיתול, והמשופעת y = x"
     },
     {
      "bankId": "24A-B-Q1",
      "recap": "x²eˣ: אופקית y = 0 ב-−∞ בלבד; ב-+∞ אין משופעת. שתי נקודות פיתול",
      "recapHtml": "x²eˣ: אופקית y = 0 ב-−∞ בלבד; ב-+∞ אין משופעת. שתי נקודות פיתול"
     },
     {
      "bankId": "23B-B-Q1",
      "recap": "x·e^{1/x}: אנכית מימין בלבד, משופעת y = x + 1 בשני הצדדים, ואין נקודות פיתול",
      "recapHtml": "x·e^{1/x}: אנכית מימין בלבד, משופעת y = x + 1 בשני הצדדים, ואין נקודות פיתול"
     }
    ]
   }
  ]
 },
 "recursive_seq": {
  "levels": [
   {
    "id": "C01",
    "order": 1,
    "icon": "🧮",
    "title": "מחשבים איברים וקוראים את הסדרה",
    "goal": "לחשב כמה איברים של סדרה רקורסיבית ולנחש מהם אם היא עולה, יורדת או מתנודדת.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p><b>סדרה רקורסיבית</b> נתונה בשני חלקים: האיבר הראשון <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_1</annotation></semantics></math></span>, וכלל שמחשב כל איבר מהקודם לו: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mi>f</mi><mo stretchy=\"false\">(</mo><msub><mi>a</mi><mi>n</mi></msub><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">a_{n+1}=f(a_n)</annotation></semantics></math></span>. כדי למצוא את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_2</annotation></semantics></math></span> מציבים את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_1</annotation></semantics></math></span> בכלל, כדי למצוא את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>3</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_3</annotation></semantics></math></span> מציבים את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_2</annotation></semantics></math></span>, וכן הלאה.</p>\n    <div class=\"lesson-ex\">דוגמה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\frac{a_n}{2}+1</annotation></semantics></math></span>.<br>\n    <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>=</mo><mn>1.5</mn></mrow><annotation encoding=\"application/x-tex\">a_2=\\frac{1}{2}+1=1.5</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mfrac><mn>1.5</mn><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>=</mo><mn>1.75</mn></mrow><annotation encoding=\"application/x-tex\">a_3=\\frac{1.5}{2}+1=1.75</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>4</mn></msub><mo>=</mo><mn>1.875</mn></mrow><annotation encoding=\"application/x-tex\">a_4=1.875</annotation></semantics></math></span>.<br>\n    האיברים גדלים, ולכן נחשוד שהסדרה <b>עולה</b>.</div>\n    <h3>איך קוראים את הסדרה</h3>\n    <ul>\n      <li><b>עולה</b>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>≤</mo><msub><mi>a</mi><mn>2</mn></msub><mo>≤</mo><msub><mi>a</mi><mn>3</mn></msub><mo>≤</mo><mo>…</mo></mrow><annotation encoding=\"application/x-tex\">a_1\\le a_2\\le a_3\\le\\dots</annotation></semantics></math></span> (כל איבר לא קטן מהקודם).</li>\n      <li><b>יורדת</b>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>≥</mo><msub><mi>a</mi><mn>2</mn></msub><mo>≥</mo><msub><mi>a</mi><mn>3</mn></msub><mo>≥</mo><mo>…</mo></mrow><annotation encoding=\"application/x-tex\">a_1\\ge a_2\\ge a_3\\ge\\dots</annotation></semantics></math></span></li>\n      <li><b>לא מונוטונית</b>: לפעמים עולה ולפעמים יורדת, למשל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><mn>0.5</mn><mo separator=\"true\">,</mo><mtext> </mtext><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><mn>0.5</mn><mo separator=\"true\">,</mo><mo>…</mo></mrow><annotation encoding=\"application/x-tex\">2,\\ 0.5,\\ 2,\\ 0.5,\\dots</annotation></semantics></math></span></li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 חישוב כמה איברים הוא <b>ניחוש מושכל, לא הוכחה</b>. הוא אומר לאן לכוון את ההוכחה (עולה או יורדת, ולאיזה ערך), אבל את ההוכחה עצמה עושים בשלבים הבאים.</div>\n    <div class=\"lesson-trap\">⚠️ שלושה איברים יכולים להטעות. כדי לטעון שהסדרה עולה מוכיחים את זה לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span>, ולא רק בודקים את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>&gt;</mo><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_2&gt;a_1</annotation></semantics></math></span>.</div>"
    },
    "questions": [
     {
      "id": "C01-Q1",
      "step": {
       "type": "numeric",
       "prompt": "נתונה הסדרה $a_1=3,\\ a_{n+1}=2a_n-1$. מהו $a_3$ ?",
       "answer": 9,
       "tol": 0,
       "explain": "$a_2=2\\cdot3-1=5$ ואז $a_3=2\\cdot5-1=9$. מציבים כל פעם את האיבר שחושב ולא את $a_1$.",
       "promptHtml": "נתונה הסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mi>n</mi></msub><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_1=3,\\ a_{n+1}=2a_n-1</annotation></semantics></math></span>. מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>3</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_3</annotation></semantics></math></span> ?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>⋅</mo><mn>3</mn><mo>−</mo><mn>1</mn><mo>=</mo><mn>5</mn></mrow><annotation encoding=\"application/x-tex\">a_2=2\\cdot3-1=5</annotation></semantics></math></span> ואז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn><mo>⋅</mo><mn>5</mn><mo>−</mo><mn>1</mn><mo>=</mo><mn>9</mn></mrow><annotation encoding=\"application/x-tex\">a_3=2\\cdot5-1=9</annotation></semantics></math></span>. מציבים כל פעם את האיבר שחושב ולא את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_1</annotation></semantics></math></span>."
      },
      "recap": "כל איבר מחשבים מהאיבר שלפניו",
      "recapHtml": "כל איבר מחשבים מהאיבר שלפניו"
     },
     {
      "id": "C01-Q2",
      "step": {
       "type": "numeric",
       "prompt": "נתונה הסדרה $a_1=11,\\ a_{n+1}=\\sqrt{a_n+5}$. מהו $a_3$ ?",
       "answer": 3,
       "tol": 0,
       "explain": "$a_2=\\sqrt{11+5}=\\sqrt{16}=4$ ואז $a_3=\\sqrt{4+5}=\\sqrt9=3$.",
       "promptHtml": "נתונה הסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>11</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>5</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=11,\\ a_{n+1}=\\sqrt{a_n+5}</annotation></semantics></math></span>. מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>3</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_3</annotation></semantics></math></span> ?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><msqrt><mrow><mn>11</mn><mo>+</mo><mn>5</mn></mrow></msqrt><mo>=</mo><msqrt><mn>16</mn></msqrt><mo>=</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_2=\\sqrt{11+5}=\\sqrt{16}=4</annotation></semantics></math></span> ואז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><msqrt><mrow><mn>4</mn><mo>+</mo><mn>5</mn></mrow></msqrt><mo>=</mo><msqrt><mn>9</mn></msqrt><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a_3=\\sqrt{4+5}=\\sqrt9=3</annotation></semantics></math></span>."
      },
      "recap": "מציבים את האיבר הקודם בתוך השורש",
      "recapHtml": "מציבים את האיבר הקודם בתוך השורש"
     },
     {
      "id": "C01-Q3",
      "question": "נתונה הסדרה $a_1=1,\\ a_{n+1}=\\frac{a_n}{2}+1$. חשבו את $a_2,a_3,a_4$. איך מתנהגת הסדרה לפי האיברים?",
      "options": [
       {
        "id": "a",
        "value": "עולה",
        "type": "text",
        "html": "עולה"
       },
       {
        "id": "b",
        "value": "יורדת",
        "type": "text",
        "html": "יורדת"
       },
       {
        "id": "c",
        "value": "לא מונוטונית",
        "type": "text",
        "html": "לא מונוטונית"
       },
       {
        "id": "d",
        "value": "קבועה",
        "type": "text",
        "html": "קבועה"
       }
      ],
      "correctId": "a",
      "explanation": "$a_1=1,\\ a_2=1.5,\\ a_3=1.75,\\ a_4=1.875$. כל איבר גדול מהקודם, ולכן הסדרה נראית עולה. היא לא קבועה כי $a_2\\ne a_1$, ולא יורדת או מתנודדת כי אין איבר שקטן מהקודם.",
      "recap": "משווים איברים סמוכים כדי לנחש את הכיוון",
      "questionHtml": "נתונה הסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\frac{a_n}{2}+1</annotation></semantics></math></span>. חשבו את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo separator=\"true\">,</mo><msub><mi>a</mi><mn>3</mn></msub><mo separator=\"true\">,</mo><msub><mi>a</mi><mn>4</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_2,a_3,a_4</annotation></semantics></math></span>. איך מתנהגת הסדרה לפי האיברים?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>1.5</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>1.75</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mn>4</mn></msub><mo>=</mo><mn>1.875</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_2=1.5,\\ a_3=1.75,\\ a_4=1.875</annotation></semantics></math></span>. כל איבר גדול מהקודם, ולכן הסדרה נראית עולה. היא לא קבועה כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo mathvariant=\"normal\">≠</mo><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_2\\ne a_1</annotation></semantics></math></span>, ולא יורדת או מתנודדת כי אין איבר שקטן מהקודם.",
      "recapHtml": "משווים איברים סמוכים כדי לנחש את הכיוון"
     },
     {
      "id": "C01-Q4",
      "question": "נתונה הסדרה $a_1=10,\\ a_{n+1}=\\frac{a_n}{2}+1$. חשבו את $a_2,a_3,a_4$. איך מתנהגת הסדרה לפי האיברים?",
      "options": [
       {
        "id": "a",
        "value": "עולה",
        "type": "text",
        "html": "עולה"
       },
       {
        "id": "b",
        "value": "יורדת",
        "type": "text",
        "html": "יורדת"
       },
       {
        "id": "c",
        "value": "לא מונוטונית",
        "type": "text",
        "html": "לא מונוטונית"
       },
       {
        "id": "d",
        "value": "קבועה",
        "type": "text",
        "html": "קבועה"
       }
      ],
      "correctId": "b",
      "explanation": "$a_1=10,\\ a_2=6,\\ a_3=4,\\ a_4=3$. האיברים קטנים. אותו כלל כמו בשאלה הקודמת נותן כאן סדרה יורדת, כי נקודת ההתחלה שונה: הכיוון תלוי גם ב-$a_1$.",
      "recap": "אותו כלל עם התחלה שונה יכול לתת כיוון הפוך",
      "questionHtml": "נתונה הסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>10</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_1=10,\\ a_{n+1}=\\frac{a_n}{2}+1</annotation></semantics></math></span>. חשבו את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo separator=\"true\">,</mo><msub><mi>a</mi><mn>3</mn></msub><mo separator=\"true\">,</mo><msub><mi>a</mi><mn>4</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_2,a_3,a_4</annotation></semantics></math></span>. איך מתנהגת הסדרה לפי האיברים?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>10</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>6</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>4</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mn>4</mn></msub><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a_1=10,\\ a_2=6,\\ a_3=4,\\ a_4=3</annotation></semantics></math></span>. האיברים קטנים. אותו כלל כמו בשאלה הקודמת נותן כאן סדרה יורדת, כי נקודת ההתחלה שונה: הכיוון תלוי גם ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_1</annotation></semantics></math></span>.",
      "recapHtml": "אותו כלל עם התחלה שונה יכול לתת כיוון הפוך"
     },
     {
      "id": "C01-Q5",
      "question": "נתונה הסדרה $a_1=2,\\ a_{n+1}=\\frac{1}{a_n}$. חשבו את $a_2,a_3,a_4$. איך מתנהגת הסדרה?",
      "options": [
       {
        "id": "a",
        "value": "עולה",
        "type": "text",
        "html": "עולה"
       },
       {
        "id": "b",
        "value": "יורדת",
        "type": "text",
        "html": "יורדת"
       },
       {
        "id": "c",
        "value": "לא מונוטונית",
        "type": "text",
        "html": "לא מונוטונית"
       },
       {
        "id": "d",
        "value": "קבועה",
        "type": "text",
        "html": "קבועה"
       }
      ],
      "correctId": "c",
      "explanation": "$a_1=2,\\ a_2=0.5,\\ a_3=2,\\ a_4=0.5$. האיברים מתחלפים בין שני ערכים, ולכן הסדרה לא מונוטונית (והיא גם לא מתכנסת).",
      "recap": "איברים שמתחלפים: לא מונוטונית",
      "questionHtml": "נתונה הסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mn>1</mn><msub><mi>a</mi><mi>n</mi></msub></mfrac></mrow><annotation encoding=\"application/x-tex\">a_1=2,\\ a_{n+1}=\\frac{1}{a_n}</annotation></semantics></math></span>. חשבו את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo separator=\"true\">,</mo><msub><mi>a</mi><mn>3</mn></msub><mo separator=\"true\">,</mo><msub><mi>a</mi><mn>4</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_2,a_3,a_4</annotation></semantics></math></span>. איך מתנהגת הסדרה?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>0.5</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mn>4</mn></msub><mo>=</mo><mn>0.5</mn></mrow><annotation encoding=\"application/x-tex\">a_1=2,\\ a_2=0.5,\\ a_3=2,\\ a_4=0.5</annotation></semantics></math></span>. האיברים מתחלפים בין שני ערכים, ולכן הסדרה לא מונוטונית (והיא גם לא מתכנסת).",
      "recapHtml": "איברים שמתחלפים: לא מונוטונית"
     },
     {
      "id": "C01-Q6",
      "step": {
       "type": "numeric",
       "prompt": "נתונה הסדרה $a_1=1,\\ a_{n+1}=\\frac{6}{5-a_n}$. מהו $a_3$ ? (עיגול לשלוש ספרות אחרי הנקודה)",
       "answer": 1.714,
       "tol": 0.001,
       "explain": "$a_2=\\frac{6}{5-1}=1.5$ ואז $a_3=\\frac{6}{5-1.5}=\\frac{6}{3.5}=\\frac{12}{7}\\approx1.714$.",
       "promptHtml": "נתונה הסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mn>6</mn><mrow><mn>5</mn><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\frac{6}{5-a_n}</annotation></semantics></math></span>. מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>3</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_3</annotation></semantics></math></span> ? (עיגול לשלוש ספרות אחרי הנקודה)",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>6</mn><mrow><mn>5</mn><mo>−</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>1.5</mn></mrow><annotation encoding=\"application/x-tex\">a_2=\\frac{6}{5-1}=1.5</annotation></semantics></math></span> ואז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mfrac><mn>6</mn><mrow><mn>5</mn><mo>−</mo><mn>1.5</mn></mrow></mfrac><mo>=</mo><mfrac><mn>6</mn><mn>3.5</mn></mfrac><mo>=</mo><mfrac><mn>12</mn><mn>7</mn></mfrac><mo>≈</mo><mn>1.714</mn></mrow><annotation encoding=\"application/x-tex\">a_3=\\frac{6}{5-1.5}=\\frac{6}{3.5}=\\frac{12}{7}\\approx1.714</annotation></semantics></math></span>."
      },
      "recap": "מציבים בכלל ומחשבים צעד אחר צעד",
      "recapHtml": "מציבים בכלל ומחשבים צעד אחר צעד"
     }
    ]
   },
   {
    "id": "C02",
    "order": 2,
    "icon": "🎯",
    "title": "נקודת שבת: הגבול המועמד",
    "goal": "למצוא מהכלל הרקורסיבי את הערכים שהגבול יכול לקבל, ולבחור ביניהם.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>נניח שהסדרה מתכנסת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">L</annotation></semantics></math></span>. אז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>→</mo><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">a_n\\to L</annotation></semantics></math></span> וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>→</mo><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">a_{n+1}\\to L</annotation></semantics></math></span> (זו אותה סדרה, מוסטת באינדקס אחד). אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> רציפה, הגבול של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><msub><mi>a</mi><mi>n</mi></msub><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f(a_n)</annotation></semantics></math></span> הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>L</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f(L)</annotation></semantics></math></span>. מכאן שמתקיים:</p>\n    <div class=\"lesson-formula\"><span class=\"math-block\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\" display=\"block\"><semantics><mrow><mi>L</mi><mo>=</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>L</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">L=f(L)</annotation></semantics></math></span></div>\n    <p>פותרים את המשוואה, וכל פתרון הוא <b>מועמד</b> לגבול (נקרא גם נקודת שבת של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span>).</p>\n    <div class=\"lesson-ex\"><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_{n+1}=\\sqrt{2+a_n}</annotation></semantics></math></span> עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1</annotation></semantics></math></span>. מציבים: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><msqrt><mrow><mn>2</mn><mo>+</mo><mi>L</mi></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">L=\\sqrt{2+L}</annotation></semantics></math></span>, מעלים בריבוע <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>=</mo><mi>L</mi><mo>+</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">L^2=L+2</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>−</mo><mi>L</mi><mo>−</mo><mn>2</mn><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">L^2-L-2=0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>L</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>L</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">(L-2)(L+1)=0</annotation></semantics></math></span>.<br>\n    המועמדים הם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">L=2</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">L=-1</annotation></semantics></math></span>. כל האיברים חיוביים, ולכן הגבול אינו שלילי ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">L=2</annotation></semantics></math></span>.</div>\n    <div class=\"lesson-rule\">🔑 כשיש כמה מועמדים בוחרים לפי מה שכבר ידוע על הסדרה: סימן האיברים, האיבר הראשון והכיוון (סדרה עולה מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_1</annotation></semantics></math></span> לא יכולה להגיע לערך קטן מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_1</annotation></semantics></math></span>).</div>\n    <div class=\"lesson-trap\">⚠️ חישוב <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">L</annotation></semantics></math></span> <b>אינו הוכחת התכנסות</b>. הסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=2a_n+1</annotation></semantics></math></span> נותנת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mn>2</mn><mi>L</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">L=2L+1</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">L=-1</annotation></semantics></math></span>, אבל האיברים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo separator=\"true\">,</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>7</mn><mo separator=\"true\">,</mo><mn>15</mn><mo separator=\"true\">,</mo><mo>…</mo></mrow><annotation encoding=\"application/x-tex\">1,3,7,15,\\dots</annotation></semantics></math></span> גדלים לאינסוף. המשוואה מניחה שהגבול קיים. את זה מוכיחים בנפרד (ברמות הבאות).</div>"
    },
    "questions": [
     {
      "id": "C02-Q1",
      "step": {
       "type": "numeric",
       "prompt": "הסדרה $a_1=1,\\ a_{n+1}=\\frac{a_n}{2}+1$ מתכנסת. מהו הגבול שלה?",
       "answer": 2,
       "tol": 0,
       "explain": "$L=\\frac{L}{2}+1\\Rightarrow\\frac{L}{2}=1\\Rightarrow L=2$.",
       "promptHtml": "הסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\frac{a_n}{2}+1</annotation></semantics></math></span> מתכנסת. מהו הגבול שלה?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mfrac><mi>L</mi><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>⇒</mo><mfrac><mi>L</mi><mn>2</mn></mfrac><mo>=</mo><mn>1</mn><mo>⇒</mo><mi>L</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">L=\\frac{L}{2}+1\\Rightarrow\\frac{L}{2}=1\\Rightarrow L=2</annotation></semantics></math></span>."
      },
      "recap": "פותרים L=f(L)",
      "recapHtml": "פותרים L=f(L)"
     },
     {
      "id": "C02-Q2",
      "question": "הסדרה $a_1=1,\\ a_{n+1}=\\sqrt{2+a_n}$ מתכנסת, וכל איבריה חיוביים. מהו הגבול?",
      "options": [
       {
        "id": "a",
        "value": "$-1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">-1</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$\\sqrt2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msqrt><mn>2</mn></msqrt></mrow><annotation encoding=\"application/x-tex\">\\sqrt2</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$4$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">4</annotation></semantics></math></span>"
       }
      ],
      "correctId": "b",
      "explanation": "$L^2=L+2$ נותן $L=2$ או $L=-1$. האיברים חיוביים ולכן $L\\ge0$ ונפסל $-1$. הערכים $\\sqrt2$ ו-$4$ אינם פתרונות של המשוואה.",
      "recap": "פותרים את L=f(L) ופוסלים שורש שלא מתאים לסימן האיברים",
      "questionHtml": "הסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\sqrt{2+a_n}</annotation></semantics></math></span> מתכנסת, וכל איבריה חיוביים. מהו הגבול?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>=</mo><mi>L</mi><mo>+</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">L^2=L+2</annotation></semantics></math></span> נותן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">L=2</annotation></semantics></math></span> או <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">L=-1</annotation></semantics></math></span>. האיברים חיוביים ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">L\\ge0</annotation></semantics></math></span> ונפסל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">-1</annotation></semantics></math></span>. הערכים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msqrt><mn>2</mn></msqrt></mrow><annotation encoding=\"application/x-tex\">\\sqrt2</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">4</annotation></semantics></math></span> אינם פתרונות של המשוואה.",
      "recapHtml": "פותרים את L=f(L) ופוסלים שורש שלא מתאים לסימן האיברים"
     },
     {
      "id": "C02-Q3",
      "question": "נתונה $a_1=1,\\ a_{n+1}=\\frac{6}{5-a_n}$, ומתקבלים האיברים $1,\\ 1.5,\\ 1.71,\\ 1.83,\\ 1.89\\dots$ מהן נקודות השבת, ולאיזו מהן הסדרה מתקרבת?",
      "options": [
       {
        "id": "a",
        "value": "$2$ ו-$3$, והיא מתקרבת ל-$2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span>, והיא מתקרבת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$2$ ו-$3$, והיא מתקרבת ל-$3$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span>, והיא מתקרבת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$-2$ ו-$-3$, והיא מתקרבת ל-$-2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">-2</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">-3</annotation></semantics></math></span>, והיא מתקרבת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">-2</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$1$ ו-$6$, והיא מתקרבת ל-$1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>6</mn></mrow><annotation encoding=\"application/x-tex\">6</annotation></semantics></math></span>, והיא מתקרבת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "$L(5-L)=6\\Rightarrow L^2-5L+6=0\\Rightarrow(L-2)(L-3)=0$, כלומר $L=2,3$. האיברים עולים ומתקרבים ל-$2$ מלמטה, ולכן הגבול הוא $2$ ולא $3$. הזוגות $-2,-3$ ו-$1,6$ אינם פתרונות.",
      "recap": "שני מועמדים: בוחרים לפי האיברים והכיוון",
      "questionHtml": "נתונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mn>6</mn><mrow><mn>5</mn><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\frac{6}{5-a_n}</annotation></semantics></math></span>, ומתקבלים האיברים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><mn>1.5</mn><mo separator=\"true\">,</mo><mtext> </mtext><mn>1.71</mn><mo separator=\"true\">,</mo><mtext> </mtext><mn>1.83</mn><mo separator=\"true\">,</mo><mtext> </mtext><mn>1.89</mn><mo>…</mo></mrow><annotation encoding=\"application/x-tex\">1,\\ 1.5,\\ 1.71,\\ 1.83,\\ 1.89\\dots</annotation></semantics></math></span> מהן נקודות השבת, ולאיזו מהן הסדרה מתקרבת?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo stretchy=\"false\">(</mo><mn>5</mn><mo>−</mo><mi>L</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mn>6</mn><mo>⇒</mo><msup><mi>L</mi><mn>2</mn></msup><mo>−</mo><mn>5</mn><mi>L</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn><mo>⇒</mo><mo stretchy=\"false\">(</mo><mi>L</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>L</mi><mo>−</mo><mn>3</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">L(5-L)=6\\Rightarrow L^2-5L+6=0\\Rightarrow(L-2)(L-3)=0</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">L=2,3</annotation></semantics></math></span>. האיברים עולים ומתקרבים ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span> מלמטה, ולכן הגבול הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span> ולא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">3</annotation></semantics></math></span>. הזוגות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>2</mn><mo separator=\"true\">,</mo><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">-2,-3</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo separator=\"true\">,</mo><mn>6</mn></mrow><annotation encoding=\"application/x-tex\">1,6</annotation></semantics></math></span> אינם פתרונות.",
      "recapHtml": "שני מועמדים: בוחרים לפי האיברים והכיוון"
     },
     {
      "id": "C02-Q4",
      "question": "נתונה $a_1=1,\\ a_{n+1}=2a_n+1$. מ-$L=2L+1$ מקבלים $L=-1$. מה נכון?",
      "options": [
       {
        "id": "a",
        "value": "הסדרה מתכנסת ל-$-1$",
        "type": "text",
        "html": "הסדרה מתכנסת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">-1</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "הסדרה לא מתכנסת, והמשוואה נותנת רק מועמד",
        "type": "text",
        "html": "הסדרה לא מתכנסת, והמשוואה נותנת רק מועמד"
       },
       {
        "id": "c",
        "value": "הסדרה מתכנסת ל-$1$",
        "type": "text",
        "html": "הסדרה מתכנסת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">1</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "הסדרה מתכנסת ל-$0$",
        "type": "text",
        "html": "הסדרה מתכנסת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">0</annotation></semantics></math></span>"
       }
      ],
      "correctId": "b",
      "explanation": "$a_n=2^n-1$ (האיברים $1,3,7,15,\\dots$) ושואפת ל-$\\infty$. הפתרון $L=-1$ נובע מההנחה שהסדרה מתכנסת, וההנחה הזו שגויה כאן.",
      "recap": "L=f(L) לא מוכיחה שהגבול קיים",
      "questionHtml": "נתונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=2a_n+1</annotation></semantics></math></span>. מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mn>2</mn><mi>L</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">L=2L+1</annotation></semantics></math></span> מקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">L=-1</annotation></semantics></math></span>. מה נכון?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msup><mn>2</mn><mi>n</mi></msup><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_n=2^n-1</annotation></semantics></math></span> (האיברים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo separator=\"true\">,</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>7</mn><mo separator=\"true\">,</mo><mn>15</mn><mo separator=\"true\">,</mo><mo>…</mo></mrow><annotation encoding=\"application/x-tex\">1,3,7,15,\\dots</annotation></semantics></math></span>) ושואפת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi mathvariant=\"normal\">∞</mi></mrow><annotation encoding=\"application/x-tex\">\\infty</annotation></semantics></math></span>. הפתרון <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">L=-1</annotation></semantics></math></span> נובע מההנחה שהסדרה מתכנסת, וההנחה הזו שגויה כאן.",
      "recapHtml": "L=f(L) לא מוכיחה שהגבול קיים"
     },
     {
      "id": "C02-Q5",
      "step": {
       "type": "numeric",
       "prompt": "הסדרה $a_1=3,\\ a_{n+1}=\\frac{1}{2}\\left(a_n+\\frac{7}{a_n}\\right)$ מתכנסת וכל איבריה חיוביים. מהו הגבול? (עיגול לשלוש ספרות אחרי הנקודה)",
       "answer": 2.646,
       "tol": 0.001,
       "explain": "$L=\\frac12\\left(L+\\frac7L\\right)\\Rightarrow2L=L+\\frac7L\\Rightarrow L=\\frac7L\\Rightarrow L^2=7$. חיובי, לכן $L=\\sqrt7\\approx2.646$.",
       "promptHtml": "הסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mrow><mo fence=\"true\">(</mo><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mfrac><mn>7</mn><msub><mi>a</mi><mi>n</mi></msub></mfrac><mo fence=\"true\">)</mo></mrow></mrow><annotation encoding=\"application/x-tex\">a_1=3,\\ a_{n+1}=\\frac{1}{2}\\left(a_n+\\frac{7}{a_n}\\right)</annotation></semantics></math></span> מתכנסת וכל איבריה חיוביים. מהו הגבול? (עיגול לשלוש ספרות אחרי הנקודה)",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mrow><mo fence=\"true\">(</mo><mi>L</mi><mo>+</mo><mfrac><mn>7</mn><mi>L</mi></mfrac><mo fence=\"true\">)</mo></mrow><mo>⇒</mo><mn>2</mn><mi>L</mi><mo>=</mo><mi>L</mi><mo>+</mo><mfrac><mn>7</mn><mi>L</mi></mfrac><mo>⇒</mo><mi>L</mi><mo>=</mo><mfrac><mn>7</mn><mi>L</mi></mfrac><mo>⇒</mo><msup><mi>L</mi><mn>2</mn></msup><mo>=</mo><mn>7</mn></mrow><annotation encoding=\"application/x-tex\">L=\\frac12\\left(L+\\frac7L\\right)\\Rightarrow2L=L+\\frac7L\\Rightarrow L=\\frac7L\\Rightarrow L^2=7</annotation></semantics></math></span>. חיובי, לכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><msqrt><mn>7</mn></msqrt><mo>≈</mo><mn>2.646</mn></mrow><annotation encoding=\"application/x-tex\">L=\\sqrt7\\approx2.646</annotation></semantics></math></span>."
      },
      "recap": "L=½(L+c/L) נותן L²=c",
      "recapHtml": "L=½(L+c/L) נותן L²=c"
     },
     {
      "id": "C02-Q6",
      "step": {
       "type": "order",
       "prompt": "סדרו את הפתרון של הגבול של $a_1=1,\\ a_{n+1}=\\sqrt{6+a_n}$ (נתון שהיא מתכנסת).",
       "lines": [
        "נסמן $L=\\lim a_n$, ואז גם $a_{n+1}\\to L$",
        "בכלל הרקורסיבי מקבלים $L=\\sqrt{6+L}$",
        "מעלים בריבוע: $L^2-L-6=0$, כלומר $(L-3)(L+2)=0$",
        "כל האיברים חיוביים ולכן $L\\ge0$ ו-$L=3$"
       ],
       "explain": "קודם מגדירים את $L$, אחר כך מציבים בכלל, פותרים את המשוואה, ורק בסוף בוחרים את השורש המתאים.",
       "promptHtml": "סדרו את הפתרון של הגבול של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><mn>6</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\sqrt{6+a_n}</annotation></semantics></math></span> (נתון שהיא מתכנסת).",
       "explainHtml": "קודם מגדירים את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">L</annotation></semantics></math></span>, אחר כך מציבים בכלל, פותרים את המשוואה, ורק בסוף בוחרים את השורש המתאים.",
       "linesHtml": [
        "נסמן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding=\"application/x-tex\">L=\\lim a_n</annotation></semantics></math></span>, ואז גם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>→</mo><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">a_{n+1}\\to L</annotation></semantics></math></span>",
        "בכלל הרקורסיבי מקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><msqrt><mrow><mn>6</mn><mo>+</mo><mi>L</mi></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">L=\\sqrt{6+L}</annotation></semantics></math></span>",
        "מעלים בריבוע: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>−</mo><mi>L</mi><mo>−</mo><mn>6</mn><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">L^2-L-6=0</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>L</mi><mo>−</mo><mn>3</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>L</mi><mo>+</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">(L-3)(L+2)=0</annotation></semantics></math></span>",
        "כל האיברים חיוביים ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">L\\ge0</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">L=3</annotation></semantics></math></span>"
       ]
      },
      "recap": "מגדירים L, פותרים L=f(L), בוחרים שורש",
      "recapHtml": "מגדירים L, פותרים L=f(L), בוחרים שורש"
     }
    ]
   },
   {
    "id": "C03",
    "order": 3,
    "icon": "🧱",
    "title": "חסימה באינדוקציה",
    "goal": "להוכיח באינדוקציה שסדרה רקורסיבית חסומה, ולבחור חסם שמתאים גם לאיבר הראשון.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>סדרה <b>חסומה מלמעלה</b> אם יש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>M</mi></mrow><annotation encoding=\"application/x-tex\">M</annotation></semantics></math></span> כך ש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mi>M</mi></mrow><annotation encoding=\"application/x-tex\">a_n\\le M</annotation></semantics></math></span> לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span>. <b>חסומה מלמטה</b> אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≥</mo><mi>m</mi></mrow><annotation encoding=\"application/x-tex\">a_n\\ge m</annotation></semantics></math></span> לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span>. את החסם מוכיחים באינדוקציה:</p>\n    <ul>\n      <li><b>בסיס:</b> בודקים שהחסם נכון עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_1</annotation></semantics></math></span> <b>עצמו</b>.</li>\n      <li><b>הנחה:</b> <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mi>M</mi></mrow><annotation encoding=\"application/x-tex\">a_n\\le M</annotation></semantics></math></span>.</li>\n      <li><b>צעד:</b> מפעילים את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> על שני צדדי אי-השוויון ומקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mi>f</mi><mo stretchy=\"false\">(</mo><msub><mi>a</mi><mi>n</mi></msub><mo stretchy=\"false\">)</mo><mo>≤</mo><mi>M</mi></mrow><annotation encoding=\"application/x-tex\">a_{n+1}=f(a_n)\\le M</annotation></semantics></math></span>. כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> עולה, אי-השוויון נשמר.</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 איזה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>M</mi></mrow><annotation encoding=\"application/x-tex\">M</annotation></semantics></math></span> בוחרים? את נקודת השבת מהרמה הקודמת. הצעד עובד בדיוק כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>M</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>M</mi></mrow><annotation encoding=\"application/x-tex\">f(M)=M</annotation></semantics></math></span>: מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mi>M</mi></mrow><annotation encoding=\"application/x-tex\">a_n\\le M</annotation></semantics></math></span> נובע <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><msub><mi>a</mi><mi>n</mi></msub><mo stretchy=\"false\">)</mo><mo>≤</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>M</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>M</mi></mrow><annotation encoding=\"application/x-tex\">f(a_n)\\le f(M)=M</annotation></semantics></math></span>.</div>\n    <div class=\"lesson-ex\"><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\sqrt{2+a_n}</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>M</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">M=2</annotation></semantics></math></span> (נקודת שבת). בסיס: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1&lt;2</annotation></semantics></math></span>. הנחה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n&lt;2</annotation></semantics></math></span>. צעד: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">2+a_n&lt;4</annotation></semantics></math></span>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msqrt><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></msqrt><mo>&lt;</mo><msqrt><mn>4</mn></msqrt><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">\\sqrt{2+a_n}&lt;\\sqrt4=2</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_{n+1}&lt;2</annotation></semantics></math></span>.</div>\n    <div class=\"lesson-trap\">⚠️ החסם חייב להתקיים כבר ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_1</annotation></semantics></math></span>. הטענה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n&lt;2</annotation></semantics></math></span> <b>שגויה</b> כשהסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=3,\\ a_{n+1}=\\sqrt{2+a_n}</annotation></semantics></math></span> מתחילה מעל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span>. אז הסדרה יורדת והחסם הנכון הוא מלמטה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≥</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\ge2</annotation></semantics></math></span>. נקודת ההתחלה קובעת אם החסם הוא מלמעלה או מלמטה.</div>"
    },
    "questions": [
     {
      "id": "C03-Q1",
      "step": {
       "type": "order",
       "prompt": "סדרו את ההוכחה ש-$a_n<2$ לכל $n$ עבור $a_1=1,\\ a_{n+1}=\\sqrt{2+a_n}$.",
       "lines": [
        "בסיס: $a_1=1<2$",
        "הנחה: $a_n<2$",
        "מכאן $2+a_n<4$",
        "פונקציית השורש עולה, ולכן $\\sqrt{2+a_n}<\\sqrt4=2$",
        "כלומר $a_{n+1}<2$, ולפי אינדוקציה $a_n<2$ לכל $n$"
       ],
       "explain": "סדר ההוכחה: בסיס, הנחה, ואז שרשרת צעדים שמסתיימת בטענה עבור $n+1$.",
       "promptHtml": "סדרו את ההוכחה ש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n&lt;2</annotation></semantics></math></span> לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span> עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\sqrt{2+a_n}</annotation></semantics></math></span>.",
       "explainHtml": "סדר ההוכחה: בסיס, הנחה, ואז שרשרת צעדים שמסתיימת בטענה עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">n+1</annotation></semantics></math></span>.",
       "linesHtml": [
        "בסיס: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1&lt;2</annotation></semantics></math></span>",
        "הנחה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n&lt;2</annotation></semantics></math></span>",
        "מכאן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">2+a_n&lt;4</annotation></semantics></math></span>",
        "פונקציית השורש עולה, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msqrt><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></msqrt><mo>&lt;</mo><msqrt><mn>4</mn></msqrt><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">\\sqrt{2+a_n}&lt;\\sqrt4=2</annotation></semantics></math></span>",
        "כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_{n+1}&lt;2</annotation></semantics></math></span>, ולפי אינדוקציה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n&lt;2</annotation></semantics></math></span> לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span>"
       ]
      },
      "recap": "בסיס, הנחה, צעד",
      "recapHtml": "בסיס, הנחה, צעד"
     },
     {
      "id": "C03-Q2",
      "question": "נתונה $a_1=3,\\ a_{n+1}=\\sqrt{2+a_n}$. איזו טענה נכונה לכל $n$ וניתנת להוכחה באינדוקציה?",
      "options": [
       {
        "id": "a",
        "value": "$a_n\\le2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\le2</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$a_n\\ge2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≥</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\ge2</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$a_n\\ge4$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≥</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\ge4</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$a_n\\le1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\le1</annotation></semantics></math></span>"
       }
      ],
      "correctId": "b",
      "explanation": "בסיס: $a_1=3\\ge2$. צעד: $a_n\\ge2\\Rightarrow2+a_n\\ge4\\Rightarrow a_{n+1}\\ge2$. הטענות $a_n\\le2$, $a_n\\ge4$ ו-$a_n\\le1$ שגויות כבר ב-$a_1=3$.",
      "recap": "בודקים את הבסיס על a_1 עצמו",
      "questionHtml": "נתונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=3,\\ a_{n+1}=\\sqrt{2+a_n}</annotation></semantics></math></span>. איזו טענה נכונה לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span> וניתנת להוכחה באינדוקציה?",
      "explanationHtml": "בסיס: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>≥</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_1=3\\ge2</annotation></semantics></math></span>. צעד: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≥</mo><mn>2</mn><mo>⇒</mo><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub><mo>≥</mo><mn>4</mn><mo>⇒</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>≥</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\ge2\\Rightarrow2+a_n\\ge4\\Rightarrow a_{n+1}\\ge2</annotation></semantics></math></span>. הטענות <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\le2</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≥</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\ge4</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\le1</annotation></semantics></math></span> שגויות כבר ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">a_1=3</annotation></semantics></math></span>.",
      "recapHtml": "בודקים את הבסיס על a_1 עצמו"
     },
     {
      "id": "C03-Q3",
      "step": {
       "type": "findbug",
       "prompt": "בהוכחה ש-$a_n<4$ עבור $a_1=1,\\ a_{n+1}=\\sqrt{a_n+12}$ יש שגיאה אחת. באיזו שורה?",
       "lines": [
        "בסיס: $a_1=1<4$",
        "הנחה: $a_n<4$",
        "לכן $a_n+12<12$",
        "פונקציית השורש עולה, ולכן $\\sqrt{a_n+12}<\\sqrt{16}$",
        "כלומר $a_{n+1}<4$"
       ],
       "bugIndex": 2,
       "explain": "מ-$a_n<4$ מקבלים $a_n+12<16$ ולא $12$. החסם החדש הוא $4+12=16$.",
       "promptHtml": "בהוכחה ש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_n&lt;4</annotation></semantics></math></span> עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>12</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\sqrt{a_n+12}</annotation></semantics></math></span> יש שגיאה אחת. באיזו שורה?",
       "explainHtml": "מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_n&lt;4</annotation></semantics></math></span> מקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>12</mn><mo>&lt;</mo><mn>16</mn></mrow><annotation encoding=\"application/x-tex\">a_n+12&lt;16</annotation></semantics></math></span> ולא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>12</mn></mrow><annotation encoding=\"application/x-tex\">12</annotation></semantics></math></span>. החסם החדש הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn><mo>+</mo><mn>12</mn><mo>=</mo><mn>16</mn></mrow><annotation encoding=\"application/x-tex\">4+12=16</annotation></semantics></math></span>.",
       "linesHtml": [
        "בסיס: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>&lt;</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1&lt;4</annotation></semantics></math></span>",
        "הנחה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_n&lt;4</annotation></semantics></math></span>",
        "לכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>12</mn><mo>&lt;</mo><mn>12</mn></mrow><annotation encoding=\"application/x-tex\">a_n+12&lt;12</annotation></semantics></math></span>",
        "פונקציית השורש עולה, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msqrt><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>12</mn></mrow></msqrt><mo>&lt;</mo><msqrt><mn>16</mn></msqrt></mrow><annotation encoding=\"application/x-tex\">\\sqrt{a_n+12}&lt;\\sqrt{16}</annotation></semantics></math></span>",
        "כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>&lt;</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_{n+1}&lt;4</annotation></semantics></math></span>"
       ]
      },
      "recap": "מוסיפים את הקבוע גם לחסם",
      "recapHtml": "מוסיפים את הקבוע גם לחסם"
     },
     {
      "id": "C03-Q4",
      "step": {
       "type": "numeric",
       "prompt": "עבור $a_{n+1}=\\frac{a_n}{2}+1$, מניחים $a_n<2$. מהו המספר $c$ המדויק שמקבלים כך ש-$a_{n+1}<c$ ?",
       "answer": 2,
       "tol": 0,
       "explain": "$a_n<2\\Rightarrow\\frac{a_n}{2}<1\\Rightarrow\\frac{a_n}{2}+1<2$, ולכן $c=2$ ושמרנו על אותו חסם.",
       "promptHtml": "עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_{n+1}=\\frac{a_n}{2}+1</annotation></semantics></math></span>, מניחים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n&lt;2</annotation></semantics></math></span>. מהו המספר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>c</mi></mrow><annotation encoding=\"application/x-tex\">c</annotation></semantics></math></span> המדויק שמקבלים כך ש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>&lt;</mo><mi>c</mi></mrow><annotation encoding=\"application/x-tex\">a_{n+1}&lt;c</annotation></semantics></math></span> ?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>2</mn><mo>⇒</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>&lt;</mo><mn>1</mn><mo>⇒</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n&lt;2\\Rightarrow\\frac{a_n}{2}&lt;1\\Rightarrow\\frac{a_n}{2}+1&lt;2</annotation></semantics></math></span>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>c</mi><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">c=2</annotation></semantics></math></span> ושמרנו על אותו חסם."
      },
      "recap": "הצעד חוזר לאותו חסם",
      "recapHtml": "הצעד חוזר לאותו חסם"
     },
     {
      "id": "C03-Q5",
      "question": "מנסים להוכיח $a_n\\le1.5$ עבור $a_1=1,\\ a_{n+1}=\\sqrt{2+a_n}$. מה קורה?",
      "options": [
       {
        "id": "a",
        "value": "הבסיס נכשל",
        "type": "text",
        "html": "הבסיס נכשל"
       },
       {
        "id": "b",
        "value": "הצעד נכשל: מ-$a_n\\le1.5$ מקבלים רק $a_{n+1}\\le\\sqrt{3.5}\\approx1.87$",
        "type": "text",
        "html": "הצעד נכשל: מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mn>1.5</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\le1.5</annotation></semantics></math></span> מקבלים רק <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>≤</mo><msqrt><mn>3.5</mn></msqrt><mo>≈</mo><mn>1.87</mn></mrow><annotation encoding=\"application/x-tex\">a_{n+1}\\le\\sqrt{3.5}\\approx1.87</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "ההוכחה מצליחה",
        "type": "text",
        "html": "ההוכחה מצליחה"
       },
       {
        "id": "d",
        "value": "אי אפשר להפעיל שורש על אי-שוויון",
        "type": "text",
        "html": "אי אפשר להפעיל שורש על אי-שוויון"
       }
      ],
      "correctId": "b",
      "explanation": "בסיס: $a_1=1\\le1.5$ תקין. בצעד, $2+a_n\\le3.5$ נותן $a_{n+1}\\le\\sqrt{3.5}\\approx1.87>1.5$, ולא מסיקים את החסם. אכן $a_3\\approx1.93>1.5$, כך שהטענה שגויה. החסם שעובד הוא נקודת השבת $2$. שורש הוא פונקציה עולה ולכן מותר להפעיל אותו.",
      "recap": "חסם שאינו נקודת שבת לא סוגר את הצעד",
      "questionHtml": "מנסים להוכיח <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mn>1.5</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\le1.5</annotation></semantics></math></span> עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\sqrt{2+a_n}</annotation></semantics></math></span>. מה קורה?",
      "explanationHtml": "בסיס: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>≤</mo><mn>1.5</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1\\le1.5</annotation></semantics></math></span> תקין. בצעד, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mn>3.5</mn></mrow><annotation encoding=\"application/x-tex\">2+a_n\\le3.5</annotation></semantics></math></span> נותן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>≤</mo><msqrt><mn>3.5</mn></msqrt><mo>≈</mo><mn>1.87</mn><mo>&gt;</mo><mn>1.5</mn></mrow><annotation encoding=\"application/x-tex\">a_{n+1}\\le\\sqrt{3.5}\\approx1.87&gt;1.5</annotation></semantics></math></span>, ולא מסיקים את החסם. אכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>3</mn></msub><mo>≈</mo><mn>1.93</mn><mo>&gt;</mo><mn>1.5</mn></mrow><annotation encoding=\"application/x-tex\">a_3\\approx1.93&gt;1.5</annotation></semantics></math></span>, כך שהטענה שגויה. החסם שעובד הוא נקודת השבת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">2</annotation></semantics></math></span>. שורש הוא פונקציה עולה ולכן מותר להפעיל אותו.",
      "recapHtml": "חסם שאינו נקודת שבת לא סוגר את הצעד"
     },
     {
      "id": "C03-Q6",
      "step": {
       "type": "numeric",
       "prompt": "עבור $a_1=1,\\ a_{n+1}=\\sqrt{3a_n+10}$ מחפשים חסם עליון $M$ שהצעד עובד עבורו בדיוק ($f(M)=M$, $M>0$). מהו $M$ ?",
       "answer": 5,
       "tol": 0,
       "explain": "$M=\\sqrt{3M+10}\\Rightarrow M^2-3M-10=0\\Rightarrow(M-5)(M+2)=0$, ולכן $M=5$. אכן $a_n\\le5\\Rightarrow3a_n+10\\le25\\Rightarrow a_{n+1}\\le5$.",
       "promptHtml": "עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><mn>3</mn><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>10</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\sqrt{3a_n+10}</annotation></semantics></math></span> מחפשים חסם עליון <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>M</mi></mrow><annotation encoding=\"application/x-tex\">M</annotation></semantics></math></span> שהצעד עובד עבורו בדיוק (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>M</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mi>M</mi></mrow><annotation encoding=\"application/x-tex\">f(M)=M</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>M</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">M&gt;0</annotation></semantics></math></span>). מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>M</mi></mrow><annotation encoding=\"application/x-tex\">M</annotation></semantics></math></span> ?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>M</mi><mo>=</mo><msqrt><mrow><mn>3</mn><mi>M</mi><mo>+</mo><mn>10</mn></mrow></msqrt><mo>⇒</mo><msup><mi>M</mi><mn>2</mn></msup><mo>−</mo><mn>3</mn><mi>M</mi><mo>−</mo><mn>10</mn><mo>=</mo><mn>0</mn><mo>⇒</mo><mo stretchy=\"false\">(</mo><mi>M</mi><mo>−</mo><mn>5</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>M</mi><mo>+</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">M=\\sqrt{3M+10}\\Rightarrow M^2-3M-10=0\\Rightarrow(M-5)(M+2)=0</annotation></semantics></math></span>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>M</mi><mo>=</mo><mn>5</mn></mrow><annotation encoding=\"application/x-tex\">M=5</annotation></semantics></math></span>. אכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mn>5</mn><mo>⇒</mo><mn>3</mn><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>10</mn><mo>≤</mo><mn>25</mn><mo>⇒</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>≤</mo><mn>5</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\le5\\Rightarrow3a_n+10\\le25\\Rightarrow a_{n+1}\\le5</annotation></semantics></math></span>."
      },
      "recap": "החסם הטבעי הוא נקודת השבת",
      "recapHtml": "החסם הטבעי הוא נקודת השבת"
     }
    ]
   },
   {
    "id": "C04",
    "order": 4,
    "icon": "📈",
    "title": "מונוטוניות: עולה או יורדת",
    "goal": "להוכיח שסדרה רקורסיבית עולה או יורדת, בשתי שיטות: הפרש ואינדוקציה.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>יש שתי דרכים להוכיח ש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>≥</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding=\"application/x-tex\">a_{n+1}\\ge a_n</annotation></semantics></math></span> לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span>.</p>\n    <h3>שיטה א: הפרש</h3>\n    <p>מחשבים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding=\"application/x-tex\">a_{n+1}-a_n</annotation></semantics></math></span> כביטוי ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding=\"application/x-tex\">a_n</annotation></semantics></math></span> בלבד, ובודקים את הסימן בעזרת <b>החסם שכבר הוכחנו</b>. לכן קודם מוכיחים חסימה ואחר כך מונוטוניות.</p>\n    <div class=\"lesson-ex\"><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_{n+1}=\\frac{a_n}{2}+1</annotation></semantics></math></span>: ההפרש הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>1</mn><mo>−</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><mn>2</mn></mfrac></mrow><annotation encoding=\"application/x-tex\">a_{n+1}-a_n=1-\\frac{a_n}{2}=\\frac{2-a_n}{2}</annotation></semantics></math></span>. אם הוכחנו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n&lt;2</annotation></semantics></math></span> ההפרש חיובי והסדרה עולה. אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&gt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n&gt;2</annotation></semantics></math></span> ההפרש שלילי והסדרה יורדת.</div>\n    <h3>שיטה ב: אינדוקציה (כש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> עולה)</h3>\n    <p>בסיס: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>≤</mo><msub><mi>a</mi><mn>2</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_1\\le a_2</annotation></semantics></math></span>. הנחה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><annotation encoding=\"application/x-tex\">a_n\\le a_{n+1}</annotation></semantics></math></span>. צעד: מפעילים את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> העולה על שני הצדדים ומקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><msub><mi>a</mi><mi>n</mi></msub><mo stretchy=\"false\">)</mo><mo>≤</mo><mi>f</mi><mo stretchy=\"false\">(</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">f(a_n)\\le f(a_{n+1})</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>≤</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub></mrow><annotation encoding=\"application/x-tex\">a_{n+1}\\le a_{n+2}</annotation></semantics></math></span>.</p>\n    <div class=\"lesson-rule\">🔑 שיטה ב עובדת רק אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> <b>עולה</b> (על התחום שבו נמצאים האיברים). אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> יורדת, למשל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">f(x)=\\frac1x</annotation></semantics></math></span>, אי-השוויון מתהפך והסדרה מתנודדת.</div>\n    <div class=\"lesson-ex\"><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>6</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\sqrt{a_n+6}</annotation></semantics></math></span>. בסיס: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><msqrt><mn>7</mn></msqrt><mo>&gt;</mo><mn>1</mn><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_2=\\sqrt7&gt;1=a_1</annotation></semantics></math></span>. הנחה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><annotation encoding=\"application/x-tex\">a_n&lt;a_{n+1}</annotation></semantics></math></span>. אז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>6</mn><mo>&lt;</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>+</mo><mn>6</mn></mrow><annotation encoding=\"application/x-tex\">a_n+6&lt;a_{n+1}+6</annotation></semantics></math></span> ובשורש (שעולה) <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>&lt;</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub></mrow><annotation encoding=\"application/x-tex\">a_{n+1}&lt;a_{n+2}</annotation></semantics></math></span>.</div>\n    <div class=\"lesson-trap\">⚠️ בשיטת ההפרש מקבלים ביטוי שהסימן שלו תלוי ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding=\"application/x-tex\">a_n</annotation></semantics></math></span>. אם לא הוכחתם חסם על <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding=\"application/x-tex\">a_n</annotation></semantics></math></span>, אי אפשר להכריע את הסימן.</div>"
    },
    "questions": [
     {
      "id": "C04-Q1",
      "question": "באיזו סדרה אפשר להוכיח מונוטוניות באינדוקציה בעזרת \"הפעלת $f$ על אי-שוויון\" (כלומר $f$ עולה על האיברים)?",
      "options": [
       {
        "id": "a",
        "value": "$a_{n+1}=\\sqrt{a_n+3}$, $a_1=1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>3</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_{n+1}=\\sqrt{a_n+3}</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$a_{n+1}=\\frac{4}{a_n+1}$, $a_1=1$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mn>4</mn><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">a_{n+1}=\\frac{4}{a_n+1}</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_1=1</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$a_{n+1}=2-a_n$, $a_1=0$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding=\"application/x-tex\">a_{n+1}=2-a_n</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">a_1=0</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$a_{n+1}=\\frac{1}{a_n}$, $a_1=2$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mn>1</mn><msub><mi>a</mi><mi>n</mi></msub></mfrac></mrow><annotation encoding=\"application/x-tex\">a_{n+1}=\\frac{1}{a_n}</annotation></semantics></math></span>, <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_1=2</annotation></semantics></math></span>"
       }
      ],
      "correctId": "a",
      "explanation": "רק $f(x)=\\sqrt{x+3}$ עולה. ב-$\\frac{4}{x+1}$, ב-$2-x$ וב-$\\frac1x$ הפונקציה יורדת, ולכן הפעלתה מהפכת את האי-שוויון.",
      "recap": "אינדוקציה על מונוטוניות מחייבת f עולה",
      "questionHtml": "באיזו סדרה אפשר להוכיח מונוטוניות באינדוקציה בעזרת \"הפעלת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> על אי-שוויון\" (כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span> עולה על האיברים)?",
      "explanationHtml": "רק <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi><mo stretchy=\"false\">(</mo><mi>x</mi><mo stretchy=\"false\">)</mo><mo>=</mo><msqrt><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">f(x)=\\sqrt{x+3}</annotation></semantics></math></span> עולה. ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>4</mn><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{4}{x+1}</annotation></semantics></math></span>, ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>−</mo><mi>x</mi></mrow><annotation encoding=\"application/x-tex\">2-x</annotation></semantics></math></span> וב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac1x</annotation></semantics></math></span> הפונקציה יורדת, ולכן הפעלתה מהפכת את האי-שוויון.",
      "recapHtml": "אינדוקציה על מונוטוניות מחייבת f עולה"
     },
     {
      "id": "C04-Q2",
      "step": {
       "type": "numeric",
       "prompt": "נתונה $a_1=1,\\ a_{n+1}=\\sqrt{a_n+6}$. מהו $a_2$ ? (עיגול לשלוש ספרות אחרי הנקודה)",
       "answer": 2.646,
       "tol": 0.001,
       "explain": "$a_2=\\sqrt{1+6}=\\sqrt7\\approx2.646>1=a_1$. זה בסיס האינדוקציה $a_1<a_2$.",
       "promptHtml": "נתונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>6</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\sqrt{a_n+6}</annotation></semantics></math></span>. מהו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_2</annotation></semantics></math></span> ? (עיגול לשלוש ספרות אחרי הנקודה)",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><msqrt><mrow><mn>1</mn><mo>+</mo><mn>6</mn></mrow></msqrt><mo>=</mo><msqrt><mn>7</mn></msqrt><mo>≈</mo><mn>2.646</mn><mo>&gt;</mo><mn>1</mn><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_2=\\sqrt{1+6}=\\sqrt7\\approx2.646&gt;1=a_1</annotation></semantics></math></span>. זה בסיס האינדוקציה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>&lt;</mo><msub><mi>a</mi><mn>2</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_1&lt;a_2</annotation></semantics></math></span>."
      },
      "recap": "בסיס: משווים את a_1 ל-a_2",
      "recapHtml": "בסיס: משווים את a_1 ל-a_2"
     },
     {
      "id": "C04-Q3",
      "step": {
       "type": "order",
       "prompt": "סדרו את ההוכחה ש-$a_n<a_{n+1}$ לכל $n$ עבור $a_1=1,\\ a_{n+1}=\\sqrt{a_n+6}$.",
       "lines": [
        "בסיס: $a_1=1<\\sqrt7=a_2$",
        "הנחה: $a_n<a_{n+1}$",
        "מוסיפים 6: $a_n+6<a_{n+1}+6$",
        "השורש עולה, לכן $\\sqrt{a_n+6}<\\sqrt{a_{n+1}+6}$",
        "כלומר $a_{n+1}<a_{n+2}$"
       ],
       "explain": "הצעד מפעיל על ההנחה בדיוק את הפעולות של $f$: הוספת $6$ ואחר כך שורש.",
       "promptHtml": "סדרו את ההוכחה ש-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><annotation encoding=\"application/x-tex\">a_n&lt;a_{n+1}</annotation></semantics></math></span> לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span> עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>6</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\sqrt{a_n+6}</annotation></semantics></math></span>.",
       "explainHtml": "הצעד מפעיל על ההנחה בדיוק את הפעולות של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>f</mi></mrow><annotation encoding=\"application/x-tex\">f</annotation></semantics></math></span>: הוספת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>6</mn></mrow><annotation encoding=\"application/x-tex\">6</annotation></semantics></math></span> ואחר כך שורש.",
       "linesHtml": [
        "בסיס: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>&lt;</mo><msqrt><mn>7</mn></msqrt><mo>=</mo><msub><mi>a</mi><mn>2</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_1=1&lt;\\sqrt7=a_2</annotation></semantics></math></span>",
        "הנחה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><annotation encoding=\"application/x-tex\">a_n&lt;a_{n+1}</annotation></semantics></math></span>",
        "מוסיפים 6: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>6</mn><mo>&lt;</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>+</mo><mn>6</mn></mrow><annotation encoding=\"application/x-tex\">a_n+6&lt;a_{n+1}+6</annotation></semantics></math></span>",
        "השורש עולה, לכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msqrt><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>6</mn></mrow></msqrt><mo>&lt;</mo><msqrt><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>+</mo><mn>6</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">\\sqrt{a_n+6}&lt;\\sqrt{a_{n+1}+6}</annotation></semantics></math></span>",
        "כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>&lt;</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub></mrow><annotation encoding=\"application/x-tex\">a_{n+1}&lt;a_{n+2}</annotation></semantics></math></span>"
       ]
      },
      "recap": "בסיס, הנחה, הפעלת f על ההנחה",
      "recapHtml": "בסיס, הנחה, הפעלת f על ההנחה"
     },
     {
      "id": "C04-Q4",
      "question": "עבור $a_{n+1}=\\frac{a_n}{2}+1$, מהו ההפרש $a_{n+1}-a_n$ ?",
      "options": [
       {
        "id": "a",
        "value": "$\\frac{a_n-2}{2}$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>−</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{a_n-2}{2}</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "$\\frac{2-a_n}{2}$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><mn>2</mn><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><mn>2</mn></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{2-a_n}{2}</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "$1+\\frac{a_n}{2}$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>+</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac></mrow><annotation encoding=\"application/x-tex\">1+\\frac{a_n}{2}</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "$\\frac{a_n}{2}$",
        "type": "text",
        "html": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{a_n}{2}</annotation></semantics></math></span>"
       }
      ],
      "correctId": "b",
      "explanation": "$\\frac{a_n}{2}+1-a_n=1-\\frac{a_n}{2}=\\frac{2-a_n}{2}$. הביטוי $\\frac{a_n-2}{2}$ הוא ההפרש בסימן הפוך.",
      "recap": "מחסרים את a_n ומאחדים",
      "questionHtml": "עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_{n+1}=\\frac{a_n}{2}+1</annotation></semantics></math></span>, מהו ההפרש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding=\"application/x-tex\">a_{n+1}-a_n</annotation></semantics></math></span> ?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>1</mn><mo>−</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><mn>2</mn></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{a_n}{2}+1-a_n=1-\\frac{a_n}{2}=\\frac{2-a_n}{2}</annotation></semantics></math></span>. הביטוי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>−</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{a_n-2}{2}</annotation></semantics></math></span> הוא ההפרש בסימן הפוך.",
      "recapHtml": "מחסרים את a_n ומאחדים"
     },
     {
      "id": "C04-Q5",
      "question": "נתונה $a_1=10,\\ a_{n+1}=\\frac{a_n}{2}+1$. כבר הוכחנו $a_n>2$ לכל $n$. מה מסיקים מהפרש $\\frac{2-a_n}{2}$ ?",
      "options": [
       {
        "id": "a",
        "value": "הסדרה עולה וחסומה מלמעלה",
        "type": "text",
        "html": "הסדרה עולה וחסומה מלמעלה"
       },
       {
        "id": "b",
        "value": "הסדרה יורדת וחסומה מלמטה, ולכן מתכנסת",
        "type": "text",
        "html": "הסדרה יורדת וחסומה מלמטה, ולכן מתכנסת"
       },
       {
        "id": "c",
        "value": "הסדרה עולה וחסומה מלמטה, ולכן מתכנסת",
        "type": "text",
        "html": "הסדרה עולה וחסומה מלמטה, ולכן מתכנסת"
       },
       {
        "id": "d",
        "value": "אי אפשר להכריע את הסימן",
        "type": "text",
        "html": "אי אפשר להכריע את הסימן"
       }
      ],
      "correctId": "b",
      "explanation": "מ-$a_n>2$ ההפרש $\\frac{2-a_n}{2}<0$, ולכן $a_{n+1}<a_n$: הסדרה יורדת. יחד עם החסם $a_n>2$ היא חסומה מלמטה ולכן מתכנסת. אילולא החסם, הסימן לא היה ידוע.",
      "recap": "הסימן של ההפרש נקבע על ידי החסם",
      "questionHtml": "נתונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>10</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_1=10,\\ a_{n+1}=\\frac{a_n}{2}+1</annotation></semantics></math></span>. כבר הוכחנו <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&gt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n&gt;2</annotation></semantics></math></span> לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span>. מה מסיקים מהפרש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><mn>2</mn><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><mn>2</mn></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{2-a_n}{2}</annotation></semantics></math></span> ?",
      "explanationHtml": "מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&gt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n&gt;2</annotation></semantics></math></span> ההפרש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><mn>2</mn><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><mn>2</mn></mfrac><mo>&lt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">\\frac{2-a_n}{2}&lt;0</annotation></semantics></math></span>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>&lt;</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding=\"application/x-tex\">a_{n+1}&lt;a_n</annotation></semantics></math></span>: הסדרה יורדת. יחד עם החסם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&gt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n&gt;2</annotation></semantics></math></span> היא חסומה מלמטה ולכן מתכנסת. אילולא החסם, הסימן לא היה ידוע.",
      "recapHtml": "הסימן של ההפרש נקבע על ידי החסם"
     },
     {
      "id": "C04-Q6",
      "step": {
       "type": "findbug",
       "prompt": "עבור $a_{n+1}=\\sqrt{2+a_n}$ ו-$0<a_n<2$ נבדקת מונוטוניות דרך ההפרש של הריבועים. בשורה אחת יש שגיאה. איזו?",
       "lines": [
        "$a_{n+1}^2-a_n^2=2+a_n-a_n^2$",
        "$=(a_n-2)(a_n+1)$",
        "מ-$0<a_n<2$ נובע שהגורם $2-a_n$ חיובי וגם $a_n+1$ חיובי",
        "לכן $a_{n+1}^2>a_n^2$, ומכיוון שהאיברים חיוביים $a_{n+1}>a_n$"
       ],
       "bugIndex": 1,
       "explain": "$2+a-a^2=-(a^2-a-2)=-(a-2)(a+1)=(2-a)(a+1)$. השורה השנייה כתבה $(a-2)(a+1)$, שהוא הפוך בסימן ($(a-2)(a+1)=a^2-a-2$).",
       "promptHtml": "עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_{n+1}=\\sqrt{2+a_n}</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn><mo>&lt;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">0&lt;a_n&lt;2</annotation></semantics></math></span> נבדקת מונוטוניות דרך ההפרש של הריבועים. בשורה אחת יש שגיאה. איזו?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>+</mo><mi>a</mi><mo>−</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mo>−</mo><mo stretchy=\"false\">(</mo><msup><mi>a</mi><mn>2</mn></msup><mo>−</mo><mi>a</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo>−</mo><mo stretchy=\"false\">(</mo><mi>a</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mo stretchy=\"false\">(</mo><mn>2</mn><mo>−</mo><mi>a</mi><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">2+a-a^2=-(a^2-a-2)=-(a-2)(a+1)=(2-a)(a+1)</annotation></semantics></math></span>. השורה השנייה כתבה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>a</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(a-2)(a+1)</annotation></semantics></math></span>, שהוא הפוך בסימן (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>a</mi><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>−</mo><mi>a</mi><mo>−</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">(a-2)(a+1)=a^2-a-2</annotation></semantics></math></span>).",
       "linesHtml": [
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msubsup><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></msubsup><mo>−</mo><msubsup><mi>a</mi><mi>n</mi><mn>2</mn></msubsup><mo>=</mo><mn>2</mn><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub><mo>−</mo><msubsup><mi>a</mi><mi>n</mi><mn>2</mn></msubsup></mrow><annotation encoding=\"application/x-tex\">a_{n+1}^2-a_n^2=2+a_n-a_n^2</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>=</mo><mo stretchy=\"false\">(</mo><msub><mi>a</mi><mi>n</mi></msub><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">=(a_n-2)(a_n+1)</annotation></semantics></math></span>",
        "מ-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn><mo>&lt;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>&lt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">0&lt;a_n&lt;2</annotation></semantics></math></span> נובע שהגורם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>−</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding=\"application/x-tex\">2-a_n</annotation></semantics></math></span> חיובי וגם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">a_n+1</annotation></semantics></math></span> חיובי",
        "לכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msubsup><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></msubsup><mo>&gt;</mo><msubsup><mi>a</mi><mi>n</mi><mn>2</mn></msubsup></mrow><annotation encoding=\"application/x-tex\">a_{n+1}^2&gt;a_n^2</annotation></semantics></math></span>, ומכיוון שהאיברים חיוביים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>&gt;</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding=\"application/x-tex\">a_{n+1}&gt;a_n</annotation></semantics></math></span>"
       ]
      },
      "recap": "בודקים את הפירוק לגורמים על ידי פתיחה",
      "recapHtml": "בודקים את הפירוק לגורמים על ידי פתיחה"
     }
    ]
   },
   {
    "id": "C05",
    "order": 5,
    "icon": "🧩",
    "title": "ההוכחה המלאה: סדרות שורש",
    "goal": "להרכיב הוכחת התכנסות שלמה לסדרה עם שורש ולבחור את הגבול הנכון.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>עכשיו מחברים את שלוש הרמות הקודמות להוכחה אחת. <b>משפט היסוד:</b> סדרה עולה וחסומה מלמעלה מתכנסת, וסדרה יורדת וחסומה מלמטה מתכנסת.</p>\n    <table><thead><tr><th>שלב</th><th>מה עושים</th></tr></thead><tbody>\n      <tr><td>1. ניחוש</td><td>מחשבים איברים ופותרים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>L</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">L=f(L)</annotation></semantics></math></span></td></tr>\n      <tr><td>2. חסימה</td><td>אינדוקציה עם חסם שהוא נקודת שבת, ובדיקה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub></mrow><annotation encoding=\"application/x-tex\">a_1</annotation></semantics></math></span></td></tr>\n      <tr><td>3. מונוטוניות</td><td>הפרש (עם החסם) או אינדוקציה</td></tr>\n      <tr><td>4. משפט היסוד</td><td>הגבול <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">L</annotation></semantics></math></span> קיים</td></tr>\n      <tr><td>5. חישוב</td><td><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>L</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">L=f(L)</annotation></semantics></math></span> ובחירת השורש לפי החסם והכיוון</td></tr>\n    </tbody></table>\n    <div class=\"lesson-ex\"><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>12</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=2,\\ a_{n+1}=\\sqrt{a_n+12}</annotation></semantics></math></span>. נקודות שבת: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>=</mo><mi>L</mi><mo>+</mo><mn>12</mn></mrow><annotation encoding=\"application/x-tex\">L^2=L+12</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>L</mi><mo>−</mo><mn>4</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>L</mi><mo>+</mo><mn>3</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">(L-4)(L+3)=0</annotation></semantics></math></span>.<br>\n    חסם: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\le4</annotation></semantics></math></span> (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>≤</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_1=2\\le4</annotation></semantics></math></span>; <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≤</mo><mn>4</mn><mo>⇒</mo><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>12</mn><mo>≤</mo><mn>16</mn><mo>⇒</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>≤</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\le4\\Rightarrow a_n+12\\le16\\Rightarrow a_{n+1}\\le4</annotation></semantics></math></span>). עולה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><msqrt><mn>14</mn></msqrt><mo>&gt;</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_2=\\sqrt{14}&gt;2</annotation></semantics></math></span> והשורש עולה.<br>\n    לכן קיים גבול, ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">L=4</annotation></semantics></math></span> כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">L=-3</annotation></semantics></math></span> אינו אפשרי (האיברים חיוביים, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">L\\ge0</annotation></semantics></math></span>).</div>\n    <div class=\"lesson-rule\">🔑 את השורש השלילי פוסלים בנימוק: <b>גבול שומר על אי-שוויון חלש</b>. אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\ge0</annotation></semantics></math></span> לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span> אז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">L\\ge0</annotation></semantics></math></span>. (אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≥</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\ge2</annotation></semantics></math></span> אז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>≥</mo><mn>2</mn></mrow><annotation encoding=\"application/x-tex\">L\\ge2</annotation></semantics></math></span>.)</div>\n    <div class=\"lesson-trap\">⚠️ אסור לכתוב <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>L</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">L=f(L)</annotation></semantics></math></span> לפני שמשפט היסוד הבטיח שהגבול קיים. סדר ההוכחה: חסימה, מונוטוניות, משפט, רק אז חישוב.</div>"
    },
    "questions": [
     {
      "id": "C05-Q1",
      "question": "מה הסדר הנכון בהוכחת התכנסות של סדרה רקורסיבית?",
      "options": [
       {
        "id": "a",
        "value": "לפתור $L=f(L)$, ואז להסיק שהסדרה מתכנסת",
        "type": "text",
        "html": "לפתור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>L</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">L=f(L)</annotation></semantics></math></span>, ואז להסיק שהסדרה מתכנסת"
       },
       {
        "id": "b",
        "value": "להוכיח חסימה ומונוטוניות, להפעיל את משפט היסוד, ורק אז לפתור $L=f(L)$",
        "type": "text",
        "html": "להוכיח חסימה ומונוטוניות, להפעיל את משפט היסוד, ורק אז לפתור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>L</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">L=f(L)</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "לחשב שלושה איברים ולהסיק שהסדרה מתכנסת",
        "type": "text",
        "html": "לחשב שלושה איברים ולהסיק שהסדרה מתכנסת"
       },
       {
        "id": "d",
        "value": "לפתור $L=f(L)$, ואז להוכיח חסימה",
        "type": "text",
        "html": "לפתור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>L</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">L=f(L)</annotation></semantics></math></span>, ואז להוכיח חסימה"
       }
      ],
      "correctId": "b",
      "explanation": "המשוואה $L=f(L)$ מניחה שהגבול קיים, ולכן היא מגיעה אחרי משפט היסוד. פתרון המשוואה לבדו או כמה איברים אינם הוכחה.",
      "recap": "חסימה, מונוטוניות, משפט, ואז L=f(L)",
      "questionHtml": "מה הסדר הנכון בהוכחת התכנסות של סדרה רקורסיבית?",
      "explanationHtml": "המשוואה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mi>f</mi><mo stretchy=\"false\">(</mo><mi>L</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">L=f(L)</annotation></semantics></math></span> מניחה שהגבול קיים, ולכן היא מגיעה אחרי משפט היסוד. פתרון המשוואה לבדו או כמה איברים אינם הוכחה.",
      "recapHtml": "חסימה, מונוטוניות, משפט, ואז L=f(L)"
     },
     {
      "id": "C05-Q2",
      "step": {
       "type": "numeric",
       "prompt": "הסדרה $a_1=2,\\ a_{n+1}=\\sqrt{a_n+12}$ עולה וחסומה מלמעלה. מהו הגבול?",
       "answer": 4,
       "tol": 0,
       "explain": "$L^2=L+12\\Rightarrow(L-4)(L+3)=0$. האיברים חיוביים ולכן $L=4$.",
       "promptHtml": "הסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>12</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=2,\\ a_{n+1}=\\sqrt{a_n+12}</annotation></semantics></math></span> עולה וחסומה מלמעלה. מהו הגבול?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>=</mo><mi>L</mi><mo>+</mo><mn>12</mn><mo>⇒</mo><mo stretchy=\"false\">(</mo><mi>L</mi><mo>−</mo><mn>4</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>L</mi><mo>+</mo><mn>3</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">L^2=L+12\\Rightarrow(L-4)(L+3)=0</annotation></semantics></math></span>. האיברים חיוביים ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">L=4</annotation></semantics></math></span>."
      },
      "recap": "פותרים L=f(L) ובוחרים את השורש החיובי",
      "recapHtml": "פותרים L=f(L) ובוחרים את השורש החיובי"
     },
     {
      "id": "C05-Q3",
      "question": "נתונה $a_1=7,\\ a_{n+1}=\\sqrt{a_n+12}$. מה נכון?",
      "options": [
       {
        "id": "a",
        "value": "יורדת ומתכנסת ל-$4$",
        "type": "text",
        "html": "יורדת ומתכנסת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">4</annotation></semantics></math></span>"
       },
       {
        "id": "b",
        "value": "עולה ומתכנסת ל-$4$",
        "type": "text",
        "html": "עולה ומתכנסת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">4</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "יורדת ומתכנסת ל-$-3$",
        "type": "text",
        "html": "יורדת ומתכנסת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">-3</annotation></semantics></math></span>"
       },
       {
        "id": "d",
        "value": "אינה מתכנסת",
        "type": "text",
        "html": "אינה מתכנסת"
       }
      ],
      "correctId": "a",
      "explanation": "$a_1=7>4$. אם $a_n\\ge4$ אז $a_{n+1}\\ge\\sqrt{16}=4$, ו-$a_2=\\sqrt{19}\\approx4.36<7$. הסדרה יורדת וחסומה מלמטה ב-$4$ ולכן מתכנסת, ו-$L=4$. הערך $-3$ נפסל כי $L\\ge4$.",
      "recap": "מעל נקודת השבת: יורדת אליה",
      "questionHtml": "נתונה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>7</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>12</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=7,\\ a_{n+1}=\\sqrt{a_n+12}</annotation></semantics></math></span>. מה נכון?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>7</mn><mo>&gt;</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_1=7&gt;4</annotation></semantics></math></span>. אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>≥</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_n\\ge4</annotation></semantics></math></span> אז <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>≥</mo><msqrt><mn>16</mn></msqrt><mo>=</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">a_{n+1}\\ge\\sqrt{16}=4</annotation></semantics></math></span>, ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><msqrt><mn>19</mn></msqrt><mo>≈</mo><mn>4.36</mn><mo>&lt;</mo><mn>7</mn></mrow><annotation encoding=\"application/x-tex\">a_2=\\sqrt{19}\\approx4.36&lt;7</annotation></semantics></math></span>. הסדרה יורדת וחסומה מלמטה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">4</annotation></semantics></math></span> ולכן מתכנסת, ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">L=4</annotation></semantics></math></span>. הערך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">-3</annotation></semantics></math></span> נפסל כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>≥</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">L\\ge4</annotation></semantics></math></span>.",
      "recapHtml": "מעל נקודת השבת: יורדת אליה"
     },
     {
      "id": "C05-Q4",
      "step": {
       "type": "findbug",
       "prompt": "בחישוב הגבול של $a_1=2,\\ a_{n+1}=\\sqrt{a_n+12}$ (אחרי שהוכח שהיא מתכנסת) יש שגיאה אחת. באיזו שורה?",
       "lines": [
        "נסמן $L=\\lim a_n$, ואז גם $a_{n+1}\\to L$",
        "$L=\\sqrt{L+12}$",
        "$L^2=L+12$",
        "$(L-4)(L+3)=0$",
        "הסדרה חיובית ולכן $L=-3$"
       ],
       "bugIndex": 4,
       "explain": "הסדרה חיובית ולכן הגבול אינו שלילי: $L=4$ ו-$L=-3$ נפסל.",
       "promptHtml": "בחישוב הגבול של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>12</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=2,\\ a_{n+1}=\\sqrt{a_n+12}</annotation></semantics></math></span> (אחרי שהוכח שהיא מתכנסת) יש שגיאה אחת. באיזו שורה?",
       "explainHtml": "הסדרה חיובית ולכן הגבול אינו שלילי: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">L=4</annotation></semantics></math></span> ו-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">L=-3</annotation></semantics></math></span> נפסל.",
       "linesHtml": [
        "נסמן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mi>lim</mi><mo>⁡</mo><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding=\"application/x-tex\">L=\\lim a_n</annotation></semantics></math></span>, ואז גם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>→</mo><mi>L</mi></mrow><annotation encoding=\"application/x-tex\">a_{n+1}\\to L</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><msqrt><mrow><mi>L</mi><mo>+</mo><mn>12</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">L=\\sqrt{L+12}</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>=</mo><mi>L</mi><mo>+</mo><mn>12</mn></mrow><annotation encoding=\"application/x-tex\">L^2=L+12</annotation></semantics></math></span>",
        "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>L</mi><mo>−</mo><mn>4</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>L</mi><mo>+</mo><mn>3</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">(L-4)(L+3)=0</annotation></semantics></math></span>",
        "הסדרה חיובית ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">L=-3</annotation></semantics></math></span>"
       ]
      },
      "recap": "פוסלים את השורש השלילי",
      "recapHtml": "פוסלים את השורש השלילי"
     },
     {
      "id": "C05-Q5",
      "question": "למה מותר לפסול את $L=-3$ כשכל איברי הסדרה חיוביים?",
      "options": [
       {
        "id": "a",
        "value": "כי $-3$ אינו שורש של המשוואה",
        "type": "text",
        "html": "כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">-3</annotation></semantics></math></span> אינו שורש של המשוואה"
       },
       {
        "id": "b",
        "value": "כי אם $a_n>0$ לכל $n$ אז הגבול $L\\ge0$",
        "type": "text",
        "html": "כי אם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">a_n&gt;0</annotation></semantics></math></span> לכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span> אז הגבול <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">L\\ge0</annotation></semantics></math></span>"
       },
       {
        "id": "c",
        "value": "כי תמיד בוחרים את השורש הגדול",
        "type": "text",
        "html": "כי תמיד בוחרים את השורש הגדול"
       },
       {
        "id": "d",
        "value": "כי ערך שלילי לא יכול להיות גבול של שום סדרה",
        "type": "text",
        "html": "כי ערך שלילי לא יכול להיות גבול של שום סדרה"
       }
      ],
      "correctId": "b",
      "explanation": "$-3$ הוא כן שורש של $L^2=L+12$ (אבל לא של $L=\\sqrt{L+12}$, שדורש $L\\ge0$). הנימוק הוא שגבול של איברים אי-שליליים אי-שלילי. \"תמיד הגדול\" אינו כלל, וסדרות יכולות להתכנס לערכים שליליים.",
      "recap": "גבול שומר על אי-שוויון חלש",
      "questionHtml": "למה מותר לפסול את <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">L=-3</annotation></semantics></math></span> כשכל איברי הסדרה חיוביים?",
      "explanationHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">-3</annotation></semantics></math></span> הוא כן שורש של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>=</mo><mi>L</mi><mo>+</mo><mn>12</mn></mrow><annotation encoding=\"application/x-tex\">L^2=L+12</annotation></semantics></math></span> (אבל לא של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><msqrt><mrow><mi>L</mi><mo>+</mo><mn>12</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">L=\\sqrt{L+12}</annotation></semantics></math></span>, שדורש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>≥</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">L\\ge0</annotation></semantics></math></span>). הנימוק הוא שגבול של איברים אי-שליליים אי-שלילי. \"תמיד הגדול\" אינו כלל, וסדרות יכולות להתכנס לערכים שליליים.",
      "recapHtml": "גבול שומר על אי-שוויון חלש"
     },
     {
      "id": "C05-Q6",
      "step": {
       "type": "numeric",
       "prompt": "הסדרה $a_1=1,\\ a_{n+1}=\\sqrt{3a_n+10}$ עולה וחסומה מלמעלה ב-$5$. מהו הגבול?",
       "answer": 5,
       "tol": 0,
       "explain": "$L^2=3L+10\\Rightarrow(L-5)(L+2)=0$. האיברים חיוביים, לכן $L=5$.",
       "promptHtml": "הסדרה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo separator=\"true\">,</mo><mtext> </mtext><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msqrt><mrow><mn>3</mn><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>10</mn></mrow></msqrt></mrow><annotation encoding=\"application/x-tex\">a_1=1,\\ a_{n+1}=\\sqrt{3a_n+10}</annotation></semantics></math></span> עולה וחסומה מלמעלה ב-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>5</mn></mrow><annotation encoding=\"application/x-tex\">5</annotation></semantics></math></span>. מהו הגבול?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mi>L</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mi>L</mi><mo>+</mo><mn>10</mn><mo>⇒</mo><mo stretchy=\"false\">(</mo><mi>L</mi><mo>−</mo><mn>5</mn><mo stretchy=\"false\">)</mo><mo stretchy=\"false\">(</mo><mi>L</mi><mo>+</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>=</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">L^2=3L+10\\Rightarrow(L-5)(L+2)=0</annotation></semantics></math></span>. האיברים חיוביים, לכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>L</mi><mo>=</mo><mn>5</mn></mrow><annotation encoding=\"application/x-tex\">L=5</annotation></semantics></math></span>."
      },
      "recap": "אותו מתכון: פותרים ובוחרים",
      "recapHtml": "אותו מתכון: פותרים ובוחרים"
     }
    ]
   }
  ]
 }
};

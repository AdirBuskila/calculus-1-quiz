# אינטגרל לא מסוים

## מה המבחן שואל
בכל מועד יש לפחות שני אינטגרלים לא מסוימים (ועוד כאלה בתוך שאלות נפח ושטח). הסוגים שהופיעו:
- **שברים חלקיים:** $\int\frac{2x^2+x+4}{(x+1)(x^2+4)}dx$, גורם כפול $\frac{x^2+2x+3}{(x-1)(x+2)^2}$, ו-$\frac{x^2+8}{x^2(x^2+4)}$. בבנק: `24B-B-Q2a`.
- **הצבה:** $\int\frac{dx}{x(\ln^2x+2\ln x+5)}$, $\int\frac{\sin2x}{3+\cos^22x}dx$, $\int x\cos(x^2)dx$, $\int\frac{\ln x}{x(\ln^2x+1)}dx$. בבנק: `24B-B-Q5b`.
- **אינטגרציה בחלקים:** $\int(x^2+2x)\cos2x\,dx$, $\int(4x+6)\arctan x\,dx$, ולעיתים אחרי הצבה ($\int x\arctan(x^2)dx$).
- **הצבה אוניברסלית** $t=\tan\frac x2$: $\int\frac{dx}{2+\cos x}$, $\int\frac{dx}{1+\sin x+3\cos x}$.
- **מנה של פולינומים עם דרגת מונה גדולה או שווה:** $\int\frac{x^3-2x}{x^2+1}dx$ (חלוקה ארוכה קודם).
- **ביטוי באקספוננט:** $\int\frac{e^{-x}-e^x}{e^{-x}+e^x}dx$.

## טבלת היסוד (דף הנוסחאות)
$$\int x^\alpha dx=\frac{x^{\alpha+1}}{\alpha+1}\ (\alpha\ne-1),\quad \int\frac{dx}{x}=\ln|x|,\quad \int a^xdx=\frac{a^x}{\ln a}$$
$$\int\sin x=-\cos x,\quad \int\cos x=\sin x,\quad \int\frac{dx}{\cos^2x}=\tan x,\quad \int\frac{dx}{\sin^2x}=-\cot x$$
$$\int\frac{dx}{\sqrt{a^2-x^2}}=\arcsin\frac xa,\quad \int\frac{dx}{a^2+x^2}=\frac1a\arctan\frac xa,\quad \int\frac{dx}{a^2-x^2}=\frac{1}{2a}\ln\left|\frac{a+x}{a-x}\right|$$
$$\int\tan x\,dx=-\ln|\cos x|,\quad \int\frac{dx}{\sin x}=\ln\left|\tan\frac x2\right|$$
**בחלקים:** $\int u\,dv=uv-\int v\,du$.
**הצבה אוניברסלית:** $t=\tan\frac x2$ נותנת $\sin x=\frac{2t}{1+t^2}$, $\cos x=\frac{1-t^2}{1+t^2}$, $dx=\frac{2\,dt}{1+t^2}$.

## איך בוחרים שיטה
| מה רואים | מה עושים |
|---|---|
| מונה הוא נגזרת המכנה: $\frac{f'}{f}$ | $\ln\lvert f\rvert+C$ ישר |
| פונקציה ונגזרתה (כמו $\frac{\ln x}{x}$, $x\cos x^2$, $\sin2x\cdot g(\cos 2x)$) | הצבה $t=$ הפונקציה הפנימית |
| מנה של פולינומים | דרגת מונה $\ge$ דרגת מכנה: חלוקה. אחר כך שברים חלקיים |
| מכנה ריבועי שלא מתפרק | השלמה לריבוע, ואז $\arctan$ |
| מכפלה של פולינום ב-$e^x$, $\sin$, $\cos$ | בחלקים, $u=$ הפולינום (חוזרים עד שמתאפס) |
| $\ln x$ או $\arctan x$ לבד או כפול פולינום | בחלקים, $u=\ln x$ או $\arctan x$, ו-$dv=$ שאר |
| רציונלי ב-$\sin,\cos$ | קודם נסו $t=\cos x$ אם יש $\sin x\,dx$ בגורם, אחרת $t=\tan\frac x2$ |
| רציונלי ב-$e^x$ | $t=e^x$ |
| שורש של $x$ בתוך הביטוי | $t=\sqrt x$ |
| $\arctan\sqrt x$ עם $\frac{dx}{(1+x)\sqrt x}$ | $t=\arctan\sqrt x$ (הנגזרת של $\arctan\sqrt x$ היא $\frac{1}{2(1+x)\sqrt x}$) |

## שברים חלקיים: כללים
- אחרי חלוקה, פרקו את המכנה לגורמים אי-פריקים (לינארי או ריבועי עם דיסקרימיננטה שלילית).
- לגורם לינארי $(x-r)$: $\frac{A}{x-r}$. לגורם $(x-r)^2$: $\frac{A}{x-r}+\frac{B}{(x-r)^2}$. לגורם ריבועי: $\frac{Bx+C}{x^2+px+q}$.
- המקדמים: הצבת שורשים, או השוואת מקדמים.
- את $\frac{Bx+C}{x^2+k}$ מפרקים לשני חלקים: $\frac B2\cdot\frac{2x}{x^2+k}\to\frac B2\ln(x^2+k)$ ו-$\frac{C}{x^2+k}\to\frac{C}{\sqrt k}\arctan\frac{x}{\sqrt k}$.

## השלמה לריבוע
$x^2+2x+5=(x+1)^2+4$, ולכן $\int\frac{dx}{x^2+2x+5}=\frac12\arctan\frac{x+1}{2}+C$.

> 🪤 לשכוח $+C$, וערך מוחלט ב-$\ln|\cdot|$.

> 🪤 הצבה בלי להמיר את $dx$ ואת כל ה-$x$ שנשארו. בהצבה באינטגרל מסוים צריך להמיר גם את הגבולות.

> 🪤 שברים חלקיים כשדרגת המונה גדולה או שווה למכנה: חובה קודם חלוקה.

> 🪤 גורם כפול במכנה דורש **שני** איברים ($\frac{A}{x+2}$ ו-$\frac{B}{(x+2)^2}$), לא איבר אחד.

> 🪤 בחלקים: בחירה הפוכה של $u,dv$ מסבכת. $\ln$ ו-$\arctan$ הם תמיד $u$, כי הנגזרת שלהם פשוטה.

> 🪤 $\int\frac{dx}{x^2+4}$ הוא $\frac12\arctan\frac x2$ ולא $\arctan\frac x2$. פקטור $\frac1a$.

> ⚠️ בדקו את התשובה בגזירה כשיש זמן. זה הדרך הבטוחה ביותר.

## חזקות של sin ו-cos, ו-tan
- **חזקה אי-זוגית של $\sin$** ($\int\sin^5x\,dx$, $\int\frac{\sin^3x}{\cos^4x}dx$): פורקים גורם $\sin x$ אחד, מחליפים את השאר ל-$\cos$ בעזרת $\sin^2x=1-\cos^2x$, ומציבים $t=\cos x$ (אז $dt=-\sin x\,dx$). באותו אופן חזקה אי-זוגית של $\cos$ עם $t=\sin x$.
- **ביטוי ב-$\tan x$ או ב-$\cos^2x$ בלבד** ($\int\frac{dx}{\cos^2x+4\cos^4x}$): מחלקים מונה ומכנה ב-$\cos^4x$ ומציבים $t=\tan x$, כי $dt=\frac{dx}{\cos^2x}$ ו-$\frac{1}{\cos^2x}=1+t^2$.
- **חזקה זוגית** ($\int\sin^2x\,dx$): נוסחאות זווית כפולה, $\sin^2x=\frac{1-\cos2x}{2}$.

## דוגמה פתורה
$\int\frac{x+3}{(x-1)(x+1)}dx$. פירוק $\frac{A}{x-1}+\frac{B}{x+1}$ עם $x+3=A(x+1)+B(x-1)$. הצבת $x=1$ נותנת $A=2$ והצבת $x=-1$ נותנת $B=-1$. התשובה: $2\ln|x-1|-\ln|x+1|+C$.

בחלקים: $\int xe^x\,dx=xe^x-\int e^xdx=(x-1)e^x+C$.

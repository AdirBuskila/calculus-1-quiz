# דף נוסחאות ומשפטים לכל הקורס

דף חוזר מרוכז, בנוי על דף הנוסחאות המורחב ועל דף כללי הנגזרות של הקורס, ומוסיף את המשפטים והתנאים שלהם.

## גבולות יסוד
$$\lim_{x\to0}\frac{\sin x}{x}=1,\quad \lim_{x\to0}\frac{\ln(1+x)}{x}=1,\quad \lim_{x\to\infty}\left(1+\frac1x\right)^x=e$$
$$\lim_{x\to0}\frac{a^x-1}{x}=\ln a,\quad \lim_{x\to0}\frac{(1+x)^p-1}{x}=p$$
צורת $1^\infty$: $\lim f^g=e^{\lim g(f-1)}$ כש-$f\to1$ ו-$g\to\infty$. $0^0,\infty^0$: דרך $e^{g\ln f}$. פרטים ב-[[function_limits]].

שקילויות ל-$u\to0$: $\sin u\sim\tan u\sim\arcsin u\sim\arctan u\sim u$, $e^u-1\sim u$, $\ln(1+u)\sim u$, $1-\cos u\sim\frac{u^2}{2}$. רק במכפלה ובמנה.

## סדרות
- עולה וחסומה מלמעלה מתכנסת. יורדת וחסומה מלמטה מתכנסת. ([[sequences_limits]])
- סנדוויץ'. חסומה כפול אפסה היא אפסה.
- $\frac{a+b}{2}\ge\sqrt{ab}$. סדר גדילה: $\ln n\ll n^p\ll q^n\ll n!\ll n^n$.
- רקורסיה: חסימה באינדוקציה, מונוטוניות, משפט, ואז $L=f(L)$ ובחירת שורש.

## רציפות
$\lim_{x\to x_0^-}f=\lim_{x\to x_0^+}f=f(x_0)$. סליקה: גבולות שווים, ערך שונה. ממין ראשון: גבולות סופיים שונים. ממין שני: גבול חד-צדדי אינסופי או לא קיים. ([[continuity]])
- ערך הביניים: רציפה ב-$[a,b]$, $f(a)f(b)<0$, אז קיים שורש. יחידות: $f'>0$ או $f'<0$.
- ויירשטראס: רציפה בקטע סגור מקבלת מקסימום ומינימום.

## נגזרות (כללים וטבלה)
$$(fg)'=f'g+fg',\quad \left(\frac fg\right)'=\frac{f'g-fg'}{g^2},\quad \left(f(g)\right)'=f'(g)g'$$
$$(x^\alpha)'=\alpha x^{\alpha-1},\quad (a^x)'=a^x\ln a,\quad (e^x)'=e^x,\quad (\ln x)'=\frac1x,\quad (\log_ax)'=\frac{1}{x\ln a}$$
$$(\sin x)'=\cos x,\quad (\cos x)'=-\sin x,\quad (\tan x)'=\frac{1}{\cos^2x},\quad (\cot x)'=-\frac{1}{\sin^2x}$$
$$(\arcsin x)'=\frac{1}{\sqrt{1-x^2}},\quad (\arccos x)'=-\frac{1}{\sqrt{1-x^2}},\quad (\arctan x)'=\frac{1}{1+x^2},\quad (\mathrm{arccot}\,x)'=-\frac{1}{1+x^2}$$
גזירה לוגריתמית: $y=f^g\Rightarrow y'=y\left(g'\ln f+g\frac{f'}{f}\right)$. גזירות בנקודה: רציפות ושוויון נגזרות חד-צדדיות. ([[derivatives_tangents]])

משיק: $y-f(x_0)=f'(x_0)(x-x_0)$. נורמל: $y-f(x_0)=-\frac{1}{f'(x_0)}(x-x_0)$.

## משפטי הערך הממוצע
תנאים: רציפה ב-$[a,b]$, גזירה ב-$(a,b)$.
- רול: $f(a)=f(b)\Rightarrow\exists c:\ f'(c)=0$.
- לגרנז': $\frac{f(b)-f(a)}{b-a}=f'(c)$.
- קושי: $\frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f'(c)}{g'(c)}$.
- $f'>0$ גורר עולה ממש. אי-שוויונות: לגרנז' עם חסם על $f'(c)$, או פונקציית עזר. ([[mean_value_theorems]])

## לופיטל וטיילור
- לופיטל: $\frac00$ או $\frac\infty\infty$, ו-$\lim\frac{f'}{g'}$ קיים, אז $\lim\frac fg=\lim\frac{f'}{g'}$. ([[lhopital_taylor]])
- $\frac{d}{dx}\int_0^{u(x)}g(t)dt=g(u(x))u'(x)$.
- טיילור: $f(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k+\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$, $c$ בין $a$ ל-$x$.
- $e^x=\sum\frac{x^k}{k!}$, $\sin x=x-\frac{x^3}{6}+\dots$, $\cos x=1-\frac{x^2}{2}+\dots$, $\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\dots$, $(1+x)^p=1+px+\frac{p(p-1)}{2}x^2+\dots$

## חקירת פונקציה ([[function_investigation]])
תחום, חיתוכים, $f'$ (עלייה/ירידה, קיצון), $f''$ (קמירות, פיתול), אסימפטוטות, שרטוט.
- $f''>0$: קעורה כלפי מעלה (הסימון בקורס). $f''<0$: קמורה כלפי מטה.
- אנכית: גבול חד-צדדי אינסופי. אופקית: $\lim_{x\to\pm\infty}f=L$.
- משופעת: $a=\lim\frac{f}{x}$, $b=\lim(f-ax)$ (כל צד בנפרד).

## קיצון ([[extrema_optimization]])
בקטע סגור: ערכי $f$ בקצוות, בנקודות $f'=0$ ובנקודות שבהן $f'$ לא קיימת, ובוחרים. פרמה: קיצון פנימי גזיר גורר $f'=0$. מבחן שני: $f'(x_0)=0$ ו-$f''>0$ מינימום, $f''<0$ מקסימום.

## אינטגרלים ([[indefinite_integrals]])
$$\int x^\alpha dx=\frac{x^{\alpha+1}}{\alpha+1},\ \int\frac{dx}{x}=\ln|x|,\ \int a^xdx=\frac{a^x}{\ln a},\ \int\tan x\,dx=-\ln|\cos x|,\ \int\cot x\,dx=\ln|\sin x|$$
$$\int\frac{dx}{a^2+x^2}=\frac1a\arctan\frac xa,\quad \int\frac{dx}{\sqrt{a^2-x^2}}=\arcsin\frac xa,\quad \int\frac{dx}{a^2-x^2}=\frac{1}{2a}\ln\left|\frac{a+x}{a-x}\right|$$
$$\int\frac{dx}{\sqrt{x^2+a}}=\ln\left|x+\sqrt{x^2+a}\right|,\quad \int\frac{dx}{\sin x}=\ln\left|\tan\frac x2\right|,\quad \int\frac{dx}{\cos x}=\ln\left|\tan\left(\frac x2+\frac\pi4\right)\right|$$
$$\int u\,dv=uv-\int v\,du,\qquad t=\tan\frac x2:\ \sin x=\frac{2t}{1+t^2},\ \cos x=\frac{1-t^2}{1+t^2},\ dx=\frac{2dt}{1+t^2}$$
שברים חלקיים: גורם לינארי $\frac{A}{x-r}$, גורם כפול $\frac{A}{x-r}+\frac{B}{(x-r)^2}$, גורם ריבועי $\frac{Bx+C}{x^2+k}$. דרגת מונה $\ge$ מכנה: חלוקה קודם.

## אינטגרל מסוים ושימושים ([[definite_integrals]])
$$S=\int_a^b(f-g)\,dx,\quad V_x=\pi\int_a^bf^2dx,\quad V_y=2\pi\int_a^bx\,f(x)\,dx,\quad L=\int_a^b\sqrt{1+(f')^2}\,dx$$
$$m(b-a)\le\int_a^bf\le M(b-a)$$
משפט הערך הממוצע לאינטגרל: $\int_a^bf=f(c)(b-a)$ עבור $c\in[a,b]$ ו-$f$ רציפה.

## זהויות טריגונומטריות
$$\sin^2x+\cos^2x=1,\quad 1+\tan^2x=\frac{1}{\cos^2x},\quad \sin2x=2\sin x\cos x,\quad \cos2x=\cos^2x-\sin^2x=2\cos^2x-1=1-2\sin^2x$$
$$\cos^2x=\frac{1+\cos2x}{2},\quad \sin^2x=\frac{1-\cos2x}{2}$$
$$\sin x\cos y=\tfrac12\left(\sin(x+y)+\sin(x-y)\right),\ \ \sin x\sin y=\tfrac12\left(\cos(x-y)-\cos(x+y)\right),\ \ \cos x\cos y=\tfrac12\left(\cos(x+y)+\cos(x-y)\right)$$

# Independent mpmath re-check of the numeric guided steps of 24B-A (the sympy values live in tools/gen/gen_24B-A.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sin, cos, tan, quad, diff, findroot, pi
from _steps_common import run
mp.dps = 30
f = lambda x: (x**3 - 1)/x**2
xc = findroot(lambda x: diff(f, x), -1.2)
xm = mpf('-1e-9'); xp = mpf('1e-9')
left = lambda b: sin(b*xm)/(xm + sin(2*xm))
den = lambda x: (x - 1) + x*log(x)
xa = 1 + mpf('1e-6'); lim4a = 1/log(xa) - 1/(xa - 1)
xb = mpf('1e-4'); lim4b = quad(tan, [0, xb])/(xb*sin(xb))
lim4b_den = sin(xb)/xb + cos(xb)
F = lambda x: ((x**2 + 2*x - mpf(1)/2)/2)*sin(2*x) + (x + 1)*cos(2*x)/2
definite = quad(lambda x: (x**2 + 2*x)*cos(2*x), [0, pi/4])
assert abs(definite - (F(pi/4) - F(0))) < 1e-20
A1 = quad(lambda x: 2*x + 5 - (x**2 + 2), [0, 3]); A2 = quad(lambda x: x**2 + 2 - (2*x + 5), [3, 6])
g = lambda x: exp(x) - 1/x - 3
y = lambda x: (x**2 + 5)/(x + 2)
assert abs(lim4a - mpf(1)/2) < 1e-4 and abs(lim4b - mpf(1)/2) < 1e-6
# Q2a: x = A(x^2+1)+(Bx+C)(x+1); at x=-1 this gives -1 = 2A
expected = [
    xc, f(xc),
    mpf(-1)/2,
    diff(lambda x: x - log(1 + x), 1),
    left(6), xp*log(xp), 0 if abs(left(0)) < 1e-12 else left(0), mpf(7)/2,
    0, left(3), left(-9),
    diff(den, 1), lim4a,
    lim4b_den, lim4b,
    2, definite,
    findroot(lambda x: x**2 - 2*x - 3, 2.5), A1, A2, A1 + A2,
    g(1), g(mpf(3)/2),
    findroot(lambda x: diff(y, x), 0.9), y(0), y(10),
]
run("24B-A", expected)

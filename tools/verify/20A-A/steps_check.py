# Independent mpmath re-check of the numeric guided steps of 20A-A (the sympy values live in tools/gen/gen_20A-A.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sin, cos, sqrt, quad, diff, findroot, pi, e, cbrt
from _steps_common import run
mp.dps = 30
f1 = lambda x: x*exp(1/x)
n = mpf(10)**6
rat = (n - cbrt(n**6 - 1))/(1 + n**3)
# Q2b: y = a x^3 + b x^2 + c x with a=2, b=6: inflection at -b/(3a); y'(x_infl) = 0 gives c
a, b = 2, 6
xi = -mpf(b)/(3*a)
c = -(3*a*xi**2 + 2*b*xi)
t = mpf('1e-4')
cosl = (cos(t) - 1)/sin(2*t)**2
# Q3b: 1 = A(t-3) + B(t-2): t=2 -> A = -1 ; t=3 -> B = 1
A3 = 1/(2 - 3); B3 = 1/(3 - 2)
left4 = lambda h: 1/(sqrt(2 - h) - 1) - sqrt(2 - h)
right4 = lambda a_, h: (sqrt(1 + a_*h) - cos(h))/h
a4 = findroot(lambda a_: right4(a_, mpf('1e-9')) - left4(mpf('-1e-9')), 1.5)
f6 = lambda x: sqrt(x - 2)*exp(-x/2)
x6 = findroot(lambda x: diff(f6, x), 2.9)
I6 = quad(lambda x: (x - 2)*exp(-x), [2, 3])
# Q5b: 1 = A(t+2) + B t at t=0 -> A = 1/2
A5 = mpf(1)/2
expected = [
    f1(1),
    rat,
    c,
    cosl, exp(cosl),
    A3, B3,
    left4(mpf('-1e-9')), a4,
    quad(lambda x: (exp(x) + exp(-x))/2, [-2, 2]),
    A5,
    x6, f6(x6),
    I6, pi*I6,
]
run("20A-A", expected)

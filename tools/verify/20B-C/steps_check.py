# Independent mpmath re-check of the numeric guided steps of 20B-C (the sympy values live in tools/gen/gen_20B-C.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sin, cos, tan, sqrt, asin, quad, diff, findroot, pi, e
from _steps_common import run
mp.dps = 30
f1 = lambda x: x**3/(2*(x + 1)**2)
f3 = lambda x: x*sqrt(18 - x**2)
g4 = lambda x: (sqrt(3*x - 2) - sqrt(x + 2))/(x**2 - 4)
h = mpf('1e-8')
left3 = (exp(-h) - 1)/sin(-2*h)
mid = lambda x: x*log(x)
integ5b = lambda x: quad(lambda t: t**2/(1 + t**4), [0, x])/x**3
x1 = findroot(lambda x: 2*x - 1/x, 0.7)
P1 = quad(lambda x: 2*x - x/2, [0, x1]); P2 = quad(lambda x: 1/x - x/2, [x1, sqrt(2)])
expected = [
    f1(-3),
    mpf(1) - (mpf(2)/3)**400/(1 + (mpf(2)/3)**400), mpf(1)/2,
    4, -1,
    left3, mid(h), asin(h)/(2*h),
    findroot(lambda x: diff(f3, x), 2.5), f3(3), f3(4),
    quad(log, [1, e]), quad(lambda x: log(x)**2, [1, e]),
    (2 + 2)*(sqrt(4) + sqrt(4)), g4(2 + mpf('1e-9')),
    1/(2*mpf(1)**4 + 1), mpf(1) - (-1),
    integ5b(mpf('1e-3')),
    pi/60, 1/cos(pi/4)**2, 1 + (1/cos(pi/4)**2)*pi/60,
    x1, P1, P1 + P2,
]
run("20B-C", expected)

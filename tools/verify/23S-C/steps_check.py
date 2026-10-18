# Independent mpmath re-check of the numeric guided steps of 23S-C (the sympy values live in tools/gen/gen_23S-C.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sin, cos, sqrt, quad, diff, findroot, pi, e, matrix, lu_solve, cbrt
from _steps_common import run
mp.dps = 30

f1 = lambda x: 2*x*exp(-x**2/2)
r3 = findroot(lambda x: diff(f1, x, 2), 1.7)
a_ = mpf(1)
for _ in range(3):
    a_ = a_/2 + 1
Lseq = mpf(1)
for _ in range(100):
    Lseq = Lseq/2 + 1
g2b = lambda x: (x**3 - 2*x)/(x**2 + 1)
defint = quad(g2b, [0, 1])
assert abs(defint - (mpf(1)/2 - mpf(3)/2*log(2))) < mpf(10)**-20
# Q3a: continuity a+b=1, derivative equality 2a+b=3
sol = lu_solve(matrix([[1, 1], [2, 1]]), matrix([1, 3]))
h3 = lambda x: 2*x**3 - x**2 + x + 1
disc = (-2)**2 - 4*6*1
X = mpf(10)**8
lim4a = 2*X*(8*X - 3)/(X**2 - 3*X + 7)
I4 = quad(lambda x: log(x)**2, [1, e])
# Q5a: slope of the curve y = pi x sin(y/2) at (1, pi), by finite difference along the solved branch
yc = lambda x: findroot(lambda y: y - pi*x*sin(y/2), pi)
hh = mpf('1e-10')
slope5 = (yc(1 + hh) - yc(1 - hh))/(2*hh)
xs = mpf('1e-8')
lh = (exp(xs) - 1)/(xs*exp(xs))
A5 = exp(log(xs)/log(exp(xs) - 1))
yfun = lambda t: 2*t + 3*(cbrt(t) if t >= 0 else -cbrt(-t))**2
crit6 = findroot(lambda t: diff(yfun, t), -0.8)
yt = lambda t: cbrt(t)
expected = [
    2/sqrt(e), r3,
    a_, Lseq,
    defint,
    sol[0], sol[1],
    disc, h3(-3), h3(0),
    lim4a,
    I4, pi*I4,
    slope5,
    lh, A5,
    crit6, yfun(mpf(-2)),
    diff(yt, 8), 2 + diff(yt, 8), abs(diff(yt, 8, 2))/2,
]
run("23S-C", expected)

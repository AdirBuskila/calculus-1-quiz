# Independent mpmath re-check of the numeric guided steps of 23A-B (the sympy values live in tools/gen/gen_23A-B.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sin, atan, sqrt, quad, diff, findroot, pi, e, matrix, lu_solve
from _steps_common import run
mp.dps = 30

f1 = lambda x: (log(x) - 1)/log(x)
xint = findroot(lambda x: f1(x), 2.5)
infl = findroot(lambda x: diff(f1, x, 2), 0.1)
hor = f1(mpf(10)**1000000)
abc = lu_solve(matrix([[1, 1, 0], [0, 1, 1], [4, 0, 1]]), matrix([2, 1, 4]))   # A+B=2, B+C=1, 4A+C=4
a2 = mpf(3)
a2 = (a2 + 7/a2)/2
t = mpf('1e-9')
f4 = lambda x: (x + 2)*sqrt(4 - x**2)
c4 = findroot(lambda x: diff(f4, x), 0.8)
I4 = quad(lambda x: x*log(x), [1, e])
u = mpf('1e-9')
xs = findroot(lambda x: 1/(1 + x**2) - 3/(9 + x**2), 1.5)
S6 = 2*quad(lambda x: 1/(1 + x**2) - 3/(9 + x**2), [0, xs])
y6 = lambda x: log(1 + x)
expected = [
    xint, infl, hor,
    abc[0], abc[1],
    a2,
    (1 + t)**(2/t),
    c4, f4(1),
    I4, pi*I4,
    (1 + u)**(1/u), u/sin(2*u),
    atan(1/u**2),
    xs, S6,
    diff(y6, 0, 2), -mpf('0.1') - mpf('0.1')**2/2, mpf('0.1')**3/(3*mpf('0.9')**3),
]
run("23A-B", expected)

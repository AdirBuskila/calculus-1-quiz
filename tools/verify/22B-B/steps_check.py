# Independent mpmath re-check of the numeric guided steps of 22B-B (the sympy values live in tools/gen/gen_22B-B.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sin, cos, atan, sqrt, quad, diff, findroot, pi, e, matrix, lu_solve
from _steps_common import run
mp.dps = 30

f1 = lambda x: x*exp(1 - 2*x**2)
xm = findroot(lambda x: diff(f1, x), 0.4)
xi = findroot(lambda x: diff(f1, x, 2), 0.8)
a = mpf(1)
for _ in range(80):
    a = 2*a/(a + 3)
a2 = 2*mpf(1)/(mpf(1) + 3)
I3b = quad(lambda x: x*log(x), [1, e])
h = mpf('1e-4')
lim4a = (h - quad(lambda t: cos(t**2), [0, h**2]))/(h**3 - 6*h)
L4b = quad(lambda x: sqrt(1 + diff(lambda t: t**mpf(1.5), x)**2), [0, 1])
f5 = lambda x: 2*x**3 + 3*atan(x) + exp(x) + 1
ca = findroot(lambda a_: 1/(2*sqrt(a_ - 1)) - sqrt(a_ - 1)/a_, 1.8)
S2 = quad(lambda x: sqrt(x - 1), [1, 2])
abc = lu_solve(matrix([[1, 1, 0], [4, 1, 1], [5, 0, 1]]), matrix([0, 0, 1]))   # x^2: A+B=0; x: 4A+B+C=0; const: 5A+C=1
y6 = lambda x: log(1 + x)
expected = [
    xm, f1(xm), xi,
    a2, a,
    I3b, pi*I3b,
    lim4a,
    L4b,
    f5(0), f5(-1),
    ca, mpf(1), S2, 1 - S2,
    abc[0], abc[1], abc[2],
    diff(y6, 0, 2), mpf('0.1') - mpf('0.1')**2/2, mpf('0.1')**3/(3*mpf('0.9')**3),
]
run("22B-B", expected)

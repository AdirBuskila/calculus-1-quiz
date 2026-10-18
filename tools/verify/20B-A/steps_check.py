# Independent mpmath re-check of the numeric guided steps of 20B-A (the sympy values live in tools/gen/gen_20B-A.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sin, cos, sqrt, quad, diff, findroot, e, matrix, lu_solve, cbrt
from _steps_common import run
mp.dps = 30
f1 = lambda x: exp(2*x)/x
xm = findroot(lambda x: diff(f1, x), 0.4)
a = mpf(3)/2
a = 3 - 2/a                                   # a_2
t = mpf('1e-3')
lnA = log(sin(t)/t)/t**2
# partial fractions: A(x^2+2x+5) + (Bx+C)x = 2x^2+15 -> three linear equations in A, B, C
M = matrix([[1, 1, 0], [2, 0, 1], [5, 0, 0]]); sol = lu_solve(M, matrix([2, 0, 15]))
lim4 = lambda av: (lambda X: X*(sqrt(X**2 + X + av) - sqrt(X**2 + X)))(mpf('1e8'))
h = mpf('1e-9'); cbrt2 = lambda u: cbrt(u*u)
# Q2b: tangent condition: slopes and intercepts of the tangents at x1, x2 agree
x1 = findroot(lambda p: 2/p + 1/(4*p**4), -0.6)
x2 = -1/(2*x1**2)
# Q6a: g'(2)=0 and asymptote y = x + 7 -> b = 7, a = 4 - 4b
b6 = 7; a6 = 4 - 4*b6
S6 = quad(lambda x: log(x + 1)/sqrt(x + 1), [0, 1])
expected = [
    xm, f1(xm),
    a,
    x1, x2,
    lnA, exp(lnA),
    sol[0], sol[1], sol[2],
    lim4(4), findroot(lambda av: lim4(av) - 3, 5),
    quad(lambda u: u/(1 + u**2), [0, 1]),
    0, sin(h)/h, cbrt2(h)*sin(h)/h,
    quad(lambda x: (x**0.25 + x**-0.25)/2, [0, 1]),
    b6, a6,
    S6,
]
run("20B-A", expected)

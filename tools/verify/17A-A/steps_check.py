# Independent mpmath re-check (no sympy) of the numeric guided steps of 17A-A.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sqrt, sin, cos, quad, diff, findroot, pi, cbrt, e, lu_solve, matrix
from _steps_common import run
mp.dps = 30
f1 = lambda x: (4*x**2 - 2*x - 1)/(x - 1)
c1 = findroot(lambda x: diff(f1, x), 0.4)
c1b = findroot(lambda x: diff(f1, x), 1.6)
a2 = mpf(1)/3 + 3
L = findroot(lambda L: L - L/3 - 3, 4)
xs = mpf('1e-6')
lim3a = log(cos(xs))/(xs*sin(xs))
y3 = lambda x: cos(pi*exp(x)/6)
y3p = diff(y3, 0)
d3 = y3(0) + y3p*mpf('0.1')
g4 = lambda a, x: (sqrt(2*x - a) - sqrt(x))/(x**2 - a**2)
a4 = findroot(lambda a: g4(a, a + mpf('1e-12')) - sqrt(a), 0.4)
Q4 = quad(lambda x: exp(x)*sin(pi*x), [0, 1])
y5 = lambda x: x*cbrt((3*x - 12)**2)
c5 = findroot(lambda x: diff(y5, x), 2.3)
# Q5b: (x^2-5x+5) = A(x^2+2x+5) + x(Bx+C): coefficients of x^2, x, 1
M = matrix([[1, 1, 0], [2, 0, 1], [5, 0, 0]]); ABC = lu_solve(M, matrix([1, -5, 5]))
P2 = lambda x: 1 + (x - 1)/2 - (x - 1)**2/8
f6 = lambda x: sqrt(x)
exp2 = diff(f6, 1, 2)/2
x6 = findroot(lambda x: x**3 - sqrt(32*x), 1.9)
expected = [
    c1, f1(c1), f1(c1b),
    a2, L,
    lim3a, exp(lim3a),
    y3(0), y3p, d3,
    a4, e*sin(pi) - sin(0), e*cos(pi) - cos(0), Q4,
    c5, y5(c5), y5(6), y5(4),
    ABC[0], ABC[2],
    exp2, P2(mpf('1.05')),
    x6, quad(lambda x: sqrt(32*x), [0, 2]), quad(lambda x: sqrt(32*x) - x**3, [0, 2]),
]
run("17A-A", expected)

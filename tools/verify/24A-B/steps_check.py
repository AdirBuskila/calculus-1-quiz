# Independent mpmath re-check of the numeric guided steps of 24A-B.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sqrt, atan, quad, diff, lu_solve, matrix, findroot, pi, e
from _steps_common import run
mp.dps = 30
f = lambda x: x**2*exp(x)
infl = findroot(lambda x: diff(f, x, 2), -0.6)
g = lambda x: (x**2 + 2*x + 3)/((x - 1)*(x + 2)**2)
pts = [0, 2, 3]
M = matrix([[1/(p - 1), 1/(p + 2), 1/(p + 2)**2] for p in pts]); ABC = lu_solve(M, matrix([g(p) for p in pts]))
a2 = sqrt(20 + 4)
n = mpf(10)**8; base = (n**2 + 5*n - 2)/(n**2 + 3*n - 2)
V = pi*quad(lambda x: (4 - sqrt(x))**2 - (x - 2)**2, [2, 4])
xi = findroot(lambda x: x - 2 - (4 - sqrt(x)), 3.5)
y = lambda x: x*exp(1/x)
c4 = findroot(lambda x: diff(y, x), 0.9)
S4 = quad(lambda x: (1.5 - 0.5*x) - sqrt(2 - 2*x), [-1, 1]) + quad(lambda x: 1.5 - 0.5*x, [1, 3])
xt = findroot(lambda x: -1/sqrt(2 - 2*x) + mpf(1)/2, -0.9)
v5 = quad(lambda x: log(x)/(x*(log(x)**2 + 1)), [1, e])
l0 = atan(2*mpf('-1e-9'))/mpf('-1e-9')
x2 = 2 + mpf('1e-12'); r2 = 4*(x2 - sqrt(3*x2 - 2))/(x2 - 2)
f6 = lambda x: 2**sqrt(x) + atan(2*x) - 5
xs6 = mpf('1e-3')
limit6b = round(xs6**4/quad(lambda t: t*mp.cos(t**2), [0, xs6**2]), 3)
expected = [
    f(-2), infl,
    ABC[0], ABC[1], ABC[2],
    a2,
    n*(base - 1), exp(2),
    xi, V/pi, V,
    c4, y(mpf(1)/2), y(3),
    xt, findroot(lambda x: 1.5 - 0.5*x, 3), S4,
    v5,
    l0, r2, (1 - l0)/2,
    f6(0), f6(16),
    limit6b,
]
run("24A-B", expected)

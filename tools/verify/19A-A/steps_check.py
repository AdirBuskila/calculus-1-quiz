# Independent mpmath re-check (no sympy) of the numeric guided steps of 19A-A.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sqrt, sin, cos, quad, diff, findroot, pi, cbrt, e, lu_solve, matrix
from _steps_common import run
mp.dps = 30
f1 = lambda x: exp(-x)/(1 - x)
fl = lambda x: x*log(x)
xs = mpf('1e-9')
ex3 = log(4/(1 + sqrt(9 + xs)))/sin(xs)
f4 = lambda x: x*(cbrt(x**2 - 1) if x**2 >= 1 else -cbrt(1 - x**2))
c4 = findroot(lambda x: 5*x**2 - 3, 0.8)
f4b = lambda x: (x - 3)**sqrt(x)
big = mpf(10)**8
orig5 = 1/((sqrt(2*big - 1) - sqrt(2*big - 3))*sqrt(big + 1))
M = matrix([[1, 1, 0], [0, -1, 1], [1, 0, -1]]); ABC = lu_solve(M, matrix([2, -1, 1]))
V6 = 2*pi*quad(lambda x: x*(2 - exp(x)), [0, log(2)])
S6 = quad(lambda x: x/2, [0, 1]) + quad(lambda x: 1/x - x/2, [1, sqrt(2)])
expected = [
    f1(0),
    mpf(1), mpf(7),
    diff(fl, e),
    round(ex3, 4), exp(round(ex3, 4)),
    c4, f4(c4), f4(3),
    f4b(4), diff(f4b, 4),
    2, round(orig5, 4),
    ABC[0], ABC[1], ABC[2],
    log(2), quad(lambda x: x*exp(x), [0, log(2)]), V6,
    findroot(lambda x: x - 1/x, 1.2), findroot(lambda x: x/2 - 1/x, 1.3), quad(lambda x: x/2, [0, 1]), S6,
]
run("19A-A", expected)

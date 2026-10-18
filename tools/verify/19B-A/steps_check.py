# Independent mpmath re-check of the numeric guided steps of 19B-A (the sympy values live in tools/gen/gen_19B-A.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sin, cos, sqrt, asin, quad, diff, findroot, pi, e, matrix, lu_solve
from _steps_common import run
mp.dps = 40
f1 = lambda x: 2*x**2/(x**2 - 1)
a = mpf(4)
for _ in range(400):
    a = sqrt(5*a - 6)
f2 = lambda x: x**3 + x + exp(x)
M = matrix([[1, 1, 0], [0, 1, 1], [1, 0, 1]]); sol = lu_solve(M, matrix([0, 1, 0]))   # A+B=0, B+C=1, A+C=0
lim3 = log(1 + exp(mpf(400)))/400
x0 = findroot(lambda x: 2*x/(1 + x**2) - 1, 0.8, verify=False)   # double root
g5 = lambda x: sqrt(2 + 2*x + x**2) - sqrt(2 - 2*x + x**2)
# Q4a: (ln a)^2 = ln a, a = exp(root of u^2 - u)
u1 = findroot(lambda u: u**2 - u, 0.1); u2 = findroot(lambda u: u**2 - u, 0.9)
xi = findroot(lambda x: sqrt(x + 2) - sqrt(2*x), 1.8)
I1 = quad(lambda x: sqrt(x + 2), [-2, 2]); I2 = quad(lambda x: sqrt(2*x), [0, 2])
V6 = pi*quad(lambda x: (pi/2 - x)**2 - cos(x)**2, [0, pi/2])
expected = [
    f1(0),
    sqrt(14), a,
    f2(-1), f2(0),
    lim3, exp(lim3),
    quad(asin, [0, mpf(1)/2]),
    exp(u1), exp(u2),
    1, x0, log(1 + x0**2),
    g5(-mpf(10)**12),
    sol[0], sol[1], sol[2],
    quad(lambda x: (pi/2 - x)**2, [0, pi/2]), quad(lambda x: cos(x)**2, [0, pi/2]), V6,
    xi, I1, I2, I1 - I2,
]
run("19B-A", expected)

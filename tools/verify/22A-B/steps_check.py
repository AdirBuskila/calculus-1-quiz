# Independent mpmath re-check (no sympy) of the numeric guided steps of 22A-B (values stored by tools/gen/gen_22A-B.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, sqrt, sin, cos, atan, log, exp, quad, pi, diff, findroot, matrix, lu_solve
from _steps_common import run
mp.dps = 40
f1 = lambda x: x**3/(x**2 - 1)
f1p = lambda x: diff(f1, x)
g3 = lambda x: log(x + 1) - (3*x + 2)/(x + 2)
y4 = lambda x: exp(x/(1 - x))/(1 - exp(x/(1 - x)))
cbrt = lambda v: (1 if v > 0 else -1)*abs(v)**(mpf(1)/3)
f6 = lambda x: x*cbrt(3*x - 1)
fp6 = lambda x: diff(f6, x)
t1 = sqrt(1 + exp(2))
L = quad(lambda x: sqrt(1 + exp(2*x)), [0, 1])
# Q6b: continuity 8a = 4 + b and 12a = 4 (derivative matching), solved as a linear system
ab = lu_solve(matrix([[8, -1], [12, 0]]), matrix([4, 4]))
abc = lu_solve(matrix([[-1, 0, 1], [3, -1, 0], [0, 3, 2]]), matrix([0, 0, 1]))   # unknowns A, B, C of (At+B)(3-t)+C(t^2+2)=1
fq = lambda x: ab[0]*x**3 if x <= 2 else x**2 + ab[1]
expected = [
    findroot(f1p, 1.7), f1(sqrt(3)),                                                        # Q1
    (5 + 5/mpf(5))/2, (1 + 5/mpf(5)**2)/2,                                                  # Q2a: a_2 and a_2/a_1
    diff(lambda x: atan(2/x), 2), quad(lambda x: 4/(x**2 + 4), [0, 2])/atan(1),             # Q2b
    g3(0), g3(100), diff(g3, 1),                                                            # Q3a
    abc[2], abc[1],                                                                         # Q3b: C and B of the decomposition
    y4(1 - mpf('1e-4')), y4(1 + mpf('1e-4')),                                               # Q4a (one-sided at 1)
    quad(lambda x: x, [pi/2, pi]), quad(lambda x: x*cos(2*x), [pi/2, pi]), 2*pi*quad(lambda x: x*cos(x)**2, [pi/2, pi]),   # Q4b
    diff(lambda t: log(1 + t), 1),                                                          # Q5a: f'(1)
    t1, L - (t1 - sqrt(2)), L,                                                              # Q5b
    findroot(fp6, 0.3), f6(mpf(1)/4), f6(-1),                                               # Q6a
    diff(lambda x: x**2, 2), ab[0], ab[1],                                                  # Q6b
]
run("22A-B", expected)

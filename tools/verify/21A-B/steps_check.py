# Independent mpmath re-check (no sympy) of the numeric guided steps of 21A-B (values stored by tools/gen/gen_21A-B.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, sqrt, sin, cos, asin, quad, pi, diff, findroot, matrix, lu_solve, cbrt
from _steps_common import run
mp.dps = 40
f1 = lambda x: x**4/(x**3 - 1)
f1p = lambda x: diff(f1, x)
X = mpf(10)**12
# Q2a: x^3/(x^2-x+2) + a x + b -> 0: the x^3 and x^2 coefficients of (a+1)x^3 + (b-a)x^2 + ... vanish
ab = lu_solve(matrix([[1, 0], [-1, 1]]), matrix([-1, 0]))
tail = X**3/(X**2 - X + 2) + ab[0]*X + ab[1]
assert abs(tail) < 1e-9
f2 = lambda x: x*abs(x - 3)/((x**2 - 4*x + 3)*asin(x/5))
e = mpf('1e-9')
f3 = lambda x: (sqrt(1 + sin(x/2)) - sqrt(1 - sin(x/2)))/x
fq = lambda x: 3*x**2 + 2*x + 1
rcb = lambda v: (1 if v > 0 else -1)*abs(v)**(mpf(1)/3)
f6 = lambda x: rcb(x**2 - 2*x)
h = mpf('1e-4')
expected = [
    findroot(f1p, 1.6), f1(cbrt(4)),                                                        # Q1
    ab[0], ab[1],                                                                           # Q2a
    f2(e), f2(3 + e),                                                                       # Q2b
    sqrt(1 + sin(0)) + sqrt(1 - sin(0)), 2*sin(h/2)/h, f3(mpf('1e-8')),                      # Q3a
    (mpf(2)**2)/2 + 2, (1**2 + 2*1)/(1**2 + 1),   # Q3b
    (fq(5) - fq(1))/4, findroot(lambda c: diff(fq, c) - 20, 2),                              # Q4a
    findroot(lambda x: x**2 - 2*x - 8, 3), 4 - sqrt(9), 8 - mpf(10)/2,                       # Q4b
    mpf(1) - 2 + 1,                                                                         # Q5a: f(1) of x^6 - 2x^2 + x
    (mpf('1e-2') - sin(mpf('1e-2')))/mpf('1e-2')**3,
    (2*(1 - cos(h))/h**4 - 1/h**2),                                                         # Q5b
    findroot(lambda x: diff(f6, x), 0.9), f6(-1), f6(1),                                    # Q6a
    sqrt(mpf(2)/4), sqrt(18), quad(lambda x: 4*x**2 - x**2/9, [0, 1/sqrt(2)]),               # Q6b
    quad(lambda x: 4*x**2 - x**2/9, [0, 1/sqrt(2)]) + quad(lambda x: 2 - x**2/9, [1/sqrt(2), sqrt(18)]),
]
run("21A-B", expected)

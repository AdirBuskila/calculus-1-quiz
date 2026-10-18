# Independent mpmath re-check (no sympy) of the numeric guided steps of 22B-A (values stored by tools/gen/gen_22B-A.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import findroot, mp, mpf, sqrt, cbrt, sin, cos, atan, tan, log, quad, pi, factorial, diff
from _steps_common import run
mp.dps = 90
rc = lambda v: (1 if v > 0 else -1)*abs(v)**(mpf(1)/3)
fr = lambda x: 2*x + 3*cbrt(x*x)
fraction = lambda n, A: (factorial(n + 2) + (A + 1)*n*factorial(n + 1))/(factorial(n + 1) - n*factorial(n))
N = mpf(10)**7
lim1b = (N + 1)*(5*N + 2)*sin(mpf(2)/(N + 1)**2)                      # A=3, C=1
a_next = lambda a, kk: (kk + 1)*a/(kk*a + 1)
f3 = lambda x: (x + 2)*(2 + cos(mpf(2)/(x + 2)))                      # A=2, B=1
X = mpf(10)**12
t0 = mpf(3)/10
g4 = lambda x: x**3 + x + cos(x) - 2                                    # B=1, C=0
g4b = lambda x: x**3 + 2*x + cos(2*x) - 1                               # C=1, B=0
w = lambda x: atan(sqrt(x))
D = mpf(10)**8
lim5 = (D**3 + 3)*(sqrt(D**2 + sqrt(D**4 + 4)) - D*sqrt(2))             # C=3, A=3
den5 = (sqrt(1 + 4/D**4) + 1)*(sqrt(1 + sqrt(1 + 4/D**4)) + sqrt(2))
f6 = lambda x: 1/sin(x) - 1/x
h = mpf('1e-6')
expected = [
    2 + 2/rc(-mpf(1)/8), findroot(lambda x: 2 + 2/rc(x), -1.2), fr(-1),              # Q1a: f'(-1/8), the critical point x=-1, f(-1)
    fraction(4, 3), lim1b,                                                                              # Q1b
    diff(atan, 1),                                                                                      # Q2a: g'(1)
    a_next(mpf(2), 2), a_next(mpf(3), 2) - 1,                                                           # Q2b
    f3(X)/X, f3(X) - 3*X,                                                                               # Q3a
    (1/((2 - t0)*(1 + t0)))/(1/(2 - t0) + 1/(1 + t0)),                                                  # Q3b
    g4(1), diff(g4b, 0),                                                                                # Q4a
    (1/((mpf(1) + 1)*sqrt(1)))/diff(w, 1), quad(lambda x: w(x)**3/((x + 1)*sqrt(x)), [0, 1]),           # Q4b
    4, den5, lim5,                                                                             # Q5a (numerator D=C+1=4)
    cos(pi/3)/sin(pi/3), log(tan(pi/6)), quad(lambda v: sqrt(1 + (cos(v)/sin(v))**2), [pi/3, pi/2]),    # Q5b
    f6(mpf('1e-20')), (h - sin(h))/h**3, f6(mpf('1e-4'))/mpf('1e-4'),                                   # Q6a
    quad(lambda u: u*sin(u)**2, [0, pi]), 2*pi*quad(lambda v: v*sin(2*v)**2, [0, pi/2]),               # Q6b
]
run("22B-A", expected)

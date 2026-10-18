# Independent mpmath re-check (no sympy) of the numeric guided steps of 22A-A (values stored by tools/gen/gen_22A-A.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, sqrt, sin, cos, atan, asin, log, exp, quad, pi, diff, findroot, polyroots
from _steps_common import run
mp.dps = 50
r5 = lambda v: (1 if v > 0 else -1)*abs(v)**(mpf(1)/5)
f1 = lambda x: mpf(4)/5*x - abs(x - 1)**(mpf(4)/5) + 2
fp1 = lambda x: mpf(4)/5 - mpf(4)/5/r5(x - 1)
def iterate(A, a1, n=60):
    s = mpf(a1)
    for _ in range(n):
        s = (s + (A + 1)/s)/2
    return s
nn = mpf(10)**9
G = lambda t: atan(t)
F2 = lambda x: (x**2*atan(x**2) - log(1 + x**4)/2)/2
f3 = lambda x: 3*x*abs(x - 3)/((2*x**2 - 7*x + 3)*atan(5*x))            # A=1, B=2, C=2
hp = mpf('1e-6')
g5 = lambda x: asin(x) - x/sqrt(1 - x**2)
roots = polyroots([1, 1, -2])
S0 = 2*2*(pi/4 - mpf(1)/6)
f6n = lambda x: x - asin(x)
x6 = mpf('1e-3')
lim6 = (x6 - asin(x6))/quad(lambda t: log(1 + t**2), [0, x6])
V = 2*pi*quad(lambda x: x*(x**2 + 2)**(mpf(1)/5), [0, 3])
# partial fractions of (3x^3+x^2+4x+8)/(x^2(x^2+4)): rows are the coefficients of x^3, x^2, x, 1 in A, B, C, D (A,B: 1/x^2, 1/x; C,D: (Cx+D)/(x^2+4))
from mpmath import matrix, lu_solve
sol = lu_solve(matrix([[0, 1, 1, 0], [1, 0, 0, 1], [0, 4, 0, 0], [4, 0, 0, 0]]), matrix([3, 1, 4, 8]))
expected = [
    fp1(33), findroot(fp1, 2.2), f1(1),                                              # Q1a
    sqrt(4), (5 + mpf(4)/5)/2, iterate(8, 12),                                       # Q1b
    sqrt(9 + 4) - 3, mpf(4)/(sqrt(nn**2 + 4) + nn),   # Q2a
    mpf(1)/2, quad(lambda x: x*atan(x**2), [0, 1]),                                  # Q2b
    max(polyroots([2, -9, 4])), f3(mpf('1e-9')),                                     # Q3a
    (exp(2*hp) - 2*hp - 1)/hp**2, (-hp - sin(-hp))/(-hp)**3, sqrt(mpf(1)/3),     # Q3b
    diff(lambda x: 6*log(x), 1), 4 + 6*(1 - 1), 4 + 6*(2 - 1),                       # Q4a (C=4)
    sol[0], sol[1], quad(lambda x: 1/(x**2 + 4), [0, 2])/atan(1),                    # Q4b
    diff(g5, mpf('0.6')), g5(mpf(1)/2),                                              # Q5a
    max(r for r in roots if r > 0), quad(lambda x: 1/(1 + x**2) - x**2/2, [0, 1]), S0,   # Q5b
    diff(f6n, mpf('0.6')), (mpf('1e-4')**2)/log(1 + mpf('1e-4')**2), lim6,           # Q6a
    (2 + 1)**2 + 1 + 1, V,                                                                 # Q6b
]
run("22A-A", expected)

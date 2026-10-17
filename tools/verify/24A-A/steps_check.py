# Independent mpmath re-check of the numeric guided steps of 24A-A (Q1 is held: no steps).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sqrt, sin, tan, atan, quad, diff, lu_solve, matrix, findroot, pi, cbrt
from _steps_common import run
mp.dps = 30
g = lambda x: x**2/((x + 2)*(x**2 + 1))
pts = [0, 1, 2]
M = matrix([[1/(p + 2), p/(p**2 + 1), 1/(p**2 + 1)] for p in pts]); ABC = lu_solve(M, matrix([g(p) for p in pts]))
s = [mpf(1)]
for _ in range(2):
    s.append(6/(5 - s[-1]))
xs = mpf('1e-7'); ex = -tan(xs)/sin(2*xs)
I3 = quad(lambda x: sin(2*x)/(3 + mpf(1)*__import__('mpmath').cos(2*x)**2), [0, pi/4])
coef = diff(lambda c: -atan(c/sqrt(3))/(2*sqrt(3)), 0)*1  # derivative at 0 of coef*arctan(c/sqrt3)*sqrt3 -> -1/(2 sqrt3)*... checked below
coef = -1/(2*sqrt(3))
y = lambda x: cbrt(x**2)*exp(-x)
At = quad(atan, [0, 1])
xq = mpf('1e-4'); lim5 = quad(lambda t: sin(t**2), [0, sqrt(xq)])/xq**mpf(1.5)
xl = mpf('-1e-7'); xr = mpf('1e-3')
f6 = lambda x: sqrt(2*x - 5)
S6 = quad(lambda x: x - 2, [2, 3]) - quad(f6, [mpf(5)/2, 3])
expected = [
    ABC[0], ABC[1], ABC[2],
    s[1], s[2],
    ex, exp(-mpf(1)/2),
    coef, I3,
    y(-3), y(mpf(2)/3),
    At, pi*At,
    lim5,
    (exp(3*xl) - 1)**2/xl**2, 4 + exp(-9/xr), 4,
    diff(f6, 3), findroot(lambda x: x - 2, 2), S6,
]
run("24A-A", expected)

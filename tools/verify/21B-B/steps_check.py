# Independent mpmath re-check (no sympy) of the numeric guided steps of 21B-B (Q2, Q6a, Q6b are held).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sqrt, sin, cos, tan, quad, diff, findroot, pi, e, cbrt
from _steps_common import run
mp.dps = 30
f1 = lambda x: ((x + 2)/(x + 1))**2
infl = findroot(lambda x: diff(f1, x, 2), -2.4)
f3 = lambda x: 2*sin(3*x)**2 + 5*cbrt(1 - x**2) - 4*x**5
xs = mpf('1e-6')
r4a = tan(xs)/tan(4*xs)
l4a = log(cos(xs))/log(cos(4*xs))
x4 = findroot(lambda x: x**2 + 2*x - 8, 1.5)
V1 = 2*quad(lambda x: (4 - x)*x**2, [0, 2])
V2 = 2*quad(lambda x: (4 - x)*(-2*x + 8), [2, 4])
f5 = lambda x: log(1 + x**2)
rt = sqrt(e - 1)
expected = [
    infl, f1(infl),
    f3(0), f3(1),
    round(r4a, 3), round(l4a, 4),
    x4, V1, V2, pi*(V1 + V2),
    findroot(lambda x: diff(f5, x), mpf('0.05')), f5(-1), f5(rt),
    diff(lambda h: 3*sin(2*h), 0), 5*diff(exp, 0),
]
run("21B-B", expected)

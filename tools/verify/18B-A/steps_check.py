# Independent mpmath re-check (no sympy) of the numeric guided steps of 18B-A.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sqrt, sin, cos, tan, atan, quad, diff, findroot, pi, e
from _steps_common import run
mp.dps = 30
f1 = lambda x: x**3/(x**2 - 3)
a2 = 3*mpf(2)/(2*2 + 1)
a = mpf(2)
for _ in range(200):
    a = 3*a/(2*a + 1)
g3 = lambda x: (x**3 + 1)*(x**3)**5*3*x**2
cr3 = findroot(lambda x: x**3 + 1, -0.9)
fe = lambda v: exp(v) + sin(v)
xs = pi/2 - mpf('1e-7')
lnA = tan(xs)*log(sin(xs))
A = sin(xs)**tan(xs)
I4 = quad(lambda x: x**2*atan(x), [0, 1])
rem4 = quad(lambda x: x**3/(1 + x**2), [0, 1])
fp5 = lambda x: exp(x**2)*(1 + 2*x**2)
L6 = quad(lambda x: sqrt(1 + diff(lambda t: sqrt(1 - t**2), x)**2), [0, mpf(1)/2])
xx = mpf('0.999999')
lim6 = log(xx)*log(1 - xx)
expected = [
    f1(3),
    a2, a,
    cr3, 
    fe(0), fe(-pi/2),
    round(lnA, 4), round(A, 4),
    rem4, I4, pi*I4,
    fp5(1), fp5(2),
    L6, round(lim6, 4),
]
run("18B-A", expected)

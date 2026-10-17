# Independent mpmath re-check of the numeric guided steps of 23B-B.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sqrt, sin, cos, atan, asin, quad, diff, findroot, pi, e, cot
from _steps_common import run
mp.dps = 30
f = lambda x: x*exp(1/x)
a_ = [mpf(0)]
a_.append(sqrt(20 + a_[0]))
xq = mpf('1e-3'); lim3 = xq**4/quad(lambda t: log(1 + 3*t), [0, xq**2])
fa = lambda x: asin(x) - x
ga = lambda x: x/sqrt(1 - x**2) - asin(x)
xi = findroot(lambda x: x**2 - 2*x, 1.5)
I4 = quad(lambda x: 2*x**2 - x**3, [0, 2])
X = mpf(10)**7
I5 = quad(lambda x: (exp(-x) - exp(x))/(exp(-x) + exp(x)), [0, 1])
L6 = quad(lambda x: sqrt(1 + cot(x)**2), [pi/3, pi/2])
h = lambda x: atan(x) + x**3 + x**5 - 2
expected = [
    f(1),
    2/sqrt(3), quad(lambda x: 1/(2 + cos(x)), [0, pi/2]),
    a_[1],
    lim3,
    log(e)**2,
    diff(fa, mpf(3)/5), diff(ga, mpf(1)/2),
    xi, I4, 2*pi*I4,
    log(1 + 1/X)/sin(3/X),
    I5,
    cot(pi/3), L6,
    h(0), h(1),
]
run("23B-B", expected)

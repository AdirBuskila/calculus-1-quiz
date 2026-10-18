# Independent mpmath re-check of the numeric guided steps of 25B-B (the sympy values live in tools/gen/gen_25B-B.py).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sin, tan, cos, sqrt, quad, diff, findroot, atan, pi, e
from _steps_common import run
mp.dps = 30

f1 = lambda x: x*exp(1/(x - 2))
infl = findroot(lambda x: diff(f1, x, 2), 1.5)
# Q2a: iterate a_{n+1} = sqrt(20 + a_n)
a = sqrt(20)
for _ in range(80):
    a = sqrt(20 + a)
F = lambda x: (2*x**2 + 6*x + 2)*atan(x) - 2*x - 3*log(1 + x**2)
defint = quad(lambda x: (4*x + 6)*atan(x), [0, 1])
assert abs(defint - (F(1) - F(0))) < mpf(10)**-20
h = mpf('1e-9')
ex3a = -tan(2*h)*log(h)
y3 = lambda x: tan(x)**cos(x)
slope3 = diff(y3, pi/4)
lim4a = lambda x: (sqrt(x + 2) - sqrt(3*x - 2))/(sqrt(4*x + 1) - sqrt(5*x - 1))
ds = diff(lambda x: x**2, 2)
S4 = quad(lambda x: x**2, [0, 2]) - quad(lambda x: 4*x - 4, [1, 2])
mx = max(exp(sin(mpf(k)/1000)**2) for k in range(0, 3200))
w = quad(lambda x: 16 - x**2, [-4, 4])
V = pi*quad(lambda x: 25 - x**2 - 9, [-4, 4])
expected = [
    exp(-1), 4*sqrt(e), infl,
    a,
    defint,
    tan(2*h)*log(h), exp(ex3a),
    y3(pi/4), slope3,
    lim4a(2 + mpf('1e-8')),
    ds, 1, S4,
    mx,
    4, w, V,
    sin(3*(-h))/(-h), h*log(h), 0,
]
run("25B-B", expected)

# Independent mpmath re-check (no sympy) of the numeric guided steps of 17B-A.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from mpmath import mp, mpf, exp, log, sqrt, sin, quad, diff, findroot, pi
from _steps_common import run
mp.dps = 30
f1 = lambda x: ((x - 2)/(x - 1))**2
infl = findroot(lambda x: diff(f1, x, 2), 2.3)
a = mpf(5)
a = 2 - 1/(2 + a)
L = findroot(lambda L: L - 2 + 1/(2 + L), 1.7)
big = mpf(30)
lim3a = big - log(1 + 2*exp(big))
inner = lambda x: exp(x)/(1 + 2*exp(x))
Vshell = lambda: 2*pi*quad(lambda x: x*(9 - (1 + x**3)), [1, 2])
x3 = findroot(lambda x: 1 + x**3 - 9, 2)
V1 = 2*pi*quad(lambda x: x*9, [1, 2]) / pi
tan = lambda x: 2 + diff(lambda t: sqrt(t), 4)*(x - 4)
ex_ = findroot(tan, -3)
S4 = quad(lambda y: y**2 - (4*y - 4), [0, 2])
f5 = lambda x: sqrt(x) + 4/x
c5 = findroot(lambda x: diff(f5, x), 3.5)
left = lambda av: (exp(av*mpf('-1e-7')) - 1)**2/mpf('1e-14')
right = lambda av: 4 + exp(-av**2/mpf('1e-3'))
expected = [
    infl, f1(infl),
    a, L,
    inner(big), lim3a, 
    x3, V1, Vshell(),
    diff(lambda x: sqrt(x), 4), ex_, S4,
    c5, f5(mpf(1)/4), f5(100),
    left(3), right(3),
]
run("17B-A", expected)

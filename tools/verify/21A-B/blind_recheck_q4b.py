# Blind re-derivation (solver, 2026-10-18) of 21A-B Q4b (handwritten page, labeled fix). ASCII output.
import sympy as sp
x, y = sp.symbols('x y', real=True)
ok = []
# region x>=0 between y=x^2 (below) and y=2x+8 (above), x in [0,4]; axis x=4
ok.append(("intersection x=4", sp.solve(sp.Eq(x**2, 2*x + 8), x) == [-2, 4]))
Vs = 2*sp.pi*sp.integrate((4 - x)*(2*x + 8 - x**2), (x, 0, 4))
# washers in y: for 0<=y<=8, x from 0 to sqrt(y); for 8<=y<=16, x from (y-8)/2 to sqrt(y)
Vw = sp.pi*(sp.integrate(16 - (4 - sp.sqrt(y))**2, (y, 0, 8)) + sp.integrate((4 - (y - 8)/2)**2 - (4 - sp.sqrt(y))**2, (y, 8, 16)))
ok.append(("shells V = 128 pi", sp.simplify(Vs - 128*sp.pi) == 0))
ok.append(("washers V = 128 pi", sp.simplify(Vw - 128*sp.pi) == 0))
for nm, c in ok: print(("OK  " if c else "FAIL"), nm)
print("mismatches:", sum(1 for _, c in ok if not c))

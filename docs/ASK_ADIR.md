# ASK_ADIR - calculus-1

Open questions for Adir. One entry per item; the orchestrator moves it to Resolved when answered.

## Open

<!-- Entry format:
### <exam code> Q<number> - <short title>
- Path: <absolute file path>
- Page: <page number>
- Question: <what is unclear or missing>
- Needed: <what Adir must provide or decide>
- Status: hold
-->

### 24A-B Q6b - official solution computes a different limit than the printed one
- Path: sitting 24A-B (exam + official solution PDF)
- Page: 6 (question), 7 (solution)
- Question: the printed limit has numerator x^4 (sympy value 2); the official solution works a limit with numerator sin^2 x and answers infinity.
- Needed: decide whether the printed question or the solution is intended (the solution is transcribed in raw, the key is not trusted).
- Status: hold

### 25B-B Q1-Q6 - no key
- Path: sitting 25B-B (scanned exam only)
- Page: 1-2
- Question: no solution exists; all 11 items (Q1, Q2a-b ... Q6a-b) are transcribed and held with reason no-key.
- Needed: route to the solver (no action from Adir).
- Status: hold

### 24A-A Q1 - official convexity claim is wrong
- Path: sitting 24A-A (exam + official solution PDF)
- Page: 1 (solution part ג)
- Question: the solution says y''<0 (concave down) for x<0, but y''=e^x(x^2-4x+6)/x^4 is positive for every x!=0 (sympy). All other parts agree.
- Needed: approve shipping the solution with the corrected convexity statement, or leave Q1 out.
- Status: hold

### 23S-C Q4b - official volume drops the factor pi
- Path: sitting 23S-C (exam + official solution PDF)
- Page: 5 (question), 6 (solution)
- Question: the solution gives V = e-2 = 0.714; the correct volume is pi*(e-2) = 2.256 (and e-2 is 0.718, not 0.714).
- Needed: approve shipping with the corrected value, or leave Q4b out.
- Status: hold

### 22B-A Q1-Q6 - no key
- Path: sitting 22B-A (printed exam only)
- Page: 1-2
- Question: no solution exists; all 12 items (Q1a-b ... Q6a-b) are transcribed and held with reason no-key.
- Needed: route to the solver (no action from Adir).
- Status: hold

### 22A-B Q5b - official arc-length decimal is off
- Path: sitting 22A-B (worked-solution PDF)
- Page: 8
- Question: the closed form is right, but the final decimal 1.98 is wrong: the exact value of the integral of sqrt(1+e^(2x)) over [0,1] is 2.0035 (sympy); the rounding of sqrt(1+e^2) to 2.9 spoils it.
- Needed: approve shipping the closed form with the corrected decimal 2.00, or leave Q5b out.
- Status: hold

### 22B-B Q6b - official remainder bound uses the wrong power
- Path: sitting 22B-B (exam + official solution PDF)
- Page: 9
- Question: for |x|<=0.1 the bound is 1/(3*0.9^3)*(0.1)^3 = 4.57e-4, but the solution prints (0.01)^3 and 4.57e-7 (sympy). The Taylor polynomial x - x^2/2 is right.
- Needed: approve shipping with the corrected bound 4.57e-4, or leave Q6b out.
- Status: hold

## Resolved

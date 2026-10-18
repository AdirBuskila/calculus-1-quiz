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

### 21B-B Q2, Q6a, Q6b - question text missing from the only file
- Path: sitting 21B-B (full-solutions PDF; both source trees hold the identical file)
- Page: 1-3 (Q2 absent), 6-7 (Q6)
- Question: the file has no Q2 at all (p.1 ends at Q1, p.3 starts at Q3), and for Q6a/Q6b it prints only the worked solution, not the stem. Q2 is held (not-in-source). Q6a/Q6b are held (stem-not-printed) with the official solutions kept in raw. Q6a is clearly "tangent line at (1,0) to 2x^4+3x^2y^3-2sin y=2" and Q6b an area between a sideways parabola and two lines, but the exact wording is not printed.
- Needed: supply the printed stems (or approve reconstructed wording) so Q6a/b can ship; Q2 needs the original exam.
- Arbiter 2026-10-18: both copies (BSC and C24-BSC) render identically page by page; a text search of every other calculus-1 PDF in both trees finds no copy of the stems. Held items remaining: 3 (Q2, Q6a, Q6b).
- Status: hold

### 19A-C - skipped, different course
- Path: sitting 19A-C (summer 2019, moed A)
- Page: 1
- Question: the header reads course 20027 (Technology Management), lecturer-specific, not 20151. Out of scope under the same rule as the EE variants. Its Q1 solution sketch also has the axes mislabelled.
- Needed: confirm skipping it (then 17-and-older is the next batch member instead).
- Status: skipped

### Silent corrections (intermediate slips, no student-facing label; for the record)
- 20B-A Q1 (p.2): printed f'' numerator has "-2e^(2x)" inside the first bracket; it must be "+2e^(2x)" (the simplified f'' printed next is right).
- 21B-B Q3b (p.4): "0.5ln|t-3| - 0.5|t-1|" is missing the second ln; restored.
- 21B-B Q6a (held, p.6): implicit derivative printed as 8x^4, should be 8x^3; the slope 4 is unchanged.
- 21A-B Q4b (p.8): the antiderivative of 8*sqrt(y)-y is written with "+ y^2/2"; it is "- y^2/2" (inside the already-labeled Q4b).
- 21A-B Q2b (p.3-4), Q4a (p.6): not slips, but the official text ignores that arcsin(x/5) is defined only on [-5,5] and divides by a2 (assumes a2 != 0); transcribed as printed.
- 18B-A Q1 (solution p.1): the handwritten one-sided limits at x=-sqrt(3) have the signs swapped (+oo from the right, -oo from the left is correct); corrected (y is odd, check agrees).
- 18B-A Q6b (solution p.4): the L'Hopital quotient drops the factor x (x -> 1, harmless); restored.
- 18A1-A Q5a (p.5-6): the substitution line lists f(0)=0, which is outside [1,4]; it must be f(2)=4 (final max 16 / min 0 unchanged). Corrected.
- 18A1-A Q3a (p.4): the denominator derivative is printed 6x^2/cos(2x^3), it is 6x^2/cos^2(2x^3) (inside the labeled Q3a).
- 17A2-A Q6b (p.9, the Note): printed z=t^2 should be z=x^2; the substituted line carries stray letters A and B (must read 1/2 * 1/(x^2-1) - 1/2 * 1/(x^2+1)). Corrected.
- 17B-A Q2 (solution p.2): a(n+1)-a(n) is written over 2-a_n twice; it is 2+a_n (numerator 3-a_n^2 and the sign conclusion unchanged). Corrected.
- 17B-A Q3b (solution p.3): V2 line reads "9pi * integral", must be 2pi (the value 77pi/5 is right). Corrected.
- 17B-A Q4a (solution p.3): the Lagrange point is written "1<x<X"; it is c. Corrected.
- 17A1-A Q3a (p.5): middle line prints (cos x - 1)/(1+sin x); it is (1/cos x - 1)/(1+sin x) (limit 0 and answer 1 unchanged). Corrected.
- 17A1-A Q5a (p.7): f(-2) printed cbrt(36); it is cbrt(4) (max cbrt(144), min 0 unchanged). Corrected.
- 17A-A Q4a (p.5): the stem prints the function and a separate continuity sentence, each with (10%); merged into one part a. Q4b stem has a stray "Q" after dx; transcribed as dx.
- Status: logged

## Resolved

### 20A-A Q6a - official solution has the sign change backwards (intermediate slip)
- Path: sitting 20A-A (exam + official solution PDF), p.6
- Page: 6
- Question: the official solution says f' changes sign "from minus to plus" at x=3. Sympy: f'(2.5)=+0.101, f'(3.5)=-0.035, so it is plus to minus. The classification (local maximum, f(3)=e^-1.5=0.2231) is correct and unchanged.
- Needed: none.
- Status: resolved
- Ruling 2026-10-18 (fixer): intermediate slip, fixed silently in the stored solution sentence; the steps and pitfalls already said plus to minus.

### 20A-A Q6b, 19B-A Q6a - rounding slip in the step explanation
- Path: sitting 20A-A (6b, step 3, explanation); sitting 19B-A (6a, step 3, explanation)
- Page: 20A-A p.6; 19B-A p.6
- Question: 20A-A explanation printed V~0.1124 for pi(e^-2-2e^-3)=0.112347, so it is 0.1123; 19B-A explanation printed V~1.5912 for pi(pi^3/24-pi/4)=1.591311, so it is 1.5913. The numeric answers (0.1123, 1.5913) were already correct.
- Needed: none.
- Status: resolved
- Ruling 2026-10-18 (fixer): intermediate slip, corrected silently in the explanation text and checked with sympy.

### 24A-B Q6b - official solution computes a different limit than the printed one
- Path: sitting 24A-B (exam + official solution PDF)
- Page: 6 (question), 7 (solution)
- Question: the printed limit has numerator x^4 (sympy value 2); the official solution works a limit with numerator sin^2 x and answers infinity.
- Needed: decide whether the printed question or the solution is intended (the solution is transcribed in raw, the key is not trusted).
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): not a transcription error (p.6 prints x^4; the only copy). The printed question is solved (answer 2, sympy) and ships with the "הפתרון הרשמי עם תיקון" label, solved, official:false; the official sin^2 x working is kept below it as a marked note.

### 25B-B Q1-Q6 - no key
- Path: sitting 25B-B (scanned exam only)
- Page: 1-2
- Question: no solution exists; all 11 items (Q1, Q2a-b ... Q6a-b) are transcribed and held with reason no-key.
- Needed: route to the solver (no action from Adir).
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): all 11 items solved (solved, official:false, confidence high), checked in tools/verify/25B-B/check.py (0 mismatches). Q1 graph rendered to images/exams/25B-B-Q1-graph.png.

### 24A-A Q1 - official convexity claim is wrong
- Path: sitting 24A-A (exam + official solution PDF)
- Page: 1 (solution part ג)
- Question: the solution says y''<0 (concave down) for x<0, but y''=e^x(x^2-4x+6)/x^4 is positive for every x!=0 (sympy). All other parts agree.
- Needed: approve shipping the solution with the corrected convexity statement, or leave Q1 out.
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): standing label rule applied; part ג corrected (y''>0 for every x!=0), labeled, solved, official:false. Official graph kept (it is right).

### 23S-C Q4b - official volume drops the factor pi
- Path: sitting 23S-C (exam + official solution PDF)
- Page: 5 (question), 6 (solution)
- Question: the solution gives V = e-2 = 0.714; the correct volume is pi*(e-2) = 2.256 (and e-2 is 0.718, not 0.714).
- Needed: approve shipping with the corrected value, or leave Q4b out.
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): standing label rule applied; V = pi(e-2) = 2.256, labeled, solved, official:false.

### 22B-A Q1-Q6 - no key
- Path: sitting 22B-A (printed exam only)
- Page: 1-2
- Question: no solution exists; all 12 items (Q1a-b ... Q6a-b) are transcribed and held with reason no-key.
- Needed: route to the solver (no action from Adir).
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): all 12 items solved in general form for A,B,C in 0..9 (solved, official:false, confidence high), checked symbolically and for every digit in tools/verify/22B-A/check.py (0 mismatches).

### 22A-B Q5b - official arc-length decimal is off
- Path: sitting 22A-B (worked-solution PDF)
- Page: 8
- Question: the closed form is right, but the final decimal 1.98 is wrong: the exact value of the integral of sqrt(1+e^(2x)) over [0,1] is 2.0035 (sympy); the rounding of sqrt(1+e^2) to 2.9 spoils it.
- Needed: approve shipping the closed form with the corrected decimal 2.00, or leave Q5b out.
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): label rule applied; decimal corrected to 2.00 (exact 2.0035). The source is an unknown-author solution, so the label reads "הפתרון שבמקור (לא רשמי) עם תיקון". Whole sitting blind re-checked (tools/verify/22A-B/blind_recheck.py): every other answer agrees.

### 22B-B Q6b - official remainder bound uses the wrong power
- Path: sitting 22B-B (exam + official solution PDF)
- Page: 9
- Question: for |x|<=0.1 the bound is 1/(3*0.9^3)*(0.1)^3 = 4.57e-4, but the solution prints (0.01)^3 and 4.57e-7 (sympy). The Taylor polynomial x - x^2/2 is right.
- Needed: approve shipping with the corrected bound 4.57e-4, or leave Q6b out.
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): standing label rule applied; bound corrected to 4.57e-4, labeled, solved, official:false.

### 20B-C Q1-Q6 - no key
- Path: sitting 20B-C (printed exam only; joint EE + CS exam, in scope)
- Page: 1-2
- Question: no solution exists; all 11 items (Q1, Q2a-b ... Q6a-b) are transcribed and held with reason no-key.
- Needed: route to the solver (no action from Adir).
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): all 11 items solved (solved, official:false, confidence high), checked in tools/verify/20B-C/check.py (0 mismatches). Q1 graph rendered to images/exams/20B-C-Q1-graph.png. Q3a stem: the cases rows were joined by a backslash-space; fixed to row breaks (transcription). Q6b: answer ln 2 for the first-quadrant region, with a note that the third-quadrant mirror region has the same area.

### 21B-B Q3a - official conclusion names the wrong interval
- Path: sitting 21B-B (full-solutions PDF)
- Page: 3
- Question: the solution concludes that a root c lies in (-1,0), but f(0)=5>0 and f(-1)=4.04>0 (no sign change there); f(1)=-3.96<0 (printed -3.99), so the root is in (0,1). The existence proof itself is fine.
- Needed: none if the corrected label is acceptable (shipped with the "הפתרון הרשמי עם תיקון" label, official:false); say if you would rather treat it as a silent intermediate slip.
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): covered by the standing label rule; stays as shipped.

### 21A-B Q4b - handwritten solution reaches a wrong volume
- Path: sitting 21A-B (image PDF)
- Page: 7-8
- Question: the stem and solution of Q4b are on a handwritten page of unknown author. The washer set-up is right, but the arithmetic ends at pi(1184 - 224*sqrt(2)/3) = 3387.9. The correct volume is 128*pi = 402.1 (sympy, washers and shells agree).
- Needed: none if shipping the corrected solution (labeled, solved, official:false, confidence med) is acceptable; it still needs the refuter pass.
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): blind re-check gives 128*pi by shells and washers (tools/verify/21A-B/blind_recheck_q4b.py); confidence raised to high.

### 18B-A Q4b - handwritten solution ends with the wrong coefficient
- Path: sitting 18B-A (handwritten solution PDF, author not stated)
- Page: solution p.3
- Question: the written solution reaches pi^2/12 - pi/3 + (pi/6)ln2, but the step before it gives int(x - x/(1+x^2)) = 1/2 - (1/2)ln2, so the correct volume is pi^2/12 - pi/6 + (pi/6)ln2 (sympy).
- Needed: none if the corrected, labeled version is acceptable (solved, official:false, confidence med).
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): blind re-check of the whole sitting (tools/verify/18B-A/blind_recheck.py) agrees with every shipped answer, the fix included. Label reworded to "הפתרון שבמקור (לא רשמי) עם תיקון" (the key is not official); confidence high.

### 18B-A Q3b - handwritten words barely legible
- Path: sitting 18B-A (handwritten solution PDF)
- Page: solution p.3 top
- Question: the existence part (IVT on [-pi/2, 0]) is clear. The uniqueness line is partly illegible; it reads as "infinitely many solutions for x<0, since sin x takes all values in [-1,1] and 0<e^x<1". Shipped as "not unique" with an IVT argument per interval [-pi/2-2*pi*k, -2*pi*k] (numerically >= 8 roots in [-30, 0.5]).
- Needed: confirm "not unique" is the intended answer; the whole 18B-A solution is an unnamed handwritten source and needs the refuter (student-solution, official:false).
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): "not unique" is correct: no root for x>=0, one root in each [-pi/2-2pi k, -2pi k] (10 sign changes in [-30, 0.5]); shipped answer confirmed.

### 18A2-A Q1 - official extremum type and inflection x misprinted
- Page: 1-2
- Question: the text calls x=e^2 a minimum (y' goes + to -, so it is a maximum) and prints the inflection point as e^(2/3) (3 ln x = 8 gives e^(8/3), matching the printed sign diagram).
- Needed: none if the corrected, labeled version is acceptable (solved, official:false, confidence med).
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): covered by the standing label rule (final-answer error, labeled); stays as shipped.

### 18A1-A Q1 - official y'' numerator and roots misprinted
- Page: 2
- Question: y'' numerator printed -4x^2-3x-2 (correct: +2), inflection roots printed (-3 +- sqrt41)/16 and labeled (3 -+ sqrt41)/16 on the diagram (correct: (-3 +- sqrt41)/8). Sympy checked.
- Needed: none if the corrected, labeled version is acceptable.
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): covered by the standing label rule; stays as shipped.

### 18A1-A Q3a - official computes only the right-hand limit
- Page: 4
- Question: the question asks lim x->0; the solution computes x->0+ (1/3). The left limit is -1/3, so the two-sided limit does not exist. Shipped as a labeled correction (solved, official:false), with the solution showing both one-sided limits.
- Needed: confirm that the intended question was x->0+ (then the official 1/3 stands).
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): the official one-sided answer 1/3 is kept as the right-hand limit, labeled; the solution shows both one-sided limits (1/3 and -1/3, sympy) and states that the printed two-sided limit does not exist. Confidence high.

### 17B-A Q5a - handwritten solution has wrong endpoint values
- Page: solution p.4
- Question: f(1/4) written 17/2 (correct 33/2), f(100) written 52/2 (correct 251/25), maximum declared at x=100; correct maximum is 33/2 at x=1/4, minimum 3 at x=4 (sympy + grid). Shipped labeled (solved, official:false).
- Needed: none if acceptable. The whole 17B-A solution is an unnamed handwritten source and needs the refuter (student-solution, official:false).
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): blind re-check of the whole sitting (tools/verify/17B-A/blind_recheck.py) agrees with every shipped answer, the fix included. Label reworded to "הפתרון שבמקור (לא רשמי) עם תיקון"; confidence high.

### 17A-A Q6a - official Taylor approximation is miscomputed
- Page: p.7
- Question: P2(1.05) printed 1.02466875 (correct 1.0246875) and the result 1.02467 +- 1e-5 misses the true sqrt(1.05)=1.024695; correct: 1.02469 +- 1e-5 (sympy). Shipped labeled (solved, official:false).
- Needed: none if acceptable.
- Status: resolved
- Ruling 2026-10-18 (solver/arbiter): covered by the standing label rule; stays as shipped.


### 23S-C Q3b - official prints f(-3) = -59
- Page: 5
- Question: f(-3) = 2(-27)-9-3+1 = -65, the official solution prints -59. Intermediate slip: only the sign is used, the conclusion (one root) is unchanged.
- Needed: none. Corrected silently to -65 in the solution and steps.
- Status: resolved
- Ruling 2026-10-18 (fixer): standing rule for intermediate slips; no student-facing label.

### 23A-B Q2b - official says the denominator is negative
- Page: 6
- Question: in the monotonicity proof the official text says "המכנה שלילי" where the numerator 7-a_n^2 is meant (the denominator 2a_n is positive, as the next sentence says). Intermediate wording slip.
- Needed: none. Corrected silently to "המונה שלילי".
- Status: resolved
- Ruling 2026-10-18 (fixer): standing rule for intermediate slips; no student-facing label.

### 23A-B Q6b - official bound truncated to 0.00045
- Page: 7
- Question: 1/(3000*0.9^3) = 0.000457247, the official final line prints delta < 0.00045 (truncated, so not a valid upper bound). Shipped with the minimal fix delta < 0.000457, labeled, solved, official:false. ln 0.9 ~ -0.105 is unaffected.
- Needed: none if acceptable.
- Status: resolved
- Ruling 2026-10-18 (fixer): final-answer error, standing label rule applied.

### 23A-B Q1 - official uses "קעורה" for f'' > 0
- Page: 2
- Question: this sitting's official solution calls the region f''>0 "קעורה" (cup), the opposite of the convention in some other sittings. Wording kept as printed, with the symbols (cup/cap) added beside the words.
- Needed: none.
- Status: resolved
- Ruling 2026-10-18 (fixer): terminology note only.

### 22B-B Q5a, Q5b - point split not printed
- Page: 7-8
- Question: the printed solution pages show no points for Q5a and Q5b. The instructions give 20% per question and every other question is split 10+10, so 10+10 is inferred (the raw items carry no explicit points; each rubric sums to 10). It is not verifiable on the page.
- Needed: confirm the 10+10 split if it matters.
- Status: open

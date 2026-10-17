# Learn coverage - calculus-1

Source of truth: every question text in `tools/raw/*.json` (92 items across 11 sittings: 22A-A, 22B-A, 23A-B, 23B-B, 23S-C, 24A-A, 24A-B, 24B-A, 24B-B, 25B-B). Ids use the bank's scheme (sitting-Qn, with a/b/... when a number holds several topics, in raw order). Only 24B-B is built into `questions.json` so far (those ids are live links in the briefs); every other id is provisional until the bank is rebuilt.

Briefs (docs/briefs): 01 sequences_limits, 02 function_limits, 03 continuity, 04 derivatives_tangents, 05 mean_value_theorems, 06 lhopital_taylor, 07 function_investigation, 08 extrema_optimization, 09 indefinite_integrals, 10 definite_integrals, 11 cheat_sheet (formula and theorem sheet for the whole course).

| concept | brief section | example question ids |
|---|---|---|
| recursive sequence: bounded + monotone + L=f(L) | 01 מתכון: הוכחת התכנסות | 23A-B-Q2b, 23B-B-Q2b, 23S-C-Q2a, 24A-A-Q2b, 24A-B-Q2b, 24B-B-Q2b, 25B-B-Q2a, 22A-A-Q1b, 22B-A-Q2b |
| AM-GM inequality in Heron-type sequences | 01 הגדרות ומשפטים | 23A-B-Q2b, 22A-A-Q1b |
| sequence limit: 1^inf, conjugate, ratio of polynomials | 01 טכניקות | 24A-B-Q3a, 24B-B-Q3a |
| bounded times null; factorial limits | 01 טכניקות | 22A-A-Q2a, 22B-A-Q1b |
| limit forms 1^inf, 0^0, inf^0 via ln | 02 מתכונים 3-4 | 23A-B-Q5a, 23S-C-Q4a, 23S-C-Q5b, 24A-A-Q3a, 25B-B-Q3a |
| conjugate for roots at a point | 02 מתכון 2 | 25B-B-Q4a |
| oblique asymptote as a limit with parameters | 02 מתכון 7 | 24B-B-Q4b |
| nested roots at infinity; oscillating asymptotes | 02 מתכונים 8-9 | 22B-A-Q5a, 22B-A-Q3a |
| fundamental limits, equivalents | 02 גבולות יסוד, מתכון 5 | 23B-B-Q5a, 24A-B-Q6b |
| continuity with parameters, one-sided limits | 03 מתכון: פרמטרים | 23B-B-Q3b, 24A-A-Q5b, 24A-B-Q5b, 24B-A-Q3a |
| types of discontinuity (removable, 1st, 2nd kind) | 03 הגדרות, מתכון מיון | 24B-A-Q3b, 24B-A-Q3c, 24B-A-Q3d, 24B-B-Q5a, 22A-A-Q3a |
| IVT existence + uniqueness of a root | 03 מתכון: קיום ויחידות | 23B-B-Q6b, 23S-C-Q3b, 24A-B-Q6a, 24B-A-Q6a, 22B-A-Q4a |
| derivative at a point by definition; one-sided | 04 הגדרה, מתכון | 23A-B-Q5b, 25B-B-Q6b, 22A-A-Q3b, 22B-A-Q6a |
| differentiability parameters at a seam | 04 מתכון: פרמטרים | 23S-C-Q3a |
| tangent with given slope; common tangent | 04 מתכונים | 24A-B-Q4b, 22A-A-Q4a |
| implicit and logarithmic differentiation; tangent | 04 מתכונים | 23S-C-Q5a, 25B-B-Q3b |
| Lagrange inequality | 05 מתכון א | 23B-B-Q4a, 24A-A-Q6a, 25B-B-Q5a |
| auxiliary function + monotonicity inequality | 05 מתכון ב | 24B-A-Q2b, 22A-A-Q5a, 22B-A-Q2a |
| L'Hopital (0/0, inf-inf) | 06 כלל לופיטל | 24B-A-Q4a, 22A-A-Q6a |
| limit with integral bound (FTC + chain rule) | 06 אינטגרל עם גבול משתנה | 23A-B-Q3a, 23B-B-Q3a, 24A-A-Q5a, 24A-B-Q6b, 24B-A-Q4b |
| Taylor approximation + Lagrange remainder error | 06 נוסחת טיילור, מתכון | 23A-B-Q6b, 23S-C-Q6b |
| function investigation (domain..sketch), asymptotes | 07 כל הסעיפים | 23A-B-Q1, 23B-B-Q1, 23S-C-Q1, 24A-A-Q1, 24A-B-Q1, 24B-A-Q1, 24B-B-Q1, 25B-B-Q1 |
| concave/convex terminology of the course | 07 הסימונים של הקורס | all of the above |
| extrema on a closed interval (incl. f' undefined) | 08 מתכון: קטע סגור | 23S-C-Q6a, 24A-A-Q4a, 24A-B-Q4a, 24B-A-Q6b, 24B-B-Q4a, 22A-A-Q1a |
| classify critical points on the whole line | 08 משפטים | 22B-A-Q1a |
| inequality via global extremum | 08 מתכון: הוכחת אי-שוויון | 23A-B-Q4a, 24B-B-Q6a |
| integral: partial fractions (simple, repeated, quadratic) | 09 שברים חלקיים | 23A-B-Q2a, 24A-A-Q2a, 24A-B-Q2a, 24B-A-Q2a, 24B-B-Q2a, 22A-A-Q4b |
| integral: improper rational (divide first) | 09 טבלת בחירה | 23S-C-Q2b |
| integral: substitution (incl. ln x, completing the square) | 09 טבלת בחירה, השלמה לריבוע | 23A-B-Q3b, 24A-A-Q3b, 24A-B-Q5a, 24B-B-Q5b, 22B-A-Q4b |
| integral: by parts (polynomial x trig, ln, arctan) | 09 טבלת בחירה | 24B-A-Q5a, 25B-B-Q2b, 22A-A-Q2b |
| integral: t = tan(x/2); t = e^x; f'/f | 09 טבלת בחירה | 23B-B-Q2a, 23B-B-Q5b, 22B-A-Q3b, 25B-B-Q5b |
| area between curves, intersections, split | 10 מתכון: שטח | 23A-B-Q6a, 24A-A-Q6b, 24A-B-Q4b, 24B-A-Q5b, 24B-B-Q6b, 25B-B-Q4b, 22A-A-Q5b |
| volume by discs/washers about x | 10 מתכון: נפח | 23A-B-Q4b, 23S-C-Q4b, 24A-A-Q4b, 24A-B-Q3b, 25B-B-Q6a |
| volume by shells about y | 10 מתכון: נפח | 23B-B-Q4b, 24B-B-Q3b, 22A-A-Q6b, 22B-A-Q6b |
| arc length | 10 נוסחאות | 23B-B-Q6a, 22B-A-Q5b |

## Gaps

None of the concepts used by the 92 transcribed items is missing from the briefs. Open items:
- Sittings 22A-B and 22B-B (page renders exist under `tools/raw/`) are not transcribed yet. Their question texts were not read, so their concepts are unchecked. Rerun this coverage pass after they land. Their image names suggest function investigation, volume and area questions, which the briefs cover.
- The older sittings (2013-2016, outside the current cutoff) are not in the bank.
- 25B-B has no key, so its method rows are matched from the question text alone.
- Improper integrals and numeric series were never seen in the in-scope exams, so the briefs do not teach them. If the syllabus examines them, add a brief section (Gate 1 flagged this as unconfirmed).
- Peano-form Taylor expansions and little-o notation are not in the briefs; none of the questions needed them.
- Thin topics: mean_value_theorems (no Rolle-style question appeared, Rolle is only stated) and extrema_optimization (word-problem optimization has no exam instance, only a recipe).

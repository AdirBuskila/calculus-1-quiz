# STATUS - calculus-1

Resume here: phase 7 - ship (awaiting Adir): QA done 2026-10-18, bank 240 questions / 22 sittings, 4 guided courses; Gate 3 (going public) and the deck redesign are still open
Opus sessions: not tracked in this repo (orchestrator keeps the count)
Engine: open   Format: open (computation + proof, no MCQ)   Cutoff: 2017 onward

Triage material (private, names students, never copied into this repo): C:\Users\Adir\Desktop\Coding\Dev\course-factory\courses\calculus-1\format_triage.md (rulings in GATE1.md next to it)

Gates 1, 2 and 7 always stop for Adir.

- [x] Phase 0 - intake
  - [x] registry entry exists (course-factory courses.json, status triaged/open)
  - [x] source folder exists and is non-empty (see course.config.json sourceFolder; triage inventory in the factory)
- [x] Phase 1 - triage  (GATE 1: Adir approves format, cutoff, topics)
  - [x] triager run per subfolder (factory courses/calculus-1/triage/)
  - [x] format_triage.md merged (verdict, cutoff, topics, engine choice)
  - [x] approved: ruled by the orchestrator under Adir's 2026-10-17 autonomy grant, recorded in the factory GATE1.md (Adir can override)
  - [x] config.overlay.json written, app repo scaffolded (triage stays in the factory)
- [ ] Phase 2 - flagship  (GATE 2: Adir tries it in the browser)
  - [x] topic taxonomy chosen (course.config.json topics)
  - [x] flagship sitting transcribed + validated (24B-B, 12/08/2024)
  - [x] steps (open questions) + refuter pass (tools/verify/_verify_24B-B.json)
  - [x] smoke / verify_dom green, running locally (verify_dom.js all ok 2026-10-18)
  - [ ] Adir tried it
- [x] Phase 3 - bank
  - [x] all in-scope sittings transcribed (22 raw files in the bank; 4 out-of-scope variants kept in raw only)
  - [x] validate.py clean (0 problems, 243 items incl. 3 held)
  - [x] solver run for questions with no trustworthy solution (25B-B etc.; tools/verify/<CODE>/blind_recheck.py)
  - [x] refuter: tools/raw/_verify_<CODE>.json for all 22 sittings
  - [x] arbiter / ASK_ADIR for disagreements (docs/ASK_ADIR.md Resolved section)
  - [x] completeness check per exam (build_report.md per-exam counts; 21B-B holds listed)
- [x] Phase 4 - steps
  - [x] step-author batches done for every open question
  - [x] rubricSource / stepsSource labeled
  - [x] refuter on every steps block (build_report: ai-draft parts stripped 0)
- [x] Phase 5 - learn
  - [x] learn-writer per topic (docs/briefs, 11 chapters)
  - [x] coverage report: no gaps (docs/learn_coverage.md, re-passed against the full 240-item bank on 2026-10-18; 4 sections added)
- [x] Phase 5b - need help
  - [x] 4 course areas in course.config.json needHelp
  - [x] lessons + coverage table complete, level questions (courses/*/C0*.js)
  - [x] course_lint.js --strict: 0 errors, all levels ai-verified; refuter verdicts in tools/verify/needhelp/
  - [x] tools/redact.txt filled, validate.py clean
- [x] Phase 6 - QA
  - [x] validate, build_questions, build_learn, build_courses, verify_dom, verify_learn, test_aiprompt, test_normalize green
  - [x] shoot.js screenshots taken (390px + 1000px, both themes) and read by hand
  - [x] sweep done by the QA agent (no render-checker run); remaining bidi items listed in the QA report
- [ ] Phase 7 - ship  (GATE 3: Adir OKs going public)
  - [ ] deck redesign done (else stop and tell Adir)
  - [x] .gitignore excludes raw PNGs, favicon.svg linked, GoatCounter in index.html, .nojekyll present
  - [ ] year range checked against data (page text names no years; README absent)
  - [ ] Adir OK to go public
  - [ ] GitHub repo + Pages live
  - [ ] deck tile added
  - [ ] registry status = live

## Notes
- Bank: 240 questions (196 computation, 44 proof), 3 held (21B-B Q2, Q6a, Q6b), 22 sittings 17A-A to 25B-B. Guided courses: investigation (9 levels), recursive_seq (8), integration (9), mvt_ineq (9).
- QA 2026-10-18: convexity wording rule applied (every qamura/qaura has the cup/cap symbol by the sign of f''), "official solution" wording removed from non-official items, raw backslash-quote fixed in two course explanations, recaps with raw TeX wrapped in math, mobile display-math font slightly smaller.

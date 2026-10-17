# Independent numeric re-check (mpmath, no sympy) of every numeric guided step in tools/raw/<CODE>.json.
# `expected` lists the values in the order the numeric steps appear in the file (question order, then step order).
import json, pathlib, sys


def run(code, expected):
    raw = pathlib.Path(__file__).resolve().parents[1] / "raw" / f"{code}.json"
    d = json.loads(raw.read_text(encoding="utf-8"))
    got = [(q["num"], s["answer"], s["tol"]) for q in d["questions"] for s in q.get("steps", []) if s["type"] == "numeric"]
    assert len(got) == len(expected), (len(got), len(expected))
    bad = 0
    for (num, ans, tol), e in zip(got, expected):
        e = float(e)
        if abs(ans - e) > max(tol, 1e-9):
            bad += 1
            print("MISMATCH Q%d: stored %r vs independent %r" % (num, ans, e))
    print(code, len(got), "numeric steps checked,", bad, "mismatches")
    sys.exit(1 if bad else 0)

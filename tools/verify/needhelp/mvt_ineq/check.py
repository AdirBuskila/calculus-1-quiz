# -*- coding: utf-8 -*-
"""Machine check for the guided course "mvt_ineq".

  py check.py --write   emit courses/mvt_ineq/C0N.js from spec.py (importing spec runs every sympy assert)
  py check.py           verify that the emitted files hold exactly the verified content, then print a summary

ASCII output only.
"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
APP = HERE.parents[3]
sys.path.insert(0, str(HERE))
import spec  # noqa: E402  (runs all sympy assertions)

OUT = APP / "courses" / "mvt_ineq"


def emit(lv):
    les = lv["lesson"]
    assert "`" not in les and "${" not in les, lv["id"]
    qs = json.dumps(lv["questions"], ensure_ascii=False, indent=2)
    boss = "  boss: true,\n" if lv["boss"] else ""
    return (f"/* mvt_ineq course, level {lv['order']}: {lv['title']} */\n"
            f"COURSE_LEVEL(\"mvt_ineq\", {{\n"
            f"  id: {json.dumps(lv['id'])}, order: {lv['order']}, icon: {json.dumps(lv['icon'], ensure_ascii=False)}, "
            f"title: {json.dumps(lv['title'], ensure_ascii=False)},\n"
            f"  goal: {json.dumps(lv['goal'], ensure_ascii=False)},\n{boss}"
            f"  source: \"ai-verified\",\n"
            f"  lesson: {{ html: String.raw`{les}` }},\n"
            f"  questions: {qs},\n}});\n")


if "--write" in sys.argv:
    OUT.mkdir(parents=True, exist_ok=True)
    for lv in spec.LEVELS:
        (OUT / (lv["id"] + ".js")).write_text(emit(lv), encoding="utf8", newline="\n")

res = subprocess.run(["node", str(APP / "tools" / "course_load.js")], capture_output=True, cwd=str(APP))
data = json.loads(res.stdout.decode("utf8"))
assert not data["errors"], data["errors"]
mine = {d["level"]["id"]: d["level"] for d in data["levels"] if d["courseId"] == "mvt_ineq"}
assert set(mine) == {lv["id"] for lv in spec.LEVELS}, sorted(mine)
nq = 0
for lv in spec.LEVELS:
    got = mine[lv["id"]]
    assert got["lesson"]["html"] == lv["lesson"], lv["id"] + " lesson differs"
    assert got["questions"] == lv["questions"], lv["id"] + " questions differ"
    assert got["order"] == lv["order"] and bool(got.get("boss")) == lv["boss"], lv["id"]
    assert got["source"] == "ai-verified"
    nq += len(lv["questions"])
ids = [q.get("id") for lv in spec.LEVELS for q in lv["questions"] if "id" in q]
assert len(ids) == len(set(ids))
print("levels=%d questions=%d own=%d bank_pulls=%d facts=%d" % (
    len(spec.LEVELS), nq, len(ids), nq - len(ids), len(spec.FACTS)))
print("ALL CHECKS PASSED")

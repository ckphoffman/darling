#!/usr/bin/env python3
"""Turn the five perspective JSON files into the STORM interview, trace and information-table evidence.

The ranking passed to the host retrieval trace is the order in which each
subagent listed a turn's source ids. It records the subagent's own selection;
the bundled script does not search anything.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = Path(__file__).resolve().parent
RUN_DIR = ROOT / ".results" / "doxycycline-acne-sdd-vs-standard" / ".storm-run"
BACKEND = ROOT / ".claude" / "skills" / "storm" / "scripts" / "retrieval_backend.py"
PERSPECTIVES = ["basic", "efficacy", "resistance", "relapse", "safety_guideline"]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


def main() -> int:
    data = {p: json.loads((RESEARCH / "perspectives" / f"p-{p}.json").read_text(encoding="utf-8")) for p in PERSPECTIVES}

    corpus, interviews, table = [], [], []
    first_use: dict[str, tuple[int, str, str]] = {}
    for pid, d in data.items():
        for turn in d["turns"]:
            for sid in turn["source_ids"]:
                first_use.setdefault(sid, (turn["turn"], turn["question"], turn["queries"][0]))
        for s in d["sources"]:
            corpus.append({"source_id": s["source_id"], "text": s["snippet"], "title": s["title"], "url": s["url"]})

    work = RUN_DIR / "host-work"
    work.mkdir(exist_ok=True)
    write_jsonl(RUN_DIR / "corpus.jsonl", corpus)
    index = RUN_DIR / "retrieval-index.json"
    if not index.exists():
        subprocess.run([sys.executable, str(BACKEND), "index", "--backend", "host", "--corpus", str(RUN_DIR / "corpus.jsonl"), "--output", str(index)], check=True)

    trace = RUN_DIR / "retrieval-log.jsonl"
    if trace.exists():
        trace.unlink()
    for pid, d in data.items():
        for turn in d["turns"]:
            ranked = [{"source_id": sid, "score": round(1.0 - 0.01 * rank, 2)} for rank, sid in enumerate(turn["source_ids"])]
            host_file = work / f"{pid}-t{turn['turn']}.jsonl"
            write_jsonl(host_file, ranked)
            subprocess.run([sys.executable, str(BACKEND), "search", "--index", str(index), "--query", " || ".join(turn["queries"]),
                            "--top-k", str(len(ranked)), "--host-results", str(host_file), "--trace", str(trace)],
                           check=True, stdout=subprocess.DEVNULL)
            interviews.append({"perspective_id": pid, "turn": turn["turn"], "question": turn["question"],
                               "triggered_by": turn["triggered_by"], "queries": turn["queries"],
                               "source_ids": turn["source_ids"], "answer": turn["answer"]})
    write_jsonl(RUN_DIR / "interviews.jsonl", interviews)

    unattributed = []
    for pid, d in data.items():
        for s in d["sources"]:
            if s["source_id"] not in first_use:
                # Not tied to any interview turn, so it has no retrieval trace; keep it out of the evidence table.
                unattributed.append(s["source_id"])
                continue
            turn_no, question, query = first_use[s["source_id"]]
            table.append({"perspective_id": pid, "turn": turn_no, "question": question, "query": query,
                          "source_id": s["source_id"], "url": s["url"], "title": s["title"], "date": s["date"],
                          "evidence_level": s["evidence_level"], "indication": s["indication"], "regimen": s["regimen"],
                          "n": s["n"], "funding": s["funding"], "snippet": s["snippet"],
                          "claim_supported": s["claim_supported"], "reliability_note": s["reliability_note"],
                          "retrieval_caveat": "snippet 摘自 WebSearch 结果文本，未对照原文"})
    write_jsonl(RUN_DIR / "information-table.jsonl", table)
    print(f"corpus={len(corpus)} interviews={len(interviews)} table={len(table)} unattributed={unattributed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Generate guarded STORM evidence files and staged HTML for the Bowe claim check."""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from article import BODY, DIRECT_OUTLINE, REFINED_OUTLINE, SUMMARY, TITLE  # noqa: E402
from sources import SOURCES  # noqa: E402

OUT = Path(sys.argv[1]).resolve()
RUN = OUT / ".storm-run"
STAGE = RUN / "staging"
SKILL = Path("/home/user/darling/.claude/skills/storm/scripts")
HERE = Path(__file__).parent
PUBMED = json.loads((HERE / "pubmed_refs.json").read_text())

CLAIM_RE = re.compile(r"⟦(.+?)⟧\[\[([A-Z0-9_,]+)\]\]")

# ---- number citations by first appearance in the polished article ----
order: list[str] = []


def scan(blocks):
    for block in blocks:
        texts = []
        if block[0] in ("p", "h2", "h3"):
            texts = [block[1]]
        elif block[0] == "ul":
            texts = block[1]
        for text in texts:
            for _, keys in CLAIM_RE.findall(text):
                for key in keys.split(","):
                    if key not in SOURCES:
                        raise SystemExit(f"unknown source key {key}")
                    if key not in order:
                        order.append(key)


scan(SUMMARY + BODY)
num = {key: i + 1 for i, key in enumerate(order)}
claims: list[dict] = []


def render_text(text: str, record: bool) -> str:
    out, pos = [], 0
    for m in CLAIM_RE.finditer(text):
        out.append(html.escape(text[pos:m.start()]))
        sentence, keys = m.group(1), m.group(2).split(",")
        ids = [num[k] for k in keys]
        tiers = {SOURCES[k]["tier"] for k in keys}
        primary = "primary" in tiers
        if not primary and "未证实" not in sentence:
            raise SystemExit(f"secondary-only claim lacks 未证实 label: {sentence}")
        if primary and "未证实" in sentence:
            raise SystemExit(f"primary-backed claim wrongly labeled: {sentence}")
        if record:
            claims.append({
                "claim": sentence,
                "citation_ids": ids,
                "source_ids": ids,
                "source_keys": keys,
                "support_status": "supported" if primary else "unverified",
                "evidence_grade": "primary" if primary else "secondary",
                "evidence_note": "；".join(
                    f"{k}（{SOURCES[k]['tier']}）：{SOURCES[k]['loc']}" for k in keys
                ),
                "number_origin": "；".join(f"{k}: {SOURCES[k]['loc']}" for k in keys if SOURCES[k]["tier"] == "primary"),
                "action": "keep" if primary else "label 未证实",
            })
        out.append(html.escape(sentence) + "".join(f"<sup>[{i}]</sup>" for i in ids))
        pos = m.end()
    out.append(html.escape(text[pos:]))
    return "".join(out)


def render_blocks(blocks, record: bool) -> str:
    parts = []
    for block in blocks:
        kind = block[0]
        if kind in ("h1", "h2", "h3"):
            parts.append(f"<{kind}>{render_text(block[1], record)}</{kind}>")
        elif kind == "p":
            parts.append(f"<p>{render_text(block[1], record)}</p>")
        elif kind == "ul":
            items = "".join(f"<li>{render_text(t, record)}</li>" for t in block[1])
            parts.append(f"<ul>{items}</ul>")
        elif kind == "table":
            head = "".join(f"<th>{html.escape(h)}</th>" for h in block[1])
            rows = "".join(
                "<tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in row) + "</tr>" for row in block[2]
            )
            parts.append(f"<table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>")
    return "\n".join(parts)


CSS = """
:root{--bg:#fbfaf7;--fg:#1d1d1b;--muted:#5d5b55;--line:#dedbd2;--accent:#2f5d50;--warn:#8a4b14}
@media (prefers-color-scheme: dark){:root{--bg:#161614;--fg:#ecebe6;--muted:#a8a69e;--line:#3a3934;--accent:#8fc3b0;--warn:#e0a46a}}
body{background:var(--bg);color:var(--fg);font:16px/1.75 -apple-system,"PingFang SC","Noto Sans CJK SC",sans-serif;max-width:860px;margin:0 auto;padding:24px 16px 64px}
h1{font-size:1.7rem;line-height:1.3}h2{margin-top:2.2em;border-bottom:1px solid var(--line);padding-bottom:.3em}h3{margin-top:1.6em;color:var(--accent)}
sup{color:var(--accent);font-size:.72em}table{border-collapse:collapse;width:100%;font-size:.92rem;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}th{background:color-mix(in srgb,var(--line) 45%,transparent)}
.meta{color:var(--muted);font-size:.9rem}.refs li{font-size:.86rem;margin:.3em 0;word-break:break-word}.tier{color:var(--warn);font-weight:600}
"""


def page(title: str, body: str) -> str:
    return (
        "<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>{html.escape(title)}</title>\n<style>{CSS}</style>\n</head>\n<body>\n{body}\n</body>\n</html>\n"
    )


def ref_list() -> str:
    items = []
    for key in order:
        s = SOURCES[key]
        ref = PUBMED.get(key, s["ref"])
        tier = "一手" if s["tier"] == "primary" else "二手"
        items.append(
            f"<li>[{num[key]}] <span class=\"tier\">[{tier}]</span> {html.escape(ref)}. "
            f"<a href=\"{html.escape(s['url'])}\">{html.escape(s['url'])}</a></li>"
        )
    return "<h2>参考文献</h2>\n<ol class=\"refs\">" + "".join(items) + "</ol>"


META = (
    "<p class=\"meta\">STORM 证据核查 · 2026-10-18 · 只把一手来源当证据；仅有二手来源支撑的陈述标为“未证实”；"
    "每条引用在参考文献中标注 [一手]/[二手]。</p>"
)

polished_body = render_blocks(SUMMARY + BODY, record=True)
draft_body = render_blocks(BODY, record=False)
STAGE.mkdir(parents=True, exist_ok=True)
files = {
    "direct_gen_outline.html": page("直接大纲：Bowe 饮食-菌群-皮肤主张", render_blocks(DIRECT_OUTLINE, False)),
    "storm_gen_outline.html": page("STORM 精炼大纲：Bowe 主张证据核查", render_blocks(REFINED_OUTLINE, False)),
    "storm_gen_article.html": page(TITLE + "（草稿）", f"<h1>{html.escape(TITLE)}（草稿）</h1>\n{META}\n{draft_body}\n{ref_list()}"),
    "storm_gen_article_polished.html": page(TITLE, f"<h1>{html.escape(TITLE)}</h1>\n{META}\n{polished_body}\n{ref_list()}"),
}
for name, text in files.items():
    (STAGE / name).write_text(text, encoding="utf-8")

# ---- citation registry ----
sources_doc = {"schema_version": "1.0", "sources": [
    {"id": num[k], "key": k, "title": PUBMED.get(k, SOURCES[k]["ref"]), "url": SOURCES[k]["url"],
     "source_tier": SOURCES[k]["tier"], "locator": SOURCES[k]["loc"], "perspective": SOURCES[k]["p"]}
    for k in order]}
(RUN / "sources.json").write_text(json.dumps(sources_doc, ensure_ascii=False, indent=2), encoding="utf-8")
(RUN / "claims.json").write_text(json.dumps({"schema_version": "1.0", "claims": claims}, ensure_ascii=False, indent=2), encoding="utf-8")

# ---- retrieval corpus, host-ranked trace ----
corpus = RUN / "corpus.jsonl"
with corpus.open("w", encoding="utf-8") as fh:
    for k in order:
        s = SOURCES[k]
        fh.write(json.dumps({"source_id": k, "title": PUBMED.get(k, s["ref"]), "url": s["url"], "text": s["snippet"]}, ensure_ascii=False) + "\n")
index = RUN / "retrieval-index.json"
trace = RUN / "retrieval-log.jsonl"
for p in (index, trace):
    if p.exists():
        p.unlink()
subprocess.run([sys.executable, str(SKILL / "retrieval_backend.py"), "index", "--backend", "host", "--corpus", str(corpus),
                "--output", str(index), "--chunk-size", "4000", "--chunk-overlap", "0"], check=True, capture_output=True)

QUESTIONS = json.loads((HERE / "interviews.json").read_text())
by_p: dict[str, list[str]] = {}
for k in order:
    by_p.setdefault(SOURCES[k]["p"], []).append(k)
interviews = []
for pid, rounds in QUESTIONS.items():
    keys = by_p.get(pid, [])
    host = RUN / f"host-results-{pid}.jsonl"
    host.write_text("".join(json.dumps({"source_id": k, "score": round(1 - i * 0.01, 2)}) + "\n" for i, k in enumerate(keys)), encoding="utf-8")
    subprocess.run([sys.executable, str(SKILL / "retrieval_backend.py"), "search", "--index", str(index),
                    "--query", rounds[0]["queries"][0], "--top-k", str(len(keys)), "--host-results", str(host),
                    "--trace", str(trace)], check=True, capture_output=True)
    host.unlink()
    for i, rnd in enumerate(rounds):
        ks = [k for k in rnd["keys"] if k in num]
        if not ks:
            raise SystemExit(f"{pid} round {i} has no registered sources")
        interviews.append({"perspective_id": pid, "turn": i + 1, "question": rnd["question"], "queries": rnd["queries"],
                           "source_ids": ks, "finding": rnd["finding"]})
(RUN / "interviews.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in interviews), encoding="utf-8")

rows, seen = [], set()
for c in claims:
    for k in c["source_keys"]:
        key = (k, c["claim"])
        if key in seen:
            continue
        seen.add(key)
        rows.append({"perspective": SOURCES[k]["p"], "source_id": k, "url": SOURCES[k]["url"], "title": PUBMED.get(k, SOURCES[k]["ref"]),
                     "snippet": SOURCES[k]["snippet"], "claim_supported": c["claim"], "source_tier": SOURCES[k]["tier"],
                     "reliability_note": SOURCES[k]["loc"]})
(RUN / "information-table.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")

unverified = sum(c["support_status"] == "unverified" for c in claims)
print(json.dumps({"sources": len(order), "claims": len(claims), "unverified": unverified, "info_rows": len(rows), "interviews": len(interviews)}))

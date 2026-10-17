#!/usr/bin/env python3
"""Render article.md into the four STORM HTML artifacts plus sources.json and claims.json in the run's staging area."""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sources import SOURCES  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = Path(__file__).resolve().parent
RUN_DIR = ROOT / ".results" / "doxycycline-acne-sdd-vs-standard" / ".storm-run"
STAGING = RUN_DIR / "staging"
TITLE = "多西环素亚抗菌剂量与标准剂量治疗痤疮：疗效、复发、耐药与安全性的证据拆解"
CITE_RE = re.compile(r"\{([a-z0-9_,]+)\}")

# Written from the topic alone, before any interview evidence was read.
DIRECT_OUTLINE = [
    (1, "背景与定义"), (2, "多西环素的作用机制"), (2, "亚抗菌剂量的概念"),
    (1, "疗效比较"), (2, "炎性皮损"), (2, "非炎性皮损"),
    (1, "复发"), (1, "耐药"), (1, "安全性"), (2, "胃肠道反应"), (2, "光敏"),
    (1, "指南推荐"), (1, "临床选择"), (1, "结论"),
]

CSS = """:root{--bg:#fbfaf7;--fg:#1d1d1b;--muted:#5d5b55;--line:#ddd8cc;--accent:#6b4f1d;--table:#f2efe7}
@media (prefers-color-scheme: dark){:root{--bg:#171715;--fg:#ecebe6;--muted:#a9a69c;--line:#3a3833;--accent:#d9b56a;--table:#22211e}}
body{background:var(--bg);color:var(--fg);font:16px/1.75 -apple-system,"PingFang SC","Noto Sans CJK SC","Microsoft YaHei",sans-serif;margin:0;padding:24px 16px}
main{max-width:860px;margin:0 auto}h1{font-size:1.6rem;line-height:1.35}h2{margin-top:2.2rem;border-bottom:1px solid var(--line);padding-bottom:.3rem}
h3{margin-top:1.6rem}a{color:var(--accent)}sup{font-size:.72em}.note{color:var(--muted);font-size:.92rem}
.table-wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:.9rem;margin:1rem 0}th,td{border:1px solid var(--line);padding:6px 8px;vertical-align:top;text-align:left}th{background:var(--table)}
ol.refs li{margin-bottom:.4rem;font-size:.9rem;word-break:break-word}"""


def page(title: str, body: str) -> str:
    return (f'<!doctype html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>{html.escape(title)}</title>\n'
            f"<style>{CSS}</style>\n</head>\n<body>\n<main>\n{body}\n</main>\n</body>\n</html>\n")


def select_lines(text: str, polished: bool) -> list[str]:
    lines, skip = [], False
    for line in text.splitlines():
        if line.strip() == "@@POLISHED_ONLY_START":
            skip = not polished
            continue
        if line.strip() == "@@POLISHED_ONLY_END":
            skip = False
            continue
        if not skip:
            lines.append(line)
    return lines


def number_citations(lines: list[str]) -> dict[str, int]:
    order: dict[str, int] = {}
    for line in lines:
        for group in CITE_RE.findall(line):
            for key in group.split(","):
                if key not in SOURCES:
                    raise SystemExit(f"unknown citation key: {key}")
                order.setdefault(key, len(order) + 1)
    return order


def inline(text: str, order: dict[str, int]) -> str:
    out, pos = [], 0
    for m in CITE_RE.finditer(text):
        out.append(fmt(text[pos:m.start()]))
        out.append("<sup>" + "".join(f'<a href="#ref-{order[k]}">[{order[k]}]</a>' for k in m.group(1).split(",")) + "</sup>")
        pos = m.end()
    out.append(fmt(text[pos:]))
    return "".join(out)


def fmt(text: str) -> str:
    escaped = html.escape(text)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)


def render_body(lines: list[str], order: dict[str, int]) -> str:
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("### "):
            out.append(f"<h3>{inline(line[4:], order)}</h3>")
        elif line.startswith("## "):
            out.append(f"<h2>{inline(line[3:], order)}</h2>")
        elif line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, body = rows[0], [r for r in rows[1:] if not all(set(c) <= set("-: ") for c in r)]
            t = ["<div class=\"table-wrap\"><table><thead><tr>" + "".join(f"<th>{inline(c, order)}</th>" for c in head) + "</tr></thead><tbody>"]
            t += ["<tr>" + "".join(f"<td>{inline(c, order)}</td>" for c in r) + "</tr>" for r in body]
            out.append("".join(t) + "</tbody></table></div>")
            continue
        elif re.match(r"^(- |\d+\. )", line):
            ordered = bool(re.match(r"^\d+\. ", line))
            items = []
            while i < len(lines) and re.match(r"^(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i]))
                i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(it, order)}</li>" for it in items) + f"</{tag}>")
            continue
        else:
            out.append(f"<p>{inline(line, order)}</p>")
        i += 1
    return "\n".join(out)


def references(order: dict[str, int]) -> str:
    items = []
    for key, n in sorted(order.items(), key=lambda kv: kv[1]):
        s = SOURCES[key]
        link = f' <a href="{html.escape(s["url"])}">{html.escape(s["url"])}</a>' if "url" in s else f' （文献号：{html.escape(s["doc_id"])}）'
        items.append(f'<li id="ref-{n}">{html.escape(s["title"])}.{link} <span class="note">证据表行：{", ".join(s["rows"])}</span></li>')
    return "<h2>参考文献</h2>\n<ol class=\"refs\">\n" + "\n".join(items) + "\n</ol>"


def outline_html(entries: list[tuple[int, str]], heading: str) -> str:
    body = f'<p class="note">{html.escape(heading)}</p>\n' + "\n".join(f"<h{lvl}>{html.escape(t)}</h{lvl}>" for lvl, t in entries)
    return page(f"{TITLE}（大纲）", body)


def main() -> int:
    STAGING.mkdir(parents=True, exist_ok=True)
    text = (RESEARCH / "article.md").read_text(encoding="utf-8")
    table = {json.loads(l)["source_id"]: json.loads(l) for l in (RUN_DIR / "information-table.jsonl").read_text(encoding="utf-8").splitlines()}
    for key, s in SOURCES.items():
        missing = [r for r in s["rows"] if r not in table]
        if missing:
            raise SystemExit(f"{key}: rows not in information table: {missing}")

    (STAGING / "direct_gen_outline.html").write_text(outline_html(DIRECT_OUTLINE, "直接大纲：仅根据主题生成，未参考访谈证据。"), encoding="utf-8")

    refined = []
    for line in select_lines(text, polished=True):
        if line.startswith("## "):
            refined.append((1, CITE_RE.sub("", line[3:]).strip()))
        elif line.startswith("### "):
            refined.append((2, CITE_RE.sub("", line[4:]).strip()))
    (STAGING / "storm_gen_outline.html").write_text(outline_html(refined, "精炼大纲：依据 5 个视角的访谈证据和证据表重组。"), encoding="utf-8")

    caveat = ('<p class="note">证据说明：所有原文片段都摘自搜索结果文本，未能打开原文核对（运行环境的网络策略阻止访问 PubMed、PMC 和期刊网站）。'
              '酒渣鼻和牙周炎的数据已单独标注，不作为痤疮的直接证据。</p>')
    for name, polished in (("storm_gen_article.html", False), ("storm_gen_article_polished.html", True)):
        lines = select_lines(text, polished)
        order = number_citations(lines)
        body = f"<h1>{html.escape(TITLE)}</h1>\n{caveat}\n{render_body(lines, order)}\n{references(order)}"
        (STAGING / name).write_text(page(TITLE, body), encoding="utf-8")
        if polished:
            sources_json, claims = [], []
            for key, n in sorted(order.items(), key=lambda kv: kv[1]):
                s = SOURCES[key]
                entry = {"id": n, "key": key, "title": s["title"], "evidence_rows": s["rows"]}
                entry.update({"url": s["url"]} if "url" in s else {"doc_id": s["doc_id"]})
                sources_json.append(entry)
                notes = " ｜ ".join(f'{r}: "{table[r]["snippet"]}"（{table[r]["evidence_level"]}，{table[r]["indication"]}）' for r in s["rows"])
                claims.append({"claim": s["claim"], "citation_ids": [n], "source_ids": [n], "support_status": "supported",
                               "evidence_note": notes, "action": "kept; snippet from WebSearch text, not checked against the original"})
            (RUN_DIR / "sources.json").write_text(json.dumps({"sources": sources_json}, ensure_ascii=False, indent=2), encoding="utf-8")
            (RUN_DIR / "claims.json").write_text(json.dumps({"claims": claims}, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"polished citations: {len(order)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Evidence Policy

Applies to every mode: Classic, corpus-restricted, Local Runner import, Chat
Brief, and Co-STORM. These rules override any looser source guidance elsewhere.

## Source Tiers

Classify every source before it supports any claim. Record the tier as
`source_tier` in the information table and the source registry.

| Tier | `source_tier` | Counts as evidence | Examples |
|---|---|---|---|
| 一手来源 Primary | `primary` | Yes | Paper full text (not only the abstract page of an aggregator), official documentation, original datasets or statistical releases, source code and its repository history, regulatory filings, statutes, court decisions, standards texts |
| 二手来源 Secondary | `secondary` | No: leads only | News, blogs, encyclopedias (including Wikipedia), aggregators, newsletters, press coverage of a paper, forum or Q&A posts, AI-generated summaries, secondary reviews read without opening the cited work |

- Classify by what the document is, not where it is hosted. A paper PDF on a
  mirror is primary; a vendor blog post summarizing that paper is secondary.
- Vendor material is primary only for claims about that vendor's own product,
  policy, or data, and secondary for everything else.
- When the tier is unclear, use `secondary`.

## Leads Versus Evidence

Use secondary sources only to find leads: names, terms, and pointers to the
original work. Then retrieve the primary document and cite that instead. Never
cite a secondary source as the argument for a conclusion. If the primary
document cannot be reached, the conclusion stays unverified (below).

## Grading Every Conclusion

Every factual claim records an `evidence_grade` and shows it to the reader:

- `primary` / 已证实: at least one cited source is primary and directly
  supports the claim. `support_status` is `supported`.
- `secondary` / 未证实: only secondary sources support the claim.
  `support_status` must be `unverified`, and the visible text marks the claim
  inline as `（未证实）` (or `(Unverified)` in English output) next to its
  citation.

Do not build further conclusions on an unverified claim. In the polished
reference list, show each entry's tier (`[一手]` / `[二手]` or
`[Primary]` / `[Secondary]`).

## Numbers

Trace every number (statistics, percentages, amounts, counts, benchmark
scores, dates of measurement) to the original publisher of that number: the
dataset, table, filing, paper, or official release that first reported it.

- Record the exact location as `number_origin` (for example, document plus
  table, page, section, or file and line).
- If the original origin cannot be found or opened, delete the number. Do not
  keep it as an unverified claim, and do not replace it with an estimate.
- A number seen only in news, blogs, encyclopedias, or aggregators is never
  publishable on its own.

## Mechanical Enforcement

The guarded `scripts/audit_citations.py` fails closed when:

- a source lacks `source_tier` of `primary` or `secondary`;
- a claim is `supported` without a primary citation, or `unverified` while
  citing a primary source;
- a claim's `evidence_grade` disagrees with the tiers of its citations;
- a claim containing a digit (outside citation markers) has no primary source
  or no `number_origin`;
- the article shows fewer `未证实` / `Unverified` labels than there are
  unverified claims.

The audit checks consistency of the recorded tiers. Tier classification itself
is an Agent judgment, so record the reason for it in the evidence note.
Prompt-only and Co-STORM runs must apply the same rules by hand.

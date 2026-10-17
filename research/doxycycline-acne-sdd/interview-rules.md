# STORM 视角访谈：通用规则（所有子 agent 适用）

研究主题：痤疮治疗中，多西环素亚抗菌剂量（SDD，如 20 mg bid 或 40 mg 改良释放剂型每日一次，长疗程）与标准抗菌剂量（50–200 mg/d，常用 100 mg/d，约 12–16 周）在疗效、复发、耐药、安全性上的差异。

## 工具
先调用 ToolSearch，query 设为 "select:WebSearch,WebFetch"，加载这两个工具。WebSearch 的 mode 默认用 "standard"；结果太少或太偏时再用 "extended"。用 WebFetch 抓取 PubMed 或 PMC 摘要和全文，获取原文片段。

## 访谈流程
- 最多 3 轮。每轮：提出 1 个新问题，最多 3 条检索词，实际执行检索，然后只根据检索到的内容作答。
- 第 2、3 轮的问题必须由上一轮新发现的具体信息引出，例如某篇研究的设计缺陷、某个指南引用的原始研究、某个出乎意料的数字。在 `triggered_by` 中写明是哪个来源的哪条信息。不要按综述目录列问题。
- 证据主体是原始研究，按下列等级标注 `evidence_level`：
  `H2H-RCT` > `placebo-RCT` > `cohort` > `case-series`。
  其他类型：`pharmacology/PK`、`in-vitro`、`review`、`guideline-position`、`regulatory`。
- 指南和专家共识不作为证据，标为 `guideline-position`，记录推荐原文和引用的原始研究，并尽量追查这些原始研究，判断该推荐是来自证据，还是来自谨慎或公共卫生考量。
- 每个来源都要标注 `indication`：`acne`、`rosacea`、`periodontitis`、`other`。酒渣鼻和牙周炎的结果不能当作痤疮的证据。
- 每个来源记录实际用药：剂量、剂型、疗程、联合用药、样本量、结局指标、资助方。
- **严禁编造**。只引用本次会话中实际检索到的来源。`snippet` 必须是从检索结果或抓取页面中逐字摘录的短句（不超过 50 词，英文原文即可）。无法核实的内容写入 `unverified`，不要写成结论。

## 输出
把结果写入指定的 JSON 文件（UTF-8），格式如下：
```json
{"perspective_id": "...",
 "turns": [{"turn": 1, "question": "...", "triggered_by": "（第 1 轮写 initial）", "queries": ["..."],
            "source_ids": ["<pid>-S1"], "answer": "仅基于本轮证据的中文回答"}],
 "sources": [{"source_id": "<pid>-S1", "url": "https://...", "title": "...", "authors_year": "...", "journal": "...",
              "date": "YYYY 或 YYYY-MM", "design": "...", "evidence_level": "...", "indication": "...",
              "regimen": "...", "n": "...", "funding": "...",
              "snippet": "逐字摘录", "claim_supported": "该片段支持的中文结论", "reliability_note": "局限、偏倚、直接程度"}],
 "key_findings": ["..."],
 "unverified": ["..."],
 "gaps": ["目前没有证据能回答的问题"]}
```
写完文件后，只返回一段不超过 300 字的中文摘要。

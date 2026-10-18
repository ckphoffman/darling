# 视角 P8 · 抗菌药物与菌群研究者：亚抗菌剂量多西环素（SDD）长期使用对菌群组成的实测证据（子 agent 原始回复）

> 主 agent 复核（2026-10-18）：用 curl 打开 PMC8878148 全文（efetch db=pmc），确认 D7 两句关键原文："both subtherapeutic (Doxy20) and therapeutic (Doxy100) doses of doxycycline altered the skin microbiome" 与 "two of the four Doxy20 subjects (Subjects 1 and 3) grew in the presence of doxycycline"；用 openFDA 确认 Oracea 标签 §12.4 原句。
> 工具：子 agent 的 WebFetch DNS 失败，改用 curl 读 PubMed E-utilities、Europe PMC、PMC、ClinicalTrials.gov API v2、openFDA。

## 1. 逐轮日志
- **R1** 问：SDD 长期使用有无实测菌群？Walker 2005 是否存在？查：WebSearch "Walker subantimicrobial dose doxycycline 9 months … intestinal vaginal flora"、"subantimicrobial dose doxycycline 20 mg gut microbiome 16S"。发现：Walker 2005 存在（69 人、9 月、粪便+阴道）；正在进行的 ORBS（NCT05296837）声称 40 mg 从未被评估过菌群。→ 需原始摘要确认测"组成"还是"耐药"。
- **R2** 问：完整研究清单及各测组成还是耐药？查：PubMed esearch ×3；efetch PMID 16212578、15633327、12707093、11022778、11022777、10415739、26639830。发现：Walker 2005（粪便/阴道）、Walker 2000（龈下）、Thomas 2000（仅药敏）、Skidmore 2003（痤疮皮肤菌群）——全部培养/显微镜法，无 16S/宏基因组；Walker 2000 有螺旋体比例下降信号。→ 找现代测序与 40 mg 数据。
- **R3** 问：有无 16S/宏基因组测 SDD？查 5 条。发现：PMID 28689869 小鼠 16S（非亚抗菌剂量）持久 OTU 改变；41329149 DFD-29 是米诺环素 40 mg（16S 三部位 16 周 RCT）；31936625 Woo 2020 为 100 mg bid。→ 查 FDA 标签与 ORBS。
- **R4** 问：ORBS 结果？Oracea 40 mg 9 月菌群数据？查：ClinicalTrials.gov API NCT05296837；PubMed Preshaw。发现：ORBS 2025-07-14 完成，实际入组 46，三臂 8 周，hasResults=false，无论文；Preshaw 2008（n=266、9 月、40 mg）仅定性陈述龈下菌群无显著改变。→ 读标签 §12.4。
- **R5** 问：Oracea §12.4 原文？有无含 20 mg bid 臂的测序研究？查：openFDA、Europe PMC。发现：§12.4 声称 18 个月无可检出长期影响（无引用、无数据）；Jo 2021 Sci Transl Med 含 Doxy20 臂，宏基因组测皮肤/口腔/粪便/阴道，结论"Doxy20 改变了皮肤菌群"。

## 2. 来源清单
| id | 文献 | URL | 类型 | 等级 | n | 剂量 | 疗程 | 部位与方法 | 结局类别 |
|---|---|---|---|---|---|---|---|---|---|
| D1 | Walker C, Preshaw PM, Novak J, Hefti AF, Bradshaw M, Powala C. Long-term treatment with sub-antimicrobial dose doxycycline has no antibacterial effect on intestinal flora. J Clin Periodontol 2005;32(11):1163-9 | https://pubmed.ncbi.nlm.nih.gov/16212578/ | 安慰剂对照 RCT | primary | 69 | 20 mg bid | 9 月 | 粪便+阴道；厌氧总菌、机会致病菌、多西环素耐药菌（≥4 µg/mL）、6 种抗生素药敏 | 组成+耐药 |
| D2 | Walker C, Thomas J, Nangó S, Lennon J, Wetzel J, Powala C. … subgingival microflora … J Periodontol 2000;71(9):1465-71 | https://pubmed.ncbi.nlm.nih.gov/11022777/ | RCT | primary | 76 | 20 mg bid | 9 月+3 月停药 | 龈下菌斑；显微镜+培养 | 组成 |
| D3 | Skidmore R, Kovach R, Walker C, et al. Effects of subantimicrobial-dose doxycycline in the treatment of moderate acne. Arch Dermatol 2003;139(4):459-64 | https://pubmed.ncbi.nlm.nih.gov/12707093/ | RCT | primary | 51 入组/40 完成 | 20 mg bid | 6 月 | 面部皮肤；培养计数、机会致病菌、药敏 | 组成+耐药 |
| D4 | Thomas J, Walker C, Bradshaw M. Long-term use of subantimicrobial dose doxycycline does not lead to changes in antimicrobial susceptibility. J Periodontol 2000;71(9):1472-83 | https://pubmed.ncbi.nlm.nih.gov/11022778/ | 4 项 RCT 汇总 | primary | 摘要未给 | 10 mg qd/20 mg qd/20 mg bid | 最长 27 月 | 龈下；MIC、交叉耐药 | 仅耐药 |
| D5 | Preshaw PM, Novak MJ, Mellonig J, et al. Modified-release subantimicrobial dose doxycycline enhances scaling and root planing. J Periodontol 2008;79(3):440-52 | https://pubmed.ncbi.nlm.nih.gov/18315426/ | 多中心 RCT | primary | 266 | 40 mg 缓释 qd | 9 月 | 龈下（摘要未述方法） | 仅定性陈述 |
| D6 | ORACEA 40 mg 标签 §12.4 Microbiology（Galderma，SPL 2026-02-11） | https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22ORACEA%22 | 监管文件 | primary | 未披露 | "similar drug exposure" | 最长 18 月 | 口腔、皮肤、肠道、阴道 | 声称测了，零数据 |
| D7 | Jo JH, Harkins CP, Schwardt NH, …, Segre JA, Kong HH. Alterations of human skin microbiome and expansion of antimicrobial resistance after systemic antibiotics. Sci Transl Med 2021;13(625):eabd8077 (NCT01631617) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8878148/ | 随机 pilot | primary | 22 入组/19 随机/14 可评估；Doxy20 臂 4 人 | 20 mg bid 与 100 mg bid | 56 天，随访至约 336 天 | 皮肤多部位+口腔+粪便+阴道；鸟枪法宏基因组+培养+WGS+MIC+皮肤药物浓度 | 组成+耐药+组织浓度 |
| D8 | Gallo RL, Baldwin H, Harper J, Bhatia N, McLane JA, Sidgiddi S. Impact of Low-Dose Oral Minocycline (DFD-29) on Skin, Gastrointestinal, and Vaginal Microflora in Healthy Adults. J Drugs Dermatol 2025;24(12):1222-30 | https://pubmed.ncbi.nlm.nih.gov/41329149/ | RCT | primary（米诺环素，非多西环素） | 60 随机/57 可评估（38/19） | 米诺环素 40 mg 缓释 | 16 周 | 前额皮肤+阴道+粪便；培养+16S；MIC90 | 组成+耐药 |
| D9 | Woo YR, Lee SH, Cho SH, Lee JD, Kim HS. Characterization and Analysis of the Skin Microbiota in Rosacea: Impact of Systemic Antibiotics. J Clin Med 2020;9(1):185 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7019287/ | 纵向队列 | primary（标准剂量） | 12 | 100 mg bid | 6 周 | 面颊+鼻 16S | 组成 |
| D10 | Becker E, Schmidt TSB, …, Frey-Wagner I. Effects of oral antibiotics and isotretinoin on the murine gut microbiota. Int J Antimicrob Agents 2017;50(3):342-51 | https://pubmed.ncbi.nlm.nih.gov/28689869/ | 小鼠 | primary | 摘要未给 | 非亚抗菌剂量 | 2 周+4 周恢复 | 粪便 16S | 组成 |
| D11 | Kim SE, et al. … subantimicrobial dose of oral doxycycline on periodontitis in dogs. Vet J 2016;208:55-9 | https://pubmed.ncbi.nlm.nih.gov/26639830/ | 动物 RCT | primary | 12 犬 | 2 mg/kg qd | 8 周 | 龈下培养+MBC | 组成+耐药 |
| D12 | ORBS（NCT05296837）；方案 Trials 2022;23:1033（PMID 36539810） | https://clinicaltrials.gov/study/NCT05296837 ；https://pmc.ncbi.nlm.nih.gov/articles/PMC9769060/ | 4 期 RCT | primary（仅注册+方案） | 46 实际入组 | 40 mg/日 vs 200 mg/日 vs 安慰剂 | 8 周 | 直肠拭子+下眼睑；AMR 基因、Simpson 多样性 | 已完成 2025-07-14，无结果 |

## 3. 关键发现
1. **有实测组成的研究**：D1 "There was no evidence that sub-antimicrobial doxycycline treatment exerted an effect on the composition or doxycycline resistance level of either the faecal or the vaginal microflora."（培养法，RCT）
2. D1 唯一显著差异在治疗前基线（粪便耐药菌计数），不归因于药物。
3. D2：SDD 组螺旋体比例显著低于安慰剂（P<0.05），且先有探诊出血位点比例下降（P<0.01）——"无影响"不完全干净。
4. D3：痤疮 6 月 SDD "had no detectable antimicrobial effect on the skin flora"（培养法）。
5. D6：FDA 标签称 "up to 18 months … no detectable long term effects on bacterial flora of the oral cavity, skin, intestinal tract and vagina"——未引研究、无数字。
6. **D7（宏基因组）相反**："both subtherapeutic (Doxy20) and therapeutic (Doxy100) doses of doxycycline altered the skin microbiome."（主 agent 已复核）
7. D7：Doxy20 臂 4 人中 2 人皮肤出现多西环素耐药菌（主 agent 已复核）。
8. D7：Doxy20 耐药 S. epidermidis 的 MIC 低于 Doxy100，皮肤药物浓度更低——"subtherapeutic doses may provide weaker selection pressure"。
9. D7：tetK/tetL 扩增仅见于皮肤；口腔/肠道/阴道宏基因组未检出（肠道 tet32 扩增仅见于 Doxy100）。
10. D8（米诺环素 40 mg，16S，16 周）：皮肤、粪便、阴道物种丰度与安慰剂无显著差异。
11. D12 方案："this 'sub-microbial' dose has never been evaluated in patients with ocular rosacea, and even the sub-microbial dose has potential to alter systemic mucosa flora."
12. D12 已完成未发表（hasResults=false）。
13. D9（100 mg bid，n=12）：Weissella confusa 相对丰度升高（P=0.008），α 多样性未变。
14. D10（小鼠）：多西环素对部分 OTU 有持久显著影响。

## 4. 判定
- **有无实测组成**：有（肠道/阴道 D1、D7；皮肤 D3、D7；口腔 D2、D5、D7）。
- **肠道与阴道**：支持"无可检出影响"，但主要依据 2005 年培养法 RCT（D1）；SDD 专项 16S/宏基因组肠道研究不存在（D7 仅 4 人、56 天）。→ 部分证实。
- **皮肤**：培养法（D3）"无影响"被宏基因组小样本（D7）挑战：Doxy20 改变皮肤菌群并选择出耐药葡萄球菌，效应弱于 100 mg。
- **FDA 标签 18 个月陈述**：无可见底层数据，只能作线索。
- **40 mg 缓释剂型**：几乎无菌群数据；独立方案明言从未评估。

## 5. 证据缺口
1. ORBS 结果未公布。2. 无 SDD 肠道 16S/宏基因组专项人体研究。3. D7 Doxy20 臂 n=4，需重复。4. 未取到 Oracea NDA 21-693 / Periostat NDA 50-805 microbiology review 原文。5. D8（米诺环素）、D9（100 mg）、D10（小鼠）不能直接用于 SDD 结论。
- 更正：题干把粪便/阴道数据归于 Thomas 2000 是错配；Thomas 2000（D4）只有龈下药敏，正确出处为 Walker 2005（D1）。

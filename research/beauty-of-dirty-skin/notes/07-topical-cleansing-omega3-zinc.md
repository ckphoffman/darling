# 视角 P7 · 皮肤屏障与外用制剂研究者：C7 外用益生菌 / C8 过度清洁 / C9 ω-3 抗氧化 / 锌

> **状态说明**：该子 agent 在第 5 轮后因 API 安全过滤（API error，[bio] 标记）被提前终止，回复在来源 T13 处截断。T1–T13 来自子 agent 回复；T14 起和第 3–6 节由主 agent 于 2026-10-18 用 curl 读 PubMed efetch 摘要补完（PMID 24553997、11586012、16702322、24970388、17014635、37579728、18795916）。
> 锌的可耐受最高摄入量（UL）：NIH ODS 页面返回 Cloudflare 403，NCBI Bookshelf DRI 原文未取得——**按证据规则不写具体数值**。

## 1. 逐轮日志（子 agent，截断前）
- R1：Nakatsuji 2017/2021、Myles 2018、Gueniche、Kang 2009；读 PMC5600545、PMC8052297、PMC6012572 全文。Nakatsuji 2017 人体部分仅 5 例 AD、单次涂抹、结局为 S. aureus 定植；Nakatsuji 2021 1 期 RCT（n=54）主要终点安全性，湿疹严重度无显著差异；Myles 2018 开放标签 n=15；任务所写 "Gueniche 2010 Exp Dermatol" 实为 B. longum 裂解物（敏感皮肤），Vitreoscilla 那篇为 Gueniche 2008 Br J Dermatol，均 L'Oréal。
- R2：FB-401（3 株 R. mucosa）16 周 RCT 154 人失败；2026 Lactobacillus 痤疮 meta（线索）5 项 RCT 阴性。
- R3：Bowe 2006 体外；专利 US8415289（Margolis、Bowe；宾大）；Choi 2006 RCT 洗脸 1/2/4 次组间无差异；洗手与手部湿疹观察性证据。
- R4：Jung 2014 ω-3 RCT n=45 阳性；Dreno 2001 n=332 锌劣于米诺环素；UL 原文被拦截。
- R5：Mogollon 2014 RCT n=74 主要终点 MED 阴性；2026 两项 ω-3 RCT 均与异维 A 酸合用。

## 2. 来源清单
| id | 文献 | 标识 | 设计 | 样本/干预 | 结局类型 | 主要结果 | 资助/COI | tier |
|---|---|---|---|---|---|---|---|---|
| T1 | Bowe WP 2013 Probiotics in acne and rosacea. Cutis 92(1):6-7 | PMID 23961518 | 评论 | — | — | 无摘要 | — | 作者观点 |
| T2 | Bowe WP, Filip JC, DiRienzo JM, Volgina A, Margolis DJ 2006 Inhibition of P. acnes by BLIS produced by Streptococcus salivarius. J Drugs Dermatol 5(9):868-70 | PMID 17039652; PMC2739725 | 体外 | — | 中间（抑菌） | — | — | primary（机制） |
| T3 | US8415289B2 Bacterial-derived BLIS for treatment of acne | Google Patents | 专利记录 | 发明人 David Margolis、Whitney Bowe；受让人 University of Pennsylvania；"Active, expires 2027-10-08" | — | — | COI 背景 | primary |
| T4 | Nakatsuji T 等 2017 Sci Transl Med 9:eaah4680 | PMID 28228596; PMC5600545 | 机制+小鼠+人体自体移植 | 5 例 AD，双盲半侧对照 | 仅 S. aureus 定植 | "No power analy[sis]" | NIH ADRN 等 | primary（机制为主） |
| T5 | Nakatsuji T 等 2021 Nat Med 27:700-709 | PMID 33619370; PMC8052297; NCT03151148 | 1 期双盲 RCT | 54 名 S. aureus 阳性成人 AD，1 周 | 安全性（主要）+EASI/SCORAD | 安全性达成；严重度全体 "not significantly different"；仅事后亚组改善 | NIH；作者为 UCSD 技术发明人，R.L.G. 持 MatriSys 股权 | primary |
| T6 | Myles IA 等 2018 JCI Insight 3(9):e120608 | PMID 29720571; PMC6012572 | 开放标签 I/II 期 | 10 成人+5 儿童 | 皮肤 | 严重度等 "significant decreases"（无对照） | NIAID 院内 | primary（非对照） |
| T7 | Myles IA 等 2020 Sci Transl Med 12:eaaz8631 | PMID 32908007 | 开放标签 | 15 名 <7 岁 | 皮肤 | 与 "historical placebo" 比较 | — | primary（非对照） |
| T8 | Jacobson ME 等 2024 FB-401 RCT. Dermatology 240(1):85-94 | PMID 37579728 | 双盲安慰剂 RCT 16 周 | 154 人 ≥2 岁轻中度 AD | 皮肤（EASI-50） | "no significant treatment group differences observed at any post-baseline visit"；"failed to prove superior to placebo"（主 agent 已复核） | Eichenfield 为 Forte 董事 | primary |
| T9 | Gueniche A 等 2008 Vitreoscilla filiformis lysate on AD. Br J Dermatol 159:1357-63 | PMID 18795916 | 双盲安慰剂 RCT 30 天 | 75 人，5% 裂解物乳膏 | 皮肤+TEWL | SCORAD vs 安慰剂 P=0.0044，瘙痒 P=0.0171；"TEWL also improved significantly with the cream alone"（主 agent 已复核） | L'Oréal Recherche | primary |
| T10 | Guéniche A 等 2010 Bifidobacterium longum lysate. Exp Dermatol 19:e1-8 | PMID 19624730 | RCT+离体 | 66 女（33/33），10% 裂解物 2 月 | 皮肤功能（敏感、屏障恢复） | 摘要仅 "significant" | L'Oréal | primary |
| T11 | Kang BS 等 2009 J Microbiol 47(1):101-9 | PMID 19229497 | 体外+痤疮洗剂对照试验 | E. faecalis SL-5 上清洗剂 vs 安慰剂 | 皮肤 | "significantly reduced the inflammatory lesions like pustules compared to the placebo lotion"；n、随机、盲法摘要未给 | 可能为 Cell Biotech（推断未核） | primary（信息不足） |
| T12 | Choi JM, Lew VK, Kimball AB 2006 Pediatr Dermatol 23(5):421-7 | PMID 17014635 | 单盲 RCT | 轻中度痤疮男性；先每天 2 次 2 周，再随机 1/2/4 次 6 周（n 摘要未给） | 皮肤 | "no statistically significant differences were noted between groups"；每天 2 次组开放性粉刺与非炎性病灶改善；每天 1 次组红斑、丘疹、炎性病灶增加；"excessive face washing may not be as culpable as previously thought"（主 agent 已复核） | — | primary |
| T13 | Larson EL 等 1998 Am J Infect Control 26:513-21 | PMID 9795681 | 前瞻观察 | 40 名护士（20 手损/20 正常） | 仅菌群 | 手受损组菌量未更高（P=.63），定植菌种更多（回复在此截断） | — | primary |
| T14 | Jung JY 等 2014 Effect of dietary supplementation with omega-3 fatty acid and gamma-linolenic acid on acne vulgaris: RCT. Acta Derm Venereol 94(5):521-5 | PMID 24553997 | 随机双盲对照 10 周 | 45 名轻中度痤疮；EPA+DHA 2,000 mg 组 / 琉璃苣油 400 mg GLA 组 / 对照 | 皮肤+组织学 | "inflammatory and non-inflammatory acne lesions decreased significantly"；IL-8 染色降低；无严重不良事件；作者："could be used as adjuvant treatments"（主 agent 读摘要） | — | primary |
| T15 | Dreno B 等 2001 zinc gluconate versus minocycline. Dermatology 203(2):135-40 | PMID 11586012 | 多中心随机双盲 | 332 人；元素锌 30 mg vs 米诺环素 100 mg，3 月 | 皮肤 | 临床成功率（炎性皮损减少 >2/3）锌 31.2% vs 米诺环素 63.4%；米诺环素优势 17%；不良反应多为胃肠道（主 agent 读摘要） | — | primary |
| T16 | Heinrich U 等 2006 Long-term ingestion of high flavanol cocoa… J Nutr 136(6):1565-9 | PMID 16702322 | 两组 12 周（摘要未写随机/盲法） | 女性；高黄烷醇 326 mg/d vs 低 27 mg/d | 皮肤（UV 红斑、水合、TEWL 等） | 1.25 MED 照射后红斑第 6、12 周降 15%、25%；TEWL 8.7±3.7→6.3±2.2 g/(h·m²)（组内）（主 agent 读摘要） | — | primary |
| T17 | Mogollon JA 等 2014 Chocolate flavanols and skin photoprotection: RCT. Nutr J 13:66 | PMID 24970388; NCT01444625 | 双盲 RCT 12 周 | 74 女（33/41），30 g/天巧克力 | 皮肤（MED 主要终点） | 主要终点 MED 差异 MD 0.0100 J/cm²（95%CI −0.0417 至 0.0618）；"failed to demonstrate a statistically-significant protective effect"；弹性 MD 0.06 mm（0.01–0.12）（主 agent 读摘要） | — | primary |

## 3. 作者引用核查
- 外用益生菌：Bowe 2013 自称 "a small number of intriguing preliminary studies"；她本人在该领域的一手工作是 2006 体外抑菌（T2）与专利（T3），无临床试验。外用菌/裂解物的人体 RCT 主要在特应性皮炎而非痤疮：L'Oréal 裂解物乳膏（T9、T10）阳性；活菌疗法 1 期（T5）主要终点为安全性、疗效不显著，3 株 R. mucosa 的 RCT（T8）失败。痤疮仅 T11 一项信息不足的洗剂试验。
- 过度清洁："不要过度清洁是第一原则"在唯一 RCT（T12）中未获直接支持：洗 4 次组与 2 次组无组间差异，反倒是洗 1 次组炎性病灶增加。作者结论："excessive face washing may not be as culpable as previously thought"。
- ω-3：一项 45 人 RCT 阳性（T14），可作辅助。
- 抗氧化/多酚饮品：可可黄烷醇 T16 阳性，同类 RCT T17 主要终点阴性——不一致。
- 锌：口服锌对炎性痤疮有作用但明显不如米诺环素（T15）；书中锌剂量只有读者转述（10–30 mg/日），未核对原书。

## 4. 判定
- C7 外用益生菌/后生元改善痤疮/屏障：**只有机制推论**（痤疮）；特应性皮炎中裂解物乳膏有厂商 RCT 支持、活菌疗法 RCT 阴性或不显著。对书中及其自有面霜所称"益生元+后生元改善屏障"，无独立 RCT。置信：中。
- C8 过度清洁有害：**证据不支持其作为"第一原则"**；唯一 RCT 组间无差异（接近"证据相反"于"多洗更差"）；"每天两次温和清洁"有轻度支持。FDA 不建议抗菌皂（见 notes/05）。置信：中。
- C9 ω-3：**有 RCT 支持（单项、小样本）**，低–中。可可多酚：**RCT 不一致**。
- 锌补充：**有 RCT 支持，但效果劣于标准抗生素**（n=332）。剂量安全性：UL 数值未从一手原文核实，不写。

## 5. 实用结论
- 温和清洁、每天 2 次：免费、风险低；不必为"保护菌群"少洗，也不必多洗。
- 益生菌/后生元面霜：价格高，痤疮无 RCT；不建议为此付费。
- ω-3 鱼油：可作辅助尝试 10 周；注意与抗凝药合用需问医生（常识提示，未核文献）。
- 锌：有效但弱于米诺环素；长期高剂量补锌须遵医嘱（UL 数值未核）。
- 可可/多酚饮品：证据不一致，不值得为皮肤专门购买。

## 6. 缺口
- 子 agent 截断：未取得其第 4–6 节完整内容（含锌 UL 原文、资助方细节）。
- 痤疮外用益生菌 RCT 几乎空白；T11 设计未核；T12 样本量未知。
- 锌 UL 一手原文未取得。

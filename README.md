# Bai Xing · 白星

I build tools for testing ideas, checking browser behavior, and producing documents and comic-drama workflows. / 我构建帮助检验想法、验证网页、制作文档和漫剧的工具。

## Build / 实用工具

| Project | Use it for / 用途 | Start here / 开始使用 |
|---|---|---|
| [dsh-verify · Witness](https://github.com/263311487-ux/dsh-verify) | Run explicit browser acceptance checks and inspect screenshots. / 浏览器验收与截图报告 | [No-key starter and failure example](https://github.com/263311487-ux/dsh-verify#first-success--no-api-key) · Node.js / CLI / MCP |
| [falsify](https://github.com/263311487-ux/falsify) | Scientific-thinking guidance and a rule-based claim coach. / 科学思维指引与启发式主张检查 | [CLI, installation and evaluation evidence](https://github.com/263311487-ux/falsify) · `npx falsify-skill --json "This is definitely the fastest option"` |
| [imprint-pdf](https://github.com/263311487-ux/imprint-pdf) | Typeset Markdown with a documented automated quality checklist. / Markdown 排版与自动质检 | [Platform prerequisites and first PDF](https://github.com/263311487-ux/imprint-pdf/blob/main/docs/first-success.md) · `pip install imprint-pdf` |
| [Yuanjing Storyforge · 元境漫界工坊](https://github.com/263311487-ux/yuanjing-storyforge) | Formerly `ai-comic-drama`; plan and validate shot manifests; rehearse delivery offline. / 原名 `ai-comic-drama`，用于分镜清单、离线流程与交付检查 | [Offline quickstart](https://github.com/263311487-ux/yuanjing-storyforge#one-command-quickstart) · Python 3.11+ |

Browser PASS means the supplied checks passed, not complete app coverage. Falsify is guidance, not a correctness guarantee. PDF quality scores are project-defined checks, not certification. Comic examples run offline; paid generation and human content approval are separate steps.

浏览器通过、启发式评分、PDF 分数和技术质检各有明确范围；请阅读项目中的限制与证据。

## Research / 研究

[**Xun / RRC-ACT**](https://github.com/263311487-ux/Xun) studies whether relation-specific feedback changes persistent artificial self-model continuity. It is a theory-and-methods preprint; empirical validation and independent replication remain pending. / 研究关系特异性反馈是否影响持久人工自我模型，尚未完成实证验证与独立复现。

[English research hub](https://263311487-ux.github.io/Xun/docs/rrc-act.html) · [中文研究入口](https://263311487-ux.github.io/Xun/docs/rrc-act-zh.html) · [Fixed preprint DOI](https://doi.org/10.5281/zenodo.23146271) · [Evidence and version map](https://github.com/263311487-ux/Xun/blob/master/docs/research-status.md)

Software tests, downloads and fluent self-reports do not establish consciousness. / 软件测试、下载量和第一人称表达不能证明意识。

## Explore / 项目目录

[完整 41 仓库目录与状态](CATALOG.md)（产品 / 研究 / 演示 / fork / 历史；含 PR 检索快照）

- [Complete public repository catalog](CATALOG.md): products, research, demos, historical material, and contribution forks with verified upstream links. / 全部公开仓库及上游贡献记录。
- [DSH team demo](https://github.com/263311487-ux/dsh-web-team-demo): a small browser interaction example. / 小型网页交互演示。
- [Historical BaiXun proposal](https://github.com/263311487-ux/-): retained historical text, not the current research publication. / 保留的历史文本。

Forks are separately tracked contribution/reference copies, not additional original products. Repository views, package downloads and clones use different counting rules; none is a count of verified active users.

If a tool helps, share a reproducible example or issue in its repository. / 欢迎在对应仓库提供可复现的问题或使用案例。

## How success is measured / 如何判断有人真正用起来

页面访问、Git 克隆、npm/PyPI 下载和 Zenodo 浏览量采用不同统计口径，也可能包含 CI、机器人、维护者操作，不能当作活跃用户数。项目运营按下面的匿名首成功信号复查：

| Project | First-success event | Reuse signal |
|---|---|---|
| dsh-verify | 固定版本安装后，starter spec 返回 PASS 并生成 report.html | 下一窗口再次运行固定版本或提交可复现 issue |
| falsify | CLI/技能返回结构化假设、证伪路径和不确定性字段 | 第二次对不同主张运行或提交反例 |
| imprint-pdf | 本地生成 PDF，并产出质检报告 | 第二份文档成功渲染或提交版式反馈 |
| ai-comic-drama | 离线 quickstart 产出 manifest/previz 与明确的 provider-review 状态 | 第二个 manifest 或真实 provider 评审记录 |
| Xun / RRC-ACT | 读者能定位固定 DOI、研究状态和预注册材料 | 复现报告、方法批评或独立实验记录 |

这些信号只记录匿名计数、版本和结果类型，不收集文档正文、提示词、密钥或个人身份。每两周用不重叠窗口复查一次，并把自动化流量与真实首成功分开报告。

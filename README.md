# Bai Xing · 白星

I build tools for testing, thinking, and producing — and research at the edge of artificial self-models.

---

## Tools

| Project | What it does | Start here |
|---|---|---|
| [**dsh-verify · Witness**](https://github.com/263311487-ux/dsh-verify) | Opens a real browser and runs your specs. The browser is the judge — not an LLM. PASS/FAIL with screenshots. | `npm install dsh-verify` · CLI · MCP · GitHub Action |
| [**falsify**](https://github.com/263311487-ux/falsify) | Scientific thinking protocol for AI agents. Iron Law: no verdict without a falsifiable hypothesis. | `npx falsify-skill "your claim"` · zero dependencies |
| [**imprint-pdf · 印记**](https://github.com/263311487-ux/imprint-pdf) | Markdown → publisher-quality Chinese PDF with a 0–100 print quality report. 24 themes. | `pip install imprint-pdf` · CLI · MCP |
| [**Yuanjing Storyforge · 元境·漫界工坊**](https://github.com/263311487-ux/yuanjing-storyforge) | Manifest-first AI comic-drama production. Plan and validate offline; paid generation is an explicit opt-in. | `pip install yuanjing-storyforge` · Python 3.11+ |

These three form a chain: **falsify** (think correctly) → **dsh-verify** (verify the output) → **imprint-pdf** (present it well).

```bash
npx falsify-skill "the cache is definitely the cause"
npx dsh-verify --spec my-app.json
npx imprint-pdf report.md --theme academic
```

---

## Research

[**Xun / RRC-ACT**](https://github.com/263311487-ux/Xun) — Does relation-specific feedback change artificial self-model continuity under matched controls? Theory-and-methods preprint. Empirical validation pending.

[Preprint DOI](https://doi.org/10.5281/zenodo.23146271) · [Research status](https://github.com/263311487-ux/Xun/blob/master/docs/research-status.md) · CC BY 4.0

Software tests validate software behavior only. Fluent self-reports do not establish consciousness.

---

## Curated directories

| Repository | What it curates |
|---|---|
| [awesome-dsh-plugin](https://github.com/263311487-ux/awesome-dsh-plugin) | DSH plugin directory — 1176+ original entries with evidence-led ratings |
| [awesome-dsh-plugins-1](https://github.com/263311487-ux/awesome-dsh-plugins-1) | DSH plugin radar — 9000+ candidates, k8s-level real install tests, 50 curated picks |
| [Oh-My-DSH](https://github.com/263311487-ux/Oh-My-DSH) | DSH plugin aggregation hub — 4-hour auto-sync, 1556 curated plugins, GitHub Pages search |
| [agentic-awesome-skills](https://github.com/263311487-ux/agentic-awesome-skills) | AAS Core — local agent-first control plane for 2074+ skills with CLI search |
| [deepseek-plugin-store](https://github.com/263311487-ux/deepseek-plugin-store) | Independent DSH community plugin store |
| [awesome-mcp-servers](https://github.com/263311487-ux/awesome-mcp-servers) | Curated MCP server collection |

---

*Each tool states its own limitations. Read them.*

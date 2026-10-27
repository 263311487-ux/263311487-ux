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

## All 42 repositories

[Full catalog](CATALOG.md) — products, research, forks, demos, and historical material with upstream links and PR records.

---

*Each tool states its own limitations. Read them.*

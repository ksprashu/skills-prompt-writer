---
name: compile-docs
description: Automates the compilation of raw Markdown documentation sheets (such as specs, roadmaps, walkthroughs, or prds) into premium, interactive HTML presentations. Leverages 4 premium Stitch themes (technical, obsidian, proscript, and dynamics).
---

# Custom Compile-Docs Skill

This skill ensures that all raw project documentation sheets are dynamically compiled into gorgeous, responsive HTML pages using standard-compliant, premium Stitch designs.

---

## 🧭 Visual Themes Reference

Declare the target presentation style by setting the `theme` key in your YAML frontmatter:

```yaml
---
title: "Developer Integration Guide"
theme: "technical" # Select from: technical | obsidian | proscript | dynamics
description: "Comprehensive step-by-step setup guides"
---
```

1.  **`theme: technical`**: Light theme with crisp white backgrounds, institutional blue/slate headers, and cyan highlights. Best for engineering specifications, APIs, and codelabs.
2.  **`theme: obsidian`**: Dark theme with high-blur glassmorphic panels (`backdrop-filter: blur(24px)`), near-black violet canvases, and pink/neon-cyan keynote outer glows. Best for slide presentations and walkthroughs.
3.  **`theme: proscript`**: Light theme with authoritative gridded structures, gray containers, checkboxes, and sign-off blocks. Best for corporate policies, functional specs, and requirements.
4.  **`theme: dynamics`**: Dark theme with ultra-dense grids, gray/dark-grey blocks, telemetry lists, and green/red live status circles. Best for performance tracking, analytics, and security reviews.

---

## 🛠️ Operations

Invoke the documentation compilation tool manually or target directories recursively:

```bash
# Compile all sheets inside a directory recursively:
python /Users/ksprashanth/code/github/skills-documentation/skills/documentation/scripts/compile_docs.py --dir ./docs

# Compile a single target file specifically:
python /Users/ksprashanth/code/github/skills-documentation/skills/documentation/scripts/compile_docs.py --file docs/walkthrough.md
```

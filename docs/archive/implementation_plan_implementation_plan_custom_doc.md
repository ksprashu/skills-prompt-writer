# Implementation Plan - Custom Documentation Skill (From Scratch) with Live-Reload Server

This plan details the design and construction of a new, standalone `documentation` skill from scratch under `/Users/ksprashanth/code/github/skills-documentation`. We will codify the 4 premium visual styles extracted from Stitch, develop a robust, zero-dependency Markdown-to-HTML compiler, construct a built-in **Live-Reload & Watch Server** (`watch_docs.py`), and integrate this new skill directly into both the `6-personas` and `prompt-writer` skills to make its adoption explicit across all projects.

---

## User Review Required

> [!IMPORTANT]
> **1. Creation of standalone `skills-documentation`:**
> We will scaffold a new local repository `/Users/ksprashanth/code/github/skills-documentation` following the canonical Custom Skill guidelines. It will be globally discoverable and version-controlled.
> 
> **2. Built-in Live-Reload & Watch Server (`watch_docs.py`):**
> We will write a lightweight, standard-library-only Python server. It will:
> *   Watch for any edits inside the project's `docs/` folder (or specific `.md` files).
> *   Automatically re-run the markdown compiler (`compile_docs.py`) when changes are saved.
> *   Serve the compiled documentation locally (e.g. at `http://localhost:8000`).
> *   Inject a lightweight JavaScript listener in "watch mode" to auto-refresh the browser on re-compilation with zero third-party packages.
> 
> **3. Explicit Integration across Prompts:**
> *   **6-Personas Skill**: The **Mentor** stage will now explicitly mandate utilizing the `documentation` skill to compile project walkthroughs and interactive user guides.
> *   **Prompt-Writer Skill**: The **Analyst** and **Builder** stages will force the generated prompts to explicitly include documentation requirements and template selections.
> 
> **4. Compiler Customization**:
> We will design a clean-slate, modular Python script `compile_docs.py` that translates raw markdown files into interactive HTML dashboards supporting the 4 distinct visual themes:
> *   `technical` (Light theme, developer portal, sticky sidebars, Inter + JetBrains Mono)
> *   `obsidian` (Dark theme, glassmorphic, glowing gradients, Outfit font, timeline pulses)
> *   `proscript` (Light theme, enterprise checklists, clean boxes, formal layouts)
> *   `dynamics` (Dark theme, high information-density, analytical stats, Geist monospaced)

---

## Open Questions

> [!NOTE]
> * **Automatic Navigation Tree**: The compiler will automatically generate a shared side navigation sidebar on every compiled HTML page, allowing seamless jumping between all guides in the project's `docs/` folder. Do you have any specific file names you want us to support as the standard suite beyond `user_guide.md`, `specifications.md`, `architecture.md`, and `walkthrough.md`?

---

## Proposed Changes

---

### 1. New Standalone Documentation Skill (`skills-documentation`)

We will create a clean-slate Custom Skill repository containing the instruction set, templates, and compiler logic.

#### [NEW] [SKILL.md](file:///Users/ksprashanth/code/github/skills-documentation/skills/documentation/SKILL.md)
*   Canonical skill definition with YAML frontmatter `name: documentation`.
*   Specifies the Markdown-to-HTML compilation standards.
*   Lays out the design guidelines, variables, and typography rules for the 4 premium Stitch themes.
*   Instructs executing agents on how to construct a comprehensive Standard Document Suite.

#### [NEW] [compile_docs.py](file:///Users/ksprashanth/code/github/skills-documentation/skills/documentation/scripts/compile_docs.py)
*   A clean, robust, standalone Python script.
*   Parses frontmatter metadata (e.g. `title`, `theme`, `description`) from Markdown source files.
*   Renders Markdown headers, paragraphs, links, list items, checkboxes, alerts (`> [!NOTE]`), tables, and code snippets into beautiful semantic HTML.
*   Injects premium responsive CSS layouts, fonts (Outfit, Hanken Grotesk, Geist, Inter), gradients, and animations corresponding to the selected theme.
*   Generates interactive side-menus and page-level tables of contents on the fly.
*   Injects a tiny live-reload long-polling fetch script when the `--watch` flag is set.

#### [NEW] [watch_docs.py](file:///Users/ksprashanth/code/github/skills-documentation/skills/documentation/scripts/watch_docs.py)
*   Standard library Python script that launches an HTTP server and watches `docs/*.md` files.
*   Exposes a `/live-reload` HTTP long-polling endpoint to notify connected clients when files are updated.
*   Automatically triggers the compiler script when changes are detected, resulting in sub-100ms rebuild-to-render times.

#### [NEW] [sample_guide.md](file:///Users/ksprashanth/code/github/skills-documentation/skills/documentation/examples/sample_guide.md)
*   A rich reference markdown file demonstrating headers, checklist items, warning blocks, tables, code blocks, and multi-theme configurations.

---

### 2. Update 6-Personas Skill (`skills-6-personas`)

We will integrate the documentation skill into our global cognitive persona framework to make documentation compilation a core delivery metric.

#### [MODIFY] [SKILL.md](file:///Users/ksprashanth/code/github/skills-6-personas/skills/6-personas/SKILL.md)
*   **Mentor Stage**: Explicitly instruct the agent to execute the `documentation` skill to compile all walkthroughs, setup guides, and project roadmaps into stunning, interactive HTML interfaces matching the chosen project theme.
*   Link to the documentation skill's path explicitly.

---

### 3. Update Prompt-Writer Skill (`skills-prompt-writer`)

We will make documentation creation and style selections an explicit part of every prompt generated for new or existing codebases.

#### [MODIFY] [SKILL.md](file:///Users/ksprashanth/code/github/skills-prompt-writer/skills/prompt-writer/SKILL.md)
*   **Analyst Stage**: Require the agent to prompt the developer for their preferred documentation theme (Technical, Obsidian, Proscript, or Dynamics) and target audiences during the Socratic Grill.
*   **Builder Stage**: Ensure the generated prompt explicitly directs the builder to draft exhaustive user documentation.
*   **Mentor Stage**: Mandate compiling interactive HTML user walkthroughs using the custom `compile_docs.py` tool.

---

## Verification Plan

### Automated Tests
*   We will run the newly built Python script against sample markdown files to verify clean compilation, CSS style injection, and frontmatter parsing:
    ```bash
    python /Users/ksprashanth/code/github/skills-documentation/skills/documentation/scripts/compile_docs.py --help
    ```
*   Verify watcher functionality:
    ```bash
    python /Users/ksprashanth/code/github/skills-documentation/skills/documentation/scripts/watch_docs.py --dir ./docs
    ```

### Manual Verification
*   We will compile a mock documentation suite for the 4 themes and view them in the browser using the `browser_subagent` and Chrome DevTools to visually audit layout elegance, mobile responsiveness, color contrast, and font correctness.
*   Verify that saving an edit inside `sample_guide.md` triggers an instant, automatic live reload of the open browser tab.

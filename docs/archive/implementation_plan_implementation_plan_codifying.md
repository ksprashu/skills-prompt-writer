# Implementation Plan - Codifying Premium Documentation Themes & Explicit Documentation Lifecycle

This plan introduces a formalized documentation lifecycle and 4 premium visual styles (designed via Stitch) into our multi-agent prompt-writing skill and the documentation compiler. This ensures that every project we work on automatically creates and maintains stunning, consistent documentation tailored to its target audience.

---

## User Review Required

> [!IMPORTANT]
> **1. Creation of the Local `skills-docs-sync` Repository:**
> We propose creating a new local repository at `/Users/ksprashanth/code/github/skills-docs-sync` to house and version-control our shared documentation skill. We will migrate the global `docs-sync-plugin` contents there to make it editable and visible alongside our other standalone skills (like `skills-prompt-writer`, `skills-6-personas`, etc.).
> 
> **2. Documentation Theme Customization:**
> Each markdown file can specify its visual theme via YAML frontmatter (e.g., `theme: technical` or `theme: obsidian`). We will update the documentation compiler `compile_html_docs.py` to support these 4 themes dynamically.
> 
> **3. Prompt-Writer Mandatory Construct:**
> We will update the `prompt-writer` skill to require documentation and guide planning as an explicit, non-negotiable stage in the generated prompts, forcing the executing agent to output beautiful user-facing guides using the codified styles.

---

## Open Questions

> [!NOTE]
> * **Default Repository Location:** Does `/Users/ksprashanth/code/github/skills-docs-sync` fit your naming convention perfectly, or would you prefer `/Users/ksprashanth/code/github/skills-documentation`? We have drafted the plan using `skills-docs-sync` to align with the name of the existing global plugin.
> * **Automatic Theme Selection:** Should `prompt-writer` make the theme choice automatically based on the project's domain (e.g., coding projects default to `technical`, interactive demos to `obsidian`), or should it always ask you during the Socratic Grill loop? (We recommend having a default suggestion with the option to change it).

---

## Proposed Changes

We will group our updates across three logical layers: the prompt-writer skill, the newly established local docs-sync skill repository, and the compiler scripts.

---

### 1. Prompt-Writer Skill Enhancements (`skills-prompt-writer`)

We will update our prompt-writing framework to explicitly integrate documentation as a primary construct at multiple stages of prompt generation.

#### [MODIFY] [SKILL.md](file:///Users/ksprashanth/code/github/skills-prompt-writer/skills/prompt-writer/SKILL.md)
*   **Analyst Stage (Socratic Grill)**: Mandate asking the user for their preferred documentation theme (Technical, Obsidian, Proscript, or Dynamics) and target audiences (technical vs. non-technical).
*   **Architect Stage**: Add explicit instructions to draft a documentation roadmap in `implementation_plan.md` mapped to specific files in the Standard Document Suite.
*   **Builder Stage**: Ensure the executing agent is instructed to create/update necessary markdown documentation (PRD, Specification, User Guide, etc.) and run the compiler script.
*   **Sentry/Mentor Stage**: Instruct the executing agent to verify that the compiled HTML documentation loads properly, is responsive, and contains zero placeholders.

---

### 2. Standardized Documentation Skill (`skills-docs-sync`)

We will establish a dedicated, version-controlled repository to house our documentation skill, integrating the 4 Stitch visual themes as codified references.

#### [NEW] [skills-docs-sync repository](file:///Users/ksprashanth/code/github/skills-docs-sync)
*   Create a local repository at `/Users/ksprashanth/code/github/skills-docs-sync` with a standard skill folder structure:
    *   `skills/docs-sync/SKILL.md`: Main instructions outlining the Standard Document Suite and compilation triggers.
    *   `skills/docs-sync/references/templates/`: Codified design tokens and layout grids for the 4 Stitch styles.
    *   `skills/docs-sync/scripts/compile_html_docs.py`: Highly optimized Python documentation compiler.

#### [NEW] [docs_templates.py / CSS references](file:///Users/ksprashanth/code/github/skills-docs-sync/skills/docs-sync/references/templates/styles.css)
Codify the 4 premium Stitch visual themes:
1.  **Technical Documentation System (Light Mode)**:
    *   *Purpose*: High-impact technical education, developer guides, API references, and knowledge bases.
    *   *Aesthetics*: Clean white background (`#fbf8ff`), deep institutional blue (`#1A237E`) and slate (`#455A64`) headers, vibrant cyan (`#00E5FF`) accents, Inter + JetBrains Mono typography, sticky 3-column layout (left sidebar nav, center prose, right sticky TOC), custom admonition banners.
2.  **Luminous Obsidian (Dark Mode)**:
    *   *Purpose*: Interactive live demos, walkthrough guides, and keynotes.
    *   *Aesthetics*: Deep obsidian violet/black canvas (`#141220`), neon-cyan (`#06dbf6`) and keynote pink (`#ff39c2`) gradients, glassmorphism containers (24px backdrop-blur, 8% white borders), glowing active buttons and interactive pulse timelines.
3.  **Proscript System (Light Mode)**:
    *   *Purpose*: Enterprise requirements, checklists, architectural blueprints, and compliance signs-off.
    *   *Aesthetics*: Crisp white backgrounds (`#f9f9fb`), deep authoritative blue accents (`#1A237E`), soft gray containers, 8px grid alignment, paper-on-desk ambient shadows, structured tabular layouts, and checkmark lists.
4.  **Delhi Traffic Dynamics (Dark Mode)**:
    *   *Purpose*: High information density reports, deep analytical summaries, and system audits.
    *   *Aesthetics*: Deep charcoal backgrounds (`#141313`), monospaced Geist font, tight spacing grids, inline technical statistics, and soft status glowing indicators.

---

### 3. Compiler Compiler Updates (`compile_html_docs.py`)

We will update the Python orchestrator script to read the `theme` option from the YAML frontmatter of individual markdown documents and dynamically compile them using the corresponding visual stylesheets and layouts.

#### [MODIFY] [compile_html_docs.py](file:///Users/ksprashanth/code/github/skills-docs-sync/skills/docs-sync/scripts/compile_html_docs.py)
*   **Frontmatter Parsing**: Parse YAML metadata at the top of markdown documents to extract the selected theme.
*   **Dynamic Theme Dispatcher**: Load distinct CSS stylesheets, font references (Google Fonts links for Outfit, Hanken Grotesk, Geist, Inter), and HTML structural templates depending on the active theme.
*   **Aesthetic Preservation**: Ensure that alert boxes, code containers, navigation lists, and SVG roadmaps adapt their colors and rounding behaviors to match the selected theme's design system tokens.

---

## Verification Plan

### Automated Tests
*   Run the compiled script with test datasets to verify multi-theme generation:
    ```bash
    python /Users/ksprashanth/code/github/skills-docs-sync/skills/docs-sync/scripts/compile_html_docs.py
    ```
*   Verify HTML layout validity, CSS compilation, and responsive tag symmetry.

### Manual Verification
*   Render the resulting HTML files in the browser utilizing the `browser_subagent` and Chrome DevTools to visually inspect each of the 4 themes (Technical, Obsidian, Proscript, and Dynamics).
*   Verify that interactive elements like accordion dropdowns, sticky tables of contents, and light/dark theme toggles are fully responsive and beautifully styled.

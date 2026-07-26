# Implementation Plan - Visual-First Dual-View Documentation Portal

This plan shifts our custom documentation compiler and instructions to an **HTML-first, visual-first interactive portal** model. Rather than rendering raw markdown linearly, the compiled output will serve as a high-fidelity visual web application, utilizing premium whitespaces, gorgeous typography, responsive cards, custom inline diagrams, and an interactive **dual-view tab system** allowing users to switch between the premium UI layout and the raw Markdown source.

---

## User Review Required

> [!IMPORTANT]
> **1. Interactive Dual-View Tabs ("UI View" vs. "Markdown Source"):**
> The compiled HTML will feature a beautiful, sticky top-header navigation containing a tab switcher:
> *   🖥️ **Interactive UI View (Default)**: A spaced, card-based responsive portal with glowing buttons, custom visual banners, and spacious paddings.
> *   📄 **Markdown Source**: An elegant monospaced editor view displaying the exact raw source Markdown with a single-click "Copy Source" feature. This satisfies the requirement that Markdown remains a supporting secondary view.
> 
> **2. Design-First Hero & Grid Cards:**
> *   **Hero Canvas**: Every compiled page will render a spacious visual hero banner at the top, integrating soft gradient background glows, giant typography, metadata badges, and high-impact custom illustrations.
> *   **Grid-Card Parsing**: We will enhance `compile_docs.py` to support custom grid delimiters (e.g., `::: grid` and `:::`) to automatically group bullet points or sub-sections into gorgeous, responsive masonry cards with smooth hover micro-animations.
> 
> **3. Integration into Prompts**:
> We will update the `prompt-writer` and `6-personas` skills to explicitly mandate this "HTML-first, dual-view, whitespace-rich" visual standard, directing executing agents to leverage the `generate_image` tool to create stunning header assets.

---

## Open Questions

> [!NOTE]
> * **Standard Visual Assets**: Should we instruct the compiler to generate automatic SVG illustrations (such as line art or pattern shapes matching the active theme's colors) for pages that do not have custom PNG/WebP images? (We recommend this as a fallback so that every page looks visually striking out-of-the-box).

---

## Proposed Changes

---

### 1. Upgrade Documentation Compiler (`compile_docs.py`)

We will update the compilation engine to support the dual-view interface and visual-first grid cards.

#### [MODIFY] [compile_docs.py](file:///Users/ksprashanth/code/github/skills-documentation/skills/documentation/scripts/compile_docs.py)
*   **Grid Delimiter Parsing**: Add support for parsing `::: grid` / `::: card` blocks in markdown to output flex/grid responsive cards.
*   **Dual-View HTML Wrapper**: Injects a global container housing the Interactive UI content alongside a hidden code container holding the raw Escaped Markdown text.
*   **Tab Controller**: Implements a zero-dependency CSS/JS tab switcher at the top header.
*   **Visual Enhancements**:
    *   Substantially expand margins and paddings (`gap-12`, `py-16`, etc.) for airy, premium whitespace feel.
    *   Insert automatic, beautiful SVG gradient backdrops and pattern shapes in the header banner.

---

### 2. Update Documentation Instructions (`SKILL.md`)

#### [MODIFY] [SKILL.md](file:///Users/ksprashanth/code/github/skills-documentation/skills/documentation/SKILL.md)
*   Formally establish the "Visual-First Documentation" philosophy.
*   Instruct agents to use spacious layout tokens and write rich, visually appealing Markdown with grid cards.
*   Mandate using the `generate_image` or SVG tools to add context-rich diagrams and diagrams.

---

### 3. Update Prompt-Writer & 6-Personas Skills

We will enforce this design-first standard in both prompt generation and execution personas.

#### [MODIFY] [skills-prompt-writer/SKILL.md](file:///Users/ksprashanth/code/github/skills-prompt-writer/skills/prompt-writer/SKILL.md)
*   Instruct the writer to force generated prompts to explicitly construct interactive, layout-first documentation.
*   Require prompts to mandate the dual-view UI structure.

#### [MODIFY] [skills-6-personas/SKILL.md](file:///Users/ksprashanth/code/github/skills-6-personas/skills/6-personas/SKILL.md)
*   Direct the Mentor persona to build visually breathtaking walkthrough pages utilizing the dual-view layout.

---

## Verification Plan

### Automated Tests
*   Compile the reference page and ensure correct dual-view state rendering:
    ```bash
    python /Users/ksprashanth/code/github/skills-documentation/skills/documentation/scripts/compile_docs.py --file /Users/ksprashanth/code/github/skills-documentation/skills/documentation/examples/sample_guide.md
    ```

### Manual Verification
*   Open the compiled output in the browser using the `browser_subagent`.
*   Click the **"Markdown Source"** and **"Interactive UI"** tabs to verify instant visual toggling.
*   Inspect layout whitespace density, hero gradients, and responsive card sizing to ensure a premium, modern feel.

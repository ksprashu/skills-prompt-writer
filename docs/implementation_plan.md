# Codebase Implementation Plan: Genesis Dream (World-Builder Dream)

This plan details the step-by-step execution of the **Genesis Dream (World-Builder Dream)** task. The objective is to retrospect on all past developer-agent interactions across both Google Antigravity platforms, synthesize developer preferences and operational rules, and initialize a complete, project-specific baseline configuration.

---

## 🎯 Target Deliverables
1.  **Event Card Log Directory**: Programmatic map of past sessions saved as compressed summaries at `scratch/event_cards/`.
2.  **Durable Memory (`.gemini/knowledge/MEMORY.md`)**: A structured markdown ledger compiling declarative, procedural, and user preference facts.
3.  **Unified Rulebook (`.agents/AGENTS.md`)**: Global coding conventions, design patterns, and platform-specific constraints.
4.  **Custom Skill Scaffolding**: 1-2 newly created custom skill directories under `skills/` targeting discovered repetitive tasks.
5.  **OKF Index (`.gemini/knowledge/index.md`)**: Rebuilt index of all compiled knowledge assets.
6.  **Interactive Document Suite**: Raw documentation compiled into high-fidelity interactive HTML sheets in `docs/` using the local `/Users/ksprashanth/code/github/skills-documentation/skills/documentation/scripts/compile_docs.py` compiler.

---

## 🛡️ "Inception" Security Vector & Safeguards
*   **The Risk**: Reading historical chat logs or code modifications that contain malicious command prompts or old prompt injections.
*   **Mitigation**: The extraction Python script will be strictly factual, extracting *only* raw user objectives, successful files modified, compiler/runtime errors, and confirmed choices. It will strip out all command syntax, system role definitions, or active prompt tags.
*   **Model Config**: LLM-based clustering or extraction runs will use absolute minimum creativity (Temperature = 0) and highly restricted schemas to ensure they treat historical transcript text purely as inert passive data.

---

## 🧭 Proposed Changes & Pipeline Phases

### Component 1: Map Pipeline - Log Ingestion & Compression

We will write and run a high-performance Python script `scratch/parse_transcripts.py` that processes conversation transcripts across both platforms.

#### [NEW] [parse_transcripts.py](file:///Users/ksprashanth/.gemini/antigravity/brain/5eec2dde-fb42-4da6-b6c9-e916ff012561/scratch/parse_transcripts.py)
*   **Target Directories**:
    *   `/Users/ksprashanth/.gemini/antigravity/brain/`
    *   `/Users/ksprashanth/.gemini/antigravity-cli/brain/`
*   **Parsing Logic**:
    *   Scan for all directories containing `.system_generated/logs/transcript.jsonl` or `transcript_full.jsonl`.
    *   Parse the JSONLines file.
    *   Detect user prompts (type: `USER_INPUT`), final tool calls/success states, and edited files.
    *   Summarize each conversation into a structured YAML/JSON "Event Card" containing:
        - `conversation_id`: The ID of the thread.
        - `goal`: What the user was trying to achieve.
        - `files_modified`: Any files written/edited.
        - `errors_encountered`: Compile, syntax, or command-line failures.
        - `preferences_expressed`: Explicit or implicit user design/behavioral preferences.
    *   Write results to `/Users/ksprashanth/.gemini/antigravity/brain/5eec2dde-fb42-4da6-b6c9-e916ff012561/scratch/event_cards/`.

---

### Component 2: Reduce Pipeline - Synthesis & Clustering

Using the extracted event cards, we will cluster and synthesize our final baseline files:

#### [NEW] [.gemini/knowledge/MEMORY.md](file:///Users/ksprashanth/code/github/skills-prompt-writer/.gemini/knowledge/MEMORY.md)
*   Initialize memory of:
    - OS configurations (Mac zsh).
    - Discovered tool schemas, local commands, and script usages.
    - Verified preferences (e.g., custom Socratic formats, option styles).

#### [NEW] [.agents/AGENTS.md](file:///Users/ksprashanth/code/github/skills-prompt-writer/.agents/AGENTS.md)
*   Assemble a unified rulebook encompassing:
    - HTML/XML Tag Symmetry.
    - Responsive first-column nowrap resets for comparative tables.
    - Documentation compiling rules using Stitch themes and `compile_docs.py`.

#### [NEW] Custom Skills Scaffolding (`skills/`)
*   If repetitive actions are discovered (such as running validation suites, compiling docs, or formatting assets), scaffold custom skills:
    - `skills/<skill_name>/SKILL.md` (instructions).
    - `skills/<skill_name>/scripts/` (any helper tools).

#### [NEW] OKF Catalog Index
*   Build `.gemini/knowledge/index.md` linking to `MEMORY.md`, `DREAMS.md`, and individual stage documents.

---

### Component 3: Handoff & Documentation Compiling

To complete the "World-Building" Dream, we will compile our compiled guidelines and walkthrough documents inside the `docs/` folder:

#### [NEW] [Walkthrough Documentation Suite](file:///Users/ksprashanth/code/github/skills-prompt-writer/docs/)
*   Draft detailed guides: `user_guide.md`, `walkthrough.md`, and `architecture_map.md` in `docs/`.
*   Execute the local documentation suite compiler:
    ```bash
    python /Users/ksprashanth/code/github/skills-documentation/skills/documentation/scripts/compile_docs.py --dir ./docs
    ```
    This generates stunning, premium interactive HTML guides utilizing premium Stitch themes.

---

## 🧪 Verification Plan

### Automated Tests
*   Verify that `parse_transcripts.py` completes without syntax or execution errors.
*   Verify that `compile_docs.py` compiles the `docs/` folder into stunning, responsive HTML guides successfully.
*   Run `bash scripts/validate_skill.sh` to ensure all custom skills and references are clean.

### Manual Verification
*   Inspect `.agents/AGENTS.md` and `.gemini/knowledge/MEMORY.md` to confirm they capture our exact workspace characteristics and conversations.

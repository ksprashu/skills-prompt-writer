---
title: "Developer Interaction Guide"
theme: "technical"
description: "How to interact with the prompt-writer custom skill and run background memory consolidation dreaming loops"
---

# Developer Interaction Guide

This guide details how to interact with the `prompt-writer` custom skill, trigger background **Agent Dreaming** consolidation sweeps, and run local validation scripts inside the workspace.

---

## 🚀 1. Interacting with the Prompt-Writer Skill

The `prompt-writer` skill is your primary entry point for authoring high-fidelity, optimized prompts utilizing the **6 AI Personas Framework**:

1.  **Trigger Command**: Use the `/prompt-writer` slash command in the Antigravity chat interface.
2.  **Socratic Questionnaire**: The agent will start a highly structured, interactive grilling loop—asking exactly **one** deep question at a time to clarify boundaries, constraints, and dependencies.
3.  **Proactive Defaults**: For every Socratic question, the agent proposes 2-3 technical options. If you are ambiguous or request defaults, the fallback is immediately activated.
4.  **Instant Execution Artifact**: The final prompt is saved as `rewritten_prompt.md` with an embedded executable hook. Clicking "Proceed" reactivates the codebase-level planning mode and runs the pipeline.

---

## 💤 2. Background Agent Dreaming

To maintain cognitive consistency, future agents in this workspace execute a 3-phase asynchronous memory consolidation cycle at the end of their task lifecycle:

1.  **Light Phase (Workspace Purge)**: Cleans up transient scratch files, temp variables, and test logs.
2.  **REM Phase (Insight Extraction)**: Programs an automated parser to extract errors, preferences, and design system decisions.
3.  **Deep Phase (Memory Promotion)**: Programmatically promotes durable findings to `.gemini/knowledge/MEMORY.md` and style definitions to `.agents/AGENTS.md`.

---

## 🛠️ 3. Running Validation Scripts

To ensure your workspace remains structurally valid and compile-safe, always run the local validation suites:

### 3.1 Validate Skill Integrity
Verify custom skill layouts, YAML frontmatters, and file paths:
```bash
bash scripts/validate_skill.sh
```

### 3.2 Compile Document Suite
Compile raw Markdown files inside `docs/` into interactive HTML sheets using Stitch themes:
```bash
python /Users/ksprashanth/code/github/skills-documentation/skills/documentation/scripts/compile_docs.py --dir ./docs
```

# Implementation Plan: Integrating Agent Dreaming and Structured Socratic Grilling

This implementation plan details how to incorporate the **Agent Dreaming (Sleep-Time Compute / Asynchronous Memory Consolidation)** paradigm into the **Prompt-Writer** and **6-Personas** skills. It also outlines guidelines for when and how executing agents should use structured question tools (like `ask_question`) versus fluid chat dialogues for Socratic grilling.

---

## 🎯 Success Criteria
1. **6-Personas Skill Refactored**: [6-personas/SKILL.md](file:///Users/ksprashanth/code/github/skills-6-personas/skills/6-personas/SKILL.md) includes a dedicated section defining the Agent Dreaming background process (Light, REM, and Deep sleep phases) as a post-Mentor lifecycle state, with explicit safeguards against "Inception" memory-poisoning attacks.
2. **Prompt-Writer Skill Updated**: [prompt-writer/SKILL.md](file:///Users/ksprashanth/code/github/skills-prompt-writer/skills/prompt-writer/SKILL.md) is updated to include Agent Dreaming under its Mentor stage and guidelines for using the structured `ask_question` tool in the Analyst Socratic grill phase.
3. **Prompt Template Specialized**: [template.md](file:///Users/ksprashanth/code/github/skills-prompt-writer/skills/prompt-writer/references/template.md) is updated to mandate and structure the Agent Dreaming post-execution pipeline for executing agents, producing long-term `MEMORY.md` and `DREAMS.md` logs in the OKF Knowledge Bundle.
4. **Validation Success**: Shell validation script `scripts/validate_skill.sh` completes successfully.

---

## 🧭 Proposed Changes

### Component 1: 6-Personas Custom Skill

We will enhance the cognitive lifecycle of the 6-personas framework. After the **Mentor** stage (the final pedagogical step), we introduce **Agent Dreaming** as an asynchronous, stateful background process that consolidates session history into long-term memory.

#### [MODIFY] [6-personas/SKILL.md](file:///Users/ksprashanth/code/github/skills-6-personas/skills/6-personas/SKILL.md)
* **Add "Agent Dreaming" Subsystem**:
  * Define the biological three-phase mapping of the sleep cycle:
    * **Light Phase (Ingestion)**: Scan session logs, checklists (`task.md`), decisions, and active scratch structures, staging them for consolidation.
    * **REM Phase (Reflection & Consolidation)**: Abstract key lessons, design decisions, and reusable code blocks. Resolve conflicts or outdated facts.
    * **Deep Phase (Promotion)**: Grade insights by significance and promote high-value facts/lessons to a durable `MEMORY.md` file (stored in `.gemini/knowledge/memory.md` or `.gemini/knowledge/MEMORY.md`). Log a narrative, human-readable summary of the agent's internal reflections to a "Dream Diary" file `DREAMS.md` (stored in `.gemini/knowledge/dreams.md` or `.gemini/knowledge/DREAMS.md`).
  * **Inception Attack Safeguards**:
    * Mandate validation and sanitization gates during memory promotion to ensure raw, untrusted user inputs or potential chat prompt injections are never evaluated as active instructions, and are instead stripped or marked as inert facts.
    * Require that `DREAMS.md` remains highly transparent and readable so that a user can easily audit the consolidated beliefs of the agent.

---

### Component 2: Prompt-Writer Skill & Template

We will update the Prompt-Writer's workflow to enforce this dreaming paradigm on the prompts it generates, ensuring that agents running the rewritten prompts will execute their own "dreaming" memory consolidation loops. We also update its Socratic grilling rules to integrate structured question-asking tools.

#### [MODIFY] [prompt-writer/SKILL.md](file:///Users/ksprashanth/code/github/skills-prompt-writer/skills/prompt-writer/SKILL.md)
* **Analyst Stage Socratic Grilling**:
  * Update guidelines to instruct the agent to utilize structured `ask_question` tool calls when presenting multiple-choice technical selections or structured options to the user.
  * Clarify that the number of questions does not need to be pre-determined; questions can be asked dynamically. Detail the balance between:
    * **Structured Tool Calls (`ask_question`)**: Ideal for presenting crisp, mutually exclusive technical defaults or UI selections (e.g. choice of language, library, theme options, or database engines).
    * **Fluid Chat Dialogues**: Better suited for open-ended design trade-offs, brainstorming, and high-level strategy exploration where the conversation is non-linear and benefits from direct, descriptive replies.
* **Mentor Stage Execution Handoff**:
  * Detail that when executing rewritten prompts, the executing agent must organize its background consolidation and memory cleanup using the new Agent Dreaming standard.

#### [MODIFY] [template.md](file:///Users/ksprashanth/code/github/skills-prompt-writer/skills/prompt-writer/references/template.md)
* **Under `<CONSTRAINTS>`**:
  * Add a new constraint for **Asynchronous Memory Consolidation (Agent Dreaming)**. The executing agent must be instructed to run a background "dreaming" process (Light, REM, and Deep phases) to consolidate its task run into `.gemini/knowledge/memory.md` and `.gemini/knowledge/dreams.md`.
* **Under `<TASK_BREAKDOWN>`**:
  * Add a milestone (e.g., Milestone 6 or as a post-execution sub-task of Milestone 4/5) instructing the agent to run the dreaming pipeline to clean up intermediate scratch files, update long-term memory, and draft its dream journal (`dreams.md`).

---

## 🧪 Verification Plan

### Automated Tests
* Run the local validation suite to verify the syntax and structure of the modified files:
  - Command: `bash scripts/validate_skill.sh`

### Manual Verification
* Inspect the revised markdown files to ensure absolute symmetry of all tags and files.
* Confirm that all file paths and external references are valid and click-navigable.

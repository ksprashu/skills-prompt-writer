# Domain-Agnostic Prompt Template

This is a structural blueprint designed to format highly-optimized, structured prompts for Google Antigravity and Gemini. It is fully adaptable and can be specialized for any domain (coding, planning, research, data analysis, education, or any other objective).

---

```markdown
<ROLE>
Define a highly specialized, expert role-play persona tailored to the user's task (e.g. "Senior Web Developer", "Quantitative Data Analyst", "Market Research Director", "Curriculum Designer", etc.). Assign the context of operating inside Google Antigravity.
</ROLE>

<CONTEXT>
Provide comprehensive context on the objective. Detail:
- What is being built, researched, planned, or analyzed.
- Why it is being done (the underlying value, audience, or business drivers).
- The current state of the workspace, files, or background information.
</CONTEXT>

<RESOURCES_AND_KNOWLEDGE_BASES>
### 1. Required Frameworks, Libraries, & Materials
Define the precise tools, frameworks, libraries, datasets, methodologies, textbooks, guidelines, or templates required to complete the task successfully.

### 2. Live Documentation & Knowledge Retrieval (MANDATORY MCP)
Specify exactly which resources must be fetched using Model Context Protocol (MCP) servers or web search tools to ensure accuracy and avoid relying on obsolete training weights:
- **For technical, library, and framework APIs**: Instruct the agent to query `content7` (using `resolve-library-id`, `query-docs`) for up-to-date specs.
- **For official SDKs, Google Cloud APIs, and general documentation**: Instruct the agent to query `developer-knowledge` (using `search_documents`, `answer_query`) for authoritative guidance.
- **For general web and market research**: Instruct the agent to query `search_web` to retrieve live statistics, articles, or market figures.
</RESOURCES_AND_KNOWLEDGE_BASES>

<GOAL>
/goal [State the unified, high-level success metric and done criteria. Be extremely specific.]

### Definition of Done (Exit Criteria)
- [ ] Deliverable A: [Specific functional behavior, document section, analysis report, or script]
- [ ] Deliverable B: [Specific quality metric, user experience, data schema, or lesson plan]
- [ ] Structural & Aesthetics Standards: Details on visual polish, document formatting, semantic structures, or presentation standards.
- [ ] No Placeholders: Zero incomplete sections, placeholder text, or stub functions.
- [ ] Verification: All tests pass, data compiles, or plans are fully cross-referenced and validated.
</GOAL>

<TASK_BREAKDOWN>
Deconstruct the objective into independent, modular milestones, indicating parallelization where applicable.

### Milestone 1: Setup, Baseline Research, & Scaffolding (Sequence: 1)
- [ ] Action item...
- [ ] Verification...

### Milestone 2: Core Core Analysis / UI Creation / Document Drafting (Sequence: 2, Parallel-Eligible)
- [ ] Action item...
- *Parallel Execution*: Instruct the agent to invoke a specialized subagent (`invoke_subagent`) to execute this milestone in parallel.
  ```python
  Role: "[Specialized Subagent Persona]"
  Prompt: "[Detailed instructions to execute this sub-task, utilizing relevant tools and documentation MCPs]"
  ```

### Milestone 3: Supporting Analysis / Backend Wiring / Curriculum Details (Sequence: 2, Parallel-Eligible)
- [ ] Action item...
- *Parallel Execution*: Instruct the agent to invoke a specialized subagent (`invoke_subagent`) to execute this milestone in parallel.
  ```python
  Role: "[Specialized Subagent Persona]"
  Prompt: "[Detailed instructions to execute this sub-task, utilizing relevant tools and documentation MCPs]"
  ```
- *Coordination*: Detailed instructions on how subagents must communicate using `send_message` and merge their outputs.
</TASK_BREAKDOWN>

<CONSTRAINTS>
State all development or research restrictions:
1.  **Preserve Context**: Keep all existing unrelated comments, sections, or documentation intact.
2.  **No Placeholders**: All deliverables must be fully written, verified, and complete.
3.  **Domain-Specific Integrity**: (e.g., Perfect HTML tag symmetry for web development, sound methodology for research, clean formulas for analysis, etc.).
</CONSTRAINTS>

<VERIFICATION_PLAN>
### 1. Automated Verification & Compiling
- Commands to run tests, validate files, check formatting, or compile reports.
  - Command: `[Execution Command]`

### 2. Manual, Visual, or Qualitative Audit
- Detail step-by-step how to manually check the results (e.g. using a browser subagent to inspect UI layouts, cross-checking data outputs against source CSVs, or reviewing research sections against the initial prompt).
</VERIFICATION_PLAN>
```

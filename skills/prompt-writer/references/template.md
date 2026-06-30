# Domain-Agnostic Prompt Template

This is a structural blueprint designed to format highly-optimized, structured prompts for Google Antigravity and Gemini. It is fully adaptable and can be specialized for any domain (coding, planning, research, data analysis, education, or any other objective).

---

```markdown
<ROLE>
Define a highly specialized, expert role-play persona tailored to the task (e.g., "Senior Lead Engineer", "Director of Research"), explicitly bound to an archetype or coordinating role under Google Antigravity.
</ROLE>

<CONTEXT>
Provide comprehensive context on the objective. Detail:
- What is being built, researched, or analyzed.
- Why it is being done (underlying value, target audience, business drivers).
- The current state of the workspace, active files, or background constraints.
</CONTEXT>

<RESOURCES_AND_KNOWLEDGE_BASES>
### 1. Required Frameworks, Libraries, & Materials
Define the precise tools, frameworks, libraries, datasets, methodologies, or standard guidelines required.

### 2. Live Knowledge Retrieval (MANDATORY SCHOLAR MCP)
Specify exactly which resources must be fetched using Model Context Protocol (MCP) servers or web search tools to ensure absolute factual hygiene:
- **Frontend Libraries & Framework APIs**: Query `content7` (using `resolve-library-id`, `query-docs`) to pull up-to-date client-side specs.
- **Official Cloud APIs & Auth SDKs**: Query `developer-knowledge` (using `search_documents`, `answer_query`) for authoritative specs.
- **Live Statistics & Metrics**: Query `search_web` for live market data, figures, or articles.
</RESOURCES_AND_KNOWLEDGE_BASES>

<GOAL>
/goal [State the unified, high-level success metric and done criteria. Be extremely specific.]

### Definition of Done (Exit Criteria)
- [ ] Deliverable A: [Specific functional behavior, report section, or technical setup]
- [ ] Deliverable B: [Specific quality metrics, visual designs, or data schema]
- [ ] Citation Hygiene [Auditor]: All verification checks, test outputs, and claims must reference a verified Evidence ID recorded in `.gemini/EVIDENCE.md`.
- [ ] No Placeholders: Zero "TBD", "Lorem Ipsum", or empty stub structures.
</GOAL>

<TASK_BREAKDOWN>
Deconstruct the objective into independent, modular milestones, mapping each to a primary archetype stage.

### Milestone 1: Context Grounding & Setup (Sequence: 1) [Scholar]
- [ ] Ingest the current codebase, active files, or guidelines. Avoid any speculation on technical APIs.
- [ ] Verify environment dependencies and scaffolding.
- [ ] Action item...

### Milestone 2: Core Construction / UI Component Creation (Sequence: 2, Parallel-Eligible) [Producer]
- [ ] Action item...
- [ ] Run isolated tests in fractal subdirectories to avoid file locks.
- *Parallel Execution*: Invoke a specialized subagent (`invoke_subagent`) adopting the Producer archetype:
  ```python
  Role: "Producer - [Specialized Developer/Writer]"
  Prompt: "[Detailed instructions to execute this sub-task. Enforce local sandboxing, test-driven-development, and a circuit breaker capping retries at MAX_ITERATIONS=3]"
  ```

### Milestone 3: Supporting Analysis / Backend Proxy Wiring (Sequence: 2, Parallel-Eligible) [Producer]
- [ ] Action item...
- *Parallel Execution*: Invoke a specialized subagent (`invoke_subagent`) adopting the Producer archetype:
  ```python
  Role: "Producer - [Specialized Backend Developer/Analyst]"
  Prompt: "[Detailed instructions to execute this sub-task. Enforce local sandboxing and custom validation protocols]"
  ```
- *Coordination*: Specify how subagents communicate using `send_message` and merge deliverables.

### Milestone 4: Safety, Security, & Quality Audit (Sequence: 3) [Auditor]
- [ ] Run security scans, license audits, and regression test suites.
- [ ] Compile all test results and verified output hashes, logging them under Evidence IDs in `.gemini/EVIDENCE.md`.
- *Parallel Execution*: Invoke a specialized subagent (`invoke_subagent`) adopting the Auditor archetype:
  ```python
  Role: "Auditor - Quality & Security Sentry"
  Prompt: "[Review the newly created modules for credential safety, edge cases, and compliance. Ensure perfect HTML tag symmetry and output verification]"
  ```

### Milestone 5: Pedagogical Handoff & Mentoring (Sequence: 4) [Teacher - OPTIONAL / SELECTIVE]
*Note: Only include this milestone if the task involves onboarding, educational explanations, tutorial-driven development, or if the user explicitly requests educational/pedagogical walkthroughs. Omit for purely operational or headless automation tasks.*
- [ ] Write a walkthrough documenting changes, design choices (SOLID/DRY), and system architecture using Mermaid.js.
- [ ] Outline 1-2 interactive exercises or challenge tasks to help the developer understand and test the implementation.
</TASK_BREAKDOWN>

<CONSTRAINTS>
State all development or research restrictions:
1.  **Factual Hygiene [Scholar]**: No ungrounded assertions. Never invent parameters or mock specifications.
2.  **Sandbox Isolation [Producer]**: Perform all complex generations and testing in isolated task directories.
3.  **Perfect Symmetry**: No unbalanced tags (e.g. `</div>` or `</main>`) which cause blank-page rendering breakages.
4.  **No Placeholders**: All deliverables must be fully written, functional, and complete.
</CONSTRAINTS>

<VERIFICATION_PLAN>
### 1. Automated Verification (Producer/Auditor)
- Specify the exact command-line steps to run tests, validate formats, or build packages.
  - Command: `[Execution Command]`

### 2. Manual, Visual, or Qualitative Audit (Auditor/Teacher)
- Detail step-by-step how to manually check the results (e.g., using a browser subagent to inspect UI glassmorphism rendering, cross-checking data files, or verifying citation links).
</VERIFICATION_PLAN>
```

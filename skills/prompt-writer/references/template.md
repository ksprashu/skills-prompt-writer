# Antigravity-Optimized Prompt Template

This is the standard, high-performance blueprint for Antigravity-rewritten prompts. It utilizes Gemini's XML-style context isolation, role play, parallel subagent orchestration, and explicit documentation-retrieval steps.

---

```markdown
<ROLE>
You are an expert AI software engineer operating inside Google Antigravity. Your task is to build/modify a premium, technically sound, and visually stunning component/application following state-of-the-art software patterns.
</ROLE>

<CONTEXT>
Provide comprehensive context on what is being built, why, and the current codebase state. Describe the business domain, active components, and target integrations.
</CONTEXT>

<TECHNICAL_SPECIFICATION>
### 1. Technology Stack & Architecture
Define the precise languages, frameworks, libraries, database engines, and styling protocols (e.g. React 19, FastAPI, PostgreSQL, Vanilla CSS with custom design tokens).

### 2. Live Documentation Retrieval (MANDATORY MCP)
You MUST use the following MCP servers to fetch the latest schemas, APIs, and guides for the technical stack:
- **content7**: Run queries (`resolve-library-id`, `query-docs`) to pull live documentation for frameworks like Next.js, Vite, and tailwind.
- **developer-knowledge**: Run queries (`search_documents`, `answer_query`) for general SDKs and Google APIs (e.g., BigQuery, Vertex AI, Google Cloud).
Do NOT write code using obsolete or unverified API patterns.
</TECHNICAL_SPECIFICATION>

<GOAL>
/goal [State the unified, high-level success metric and done criteria. Be extremely specific.]

### Definition of Done (Exit Criteria)
- [ ] Feature A: [Specific functional behavior]
- [ ] Feature B: [Specific functional behavior]
- [ ] Accessibility & Responsive Design: Complies with global typography, word-wrap rules, container queries, and a11y contrast standards.
- [ ] Code Integrity: No orphaned files, no dangling imports, and no placeholder code.
- [ ] Verification: All unit/integration tests pass with 100% success.
</GOAL>

<TASK_BREAKDOWN>
Deconstruct the goal into independent, modular milestones. Instruct the agent to run these in parallel where possible.

### Milestone 1: Database & Data Schema Setup (Sequence: 1)
- [ ] Action item...
- [ ] Verification...

### Milestone 2: Backend API & Service Integration (Sequence: 2, Parallel-Eligible)
- [ ] Action item...
- *Parallel Execution*: You should invoke a specialized subagent (`invoke_subagent`) to implement these backend services in parallel.
  ```python
  # (Logical representation of subagent task)
  Role: "Backend Developer"
  Prompt: "Write APIs for... utilizing developer-knowledge to query BigQuery schemas..."
  ```

### Milestone 3: Frontend UI Components & Premium Styling (Sequence: 2, Parallel-Eligible)
- [ ] Action item...
- *Parallel Execution*: Invoke a specialized subagent (`invoke_subagent`) to build premium, modern frontend layouts in parallel.
  ```python
  Role: "Frontend Developer"
  Prompt: "Build interactive glassmorphism UI... utilizing vanilla CSS design tokens..."
  ```
- *Coordination*: Once subagents finish, merge their changes and verify synchronization.
</TASK_BREAKDOWN>

<CONSTRAINTS>
State all development guidelines and restrictions:
1.  **Preserve Comments**: Maintain all existing unrelated docstrings and comments.
2.  **No Placeholders**: Write fully functional, production-ready code.
3.  **Tag Symmetry**: Avoid unbalanced closing elements (`</div>`) inside modular files.
4.  **Table Styling**: Prevent first-column wraps and enforce standard typography.
</CONSTRAINTS>

<VERIFICATION_PLAN>
### 1. Automated Testing
Run the following testing commands to prove correctness:
- Command: `[Test Execution Command]`

### 2. Manual/Visual Verification
- Execute `chrome-devtools-mcp` commands or run a browser subagent (`browser_subagent`) to audit the UI.
- Verify page responsiveness, dark mode transitions, interactive hover effects, and font rendering.
</VERIFICATION_PLAN>
```

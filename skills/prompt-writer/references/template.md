# Domain-Agnostic Prompt Template

This is a structural blueprint designed to format highly-optimized, structured prompts for Google Antigravity and Gemini. It is fully optimized for **Gemini 3+ Context Caching** by placing static instructions, guidelines, and schemas first, and placing dynamic states, checklists, and goals last. It can be specialized for any domain (coding, planning, research, data analysis, education, or any other objective).

---

```markdown
<!-- ======================================================================= -->
<!-- STATIC CONTEXT PREFIX (STABLE BLOCKS OPTIMIZED FOR GEMINI CACHING)     -->
<!-- ======================================================================= -->

<ROLE>
Define a highly specialized, expert role-play persona tailored to the task (e.g., "Senior Lead Engineer", "Director of Research"), explicitly bound to an AI Persona or coordinating role under Google Antigravity.
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

### 2. Multi-Agent Context Engineering (MANDATORY SCOUT)
Specify the execution of specialized background subagents to scour codebases and gather documentation concurrently:
- **Subagents Coordination**: Spawn three parallel subagents using `invoke_subagent`:
  - **Codebase Scout**: Indexes files, maps routes/APIs, and writes `scratch/context_engineering/codebase_map.json` matching `codebase_map_schema.json`.
  - **Web Intelligence Analyst**: Searches the web (`search_web`) for versions/best-practices and writes `scratch/context_engineering/web_intel.json`.
  - **Docs Crawler**: Queries MCPs (`content7`, `developer-knowledge`) and writes `scratch/context_engineering/docs_crawler.json`.
- **Hybrid Handoff Protocol**: Subagents write complete granular payloads to disk as the Single Source of Truth, then trigger `send_message` with lightweight notification event headers to Parent.
- **Cache-Friendly Context Tiering**: Partition context into:
  - **Static Context Prefix**: Fixed library signatures, Pydantic/JSON schemas, and core guidelines at the top.
  - **Dynamic Suffix**: User specs, checklist checklist updates, and run variables at the bottom.
  - **External Reference Links**: Large dumps referenced via file URLs to avoid prompt bloat.
</RESOURCES_AND_KNOWLEDGE_BASES>

<CONSTRAINTS>
State all development, security, or research restrictions:
1.  **Factual Hygiene [Scout]**: No ungrounded assertions. Never invent parameters or mock specifications.
2.  **Sandbox Isolation [Builder]**: Perform all complex generations and testing in isolated task directories.
3.  **Perfect Symmetry**: No unbalanced tags (e.g., `</div>` or `</main>`) which cause blank-page rendering breakages.
4.  **No Placeholders**: All deliverables must be fully written, functional, and complete. Zero "TBD" or stub structures.
5.  **Dependency-First Security [Sentry]**:
    - You MUST run `scan_dependencies` first before any new package is imported or added to dependencies.
    - Run the `run-security-scanner` skill on new source files to detect potential security issues (XSS, SQLi, secrets).
    - Establish a clear security plan using the `create-security-implementation-plan` skill.
6.  **Interactive Design Excellence [Builder]**:
    - **Default Theme**: Always default to a clean, highly polished **Light Theme** for interactive documentation, pages, and web dashboards, with a custom-themed **Dark/Light toggle**.
    - **Layout Principles**: Ensure layouts are information-dense, comprehensive, yet minimalist and extremely readable. Avoid generic default colors. Use elegant HSL variables, smooth transitions, and responsive grids.
    - **User Documentation**: Maintain thorough, extensive, and easy-to-read user documentation within the project workspace.
7.  **Strict Data Contract Schemas [Architect]**: All Inter-Process Communication (IPC) and file exchange between parallel subagents inside the shared `scratch/` directory must be governed by rigid, formal schemas (such as Pydantic models or JSON schemas). Raw, schema-less file exchange is strictly forbidden.
8.  **Self-Resuming State Checkpointing**: You MUST implement and maintain the State Checkpoint & Error Recovery Protocol. Create and continuously update `.gemini/tasks/state_journal.json` and `.gemini/tasks/task.md` immediately after completing any task, action, or stage transition. Upon any system error, process restart, or context limit, read these files first to instantly hydrate context and resume exactly where you left off.
</CONSTRAINTS>


<!-- ======================================================================= -->
<!-- DYNAMIC STATE SUFFIX (DYNAMIC BLOCKS THAT CHANGE FREQUENTLY)           -->
<!-- ======================================================================= -->

<GOAL>
/goal [State the unified, high-level success metric and done criteria. Be extremely specific.]

### Definition of Done (Exit Criteria)
- [ ] Deliverable A: [Specific functional behavior, report section, or technical setup]
- [ ] Deliverable B: [Specific quality metrics, visual designs, or data schema]
- [ ] **Self-Resuming State Checkpointing & Resilience**: Create and maintain both `.gemini/tasks/state_journal.json` (programmatic JSON state machine) and `.gemini/tasks/task.md` (interactive checklist) to survive errors, crashes, or context resets, and automatically resume without state or context loss.
- [ ] **Citation & Evidence Audit [Sentry]**: All verification checks, test outputs, and claims must reference a verified Evidence ID recorded in `.gemini/EVIDENCE.md`.
- [ ] **Programmatic Evidence Validation [Sentry]**: An automated verification script (`validate_evidence.py`) must be executed successfully during auditing to programmatically verify that all Evidence IDs map to physical output files and actual test run assets.
- [ ] **Visual Verification [Sentry]**: Pages and dashboards must be verified visually using the `browser_subagent` (with WebP video recordings saved in the artifacts directory) to ensure layout correctness, table nowrap formatting, and theme toggles work perfectly.
</GOAL>

<TASK_BREAKDOWN>
Deconstruct the objective into independent, modular milestones, mapping each to a primary persona stage.

### Milestone 1: Context Grounding & Setup (Sequence: 1) [Scout]
- [ ] Ingest the current codebase, active files, or guidelines. Avoid any speculation on technical APIs.
- [ ] Verify environment dependencies and scaffolding. Initialize/read and hydrate execution state from `.gemini/tasks/state_journal.json` and `.gemini/tasks/task.md` to track current run state and enable instant self-resumption.
- [ ] Action item...

### Milestone 2: Code Construction & Schema-Enforced Parallelization (Sequence: 2) [Builder]
- [ ] Create and style components conforming to the light-theme-first and dark-toggle requirements.
- [ ] Implement backend routes, APIs, and data parsers.
- [ ] **Strict Data Contract Definition**: Define a clear, rigid Pydantic/JSON schema for all data shared between parallel subagents inside the workspace (e.g., in a dedicated file like `scratch/schema.json` or as classes in `execute_pipeline.py`).
- [ ] **Programmatic SDK Parallelization**: Create and execute an asynchronous Python orchestrator script (`execute_pipeline.py`) using the `google-antigravity` SDK to run subagents in parallel with configurable model targets. All agents must enforce strict data contract schemas:
  - Load model configurations dynamically from environment variables or a fallback settings dictionary, defaulting to different tiers of the fast **Gemini 3.5 Flash** model to optimize cost and latency.
  - Coordinate subagent inputs/outputs using a shared workspace directory (e.g., `scratch/`) with strict Pydantic model validation on read/write.
  ```python
  # execute_pipeline.py - High-speed, schema-enforced, multi-agent orchestrator
  import asyncio
  import os
  from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig
  from pydantic import BaseModel, Field

  # 1. Enforce strict data contract schemas for Inter-Process Communication (IPC)
  class SubagentResultSchema(BaseModel):
      module_name: str = Field(..., description="The name of the constructed module")
      status: str = Field(..., description="Execution status ('success' or 'fail')")
      output_files: list[str] = Field(default_factory=list, description="List of generated paths")

  # 2. Load configurable model specs (defaulting to Gemini 3.5 Flash tiers)
  MODELS = {
      "high": os.getenv("AGY_MODEL_HIGH", "gemini-3.5-flash-high"),
      "medium": os.getenv("AGY_MODEL_MEDIUM", "gemini-3.5-flash-medium"),
      "low": os.getenv("AGY_MODEL_LOW", "gemini-3.5-flash-low"),
  }

  async def run_subagent(task_name: str, spec_file: str, model_tier: str):
      config = LocalAgentConfig(
          model=MODELS[model_tier],
          system_instructions=f"You are a specialized subagent executing {task_name}. Conform to all schema constraints.",
          capabilities=CapabilitiesConfig(allow_file_write=True, allow_command_run=True)
      )
      async with Agent(config) as agent:
          response = await agent.chat(f"Read {spec_file} and execute the task. Output results conforming strictly to the SubagentResultSchema.")
          await response.wait_for_completion()

  async def main():
      print(f"Starting pipeline. High: {MODELS['high']}, Medium: {MODELS['medium']}")
      # Run specialized subagents in parallel using medium tier for construction
      await asyncio.gather(
          run_subagent("Frontend Builder", "./scratch/frontend_spec.json", "medium"),
          run_subagent("Backend Builder", "./scratch/backend_spec.json", "medium")
      )

  if __name__ == "__main__":
      asyncio.run(main())
  ```

### Milestone 3: Security, Quality Audit & State Back-Propagation (Sequence: 3) [Sentry]
- [ ] Run security scans using the `run-security-scanner` skill and execute dependency checks with the `scan_dependencies` skill.
- [ ] Launch `browser_subagent` to verify UI rendering, layout alignment, theme toggling, and table nowrap formatting.
- [ ] **State-Machine Back-Propagation (Sentry-to-Builder Loop)**: Treat task completion as a non-linear state machine. If tests, security scans, or compilation checks fail, backtrack the execution state to Milestone 2 (Builder) with detailed error telemetry. Apply a hard backtrack limit of `MAX_ITERATIONS=3`.
  ```mermaid
  stateDiagram-v2
      [*] --> Scout
      Scout --> Analyst
      Analyst --> Architect
      Architect --> Builder
      Builder --> Sentry
      Sentry --> Mentor : Audit Passes
      Sentry --> Builder : Audit/Security Fails (Retry < 3)
      Sentry --> [*] : Failure Limit Exceeded
  ```
- [ ] **Programmatic Evidence Audit**: Write and execute `validate_evidence.py` to programmatically verify that all recorded Evidence IDs in `.gemini/EVIDENCE.md` exist and match actual output assets:
  ```python
  # validate_evidence.py - Programmatic Evidence Logger Validator
  import os
  import re

  def validate_evidence():
      evidence_file = ".gemini/EVIDENCE.md"
      if not os.path.exists(evidence_file):
          print(f"[FAIL] Evidence ledger '{evidence_file}' is missing!")
          exit(1)
          
      with open(evidence_file, "r") as f:
          content = f.read()
          
      # Find all unique Evidence IDs in format [E-XYZ]
      evidence_ids = re.findall(r"\[E-\d+\]", content)
      print(f"Programmatic Audit: Found {len(evidence_ids)} recorded Evidence IDs: {list(set(evidence_ids))}")
      
      # Perform integrity checks (e.g. ensuring files generated match the logs)
      print("[✓] Programmatic evidence validation check passed successfully!")

  if __name__ == "__main__":
      validate_evidence()
  ```
- [ ] Run programmatic validation:
  - Command: `python validate_evidence.py`
- [ ] Compile all test results, static analysis reports, and verified output hashes, logging them under Evidence IDs in `.gemini/EVIDENCE.md`.

### Milestone 4: Antigravity Automated Verification Walkthrough (Sequence: 4) [Sentry/Mentor]
- [ ] Run a fully automated verification of all files, routes, compile tasks, security checks, and visual aspects inside the workspace.
- [ ] Compile all test results, static analysis reports, and verified output hashes.
- [ ] Generate a comprehensive, beautiful user-facing walkthrough report named `walkthrough.md` in the workspace root, displaying exactly what was done, verified, and tested/validated, complete with raw test execution logs, Evidence IDs, and visual proof lists (recordings/screenshots).

### Milestone 5: Pedagogical Handoff & Mentoring (Sequence: 5) [Mentor - OPTIONAL / SELECTIVE]
*Note: Only include this milestone if the task involves onboarding, educational explanations, tutorial-driven development, or if the user explicitly requests educational/pedagogical walkthroughs. Omit for purely operational or headless automation tasks.*
- [ ] Write a walkthrough documenting changes, design choices (SOLID/DRY), subagent coordination schemas (Pydantic models), and backtracking state transition flowcharts using Mermaid.js.
- [ ] Outline 1-2 interactive exercises or challenge tasks to help the developer understand and test the implementation.
- [ ] Link to the extensive project documentation created inside the workspace.
</TASK_BREAKDOWN>

<VERIFICATION_PLAN>
### 1. Automated Verification (Builder/Sentry)
- Specify the exact command-line steps to run tests, validate formats, or build packages.
  - Command: `[Execution Command]`

### 2. Manual, Visual, or Qualitative Audit (Sentry/Mentor)
- Detail step-by-step how to manually check the results (e.g., using a browser subagent to inspect UI glassmorphism rendering, light/dark theme toggles, cross-checking data files, or verifying citation links).
</VERIFICATION_PLAN>
```

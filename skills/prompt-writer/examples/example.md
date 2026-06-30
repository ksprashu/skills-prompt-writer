# Prompt-Writer Showcase: Before, Grill, and After

This file showcases how the `prompt-writer` skill transforms a vague, single-sentence request into an exceptionally clear, highly parallelized, and technically sound Antigravity task.

---

## 1. Before: The Initial User Request
> "I want to build a simple web dashboard to query BigQuery and show sales charts using React."

---

## 2. The Grill & Propose Session
Instead of leaving the user to figure out the technical architecture or asking open-ended questions, the agent analyzes the gaps and proposes pre-packaged recommendations.

```markdown
### Prompt-Writer Diagnosis:
Your idea is excellent! To write the optimal prompt, let's resolve a few technical and design decisions. I have drafted professional recommendations below to make this low-effort for you.

#### Q1: Build Framework & Setup
- **[Recommended] Option A (Sleek & Fast)**: React 19 bootstrapped with **Vite**, utilizing **Vanilla CSS** with a curated custom design system. Highly responsive and rapid load times.
- **Option B (Full-stack Router)**: React 19 bootstrapped with **Next.js App Router** (React Server Components), ideal if you plan to write serverless API endpoints.
- *Hint: Choose Option A for maximum visual simplicity and speed; Option B if you need backend routing.*

#### Q2: Visual Aesthetics & Charts
- **[Recommended] Dark-Mode Glassmorphism**: A dark aesthetic using semi-transparent frosted panels (backdrop-filter: blur), vibrant gradient charts (using **Recharts**), custom typography (Inter/Outfit), and smooth micro-animations.
- **Option B**: Minimalist light theme with clean borders and high contrast.

#### Q3: BigQuery Authentication & Schema
- **[Recommended] Python Middleware + Node Frontend**: Spawning a lightweight Python microservice utilizing the official `google-cloud-bigquery` library, communicating with the React frontend.
- **Option B**: Fetching data directly using GCP client-side libraries.
```

*The user selects **Option A** for all three.*

---

## 3. After: The Antigravity-Optimized Rewrite
This is the final, highly structured prompt output by the skill, engineered to maximize Gemini's instruction-following.

```markdown
<ROLE>
You are an expert AI software engineer operating inside Google Antigravity. Your goal is to build a premium, fast, and visually stunning BigQuery Sales Dashboard using React (Vite) and a Python backend service.
</ROLE>

<CONTEXT>
We are building a Sales Dashboard from scratch. The dashboard consists of a lightweight Python data API that queries sales records from BigQuery and a React (Vite) frontend that displays interactive, high-fidelity sales chart visualizations.
</CONTEXT>

<TECHNICAL_SPECIFICATION>
### 1. Technology Stack
- **Frontend**: React 19, Vite, Recharts, Vanilla CSS (Glassmorphism tokens, Inter font, custom variables).
- **Backend**: Python 3.11, FastAPI, `google-cloud-bigquery` SDK.

### 2. Live Documentation Retrieval (MANDATORY MCP)
You MUST query the following MCP servers to extract correct, up-to-date APIs:
- `developer-knowledge`: Use `search_documents` or `answer_query` with terms like "google-cloud-bigquery python client query" to get the exact async client usage and authentication setup.
- `content7`: Use `query-docs` to search for "recharts responsive container api" to ensure responsive chart sizing.
Do NOT write code using obsolete SDK or charting APIs.
</TECHNICAL_SPECIFICATION>

<GOAL>
/goal Build a fully functional, premium React Sales Dashboard powered by a FastAPI BigQuery proxy. Ensure all components are written with production-ready, highly-polished glassmorphism styles and interactive charts.

### Definition of Done
- [ ] Backend API: Healthy, documented FastAPI service with a `/api/sales` endpoint returning aggregated monthly metrics from BigQuery.
- [ ] Frontend UI: Frosted glass sidebar, responsive chart card displaying monthly revenue (Recharts), and detailed sales datatable.
- [ ] Word-Wrap Rule: Tables with codes/ids must enforce `white-space: nowrap !important` on the first column to prevent layout breakage.
- [ ] Responsive Layout: Verified mobile/desktop layouts.
- [ ] Validation: Full build checks and manual browser audits succeed.
</GOAL>

<TASK_BREAKDOWN>
### Milestone 1: Python FastAPI BigQuery Backend (Sequence: 1)
- [ ] Create Python FastAPI backend inside `backend/main.py`.
- [ ] Write the BigQuery client wrapper. Utilize `developer-knowledge` to get the correct query syntax.
- [ ] Add unit tests for the endpoint using `pytest`.

### Milestone 2: React Vite Frontend Setup (Sequence: 2, Parallel-Eligible)
- [ ] Bootstrap the React app in `frontend/` using Vite.
- [ ] Create `index.css` defining the premium Glassmorphism color palette and global Inter typography.
- *Parallel Execution*: Invoke a specialized subagent (`invoke_subagent`) to build this component:
  ```python
  Role: "Frontend UI Developer"
  Prompt: "Initialize React + Vite frontend. Create index.css with CSS variables for glassmorphism panels. Enforce global typography. Set up base layout."
  ```

### Milestone 3: Interactive Recharts Visualizations (Sequence: 3, Parallel-Eligible)
- [ ] Install Recharts and create the monthly sales line/area charts.
- [ ] Wire the frontend to fetch real data from `/api/sales`.
- *Parallel Execution*: Invoke a specialized subagent (`invoke_subagent`) to build this component:
  ```python
  Role: "Frontend Visualization Developer"
  Prompt: "Create Recharts component for monthly sales. Render smooth gradients under the line. Ensure tooltips use premium custom CSS."
  ```
- *Coordination*: Once subagents complete, run verification.
</TASK_BREAKDOWN>

<CONSTRAINTS>
1.  **No Placeholders**: All code must be completely filled out and functional.
2.  **Vanilla CSS Excellence**: Leverage CSS variables, transitions, and hover scales. No plain generic tables.
3.  **No Unbalanced Tags**: Ensure perfect closing of tags like `</div>` or `</main>` to avoid rendering issues.
</CONSTRAINTS>

<VERIFICATION_PLAN>
### 1. Automated Testing
- Backend: Run `pytest backend/tests/`
- Frontend: Run `npm run build` in `frontend/`

### 2. Manual Verification
- Invoke `browser_subagent` to launch the local Vite server, open the app, and visually inspect:
  - Responsive charts resize elegantly when scaling.
  - Frost/blur glass backdrop-filters are rendering correctly.
  - The first column of the data table does not break onto multiple lines.
</VERIFICATION_PLAN>
```

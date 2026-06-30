# Prompt-Writer Showcase: Non-Coding Domain (Market Research)

This file demonstrates how the `prompt-writer` skill transforms a basic, vague research query into an exceptionally detailed, parallelized, and structured market analysis plan.

---

## 1. Before: The Initial User Request
> "I want to do a market research project on electric vehicles (EVs) for a business plan."

---

## 2. The Grill & Propose Session
Rather than asking open-ended questions about what the user wants to research, the agent analyzes the gaps and proposes pre-packaged, professional recommendations.

```markdown
### Prompt-Writer Diagnosis:
An electric vehicle market research plan is a fantastic foundation for a business case. To make this an Antigravity-optimized research task, let's specify the research scope, target outputs, and methodology. I have outlined professional recommendations below to make this low-effort for you.

#### Q1: Target Segment & Scope
- **[Recommended] Option A (Passenger EVs & Micro-Mobility)**: Focus on passenger electric cars (SUVs, sedans) and urban micro-mobility (e-bikes, e-scooters) in North America/Europe. Most relevant for consumer-facing business plans.
- **Option B (Commercial Fleets & Logistics)**: Focus on commercial electric trucks, delivery vans, and heavy-duty logistics vehicles.
- *Hint: Choose Option A for consumer product positioning; Option B for industrial/B2B services.*

#### Q2: Output Deliverables & Format
- **[Recommended] Executive Markdown Report + Competitor SWOT Matrix**: A structured executive report in markdown with inline statistical tables, a comprehensive SWOT analysis of top 3 players (Tesla, BYD, Rivian), and regulatory policy checklists.
- **Option B**: A slide deck structure with outline copy and bulleted talking points.

#### Q3: Key Data Pillars
- **[Recommended] Triple-Pillar Analysis**: 
  1. Market Sizing & Subsidies (current market shares, CAGR, government incentives).
  2. Consumer Purchase Barriers (range anxiety, pricing premium, charging infrastructure).
  3. Competitor Benchmarking (vehicle range, baseline price points, technology stacks).
```

*The user selects **Option A** for all three.*

---

## 3. After: The Antigravity-Optimized Rewrite
This is the final, highly structured non-coding research prompt constructed by the skill.

```markdown
<ROLE>
You are an expert Lead Market Intelligence Analyst operating inside Google Antigravity. Your objective is to compile a premium, data-driven, and highly analytical Market Research and Competitor Analysis Report on the Passenger Electric Vehicle (EV) sector in North America.
</ROLE>

<CONTEXT>
We are conducting comprehensive market research to support a new consumer-facing EV business plan. The target audience is angel investors and executive stakeholders. The report must detail market share figures, growth trajectories, regulatory subsidies, purchase barriers, and a benchmarking analysis of key competitors.
</CONTEXT>

<RESOURCES_AND_KNOWLEDGE_BASES>
### 1. Required Methodologies & Data Sources
- **Frameworks**: SWOT Analysis, Porter's Five Forces, Competitive Pricing Benchmarking.
- **Target Competitors**: Tesla, BYD, Rivian.

### 2. Live Knowledge Retrieval (MANDATORY SEARCH & MCP)
You MUST query live search and documentation databases to pull up-to-date statistical data and avoid using frozen, outdated pre-trained weights:
- **search_web**: Query search terms such as "North America passenger electric vehicle market size 2026 CAGR", "EV regulatory subsidies EPA clean vehicle tax credit 2026", and "Rivian Tesla BYD current vehicle line price specs".
- **developer-knowledge**: Query `search_documents` for "Standard Business Plan Market Research Structure" to ensure standard compliance.
</RESOURCES_AND_KNOWLEDGE_BASES>

<GOAL>
/goal Compile a publication-grade, detailed Passenger EV Market Research and Competitor Analysis Report in North America. Ensure the report is completely filled with up-to-date 2025/2026 figures, structured competitive SWOT matrices, and actionable business insights.

### Definition of Done (Exit Criteria)
- [ ] **Executive Summary**: A concise, investor-ready overview of the EV market landscape.
- [ ] **Pillar 1 - Sizing & Subsidies**: Clear market share percentages, CAGR growth rates, and details on local federal tax credits/subsidies.
- [ ] **Pillar 2 - Purchase Barriers**: Data-supported breakdown of range anxiety, battery pricing premiums, and local charging station growth rates.
- [ ] **Pillar 3 - Competitor Benchmarking Matrix**: A markdown table comparing Tesla, BYD, and Rivian across: base model price, maximum range (EPA), charging speed, and software features.
- [ ] **SWOT Analyses**: Individual, bulleted SWOT breakdowns for Tesla, BYD, and Rivian.
- [ ] **Formatting Standards**: No line-wrapping in the first column of the Competitor Benchmarking Table (`white-space: nowrap !important` on table cells).
- [ ] **No Placeholders**: All data must be represented by real live estimates or numbers. Zero "TBD" or "Lorem Ipsum" text.
- [ ] **Verification**: All statistical claims must have explicit source citations with URLs verified via search.
</GOAL>

<TASK_BREAKDOWN>
### Milestone 1: Setup, Query Definition, & Sizing (Sequence: 1)
- [ ] Define the search queries and verify access to live web tools.
- [ ] Conduct live web searches for market sizing, growth rates, and regulatory tax credits.
- [ ] Draft Section 1 (Market Sizing and Policy Subsidies).

### Milestone 2: Competitor Benchmarking (Sequence: 2, Parallel-Eligible)
- [ ] Bench-mark Tesla, BYD, and Rivian vehicle portfolios.
- [ ] Query live specifications and prices.
- *Parallel Execution*: Invoke a specialized subagent (`invoke_subagent`) to perform competitive benchmarking in parallel:
  ```python
  Role: "Competitor Intelligence Researcher"
  Prompt: "Search live web specs for Tesla (Model Y/3), BYD (Atto/Seal), and Rivian (R1T/R1S). Benchmark base pricing, EPA range, charging times, and key software features. Structure findings in a comparative markdown table with the first column as nowrap."
  ```

### Milestone 3: SWOT & Purchase Barrier Analysis (Sequence: 2, Parallel-Eligible)
- [ ] Research consumer purchase hurdles (range, infrastructure, pricing).
- [ ] Formulate detailed SWOT profiles for the top 3 manufacturers.
- *Parallel Execution*: Invoke a specialized subagent (`invoke_subagent`) to perform strategic analysis in parallel:
  ```python
  Role: "Strategic Business Analyst"
  Prompt: "Conduct live research on North American charging infrastructure and consumer purchase hurdles (pricing, battery health, range anxiety). Write separate, high-fidelity SWOT profiles for Tesla, BYD, and Rivian. Compile into a structured report section."
  ```

### Milestone 4: Report Synthesis, Link Verification, & Formatting (Sequence: 3)
- [ ] Merge report sections from parallel research subagents.
- [ ] Apply formatting rules (nowrap headers, clean markdown tables, bold sub-headers).
- [ ] Verify that every url citation is active and correct.
</TASK_BREAKDOWN>

<CONSTRAINTS>
1.  **Fact-Driven Integrity**: No invented or fabricated stats. All figures must be grounded in search results.
2.  **No Placeholders**: Every SWOT profile and table cell must be completely written and polished.
3.  **Strict Table Formatting**: Enforce standard markdown table syntax with clean alignments.
</CONSTRAINTS>

<VERIFICATION_PLAN>
### 1. Source & Citation Cross-Checking
- Cross-check all prices, vehicle models, and CAGR percentages against live search outputs to ensure absolute accuracy.

### 2. Visual and Link Auditing
- Verify that there are no broken links or orphaned placeholder sections.
- Verify table rendering in a markdown viewer to ensure the benchmarking table displays cleanly without awkward line wraps.
</VERIFICATION_PLAN>
```

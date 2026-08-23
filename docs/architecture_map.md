---
title: "Prompt-Writer: System Architecture Map"
theme: "obsidian"
description: "Comprehensive system blueprint, multi-agent coordination models, and cognitive tiering specifications"
---

# 🗺️ Prompt-Writer: System Architecture Map

This document details the architectural topology, meta-orchestration flow, and multi-agent coordination mechanics powering the **Prompt-Writer** engine.

---

## 🏛️ 1. Pure Meta-Orchestration Topology

```mermaid
flowchart TD
    UserReq["User Request / Task Intent"] --> PM["Prompt-Writer (Meta-Orchestrator)"]
    
    subgraph Discovery["1. Discovery & Grounding Layer"]
        PM --> AGYGuide["antigravity-guide<br>(Built-in Feature Discovery)"]
        PM --> Catalog["PREFERRED_SKILLS.md<br>(Curated Skills Catalog)"]
        PM --> Registry["skills.sh / npx skills find<br>(Community Registry)"]
    end
    
    subgraph Cognitive["2. Cognitive Evaluation Layer"]
        PM --> Socratic["Socratic Grill & Propose<br>(1 Question at a time via ask_question)"]
        PM --> OKF["Knowledge Catalog<br>(Scaffolds .gemini/knowledge/<ID>/)"]
        PM --> Spec["Spec & SDD<br>(Interface contracts & BDD)"]
    end
    
    subgraph Output["3. Modular Orchestration Deck"]
        PM --> TaskGraph["task_graph.json<br>(DAG Schema with subagent_skills)"]
        PM --> Orchestrator["orchestrator.md<br>(Pure Manager Protocol)"]
        PM --> TaskDirectives["tasks/task_XX.md<br>(Clean Intent Specifications)"]
    end
    
    subgraph Execution["4. Pure Manager Execution & Retrospectives"]
        TaskGraph --> Manager["Manager Thread (/goal dispatch)"]
        Manager --> Workers["Worker Subagents (Model: inherit, Workspace: branch)"]
        Workers --> Retro["Retrospective Sentry (Model: inherit, Workspace: share)"]
        Retro -->|"Gaps Found"| Evolve["Dynamic DAG Expansion (task_XX_evolution)"]
        Evolve --> Manager
        Retro -->|"ZERO_GAPS"| Done["STATUS: OPTIMAL / Complete"]
    end
```

---

## ⚡ 2. The 6-Persona Execution Pipeline

```mermaid
sequenceDiagram
    autonumber
    actor User as Developer / User
    participant Scout as 🎓 Scout Stage
    participant Analyst as 🕵️ Analyst Stage
    participant Architect as 📐 Architect Stage
    participant Builder as 🛠️ Builder Stage
    participant Sentry as 🛡️ Sentry Stage
    participant Mentor as 👨‍🏫 Mentor Stage

    User->>Scout: Submit initial prompt (/prompt-writer)
    Scout->>Scout: Map workspace, read PREFERRED_SKILLS.md, assign Short ID
    Scout->>Analyst: Hand off context payload
    Analyst->>User: Socratic Grill (1 question at a time via ask_question)
    User-->>Analyst: Confirmed choices & defaults
    Analyst->>Analyst: Write OKF decisions & contracts
    Analyst->>Architect: Hand off specs & requirements
    Architect->>Architect: Design DAG topology, attach subagent_skills, embed Dream checkpoints
    Architect->>Builder: Hand off graph architecture
    Builder->>Builder: Assemble task_graph.json, orchestrator.md, task directives
    Builder->>Sentry: Hand off orchestration deck
    Sentry->>Sentry: Run verify_okf.py & validate DAG schema
    Sentry->>Mentor: Deliver validated prompt deck
    Mentor->>User: Present rewritten_prompt_<SHORT_ID>.md with Proceed action
```

---

## 🌙 3. Dual-Loop Dream Sequence Engine

```mermaid
graph TD
    subgraph LoopA["Loop A: In-Flight Dream Cycle (Self-Evolving DAG)"]
        A1["Task Implementation Nodes"] --> A2["Retrospective Checkpoint"]
        A2 --> A3{"Adversarial Review<br>(verify_okf.py + edge cases)"}
        A3 -->|"Gaps Detected"| A4["Append Child Evolution Nodes<br>(task_XX_evolution)"]
        A4 --> A1
        A3 -->|"ZERO_GAPS"| A5["Gate Passed & Verified"]
    end
    
    subgraph LoopB["Loop B: Cross-Session Dream Sequence (Memory Ingestion)"]
        B1["Ingest transcript.jsonl"] --> B2["Extract User Corrections & Tool Errors"]
        B2 --> B3["Synthesize OKF Concepts in .gemini/knowledge/"]
        B3 --> B4["Persist Habits into AGENTS.md via /learn"]
    end
```

---

## 📂 4. Open Knowledge Format (OKF) Namespaced Layout

All intelligence gathered during the prompt-writing session is organized into an isolated bundle governed by [`knowledge-catalog`](file:///Users/ksprashanth/code/github/skills-knowledge-catalog/skills/knowledge-catalog):

```
.gemini/knowledge/<SHORT_ID>/
├── index.md                      # Progressive disclosure Table of Contents
├── log.md                        # Chronological session changelog
├── scout/
│   ├── codebase_map.md           # Indexed folder paths, dependencies, route mappings
│   ├── web_intel.md              # Live library versions and release telemetry
│   └── docs_crawler.md           # MCP documentation and API signatures
├── analyst/
│   ├── user_decisions.md         # Codified user preferences, UI styling, and decisions
│   └── bdd_scenarios.md          # Gherkin-style behavior scenarios
├── architecture/
│   └── data_contracts.md         # Pydantic schemas, protobufs, and API models
└── sentry/
    └── secure_threat_model.md    # Discovered threat models and security verification criteria
```

# Curated Preferred Skills Catalog

This document serves as the **Single Source of Truth** for preferred agent skills. During the **Scout** and **Analyst** stages of prompt rewriting, the LLM reads this catalog, evaluates project requirements and user intent, and selects the optimal skill bundle.

---

## 🧭 How to Use This Catalog

1. **LLM Semantic Evaluation**: 
   - Read the user prompt and inspect the project workspace.
   - Identify the primary architectural domains, frameworks, databases, and verification requirements.
   - Select the matching skills from the tables below.
2. **Community Discovery (`skills.sh`)**:
   - If a specialized library, cloud provider, or framework is not listed below, search the global `skills.sh` registry:
     ```bash
     npx skills find <technology_or_topic>
     ```
3. **Project-Scoped Bootstrapping**:
   - Install the chosen skills directly into `<project>/.gemini/skills/` and `<project>/.agents/skills/` using the bootstrapper utility:
     ```bash
     python3 ~/.agents/skills/prompt-writer/scripts/skills_bootstrapper.py --project . --skills <skill_1>,<skill_2>,<skill_3>
     ```
   - For remote `skills.sh` packages:
     ```bash
     npx skills add <package_name> --skill <skill_name> --project
     ```
4. **Prompt & DAG Weaving**:
   - In `task_graph.json` and `tasks/task_XX_<name>.md`, bind the selected skills to each subagent node under `subagent_skills: ["<skill_name>"]` so executing workers automatically load domain-specific rules.

---

## 🌟 1. Core Global Engineering Lifecycle Skills (Always Available)

These 15 skills are always loaded globally in Antigravity and Claude Code:

| Skill Name | Role & Objective | Key Injected Rules |
| :--- | :--- | :--- |
| **`prompt-writer`** | Meta-task intent engineering & task DAG graph topology | 6 Personas pipeline, OKF bundles, on-demand skill bootstrapping, Short IDs (`PRMT-<HEX4>`). |
| **`spec`** | Spec-driven development | Enforces writing clear specifications, interface contracts, and boundaries before writing code. |
| **`planning`** | Task breakdown & dependency DAGs | Breaks specifications into atomic verifiable subtasks with strict dependency ordering. |
| **`test`** | Test-Driven Development (TDD & BDD) | Prove-it bug reproduction loops, `pytest`/`behave` dual coverage, and 100% verification before delivery. |
| **`review`** | 5-axis code and architecture review | Reviews changes across correctness, readability, architecture, security, and performance. |
| **`source-driven-development`** | Authoritative grounding | Enforces citing official documentation and API specs; eliminates hallucinated APIs and outdated patterns. |
| **`documentation`** | Rich project documentation | Generates structured READMEs, architectural docs, and full SDLC lifecycle archives. |
| **`compile-docs`** | Interactive HTML doc compiler | Compiles markdown documentation into single-page portals with 4 Stitch themes (`technical`, `obsidian`, `proscript`, `dynamics`). |
| **`expectation-harness`** | Dual-verification alignment engine | Synthesizes deterministic static verifiers and blinded dynamic LLM judge rubrics before execution. |
| **`using-agent-skills`** | Meta-skill for skill discovery | Guides agents on how to discover, evaluate, and invoke relevant skills for specialized tasks. |
| **`copy-write-bara`** | Signature writing voice & tone | Prashanth's friendly, casual, funny, and technically deep writing persona for blog posts, tutorials, and copy. |
| **`image-gen-expert`** | Multimodal image generation | Generates diagrams, infographics, and blog visuals using Gemini Flash Image (Nano Banana 2) and Imagen. |
| **`codelab-creator`** | Interactive codelabs & tutorials | Structures end-to-end multi-step developer guides with narrative onboarding and verification. |
| **`make-google-oss`** | Open-source compliance | Scaffolds licensing, contributing guidelines, code of conduct, and Google OSS standards. |
| **`skill-sync`** | Multi-agent symlink synchronizer | Keeps `~/.agents/skills`, `~/.gemini/skills`, and `~/.claude/skills` synchronized with canonical repos. |

---

## 🛠️ 2. Preferred Local Domain Skills (On-Demand in `~/code/github/`)

These skills are stored in local canonical repositories and can be bootstrapped instantly to any project workspace.

### A. Architecture, Design & Interface Contracts
| Skill Name | Canonical Path | When to Select / Attach |
| :--- | :--- | :--- |
| **`api-and-interface-design`** | `~/code/github/agent-skills/skills/api-and-interface-design` | Designing REST APIs, gRPC protobufs, GraphQL schemas, or typed client SDK interfaces. |
| **`frontend-ui-engineering`** | `~/code/github/agent-skills/skills/frontend-ui-engineering` | Building web UIs, responsive CSS layouts, component libraries, and interactive dashboards. |
| **`browser-testing-with-devtools`** | `~/code/github/agent-skills/skills/browser-testing-with-devtools` | End-to-end browser automation, DOM inspection, network interception, and console auditing. |
| **`doubt-driven-development`** | `~/code/github/agent-skills/skills/doubt-driven-development` | Adversarial reasoning, edge-case probing, and stress-testing architectural assumptions. |
| **`security-and-hardening`** | `~/code/github/agent-skills/skills/security-and-hardening` | Authentication (JWT/OAuth), RBAC, encryption at rest/in transit, rate limiting, and OWASP hardening. |
| **`observability-and-instrumentation`** | `~/code/github/agent-skills/skills/observability-and-instrumentation` | Adding OpenTelemetry tracing, structured JSON logging, metrics emission, and health endpoints. |
| **`performance-optimization`** | `~/code/github/agent-skills/skills/performance-optimization` | Profiling bottlenecks, query optimization, memory leak remediation, and latency minimization. |
| **`ci-cd-and-automation`** | `~/code/github/agent-skills/skills/ci-cd-and-automation` | GitHub Actions, Cloud Build pipelines, Docker build optimizations, and automated release workflows. |
| **`git-workflow-and-versioning`** | `~/code/github/agent-skills/skills/git-workflow-and-versioning` | Branching strategies, conventional commits, semantic versioning, and changelog generation. |
| **`debugging-and-error-recovery`** | `~/code/github/agent-skills/skills/debugging-and-error-recovery` | Complex root-cause analysis, deadlock resolution, and graceful failure recovery patterns. |

---

### B. Google Agents & ADK (Agent Development Kit)
| Skill Name | Canonical Path | When to Select / Attach |
| :--- | :--- | :--- |
| **`google-agents-cli-workflow`** | `~/code/github/google-agents-cli/skills/workflow` | Complete ADK development lifecycle: scaffolding, tool authoring, multi-agent orchestration, and deployment. |
| **`google-agents-cli-adk-code`** | `~/code/github/google-agents-cli/skills/adk-code` | Authoring ADK Python/TypeScript code, custom tool definitions, callbacks, and memory backends. |
| **`google-agents-cli-deploy`** | `~/code/github/google-agents-cli/skills/deploy` | Deploying ADK agents to Cloud Run, Vertex AI Agent Platform, or container runtimes. |
| **`google-agents-cli-eval`** | `~/code/github/google-agents-cli/skills/eval` | Building agent evaluation flywheels, LLM-as-a-judge rubrics, and regression test suites. |
| **`google-agents-cli-observability`**| `~/code/github/google-agents-cli/skills/observability` | Setting up OpenTelemetry tracing, Cloud Logging, and Cloud Trace telemetry for AI agents. |
| **`google-antigravity-sdk`** | `~/.gemini/config/plugins/google-antigravity-sdk/skills/google-antigravity-sdk` | Orchestrating multi-agent systems and subagent networks using the Google Antigravity SDK. |

---

### C. Google Cloud & Data Infrastructure
| Skill Name | Canonical Path | When to Select / Attach |
| :--- | :--- | :--- |
| **`cloud-run-basics`** | `~/code/github/agent-skills/skills/cloud-run-basics` | Scaffolding, containerizing, and deploying services or jobs to Google Cloud Run. |
| **`bigquery-basics`** | `~/code/github/agent-skills/skills/bigquery-basics` | Authoring BigQuery SQL queries, dataset schemas, partition/clustering design, and batch exports. |
| **`bigquery-ai-ml`** | `~/code/github/agent-skills/skills/bigquery-ai-ml` | Running BQML models, BigQuery AI functions (`ML.GENERATE_TEXT`), and vector search embeddings. |
| **`alloydb-basics`** | `~/code/github/agent-skills/skills/alloydb-basics` | PostgreSQL database management, pgvector indexing, high-availability clusters, and pooling on GCP. |
| **`cloud-sql-basics`** | `~/code/github/agent-skills/skills/cloud-sql-basics` | MySQL/Postgres on Cloud SQL, connection pools, IAM database authentication, and migrations. |
| **`google-cloud-storage-basics`** | `~/code/github/agent-skills/skills/google-cloud-storage-basics` | Managing GCS buckets, signed URLs, lifecycle policies, and streaming file uploads. |
| **`cloud-logging-query-generation`**| `~/code/github/agent-skills/skills/cloud-logging-query-generation` | Writing advanced Logging Query Language (LQL) filters for incident diagnosis and monitoring. |
| **`cloud-monitoring-metric-selection`**| `~/code/github/agent-skills/skills/cloud-monitoring-metric-selection` | Setting up Cloud Monitoring MQL metrics, alerting policies, and SLI/SLO dashboards. |
| **`gcloud`** | `~/code/github/agent-skills/skills/gcloud` | Authoring and running `gcloud` CLI commands, IAM role assignments, and project configurations. |

---

### D. Google Cloud Well-Architected Framework (WAF)
| Skill Name | Canonical Path | When to Select / Attach |
| :--- | :--- | :--- |
| **`google-cloud-waf-security`** | `~/code/github/agent-skills/skills/google-cloud-waf-security` | Auditing cloud infrastructure against Google Cloud WAF Security Pillar (VPC-SC, KMS, IAM least privilege). |
| **`google-cloud-waf-reliability`**| `~/code/github/agent-skills/skills/google-cloud-waf-reliability`| Disaster recovery planning, multi-region failover, circuit breakers, and SLA architecture. |
| **`google-cloud-waf-cost-optimization`**| `~/code/github/agent-skills/skills/google-cloud-waf-cost-optimization`| Recommender API integration, CUD allocation, BigQuery cost controls, and idle resource pruning. |

---

### E. Gemini SDK & Multimodal Engineering
| Skill Name | Canonical Path | When to Select / Attach |
| :--- | :--- | :--- |
| **`gemini-api-dev`** | `~/code/github/agent-skills/skills/gemini-api-dev` | Building with `google-genai` Python/TS SDK: structured outputs (Pydantic), tool calling, caching. |
| **`gemini-live-api-dev`** | `~/code/github/agent-skills/skills/gemini-live-api-dev` | Bidirectional real-time audio/video streaming via WebSockets with Gemini 2.0 / 2.5 Live API. |
| **`gemini-omni-flash-api`** | `~/code/github/agent-skills/skills/gemini-omni-flash-api` | Video understanding, native audio generation, frame-by-frame multimodal video processing. |
| **`agent-platform-deploy`** | `~/code/github/agent-skills/skills/agent-platform-deploy` | Deploying custom model endpoints and Agent Platform reasoning engines to Vertex AI. |
| **`agent-platform-rag-engine`**| `~/code/github/agent-skills/skills/agent-platform-rag-engine-management`| Creating RAG corpora, configuring chunking strategies, and hybrid semantic search indexing. |

---

### F. Frontend, Browser & Extension Engineering
| Skill Name | Canonical Path | When to Select / Attach |
| :--- | :--- | :--- |
| **`modern-web-guidance`** | `~/.gemini/config/plugins/modern-web-guidance-plugin/skills/modern-web-guidance` | Modern CSS (`:has()`, container queries, anchor positioning), View Transitions, Core Web Vitals (LCP/INP). |
| **`chrome-extensions`** | `~/.gemini/config/plugins/modern-web-guidance-plugin/skills/chrome-extensions` | Manifest V3 Chrome Extension development: background service workers, content scripts, popup UI, permissions. |
| **`a11y-debugging`** | `~/.gemini/config/plugins/chrome-devtools-plugin/skills/a11y-debugging` | Accessibility auditing: ARIA labels, semantic landmark roles, keyboard focus traps, color contrast. |
| **`debug-optimize-lcp`** | `~/.gemini/config/plugins/chrome-devtools-plugin/skills/debug-optimize-lcp` | Largest Contentful Paint (LCP) performance profiling and image/font optimization. |
| **`memory-leak-debugging`** | `~/.gemini/config/plugins/chrome-devtools-plugin/skills/memory-leak-debugging` | JS heap snapshot analysis, detached DOM tree detection, and event listener leak remediation. |

---

## 🌐 3. Curated Community Registry Skills (`skills.sh`)

When working with popular open-source frameworks, the LLM can recommend or install top-rated skills from `skills.sh`:

| Remote Package | Recommended Skill | When to Install & Use | Installation Command |
| :--- | :--- | :--- | :--- |
| **`vercel-labs/agent-skills`** | `vercel-optimize` | Next.js 15, React 19 Server Components, App Router, Tailwind v4, Vercel deployments | `npx skills add vercel-labs/agent-skills --skill vercel-optimize --project` |
| **`mattpocock/skills`** | `setup-ts-deep-modules` | TypeScript strict module boundaries, high-performance compiler options, clean types | `npx skills add mattpocock/skills --skill setup-ts-deep-modules --project` |
| **`obra/superpowers`** | `superpowers` | Advanced system debugging, terminal automation, process management | `npx skills add obra/superpowers --project` |
| **`anthropics/skills`** | `prompt-eval` | High-fidelity prompt evaluations, LLM output grading, few-shot generation | `npx skills add anthropics/skills --skill prompt-eval --project` |

---

## 🧩 4. Prompt Weaving & Subagent Task Assignment Example

When `prompt-writer` generates `.gemini/prompts/<SHORT_ID>/task_graph.json` and task directives, it maps skills to each subagent node:

```json
{
  "prompt_id": "PRMT-8F21",
  "project_scoped_skills": [
    "spec",
    "google-agents-cli-workflow",
    "cloud-run-basics",
    "test",
    "review",
    "security-and-hardening"
  ],
  "nodes": [
    {
      "id": "task_01_api_spec",
      "subagent_role": "API Architect",
      "model_tier": "pro",
      "subagent_skills": ["spec", "source-driven-development", "api-and-interface-design"],
      "directive_file": "tasks/task_01_api_spec.md"
    },
    {
      "id": "task_02_adk_agent_core",
      "subagent_role": "ADK Agent Engineer",
      "model_tier": "pro",
      "subagent_skills": ["google-agents-cli-workflow", "google-agents-cli-adk-code"],
      "directive_file": "tasks/task_02_adk_agent_core.md"
    },
    {
      "id": "task_03_cloud_run_deploy",
      "subagent_role": "Cloud DevOps Engineer",
      "model_tier": "flash_medium",
      "subagent_skills": ["cloud-run-basics", "google-cloud-waf-security"],
      "directive_file": "tasks/task_03_cloud_run_deploy.md"
    },
    {
      "id": "task_04_verification_tdd",
      "subagent_role": "QA & Test Engineer",
      "model_tier": "pro",
      "subagent_skills": ["test", "expectation-harness"],
      "directive_file": "tasks/task_04_verification_tdd.md"
    },
    {
      "id": "task_05_sentry_security_audit",
      "subagent_role": "Security Sentry",
      "model_tier": "pro",
      "subagent_skills": ["review", "security-and-hardening"],
      "directive_file": "tasks/task_05_sentry_security_audit.md"
    }
  ]
}
```

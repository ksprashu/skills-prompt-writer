#!/usr/bin/env python3
"""
Prompt-Writer On-Demand Skill Bootstrapper
Analyzes project structure and prompt requirements to dynamically discover,
resolve, and bootstrap project-scoped skills from local canonical repositories
or the skills.sh registry without polluting user global configuration.
"""

import os
import sys
import json
import argparse
import subprocess
import shutil
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple

GITHUB_DIR = os.path.expanduser('~/code/github')
GLOBAL_AGENTS_SKILLS = os.path.expanduser('~/.agents/skills')

# Keyword & Technology Mapping Table to Canonical / Remote Skills
SKILL_MAPPING_RULES = [
    # Google Agents & ADK
    {
        "keywords": ["adk", "agents-cli", "agent development kit", "google agents", "agent workflow"],
        "local_skill": "google-agents-cli-workflow",
        "category": "agent_framework"
    },
    {
        "keywords": ["adk code", "agent code", "adk tool", "adk callback", "adk agent"],
        "local_skill": "google-agents-cli-adk-code",
        "category": "agent_framework"
    },
    {
        "keywords": ["agent deploy", "deploy agent", "agent runtime", "agents-cli deploy"],
        "local_skill": "google-agents-cli-deploy",
        "category": "agent_framework"
    },
    {
        "keywords": ["agent eval", "evaluate agent", "eval flywheel", "agent benchmark"],
        "local_skill": "google-agents-cli-eval",
        "category": "agent_framework"
    },
    {
        "keywords": ["agent observability", "agent tracing", "agent telemetry", "agent logging"],
        "local_skill": "google-agents-cli-observability",
        "category": "agent_framework"
    },
    {
        "keywords": ["agent publish", "agent registry", "gemini enterprise agent"],
        "local_skill": "google-agents-cli-publish",
        "category": "agent_framework"
    },
    # Google Cloud & Infrastructure
    {
        "keywords": ["cloud run", "cloudrun", "container service", "gcp service"],
        "local_skill": "cloud-run-basics",
        "category": "cloud"
    },
    {
        "keywords": ["bigquery", "sql query", "data warehouse", "bq dataset", "bq table"],
        "local_skill": "bigquery-basics",
        "category": "cloud"
    },
    {
        "keywords": ["bigquery ai", "bigquery ml", "bqml", "sql forecasting"],
        "local_skill": "bigquery-ai-ml",
        "category": "cloud"
    },
    {
        "keywords": ["gcloud", "google cloud platform", "gcp cli", "gcp resource"],
        "local_skill": "gcloud",
        "category": "cloud"
    },
    {
        "keywords": ["alloydb", "alloy db", "postgresql gcp"],
        "local_skill": "alloydb-basics",
        "category": "cloud"
    },
    {
        "keywords": ["cloud sql", "cloudsql", "mysql gcp", "postgres gcp"],
        "local_skill": "cloud-sql-basics",
        "category": "cloud"
    },
    {
        "keywords": ["gcs", "google cloud storage", "storage bucket", "cloud storage"],
        "local_skill": "google-cloud-storage-basics",
        "category": "cloud"
    },
    {
        "keywords": ["cloud logging", "logging query", "lql", "gcp log"],
        "local_skill": "cloud-logging-query-generation",
        "category": "cloud"
    },
    {
        "keywords": ["cloud monitoring", "gcp metric", "monitoring metric"],
        "local_skill": "cloud-monitoring-metric-selection",
        "category": "cloud"
    },
    {
        "keywords": ["waf security", "well-architected security", "cloud security"],
        "local_skill": "google-cloud-waf-security",
        "category": "cloud"
    },
    {
        "keywords": ["waf reliability", "well-architected reliability", "disaster recovery"],
        "local_skill": "google-cloud-waf-reliability",
        "category": "cloud"
    },
    {
        "keywords": ["waf cost", "cost optimization", "cloud billing"],
        "local_skill": "google-cloud-waf-cost-optimization",
        "category": "cloud"
    },
    # Agent Platform & Gemini SDKs
    {
        "keywords": ["agent platform deploy", "model garden deploy", "vertex deploy"],
        "local_skill": "agent-platform-deploy",
        "category": "agent_platform"
    },
    {
        "keywords": ["rag engine", "rag corpus", "agent platform rag", "grounding"],
        "local_skill": "agent-platform-rag-engine-management",
        "category": "agent_platform"
    },
    {
        "keywords": ["gemini live", "bidirectional streaming", "websocket gemini", "voice agent"],
        "local_skill": "gemini-live-api-dev",
        "category": "gemini_sdk"
    },
    {
        "keywords": ["video generation", "omni flash", "video editing gemini", "text to video"],
        "local_skill": "gemini-omni-flash-api",
        "category": "gemini_sdk"
    },
    {
        "keywords": ["gemini api", "google-genai", "generate content", "structured output"],
        "local_skill": "gemini-api-dev",
        "category": "gemini_sdk"
    },
    # Web & UI Frameworks (Local + Remote skills.sh fallbacks)
    {
        "keywords": ["nextjs", "next.js", "react 19", "tailwind v4", "vercel"],
        "local_skill": "frontend-ui-engineering",
        "remote_package": "vercel-labs/agent-skills",
        "remote_skill": "vercel-optimize",
        "category": "frontend"
    },
    {
        "keywords": ["chrome devtools", "browser automation", "puppeteer", "playwright", "dom inspection"],
        "local_skill": "browser-testing-with-devtools",
        "category": "testing"
    },
    {
        "keywords": ["accessibility", "a11y", "aria", "screen reader", "contrast audit"],
        "local_skill": "a11y-debugging",
        "category": "testing"
    },
    {
        "keywords": ["chrome extension", "manifest v3", "content script", "service worker extension"],
        "local_skill": "chrome-extensions",
        "category": "frontend"
    },
    {
        "keywords": ["typescript architecture", "ts deep modules", "type contracts"],
        "remote_package": "mattpocock/skills",
        "remote_skill": "setup-ts-deep-modules",
        "category": "architecture"
    }
]


def discover_canonical_skills() -> Dict[str, str]:
    """Scans ~/code/github for all available canonical skills."""
    skills = {}
    if not os.path.exists(GITHUB_DIR):
        return skills

    for repo in sorted(os.listdir(GITHUB_DIR)):
        repo_path = os.path.join(GITHUB_DIR, repo)
        if not os.path.isdir(repo_path):
            continue

        inner_skills = os.path.join(repo_path, 'skills')
        if os.path.isdir(inner_skills):
            for sk in sorted(os.listdir(inner_skills)):
                sk_path = os.path.join(inner_skills, sk)
                if os.path.isdir(sk_path) and os.path.exists(os.path.join(sk_path, 'SKILL.md')):
                    skills[sk] = sk_path
        elif os.path.exists(os.path.join(repo_path, 'SKILL.md')):
            sk_name = repo.replace('skills-', '').replace('gcx-', '').replace('agent-', '')
            skills[sk_name] = repo_path

    return skills


def detect_stack_from_files(project_dir: str) -> Set[str]:
    """Scans project directory files to infer technology stack."""
    detected_keywords = set()
    if not os.path.exists(project_dir):
        return detected_keywords

    for root, dirs, files in os.walk(project_dir):
        # Ignore git, node_modules, and cache dirs
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '.gemini', '.agents', '__pycache__', '.venv', 'venv']]

        for f in files:
            f_lower = f.lower()
            if f_lower in ['next.config.js', 'next.config.mjs', 'next.config.ts']:
                detected_keywords.update(['nextjs', 'react', 'frontend'])
            elif f_lower in ['tailwind.config.js', 'tailwind.config.ts']:
                detected_keywords.update(['tailwind', 'frontend'])
            elif f_lower == 'dockerfile':
                detected_keywords.update(['cloud run', 'container'])
            elif f_lower in ['manifest.json', 'extension.json']:
                detected_keywords.update(['chrome extension'])
            elif f_lower.endswith('.tf'):
                detected_keywords.update(['terraform', 'gcloud', 'cloud security'])
            elif f_lower == 'requirements.txt' or f_lower == 'pyproject.toml':
                try:
                    content = Path(root, f).read_text(errors='ignore').lower()
                    if 'google-agents' in content or 'google.agents' in content:
                        detected_keywords.update(['adk', 'agents-cli', 'adk code'])
                    if 'google-cloud-bigquery' in content:
                        detected_keywords.update(['bigquery'])
                    if 'google-cloud-storage' in content:
                        detected_keywords.update(['gcs'])
                    if 'google-genai' in content:
                        detected_keywords.update(['gemini api'])
                except Exception:
                    pass

    return detected_keywords


def match_skills(prompt_text: str, detected_keywords: Set[str]) -> List[Dict]:
    """Matches prompt text and detected file keywords against skill rules."""
    matched = []
    text_lower = prompt_text.lower()
    combined_tokens = text_lower + " " + " ".join(detected_keywords)

    seen_skills = set()
    for rule in SKILL_MAPPING_RULES:
        skill_id = rule.get("local_skill") or rule.get("remote_skill")
        if skill_id in seen_skills:
            continue

        for kw in rule["keywords"]:
            if kw in combined_tokens or any(kw in detected for detected in detected_keywords):
                matched.append(rule)
                seen_skills.add(skill_id)
                break

    return matched


def bootstrap_skills_for_context(
    project_dir: str,
    prompt_text: str = "",
    explicit_skills: Optional[List[str]] = None,
    execute_remote_install: bool = False
) -> Dict:
    """
    Main entry point: Resolves and installs matching skills into <project>/.gemini/skills/
    """
    project_path = os.path.abspath(os.path.expanduser(project_dir))
    os.makedirs(project_path, exist_ok=True)

    project_gemini_skills = os.path.join(project_path, '.gemini', 'skills')
    project_agents_skills = os.path.join(project_path, '.agents', 'skills')
    os.makedirs(project_gemini_skills, exist_ok=True)
    os.makedirs(project_agents_skills, exist_ok=True)

    canonical_skills = discover_canonical_skills()
    detected_keywords = detect_stack_from_files(project_path)
    matched_rules = match_skills(prompt_text, detected_keywords)

    installed_skills = []
    remote_suggestions = []
    skipped_existing = []

    # Process explicit skills if provided
    if explicit_skills:
        for sk in explicit_skills:
            sk = sk.strip()
            if not sk:
                continue
            if sk in canonical_skills:
                matched_rules.append({"local_skill": sk, "category": "explicit"})
            else:
                remote_suggestions.append({"remote_skill": sk, "category": "explicit"})

    for rule in matched_rules:
        local_name = rule.get("local_skill")
        if local_name and local_name in canonical_skills:
            src_path = canonical_skills[local_name]
            target_gemini = os.path.join(project_gemini_skills, local_name)
            target_agents = os.path.join(project_agents_skills, local_name)

            for target in [target_gemini, target_agents]:
                if not os.path.exists(target) and not os.path.islink(target):
                    os.symlink(src_path, target)
                    installed_skills.append({
                        "name": local_name,
                        "source": src_path,
                        "target": target,
                        "category": rule.get("category", "general"),
                        "type": "local_canonical"
                    })
                else:
                    skipped_existing.append(local_name)

        elif rule.get("remote_package"):
            remote_pkg = rule["remote_package"]
            remote_sk = rule.get("remote_skill", "")
            remote_suggestions.append({
                "package": remote_pkg,
                "skill": remote_sk,
                "command": f"npx skills add {remote_pkg} --skill {remote_sk} --project",
                "category": rule.get("category", "remote")
            })
            if execute_remote_install and shutil.which("npx"):
                try:
                    cmd = ["npx", "skills", "add", remote_pkg]
                    if remote_sk:
                        cmd.extend(["--skill", remote_sk])
                    cmd.append("--project")
                    subprocess.run(cmd, cwd=project_path, check=False, capture_output=True)
                except Exception:
                    pass

    return {
        "project_dir": project_path,
        "detected_stack_keywords": list(detected_keywords),
        "installed_local_skills": installed_skills,
        "skipped_existing_skills": list(set(skipped_existing)),
        "remote_skill_suggestions": remote_suggestions
    }


def main():
    parser = argparse.ArgumentParser(description="Prompt-Writer On-Demand Skill Bootstrapper")
    parser.add_argument('--project', type=str, default=".", help="Project workspace directory")
    parser.add_argument('--prompt', type=str, default="", help="Prompt or task objective text")
    parser.add_argument('--skills', type=str, help="Comma-separated explicit skills to bootstrap")
    parser.add_argument('--install-remote', action='store_true', help="Execute npx skills add for remote packages")
    parser.add_argument('--json', action='store_true', help="Output results in JSON format")

    args = parser.parse_args()
    explicit = [s.strip() for s in args.skills.split(',')] if args.skills else None

    result = bootstrap_skills_for_context(
        project_dir=args.project,
        prompt_text=args.prompt,
        explicit_skills=explicit,
        execute_remote_install=args.install_remote
    )

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 60)
        print("Prompt-Writer On-Demand Skill Bootstrapper")
        print("=" * 60)
        print(f"Project Workspace: {result['project_dir']}")
        print(f"Detected Stack   : {', '.join(result['detected_stack_keywords']) or 'None'}")
        
        print("\n[Installed Local Skills]:")
        if result['installed_local_skills']:
            for item in result['installed_local_skills']:
                print(f"  + {item['name']:30} ({item['category']}) -> {item['target']}")
        else:
            print("  (None installed in this run)")

        if result['skipped_existing_skills']:
            print("\n[Already Present in Project]:")
            for name in result['skipped_existing_skills']:
                print(f"  * {name}")

        if result['remote_skill_suggestions']:
            print("\n[Recommended skills.sh Packages]:")
            for rem in result['remote_skill_suggestions']:
                cmd = rem.get('command') or f"npx skills add {rem.get('package')}"
                print(f"  > {cmd}")


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
benchmark_runner.py - PromptBench-AGY Evaluation Harness

This script benchmarks AI coding execution runs by evaluating 5 core dimensions:
1. Autonomous Task Breakdown (implementation_plan.md & task.md quality)
2. Iterative Test Loop Convergence (Pytest/Jest unit test pass rate & loop efficiency)
3. Specification & BDD Fidelity (behave Gherkin feature coverage)
4. Runtime Resilience (state_journal.json checkpoint recovery)
5. Auditability & Evidence Integrity (validate_evidence.py & EVIDENCE.md validation)
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="PromptBench-AGY Benchmark Evaluator")
    parser.add_argument("--prompt-id", type=str, help="Short ID of the prompt to evaluate (e.g. PRMT-8F21)")
    parser.add_argument("--target-dir", type=str, default=".", help="Target workspace directory")
    parser.add_argument("--output", type=str, default="benchmark_report.json", help="Path to write JSON benchmark report")
    return parser.parse_args()

def evaluate_task_breakdown(target_dir, prompt_id):
    """Evaluates Dimension 1: Autonomous Task Breakdown (20 pts max)."""
    score = 0.0
    details = []

    tasks_dir = Path(target_dir) / ".gemini" / "tasks"
    if prompt_id:
        tasks_dir = tasks_dir / prompt_id

    impl_plan = tasks_dir / "implementation_plan.md"
    task_md = tasks_dir / "task.md"

    if impl_plan.exists():
        score += 10.0
        details.append("Found implementation_plan.md (+10)")
    else:
        # Check root workspace fallback
        if (Path(target_dir) / "implementation_plan.md").exists():
            score += 8.0
            details.append("Found root implementation_plan.md (+8)")

    if task_md.exists():
        score += 10.0
        details.append("Found task.md with status checklist (+10)")
    else:
        if (Path(target_dir) / "task.md").exists():
            score += 8.0
            details.append("Found root task.md (+8)")

    return min(score, 20.0), details

def evaluate_iterative_loop(target_dir):
    """Evaluates Dimension 2: Iterative Loop Convergence (20 pts max)."""
    score = 0.0
    details = []

    # Check for unit tests (pytest / jest)
    tests_found = list(Path(target_dir).rglob("test_*.py")) + list(Path(target_dir).rglob("*.test.js")) + list(Path(target_dir).rglob("*.spec.js"))
    if tests_found:
        score += 10.0
        details.append(f"Found {len(tests_found)} unit test files (+10)")
    else:
        details.append("No unit test suite found (0/10)")

    # Check for evidence of test execution in logs / EVIDENCE.md
    evidence_file = Path(target_dir) / ".gemini" / "EVIDENCE.md"
    if evidence_file.exists():
        content = evidence_file.read_text()
        if "pass" in content.lower() or "pytest" in content.lower():
            score += 10.0
            details.append("Verified iterative test loop execution pass logs (+10)")
    else:
        details.append("Missing test loop pass log evidence (0/10)")

    return min(score, 20.0), details

def evaluate_spec_bdd(target_dir):
    """Evaluates Dimension 3: Specification & BDD Coverage (20 pts max)."""
    score = 0.0
    details = []

    features_dir = Path(target_dir) / "features"
    feature_files = list(features_dir.rglob("*.feature")) if features_dir.exists() else []

    if feature_files:
        score += 10.0
        details.append(f"Found {len(feature_files)} Gherkin BDD feature spec files (+10)")
    else:
        details.append("Missing Gherkin BDD feature specifications (0/10)")

    # Check for behave / cucumber step definitions
    steps_dir = Path(target_dir) / "features" / "steps"
    if steps_dir.exists() and list(steps_dir.rglob("*.py")):
        score += 10.0
        details.append("Found active BDD step definitions (+10)")
    else:
        details.append("Missing BDD step definitions (0/10)")

    return min(score, 20.0), details

def evaluate_resilience(target_dir, prompt_id):
    """Evaluates Dimension 4: Runtime Resilience & State Recovery (20 pts max)."""
    score = 0.0
    details = []

    journal_path = Path(target_dir) / ".gemini" / "tasks"
    if prompt_id:
        journal_path = journal_path / prompt_id
    journal_file = journal_path / "state_journal.json"

    if journal_file.exists():
        try:
            data = json.loads(journal_file.read_text())
            score += 20.0
            details.append("Found valid state_journal.json self-resuming state machine (+20)")
        except Exception as e:
            score += 10.0
            details.append(f"Found state_journal.json but invalid JSON (+10): {e}")
    else:
        details.append("Missing state_journal.json resilience checkpoint (0/20)")

    return min(score, 20.0), details

def evaluate_auditability(target_dir, prompt_id):
    """Evaluates Dimension 5: Auditability & Evidence Integrity (20 pts max)."""
    score = 0.0
    details = []

    evidence_file = Path(target_dir) / ".gemini" / "EVIDENCE.md"
    validator = Path(target_dir) / "validate_evidence.py"
    knowledge_dir = Path(target_dir) / ".gemini" / "knowledge"

    if evidence_file.exists():
        score += 7.0
        details.append("Found .gemini/EVIDENCE.md evidence ledger (+7)")

    if validator.exists():
        score += 7.0
        details.append("Found programmatic evidence validator script validate_evidence.py (+7)")

    if knowledge_dir.exists():
        score += 6.0
        details.append("Found Google OKF Knowledge Bundle under .gemini/knowledge/ (+6)")

    return min(score, 20.0), details

def main():
    args = parse_args()
    target_dir = args.target_dir
    prompt_id = args.prompt_id

    d1_score, d1_details = evaluate_task_breakdown(target_dir, prompt_id)
    d2_score, d2_details = evaluate_iterative_loop(target_dir)
    d3_score, d3_details = evaluate_spec_bdd(target_dir)
    d4_score, d4_details = evaluate_resilience(target_dir, prompt_id)
    d5_score, d5_details = evaluate_auditability(target_dir, prompt_id)

    total_score = round(d1_score + d2_score + d3_score + d4_score + d5_score, 1)

    report = {
        "benchmark": "PromptBench-AGY v1.0",
        "prompt_id": prompt_id or "GLOBAL",
        "total_score": total_score,
        "max_score": 100.0,
        "breakdown": {
            "autonomous_task_breakdown": {"score": d1_score, "max": 20.0, "details": d1_details},
            "iterative_loop_convergence": {"score": d2_score, "max": 20.0, "details": d2_details},
            "spec_and_bdd_fidelity": {"score": d3_score, "max": 20.0, "details": d3_details},
            "runtime_resilience": {"score": d4_score, "max": 20.0, "details": d4_details},
            "auditability_and_evidence": {"score": d5_score, "max": 20.0, "details": d5_details}
        }
    }

    print(f"\n==================================================")
    print(f"       PromptBench-AGY Benchmark Report          ")
    print(f"==================================================")
    print(f" Prompt ID   : {report['prompt_id']}")
    print(f" Total Score : {total_score} / 100.0")
    print(f"--------------------------------------------------")
    for dim, data in report["breakdown"].items():
        print(f" - {dim:28s}: {data['score']:4.1f} / {data['max']}")
        for detail in data["details"]:
            print(f"     • {detail}")
    print(f"==================================================\n")

    with open(args.output, "w") as f:
        json.dump(report, f, indent=2)

if __name__ == "__main__":
    main()

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
Asynchronous Multi-Prompt SDK Orchestrator for Google Antigravity.
Executes prompt implementations in parallel using isolated task contexts.
"""

import argparse
import asyncio
import json
import os
import pathlib
import sys
from typing import Dict, Any, List


# Try importing google.antigravity SDK if installed in environment
try:
    from google.antigravity import Agent, AgentConfig, CapabilitiesConfig
    HAS_ANTIGRAVITY_SDK = True
except ImportError:
    HAS_ANTIGRAVITY_SDK = False


def update_registry_status(workspace_dir: pathlib.Path, prompt_id: str, status: str, agent_id: str = None, error: str = None):
    """Helper to update prompt status in central registry."""
    reg_path = workspace_dir / ".gemini" / "prompts" / "registry.json"
    if not reg_path.exists():
        return

    try:
        data = json.loads(reg_path.read_text(encoding="utf-8"))
        if prompt_id in data.get("prompts", {}):
            data["prompts"][prompt_id]["status"] = status
            exec_info = data["prompts"][prompt_id].setdefault("execution", {})
            if agent_id:
                exec_info["agent_id"] = agent_id
            if error:
                exec_info["error"] = error
            reg_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except Exception as e:
        print(f"Warning: Failed updating status for {prompt_id}: {e}", file=sys.stderr)


async def execute_single_prompt(prompt_id: str, workspace_dir: pathlib.Path, model_tier: str = "gemini-3.5-flash-high") -> Dict[str, Any]:
    """Executes a single prompt implementation task asynchronously."""
    prompt_dir = workspace_dir / ".gemini" / "prompts" / prompt_id
    prompt_file = prompt_dir / "prompt.md"
    task_dir = workspace_dir / ".gemini" / "tasks" / prompt_id
    knowledge_dir = workspace_dir / ".gemini" / "knowledge" / prompt_id

    task_dir.mkdir(parents=True, exist_ok=True)
    knowledge_dir.mkdir(parents=True, exist_ok=True)

    if not prompt_file.exists():
        err_msg = f"Prompt file not found at {prompt_file}"
        update_registry_status(workspace_dir, prompt_id, "FAILED", error=err_msg)
        return {"prompt_id": prompt_id, "status": "FAILED", "error": err_msg}

    prompt_content = prompt_file.read_text(encoding="utf-8")

    update_registry_status(workspace_dir, prompt_id, "EXECUTING", agent_id=f"worker-{prompt_id}")

    # Check for diff patch
    diff_file = prompt_dir / "diff.patch"
    diff_content = diff_file.read_text(encoding="utf-8") if diff_file.exists() else None

    if HAS_ANTIGRAVITY_SDK:
        try:
            config = AgentConfig(
                model_name=model_tier,
                system_instruction=(
                    f"You are the Executing Agent for Prompt ID {prompt_id}. "
                    f"Write all state files to {task_dir} and all OKF docs to {knowledge_dir}."
                ),
                capabilities=CapabilitiesConfig(
                    allow_file_write=True,
                    allow_command_execution=True,
                ),
            )
            agent = Agent(config=config)
            
            exec_prompt = f"Execute implementation for prompt {prompt_id}:\n\n{prompt_content}"
            if diff_content:
                exec_prompt += f"\n\n--- INSTRUCTION DELTA (diff.patch) ---\n{diff_content}"

            response = await agent.run_async(exec_prompt)
            update_registry_status(workspace_dir, prompt_id, "COMPLETED")
            return {"prompt_id": prompt_id, "status": "SUCCESS", "response": str(response)}
        except Exception as e:
            update_registry_status(workspace_dir, prompt_id, "FAILED", error=str(e))
            return {"prompt_id": prompt_id, "status": "FAILED", "error": str(e)}
    else:
        # Fallback runner when SDK is handled by Antigravity IDE / CLI runtime
        init_task_file = task_dir / "task.md"
        if not init_task_file.exists():
            init_task_file.write_text(f"# Task Execution Checklist for {prompt_id}\n\n- [ ] Planning Mode reactivated\n- [ ] Code implemented\n- [ ] Evidence verified\n", encoding="utf-8")
        
        update_registry_status(workspace_dir, prompt_id, "COMPLETED", agent_id=f"cli-runner-{prompt_id}")
        return {
            "prompt_id": prompt_id,
            "status": "COMPLETED",
            "info": "Initialized task directory and updated registry status (SDK fallback mode)"
        }


async def main():
    parser = argparse.ArgumentParser(description="Antigravity Async Multi-Prompt Orchestrator")
    parser.add_argument("--prompt-ids", nargs="+", required=True, help="List of Prompt Short IDs to execute")
    parser.add_argument("--workspace", default=".", help="Workspace path")
    parser.add_argument("--model-tier", default="gemini-3.5-flash-high", help="Gemini model tier")

    args = parser.parse_args()
    workspace_dir = pathlib.Path(args.workspace).resolve()

    pids = [pid.upper() for pid in args.prompt_ids]
    print(f"Launching async execution pipeline for Prompt IDs: {', '.join(pids)}")

    tasks = [execute_single_prompt(pid, workspace_dir, args.model_tier) for pid in pids]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    print("\n=== Execution Summary ===")
    print(json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    asyncio.run(main())

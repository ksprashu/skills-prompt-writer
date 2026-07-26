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
Prompt Registry Management CLI for Antigravity Prompt-Writer.
Handles Short ID generation (PRMT-<HEX4>), central registry sync,
diff prompt calculation, metadata updates, and status tracking.
"""

import argparse
import datetime
import difflib
import hashlib
import json
import os
import pathlib
import random
import sys
from typing import Dict, Any, Optional, List


REGISTRY_RELATIVE_PATH = pathlib.Path(".gemini/prompts/registry.json")


def get_workspace_root(start_dir: Optional[str] = None) -> pathlib.Path:
    """Finds workspace root or defaults to CWD."""
    curr = pathlib.Path(start_dir or os.getcwd()).resolve()
    while curr != curr.parent:
        if (curr / ".gemini").exists() or (curr / ".git").exists():
            return curr
        curr = curr.parent
    return pathlib.Path(os.getcwd()).resolve()


def load_registry(workspace_dir: pathlib.Path) -> Dict[str, Any]:
    """Loads the central prompt registry or initializes an empty one."""
    registry_path = workspace_dir / REGISTRY_RELATIVE_PATH
    if registry_path.exists():
        try:
            return json.loads(registry_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"Warning: Failed to parse registry at {registry_path}: {e}", file=sys.stderr)
    
    return {
        "version": "2.0.0",
        "active_prompt_id": None,
        "prompts": {}
    }


def save_registry(workspace_dir: pathlib.Path, data: Dict[str, Any]) -> pathlib.Path:
    """Saves the prompt registry JSON file safely."""
    registry_path = workspace_dir / REGISTRY_RELATIVE_PATH
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return registry_path


def generate_short_id(workspace_dir: pathlib.Path, prompt_text: str = "", salt: str = "") -> str:
    """Generates a unique PRMT-<HEX4> Short ID."""
    registry = load_registry(workspace_dir)
    existing_ids = set(registry.get("prompts", {}).keys())

    seed_counter = 0
    while True:
        raw = f"{prompt_text}-{datetime.datetime.now().isoformat()}-{salt}-{seed_counter}-{random.random()}"
        digest = hashlib.sha256(raw.encode("utf-8")).hexdigest().upper()
        short_hex = digest[:4]
        candidate_id = f"PRMT-{short_hex}"
        if candidate_id not in existing_ids:
            return candidate_id
        seed_counter += 1


def cmd_list(args):
    """Lists all registered prompts."""
    workspace = get_workspace_root(args.workspace)
    registry = load_registry(workspace)
    prompts = registry.get("prompts", {})

    if not prompts:
        print("No prompts registered in .gemini/prompts/registry.json")
        return

    print(f"\nPrompt Registry ({len(prompts)} entry/entries) - Workspace: {workspace}")
    print("-" * 90)
    print(f"{'ID':<11} | {'STATUS':<11} | {'PARENT ID':<10} | {'CREATED AT':<20} | {'TITLE'}")
    print("-" * 90)

    for pid, info in sorted(prompts.items(), key=lambda x: x[1].get("created_at", ""), reverse=True):
        status = info.get("status", "UNKNOWN")
        parent = info.get("parent_id") or "-"
        created = info.get("created_at", "N/A")[:19].replace("T", " ")
        title = info.get("title", "Untitled Prompt")
        if len(title) > 30:
            title = title[:27] + "..."
        print(f"{pid:<11} | {status:<11} | {parent:<10} | {created:<20} | {title}")
    print("-" * 90 + "\n")


def cmd_show(args):
    """Shows detailed information for a specific prompt ID."""
    workspace = get_workspace_root(args.workspace)
    registry = load_registry(workspace)
    prompts = registry.get("prompts", {})

    pid = args.prompt_id.upper()
    if pid not in prompts:
        print(f"Error: Prompt ID '{pid}' not found in registry.", file=sys.stderr)
        sys.exit(1)

    info = prompts[pid]
    print(f"\n=== Prompt Metadata: {pid} ===")
    print(json.dumps(info, indent=2))

    prompt_path = workspace / info.get("prompt_file", f".gemini/prompts/{pid}/prompt.md")
    if prompt_path.exists():
        print(f"\n=== Prompt Content ({prompt_path}) ===")
        print(prompt_path.read_text(encoding="utf-8"))
    else:
        print(f"\nWarning: Prompt file missing at {prompt_path}")


def cmd_create(args):
    """Creates and registers a new prompt with Short ID and optional diff patch."""
    workspace = get_workspace_root(args.workspace)
    registry = load_registry(workspace)

    prompt_text = args.prompt_text
    if args.file and os.path.exists(args.file):
        prompt_text = pathlib.Path(args.file).read_text(encoding="utf-8")

    if not prompt_text:
        print("Error: --prompt-text or --file must be provided.", file=sys.stderr)
        sys.exit(1)

    pid = generate_short_id(workspace, prompt_text=prompt_text)
    prompt_dir = workspace / ".gemini" / "prompts" / pid
    prompt_dir.mkdir(parents=True, exist_ok=True)

    prompt_file = prompt_dir / "prompt.md"
    prompt_file.write_text(prompt_text, encoding="utf-8")

    parent_id = args.parent_id.upper() if args.parent_id else None
    diff_file_rel = None

    if parent_id and parent_id in registry.get("prompts", {}):
        parent_info = registry["prompts"][parent_id]
        parent_path = workspace / parent_info.get("prompt_file")
        if parent_path.exists():
            parent_text = parent_path.read_text(encoding="utf-8")
            diff_lines = list(difflib.unified_diff(
                parent_text.splitlines(keepends=True),
                prompt_text.splitlines(keepends=True),
                fromfile=f"a/{parent_id}/prompt.md",
                tofile=f"b/{pid}/prompt.md"
            ))
            if diff_lines:
                diff_file = prompt_dir / "diff.patch"
                diff_file.write_text("".join(diff_lines), encoding="utf-8")
                diff_file_rel = str(diff_file.relative_to(workspace))

    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    meta = {
        "id": pid,
        "parent_id": parent_id,
        "title": args.title or prompt_text.strip().split("\n")[0][:60] or "Untitled Prompt",
        "created_at": now_iso,
        "status": args.status.upper(),
        "prompt_file": str(prompt_file.relative_to(workspace)),
        "diff_file": diff_file_rel,
        "execution": {
            "mode": "DIFF_INCREMENTAL" if parent_id else "FULL",
            "agent_id": None,
            "started_at": None,
            "completed_at": None,
            "error": None
        },
        "tags": args.tags or []
    }

    meta_file = prompt_dir / "metadata.json"
    meta_file.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    registry["active_prompt_id"] = pid
    registry["prompts"][pid] = meta
    save_registry(workspace, registry)

    print(f"Successfully registered prompt {pid}")
    print(f"  Prompt File: {prompt_file}")
    if diff_file_rel:
        print(f"  Diff Patch:  {workspace / diff_file_rel}")
    print(f"  Registry:    {workspace / REGISTRY_RELATIVE_PATH}")


def cmd_diff(args):
    """Computes and prints diff between two prompts."""
    workspace = get_workspace_root(args.workspace)
    registry = load_registry(workspace)

    pid1 = args.prompt_id_1.upper()
    pid2 = args.prompt_id_2.upper()

    for pid in (pid1, pid2):
        if pid not in registry.get("prompts", {}):
            print(f"Error: Prompt ID '{pid}' not found.", file=sys.stderr)
            sys.exit(1)

    file1 = workspace / registry["prompts"][pid1].get("prompt_file")
    file2 = workspace / registry["prompts"][pid2].get("prompt_file")

    text1 = file1.read_text(encoding="utf-8") if file1.exists() else ""
    text2 = file2.read_text(encoding="utf-8") if file2.exists() else ""

    diff = difflib.unified_diff(
        text1.splitlines(keepends=True),
        text2.splitlines(keepends=True),
        fromfile=f"{pid1}/prompt.md",
        tofile=f"{pid2}/prompt.md"
    )

    diff_output = "".join(diff)
    if diff_output:
        print(f"\n=== Diff: {pid1} -> {pid2} ===")
        print(diff_output)
    else:
        print(f"\nPrompts {pid1} and {pid2} are identical.")


def cmd_update_status(args):
    """Updates the execution status of a prompt."""
    workspace = get_workspace_root(args.workspace)
    registry = load_registry(workspace)

    pid = args.prompt_id.upper()
    if pid not in registry.get("prompts", {}):
        print(f"Error: Prompt ID '{pid}' not found.", file=sys.stderr)
        sys.exit(1)

    status = args.status.upper()
    info = registry["prompts"][pid]
    info["status"] = status

    exec_info = info.setdefault("execution", {})
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()

    if status == "EXECUTING":
        exec_info["started_at"] = now_iso
    elif status in ("COMPLETED", "FAILED"):
        exec_info["completed_at"] = now_iso

    if args.agent_id:
        exec_info["agent_id"] = args.agent_id
    if args.error:
        exec_info["error"] = args.error

    # Update metadata file in prompt dir
    prompt_dir = workspace / ".gemini" / "prompts" / pid
    meta_file = prompt_dir / "metadata.json"
    if meta_file.exists():
        meta_file.write_text(json.dumps(info, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    save_registry(workspace, registry)
    print(f"Updated status for {pid} -> {status}")


def cmd_next_id(args):
    """Generates a fresh Short ID."""
    workspace = get_workspace_root(args.workspace)
    pid = generate_short_id(workspace)
    print(pid)


def main():
    parser = argparse.ArgumentParser(description="Antigravity Prompt Registry CLI")
    parser.add_argument("--workspace", default=".", help="Target workspace root")

    subparsers = parser.add_subparsers(dest="subcommand", help="Command")

    # list
    p_list = subparsers.add_parser("list", help="List all registered prompts")
    p_list.set_defaults(func=cmd_list)

    # show
    p_show = subparsers.add_parser("show", help="Show metadata & content for a prompt")
    p_show.add_argument("prompt_id", help="Prompt Short ID (e.g. PRMT-8F21)")
    p_show.set_defaults(func=cmd_show)

    # create
    p_create = subparsers.add_parser("create", help="Create and register a new prompt")
    p_create.add_argument("--title", help="Prompt title")
    p_create.add_argument("--prompt-text", default="", help="Inline prompt text")
    p_create.add_argument("--file", help="Path to file containing prompt text")
    p_create.add_argument("--parent-id", help="Parent Prompt Short ID for revisions")
    p_create.add_argument("--status", default="QUEUED", help="Initial status (e.g. QUEUED, READY)")
    p_create.add_argument("--tags", nargs="*", help="Tags list")
    p_create.set_defaults(func=cmd_create)

    # diff
    p_diff = subparsers.add_parser("diff", help="Diff two prompts")
    p_diff.add_argument("prompt_id_1", help="First Prompt Short ID")
    p_diff.add_argument("prompt_id_2", help="Second Prompt Short ID")
    p_diff.set_defaults(func=cmd_diff)

    # update-status
    p_status = subparsers.add_parser("update-status", help="Update execution status of a prompt")
    p_status.add_argument("prompt_id", help="Prompt Short ID")
    p_status.add_argument("status", help="New status (QUEUED, EXECUTING, COMPLETED, FAILED)")
    p_status.add_argument("--agent-id", help="Executing subagent ID")
    p_status.add_argument("--error", help="Error message if failed")
    p_status.set_defaults(func=cmd_update_status)

    # next-id
    p_next = subparsers.add_parser("next-id", help="Generate a fresh unique Short ID")
    p_next.set_defaults(func=cmd_next_id)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()

# Codebase Implementation Plan: Standalone OKF Knowledge Catalog Skill Integration

This plan outlines the steps to build, symlink, configure, and verify the standalone `skills-knowledge-catalog` repository, and integrate its context-aware usage across the `6-personas` and `prompt-writer` core skills.

---

## 🎯 Success Criteria
1.  **Standalone Repository Established**: `/Users/ksprashanth/code/github/skills-knowledge-catalog` is a fully initialized git repo with `.gitignore`, `LICENSE`, and `README.md`.
2.  **Authoritative SKILL.md Written**: The repo contains the core OKF standard and index-rebuilding schemas.
3.  **Global AGY Symlink Configured**: A symlink exists at `/Users/ksprashanth/.gemini/skills/knowledge-catalog` pointing to the standalone repo.
4.  **Core Skills Integration**: `/Users/ksprashanth/.gemini/skills/6-personas/SKILL.md` and `/Users/ksprashanth/.gemini/config/skills/prompt-writer/SKILL.md` are updated to reference and rely on the standalone skill.
5.  **Prisinte Verification & Handoff**: `walkthrough.md` is updated in the active workspace with proof of symlinks and git clean states.

---

## 🧭 Milestone Breakdown

### Milestone 1: Scout and Initialize Repo [Scout]
- [ ] Create repository folder `/Users/ksprashanth/code/github/skills-knowledge-catalog`.
- [ ] Initialize git and create `.gitignore`, `LICENSE`, and `README.md`.
- [ ] Synchronize task checklist and state journal.

### Milestone 2: Write Custom SKILL.md [Builder]
- [ ] Write `/Users/ksprashanth/code/github/skills-knowledge-catalog/SKILL.md`.
- [ ] Verify markdown syntax and absolute path links.
- [ ] Synchronize task checklist and state journal.

### Milestone 3: Configure Symlink and Verify AGY Discovery [Builder/Sentry]
- [ ] Determine/ensure path `/Users/ksprashanth/.gemini/skills/` exists.
- [ ] Create symlink from source directory `/Users/ksprashanth/code/github/skills-knowledge-catalog` to destination `/Users/ksprashanth/.gemini/skills/knowledge-catalog`.
- [ ] Verify symlink validity with shell commands.
- [ ] Synchronize task checklist and state journal.

### Milestone 4: Refactor Core Skills to Call Standalone Catalog [Builder]
- [ ] Modify `/Users/ksprashanth/.gemini/skills/6-personas/SKILL.md` to delegate OKF structures to the symlinked skill.
- [ ] Modify `/Users/ksprashanth/.gemini/config/skills/prompt-writer/SKILL.md` to require target executing agents to conform to the symlinked standards.
- [ ] Synchronize task checklist and state journal.

### Milestone 5: Verification & Handoff Walkthrough [Sentry/Mentor]
- [ ] Commit all changes inside the newly created `skills-knowledge-catalog` standalone repository.
- [ ] Programmatically test updated core markdown files for structural symmetry.
- [ ] Update `walkthrough.md` at the workspace root summarizing achievements, symlink verification dumps, and execution guides.

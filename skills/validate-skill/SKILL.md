---
name: validate-skill
description: Automates the structural, syntactic, and frontmatter verification of custom prompt-writer skills to ensure seamless integration and system recognition.
---

# Custom Validate-Skill Skill

This skill ensures that all custom skills and agent configurations maintain complete structural integrity, validating YAML frontmatters, required directories, and script references.

---

## 🧭 Skill File Structure Checklist

Standard custom skills must match the following layout constraints:
- Must have a `SKILL.md` file at the root.
- `SKILL.md` must start with a `---` YAML frontmatter separator.
- Frontmatter must define `name` (exactly matching folder name) and a short `description`.
- Supporting folders (such as `references/`, `examples/`, `scripts/`) must exist when needed.

---

## 🛠️ Validation Operations

Run the local validation script programmatically to verify skill structures:

```bash
# Execute local structural and frontmatter validations:
bash scripts/validate_skill.sh
```

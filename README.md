# Google Antigravity Custom Skill: Prompt-Writer

[![npx skills](https://img.shields.io/badge/skills.sh-installed-brightgreen)](https://skills.sh)

A custom, version-controlled skill for Google Antigravity that transforms basic, vague, or incomplete user prompts into highly-structured, technically precise, and optimized instruction sets designed specifically for Gemini models and Antigravity features.

---

## Features

-   **Interactive Grill & Propose Loop**: Analyzes basic prompts for omissions, formulates concrete technical and design recommendations, and guides the user through low-effort selection loops.
-   **Up-to-Date API Fetching (MCP)**: Explicitly instructs executing agents to utilize primary MCP documentation servers (`content7`, `developer-knowledge`) to pull live API specifications.
-   **Antigravity Architecture Integration**: Automatically structures rewritten prompts to leverage `/goal` directives, multi-agent parallel execution (`invoke_subagent`), and custom rules.
-   **Gemini Context Engineering**: Uses XML-style tagging structures to isolate contexts and optimize Gemini's instruction-following.

---

## Directory Structure

```
.
├── LICENSE                          # MIT License
├── README.md                        # Project documentation (this file)
├── requirements.md                  # original user requirements document
├── scripts/
│   └── validate_skill.sh            # Automated verification/linting script
└── skills/
    └── prompt-writer/
        ├── SKILL.md                 # Core custom skill definition & instructions
        ├── examples/
        │   └── example.md           # Before-and-After prompt rewriting showcase
        └── references/
            └── template.md          # Standard Antigravity prompt template
```

---

## Installation & Activation

### Recommended: Using `npx skills`
Install this skill into your agent environment using `npx skills`:

```bash
npx skills add ksprashu/skills-prompt-writer
```

### Alternative: Local Linking
To register this custom skill globally within your Antigravity desktop application or CLI:

1.  Open your terminal.
2.  Create a symlink from this repository's skill folder to your Global Customizations Root:
    ```bash
    ln -s "/Users/ksprashanth/code/github/skills-prompt-writer/skills/prompt-writer" "/Users/ksprashanth/.gemini/config/skills/prompt-writer"
    ```
3.  Restart or refresh your Antigravity conversation. The custom skill `prompt-writer` will be automatically discovered and loaded!

---

## Quality Assurance & Verification

To verify that the custom skill is fully intact, complies with YAML frontmatter guidelines, and matches all internal link structures, run the automated validation script:

```bash
bash scripts/validate_skill.sh
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

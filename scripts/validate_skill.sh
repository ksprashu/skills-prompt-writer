#!/usr/bin/env bash
# validate_skill.sh - Validates the prompt-writer skill integrity and structure.

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Antigravity Skill Validation ===${NC}"

SKILL_DIR="skills/prompt-writer"
SKILL_MD="$SKILL_DIR/SKILL.md"
TEMPLATE_MD="$SKILL_DIR/references/template.md"
EXAMPLE_MD="$SKILL_DIR/examples/example.md"

# 1. Check file existence
echo "Checking file paths..."
for file in "$SKILL_MD" "$TEMPLATE_MD" "$EXAMPLE_MD"; do
  if [[ -f "$file" ]]; then
    echo -e "  [${GREEN}OK${NC}] Found file: $file"
  else
    echo -e "  [${RED}FAIL${NC}] Missing file: $file"
    exit 1
  fi
done

# 2. Parse and validate YAML Frontmatter in SKILL.md
echo "Validating YAML Frontmatter in SKILL.md..."

# Check if file starts with ---
first_line=$(head -n 1 "$SKILL_MD")
if [[ "$first_line" != "---" ]]; then
  echo -e "  [${RED}FAIL${NC}] SKILL.md does not start with YAML delimiter '---'."
  exit 1
fi

# Extract frontmatter section
frontmatter=$(sed -ne '1,/---/p' "$SKILL_MD")

# Check name
if echo "$frontmatter" | grep -q "^name: \?prompt-writer$"; then
  echo -e "  [${GREEN}OK${NC}] Frontmatter contains correct 'name: prompt-writer'"
else
  echo -e "  [${RED}FAIL${NC}] Frontmatter missing or incorrect 'name' key. Must be exactly 'prompt-writer'."
  exit 1
fi

# Check description
if echo "$frontmatter" | grep -q "^description: \?."; then
  echo -e "  [${GREEN}OK${NC}] Frontmatter contains a 'description' key."
else
  echo -e "  [${RED}FAIL${NC}] Frontmatter missing 'description' key."
  exit 1
fi

echo -e "\n${GREEN}Success: Custom skill 'prompt-writer' is structurally and syntactically valid!${NC}"
exit 0

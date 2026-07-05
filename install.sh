#!/usr/bin/env bash
# install.sh - Automates the global registration of the prompt-writer skill.

set -euo pipefail

# ANSI color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}==============================================${NC}"
echo -e "${BLUE}   Antigravity Prompt-Writer Installer        ${NC}"
echo -e "${BLUE}==============================================${NC}\n"

# 1. Resolve absolute repository root directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_SOURCE_DIR="$SCRIPT_DIR/skills/prompt-writer"
GLOBAL_SKILLS_DIR="$HOME/.gemini/config/skills"
GLOBAL_SKILL_TARGET="$GLOBAL_SKILLS_DIR/prompt-writer"

echo -e "Detecting paths..."
echo -e "  Local Skill Source:  ${YELLOW}$SKILL_SOURCE_DIR${NC}"
echo -e "  Global Target Path:  ${YELLOW}$GLOBAL_SKILL_TARGET${NC}\n"

# Verify source directory exists
if [[ ! -d "$SKILL_SOURCE_DIR" ]]; then
  echo -e "  [${RED}ERROR${NC}] Local skill source directory not found: $SKILL_SOURCE_DIR"
  echo -e "  Make sure you are running this installer from the repository root."
  exit 1
fi

# 2. Ensure the global skills directory exists
if [[ ! -d "$GLOBAL_SKILLS_DIR" ]]; then
  echo -e "Global config folder missing. Creating directory: ${YELLOW}$GLOBAL_SKILLS_DIR${NC}"
  mkdir -p "$GLOBAL_SKILLS_DIR"
fi

# 3. Handle existing target
if [[ -L "$GLOBAL_SKILL_TARGET" ]]; then
  echo -e "Existing symlink detected. Re-linking..."
  rm "$GLOBAL_SKILL_TARGET"
elif [[ -d "$GLOBAL_SKILL_TARGET" ]]; then
  echo -e "  [${YELLOW}WARNING${NC}] Direct directory exists at target location. Backing it up to ${YELLOW}${GLOBAL_SKILL_TARGET}.bak${NC}..."
  mv "$GLOBAL_SKILL_TARGET" "${GLOBAL_SKILL_TARGET}.bak"
fi

# 4. Create symlink
echo -e "Creating symbolic link..."
ln -s "$SKILL_SOURCE_DIR" "$GLOBAL_SKILL_TARGET"
echo -e "  [${GREEN}OK${NC}] Symlink created successfully!\n"

# 5. Execute post-install validation
echo -e "Running post-installation validation checks..."
if bash "$SCRIPT_DIR/scripts/validate_skill.sh"; then
  echo -e "\n${GREEN}🎉 Installation and validation completed successfully!${NC}"
  echo -e "The ${BLUE}prompt-writer${NC} skill is now globally registered and ready to use."
else
  echo -e "\n${RED}⚠️ Installation succeeded, but post-installation validation failed.${NC}"
  echo -e "Please inspect the error logs above and check your skill files."
  exit 1
fi

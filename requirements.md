# Prompt Writer Skill Requirements

The user wants to create a new custom skill for Google Antigravity that rewrites user prompts/tasks. 

## Requirements Detail

1. **Prompt Rewriting**:
   - The user might provide basic, incomplete, or not fully thought-through prompts.
   - The skill must rewrite the prompt using the latest best practices for prompting Gemini models, maximizing instruction-following and comprehension.

2. **Antigravity Features & Capability Integration**:
   - The rewritten prompt must explicitly leverage available MCP servers and agent skills.
   - It should use the `antigravity-guide` skill to understand all capabilities in Antigravity.
   - It must explicitly rewrite the prompt to use the latest and greatest Antigravity features.
   - The rewritten prompt must break down the tasks, use parallelisation, use subagents (`invoke_subagent`), use hooks, and use other available capabilities, writing explicit instructions to use them.

3. **MCP Server Integration (Primary: `content7` & `developer-knowledge`)**:
   - These MCP servers provide the latest documentation for all APIs, libraries, frameworks, SDKs, or technical components.
   - Whenever any technical component is used, the rewritten prompt must understand and explain what is being built and make explicit references to use these MCP servers for documentation queries.

4. **Interactive Grill & Propose Loop (Pre-rewrite Phase)**:
   - Before rewriting, the skill must analyze the user prompt, identify gaps, vague parts, or open-ended questions, and ask follow-up questions.
   - It must run this as an interactive loop until fully satisfied with all the inputs.
   - It should propose answers/options/hints and recommendations to the user rather than just asking them to think from scratch (since basic prompts are vague). This is much more efficient.
   - To execute this interactive loop until completion, it should leverage `/goal` or the "goal" skill/command.

5. **Clear Completion & Goal Definition**:
   - The rewritten prompt must have clear exit/done criteria, validation, verification, and completion requirements.
   - All of this information must form a "goal" (integrating with the `/goal` concept).
   - Use AGY best practices to place this goal within the rewritten prompt.

6. **Gemini & Context Engineering Best Practices**:
   - Use best practices for Gemini models (such as XML tags for structural isolation, precise system instructions, role assignment, prompt formatting, clear output structures) to build out the final rewritten prompt.

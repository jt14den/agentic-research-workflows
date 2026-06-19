---
title: "Reference"
---

## Glossary

AGENTS.md
: A portable Living Spec file supported across multiple AI coding tools (Claude Code, Codex CLI, Cursor, and others). Use it when you want your spec to travel with the project regardless of which agent you run. See also: CLAUDE.md.

Agent
: An AI system capable of using tools (like reading files, running code, or searching the web) to complete autonomous tasks.

Agentic Research Workflows
: A way of working where AI agents help generate and modify research code while the researcher stays responsible for specifying intent, reviewing the output, and validating that it is correct.

Approval Gates
: Strategic points of friction in an agentic workflow (e.g., reviewing a diff before accepting, running tests before merging) designed to prevent approval fatigue and ensure human oversight.

Bootstrap Workflow
: An iterative process where an AI agent scans a researcher's raw data and goals to draft the initial `CLAUDE.md` spec, which the researcher then reviews and approves.

Chain of Thought
: A prompting technique that encourages the AI to explain its reasoning step-by-step. Reasoning models (like o1 or R1) have this capability built-in.

CLEAR Framework
: A prompt engineering model (Concise, Logical, Explicit, Adaptive, Reflective) developed by Leo Lo to optimise AI interactions.

CLI (Command Line Interface)
: A text-based interface for interacting with your computer's operating system. Essential for giving AI agents direct access to the file system.

CO-STAR Framework
: A prompt engineering framework (Context, Objective, Style, Tone, Audience, Response) emphasizing the importance of persona and audience.

Context Poisoning
: A failure mode where irrelevant, stale, or contradictory information within a long context window (e.g., an `/archive` folder) causes the AI to hallucinate or generate incorrect code.

Declarative Programming (with AI)
: A focus on describing the *desired outcome* (what the data should look like) and letting an agent draft the *mechanical steps* (how to write the loop), which you then read and verify rather than accept blindly.

Determinism Collapse
: The risk that small variations in prompts or silent updates to AI model weights will result in different code outputs for the same task, threatening research reproducibility.

Evidence Mantra ("No Evidence, No Merge")
: The principle that a researcher should never approve an AI-generated change without supporting evidence (passing tests, invariant reports, or a readable diff).

External Brain
: The practice of storing a project's persistent memory in plain markdown files (such as `CLAUDE.md`, `PLAN.md`, and a running notes log) that an AI agent reads and updates, rather than relying on the model's limited, disposable context. The framing was popularized by Andrej Karpathy. In research it doubles as provenance.

Few-shot Prompting
: Providing examples in the prompt to guide the AI's output.

CLAUDE.md (Living Spec)
: A project-level Markdown file that Claude Code loads automatically at the start of every session. It defines the project's goals, rules, constraints, and context, acting as the persistent source of truth that keeps the agent on track across sessions. The Claude Code native equivalent of the portable AGENTS.md.

Hallucination
: When an AI generates factually incorrect or nonsensical information confidently.

Immutable Requirements
: Human-authored domain rules and constraints (e.g., "dates must be chronological") that act as the "Ground Truth" and cannot be modified by the AI agent.

LLM (Large Language Model)
: A deep learning model trained on vast amounts of text data to generate human-like text (e.g., Claude Sonnet/Opus, GPT-4o, Gemini).

MCP (Model Context Protocol)
: An open standard that lets AI agents call external tools (file systems, databases, APIs, services like Zotero) in a consistent way. When you install a tool like `zotero-mcp`, you are giving the agent a structured interface to that tool via MCP. You configure it once; the agent handles the rest.

Metamorphic Testing
: A validation strategy that checks the *relationships* between inputs and outputs (e.g., "If I double the input, does the output also double?") rather than checking for a single fixed value.

Natural Language Orchestration
: Using natural language to guide an AI agent in performing complex, multi-step tasks across multiple files in a project.

Provenance Tracking
: The practice of documenting the metadata of an AI interaction (model version, prompt, context hashes) to ensure research accountability.

Reasoning Models
: A new class of AI models (e.g., o1, DeepSeek-R1) trained to perform complex logical reasoning and verification before producing an output.

Silent Semantic Drift
: A failure mode where an AI's code runs and passes basic tests but quietly changes the underlying research assumptions or data meanings.

Spec-Driven Research Orchestration
: The practice of using AI agents to coordinate research tasks against a persistent, human-validated specification (`CLAUDE.md`). This replaces the "vibe-based" approach with a disciplined, auditable workflow.

Synthetic Data
: Artificially generated data used for testing validation pipelines without risking sensitive real-world data.

Vibe Coding
: The early (2023-2024) term for using AI intuition and natural-language prompts to handle the "grunt work" of coding. In research, this has evolved into the more rigorous **Spec-Driven Research Orchestration**.

## References

1. Lo, L. S. (2023). The CLEAR path: A framework for enhancing information literacy through prompt engineering. *The Journal of Academic Librarianship*, 49(4), 102720. [https://doi.org/10.1016/j.acalib.2023.102720](https://doi.org/10.1016/j.acalib.2023.102720)
2. Teo, S. (2023). *How I Won Singapore’s GPT-4 Prompt Engineering Competition*. Towards Data Science. [https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41)
3. Smaniotto, B. & van Nuenen, T. (2024). Vibe Coding for Research: AI-Assisted Programming with Validation Best Practices. UC Berkeley D-Lab. [https://github.com/dlab-berkeley/Vibe-Coding-for-Research](https://github.com/dlab-berkeley/Vibe-Coding-for-Research)
4. Claude Code Documentation: [https://docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code)

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

Backend
: The specific model and hosting arrangement an agent sends your data to (a vendor's cloud API, an institutionally approved endpoint, or a local model), as distinct from the tool you type into.

Bootstrap Workflow
: An iterative process where an AI agent scans a researcher's raw data and goals to draft the initial `CLAUDE.md` spec, which the researcher then reviews and approves.

Chain of Thought
: A prompting technique that encourages the AI to explain its reasoning step-by-step. Current frontier models build this in as an adjustable reasoning-effort or thinking setting on the same model, rather than requiring a separate "reasoning model." A displayed chain of thought is not necessarily a faithful record of the model's internal computation.

CLEAR Framework
: A prompt engineering model (Concise, Logical, Explicit, Adaptive, Reflective) developed by Leo Lo to optimise AI interactions.

CLI (Command Line Interface)
: A text-based interface for interacting with your computer's operating system. Essential for giving AI agents direct access to the file system.

CO-STAR Framework
: A prompt engineering framework (Context, Objective, Style, Tone, Audience, Response) emphasizing the importance of persona and audience.

Closed-weight Models
: Models whose weights are not published (e.g., Claude, GPT, Gemini), sometimes called proprietary models. You cannot verify their training data, and providers may update them silently, which can affect reproducibility. Institutional agreements may cover data privacy but do not solve this. See also: Open-weight Models.

Context Poisoning
: A failure mode where irrelevant, stale, or contradictory information within a long context window (e.g., an `/archive` folder) causes the AI to hallucinate or generate incorrect code.

Context Window
: The total amount of text an agent can hold in view at once during a session: your prompts, the files it has read, and its own output. When it fills up, earlier instructions can be lost. See also: Token.

Intent Specification
: A focus on describing the *desired outcome* (what the data should look like) and letting an agent draft the *mechanical steps* (how to write the loop), which you then read and verify rather than accept blindly. Not "declarative programming": the agent still writes an ordinary imperative implementation, and the spec itself is not executable.

Determinism Collapse
: The risk that small variations in prompts or silent updates to AI model weights will result in different code outputs for the same task, threatening research reproducibility.

Deterministic Check
: An executable test that returns the same pass/fail answer every time it runs on the same input, unlike asking a model whether code looks correct.

Domain Plausibility
: A check on whether a result is credible given what you actually know about the subject matter (for example, whether weekly sampling should produce evenly spaced points), as distinct from checking that the code ran without error.

Etherpad
: The shared, browser-based collaborative notes document used during a live workshop for posting answers, questions, and feedback. Self-directed learners can substitute a personal notes file.

Evidence Mantra ("No Evidence, No Merge")
: The principle that a researcher should never approve an AI-generated change without supporting evidence (passing tests, invariant reports, or a readable diff).

External Brain
: The practice of storing a project's persistent memory in plain markdown files (such as `CLAUDE.md`, `PLAN.md`, and a running notes log) that an AI agent reads and updates, rather than relying on the model's limited, disposable context. The framing was popularized by Andrej Karpathy. In research it doubles as provenance.

Few-shot Prompting
: Providing examples in the prompt to guide the AI's output.

Frontier Model
: The most capable commercially released models at a given moment (currently the top Claude, GPT, and Gemini tiers). The term is time-relative; what counts as frontier changes every few months.

CLAUDE.md (Living Spec)
: A project-level Markdown file that Claude Code loads automatically at the start of every session. It defines the project's goals, rules, constraints, and context, acting as the persistent source of truth that keeps the agent on track across sessions. The Claude Code native equivalent of the portable AGENTS.md.

Hallucination
: When an AI generates factually incorrect or nonsensical information confidently.

Immutable Requirements
: Human-authored domain rules and constraints (e.g., "dates must be chronological") that act as the "Ground Truth" and cannot be modified by the AI agent.

Imputation / Impute
: Filling in a missing value with an estimate (a group mean, a model prediction) instead of dropping the row that contains it. Which estimate to use is a research decision, not a technical default.

Invariant (Check)
: A property of your data that must hold true no matter how the pipeline is run (e.g., a fixed row count), expressed as a check that fails loudly when it stops holding. See also: Metamorphic Testing.

LLM (Large Language Model)
: A deep learning model trained on vast amounts of text data to generate human-like text (e.g., Claude, GPT, Gemini). Check `/status` in Claude Code for the exact current model in use; specific model names in this lesson go stale within months.

MCP (Model Context Protocol)
: An open standard that lets AI agents call external tools (file systems, databases, APIs, services like Zotero) in a consistent way. When you install a tool like `zotero-mcp`, you are giving the agent a structured interface to that tool via MCP. You configure it once; the agent handles the rest.

MCP Server
: A single connector that exposes one tool or data source (a database, a filesystem, Zotero) to an agent over MCP. See also: MCP (Model Context Protocol).

Metamorphic Testing
: A validation strategy that checks the *relationships* between inputs and outputs (e.g., "If I double the input, does the output also double?") rather than checking for a single fixed value.

Natural Language Orchestration
: Using natural language to guide an AI agent in performing complex, multi-step tasks across multiple files in a project.

Open-weight Models
: Models whose weights are downloadable and can be run locally (e.g., Qwen3, Gemma, OpenAI's gpt-oss), often via tools like Ollama. "Open-weight" is the precise term: downloadable weights alone don't make a model open source under the fuller definition (training data, code, and license may still be closed or restricted). Offer better reproducibility since you can pin a specific, frozen revision, but license terms still vary by model. See also: Closed-weight Models.

Plan Mode
: A Claude Code session mode in which the agent can read files and propose an approach but is blocked by the tool itself from writing files or running mutating commands until you approve the plan.

Prompt Injection
: An attack where instructions hidden in content an agent processes (a file, a web page, an MCP tool's returned data) get executed as if you had typed them yourself. A risk whenever an agent reads untrusted input, not just when it calls external tools, though MCP tool descriptions and returned data are a common vector.

Provenance Tracking
: The practice of documenting the metadata of an AI interaction (model version, prompt, context hashes) to ensure research accountability.

Reasoning Effort
: An adjustable setting (in Claude Code, `low` through `xhigh`, with `max` on some models) that controls how much a model reasons before responding, on the same model rather than a separate "reasoning model" line. Higher effort costs more time and tokens and does not guarantee a better answer.

Review-ready Bundle
: The complete set of artifacts that makes an AI-assisted result auditable by someone else: spec, plan, code, validation script, result, provenance note, and approval decision.

Sandboxing
: Running an agent or an MCP server with deliberately restricted filesystem and network access, so a compromised tool cannot reach data outside a defined boundary.

Schema
: The agreed set of column names, types, and formats a cleaned dataset must conform to, defined in advance and used as the target for any AI-generated cleaning code.

Silent Semantic Drift
: A failure mode where an AI's code runs and passes basic tests but quietly changes the underlying research assumptions or data meanings.

Slash Command
: A command typed inside a running Claude Code session (beginning with `/`, such as `/init`, `/model`, `/status`, or `/clear`) that controls the agent or session itself rather than being sent to the model as a prompt.

Spec-Driven Research Orchestration
: The practice of using AI agents to coordinate research tasks against a persistent, human-validated specification (`CLAUDE.md`). This replaces the "vibe-based" approach with a disciplined, auditable workflow.

Synthetic Data
: Artificially generated data used for testing validation pipelines without risking sensitive real-world data.

Token
: The unit an LLM processes text in, roughly a word-fragment. Context window sizes and usage are measured in tokens, not words or lines. See also: Context Window.

Verification Load
: The work of checking that an agent's actions actually match your specification and your data, which grows as the agent produces more code faster than you can read it.

Vibe Coding
: The early (2023-2024) term for using AI intuition and natural-language prompts to handle the "grunt work" of coding. In research, this has evolved into the more rigorous **Spec-Driven Research Orchestration**.

## References

1. Lo, L. S. (2023). The CLEAR path: A framework for enhancing information literacy through prompt engineering. *The Journal of Academic Librarianship*, 49(4), 102720. [https://doi.org/10.1016/j.acalib.2023.102720](https://doi.org/10.1016/j.acalib.2023.102720)
2. Teo, S. (2023). *How I Won Singapore’s GPT-4 Prompt Engineering Competition*. Towards Data Science. [https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41)
3. Smaniotto, B. & van Nuenen, T. (2024). Vibe Coding for Research: AI-Assisted Programming with Validation Best Practices. UC Berkeley D-Lab. [https://github.com/dlab-berkeley/Vibe-Coding-for-Research](https://github.com/dlab-berkeley/Vibe-Coding-for-Research)
4. Claude Code Documentation: [https://docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code)
5. O'Brien, G., Parker, A., Eisty, N., & Carver, J. (2025). *A survey of generative AI adoption and perceived productivity among scientists who program*. [https://arxiv.org/abs/2512.19644](https://arxiv.org/abs/2512.19644)
6. Churilov, A. (2026). *The Range Shrinks, the Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026 Frontier-Model Cohort*. [https://arxiv.org/abs/2605.17062](https://arxiv.org/abs/2605.17062)

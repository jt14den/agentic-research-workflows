---
title: "Instructor Notes"
---

## Teaching Philosophy: The Researcher Stays the Active Reviewer

This lesson helps researchers work with AI coding agents without handing off the thinking. The shift is from writing every line of syntax towards reading, questioning, and validating code the agent produced. Resist framing this as "the AI does the work and you orchestrate", the episodes deliberately push back on that. The core challenge for learners isn't syntax; it's managing **cognitive load** and staying the **active reviewer** who can explain and judge the result.

### Key Concepts to Emphasize:
- **Verification Load:** It is often harder to *verify* code you didn't write than to write it yourself. Normalise this "friction" as a sign of high-quality research.
- **Evidence Mantra:** "I do not approve changes; I approve evidence." This should be the recurring theme of the workshop.
- **Sandboxing:** Always emphasize the security implications of giving an AI direct access to the filesystem.

---

## Episode: Before We Use AI (opening)
- **Purpose:** Reset expectations before anyone opens a terminal. Some learners arrive expecting a speed demo; this episode says plainly that the workshop measures whether they can *explain and validate* AI output.
- **Set the norm:** Make it safe to say "I don't understand this line." Treat confusing AI output as a shared teaching artefact, not a personal failure.
- **The run / revise / reject checkpoint** introduced here is reused in every later episode. Refer back to it by name.
- **Sticky-note opener:** Collect what learners want from AI and what they fear it will get wrong. Revisit at the end.

## Episode 1: Understanding CLI-Based AI
- **Auth Check:** Ask learners to run `claude --version`. If it returns a version number they are ready. If not, have them launch `claude` once and complete sign-in before continuing.
- **Model Check:** Have all learners set the same model with `/model` (e.g., `claude-sonnet-4-6`) before starting, so outputs are comparable and provenance records are meaningful.
- **Starter folder:** No pre-built repo is required. Learners create an empty `agentic-research-project` folder in setup, and the practice data is generated in Episode 3 (`make_messy_data.py`). If you prefer a real dataset over synthetic data, a ready-made one ships at `learners/files/coastal-water-quality/` (three inconsistent site CSVs with the same kinds of issues); point learners at it instead of generating data.
- **The Browser vs. CLI distinction:** Use the analogy of a "consultant" (Browser) vs. a "research assistant with keys to the lab" (CLI).
- **Discussion:** The prompt about "ChatGPT writing code that looks correct but fails" is a great way to bond over shared frustration and set the stage for why we need the CLI (to run and test immediately).

## Episode 2: Best Practices for Prompting
- **CO-STAR vs. CLEAR:** Don't get bogged down in the acronyms. The goal is *intentionality*.
- **Live Demo Tip:** Show a "Bad Prompt" vs. a "Good Prompt" live. Purposely run a vague command and show how it fails or produces messy output before using the refined version.
- **Self-Correction:** This is the "lightbulb" moment. Demonstrate asking the AI, "Are you sure? Review your code for edge cases."

## Episode 3: Data Cleaning (Live Demo)
- **High Intensity:** This is the most technically demanding episode. 
- **The "Safety Net":** If a learner's AI fails to generate working code after two attempts, have them copy the pre-written script from `instructors/files/backup_clean_and_merge.py`. This prevents them from falling behind.
- **Stop and Read:** Literally tell the class to "hands off keyboards" for two minutes to read the generated script before they run it.

## Episode 4: Validation Best Practices
- **Four-Layer Validation Stack** (match the episode exactly):
    1. Requirement constraints / No-Go Zones (human-authored ground truth in `CLAUDE.md`)
    2. Automated unit tests (written and approved before the implementation)
    3. Metamorphic and invariant checks (relationships that must not change)
    4. Domain plausibility (where the researcher's expertise is irreplaceable; do not omit this layer)
- **Activity:** Encourage learners to try the "Metamorphic Sanity Check" (Challenge). It's a powerful way to show how "reproducibility" can be subtly broken by AI randomness.

## Episode 5: Limitations and Cautions
- **Silent Semantic Drift:** This is the most "dangerous" failure. Use the example of a filtering threshold (e.g., `> 0.5` vs. `>= 0.5`) that might not crash the code but changes the science.
- **Environmental Cost:** This is often a new topic for researchers. It grounds the "Spec-Driven Research Orchestration" hype in physical reality.

## Episode 6: Resources and Next Steps
- **The Toolscape:** Acknowledge that tools (Aider, Cursor, Claude Code) change weekly. Focus on the *principles* (CLI, validation, provenance) rather than specific software.
- **Attribution:** Remind learners that while AI can't be an author, transparency about its use is a core tenet of Open Science.

---

## Troubleshooting & Common Issues

### API Quotas & Limits
If learners hit "Resource Exhausted" errors, it's likely they've exceeded their free tier quota or are prompting too rapidly. Suggest they wait 60 seconds or use a smaller "context" (don't send every file in the folder).

### "claude: command not found"
Ensure the global npm install (`npm install -g @anthropic-ai/claude-code`) worked and that their `PATH` is updated. In Docker, this is handled automatically. On host machines, they might need to restart their terminal.

### Hallucinations
If a learner gets a script that imports a non-existent library (e.g., `import science_cleaner`), use it as a "teachable moment" for the whole class about verification.

---

## Maintainer checklist

Run through this before teaching a pilot or merging substantial changes. It encodes the Carpentries guidance on teaching with generative AI.

### Cognitive load
- [ ] No exercise depends on syntax, libraries, or abstractions the lesson has not introduced.
- [ ] Where generated code is likely to over-reach (lambdas, regex, extra files), there is an instructor note flagging it.
- [ ] Small, interpretable tasks come before larger agentic workflows.

### Learner agency
- [ ] No exercise can be completed by pasting the task into an AI and copying the answer.
- [ ] Every challenge requires at least one of: explain, predict, trace, modify-and-justify, or validate.
- [ ] Language frames the learner as the active reviewer and final judge, not a passive orchestrator.

### Feedback loop
- [ ] Each episode has at least one pause-and-report checkpoint (sticky note / Etherpad / think-aloud).
- [ ] Checkpoints surface where learners are confused, not only whether code ran.

### Validation and reproducibility
- [ ] Exercises validate with concrete checks (counts, invariants, tests), not "it ran."
- [ ] Provenance (model, date, prompt) is recorded for generated code.
- [ ] Rewrite time is framed as a formative signal, never as proof AI is faster.

### Privacy and security
- [ ] Sensitive-data and security-critical tasks are explicitly flagged as out of scope for AI.
- [ ] Institutional vs personal account privacy differences are stated where relevant.

---

## Keeping the lesson current

The AI tool landscape moves faster than a Carpentries release cycle. The most volatile parts of this lesson are the **tool landscape** and **reputable sources** in Episode 6, the **failure modes** in Episode 5, and any **named model or CLI command** in Episodes 1-4.

Before each teaching, refresh these by running the `last30days` skill (see `~/projects/last30days-skill`):

```bash
python3 scripts/last30days.py "vibe coding" --include-web --emit=md --store --save-dir research
python3 scripts/last30days.py "AI coding agents" --include-web --emit=md --save-dir research
```

Use the output two ways: confirm the tool names and claims in Episodes 5-6 are still accurate, and pull one *current* hype example to debunk live in the Episode 6 "Identifying hype" discussion. A fresh example beats a canned one.

### Tooling status (last checked 2026-06-19)

- **The lesson now uses Claude Code (Anthropic).** Learners run it on one of two backends: a personal Pro/Max plan or API key for non-sensitive (P1-P3) work, or **UCLA Amazon Bedrock** (Anthropic models) for sensitive (P3/P4) research data. The same commands work on both; only the backend changes. Confirm Bedrock access and data-tier approval with the learner's unit before using real sensitive data. See `learners/setup.md`.
- **Historical note (why we migrated):** Google retired the free/consumer Gemini CLI on June 18, 2026 (folded into the paid Antigravity platform), which broke the lesson's original tooling. Paid Gemini Code Assist Standard/Enterprise and API-key access continued, but the free `gemini` command did not.
- As of June 2026, the most common research-capable CLI agents are Claude Code (Anthropic), Codex CLI (OpenAI), Antigravity CLI (Google), Cursor Agent, and open-source OpenCode/Aider. The lesson's principles (Living Spec, plan-first, validation stack, provenance) transfer across all of them, see the `agentic-research/cli-agent-landscape` wiki note.

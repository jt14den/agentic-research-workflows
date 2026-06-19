---
title: "Instructor Notes"
---

## Teaching Philosophy: The Researcher Stays the Active Reviewer

This lesson helps researchers work with AI coding agents without handing off the thinking. The shift is from writing every line of syntax towards reading, questioning, and validating code the agent produced. Resist framing this as "the AI does the work and you orchestrate", the episodes deliberately push back on that. The core challenge for learners isn't syntax; it's managing **cognitive load** and staying the **active reviewer** who can explain and judge the result.

### Key Concepts to Emphasize:
- **Verification Load:** It is often harder to *verify* code you didn't write than to write it yourself. Normalise this "friction" as a sign of high-quality research.
- **Evidence Mantra:** "I do not approve changes; I approve evidence." This should be the recurring theme of the workshop.
- **Sandboxing:** Always emphasize the security implications of giving an AI direct access to the filesystem.

### The worked example (one project all the way through)
The whole lesson uses one fixture, `learners/files/coastal-water-quality/` (three messy site CSVs). Learners carry it from spec to clean merge to validation to a trend plot in the capstone. Two anchors to keep in mind:
- **Expected result:** a merged `data/master_dataset.csv` with **60 rows** (3 sites x 20 weekly samples), all dates in 2023.
- **The planted trap (the lesson's climax):** site C dates are day-month-year (`05-01-2023` is 5 January). If parsed as month-day, January samples land in May. The script still runs, the row count is still 60, and the trend plot is still wrong. This is the concrete "working code is not trustworthy code" moment; let it happen and use it.

---

## Episode: Before We Use AI (opening)
- **Purpose:** Reset expectations before anyone opens a terminal. Some learners arrive expecting a speed demo; this episode says plainly that the workshop measures whether they can *explain and validate* AI output.
- **Set the norm:** Make it safe to say "I don't understand this line." Treat confusing AI output as a shared teaching artefact, not a personal failure.
- **The run / revise / reject checkpoint** introduced here is reused in every later episode. Refer back to it by name.
- **Sticky-note opener:** Collect what learners want from AI and what they fear it will get wrong. Revisit at the end.

## Episode 1: Understanding CLI-Based AI
- **Auth Check:** Ask learners to run `claude --version`. If it returns a version number they are ready. If not, have them launch `claude` once and complete sign-in before continuing.
- **Model Check:** Have all learners set the same model with `/model` (e.g., `claude-sonnet-4-6`) before starting, so outputs are comparable and provenance records are meaningful.
- **Starter folder:** Everyone works in the provided `coastal-water-quality` folder (ships at `learners/files/coastal-water-quality/`). Confirm learners have it and can `ls data/` to see the three site CSVs before starting. Episode 1 has them inspect a real file and compare the agent's description to it, the first hands-on win.
- **The Browser vs. CLI distinction:** Use the analogy of a "consultant" (Browser) vs. a "research assistant with keys to the lab" (CLI).
- **Discussion:** The prompt about "ChatGPT writing code that looks correct but fails" is a great way to bond over shared frustration and set the stage for why we need the CLI (to run and test immediately).

## Episode 2: Best Practices for Prompting
- **CO-STAR vs. CLEAR:** Don't get bogged down in the acronyms. The goal is *intentionality*.
- **Live Demo Tip:** Show a "Bad Prompt" vs. a "Good Prompt" live. Purposely run a vague command and show how it fails or produces messy output before using the refined version.
- **Self-Correction:** This is the "lightbulb" moment. Demonstrate asking the AI, "Are you sure? Review your code for edge cases."

## Episode 3: Data Cleaning (Live Demo)
- **High Intensity:** This is the most technically demanding episode.
- **Expected output:** `data/master_dataset.csv` with 60 rows. The "Update the script" challenge (exclude January) should remove 12 rows, leaving 48; a different number usually means the site C date format was misparsed.
- **The "Safety Net":** If a learner's AI fails to produce working code after two attempts, have them copy `instructors/files/backup_clean_and_merge.py` (it is written for this fixture and parses site C dates correctly). This keeps them on pace for the validate-and-judge steps, which are the point.
- **Stop and Read:** Literally tell the class to "hands off keyboards" for two minutes to read the generated script before they run it.

## Episode 4: Validation Best Practices
- **Four-Layer Validation Stack** (match the episode exactly):
    1. Requirement constraints / No-Go Zones (human-authored ground truth in `CLAUDE.md`)
    2. Executable checks you can run (finish the shipped `validate_data.py`)
    3. Metamorphic and invariant checks (60-row invariant; mean unchanged when rows are shuffled)
    4. Domain plausibility (where the researcher's expertise is irreplaceable; do not omit this layer)
- **Build the validator:** the core activity. Learners finish the three TODO checks in `validate_data.py`, then deliberately misparse the site C dates and confirm the validator now fails. A validator that cannot fail on a known-bad input is not protecting them.

## Episode 5: Limitations and Cautions
- **Silent Semantic Drift:** This is the most "dangerous" failure. The site C date trap from the worked example is the live version of this; refer back to it.
- **Environmental Cost:** This is often a new topic for researchers. It grounds the workflow in physical reality.

## Episode 6: From AI Output to Research-Ready Code (capstone)
- **Mostly doing:** budget the time for work, not exposition. Learners assemble the full bundle (spec, plan, code, validator, plot, provenance, approval decision) on the coastal data.
- **Expect the date trap to surface** for several learners during the plot step; that is the highlight. Collect a few approval decisions and read them aloud, especially the honest "revise" answers.
- **Fallbacks:** `backup_clean_and_merge.py` and `backup_plot_trend.py` let a stuck group still reach the validate-and-judge steps.

## Episode 7: Resources and Next Steps
- **The Toolscape:** Acknowledge that tools (Aider, Cursor, Claude Code) change weekly. Focus on the *principles* (CLI, validation, provenance) rather than specific software.
- **Monday workflow card:** the takeaway exercise; push learners to name the one check that would catch a silent error in their own data.
- **Attribution:** Remind learners that while AI can't be an author, transparency about its use is a core tenet of Open Science.

---

## Suggested first-pilot path (compressed)

For a first pilot, do not teach every section evenly. Protect the practical spine and let the rest be optional. The pilot should answer one question: **can learners use Claude Code to clean a small messy dataset, explain what changed, validate it with checks, and decide whether to approve the result?**

**Teach live:** Before We Use AI (briefly); CLI setup, the early data inspection, and `/init`; the Living Spec; Data Cleaning with AI; the `validate_data.py` approval gate; the capstone bundle.

**Make optional / skim if short on time:** CO-STAR and reasoning-model detail; the advanced tool landscape, MCP, and local-model material in Resources; multi-model verification.

If you run short, cut whole objectives (and their assessments), not bits from everywhere. The data-cleaning-to-validation-to-capstone arc is the part that must survive.

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

The AI tool landscape moves faster than a Carpentries release cycle. The most volatile parts of this lesson are the **tool landscape** and **reputable sources** in Episode 7, the **failure modes** in Episode 5, and any **named model or CLI command** in Episodes 1-4.

Before each teaching, refresh these by running the `last30days` skill (see `~/projects/last30days-skill`):

```bash
python3 scripts/last30days.py "vibe coding" --include-web --emit=md --store --save-dir research
python3 scripts/last30days.py "AI coding agents" --include-web --emit=md --save-dir research
```

Use the output two ways: confirm the tool names and claims in Episodes 5 and 7 are still accurate, and pull one *current* hype example to debunk live in the Episode 7 "Spotting hype" section. A fresh example beats a canned one.

### Tooling status (last checked 2026-06-19)

- **The lesson now uses Claude Code (Anthropic).** Learners run it on one of two backends: a personal Pro/Max plan or API key for non-sensitive (P1-P3) work, or **UCLA Amazon Bedrock** (Anthropic models) for sensitive (P3/P4) research data. The same commands work on both; only the backend changes. Confirm Bedrock access and data-tier approval with the learner's unit before using real sensitive data. See `learners/setup.md`.
- **Historical note (why we migrated):** Google retired the free/consumer Gemini CLI on June 18, 2026 (folded into the paid Antigravity platform), which broke the lesson's original tooling. Paid Gemini Code Assist Standard/Enterprise and API-key access continued, but the free `gemini` command did not.
- As of June 2026, the most common research-capable CLI agents are Claude Code (Anthropic), Codex CLI (OpenAI), Antigravity CLI (Google), Cursor Agent, and open-source OpenCode/Aider. The lesson's principles (Living Spec, plan-first, validation stack, provenance) transfer across all of them, see the `agentic-research/cli-agent-landscape` wiki note.

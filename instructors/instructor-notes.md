---
title: "Instructor Notes"
---

## Teaching approach: the researcher stays the active reviewer

This lesson helps researchers work with AI coding agents without handing off the thinking. The shift is from writing every line toward reading, questioning and checking code the agent produced. The episodes push back on the idea that "the AI does the work and you orchestrate." The core challenge for learners is not syntax. It is managing cognitive load and staying the reviewer who can explain and judge the result.

The lesson teaches three ways of working with AI, on one dataset:

1. Ask AI to help you understand. Predict first, then ask for an explanation or hint, then compare it with the data.
2. Delegate one small change. Introduce each practice when the task creates a need for it: state the expected result, review the plan, inspect the action, read the diff, compare the output with an independent expectation.
3. Test and hand off a result. Complete one check, show that it fails on bad data, and have another pair rerun the work without AI.

### Key ideas to emphasise

- Reviewing unfamiliar generated code can add cognitive load, especially when it brings in concepts a learner does not know. Treat that friction as normal.
- Permission to run an action is separate from approval of its result. Evidence supports approval.
- A check earns trust when it fails on a known-bad input.
- Access limits are enforced by tool permissions and isolation. A line in a Markdown file is a request.

### The worked example

The whole lesson uses one synthetic fixture, `learners/files/coastal-water-quality/`: three messy site CSVs. The data describe no real study. Learners carry it from a plan to a clean merge, to checks, to a trend plot in the capstone.

- Expected result: `data/master_dataset.csv` with 60 rows (3 sites x 20 weekly samples), all dates in 2023. Missing scores are filled with the median of that site's observed scores: A004 = 72.0, B-006 = 71.5, SC002 = 71.6. This is the exercise's fixed choice and not a recommendation for real studies.
- The planted trap: site C dates are day-month-year (`05-01-2023` is 5 January). A bare `pd.to_datetime()` with no format raises an error on this file, which is a loud and acceptable failure. The dangerous case is `format="mixed"`. It swaps day and month for some rows and parses others correctly by accident. The row count stays 60, and the plot is still wrong.

### Before any session

Run these from the lesson folder and keep the output:

```bash
python instructors/files/test_validators.py
```

It builds a good file and eight bad ones in a temporary folder, and confirms that the reference validator accepts the good file and rejects each bad one. Record the Claude Code version, the Python and package versions, the model name and the date. Test a learner route on each platform you will support: download, environment, one read-only agent action and one small diff.

---

## Timed route: four-hour pilot

Assume learners finish installation or receive a supplied environment before they arrive. Offer a separate 30-minute setup clinic. Send prework of 20 to 30 minutes: environment, download, the synthetic-data statement and a ten-minute no-AI entry check.

| Elapsed | Min | Activity | Where |
|---|---:|---|---|
| 00:00 | 15 | Setup diagnostic and entry check. Assign the live-agent route or the saved-output route. | `learners/setup.md` |
| 00:15 | 30 | `dropna` reading, then the date exercise: predict, pair trace, run, add checks, decide. | Episode 0 |
| 00:45 | 25 | CLI scope, shell versus agent, `/init` once, one diff, one constraint plus check. | Episode 1 |
| 01:10 | 10 | Catch-up checkpoint. Share a question the agent did not resolve. | |
| 01:20 | 25 | Repair a prompt. Review a plan, mark one unsupported assumption, approve one bounded action. | Episode 2 |
| 01:45 | 15 | Break. | |
| 02:00 | 40 | Cleaning: predict, plan, one bounded change, read the diff, explain, run. | Episode 3 |
| 02:40 | 35 | Complete the date check, run it on good and bad files, discuss what remains unchecked. | Episode 4 |
| 03:15 | 10 | Catch-up using the checkpoint packs. Restore the canonical 60-row output. | |
| 03:25 | 25 | Assemble and swap the bundle. The partner reruns without AI. | Episode 6 |
| 03:50 | 10 | Unaided transfer decision and the Monday card. | Episode 7 |

Episode 5 is not taught as its own block in the pilot. Its scope and privacy points sit in Episode 1, and its failure modes sit in Episodes 2 and 4. The full eight-episode course is longer. The episode front matter adds up to about 9.5 hours, before breaks and installation.

### Reference and follow-on

- Reference: the CO-STAR framework, tool comparisons, reasoning-effort settings, MCP, the model taxonomy, the environmental discussion and publication policies.
- Follow-on: write every validator check yourself, a metamorphic shuffle test, alternative missing-value methods, the February filter, registry verification, a multi-model critique, and Git recovery practice. Do not claim these objectives in the four-hour pilot.

### Checkpoint packs

Keep four folders ready, so a learner who falls behind can rejoin without skipping the judgment tasks:

1. Raw inputs only.
2. A working `clean_and_merge.py` (`instructors/files/backup_clean_and_merge.py`) with its output.
3. The complete checks (`instructors/files/backup_validate_data.py`).
4. The final bundle, including `plot_trend.py` (`instructors/files/backup_plot_trend.py`).

A learner who uses a pack still predicts, explains, tests and decides. Label which parts were supplied.

### When outputs differ

Compare behaviour and not text. Stop after each bounded change. Ask every learner for the same prediction and the same evidence. After two failed generation attempts, use a supplied script.

### No-account learners

They use the same terminal and Python files, plus saved agent plans, diffs and transcripts. They make the same approval decisions and run the same tests. If Python is also unavailable, supply a pre-provisioned terminal or a loan device. A printed-output-only route can assess review, but it cannot honestly certify independent execution. Do not require a second vendor account for any pilot outcome.

### Entry check (ten minutes, no AI)

Learners should be able to: go to the supplied folder; list the three inputs; run a supplied script; say which rows `dropna()` removes; predict how four January records per site change the 60-row total; and see that `05-01-2023` needs the source metadata. Treat errors as information for routing. Offer a refresher or a supported pair. Do not surprise anyone with an exclusion after enrolment.

---

## Helper observation sheet

Ask helpers to record, for each learner who asks for help:

- The time and the episode.
- The route: live agent or saved output.
- What the help was about: installation, Python, shell, a concept, or the agent.
- Whether a concept stayed unresolved at the end.

Helpers route a learner to a known state. They do not do the learner's judgment task. Record whether the partner in the capstone actually reran the bundle or only inspected saved output.

---

## Episode notes

### Episode 0: Before We Use AI
- Purpose: reset expectations. The workshop measures whether learners can explain and check AI output, not how fast they can generate it.
- Make it safe to say "I do not understand this line." Treat confusing output as a shared example.
- The run, revise or reject checkpoint appears here and in every later episode. Refer to it by name.
- The date exercise is deliberately faulty teaching code. Do not claim every agent makes this mistake.

### Episode 1: CLI-Based AI
- Run the setup check, including the read-only agent action. A version number confirms only the program.
- Set the same available model with `/model`. Record the resolved model name, tool version and settings.
- Everyone works in the provided `coastal-water-quality` folder. Confirm that `ls data/` shows three files.
- The consultant versus research assistant analogy helps, but stress that access depends on configuration.

### Episode 2: Prompting
- Do not linger on acronyms. The goal is a prompt that names the input, the intended change, the constraints and the evidence.
- Show a weak prompt and a better one live. Let the weak one fail first.

### Episode 3: Data cleaning
- This is the most demanding episode.
- Expected output: `data/master_dataset.csv` with 60 rows. The February challenge writes `data/feb_onward.csv` (48 rows) and leaves the canonical file alone. A wrong count usually means some site C dates were misparsed.
- Safety net: after two failed attempts, use `instructors/files/backup_clean_and_merge.py`.
- Stop and read: ask the class to take their hands off the keyboards for two minutes.

### Episode 4: Validation
- The four layers: recorded requirements, executable checks, metamorphic and invariant checks, domain plausibility.
- Learners write one check, the date check, from the source documentation. Unfinished checks fail closed.
- Learners then break a copy of the output on purpose and confirm that the check fails. Restore the correct output afterward.
- The reference validator has eight checks and covers more than the starter.

### Episode 5: Limitations
- Silent semantic drift is the dangerous failure. The date trap is its live version.
- Spec drift: compare code with approved requirements. Do not sync requirements to code without evidence.

### Episode 6: Capstone
- Mostly doing. Reuse the existing cleaner and validator.
- The partner reruns the bundle in a fresh copy without AI. Use the site-relabel case as the transfer error.
- Read a few approval decisions aloud, especially honest "revise" answers.

### Episode 7: Resources
- Tools change fast. Focus on the principles.
- Monday card: push learners to name one likely error, the check that would catch it and one unchecked claim.
- AI cannot be an author. Openness about its use is part of open science.

---

## Troubleshooting

### Account or quota failure
If a learner hits a usage or quota error, switch them to the saved-output route. Check the account type and the current limits in the official documentation. Do not rely on a fixed waiting time.

### `claude: command not found`
Re-run the installer from `learners/setup.md` and restart the terminal. For an npm install, check Node.js 22 or newer and the `PATH`. Run `claude doctor` for a diagnostic.

### Hallucinations
If a learner gets a script that imports a nonexistent library, use it as a teachable moment for the class.

---

## Maintainer checklist

Run through this before teaching a pilot or merging substantial changes. It encodes Carpentries guidance on teaching with generative AI.

### Cognitive load
- [ ] No exercise depends on syntax, libraries or abstractions the lesson has not introduced.
- [ ] Where generated code is likely to over-reach (lambdas, regular expressions, extra files), an instructor note says so.
- [ ] Small, interpretable tasks come before larger agentic workflows.

### Learner agency
- [ ] No exercise can be finished by pasting the task into an AI and copying the answer.
- [ ] Every challenge needs at least one of: explain, predict, trace, modify and justify, or validate.
- [ ] The language frames the learner as the active reviewer and final judge.

### Feedback loop
- [ ] Each episode has at least one pause-and-report checkpoint.
- [ ] Checkpoints show where learners are confused, not only whether code ran.

### Validation and reproducibility
- [ ] Exercises check with concrete evidence (counts, invariants, tests), not "it ran."
- [ ] `python instructors/files/test_validators.py` passes.
- [ ] Provenance (tool version, model, date, prompt) is recorded for generated code, and code, data, environment and commands are archived so a result reruns without the model.
- [ ] Rewrite time is framed as a formative signal, never as proof that AI is faster.

### Privacy and security
- [ ] Sensitive-data and security-critical tasks are flagged as out of scope for AI.
- [ ] Institutional and personal account differences are stated where relevant, and policy wording was checked against the current campus source.

---

## Keeping the lesson current

The AI tool landscape moves faster than a release cycle. The most volatile parts are the tool table in Episode 7, the failure modes in Episode 5, the account and retention wording in `learners/setup.md`, and any named model or command in Episodes 1 to 4.

Before each offering:

1. Record the tested tool and package versions, the backend, the platform and the date, with a command transcript.
2. Check official documentation and institutional policy first. News and the topic wiki help you find claims worth checking. They are not authority for account permissions or commands.
3. The `last30days` workflow can discover changes. It cannot replace that verification.

Use the output two ways: confirm the claims in Episodes 5 and 7, and find one current hype example to take apart live in "Spotting hype."

### UCLA sources (checked 2026-11-07)

- Tool matrix: [campus AI tools comparison][ucla-ai-tools] (October 2026). Footnote 1: P1 to P3 in a UCLA account; P4 with Unit Head and CISO approval. Anthropic products: "coming soon," TBD.
- [AI use and recommendation guide][ucla-ai-guide]: says Anthropic "has been reviewed and approved at P2 levels" with no access route, lists AWS Bedrock models (including Claude) with no tier, and gives `grc@ucla.edu` as the intake for questions about restricted data. The matrix and the guide disagree about Anthropic. Do not tell learners either is the final word.
- Open question for GRC: the UC guide puts FERPA records at P3, and the matrix allows P1 to P3, but the UCLA guide says FERPA data need a secure environment. Ask before you tell learners whether FERPA data may go into a listed tool.
- [UC Protection Level Classification Guide][uc-protection-levels] (revised July 2022): attorney-client privileged information P3; FERPA student records P3; PHI P4; human-subjects data with identifiers P4; export-controlled research P3 or P4 by case; de-identified patient information and unpublished research P2. UCLA's pages do not address attorney-client material. Do not claim approval for it.
- Not found: a UCOP legal alert on AI tools, and the identifiers "BUS-43" and "RMP-7" that one reviewer cited. Do not quote them.

### Tooling status

- The lesson uses Claude Code as its tested route. Other CLI products and access options change.
- Learners use a personal subscription or API key for the synthetic data in this workshop. Do not read permission for institutional data into any account type. Confirm the specific account, configuration and data category with the responsible campus authority before using real sensitive data. See `learners/setup.md`.
- The lesson's principles (plan first, checks, provenance, review) transfer across CLI agents. See the `agentic-research/cli-agent-landscape` wiki note as a lead, and verify against current documentation.

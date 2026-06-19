# Lesson Design Notes

Design record for *Agentic Research Workflows: AI Coding, Validation, and Research
Responsibility*. Follows the Carpentries [collaborative lesson development](https://carpentries.github.io/lesson-development-training/)
backward-design process. Living document; update it when the design changes.

## Lesson summary

Help researchers work with AI coding agents (Claude Code) without giving up the
learning, feedback, validation, and judgement that make code trustworthy. The lesson
is built around one worked example carried from messy data to a validated, documented
result.

Lifecycle stage: **pre-alpha** (see "Pilot and feedback plan").

## Target audience

Researchers, graduate students, librarians, and research-data support staff who do
their own data work and are starting to use AI coding tools. Expertise: **novice to
competent practitioner** in Python and the command line; **novice** with AI agents.
Personas are in `profiles/learner-profile.md` (Amara, ecology postdoc; Diego, cautious
PhD first-timer; Priya, skeptical data analyst).

Prerequisites: basic command line; basic Python (variables, functions, scripts). No
prior AI-agent experience required.

**Audiences we explicitly do not target (and why):**

- Software engineers building production systems (this is about research judgement,
  not shipping software).
- Complete programming beginners (they should take Software/Data Carpentry first;
  AI output is hardest to judge with no code background).
- Researchers needing statistical-methods instruction (out of scope; we use a simple
  analysis only as something to validate).

## Lesson-level learning objectives

At the end of this lesson, learners will be able to:

1. Distinguish code generation, code understanding, and code validation, and explain
   why AI-generated code can raise a novice's cognitive load.
2. Use a CLI agent guided by a Living Spec (`CLAUDE.md`) to plan and generate research
   code, reviewing and approving each step rather than accepting it wholesale.
3. Validate an AI-generated result with concrete, runnable checks (invariants and
   domain plausibility) and decide whether to approve, revise, or reject it.
4. Document an AI-assisted workflow (prompt, spec, validation, provenance) so another
   researcher could reproduce and judge the result.

Scope check: ~5 hours of material (roughly a long half-day to one day); 4 lesson-level
objectives is within the Carpentries guideline of 3-4 per 6 hours.

## Episode breakdown

| # | Episode | Serves objective(s) | Main assessment |
|---|---|---|---|
| 0 | Before We Use AI | 1 | snippet run/revise/reject decision |
| 1 | CLI-Based AI | 2 | inspect real data; `/init` a spec |
| 2 | Best Practices for Prompting | 2 | prompt-repair / plan-first challenges |
| 3 | Data Cleaning with AI | 2, 3 | predict -> plan -> clean -> validate the merge |
| 4 | Validation: The Approval Gate | 3 | build the validator; explain the approval gate |
| 5 | Limitations and Cautions | 1, 3 | when (not) to use AI; hallucination check |
| 6 | From AI Output to Research-Ready Code (capstone) | 2, 3, 4 | full bundle + approval decision |
| 7 | Resources and Next Steps | 4 | Monday workflow planning card |

## The worked example (central narrative)

`learners/files/coastal-water-quality/`: three synthetic site CSVs (60 rows total)
with inconsistent column names, three different date formats, and missing values.

Why this dataset:
- **Relevance:** data cleaning is near-universal across research domains; low
  domain-knowledge barrier.
- **Authentic but small:** real-feeling messiness, small enough to read by eye.
- **Verifiable:** concrete checks (60-row invariant, date ranges, score 0-100) make
  formative assessment and the validation stack meaningful.
- **A planted trap:** site C dates are day-month-year (`05-01-2023` = 5 January). If
  misparsed, the script still runs, the row count is still right, and the trend plot
  is still wrong, the lesson's "working code is not trustworthy code" thesis in one
  concrete failure.
- **Ethics/licence:** synthetic, so no privacy or consent concerns; labelled as such
  so no one cites it as real.

The example continues into a light analysis (score trend over time by site) so there
is a research *result* to judge, not just a clean file.

## Key design decisions

- **Active reviewer, not orchestrator.** The framing deliberately rejects "the AI does
  the work and you orchestrate." Learners must explain and validate, not delegate.
- **Fixed data, not AI-generated.** Everyone works the same provided files so debugging
  and formative assessment are tractable; AI-generated data is an optional aside.
- **Executable validation.** `validate_data.py` ships incomplete; learners finish it, so
  "valid" means "checks passed," not "looked fine."
- **Tool: Claude Code, dual-backend.** Personal plan for non-sensitive (P1-P3) data;
  UCLA Amazon Bedrock for sensitive (P3/P4). Principles transfer to other CLI agents.
- **Style:** British English, Title Case episode titles (Carpentries style guide).
  **Contractions are kept** for an approachable tone; this departs from the lesson-dev
  accessibility checklist's "avoid contractions," a deliberate readability choice.

## Terminology

Glossary in `learners/reference.md`. Consider contributing shared terms to
[Glosario](https://glosario.carpentries.org/).

## Pilot and feedback plan

To move pre-alpha -> alpha, the original authors teach it and collect structured
feedback.

**During the pilot, capture:**
- Actual time per episode vs the planned timings (the biggest unknown).
- Where learners got stuck, confused, or went quiet.
- Whether the site C date trap surfaced and whether learners caught it.
- Which objectives clearly landed and which did not.

**Learner feedback survey (end of workshop):**
1. Which part most changed how you will use AI for your own data?
2. Where did you get stuck or confused?
3. Did you catch the date problem in site C? If not, where did you first notice
   something was off?
4. After today, could you run this workflow on your own data? What would still block
   you?
5. One thing to cut, and one thing you wanted more of.
6. Confidence (1-5) before and after: "I can judge whether AI-generated code is correct
   for my research."

**After the pilot:** revisit this document and the episodes; if over time, cut whole
objectives (and their assessments and content) rather than trimming everywhere. Record
changes here.

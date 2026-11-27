# One-page map: learner path to episodes

Draft. Episode numbers start at 0, like the file names. Nothing here is timed with
learners.

Path: explore, understand, check, save as a program, name it, reuse it, connect it.

| Step | Learner work (not the agent's) | Episode | Keep | Add or change | Cut from the pilot core |
|---|---|---|---|---|---|
| Explore | Sketch the steps, spot what repeats and what differs across sites, state inputs and outputs, before seeing any agent plan | 0, 3 | date exercise; looking at raw files | remove the worked list of inconsistencies in cleaning step A until after learners write theirs | separate prompt-repair exercise (merge with plan review in 2) |
| Understand | Predict what one block changes and what it must preserve | 1, 2, 3 | plan review; explain before running | ask for "must not change" in every prediction | extended tool setup; CLI mode comparison stays reference |
| Check | Complete the date check by hand, say where expected values come from, make it fail | 4 | independent expected values; bad-copy test | one worked check with purpose labels, then learners label their own; no agent draft of the date check in the pilot | other validation layers as exposition |
| Save as a program | Say what the cleaner and validator read, write and assume | 3, 4 | the two existing scripts | a short header: inputs, outputs, assumptions | generating a new plot script |
| Name it | Give each program and its main function a name that says what it promises | 3 | `clean_site` and the `SITES` table as the worked example of pattern and abstraction | learners say what is shared and what is a setting | general CLI design and packaging |
| Reuse | Run on batch 2, diagnose, make one change by hand, decide what the median means | new, after 4 | same source formats | batch 2 and its delivery note | time must come from cuts above |
| Connect | Decide whether a later step used the file that was checked | 6 | partner rerun | supplied plot script; wrong-file record | planning and generating the plot |

## Three questions that stay in every step

- What does this step expect and hand on?
- What can it change?
- What would show that it failed, and what would a pass leave untested?

## Open points

- The four-hour route is full. The cuts above may not make enough room.
- Episode 1 has an objective about creating `CLAUDE.md`, and episodes 3 and 6 read
  it. If `/init` moves out of the pilot, supply a new starter file.
  `CLAUDE.example.md` is not loaded automatically and gives away checks.
- Cutting plot generation means the pilot must not claim learners planned or
  generated the plot.

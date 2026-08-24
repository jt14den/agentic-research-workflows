# Pedagogical Evaluation: Agentic Research Workflows (ARCHIVED)

> **This evaluation is a superseded historical snapshot, not current guidance.**
> It predates the pivot from `AGENTS.md`/Gemini CLI to `CLAUDE.md`/Claude Code,
> references a 6-episode structure (the lesson now has 8), and its "ready for
> alpha testing" conclusion does not reflect the current `pre-alpha` lifecycle
> status. Kept for historical reference only. For current status, see the
> repository's most recent audit and adjudication documents rather than this
> file.

**Date:** January 11, 2026
**Evaluator:** Gemini Agent (Pedagogy & Design)
**Standards Source:** `AGENTS.md` (Backward Design, Student-Centered Learning, Cognitive Load, Professional Values)

## Executive Summary
The lesson "Agentic Research Workflows" effectively introduces AI-assisted programming using a CLI-first approach. It scores highly on **Professional Values** and **Active Learning** but has minor gaps in **Backward Design** (specifically assessment alignment) and **Cognitive Load** (some scaffolding could be improved). The shift to **Spec-Driven Research Orchestration** clarifies the researcher's role.

---

## Episode-by-Episode Analysis

### Episode 1: Understanding CLI-Based AI
*   **Backward Design:** 
    *   *Objectives:* "Compare CLI and Browser-based AI", "Create Living Spec (AGENTS.md)", "Explain shift to Orchestrator".
    *   *Alignment:* Strong. The challenges directly ask users to compare output (`ls` vs AI) and create `AGENTS.md`.
*   **Student-Centered:** 
    *   Uses "I Do" (Explanation) -> "You Do" (Challenges).
    *   Includes a `Discussion Prompt` to activate prior knowledge ("Have you ever used ChatGPT...").
*   **Cognitive Load:** 
    *   *Risk:* The switch between "Browser" vs "CLI" tables is heavy on text.
    *   *Mitigation:* The "Visual Aids" tips for instructors are helpful.
*   **Professional Values:** 
    *   Excellent "Data Privacy Warning" and emphasis on "Verification Load".

### Episode 2: Best Practices for Prompts
*   **Backward Design:**
    *   *Objectives:* "Apply CLEAR framework", "Identify sneaky behaviors", "The Bootstrap Workflow".
    *   *Alignment:* The challenge "The Prompt Refinement Loop" directly tests applying CLEAR. The Bootstrap Workflow encourages iterative spec drafting.
*   **Student-Centered:**
    *   The "Bad vs Good" table serves as a good scaffold.
    *   *Gap:* The "Introspection" objective is taught but not explicitly tested in a challenge (only mentioned in text).
*   **Cognitive Load:**
    *   The acronym "CLEAR" provides good mnemonic scaffolding.
*   **Professional Values:**
    *   Strong focus on "Self-Correction" and "Sneaky AI" aligns with the "Orchestrator" mindset.

### Episode 3: Data Cleaning (Live Demo)
*   **Backward Design:**
    *   *Objectives:* "Generate test dataset", "Spec-Guided Cleaning", "Verify code", "Document process".
    *   *Alignment:* Strong. The episode is a continuous project where learners build the pipeline step-by-step using the `AGENTS.md` spec.
*   **Student-Centered:**
    *   "The Curveball" challenge (PI changing requirements) is an excellent real-world scenario that promotes adaptability.
*   **Cognitive Load:**
    *   *High Load:* This is a dense episode. Writing 3-4 distinct scripts (`make_messy_data`, `inspect`, `clean`, `readme`).
    *   *Mitigation:* The `prereq` block helps setup.
    *   *Suggestion:* Consider providing the `make_messy_data.py` code directly instead of generating it, if time is tight, to focus purely on *cleaning*.
*   **Professional Values:**
    *   The "Stop and Read" callout is a critical intervention for the "Orchestrator" mindset.

### Episode 4: Validation Best Practices
*   **Backward Design:**
    *   *Objectives:* "Implement checks", "Domain Plausibility", "Traceable Orchestration (Aider)".
    *   *Alignment:* Challenge "The Integrity Check" covers implementing checks. Layer 4 (Domain Plausibility) is a key addition.
    *   *Gap:* "Cross-AI auditing" is an objective but the challenge focuses mainly on writing a Python validation script.
*   **Student-Centered:**
    *   Good use of "Future-Proofing" to motivate *why* validation matters.
*   **Professional Values:**
    *   Strong emphasis on "Defensive Programming" and "Commit-as-Draft" as research insurance.

### Episode 5: Limitations and Cautions
*   **Backward Design:**
    *   *Objectives:* "Recognize high-risk", "Identify hallucination", "Distinguish Open vs Proprietary".
    *   *Alignment:* Challenge "Spot the Hallucination" matches the objective perfectly.
*   **Student-Centered:**
    *   This is the most "lecture-heavy" episode. The "Hallucination" challenge is fun but brief.
*   **Cognitive Load:**
    *   Low load, mostly conceptual.
*   **Professional Values:**
    *   The distinction between "Proprietary" and "Open Weights" is crucial for open science transparency.

### Episode 6: Resources and Next Steps
*   **Backward Design:**
    *   *Objectives:* "List tools", "Locate help", "Understand MCP".
    *   *Alignment:* No formal challenge (exercises: 0). This is acceptable for a wrap-up, but a "Personal Action Plan" challenge could strengthen it.
*   **Student-Centered:**
    *   The new "Signal vs Noise" discussion block engages learners' critical thinking.
*   **Professional Values:**
    *   The "Hype Detection Kit" and "Attribution Pattern" are high-value takeaways for ethical research.

---

## Recommendations for Future Lesson Development

### 1. Assessment Alignment (Backward Design)
*   **Issue:** Some objectives (e.g., "Cross-AI Auditing" in Ep 4) are discussed but not rigorously tested in a Challenge.
*   **Fix:** Ensure *every* bullet point in "Objectives" maps to a specific action in a "Challenge". If it can't be challenged, downgrade it to a "Key Point" or remove it.

### 2. Scaffolding Complex Tasks (Cognitive Load)
*   **Issue:** Episode 3 (Data Cleaning) requires generating multiple scripts in sequence. If step 1 fails, the whole lesson stalls.
*   **Fix:** Create "Parsons Problems" or "Fill-in-the-blank" prompts for struggling learners. Provide "Safety Net" files (e.g., `data/backup_clean_script.py`) so learners can jump to Step 3 even if Step 2 failed.

### 3. Explicit Reflection (Student-Centered)
*   **Issue:** We tell learners to "be editors," but we don't always give them structured time to reflect on *how* that felt.
*   **Fix:** Add specific "Reflection Questions" inside the solution blocks (e.g., "Did the AI write code you wouldn't have thought of? Did it make a mistake you almost missed?").

### 4. Expanding the "Editor" Mindset
*   **Issue:** The "Editor" concept is introduced well in Ep 1 but could be reinforced more explicitly in Ep 5 & 6.
*   **Fix:** Use the term "Verification Load" consistently across all episodes to tie the narrative together.

## Conclusion
The lesson is pedagogically sound and ready for alpha testing. The additions of the "Discussion" and "Checklist" components have significantly improved the interactivity and professional value of the content.

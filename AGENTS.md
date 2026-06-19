# Project Context: Agentic Research Workflows: AI Coding, Validation, and Research Responsibility

This repository contains the "Agentic Research Workflows" lesson, part of the IMLS Open Science curriculum hub. It is a Carpentries-style lesson (using the Sandpaper framework) designed to introduce researchers to AI-assisted programming and validation best practices.

## Recent Accomplishments

### Current Lesson Development (`agentic-research-workflows`)
- **Orchestration Context**: Added sections on "Spec-Driven Research Orchestration" and cognitive load management, emphasizing the shift from "writer" to "orchestrator" in the development process.
- **Framework Integration**: Integrated the **CO-STAR** prompting framework, the **CLEAR** framework, and the **Bootstrap Workflow** into the curriculum.
- **Glossary & References**: Converted the glossary to a semantic definition list format and updated references to include Aider and the Spec-Driven workflow.
- **Markdown Polish**: Performed multiple passes of markdown formatting improvements for better readability and accessibility.
- **Lesson Structure**: Defined 6 core episodes:
    1. Understanding CLI-Based AI (Writer to Orchestrator)
    2. Effective Prompting (The Bootstrap Workflow)
    3. AI-Assisted Data Cleaning (Spec-Guided Cleaning)
    4. Validation Strategies (The 4-Layer Validation Stack)
    5. Limitations & Bias (Spec Drift & Bootstrap Failures)
    6. Resources & Next Steps (Aider & Commit-as-Draft)

## Project Structure
- `episodes/`: Markdown files for each lesson chapter.
- `instructors/`: Teaching notes and guides.
- `learners/`: Setup instructions and reference materials.
- `site/`: Built static site files and configuration.
- `config.yaml`: Lesson configuration and episode order.

## Orchestration Standards (2026)

### Requirement Constraints (No-Go Zones)
When editing this lesson, AI agents must adhere to these hard constraints:
- **No-Go Zone 1**: Do not change the fundamental Carpentries Sandpaper syntax (e.g., keep the colons `:::` blocks).
- **No-Go Zone 2**: Do not modify existing technical setup instructions in `learners/` without human approval.
- **No-Go Zone 3**: Ensure all examples remain relevant to general research (avoid overly domain-specific jargon).

### Efficiency Metrics
- **Target Rewrite Time**: < 10% (Human review and refactoring should take minimal time).
- **Validation Gate**: All new content must be cross-verified by a "Challenger" model (e.g., Gemini CLI auditing Claude Code).

## Tech Stack & Conventions
- **Framework**: Carpentries Sandpaper (R-based lesson engine).
- **Language**: Markdown, with R-Markdown support.
- **Style**: Semantic HTML elements within markdown (e.g., definition lists), clear callout blocks.
- **Validation Focus**: Emphasis on Synthetic Data, Domain Plausibility, Cross-AI verification, Unit Testing, and Traceable Commits (Aider).

## Pedagogical Standards

### Core Design Principles
1.  **Backward Design & Constructive Alignment**:
    *   **Outcomes First**: Define clear, measurable *Learning Objectives*.
    *   **Alignment**: Ensure teaching methods and assessments (challenges) directly match the objectives.
    *   **Assessment**: Create challenges that allow learners to demonstrate they have met the outcomes.

2.  **Student-Centered Learning**:
    *   **Active Learning**: Prioritize "doing" over "listening." Use the "I Do, We Do, You Do" flow.
    *   **Reflection**: Include opportunities for learners to reflect on *how* they are solving problems (metacognition), especially when using AI.
    *   **Diversity**: Acknowledge different learning styles by offering various types of explanations (visual, code, text) and challenges.

3.  **Cognitive Load Management**:
    *   **Minimize Extraneous Load**: Remove complex setups or tools not central to the learning goal.
    *   **Scaffolding**: Provide partial code or "parsons problems" for complex tasks to reduce initial friction.
    *   **The "Orchestrator" Mindset**: Shift focus from syntax generation (high load) to logic verification and spec management (high value).

4.  **Professional Values**:
    *   **Scholarship**: Connect AI tools to established research methods, not just "productivity hacks."
    *   **Inclusivity**: Ensure examples and language are accessible to researchers from diverse backgrounds.
    *   **Transparency**: Be open about the limitations and "black box" nature of AI tools.

## Carpentries Workbench Standards

### Documentation
- **Pedagogy**: [Carpentries Lesson Development Training](https://carpentries.github.io/lesson-development-training/)
- **Technical**: [The Carpentries Workbench](https://carpentries.github.io/workbench/)

### Verification
To ensure the lesson is correctly formatted and free of errors, run the following commands in the R console:

1.  **Check Lesson Structure**:
    ```r
    sandpaper::check_lesson()
    ```
2.  **Validate Lesson Content** (links, images, components):
    ```r
    sandpaper::validate_lesson()
    ```
3.  **Build and Preview**:
    ```r
    sandpaper::serve()
    ```

### Component Syntax
The Workbench uses **Pandoc fenced divs** (colons `:::`) for special blocks. The opening and closing tags must match in length (at least 3 colons, usually recommended to use more to distinguish from nested blocks).

**Episode Structure Blocks:**
*   `::::::::::::::::::::::::::::::::::::::: objectives` (Start of episode)
*   `:::::::::::::::::::::::::::::::::::::::: questions` (Start of episode)
*   `:::::::::::::::::::::::::::::::::::::::: keypoints` (End of episode)

**Interactive Blocks:**
*   `::::::::::::::::::::::::::::::::::::::::: challenge` (Exercises)
    *   `:::::::::::::::::::::::::::::::::::::::: solution` (Must be nested inside `challenge`)
    *   `:::::::::::::::::::::::::::::::::::::::::::: hint` (Optional; Must be nested inside `challenge`)

**Callout Blocks:**
*   `::::::::::::::::::::::::::::::::::::::::: callout` (General info/warning)
*   `:::::::::::::::::::::::::::::::::::::::::: prereq` (Prerequisites)
*   `::::::::::::::::::::::::::::::::::::::: checklist` (Checklists)
*   `:::::::::::::::::::::::::::::::::::::: discussion` (Discussion topics)
*   `::::::::::::::::::::::::::::::::::::: testimonial` (Quotes/Testimonials)

**Advanced Blocks:**
*   `::::::::::::::::::::::::::::::::::::::::: instructor` (Instructor-only notes - visible in instructor view)
*   `::::::::::::::::::::::::::::::::::::::::::::::::: spoiler` (Collapsible content)
*   `::::::::::::::::::::::::::::::::::::::::: output` (Output block for code results)
*   `::::::::::::::::::::::::::::::::::::::: div` (Generic div for custom styling)

**Tabs:**
*   `::::::::::::::::::::::::::::::::::::::::: panel-tabset` (Container for tabs - automatic tab creation from headers)
    *   OR
*   `:::::::::::::::::::::::::::::::::::::::::: group-tab` (Manual Container for tabs)
    *   `:::::::::::::::::::::::::::::::::::::::::: tab` (Individual tab content)

### Structure Rules
1.  **Front Matter**: Each episode (`.md` file) must start with YAML front matter defining `title`, `teaching` (minutes), and `exercises` (minutes).
2.  **Flow**: `objectives` and `questions` blocks must appear immediately after the front matter.
3.  **Closing**: The `keypoints` block must be the final element of the episode.
4.  **Nesting**: 
    - `solution` and `hint` blocks **must** be inside a `challenge` block.
    - Ensure nested blocks use a different number of colons than their parent block to avoid Markdown parsing errors (e.g., parent uses 40 colons, child uses 35).
    - Always check for matching closing tags.

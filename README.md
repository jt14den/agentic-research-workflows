# Agentic Research Workflows: AI Coding, Validation, and Research Responsibility

[![Status](https://img.shields.io/badge/Status-pre--alpha-red.svg)](https://github.com/jt14den/agentic-research-workflows)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This lesson introduces researchers to **Agentic Research Workflows**: using AI coding agents in the terminal while keeping the validation, reproducibility, and research judgment that make code trustworthy.

**[View the Lesson Website](https://www.tim-dennis.com/agentic-research-workflows/)**

## Overview

This lesson teaches researchers to work with AI coding agents without giving up the learning, feedback, validation, and research judgment that make code trustworthy. AI changes *what you need to practice*: less time recalling every line of syntax, more time understanding intent, dependencies, assumptions, tests, and failure modes. The hands-on work uses **Claude Code**, but the principles apply to any CLI coding agent.

## Key Features
*   **CLI-First Approach**: Learn to use AI directly in your terminal where your data lives.
*   **The Living Spec**: Master the use of `CLAUDE.md` (and the portable `AGENTS.md` convention) to ground your AI in your specific project goals.
*   **Validation**: Learn strategies like Synthetic Data Generation, Domain Plausibility, and Cross-AI Auditing to ensure research integrity.


## Contributing

We welcome contributions! This lesson is built using [The Carpentries Workbench](https://carpentries.github.io/workbench/).

To get started:
1.  Fork this repository.
2.  Clone your fork locally.
3.  Install the required tools (R, Pandoc, Sandpaper).

## Building the Lesson Locally

This lesson is written in Markdown and built with [Sandpaper](https://carpentries.github.io/sandpaper/).

1.  **Install R and the Workbench:**
    Follow the instructions in the [Workbench Documentation](https://carpentries.github.io/workbench/).

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/jt14den/agentic-research-workflows.git
    cd agentic-research-workflows
    ```

3.  **Preview the Lesson:**
    Open R/RStudio and run:
    ```r
    sandpaper::serve()
    ```

## Credits

This lesson is adapted from the workshop "Vibe Coding for Research" by **Bruno Smaniotto** and **Tom van Nuenen** at the **UC Berkeley D-Lab**.

## AI Attribution

This lesson was developed with the assistance of AI tools, adhering to the project's own transparency standards:

*   **Model:** Anthropic Claude (Opus/Sonnet, 2026)
*   **Role:** 
    *   **Porting & Conversion:** Assisted in porting the lesson content from original D-Lab workshop slides into the Carpentries Workbench markdown format.
    *   **Curriculum Validation:** Performed automated checks for completeness and alignment with Carpentries pedagogical standards.
    *   **Content Refactoring:** Identified gaps in the "Validation" and "Limitations" sections and assisted in refactoring the glossary into semantic HTML.
*   **Verification:** All AI-assisted content was reviewed, edited, and validated by the maintainers to ensure pedagogical accuracy and technical correctness.

## License

This content is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).

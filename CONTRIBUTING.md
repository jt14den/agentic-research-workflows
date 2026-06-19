---
title: "Contributing"
---

Thank you for considering a contribution to this lesson. It is developed openly,
and contributions of all kinds are welcome: fixing typos, reporting confusing
sections, suggesting exercises, improving accessibility, or piloting and reporting
back from a workshop.

By contributing, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to contribute

- **Report a problem or idea:** open an issue describing what was confusing,
  incorrect, or missing. Concrete examples (the episode, the step, what you
  expected) help most.
- **Suggest a change:** open a pull request. Small fixes can go straight to a PR;
  for larger changes, please open an issue first so we can discuss the approach.
- **Pilot the lesson:** if you teach it, the feedback in `DESIGN.md` ("Pilot and
  feedback plan") tells you what we most want to learn. Notes on timing,
  sticking points, and which objectives landed are especially valuable.

## Building the lesson locally

This lesson uses [The Carpentries Workbench](https://carpentries.github.io/workbench/).
With R installed:

```r
# install.packages("sandpaper", repos = "https://carpentries.r-universe.dev")
sandpaper::serve()      # preview locally
sandpaper::check_lesson()  # validate structure
```

## What we look for

- Changes align with the lesson's design (see `DESIGN.md`): one worked example,
  active-reviewer framing, executable validation, learner agency.
- Prose follows the [Carpentries style guide](https://docs.carpentries.org/resources/communications/style-guide.html)
  (British English, Title Case episode titles, descriptive link text).
- Episodes keep their questions / objectives / keypoints, and exercises ask
  learners to predict, explain, modify, or validate rather than copy and paste.

## Recognition

Contributors are acknowledged in the lesson. Significant contributions may be
recognised as authorship in `CITATION.cff`.

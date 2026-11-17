# For loops

Start with [the student notebook](instruction_exercises.ipynb) and follow the [instruction slides](instruction_slides.pptx) ([PDF](instruction_slides.pdf)).

Students should already know lists, `if` blocks, and functions. The lesson briefly introduces `range()`, then covers direct list iteration, decisions, building results, functions that process lists, and one small nested-loop example. It does not teach `while`, `break`, or `continue`, or introduce sets, tuples, or dictionaries.

## Using the notebook

Open the notebook in Jupyter or Google Colab with a Python 3 kernel. No extra packages or data files are needed. Run cells with Shift+Enter. Predict each teaching example's output, then try the matching modification. The notebook contains seven follow-along exercises, two suggested starting tasks for partner/instructor practice, and sixteen optional challenges. Optional challenges are choices, not a completion requirement.

The 61-slide deck includes prediction/reveal pairs, terminology examples, reference material, and exercise prompts. Select examples for about 20 minutes of direct instruction and reserve the rest of class for practice. The full deck is not a lecture checklist.

## Review

Use the [review slides](review_slides.pptx) ([PDF](review_slides.pdf)) for four short retrieval/application tasks. Each task is followed by an intentional answer slide. Pause before advancing if students should try it first.

Exercise solutions, instructor guides, and private speaker notes are not included in this distribution. Teaching examples remain runnable in the student notebook. Both PowerPoints have their speaker-note parts removed.

## Legacy materials

The original decks remain under `assets/` for reference. Use the generated materials linked above for this lesson's current sequence and scope.

## Authoring and verification

Source repository: `pi515/tech-mentorship-instruction`, `src/lessons/for-loops/`.

- Authoring commit: `37b56fc30c6b9ff29694d6b30b969d647c42e53e` (retained locally in the authoring repository; this publication does not push that private repository).
- Source SHA-256: `5ba63ab3526fc8e0a1f456927dc8406ec39fba02d069ccf036788437f2bc77de`.
- Generator SHA-256: `822b176bc509fe9e94abdae489753975fb43cc9869679dc5d646de93141b3663`.
- Renderers: Quarto 1.10.19; LibreOfficeDev 26.8.0.0.alpha0 2c87e51eeaa2b413ff4ae097b2705eea1995d8e5.
- Validation: 25 tests passed, lesson build/check passed, notebooks executed, student/instructor separation checked, and rendered slides/print materials visually inspected. Microsoft PowerPoint rendering was not independently inspected.

PDFs and the notebook match the generated files byte-for-byte. Published PPTX hashes differ because speaker-note parts and their package references were removed. Slide XML is unchanged, and all remaining internal relationships resolve.

| File | Generated SHA-256 | Published SHA-256 |
| --- | --- | --- |
| `instruction_slides.pptx` | `caa76e59c2c664f3e1846d4371a638c85362cdcadcf2da249b42c166bfc82541` | `a887866999bc55db09e2daf353b4188c40ceb8889300e733782ffc3de6dae1bb` |
| `instruction_slides.pdf` | `67bb8d75d0f6c9c93dd6de8cfcfcd575bdb774870d4d8ac6c762d4c9c052309e` | `67bb8d75d0f6c9c93dd6de8cfcfcd575bdb774870d4d8ac6c762d4c9c052309e` |
| `instruction_exercises.ipynb` | `21da34a21474dbecfb35b9c728d9f9cfe33a72eab44d7f6385178f96215ccb52` | `21da34a21474dbecfb35b9c728d9f9cfe33a72eab44d7f6385178f96215ccb52` |
| `review_slides.pptx` | `2cf7230ca85965e103e5bdcba9aba12e83d6e58bb289ad40bb25f0b16cc4be09` | `6ccbc599ef5a6b84bc37fb9b84c5d6e816a1991e7c7814405bfdcb7d7bb53512` |
| `review_slides.pdf` | `1b6ff3fb69fb1ddbe77497abaff33ab6d045d10e243a63fb34e8164aa404f32a` | `1b6ff3fb69fb1ddbe77497abaff33ab6d045d10e243a63fb34e8164aa404f32a` |

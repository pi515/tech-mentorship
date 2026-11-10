# Functions: inputs, results, and behavior

## Current lesson materials

- Instruction slides: [PowerPoint](instruction_slides.pptx) · [PDF](instruction_slides.pdf)
- [Student instruction notebook](instruction_exercises.ipynb): slide-aligned terminology/examples followed by instructor-paired practice. Exercises 0–7 follow instruction, 8–9 begin paired practice, and 10–29 are optional challenges.
- Review slides: [PowerPoint](review_slides.pptx) · [PDF](review_slides.pdf). These intentionally include authored answer slides after each review prompt.

Download the notebook and open it in Jupyter or upload it to Google Colab. It uses Python 3 and requires no extra packages or external data. Code cells have no saved outputs. Starter cells are intentionally incomplete. Run examples in order and save your own copy before editing.

The lesson covers defining/calling functions, inputs and returns, scope, purity, idempotence, higher-order functions, closures, and remembered state. Lists receive a brief introduction. Defaults and lambda notation are optional references. Select examples for instruction, then choose practice problems with an instructor. The full deck is not a checklist to present in one session.

Teaching code has a prediction slide followed by an output reveal. Terminology slides emphasize the code being discussed. Public PowerPoint copies omit speaker notes. Instruction exercise solutions and mentor guides are not included. Review answers remain intentionally visible in the review deck.

## Earlier materials

The original [6.4.pptx](6.4.pptx) and [assets](assets/) remain available as legacy materials. Use the named instruction/review files above for the current lesson. The earlier assets include advanced topics and unfinished exercises beyond this lesson's selected scope.

## Authoring and provenance

These files were generated from `src/lessons/functions/` in the `pi515/tech-mentorship-instruction` authoring repository. Make content changes there, then use `pnpm build functions` and `pnpm check functions`. Copy the five selected public files together so slides and notebook remain synchronized. Do not distribute solved notebooks or mentor guides.

This publication was built from an **uncommitted authoring working tree**. There is no recoverable authoring commit recorded for these exact inputs. The hashes below identify the source/build inputs and the published files, but do not substitute for a committed source revision.

- Lesson source SHA-256: `f3bfe20ab2e16aeea61a91eeb4b13673805fb268c60f3c5b128d9f726ebc3a7e`
- Generator SHA-256: `337aa7d1498c433d21b09971e8c83b3e5db7f1ec5816bd6505300c4aa13a6551`
- Quarto: `1.10.19`
- Slide PDF renderer: `LibreOfficeDev 26.8.0.0.alpha0 2c87e51eeaa2b413ff4ae097b2705eea1995d8e5`

Validation: 24 authoring tests passed; lesson build/check passed, including notebook execution and student/instructor separation. Affected slides were visually reviewed in LibreOffice PDF exports. Microsoft PowerPoint rendering and remote CI have not been verified.

The PDF and notebook files match the generated manifest exactly. Public PPTX files differ only by removal of speaker-note parts and their package references. Slide content is unchanged.

| File | Generated SHA-256 | Public SHA-256 |
| --- | --- | --- |
| `instruction_slides.pptx` | `8ab57ea3088145aecf5aef881fefc2b8973550d05c5075998a9fa32cb030bc14` | `72069151cc15b83cfc85bb58073aea6a833733f90131c5fadd385d7f134238fe` |
| `instruction_slides.pdf` | `33656c0619ea155c917bb7bc36cbcbca59e092518560f4dacc78c978154d4f01` | `33656c0619ea155c917bb7bc36cbcbca59e092518560f4dacc78c978154d4f01` |
| `instruction_exercises.ipynb` | `60f2ca03ab004da511e95db314831bf517a2a5472544e8af4cc38c01635df15d` | `60f2ca03ab004da511e95db314831bf517a2a5472544e8af4cc38c01635df15d` |
| `review_slides.pptx` | `94bba9f786aab858fe02457e2224405c907edf7524e7654b8b09f454fb579d9a` | `dc01bbde03b8e431d84c53887a2e0ea701bc2533d83a7863b2d1ded7b973777b` |
| `review_slides.pdf` | `83c797231a2d574bc79f667510ae6db9400254aabfbbeabb169e827e05bfe5bf` | `83c797231a2d574bc79f667510ae6db9400254aabfbbeabb169e827e05bfe5bf` |

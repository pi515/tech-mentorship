# Strings: indexing, slicing, and methods

## Current lesson materials

- Instruction slides: [PowerPoint](instruction_slides.pptx) · [PDF](instruction_slides.pdf)
- [Instruction exercises notebook](instruction_exercises.ipynb): follow-along examples and the remaining class exercises, using the same Exercise 0–9 titles as the instruction slides.
- Review slides: [PowerPoint](review_slides.pptx) · [PDF](review_slides.pdf). The review deck includes answer slides to reveal after students attempt each prompt.

Download the notebook and open it in Jupyter or upload it to Google Colab. It uses Python 3 with no additional packages. Code cells have no saved outputs. Follow-along examples are runnable, and exercise starter cells are intentionally unfinished.

The instruction deck includes reference examples and optional practice. Select material for the session rather than presenting every slide. Teaching examples have a prediction slide followed by the same slide with printed output. Exercise answers are kept in the instructor repository's solved notebook.

## Guess the word

The original [hangman.py](hangman.py) activity accompanies Exercise 2. The instructor runs `python3 hangman.py` in a terminal, chooses a hidden word privately, and projects the game. Students propose length, membership, and indexing questions. The notebook's game queries are discussion prompts, not executable cells, because the hidden word lives in the instructor's game.

## Sources and updates

The current materials are generated from `src/lessons/strings/` in the `pi515/tech-mentorship-instruction` authoring repository. Submit content changes there and rebuild with `pnpm build strings`, then validate with `pnpm check strings`. Copy the five current files listed above here together so slide and notebook exercise names remain synchronized. Do not copy solved notebooks into the student distribution. PowerPoint can be personalized for teaching, but substantive content changes should also be made in the Markdown sources.

The existing `2.2.*` and `2.2-updated.*` files are retained as earlier lesson versions. Use the named instruction/review materials above for the current lesson.

# Contribution and submission workflow

1. Sync with `main`.
2. Create a focused branch, for example `week-01/bytecount`.
3. Read the assignment before editing starter code.
4. Write predictions before running the program or tracing it.
5. Implement the task and add tests for every bug or edge case you discover.
6. Run the normal and sanitizer targets. Save the exact commands and output.
7. Open a pull request against `main`.

## Required PR notes

Include:

- **Prediction:** expected output, errors, syscalls, and resource behaviour.
- **Implementation:** key design decisions and error paths.
- **Verification:** commands, test output, sanitizer output, and (where requested) trace excerpts.
- **Explanation:** answer the assignment's source-based question.
- **Unresolved issues:** anything you could not verify.

Never describe code as tested unless you ran it and can show the evidence. CI results are evidence for the exact commit tested, not for later changes.

# Week 1 — Toolchain, file I/O, and debugging

<badge>Type: Implement</badge> <badge>Language: C</badge>

## Objective

Implement `bytecount`, a small command-line utility that reports the number of bytes in one file. The assignment is deliberately about correct I/O and failure handling, not merely counting a short text file.

**Interface:** `./bytecount PATH`

- On success, print the file's byte count as an unsigned decimal integer followed by a newline; exit 0.
- On failure, print a useful diagnostic to standard error and exit non-zero.
- Require exactly one path argument.
- Count bytes, not characters, lines, or Unicode code points.
- Do not load the whole file into memory.

## Read before coding

1. **OSTEP, Chapter 2 — Introduction to Operating Systems:** https://pages.cs.wisc.edu/~remzi/OSTEP/intro.pdf  
   Focus on the OS role and the system-call boundary. This is conceptual context, not a substitute for the API documentation.
2. **POSIX `fread()` specification:** https://pubs.opengroup.org/onlinepubs/9799919799/functions/fread.html  
   Read the return-value and error/EOF semantics carefully.
3. **Linux `read(2)` manual:** https://man7.org/linux/man-pages/man2/read.2.html  
   Compare the byte-count and short-read semantics with stdio.
4. **CS 162 course materials:** https://cs162.org/  
   Use the course's introductory material on the executable/process boundary as supporting context; do not treat a lecture overview as the specification for `fread()`.

## Work sequence

### 1. Predict — before the first run

Write down predictions in your submission notes:

- What should the program print for an empty file, a 1-byte file, and a file larger than the buffer?
- Which library call will your implementation use? Which kernel syscall(s) do you expect underneath it?
- Will one `fread()` call necessarily correspond to one `read(2)` syscall? Why?
- What should happen if the path does not exist, names a directory, or the process lacks permission?
- What is the maximum amount of file data your program should hold in memory at once?

Do not look at a trace before recording your predictions.

### 2. Implement

Complete `c/src/bytecount.c`.

Constraints:

- Use a fixed-size buffer and stream until EOF.
- Use `uint64_t` for the accumulated byte count; check for overflow before adding.
- Distinguish EOF from an I/O error using the stdio error indicators.
- Check the result of opening and closing the stream.
- Do not assume a read fills the requested buffer.
- Do not print a success result if an I/O or close error occurred.
- Avoid leaking the stream on any error path.
- Keep diagnostics on standard error and the successful count on standard output.

You may reorganize the starter code, but preserve the CLI contract above.

### 3. Verify

From this directory:

```sh
make clean all
make test
make sanitize
```

The Python tests cover empty, ordinary, binary, and multi-buffer files, invalid arguments, and a missing path. Add at least one test of your own.

### 4. Investigate the abstraction boundary

After your implementation passes the tests, run:

```sh
printf 'hello\\n' > /tmp/bytecount-small
strace -e trace=openat,read,close ./bytecount /tmp/bytecount-small
```

Then run it on a file substantially larger than the buffer. Record the relevant trace lines. Explain why the number and sizes of userspace `fread()` operations need not match the kernel `read(2)` calls.

### 5. Explain from the source

Using the POSIX `fread()` specification, explain precisely how your code distinguishes end-of-file from an I/O error. Why is checking only whether `fread()` returned fewer bytes than requested insufficient to diagnose an error?

## Submission requirements

Your PR must include:

- Completed C implementation.
- Any additional tests you wrote.
- A short `NOTES.md` containing predictions, actual observations, exact commands, relevant output/trace excerpts, and the source-based explanation.
- A statement of what you did not test or could not verify.

## Acceptance criteria

- Builds with warnings treated as errors.
- All provided tests pass.
- Sanitizer run reports no memory or undefined-behaviour errors.
- Correctly handles empty, binary, and files larger than the buffer.
- Correctly handles invalid CLI usage and file/I/O errors without printing a false success count.
- Uses bounded memory and closes resources on all paths.
- Explanation matches the POSIX API contract and the observed trace.

## Evaluation (100 points)

| Area | Weight |
|---|---:|
| Correctness and failure handling | 35 |
| Resource and memory management | 20 |
| Predictions, explanation, and source-based reasoning | 25 |
| Test and debugging evidence | 15 |
| Performance (only if relevant) | 5 |

No solution is included in the starter repository. Ask for hints in stages: reasoning first, then suspect area, concept hint, experiment, stronger hint, and only then a full solution if needed.

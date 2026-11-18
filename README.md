# Linux Systems Lab

A practice-first Linux systems programming course in C.

The goal is to understand what happens beneath a program: processes, kernel interfaces, memory, CPU scheduling, synchronization, filesystems, and networking.

## Learning loop

Every assignment follows:

1. **Predict** — write down expected syscalls, errors, resource behaviour, and (when relevant) page faults or context switches.
2. **Implement or fix** — work from the starter code; do not skip failure cases.
3. **Verify** — run tests and inspect evidence with tools such as `strace`, `gdb`, `/proc`, sanitizers, or `perf`.
4. **Explain** — connect observed behaviour to the API contract and, where requested, kernel behaviour.
5. **Measure** — only when performance is part of the question.

## Course sequence

| Week | Topic | Main work |
|---|---|---|
| 1 | Toolchain, byte-oriented file I/O, debugging | Implement `bytecount`; inspect stdio and syscalls |
| 2 | Processes | `fork`, `exec`, `waitpid`, exit status |
| 3 | File descriptors and IPC | descriptor lifetime, pipes, partial I/O |
| 4 | Threads and synchronization | races, mutexes, condition variables |
| 5 | Virtual memory | `mmap`, page faults, copy-on-write |
| 6 | Scheduling and synchronization | contention, deadlocks, measurement |
| 7 | Filesystems | metadata, directory operations, durability |
| 8 | Networking | sockets, framing, partial reads/writes |

The sequence may be adjusted when assignment evidence shows a prerequisite needs more work.

## Repository workflow

- One assignment directory per task.
- Work on a topic branch; submit a pull request for review.
- Keep predictions, commands, raw output, and explanations in your submission notes.
- Do not claim a test passed unless you have output or a CI log to support it.
- Starter tests may fail until the assignment is implemented; that is intentional.

## Assessment

- Correctness and failure handling: 35%
- Resource and memory management: 20%
- Understanding and source-based explanation: 25%
- Testing and debugging evidence: 15%
- Performance: 5% when relevant

A program that works on the happy path but leaks resources or mishandles errors is not a complete solution.

## Local environment

Week 1 assumes Linux, GCC, GNU Make, Python 3, and (for the investigation) `strace`, `gdb`, and GCC sanitizers.

Start with [Week 1](assignments/week-01-toolchain/README.md).

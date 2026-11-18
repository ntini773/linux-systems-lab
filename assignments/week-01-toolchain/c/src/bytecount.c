#include <stdint.h>
#include <stdio.h>

/*
 * Week 1 assignment:
 * Implement ./bytecount PATH.
 *
 * Contract:
 *   - exactly one path argument
 *   - count bytes (not characters or lines)
 *   - fixed-size buffer; do not load the whole file
 *   - uint64_t total with overflow detection
 *   - distinguish EOF from I/O error
 *   - check open/read/close failures
 *   - success: decimal count + newline on stdout, exit 0
 *   - failure: diagnostic on stderr, non-zero exit
 *
 * Read assignments/week-01-toolchain/README.md before editing.
 */

int main(int argc, char **argv)
{
    (void)argc;
    (void)argv;

    /*
     * TODO: replace this placeholder with your implementation.
     * The starter intentionally builds but does not pass the tests.
     */
    fputs("TODO: implement bytecount\n", stderr);
    return 2;
}

# Week 1 test suite

Run the acceptance suite from the assignment directory:

```sh
make clean all
make test
make sanitize
```

The Python tests invoke the binary at `build/bytecount`. The sanitizer target rebuilds that same path with AddressSanitizer and UndefinedBehaviorSanitizer before running the identical suite.

Add regression tests here when you discover and fix a defect. Keep test inputs byte-oriented so binary data is covered, not just text.

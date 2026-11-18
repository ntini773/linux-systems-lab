CC ?= gcc
PYTHON ?= python3

SRC := c/src/bytecount.c
BIN := build/bytecount
COMMON := -std=c17 -Wall -Wextra -Wpedantic -Werror -g
CFLAGS ?= -O0

.PHONY: all test sanitize clean

all: $(BIN)

$(BIN): $(SRC)
	@mkdir -p build
	$(CC) $(COMMON) $(CFLAGS) $< -o $@

test: all
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py' -v

sanitize:
	@mkdir -p build
	$(CC) $(COMMON) -O1 -fno-omit-frame-pointer -fsanitize=address,undefined $(SRC) -o build/bytecount-sanitize
	ASAN_OPTIONS=detect_leaks=1:halt_on_error=1 UBSAN_OPTIONS=halt_on_error=1 $(PYTHON) -m unittest discover -s tests -p 'test_*.py' -v

clean:
	rm -rf build

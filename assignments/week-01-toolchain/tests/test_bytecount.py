#!/usr/bin/env python3
import pathlib
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "build" / "bytecount"


class BytecountTests(unittest.TestCase):
    def run_file(self, data):
        with tempfile.NamedTemporaryFile() as source:
            source.write(data)
            source.flush()
            return subprocess.run(
                [str(PROGRAM), source.name],
                text=True,
                capture_output=True,
                check=False,
            )

    def assert_count(self, data, expected):
        result = self.run_file(data)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, f"{expected}\n")
        self.assertEqual(result.stderr, "")

    def test_empty_file(self):
        self.assert_count(b"", 0)

    def test_one_byte(self):
        self.assert_count(b"x", 1)

    def test_text_with_newline(self):
        self.assert_count(b"hello\n", 6)

    def test_binary_bytes(self):
        self.assert_count(bytes(range(256)), 256)

    def test_multiple_buffers(self):
        data = bytes(range(256)) * 8193
        self.assert_count(data, len(data))

    def test_no_argument(self):
        result = subprocess.run(
            [str(PROGRAM)], text=True, capture_output=True, check=False
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

    def test_too_many_arguments(self):
        result = subprocess.run(
            [str(PROGRAM), "one", "two"],
            text=True, capture_output=True, check=False
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

    def test_missing_path(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = pathlib.Path(directory) / "does-not-exist"
            result = subprocess.run(
                [str(PROGRAM), str(missing)],
                text=True, capture_output=True, check=False
            )
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""Negative-case tests for offline CSV fixture validation."""
import tempfile
import unittest
from pathlib import Path
from scripts.verify_offline import validate_csv, validate


class CSVValidationTests(unittest.TestCase):
    def check_bad(self, data, message):
        with tempfile.TemporaryDirectory() as dirname:
            file = Path(dirname) / "sample.csv"
            file.write_text(data, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, message):
                validate_csv(file)

    def test_normal_fixture(self):
        with tempfile.TemporaryDirectory() as dirname:
            file = Path(dirname) / "sample.csv"
            file.write_text("id,kind\n1,ok\n2,ok\n", encoding="utf-8")
            self.assertEqual(validate_csv(file), 2)

    def test_duplicate_header(self):
        self.check_bad("id,id\n1,2\n", "duplicate")

    def test_blank_header(self):
        self.check_bad("id, \n1,ok\n", "blank")

    def test_surplus_cells(self):
        self.check_bad("id,kind\n1,ok,unexpected\n", "expected 2")

    def test_missing_cells(self):
        self.check_bad("id,kind\n1\n", "expected 2")

    def test_blank_data(self):
        self.check_bad("id,kind\n1,\n", "blank field")

    def test_empty_dataset(self):
        self.check_bad("id,kind\n", "no records")

    def test_reject_nonexistent_root(self):
        with tempfile.TemporaryDirectory() as dirname:
            issues = validate(Path(dirname))
            self.assertTrue(any("Missing file" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()

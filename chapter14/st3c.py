# assertEqual需要else,因此使用assertRaisesRegex
import unittest


def parse_int(s):
    return int(s)


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaisesRegex(ValueError, 'invalid literal .*', parse_int, 'N/A')

    def test_bad_int2(self):
        with self.assertRaisesRegex(ValueError, 'invalid literal .*'):
            r = parse_int('N/A')
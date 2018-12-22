import unittest
from pyowm.utils import stringutils


class TestStringUtils(unittest.TestCase):

    def test_obfuscate_API_key(self):
        API_key = '22e28da2669c4283acdbd9cfa7dc0903'
        expected = '************************a7dc0903'

        self.assertEqual(expected, stringutils.obfuscate_API_key(API_key))
        self.assertIsNone(stringutils.obfuscate_API_key(None))

    def test_version_tuple_to_str(self):
        version_tuple = (1, 4, 6)
        expected = '1.4.6'
        result = stringutils.version_tuple_to_str(version_tuple)
        self.assertEqual(expected, result)
        version_tuple = (1, 4, 6, 9)
        separator = ';'
        expected = '1;4;6;9'
        result = stringutils.version_tuple_to_str(version_tuple, separator=separator)
        self.assertEqual(expected, result)

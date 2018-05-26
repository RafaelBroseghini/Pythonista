import unittest
from regexBeginner import *


class Tester(unittest.TestCase):
    def test_file_extension(self):
        self.assertEqual(file_extension("helloWorld.py"),".py")
        self.assertEqual(file_extension("package.json"),".json")
        self.assertNotEqual(file_extension("index.html"),".Html")
        self.assertNotEqual(file_extension("effects.css"),".CSS")

    def test_a3bs(self):
        self.assertTrue(aFollowedByThreeBs("aaabbbb"))
        self.assertTrue(aFollowedByThreeBs("ababababbbb"))
        self.assertFalse(aFollowedByThreeBs("ababababb"))
        self.assertFalse(aFollowedByThreeBs("abbabb"))

    

if __name__ == '__main__':
    unittest.main()
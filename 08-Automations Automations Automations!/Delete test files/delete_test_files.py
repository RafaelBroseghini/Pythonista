#!/usr/bin/env python

"""
This script gets rid of all the 'test' files that
you may have created and forgot about it.

For people starting out in programming it
is common to create 'test.*' files, for quick
dirty code. Maybe just checking if that
list comprehension works, maybe trying a new
control flow etc.
"""

import os
import re
import sys

__author__ = "Rafael Broseghini"
__credits__ = ["Rafael Broseghini"]
__version__ = "1.0.1"
__maintainer__ = "Rafael Broseghini"
__email__ = "rafaellopesbroseghini@gmail.com"
__status__ = "Prototype"


class TestFileEraser(object):
    PATH = os.getcwd()

    def __init__(self):
        self.all_files = os.listdir(self.PATH)

    def get_test_files(self, extension=sys.argv[1]) -> list:
        """
        Returns array with files starting with 'test'.
        If extension is specified, only files with that
        extension will be matched.
        """

        result = []
        pattern = "^test" + extension
        for file in self.all_files:
            if re.search(pattern, file) and not os.path.isdir(file):
                result.append(file)

        return result

    def delete_test_files(self, files_list=[]) -> None:
        """
        Deletes all 'test' files passed in files_list
        parameter.
        """
        for file in files_list:
            os.remove(file)


def main():
    t = TestFileEraser()
    test_files = t.get_test_files()
    t.delete_test_files(test_files)


if __name__ == "__main__":
    main()

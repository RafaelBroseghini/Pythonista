#!/usr/bin/env python

"""
Concatenates content of all files with specified
extension into one output file.
"""

import os
import sys
import re

__author__ = "Rafael Broseghini"
__credits__ = ["Rafael Broseghini"]
__version__ = "1.0.1"
__maintainer__ = "Rafael Broseghini"
__email__ = "rafaellopesbroseghini@gmail.com"
__status__ = "Prototype"


class FileConcatenator(object):
    PATH = os.getcwd()
    
    def __init__(self):
        """
        Initialize class member to a list with all
        files and directories within current path.
        """
        self.file_list = os.listdir(self.PATH)

    def get_files_with_extension(self, extension=sys.argv[1]) -> list:
        """
        Gets all files from current path with specified
        extension. If no extension is provided, returns
        an error.
        """
        if extension == "":
            raise EnvironmentError("No extension provided!")

        result = []
        for idx, file in enumerate(self.file_list):
            if re.search(extension+"$",file):
                result.append(file)
        
        if len(result) == 0:
            raise Exception("No {} files found.".format(extension))

        return result

    def write_to_master_file(self, all_files=[], filename=sys.argv[2], separator=sys.argv[3]) -> None:
        """
        Writes content of all found files with extension
        to a single source name passed as command line argument
        by the user.
        """
        if filename == "":
            raise EnvironmentError("No filename provided!")

        first_file = all_files[0]

        with open(filename, "w+") as master:
            with open(first_file, "r+") as initial_write:
                for line in initial_write:
                    master.write(line)

                if len(all_files) > 1:
                    for i in range(1, len(all_files)):
                        master.write(separator)
                        with open(all_files[i], "r+") as file_to_append:
                            for line in file_to_append:
                                master.write(line)


def main():
    a = FileConcatenator()
    all_found_files = a.get_files_with_extension() 
    a.write_to_master_file(all_found_files)

if __name__ == '__main__':
    main()
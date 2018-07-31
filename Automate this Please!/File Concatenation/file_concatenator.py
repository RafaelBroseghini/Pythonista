import os
import re

class FileConcatenator(object):
    PATH = os.getcwd()
    
    def __init__(self):
        self.file_list = os.listdir(self.PATH)
        # self.files_with_extension = []

    def get_files_with_extension(self, extension=None):
        if extension == None:
            raise EnvironmentError("No extension provided!")

        result = []
        for idx, file in enumerate(self.file_list):
            if re.search(extension+"$",file):
                result.append(file)
        return result

    def write_to_master_file(self, filename=None, all_files=[], separator=""):
        if filename == None:
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
    all_files_txt = a.get_files_with_extension(".txt") 
    a.write_to_master_file("theConcatenation.txt", all_files_txt,"\n")

if __name__ == '__main__':
    main()
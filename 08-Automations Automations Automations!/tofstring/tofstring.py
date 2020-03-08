import re


def read_file(filename: str) -> list:
    with open(filename, "r+") as infile:
        lines = [x.strip() for x in infile.readlines()]
    return lines


def parse_lines(lines: list) -> list:
    for i in range(len(lines)):
        patt = r"[\"\'](.*)[\"\']"
        match = re.search(patt, lines[i])
        if match:
            # match format
            content = match.groups(0)
            # print(content[0])
            # substitute content in string for empty string
            new_line = re.sub(content[0], "", lines[i])
            # print(new_line)
            format_match = re.search(r"\.format\((.*)\)$", new_line)
            if format_match:
                vals = [
                    "{" + x + "}" for x in format_match.groups(0)[0].split(",")]
                print(re.sub("{}", vals, lines[i]))
                # re.


def main():
    lines = read_file("training.py")
    # parse_lines(lines)
    print("{}".format("{}".format("a")), "{}".format("b"))


if __name__ == "__main__":
    main()

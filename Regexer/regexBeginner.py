import re

def file_extension(file):
    pattern = re.compile(r"(\.\w+$)")
    match = pattern.search(file)
    print("Input file: \033[1;32m{}\033[0m".format(file))
    print("Extension: ", end="")
    return match.group()

def hexadecimal(word):
    pattern = re.compile(r"(^[ABCDEF]+$)")
    match = pattern.search(word)
    print("Input string: \033[1;32m{}\033[0m".format(word))
    print("Is hexadecimal? ", end="")
    return bool(match)

def aFollowedByThreeBs(word):
    pattern = re.compile(r"[a|A][b|B]{3}")
    match = pattern.search(word)
    print("Input string: \033[1;32m{}\033[0m".format(word))
    print("A3B's? ", end="")
    return bool(match)

def substituteSpaceForUnderscore(word):
    pattern = re.compile(r"\s")
    match = pattern.sub("_", word)
    print("Input string: \033[1;32m{}\033[0m".format(word))
    print("After Space2Underscore substitution => ", end="")
    return match

def isValidFraction(fraction):
    pattern = re.compile(r"^[1-9][0-9]*\/[1-9][0-9]*")
    match = pattern.search(str(fraction))
    print("Input Fraction: \033[1;32m{}\033[0m".format(fraction))
    print("Valid fraction? ", end="")
    return bool(match)


def displayOutput():
    print("\nUsing Regular Expressions!\n")
    print("\033[1;31mFile extension capturer:\033[0m")
    print("="*30)
    print(file_extension("structures.py")+"\n")
    print(file_extension("utftokenizer.tar.gz")+"\n")
    print("\033[1;31mHexadecimal word:\033[0m")
    print("="*30)
    print("{}\n".format(hexadecimal("BABACADEFAFACADE")))
    print("{}\n".format(hexadecimal("babacadefafacade")))
    print("{}\n".format(hexadecimal("BABACADEFAFACASE")))
    print("\033[1;31mA followed by Three B's (not case sensitive):\033[0m")
    print("="*30)
    print("{}\n".format(aFollowedByThreeB("abbaabbba")))
    print("{}\n".format(aFollowedByThreeB("aaaABbaABABABABa")))
    print("{}\n".format(aFollowedByThreeB("AbBb")))
    print("\033[1;31mSubstituting spaces for underscores:\033[0m")
    print("="*30)
    print("{}\n".format(substituteSpaceForUnderscore("I like to beep_bop")))
    print("{}\n".format(substituteSpaceForUnderscore("my name is John Doe")))
    print("{}\n".format(substituteSpaceForUnderscore("Ninja mode from now         on")))
    print("="*30)
    print("{}\n".format(isValidFraction("0/3")))
    print("{}\n".format(isValidFraction("11/32")))
    print("{}\n".format(isValidFraction("9/184")))

def main():
    displayOutput()

if __name__ == "__main__":
    main()


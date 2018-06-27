import unittest

def make_string(inp_str):
    if len(inp_str) < 2:
        return ""
    else:
        new_str = ""
        first, second, one_before_last, last = inp_str[0], inp_str[1], inp_str[len(inp_str)-2], inp_str[-1]
        new_str = "{}{}{}{}".format(first, second, one_before_last, last)
        return new_str

def change_first_char(inp_str):
    first_char = inp_str[0]
    inp_str = list(inp_str)
    for char in range(1,len(inp_str)):
        if inp_str[char] == first_char:
            inp_str[char] = "$"

    return "".join(inp_str)

def translate_to_pirate(inp_str):

    # NOTE: Should think about constraints if word is upper case or not. Separated by , or not etc.

    pirate_dict = {"sir":"matey","hotel":"fleabag inn","student":"swabbie",
    "boy":"matey","madam":"proud beauty",
    "professor":"foul blaggart","restaurant":"galley",
    "your":"yer","excuse":"arr","students":"swabbies",
    "are":"be","lawyer":"foul blaggart","the":"th’","restroom":"head",
    "my":"me","hello":"avast","is":"be","man":"matey"}

    # NOTE: Some constraints.
    inp_str = inp_str.replace(",","").replace(".",".").replace("|","").split()

    for i in range(len(inp_str)):
        if inp_str[i].lower() in pirate_dict:
            inp_str[i] = pirate_dict[inp_str[i].lower()]

    inp_str = " ".join(inp_str)

    return inp_str.lower()


class Tester(unittest.TestCase):
    def test_checkMakeString(self):
        self.assertEqual(make_string("rafaelbroseghini"),"rani")
        self.assertNotEqual(make_string("rafaelbroseghini"),"reni")

    def test_change_first_char(self):
        self.assertEqual(change_first_char("rafaelrararra"),"rafael$a$a$$a")


if __name__ == '__main__':
    unittest.main()

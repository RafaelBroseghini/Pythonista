EOF = 3
digits = set(list("0123456789"))
lettersdigitsunderscore = set(
    list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789"))
letters = set(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
ws = set(list(" \t\n\r"))
badidentifiertoken = 1
notAChar = 2


class StreamReader:

    def __init__(self, instream):
        self.instream = instream
        self.nextChars = ""
        self.EOF = False
        self.line = 1
        self.column = 0
        self.charsRead = 0

    def readChar(self):

        if len(self.nextChars) > 0:
            nextChar = self.nextChars[0]
            self.nextChars = self.nextChars[1:]

        else:
            nextChar = self.instream.read(1)

        if nextChar == "":
            nextChar = chr(EOF)

        elif nextChar == '\n':
            self.line += 1
            self.column = 0

        else:
            self.column += 1

        if nextChar == chr(EOF):
            self.EOF = True

        self.charsRead += 1

        return nextChar

    def unreadChar(self, ch):
        if len(ch) == 0:
            return

        if len(ch) != 1:
            raise Exception(notAChar)

        self.EOF = False

        self.nextChars = ch + self.nextChars

        if ch == '\n':
            self.line -= 1
        else:
            self.column -= 1

        self.charsRead -= 1

    def numCharsRead(self):
        # return the number of characters read. This is useful when backtracking is performed
        # in case no progress is being made in reading the stream.
        return self.charsRead

    def eof(self):
        return self.EOF

    def readUpTo(self, delimiter):
        result = ""

        done = False

        while not done and not self.eof():

            c = self.readChar()

            if not self.eof():
                result += c

            if result[-len(delimiter):] == delimiter:
                done = True

        return result

    def readInt(self):
        number = ""

        self.skipWhiteSpace()

        digit = self.readChar()

        while digit in digits:
            number += digit
            digit = self.readChar()

        self.unreadChar(digit)

        return int(number)

    def readIdentifier(self):
        id = ""

        self.skipWhiteSpace()

        c = self.readChar()

        if not c in letters:
            print("Bad identifier token found in source file starting with",
                  c, "at line", self.line, "and column", self.column)
            raise Exception(badidentifiertoken)

        while c in lettersdigitsunderscore:
            id += c
            c = self.readChar()

        self.unreadChar(c)

        return id

    def skipWhiteSpace(self):
        c = self.readChar()

        while c in ws:
            c = self.readChar()

        self.unreadChar(c)

    def peek(self, value):
        # Skip white space, then look for the value as the next characters in the input file.
        # Remember the read characters, but return true if they are found and
        # false otherwise.

        readChars = ""

        self.skipWhiteSpace()

        done = False

        while len(readChars) < len(value) and not done:
            c = self.readChar()
            if c == EOF:
                done = True
            else:
                readChars += c

        for i in range(len(readChars) - 1, -1, -1):
            self.unreadChar(readChars[i])

        if readChars == value:
            return True

        return False

    def skipComments(self):
        # skip comments

        while self.peek("(*"):
            self.readUpTo("*)")

    def getLineNumber(self):
        return self.line

    def getColNumber(self):
        return self.column

    def getToken(self):
        self.skipWhiteSpace()
        c = self.readChar()

        if c in digits:
            self.unreadChar(c)
            return self.readInt()

        if c in letters:
            self.unreadChar(c)
            return self.readIdentifier()

        return c

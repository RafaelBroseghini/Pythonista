import calcscanner
import calcparser
import sys
import io


def main():

    # strm = sys.stdin
    strm = io.StringIO("457+300+300;")
    theScanner = calcscanner.calcScanner(strm)

    """while True:
        tokenId, lex = theScanner.getToken()
        print(tokenId,lex)
        if tokenId == 10:
            return"""

    theParser = calcparser.calcParser()
    ast = theParser.parse(theScanner)


if __name__ == "__main__":
    main()

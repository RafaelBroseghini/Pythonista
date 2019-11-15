#!/usr/bin/env python

"""
Implementation of the conversion from infix
to postfix notation using a stack.
"""

from pythonds.basic.stack import Stack


def convert(expression: str) -> str:
    expression = list(expression)
    output = []
    opstack = Stack()
    precedence = {"(": 1, "-": 2, "+": 2, "/": 3, "*": 3}
    for token in expression:
        if token in "ABCD":
            output.append(token)

        elif token == "(":
            opstack.push(token)

        elif token == ")":
            topElement = opstack.pop()
            while topElement != "(":
                output.append(topElement)
                topElement = opstack.pop()

        elif token in precedence:
            lowerPrec = False
            while opstack.size() > 1 and not lowerPrec:
                if (
                    opstack.peek() in precedence
                    and precedence[opstack.peek()] >= precedence[token]
                ):
                    output.append(opstack.pop())
                else:
                    lowerPrec = True
            opstack.push(token)

    while not opstack.isEmpty():
        output.append(opstack.pop())
    return " ".join(output)


def main():
    print(convert("(A+B)*(C+D)"))


if __name__ == "__main__":
    main()

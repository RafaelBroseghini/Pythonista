import re


def abbreviate(word):
    pattern = re.compile(r"\b\w|[A-Z]")
    match = pattern.findall(word)
    return "".join(match).upper()


def normalize_whitespace(word):
    pattern = re.compile(r"\s+")
    match = pattern.sub(" ", word)
    return match


def main():
    print(abbreviate("Graphics Interchange Format"))
    print(abbreviate("JavaScript Object Notation"))
    print(abbreviate("content management system"))
    print(abbreviate("frequently asked questions"))
    print("=" * 30)
    print(
        normalize_whitespace(
            """Hold          fast to dreams 
    For if dreams die Life is a broken-winged
                            bird That cannot fly. Hold fast to dreams For                   
    when dreams go Life is         a barren field Frozen with snow."""
        )
    )


if __name__ == "__main__":
    main()

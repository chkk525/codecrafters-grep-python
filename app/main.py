import sys
import re
# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == '\d':
        return any(char.isdigit() for char in input_line)
    elif pattern == '\w':
        return any(char.isalpha() or char.isdigit() for char in input_line)
    elif re.search("\[^\w+?\]", pattern):
        chars = re.search("\[(.+?)\]", pattern).group(1)
        return not (any((char in input_line) for char in chars))
    elif re.search("\[\w+?\]", pattern):
        chars = re.search("\[(.+?)\]", pattern).group(1)
        return any((char in input_line) for char in chars)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()

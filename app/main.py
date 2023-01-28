import math
import sys
# import re
# import pyparsing - available if you need it!
# import lark - available if you need it!


def find_first_match_index(input_line: str, pattern: str) -> int:
    """
    Finds the index of the first match of the given pattern in the input_line.
    If no match is found, returns -1.

    Parameters:
        input_line (str): The text to search in.
        pattern (str): The pattern to search for.

    Returns:
        int: The index of the first match, or -1 if no match is found.
    """
    if pattern in ('\\d', '\\w'):
        for i, char in enumerate(input_line):
            if (pattern == '\\d' and char.isdigit()) or (pattern == '\\w' and (char.isalpha() or char.isdigit())):
                return i+1
    elif pattern[0] == '[' and pattern[-1] == ']':
        if pattern[1] == '^':
            negative_pattern = pattern[2:-1]
            if any(c in input_line for c in negative_pattern):
                return -1
            else:
                return 0
        else:
            positive_pattern = pattern[1:-1]
            for c in positive_pattern:
                idx = input_line.find(c)
                if idx != -1:
                    return idx+1
    else:
        idx = input_line.find(pattern)
        if idx >= 0:
            return idx+1

    return -1


def match_pattern_sequence(input_line: str, pattern: str) -> bool:
    """
    Check if input_line matches pattern. This method is called recursively.

    Parameters:
        input_line (str): Text to check.
        pattern (str): patterns.

    Returns:
        bool: True if input_line matches pattern, False otherwise.
    """

    while pattern:
        if pattern[0] == '\\':
            pt, pattern = pattern[:2], pattern[2:]
        elif pattern[0] == '[':
            closing_index = pattern.find(']') + 1
            if closing_index == 0:
                raise ValueError('Closing not found')
            pt, pattern = pattern[:closing_index], pattern[closing_index:]
        else:
            pt, pattern = pattern[:1], pattern[1:]

        input_start_pos = find_first_match_index(input_line, pt)

        if input_start_pos < 0:
            return False
        input_line = input_line[input_start_pos:]

    # Return True once whole pattern is checked without returning False
    return True


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if match_pattern_sequence(input_line, pattern):
        exit(0)
    else:
        exit(1)


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if match_pattern_sequence(input_line, pattern):
        exit(0)
    else:

        exit(1)


if __name__ == "__main__":
    main()

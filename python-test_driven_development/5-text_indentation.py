"""
This module provides a function for text formatting.
It handles newlines specifically for punctuation marks.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each: ., ? and :
    There should be no space at the beginning or end of each line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special = (".", "?", ":")
    i = 0
    text = text.strip()

    while i < len(text):
        print(text[i], end="")
        if text[i] in special:
            print()
            print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

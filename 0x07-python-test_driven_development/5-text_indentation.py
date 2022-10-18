#!/usr/bin/python3


def text_indentation(text):
    """
    Args: Prints a text with 2 new lines after each of these character . ? and :
     There should be no space at the beginning or at the end of each printed line.
        :param text: the text to print (a string).

    Raises: TypeError - If text is not a string.
    """
    special = ['.', '?', ':']
    if type(text) != str:
        raise TypeError("text must be string")
    for i in text:
        print(i, end='')
        if i in special:
            print('\n\n', end='')

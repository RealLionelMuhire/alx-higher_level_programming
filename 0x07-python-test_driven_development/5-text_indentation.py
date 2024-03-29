#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?' and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
        """ 
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    lines = []
    current_line = ""
    for char in text:
        current_line += char
        if char in punctuations:
            lines.append(current_line.strip())
            lines.append("")  # Add two new lines
            current_line = ""

    if current_line:
        lines.append(current_line.strip())

    for line in lines:
        print(line)

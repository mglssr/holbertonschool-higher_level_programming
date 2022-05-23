#!/usr/bin/python3
""" Task 5 - Text identation """


def text_indentation(text):
    """function that prints a text with 2 new\
    lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text1 = text.replace(". ",".\n\n")
    text2 = text1.replace(": ",":\n\n")
    text3 = text2.replace("? ","?\n\n")
    print(f"{text3}", end="")

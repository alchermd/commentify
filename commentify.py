#! /usr/bin/python3.5
"""" Transform your plaintext into a comment. """
import sys
import pyperclip


def commentify(lang):
    """ Grabs the text from the clipboard and transforms it into comments.
    lang -> A string that signifies the programming language to base
    the comment format.
    """
    plaintext = pyperclip.paste().split('\n')

    if lang == 'python':
        comment = ['###\n']
        char = ' # '
        end = '###\n'

    else:
        comment = ['/*\n']
        char = ' * '
        end = '*/\n'

    for line in plaintext:
        comment.append(char + line + '\n')

    comment.append(end)
    return ''.join(comment)


def main():
    """ Main method of the program. Ensures proper usage
    and calls the commentify function. """
    if len(sys.argv) > 2:
        print('Usage: commentify [language]')
        sys.exit(1)
    language = sys.argv[1] if len(sys.argv) > 1 else 0
    pyperclip.copy(commentify(language))


if __name__ == '__main__':
    main()

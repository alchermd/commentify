#! /usr/bin/python3.5
"""" Transform your plaintext into a comment. """
import sys
import pyperclip


def commentify(lang):
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
    if len(sys.argv) > 2:
        print('Usage: commentify [language]')
        sys.exit(1)
    language = sys.argv[1] if len(sys.argv) > 1 else 0
    pyperclip.copy(commentify(language))


if __name__ == '__main__':
    main()

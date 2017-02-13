#! /usr/bin/python3.5
# Transform your plaintext into a comment.

import sys
import pyperclip

def commentify():
    plaintext = pyperclip.paste()
    plaintext = plaintext.split('\n')

    comment = ['/*\n']
    for line in plaintext:
        comment.append(' * ' + line + '\n')

    comment.append('*/')
    return ''.join(comment)

def main():
    if len(sys.argv) != 1:
        print('Usage: commentify')
        sys.exit(1)

    pyperclip.copy(commentify())

main()

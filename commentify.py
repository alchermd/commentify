#! /usr/bin/python3.5
# Transform your plaintext into a comment.

import sys, pyperclip

if len(sys.argv) != 1:
    print('Usage: commentify')

plaintext = pyperclip.paste()
plaintext = plaintext.split('\n')

comment = '/*\n'
for line in plaintext:
    comment += ' * ' + line + '\n'

comment += '*/'
pyperclip.copy(comment)

# Commentify

Transform your plaintext into programming-friendly comment syntax.

## Update (2018)

This is one of my earlier programs that I used intensively. I didn't know much about IDE's and text editors back then, so it's funny to see how all of what the program does can be done with a simple `CTRL + /`. Thanks for reading!

## Usage

```
$ # Copy your plaintext into the clipboard
$ chmod +x commentify.py [language]
$ ./commentify.py
$ # Your comment is now ready for pasting!
```

## Language Support

1.) C style multi-line comments

```
$  #This is the default behaviour
$ ./commentify.py
# Result:
/*
 * Foo
 * Bar
 * Baz
*/
```    

2.) Python
```
$ ./commentify.py python
# Result:
###
 # Foo
 # Bar
 # Baz
###
```

## Dependencies

`commentify` requires `Python3.5` and the `pyperclip` module. 

Linux users should get a copy/paste mechanism for `commentify` to work. [Instructions here](https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error)

## Credits

* [Automate the Boring Stuff with Python](https://www.automatetheboringstuff.com) for the idea.

## License

The code in this repository is under the following license(s):

* MIT

# Commentify

Transform your plaintext into programming-friendly comment syntax.

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

`Commentify` requires `Python3.5` and the `pyperclip` module.

## Credits

* [Automate the Boring Stuff with Python](https://www.automatetheboringstuff.com) for the idea.

## License

The code in this repository is under the following license(s):

* MIT

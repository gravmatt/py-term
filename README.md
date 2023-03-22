# pyterm

Python 3 package to easily handle style terminal output, moving and positioning the cursor and some other features.
This project is heavily based on [gravmatt/py-term](https://github.com/gravmatt/py-term]github.com) project.

## Installation

Install through **pip**.

```shell
$ pip3 install git+https://github.com/havocesp/pyterm
```

or get from source

```shell
$ git clone https://github.com/havocesp/pyterm
$ cd pyterm
$ python3 setup.py install
```

## Import module

Import the module into your python project.

```python3
from pyterm import Term as Tm
```

## Usage

```python
from pyterm import Term as Tm

Tm.write('Hello, ')
Tm.write('Python!')

> Hello, Python!

Tm.write_line('Hello')
Tm.write_line('Python!')

> Hello
> Python!
```

## Style output

The first argument is the text output and all following arguments are for styling.

```python3
from pyterm import Term as Tm

Tm.write_line('text', Tm.BOLD)

text = Tm.style('text', Tm.DIM)
Tm.write_line(text)
```

### Usage

```python
from pyterm import Term as Tm

Tm.write_line('Hello, Python!')

Tm.write_line('This text line will be green', Tm.GREEN)

Tm.write_line('Reverse the green color', Tm.GREEN, Tm.REVERSE)
```

Or

```
output = term.format('Hello, ', term.green) + term.format('Python!', term.blue, term.bold)

term.write_line(output)

term.write(term.format('All in one line', term.reverse))
```

#### Text align

**Center align**

```
# term.textCenter(text)

term.write_line(term.textCenter('Super Python!'))
```

**Right align**

```
# term.text_right(text)

term.write_line(term.text_right('Rene Tanczos (@gravmatt)'))

( Function term.right() to align text is depricated because of naming conflicts! )
```

##### Style attributes

| Code                  | Description                          |
| :-------------------- | :----------------------------------- |
| term.off        | All attributes off                   |
| term.bold       | Bold                                 |
| term.dim        | Dim                                  |
| term.underscore | Underscore (monochrome display only) |
| term.blink      | Blink                                |
| term.reverse    | Reverse                              |
| term.hide       | Hide                                 |

##### Text color

| Code               | Color       |
| :----------------- | :---------- |
| term.black   | Black       |
| term.red     | Red         |
| term.green   | Green       |
| term.yellow  | Yellow      |
| term.blue    | Blue        |
| term.magenta | Magenta     |
| term.cyan    | Cyan        |
| term.white   | White       |

##### Background color

| Code                 | Color       |
| :------------------- | :---------- |
| term.bgblack   | Black       |
| term.bgred     | Red         |
| term.bggreen   | Green       |
| term.bgyellow  | Yellow      |
| term.bgblue    | Blue        |
| term.bgMagenta | Magenta     |
| term.bgcyan    | Cyan        |
| term.bgwhite   | White       |

## Remove style attributes

Removes style characters.

(Good to call before you count a string)
```
term.strip(formatted_text)

hello = term.red + 'hello, world' + term.off
print hello
# '\x1b[31mhello, world\x1b[0m\x1b[27m'

print term.strip(hello)
# hello, world
```

## Highlighting text

Simple highlighting of unformatted text strings
```
def callback(matching_text):
  return term.blue + matching_text + term.off

output, match_count, array_of_positions = term.highlight(regex_pattern, text, callback)
```

Return a tuple.

output (index 0) = formatted text output

match_count (index 1) = match count of the pattern

array_of_positions (index 2) = array of tuples with start and stop points of the matches [(4, 6), (9, 11), ..]

## Set title

```
term.set_title('Hello Terminal')

# or clear it

term.clear_title()
```

## Set tab name

```
term.set_tab('Hello Tab')

# or clear it

term.clear_tab()
```

## Cursor position

Move the cursor to a specific position.
```
term.pos(line, column)

term.pos(2, 15)
```

Get the size of the terminal (lines and columns)

```
(30, 100) = term.get_size()

# (lines, colums) = term.get_size()
```

Move the cursor to the home position (1, 1).

```
term.homePos()
```

Moves the current cursor position up, down, left or right by the specified value.

```
term.up(value=1)
term.down(value=1)
term.left(value=1)
term.right(value=1)
```

Saves the current cursor position.

```
term.save_cursor()
```

Restore the previously stored cursor position.

```
term.restore_cursor()
```

Clear the terminal screen.

```
term.clear()
```

Clear the entire line on the current cursor position.

```
term.clear_line()
```

Clear line from the current cursor position to the end.

```
term.clear_line_from_pos()
```

Clear line from begin to current cursor position.

```
term.clear_line_to_pos()
```

## Licence

The MIT License (MIT)

Copyright (c) 2015-2021 René Tanczos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

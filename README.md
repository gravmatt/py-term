# pyTerminal
Python module to style terminal output, moving and positioning the cursor.

## Install
```
cd <path to your project>
git clone https://github.com/gravmatt/pyTerminal.git
```

## Import module
Import the module into your python project.
```
import pyTerminal
```

## Usage
```
pyTerminal.write('Hello')
pyTerminal.write(',Python!')

> Hello, Python!

pyTerminal.writeLine('Hello')
pyTerminal.writeLine('Python!')

> Hello
> Python!
```

## Style output

The first argument is the text output and all following arguments are for styling.
```
pyTerminal.writeLine(text, *style)
```
### Usage
```
pyTerminal.writeLine('Hello, Pyhton!')

pyTerminal.writeLine('This text line will be green', pyTerminal.green)

pyTerminal.writeLine('Reverse the green color', pyTerminal.green, pyTerminal.reverse)
```

##### Style attributes

| Code                  | Description                          |
| :-------------------- | :----------------------------------- |
| pyTerminal.off        | All attributes off                   |
| pyTerminal.bold       | Bold                                 |
| pyTerminal.dim        | Dim                                  |
| pyTerminal.underscore | Underscore (monochrome display only) |
| pyTerminal.blink      | Blink                                |
| pyTerminal.reverse    | Reverse                              |
| pyTerminal.hide       | Hide                                 |

##### Text color

| Code               | Color       |
| :----------------- | :---------- |
| pyTerminal.black   | Black       |
| pyTerminal.red     | Red         |
| pyTerminal.Green   | Green       |
| pyTerminal.yellow  | Yellow      |
| pyTerminal.blue    | Blue        |
| pyTerminal.magenta | Magenta     |
| pyTerminal.cyan    | Cyan        |
| pyTerminal.white   | White       |

##### Background color

| Code                 | Color       |
| :------------------- | :---------- |
| pyTerminal.bgblack   | Black       |
| pyTerminal.bgred     | Red         |
| pyTerminal.bggreen   | Green       |
| pyTerminal.bgyellow  | Yellow      |
| pyTerminal.bgblue    | Blue        |
| pyTerminal.bgMagenta | Magenta     |
| pyTerminal.bgcyan    | Cyan        |
| pyTerminal.bgwhite   | White       |


## Cursor position

Move the cursor to a specific position.
```
pyTerminal.pos(line, column)

pyTerminal.pos(2, 15)
```

Move the cursor to the home position (1, 1).
```
pyTerminal.homePos()
```

Moves the current cursor position up, down, left or right by the specified value.
```
pyTerminal.up(value=1)
pyTerminal.down(value=1)
pyTerminal.left(value=1)
pyTerminal.right(value=1)
```

Saves the current cursor position.
```
pyTerminal.saveCursor()
```

Restore the previously stored cursor position.
```
pyTerminal.restoreCursor()
```

Clear the terminal screen.
```
pyTerminal.clear()
```

Clear the entire line on the current cursor position.
```
pyTerminal.clearLine()
```

Clear line from the current cursor position to the end.
```
pyTerminal.clearLineFromPos()
```

Clear line from begin to current cursor position.
```
pyTerminal.clearLineToPos()
```

## Licence

The MIT License (MIT)

Copyright (c) 2015 René Tanczos

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

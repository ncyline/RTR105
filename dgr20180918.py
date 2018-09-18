Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __builtins__
<module '__builtin__' (built-in)>
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print__builtins__.__doc__

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print__builtins__.__doc__
NameError: name 'print__builtins__' is not defined
>>> print __builtins__.__doc__
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> print __builtins__.abs.__doc__
abs(number) -> number

Return the absolute value of the argument.
>>> abs(10)
10
>>> abs(-10)
10
>>> a = 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> a = 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 20, '__package__': None}
>>> a * b

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a * b
NameError: name 'b' is not defined
>>> a.__NameError: name 'b' is not defined
SyntaxError: invalid syntax
>>> a.__doc__
"int(x=0) -> int or long\nint(x, base=10) -> int or long\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is floating point, the conversion truncates towards zero.\nIf x is outside the integer range, the function returns a long instead.\n\nIf x is not a number or if base is given, then x must be a string or\nUnicode object representing an integer literal in the given base.  The\nliteral can be preceded by '+' or '-' and be surrounded by whitespace.\nThe base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to\ninterpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
>>> type(a)
<type 'int'>
>>> b = 1.5
>>> vars()
{'a': 20, 'b': 1.5, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> b.__doc__
'float(x) -> floating point number\n\nConvert a string or number to a floating point number, if possible.'
>>> type(b)
<type 'float'>
>>> c = d

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c = d
NameError: name 'd' is not defined
>>> c = "D"
>>> print c.__doc__
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
>>> type(c)
<type 'str'>
>>> burts = "R"
>>> ord(R)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    ord(R)
NameError: name 'R' is not defined
>>> ord(burts)
82
>>> hex(ord(burts))
'0x52'
>>> bin(ord(burts))
'0b1010010'
>>> 

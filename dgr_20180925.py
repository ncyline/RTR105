Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input ("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: "
       10
       
SyntaxError: invalid syntax
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainīgais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
SyntaxError: invalid syntax
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 10
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 20
>>> vars()
{'mans_mainiigais': 20, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainiigais)
<type 'int'>
>>> 
>>> 
>>> vars()
{'mans_mainiigais': 20, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 8
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 7
>>> vars()
{'mans_mainiigais': 7, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', '__package__': None, 'x': 49, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 89
mans_mainiigais = 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 112

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 5, in <module>
    print("mans_mainiigais =&d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais =&d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais =&d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais =&d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print ("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print ("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print ("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print ("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12
mans_mainiigais = 12
respektīvi, Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12
mans_mainiigais =     12.000
respektīvi, Tu esi ievadījis skaitli:    12.0000
vēl atmiņā tagad ir arī mainīgais x =     144.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 6.4567
mans_mainiigais =      6.457
respektīvi, Tu esi ievadījis skaitli:     6.4567
vēl atmiņā tagad ir arī mainīgais x =      41.6889749
>>> type(mans_mainiigais)
<type 'float'>
>>> type(x)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simbolu rindu: 21

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 2, in <module>
    x = mans_mainiigais * mans_mainiigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simbolu rindu: dddd
mans_mainiigais = dddd
respektīvi, Tu esi ievadījis skaitli: dddd
>>> 
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input ("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: "
       10
       
SyntaxError: invalid syntax
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainīgais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
SyntaxError: invalid syntax
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 10
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 20
>>> vars()
{'mans_mainiigais': 20, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainiigais)
<type 'int'>
>>> 
>>> 
>>> vars()
{'mans_mainiigais': 20, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 8
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 7
>>> vars()
{'mans_mainiigais': 7, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', '__package__': None, 'x': 49, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 89
mans_mainiigais = 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 112

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 5, in <module>
    print("mans_mainiigais =&d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais =&d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais =&d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais =&d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print ("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print ("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print ("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print ("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12
mans_mainiigais = 12
respektīvi, Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12
mans_mainiigais =     12.000
respektīvi, Tu esi ievadījis skaitli:    12.0000
vēl atmiņā tagad ir arī mainīgais x =     144.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 6.4567
mans_mainiigais =      6.457
respektīvi, Tu esi ievadījis skaitli:     6.4567
vēl atmiņā tagad ir arī mainīgais x =      41.6889749
>>> type(mans_mainiigais)
<type 'float'>
>>> type(x)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simbolu rindu: 21

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 2, in <module>
    x = mans_mainiigais * mans_mainiigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simbolu rindu: dddd
mans_mainiigais = dddd
respektīvi, Tu esi ievadījis skaitli: dddd
>>> 
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input ("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: "
       10
       
SyntaxError: invalid syntax
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainīgais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
SyntaxError: invalid syntax
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 10
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 20
>>> vars()
{'mans_mainiigais': 20, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainiigais)
<type 'int'>
>>> 
>>> 
>>> vars()
{'mans_mainiigais': 20, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 8
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 7
>>> vars()
{'mans_mainiigais': 7, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', '__package__': None, 'x': 49, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 89
mans_mainiigais = 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 112

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 5, in <module>
    print("mans_mainiigais =&d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais =&d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais =&d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais =&d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print ("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print ("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 1, in <module>
    mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print ("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 6, in <module>
    print ("mans_mainiigais = &d"%(mans_mainiigais))
TypeError: not all arguments converted during string formatting
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12
mans_mainiigais = 12
respektīvi, Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 12
mans_mainiigais =     12.000
respektīvi, Tu esi ievadījis skaitli:    12.0000
vēl atmiņā tagad ir arī mainīgais x =     144.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 6.4567
mans_mainiigais =      6.457
respektīvi, Tu esi ievadījis skaitli:     6.4567
vēl atmiņā tagad ir arī mainīgais x =      41.6889749
>>> type(mans_mainiigais)
<type 'float'>
>>> type(x)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simbolu rindu: 21

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 2, in <module>
    x = mans_mainiigais * mans_mainiigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simbolu rindu: dddd
mans_mainiigais = dddd
respektīvi, Tu esi ievadījis skaitli: dddd
>>> 


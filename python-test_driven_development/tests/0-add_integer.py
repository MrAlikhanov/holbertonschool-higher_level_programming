======================================
Test suite for 0-add_integer module
======================================

>>> add_integer = __import__('0-add_integer').add_integer

Testing normal addition:
>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98

Testing default b=98:
>>> add_integer(2)
100

Testing floats (should be casted to ints):
>>> add_integer(100.3, -2)
98
>>> add_integer(10.9, 10.9)
20

Testing wrong types (strings, None):
>>> add_integer(4, "School")
Traceback (most recent call last):
    ...
TypeError: b must be an integer

>>> add_integer("Hello", 4)
Traceback (most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer(None)
Traceback (most recent call last):
    ...
TypeError: a must be an integer

Testing float overflow:
>>> add_integer(float('inf'))
Traceback (most recent call last):
    ...
OverflowError: cannot convert float infinity to integer

Testing float NaN:
>>> add_integer(float('nan'))
Traceback (most recent call last):
    ...
ValueError: cannot convert float NaN to integer

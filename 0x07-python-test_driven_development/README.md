0. Integers addition
mandatory
Write a function that adds 2 integers.

Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
You are not allowed to import any module

1. Divide a matrix
mandatory
Write a function that divides all elements of a matrix.

Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal places
Returns a new matrix
You are not allowed to import any module

2. Say my name
mandatory
Write a function that prints My name is <first name> <last name>

Prototype: def say_my_name(first_name, last_name=""):
first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
You are not allowed to import any module

3. Print square
mandatory
Write a function that prints a square with the character #.

Prototype: def print_square(size):
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
You are not allowed to import any module

4. Text indentation
mandatory
Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with the message text must be a string
There should be no space at the beginning or at the end of each printed line
You are not allowed to import any module

5. Max integer - Unittest
mandatory
Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function def max_integer(list=[]):.

Your test file should be inside a folder tests
You have to use the unittest module
Your test file should be python files (extension: .py)
Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
All tests you make must be passable by the function below
We strongly encourage you to work together on test cases, so that you don’t miss any edge case

6. Matrix multiplication
#advanced
Write a function that multiplies 2 matrices:

Read: Matrix multiplication - only Matrix product (two matrices)

Prototype: def matrix_mul(m_a, m_b):

m_a and m_b must be validated with these requirements in this order

m_a and m_b must be an list of lists of integers or floats:

if m_a or m_b is not a list: raise a TypeError exception with the message m_a must be a list or m_b must be a list
if m_a or m_b is not a list of lists: raise a TypeError exception with the message m_a must be a list of lists or m_b must be a list of lists
if m_a or m_b is empty (it means: = [] or = [[]]): raise a ValueError exception with the message m_a can't be empty or m_b can't be empty
if one element of those list of lists is not an integer or a float: raise a TypeError exception with the message m_a should contain only integers or floats or m_b should contain only integers or floats
if m_a or m_b is not a rectangle (all ‘rows’ should be of the same size): raise a TypeError exception with the message each row of m_a must be of the same size or each row of m_b must be of the same size
If m_a and m_b can’t be multiplied: raise a ValueError exception with the message m_a and m_b can't be multiplied

You are not allowed to import any module

7. Lazy matrix multiplication
#advanced
Write a function that multiplies 2 matrices by using the module NumPy

To install it: pip3 install numpy==1.15.0

Prototype: def lazy_matrix_mul(m_a, m_b):
Test cases should be the same as 100-matrix_mul but with new exception type/message

8. CPython #3: Python Strings
#advanced


Create a function that prints Python strings.

Prototype: void print_python_string(PyObject *p);
Format: see example
If p is not a valid string, print an error message (see example)
Read: Unicode HOWTO
About:

Python version: 3.4
You are allowed to use the C standard library
Your shared library will be compiled with this command line: gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c

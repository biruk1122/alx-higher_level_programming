#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) not in ('q', 'e'):
        print("{}".format(chr(letter)), end="")

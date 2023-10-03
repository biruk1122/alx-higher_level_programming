#!/usr/bin/python3
for letter in range(ord('a'), ord('z')+1):
    if chr(letter) not in ('q', 'e'):
        print(chr(letter), end='')

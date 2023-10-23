#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    i = 0
    try:
        while printed_integers < x:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
            i += 1
    except IndexError:
        pass
    finally:
        print()  # Print a new line after the integers
    return printed_integers

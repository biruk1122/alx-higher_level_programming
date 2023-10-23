#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        num = fct(*args)
        return num
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None

#! /usr/bin/env python3

def print_hello(name: str):
    """Will print "Hello {name} !" for a given name.
    """
    print("Hello", name, "!")

if __name__ == '__main__':
    print_hello("Peter")
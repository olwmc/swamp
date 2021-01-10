#!/bin/python
import sys
from parser import *

stack = []
env = make_env()


# Check if evaluate
if "-e" in sys.argv:
    try:
        run_program(sys.argv[-1], stack, env)

    except:
        print("Invalid program")

# Else REPL
elif len(sys.argv) == 1:
    while(True):
        inp = input("[🐊]> ")
        run_program(inp, stack, env)

# Else run from file
else:
    run_program_from_file(sys.argv[-1], stack, env)


# """Debug""" mode
if "-d" in sys.argv:
    print("STACK: ", end="")
    print(stack)
    print(env)
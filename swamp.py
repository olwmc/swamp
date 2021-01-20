#!/bin/python
import sys
from parser import *

stack = []
env = make_env()

<<<<<<< HEAD
=======
# TODO: Fix this whole hacky situation later. This works for now
# but is totally unacceptable.

>>>>>>> 608b7882815de27a3211c7e81d4291997bcef486
# Check if evaluate
if "-e" in sys.argv:
    try:
        run_program(sys.argv[-1], stack, env)
    except:
        print("Invalid program")

# Else REPL
elif len(sys.argv) == 1:
    while(True):
        inp = input('\033[34m[🐊]\033[0m\033[31m>\033[0m ')
        run_program(inp, stack, env)

# Else run from file
else:
    run_program_from_file(sys.argv[-1], stack, env)


# """Debug""" mode
if "-d" in sys.argv:
    print("STACK: ", end="")
    print(stack)
    print(env)

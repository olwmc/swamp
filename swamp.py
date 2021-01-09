#!/bin/python
import sys
from parser import *

stack = []
env = make_env()

# Check if execute
if len(sys.argv) > 1 and sys.argv[1] == "-e":
    try:
        run_program(sys.argv[2], stack, env)

    except:
        print("Invalid program")

elif len(sys.argv) > 1:
    run_program_from_file(sys.argv[1], stack, env)

else:
    while(True):
        inp = input("[🐊]> ")
        run_program(inp, stack, env)
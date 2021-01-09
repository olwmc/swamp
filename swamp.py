#!/bin/python
import sys
from parser import *

stack = []
env = make_env()

if len(sys.argv) > 1:
    run_program_from_file(sys.argv[1], stack, env)

else:
    while(True):
        inp = input("[🐊]> ")
        run_program(inp, stack, env)
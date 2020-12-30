from parser import *
stack = []
env = make_env()

run_program_from_file("progs/recursion.fs", stack, env)
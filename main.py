from parser import *
stack = []
env = make_env()

run_program_from_file("progs/input.fs", stack, env)
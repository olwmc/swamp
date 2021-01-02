from parser import *
stack = []
env = make_env()

run_program_from_file("progs/begin-until.fs", stack, env)
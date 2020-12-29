from parser import *
stack = []
env = make_env()

program = """
variable beans 
10 alloc

10 0 do
        i
        i beans + !
    loop
"""
run_program(program, stack, env)
print(env)
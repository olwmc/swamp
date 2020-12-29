from lexer import *

def run_program(program, stack, env):
  tokens = tokenize(program)
  words = make_words(tokens)

  for word in words:
      word.execute(stack, env)

def run_program_from_file(file_name, stack, env):
  with open(file_name) as open_file:
    program = "\n".join(open_file.readlines())

  run_program(program, stack, env)

stack = []
env = make_env()

run_program_from_file("progs/fizzbuzz.fs", stack,env)

"""
To get allot, all you need to do is just add to the specified number of memory
"""
from lexer import *
import json

def run_program(program, stack, env):
  tokens = tokenize(program)
  words = make_words(tokens)

  for word in words:
      word.execute(stack, env)
      # Check graphics and change accordingly

fizzbuzz = """
: fizz?  3 mod 0 = dup if ." Fizz" then ;
: buzz?  5 mod 0 = dup if ." Buzz" then ;
: fizz-buzz?  dup fizz? swap buzz? or invert ;
: do-fizz-buzz  25 1 do cr i fizz-buzz? if i . then loop ;
do-fizz-buzz
"""

var_test = """
( Testing simple variable )
variable beans
123 beans !
beans @ . cr

( Testing additional variable to see if 
  it can do memory correctly )
variable court
567 court !
court @ . cr

 
: foo 0 10 0 do i + loop ;
foo
?
"""

const_test = """
( Testing constants )
34 constant beans
beans .
"""

stack = []
env = make_env()

run_program(var_test, stack, env)

"""
To get allot, all you need to do is just add to the specified number of memory
"""
from lexer import *

def run_program(program, stack, env):
  tokens = tokenize(program)
  words = make_words(tokens)

  for word in words:
      word.execute(stack, env)

fizzbuzz = """
: fizz?  3 mod 0 = dup if ." Fizz" then ;
: buzz?  5 mod 0 = dup if ." Buzz" then ;
: fizz-buzz?  dup fizz? swap buzz? or invert ;
: do-fizz-buzz  25 1 do cr i fizz-buzz? if i . then loop ;
do-fizz-buzz
"""

var_test = """
( Testing simple variable. Should print 576 )
variable beans
123 beans !
beans @ . cr

( Testing additional variable to see if 
  it can do memory correctly. Should print 777 )
variable court
777 court !
court @ . cr

( Function test. Should print 45 [0+1+2+3+4+5+6+7+8+9+10] )
: foo 0 10 1 do i + loop ;
foo . cr

( Testing constants. Should print 34 )
34 constant test_const
test_const . cr
"""

stack = []
env = make_env()

run_program(var_test, stack, env)

"""
To get allot, all you need to do is just add to the specified number of memory
"""